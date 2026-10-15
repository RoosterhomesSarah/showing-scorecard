#!/usr/bin/env python3
"""Spanish tripwire. Builds the template with ES_COMPLETE forced on and every agent-supplied
word set to nonsense (so any real English on screen is the template's, not the agent's),
then for a couple AND a single buyer:

  1. opens every view in Spanish (stops, one stop's detail, compare, the restore box, the
     closing decision, a skipped stop) and fails on any visible English,
  2. switches back to English and fails unless every view reads exactly as it did before
     the first switch (so Spanish never leaves residue),
  3. fails if a key in the English table has no Spanish twin.

    python3 tests/spanish.py            exit 0 = clean

Visible English is detected by common English function words, so a leaked sentence is
caught even when it is short. A word that is a real word in both languages (no, sin) is
not on the list."""
import html, json, os, re, subprocess, sys, tempfile
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL=os.environ.get("TPL") or os.path.join(ROOT,".claude/skills/showing-scorecard/assets/template.html")
def _find_chrome():
    import shutil
    for c in (os.environ.get("CHROME"), "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              shutil.which("google-chrome"), shutil.which("google-chrome-stable"), shutil.which("chromium"),
              shutil.which("chromium-browser")):
        if c and os.path.exists(c): return c
    sys.exit("Chrome was not found. Set CHROME to its path.")
CHROME=_find_chrome()
EN_WORDS=set("""the you your and is are to of this that for with it not one scored home homes stop stops
must have haves nice tap taps phone nothing nobody agree agreed everything missing deal breakers
breaker saved copy copied restore code ask send text email score points each from before after
which where when what they their them we our us into out on at an be been was were will would
should can could has had do does did if but or so than then there these those all any some more
most other only own same too very just also how about over under again further once here why
because while during between through until against both few such no_ nor""".split())
EN_WORDS-= {"no_"}

def build(solo,es_note="Zxq"):
    s=open(TPL).read()
    s=s.replace("var ES_COMPLETE = false;","var ES_COMPLETE = true;")
    def li(n,pre): return "\n".join('<li data-hint="h%s%d">%s%d</li>'%(pre,i,pre,i) for i in range(n))
    stops="\n".join('<li data-id="s%d" data-n="%d Zorro Calle" data-facts="Zxq" data-area="Zxq" data-type="house" data-date="d1"></li>'%(i,100+i) for i in (1,2,3))
    vals={k:"Zxq" for k in re.findall(r"\{\{([A-Z0-9_]+)\}\}",s)}
    vals.update(dict(MUSTS=li(3,"mm"),KILLS=li(2,"kk"),NICES=li(3,"nn"),CONSIDER=li(2,"cc"),COND_SYS=li(2,"ss"),
      COND_WORK=li(2,"ww"),TOUR=stops,P1_NAME="Alfa",P1_INITIAL="A",P2_NAME="" if solo else "Beta",P2_INITIAL="" if solo else "B",
      COLOR_ACCENT="#B8860B",COLOR_ACTION="#B22222",ON_ACCENT="#fff",ON_ACTION="#fff",FONT_QUERY="family=Inter",
      FONT_DISPLAY="Inter",FONT_BODY="Inter",AGENT_FIRST_NAME="Zorro",AGENT_PHONE_RAW="5551234567",AGENT_PHONE="555",
      AGENT_SEND_EMAIL="z@z.zz",DEFAULT_LANG=("" if solo else "es"),ES_NOTE=es_note,BRIEF_CELLS='<li data-label="Zxq">Zxq\n<li data-label="Zxq">Zxq',LOGO_SRC="",STORAGE_KEY="spanish-test-"+("s" if solo else "c")))
    for k,v in vals.items(): s=s.replace("{{%s}}"%k,v)
    return s

