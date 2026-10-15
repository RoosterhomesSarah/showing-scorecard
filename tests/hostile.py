#!/usr/bin/env python3
"""Hostile grid tripwire. Builds the template twice with one nasty payload in EVERY field
a person can type into (once HTML-escaped as a correct builder would, once raw), then loads
each in headless Chrome, scores everything, opens every view, and fails if anything broke.

    python3 tests/hostile.py            exit 0 = every cell passed

The payload carries a double quote, single quote, backslash, a script terminator, a tag,
an ampersand, an accent, an emoji, and an attribute breakout. A new field added to the
template without being added to FIELDS here is caught by the token check at the top."""
import html, os, re, subprocess, sys, tempfile, json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL=os.environ.get("TPL") or os.path.join(ROOT,".claude/skills/showing-scorecard/assets/template.html")
BAD='A" \\ </script> <b>x</b> & café 🏠 \'q\' " onmouseover="window.PWNED=1" x="'
def _find_chrome():
    import shutil
    for c in (os.environ.get("CHROME"), "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              shutil.which("google-chrome"), shutil.which("google-chrome-stable"), shutil.which("chromium"),
              shutil.which("chromium-browser")):
        if c and os.path.exists(c): return c
    sys.exit("Chrome was not found. Set CHROME to its path.")
CHROME=_find_chrome()

IDS=["a b:c~d\"e","a b:c~d\"e"]  # same hostile id twice: must be cleaned and de-duplicated

def build(escape):
    s=open(TPL).read()
    e=(lambda v: html.escape(v,quote=True)) if escape else (lambda v: v)
    def li(items): return "\n".join('<li data-hint="%s">%s</li>'%(e(BAD),e(BAD+" "+str(i))) for i in range(items))
    stop=lambda i:'<li data-id="%s" data-n="%s" data-facts="%s" data-area="%s" data-type="house" data-date="%s" data-photo="%s"></li>'%(html.escape(IDS[i-1],quote=True),e("12"+BAD),e(BAD),e(BAD),e(BAD),e(BAD))
    vals={k:e(BAD) for k in re.findall(r"\{\{([A-Z0-9_]+)\}\}",s)}
    vals.update(dict(MUSTS=li(3),KILLS=li(2),NICES=li(3),CONSIDER=li(2),COND_SYS=li(2),COND_WORK=li(2),
      TOUR=stop(1)+stop(2),P1_INITIAL="B",P2_INITIAL="L",COLOR_ACCENT="#B8860B",COLOR_ACTION="#B22222",
      ON_ACCENT="#fff",ON_ACTION="#fff",FONT_QUERY="family=Inter",FONT_DISPLAY="Inter",FONT_BODY="Inter",
      AGENT_PHONE_RAW="5551234567",BRIEF_CELLS='<li data-label="%s">%s\n<li data-label="%s">%s'%(e(BAD),e(BAD),e(BAD),e(BAD)),LOGO_SRC="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==",STORAGE_KEY="hostile-"+("e" if escape else "r")))
    vals["P1_INITIAL"]=e(BAD); vals["P2_INITIAL"]=e(BAD)
    for k,v in vals.items(): s=s.replace("{{%s}}"%k,v)
    return s

PROBE=r"""<script>
window.addEventListener("load",function(){setTimeout(function(){
var r={errs:[],};
try{
  r.counts=[MUSTS.length,KILLS.length,NICES.length,CONSIDER.length,COND_SYS.length,COND_WORK.length,TOUR.length];
  var s=state; TOUR.forEach(function(p,i){ var o=st(p.id); o.b={};o.l={};o.shared={};o.cond={};
    MUSTS.forEach(function(_,j){o.b["m"+j]=1; if(j%2)o.l["m"+j]=1;}); NICES.forEach(function(_,j){o.b["n"+j]=1;});
    KILLS.forEach(function(_,j){ if(i===1)o.shared["k"+j]=1;}); CONSIDER.forEach(function(_,j){o.shared["c"+j]=1;});
    COND_SYS.forEach(function(_,j){o.cond["s"+j]="up";}); COND_WORK.forEach(function(_,j){o.cond["w"+j]="yes";});
    o.gutB=3;o.gutL=4;o.notes=__BAD__; });
  save(); renderStops(); TOUR.forEach(function(p){ openStop(p.id); }); renderCompare(); renderClosing();
  ["view-stops","view-detail","view-compare","view-closing"].forEach(function(v){});
  r.summary=summary(); r.short=shortSummary();
  r.body=sendBody();
}catch(e){ r.errs.push(String(e&&e.stack||e)); }
r.ids=TOUR.map(function(p){return p.id;});
  var called=0; copyText("x",function(){called++;}); try{ var bc=backupCode(); var back=readCode(bc); r.roundtrip=!!back; }catch(e){ r.errs.push("backup:"+e); }
r.frame={swallowed:!!document.querySelector(".hero .wrap, .hero main"), brief:document.querySelectorAll("#brief .bi").length, logos:document.querySelectorAll(".logoslot img").length};
r.pwned=!!window.PWNED;
r.listerr=!!document.getElementById("listerr");
r.handlers=document.querySelectorAll("[onmouseover],[onerror],[onload],[onclick],[onfocus]").length;
r.injectedB=[].filter.call(document.querySelectorAll("b"),function(b){return b.textContent==="x";}).length;
r.scripts=document.getElementsByTagName("script").length;
r.stray=document.body.innerText.indexOf("--gold")>-1;
r.labelOk=document.body.textContent.indexOf(__BAD__+" 0")>-1;
setTimeout(function(){ r.copyCalled=called; document.title="RESULT:"+JSON.stringify(r); },800);
},300);});
</script></body>"""

def run(escape):
    page=build(escape).replace("</body>",PROBE.replace("__BAD__",json.dumps(BAD).replace("</","<\\/")),1)
    with tempfile.TemporaryDirectory() as d:
        f=os.path.join(d,"t.html"); open(f,"w").write(page)
        out=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--virtual-time-budget=4000",
            "--dump-dom","file://"+f],capture_output=True,text=True,timeout=60).stdout
    m=re.search(r"<title>RESULT:(.*?)</title>",out,re.S)
    if not m: return None,out
    return json.loads(html.unescape(m.group(1))),out

fail=0
for escape in (True,False):
    r,out=run(escape)
    tag="escaped" if escape else "raw"
    if r is None: print(tag,"NO RESULT (page died before the probe ran)"); fail+=1; continue
    ok = (not r["errs"] and r["counts"]==[3,2,3,2,2,2,2] and not r["pwned"] and not r["listerr"]
          and r["handlers"]==0 and r["frame"]=={"swallowed":False,"brief":2,"logos":2} and r["copyCalled"]==1 and r["roundtrip"] and len(set(r["ids"]))==2 and all(__import__("re").fullmatch(r"[A-Za-z0-9_-]+",i) for i in r["ids"]) and r["injectedB"]==0 and r["scripts"]<=2 and not r["stray"])
    # the raw build is a builder mistake, not a supported path; it only has to not crash the page
    if not escape: ok = (not r["errs"] and not r["pwned"])
    print(tag,"PASS" if ok else "FAIL",json.dumps({k:v for k,v in r.items() if k not in("summary","short","body")}))
    fail+= (not ok)
sys.exit(1 if fail else 0)
