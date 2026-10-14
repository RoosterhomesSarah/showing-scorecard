"""Old scorecard -> rebuild with the new template -> does the buyer's progress survive?

    python3 tests/rebuild_old.py /path/to/a/client/folder/with/old/scorecards/

Loads each old scorecard in headless Chrome (so the OLD page's own code reads its lists), seeds
answers, then rebuilds with the current template and checks: same list counts, same stop ids,
same storage key, identical scores from the buyer's stored answers, an identical backup code,
and a backup code made by the OLD page restored by the NEW page. Needs no network."""
import html, json, re, subprocess, sys, tempfile, os
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL=os.path.join(ROOT,".claude/skills/showing-scorecard/assets/template.html")
OLD_DIR=(sys.argv[1] if len(sys.argv)>1 else sys.exit("give the folder holding the old scorecards")).rstrip("/")+"/"
SP=tempfile.mkdtemp()+"/"

def chrome(page,title_prefix):
    f=SP+"p.html"; open(f,"w").write(page)
    o=subprocess.run([CHROME,"--headless=new","--no-sandbox","--virtual-time-budget=4000","--dump-dom","file://"+f],
        capture_output=True,text=True,stdin=subprocess.DEVNULL,timeout=90).stdout
    m=re.search(r"<title>"+title_prefix+r"(.*?)</title>",o,re.S)
    return json.loads(html.unescape(m.group(1))) if m else None

EXPORT=r"""<script>addEventListener("load",function(){setTimeout(function(){
var R={};
try{
 R.lists={musts:MUSTS,kills:KILLS,nices:NICES,consider:CONSIDER,cond_sys:COND_SYS,cond_work:COND_WORK};
 R.brief=[].map.call(document.querySelectorAll(".brief .bi"),function(d){ return [d.querySelector("b")?d.querySelector("b").textContent:"", d.querySelector("span")?d.querySelector("span").textContent:""]; });
 R.tour=TOUR; R.key=KEY; R.p=[P.b.name,P.b.initial,P.l.name,P.l.initial]; R.solo=(typeof SOLO!=="undefined"?SOLO:false); R.agent=(typeof AGENT!=="undefined"?AGENT:"");
 // seed answers the way a buyer would have, against the OLD page
 TOUR.forEach(function(p,i){ var o=st(p.id);
   MUSTS.forEach(function(_,j){ if((i+j)%2===0) o.b["m"+j]=1; if(j%3===0) o.l["m"+j]=1; });
   NICES.forEach(function(_,j){ if((i+j)%3===0) o.b["n"+j]=1; });
   CONSIDER.forEach(function(_,j){ if(j%2===0) o.shared["c"+j]=1; });
   if(i===1) KILLS.forEach(function(_,j){ if(j===0) o.shared["k0"]=1; });
   COND_SYS.forEach(function(_,j){ o.cond["s"+j]=["up","orig","issue","ask"][(i+j)%4]; });
   COND_WORK.forEach(function(_,j){ o.cond["w"+j]=["yes","part","no","ask"][(i+j)%4]; });
   o.gutB=(i%5)+1; o.gutL=((i+2)%5)+1; o.notes="note "+i+" \"q\" & <b>";
   if(i===TOUR.length-1) o.skipped=true; });
 save(); renderStops();
 R.state=JSON.parse(JSON.stringify(state));
 R.scores=TOUR.map(function(p){ var s=score(p); return [p.id,s.b.pct,s.l.pct,s.killed.length,s.split.length,s.b.missed.length]; });
 R.code=backupCode(); R.summary=summary();
}catch(e){ R.err=String(e&&e.stack||e); }
document.title="OLD:"+JSON.stringify(R);
},400);});</script></body>"""

CHECK=r"""<script>addEventListener("load",function(){setTimeout(function(){
var R={}; var S=__STATE__, CODE=__CODE__;
try{
 R.briefAfter=[].map.call(document.querySelectorAll("#brief .bi"),function(d){ return [d.querySelector("b").textContent,d.querySelector("span").textContent]; });
 R.counts=[MUSTS.length,KILLS.length,NICES.length,CONSIDER.length,COND_SYS.length,COND_WORK.length,TOUR.length];
 R.key=KEY; R.ids=TOUR.map(function(p){return p.id;}); R.listerr=!!document.getElementById("listerr");
 // 1) the stored state the buyer already has, read by the NEW page
 state=S; save(); renderStops(); renderCompare();
 R.scores=TOUR.map(function(p){ var s=score(p); return [p.id,s.b.pct,s.l.pct,s.killed.length,s.split.length,s.b.missed.length]; });
 R.code=backupCode(); R.summary=summary();
 // 2) a backup code the OLD page produced, restored by the NEW page
 var res=readCode(CODE); R.restore= res.err ? {err:res.err} : {houses:res.houses,known:res.known};
}catch(e){ R.err=String(e&&e.stack||e); }
document.title="NEW:"+JSON.stringify(R);
},400);});</script></body>"""