PROBE=r"""<script>
addEventListener("load",function(){setTimeout(function(){
var R={missing:[],views:{}}; R.initialLang=LANG;
function snap(name){
  var out={};
  show("stops"); out.stops=document.body.innerText;
  var first=TOUR[0].id; openStop(first); out.detail=document.body.innerText;
  show("compare"); out.compare=document.body.innerText;
  document.getElementById("showrestore").click(); out.restore=document.body.innerText;
  document.getElementById("showrestore").click();
  R.views[name]=out;
}
function restoreScored(){ TOUR.forEach(function(p){ var o=st(p.id); o.b["m0"]=1; o.l["m0"]=1; }); save(); }
try{
  var k; for(k in STRINGS.en){ if(STRINGS.en.hasOwnProperty(k) && STRINGS.es[k]==null && STRINGS.es[k+"_1"]==null) R.missing.push(k); }
  TOUR.forEach(function(p,i){ var o=st(p.id);
    MUSTS.forEach(function(_,j){ if(j<2) o.b["m"+j]=1; if(j===0) o.l["m"+j]=1; });
    NICES.forEach(function(_,j){ o.b["n"+j]=1; });
    CONSIDER.forEach(function(_,j){ o.shared["c"+j]=1; });
    if(i===1) KILLS.forEach(function(_,j){ o.shared["k"+j]=1; });
    COND_SYS.forEach(function(_,j){ o.cond["s"+j]=["up","orig","issue","ask"][j%4]; });
    COND_WORK.forEach(function(_,j){ o.cond["w"+j]=["yes","part"][j%2]; });
    o.gutB=3;o.gutL=4;o.notes="nota"; if(i===2) o.skipped=true; });
  save(); renderStops(); renderCompare(); renderClosing();
  document.getElementById("closing").hidden=false;
  document.querySelectorAll(".closebtn")[0].click();
  setLang("en"); snap("en1");
  setLang("es"); snap("es");
  setLang("en"); snap("en2");
  setLang("es");
  // press the buttons that write messages, in Spanish, and read what they said
  R.actions={}; var ids=["send","copy","reset","copycode","dorestore","showrestore","sendhint","restoremsg","sendempty","closehint"];
  function grab(tag){ var o=[]; ids.forEach(function(i){ var e=document.getElementById(i); if(e&&!e.hidden) o.push((e.innerText||"").trim()); }); R.actions[tag]=o.join("\n"); }
  show("compare");
  document.getElementById("send").click(); document.getElementById("copy").click();
  document.getElementById("reset").click(); grab("clicked");
  document.getElementById("showrestore").click();
  var good=backupCode(); var ta=document.getElementById("restorein");
  ta.value="garbage"; document.getElementById("dorestore").click(); grab("badcode");
  ta.value="RH1.zzzz.a:0:0:0:0:-:-:00:0:"; document.getElementById("dorestore").click(); grab("oldcode");
  ta.value=good.slice(0,good.length-12); document.getElementById("dorestore").click(); grab("cutcode");
  ta.value=good; document.getElementById("dorestore").click(); grab("replacewarn");
  document.getElementById("dorestore").click(); grab("restored");
  document.getElementById("copycode").click(); grab("copycode");
  state={}; save(); document.getElementById("send").click(); grab("emptysend");
  // messages and armed labels written in Spanish must turn English when the language does
  var go=function(){};
  R.pending=true;
  restoreScored(); R.summaryText=summary();
  DECISION="offer"; try{ localStorage.setItem(KEY+"-decision","offer"); }catch(e){}
  R.sumHasDec=summary().indexOf("WHERE WE LANDED")>-1; R.shortHasDec=shortSummary().indexOf("WHERE WE LANDED")>-1;
  (function(){ var c=document.getElementById("closing"), g=document.getElementById("gridbox"), b=document.getElementById("sendsms");
    R.order=[!!(g.compareDocumentPosition(c)&4), !!(c.compareDocumentPosition(b)&4)]; })();

  document.getElementById("send").click();
  document.getElementById("showrestore").click(); if(document.getElementById("restorewrap").hidden) document.getElementById("showrestore").click();
  document.getElementById("restorein").value="garbage"; document.getElementById("dorestore").click();
  document.getElementById("reset").click();
  setTimeout(function(){
    document.getElementById("reset").click();
    R.decisionAfterClear=[DECISION, (function(){try{return localStorage.getItem(KEY+"-decision")||"";}catch(e){return "?";}})()].join("|");
    setLang("en");
    R.afterSwitch=["sendhint","restoremsg","showrestore","reset","dorestore"].map(function(i){ var e=document.getElementById(i); return e&&!e.hidden?(e.innerText||"").trim():""; }).join("\n");
    document.title="RESULT:"+JSON.stringify(R);
  },500);
}catch(e){ R.err=String(e&&e.stack||e); }
if(!R.pending) document.title="RESULT:"+JSON.stringify(R);
},400);});
</script></body>"""

def run(solo):
    page=build(solo).replace("</body>",PROBE,1)
    with tempfile.TemporaryDirectory() as d:
        f=os.path.join(d,"t.html"); open(f,"w").write(page)
        out=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--virtual-time-budget=5000",
            "--dump-dom","file://"+f],capture_output=True,text=True,timeout=90).stdout
    m=re.search(r"<title>RESULT:(.*?)</title>",out,re.S)
    return json.loads(html.unescape(m.group(1))) if m else None

def english_lines(text):
    bad=[]
    for line in text.splitlines():
        words=re.findall(r"[A-Za-zÀ-ÿ']+",line.lower())
        hits=[w for w in words if w in EN_WORDS]
        if hits and len(words)>=1 and not re.fullmatch(r"[a-z0-9 ]*",line.lower()) is None and False: pass
        if hits: bad.append((line.strip()[:110],hits[:4]))
    return bad