def li_list(items):
    out=[]
    for lab,hint in items:
        out.append('<li%s>%s</li>'%((' data-hint="%s"'%html.escape(hint,quote=True)) if hint else '', html.escape(lab,quote=True)))
    return "\n".join(out)
def li_tour(tour):
    out=[]
    for p in tour:
        # the old facts string was written as HTML ("&middot;"); the new attribute holds the decoded text
        attrs=" ".join('data-%s="%s"'%(k,html.escape(html.unescape(str(p[k])),quote=True)) for k in ("id","n","facts","area","type","date","photo") if p.get(k) not in (None,""))
        out.append("<li %s></li>"%attrs)
    return "\n".join(out)

def rebuild(old):
    s=open(TPL).read()
    e=lambda v: html.escape(v,quote=True)
    vals={k:"x" for k in re.findall(r"\{\{([A-Z0-9_]+)\}\}",s)}
    vals.update(dict(MUSTS=li_list(old["lists"]["musts"]),KILLS=li_list(old["lists"]["kills"]),NICES=li_list(old["lists"]["nices"]),
      CONSIDER=li_list(old["lists"]["consider"]),COND_SYS=li_list(old["lists"]["cond_sys"]),COND_WORK=li_list(old["lists"]["cond_work"]),
      TOUR=li_tour(old["tour"]),STORAGE_KEY=e(old["key"]),P1_NAME=e(old["p"][0]),P1_INITIAL=e(old["p"][1]),P2_NAME=e(old["p"][2]),P2_INITIAL=e(old["p"][3]),
      AGENT_FIRST_NAME=e(old["agent"] or "Agent"),DEFAULT_LANG="",COLOR_ACCENT="#8A6A3B",COLOR_ACTION="#1F4E5F",ON_ACCENT="#fff",ON_ACTION="#fff",
      FONT_QUERY="family=Inter",FONT_DISPLAY="Inter",FONT_BODY="Inter",AGENT_PHONE_RAW="5550100",BRIEF_CELLS="\n".join("<li data-label=\"%s\">%s</li>"%(e(l),e(v)) for v,l in old.get("brief",[])),LOGO_SRC=""))
    for k,v in vals.items(): s=s.replace("{{%s}}"%k,v)
    return s

fail=0
for name in sorted(f for f in os.listdir(OLD_DIR) if f.endswith(".html")):
    old_html=open(OLD_DIR+name).read()
    old=chrome(old_html.replace("</body>",EXPORT,1),"OLD:")
    if not old or "err" in old: print(name,"OLD PAGE FAILED",(old or {}).get("err")); fail+=1; continue
    new_html=rebuild(old)
    chk=CHECK.replace("__STATE__",json.dumps(old["state"]).replace("</","<\\/")).replace("__CODE__",json.dumps(old["code"]).replace("</","<\\/"))
    new=chrome(new_html.replace("</body>",chk,1),"NEW:")
    probs=[]
    if not new or "err" in new: probs.append("NEW PAGE FAILED: %s"%((new or {}).get("err")))
    else:
        want=[len(old["lists"][k]) for k in ("musts","kills","nices","consider","cond_sys","cond_work")]+[len(old["tour"])]
        if new["counts"]!=want: probs.append("counts %s != %s"%(new["counts"],want))
        if new["key"]!=old["key"]: probs.append("storage key changed %r -> %r"%(old["key"],new["key"]))
        if new["ids"]!=[p["id"] for p in old["tour"]]: probs.append("stop ids changed %s -> %s"%([p["id"] for p in old["tour"]],new["ids"]))
        if new.get("briefAfter")!=old.get("brief"): probs.append("header strip changed or lost: %s -> %s"%(old.get("brief"),new.get("briefAfter")))
        if new["listerr"]: probs.append("list error banner")
        if new["scores"]!=old["scores"]: probs.append("SCORES DIFFER\n   old %s\n   new %s"%(old["scores"],new["scores"]))
        if new["code"]!=old["code"]: probs.append("backup code differs (old %s... new %s...)"%(old["code"][:40],new["code"][:40]))
        if "err" in new.get("restore",{}): probs.append("old backup code refused by new page: %s"%new["restore"]["err"])
        elif new["restore"]["known"]!=new["restore"]["houses"]: probs.append("restore held houses it cannot show: %s"%new["restore"])
        # the first two lines are the title and the agent's own subhead, which a rebuild rewrites
        norm=lambda t:[l for l in t.splitlines()[2:] if "Agreed on everything" not in l and l.strip()!=""]
        if norm(new["summary"])!=norm(old["summary"]):
            a,b=norm(old["summary"]),norm(new["summary"])
            probs.append("summary text differs: %r"%[(x,y) for x,y in zip(a,b) if x!=y][:2])
    print(name,"PASS" if not probs else "FAIL", "| old format lists in:", "script" if "var MUSTS=[" in old_html else "html")
    for p in probs: print("   ",p)
    fail+=bool(probs)
sys.exit(1 if fail else 0)