NOTE_PROBE=r"""<script>addEventListener("load",function(){setTimeout(function(){
var R={}; try{ setLang("es"); var n=document.getElementById("escorrect"); R.es=!n.hidden; R.text=n.innerText; setLang("en"); R.en=!n.hidden; }catch(e){R.err=String(e)}
document.title="RESULT:"+JSON.stringify(R);},300);});</script></body>"""
def note_case(value):
    page=build(False,value).replace("</body>",NOTE_PROBE,1)
    with tempfile.TemporaryDirectory() as d:
        f=os.path.join(d,"t.html"); open(f,"w").write(page)
        out=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--virtual-time-budget=3000","--dump-dom","file://"+f],capture_output=True,text=True,timeout=60).stdout
    m=re.search(r"<title>RESULT:(.*?)</title>",out,re.S)
    return json.loads(html.unescape(m.group(1))) if m else None

fail=0
# the "translated with a tool" line: hidden only by an explicit off, never in English
for value,shown in (("off",False),("OFF",False),(" off ",False),("on",True),("",True),("{{ES_NOTE}}",True),("Zxq",True)):
    r=note_case(value)
    ok = r and "err" not in r and r["es"]==shown and r["en"] is False
    print("ES_NOTE=%r"%value, "PASS" if ok else "FAIL %s"%r); fail+=not ok
# a couple is ustedes all the way through the line; one buyer is usted
src=open(TPL).read()
m1=re.search(r'esCorrect: "([^"]*)"',src); m2=re.search(r'esCorrect_1: "([^"]*)"',src)
g=(m1 and "lo notan" in m1.group(1) and "díganselo" in m1.group(1) and "lo nota," not in m1.group(1)) and (m2 and "lo nota," in m2.group(1) and "dígaselo" in m2.group(1))
print("correction line grammar (couple notan/díganselo, one buyer nota/dígaselo)","PASS" if g else "FAIL"); fail+=not g
for solo in (False,True):
    tag="solo" if solo else "couple"
    r=run(solo)
    if r is None or "err" in r:
        print(tag,"NO RESULT / ERROR",(r or {}).get("err")); fail+=1; continue
    problems=[]
    if r["missing"]: problems.append("keys with no Spanish twin: "+", ".join(r["missing"][:12]))
    for view,text in r["views"]["es"].items():
        for line,hits in english_lines(text):
            problems.append("English in %s: %r %s"%(view,line,hits))
    for view in r["views"]["en1"]:
        if r["views"]["en1"][view]!=r["views"]["en2"][view]:
            a,b=r["views"]["en1"][view].splitlines(),r["views"]["en2"][view].splitlines()
            diff=[(x,y) for x,y in zip(a,b) if x!=y][:2]
            problems.append("English changed after a round trip in %s: %r"%(view,diff))
    ALLOW={"original","no","waze","apple maps","es","en","a","b","—"}
    AGENT=re.compile(r"^(mm|nn|kk|cc|ss|ww|h(mm|nn|kk|cc|ss|ww))\d|zxq|zorro|alfa|beta|z@z|calle|^[\d%/ .:·—-]*$|^[a-z]$",re.I)
    for view,text in r["views"]["es"].items():
        en_lines=set(l.strip().lower() for l in r["views"]["en1"][view].splitlines())
        for l in text.splitlines():
            k=l.strip().lower()
            if len(re.findall(r"[a-zà-ÿ]",k))>=3 and k in en_lines and k not in ALLOW and not AGENT.search(k):
                problems.append("Same as English in %s: %r"%(view,l.strip()[:80]))
    if re.search(r"[áéíóúñ¿¡]|ahora|código|péguen|restaur|cancelar|toquen",r.get("afterSwitch",""),re.I):
        problems.append("Spanish left behind after switching to English: %r"%r["afterSwitch"][:200])
    for name,text in (r.get("actions") or {}).items():
        for line,hits in english_lines(text): problems.append("English after pressing buttons (%s): %r %s"%(name,line,hits))
    want="es" if not solo else "en"
    if r.get("initialLang")!=want: problems.append("opened in %r, expected %r (DEFAULT_LANG %s)"%(r.get("initialLang"),want,"es" if not solo else "empty, phone is en"))
    if r.get("decisionAfterClear")!="|": problems.append("Clear this tour left the decision behind: %r"%r.get("decisionAfterClear"))
    if "Agreed on everything" in r.get("summaryText","") and (solo or "Nobody scored" in r.get("summaryText","")): problems.append("summary claims agreement with no basis")
    if not (r.get("sumHasDec") and r.get("shortHasDec")): problems.append("the decision is missing from a report to the agent")
    if r.get("order")!=[True,True]: problems.append("'What happens next' is not between the grid and the send buttons: %s"%r.get("order"))
    if "traducida" not in r["views"]["es"]["stops"]: problems.append("the correction line is missing from the Spanish view")
    if "traducida" in r["views"]["en1"]["stops"] or "translated into Spanish" in r["views"]["en1"]["stops"]: problems.append("the correction line shows in English")
    if r["views"]["es"]["stops"]==r["views"]["en1"]["stops"]: problems.append("Spanish identical to English (toggle did nothing)")
    print(tag,"PASS" if not problems else "FAIL")
    for p in problems[:25]: print("   ",p)
    fail+=bool(problems)
sys.exit(1 if fail else 0)
