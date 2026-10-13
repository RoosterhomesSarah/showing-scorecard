# Verification log

## Slice: the public skill repo, v1.0

**Working means:** an agent who has never seen this installs it, answers seven questions
once, and gets a branded phone scorecard built from one buyer's own stated criteria,
with nothing in it that could cost them their license.

**Consumers:** the installing agent reading SKILL.md; Claude Code loading the skill; the
buyer on a phone in light mode and in dark mode; the buyer on an older iPhone without
`color-mix`; the agent reading the copied summary as plain text; a stranger reading the
README on github.com; and a lawyer reading the scored criteria after a complaint.

**Ran the real thing, per consumer:** the template was filled and served over HTTP and
driven in a real browser for four configurations (solo buyer, two buyers, near-black
accent, pale accent), in both light and dark. Scoring, deal-breakers, disagreements, the
condition section, both exports and the empty states were exercised through the page's
own functions, not by reading the source.

**Real path or stand-in:** REAL for everything except the one-line installer. `npx
skills add` requires Node 22 and this machine is on 20, so **whether that command copies
`assets/template.html` alongside SKILL.md is UNTESTED.** The skill is inert without the
template. Logged as an open risk; the clone install path is documented and does work.

**Design pass:** computed styles verified in-browser, not read off the CSS. Fonts render
as the named faces rather than falling back. Contrast measured at both accent extremes
in both themes, worst surviving value 4.4:1. Empty states written for an empty tour and
an unscored property. Checked at phone width.

**Tripwire:** none automated. There is no build step to hang a guard on. The risk lives
in anyone editing `MUST`, `NICE` or the list lengths without re-reading the invariant,
and in anyone editing the condition prompts back toward market-specific claims. Both are
called out in SKILL.md at the point of edit. Logged as a real gap.

### Break attempts

1. **Solo buyer** (P2 empty). Before: 12 phantom disagreements with a person who does not
   exist, "Pat counted it, ______ didn't" in the panel, and an export telling the agent
   the buyer disagreed with themselves about everything. After: `SOLO=true`, splits 0,
   one score, one tap column, no initials, disagreement panel hidden, export reads
   "Showing scorecard - Pat".
2. **Two buyers, after the solo work.** Regression check. Both columns, real initials
   P/J rather than the hardcoded B/L, disagreement panel back, both gut rows,
   "Pat 87% Jo 52%", "Jo missing: Parking included; 3 bedrooms".
3. **Near-black accent `#1A1A1A`**, which SKILL.md itself used to recommend. Before:
   hero text 1.06:1 on the dark band, invisible. After: 6.18:1.
4. **Pale yellow accent `#F2C94C` with a pale action.** Before: section heading 1.59:1,
   group heading 1.39:1, primary button label 1.84:1. After: 4.9, 4.9 and 12.52. The
   deal-breaker heading was found failing at 1.39 during this pass and fixed separately.
5. **Empty tour.** Before: empty containers, and `POSS` of 0 giving `NaN%` on the card.
   After: a sentence telling the buyer to ask their agent to add addresses, and `POSS`
   floored at 1.
6. **localStorage blocked.** Both read and write swallow the exception, so every tap
   looked saved and a reload wiped the tour silently, under a page promising the answers
   were kept. After: probed on load, and a visible warning.
7. **A corrupt stored value.** `load()` returned whatever `JSON.parse` gave it. A stored
   `"null"` or a number would throw on first render and kill the page. Now type-checked.
8. **Ranking against the gate.** Before: a home missing a must-have ranked above one
   meeting all of them, because the sort read only the percentage. After: the gate is
   first in the sort.

### Two-weeks-later audit would flag

The invariant that one must-have outweighs every nice-to-have combined holds at the
shipped weights, but it depends on list **length**, not only the weights. At 25 points it
breaks somewhere past six nice-to-haves. A chatty consultation will produce more than
that. SKILL.md warns about changing the weights and says nothing about adding items.
**Open.**

### Fresh-eyes review

An independent reviewer with no build context, told to assume it was broken. Returned 17
findings plus cosmetics. Two categories came back clean: token coverage, and the absence
of client data or the originating kit's architecture apart from one README section.

All 17 are now closed. The two that mattered most:

- **No fair housing filter existed, and the skill instructed the opposite.** "Transcribe
  their must-haves exactly as written" plus an open question about the area is a machine
  for printing protected-class proxies onto a branded, scored, emailed document. Three
  shipped starter-set lines were themselves problems, one of them textbook steering.
  Fixed against HUD and the C.A.R. advisory, and reframed: done right, this is the
  advisory's own first example of a positive practice.
- **The page told the buyer a must-have was worth 10 while the engine scored it 25**,
  which also made the sentence directly below it false.

### Must-fix

All closed.

### Nice-to-have, logged and not done

ARIA tablist is incomplete, no `aria-controls` and no arrow keys. `p.facts` goes in
through innerHTML unescaped, author-controlled so low risk. No automated guard on the
scoring invariant. The `npx` install path is unverified above.

**Status: DONE** for the repo as it stands locally. **NOT PUBLISHED.** Publishing waits
on Sarah reading the fair housing section, since she holds the license and the wording
in it is hers to correct.

---

## Slice: the property tile, v1.1

**Working means:** a stop looks finished with nobody having supplied a photograph, each
stop is distinguishable at a glance, and anyone who wants a real picture on one can add
it from their phone in two taps.

**Consumers:** the buyer on a phone in light and dark mode; the agent on a laptop; an
agent whose brand color is nearly black, and one whose brand color is pale; a buyer
whose phone storage is full; the print stylesheet; the plain-text summary the agent
receives.

**Ran the real thing, per consumer:** served over HTTP and driven in a real browser. The
upload went through the real `attachPhoto` with real `File` objects built in the page, not
a stub: an 84KB 1600x1200 JPEG stored at 4KB and 420x315, and a 6000x4000 image resized
without error. Contrast was measured against the tile gradient's own computed color
stops, not against the card behind it.

**Real path or stand-in:** REAL except the operating system's file picker, which cannot be
opened from automation. Everything after the picker hands over a file is the shipped path.
**Whether the picker opens the camera on a real iPhone is UNTESTED** and rests on
`accept="image/*"`.

**Design pass:** Playfair Display confirmed rendering as itself rather than falling back.
Number 13.43:1 light and 12.25:1 dark. Street suffix 7.06:1 and 7.05:1. Frame and pediment
4.29:1 at the pale accent. Checked at phone and laptop width in both themes and at both
accent extremes.

**Tripwire:** none automated, same gap as v1.0. The contrast and the duplicate-token
failure below are both the kind a build-time check could hold, and there is still no build
step to hang one on. Logged.

### Break attempts

1. **A pale brand color.** The frame and the pediment measured **1.39:1** against the
   tile ground, which is invisible. Every agent with a light brand color would have got a
   bare number in an empty box. Both now draw in the darkened derivative: 4.29:1.
2. **The street suffix against the darker end of the gradient.** 4.19:1, under the 4.5
   minimum for small text. Measured against the card surface it had looked like 4.79 and
   passed, which is why it survived the first pass. Now on `--ink2` at 7.06:1.
3. **One tap on the camera fired the handler twice.** The file input was a child of the
   button, so its own click bubbled back in. On a phone that is the confirm dialog
   appearing twice. The input is now a sibling. One tap, one handler, one dialog.
4. **A PDF, and a corrupt file claiming to be a JPEG.** Both refused with a plain
   sentence. Nothing written, nothing rendered.
5. **A full phone.** Forced the write to fail and confirmed the rollback: the message
   names the real problem, nothing is kept in memory, nothing reaches storage, and the
   photos already on other stops survive.
6. **A photo on a short card.** The image sat at its natural ratio with white bands above
   and below it. Now absolutely positioned, filling the tile at any card height.
7. **Deal-breakers, which v1.0 never exercised** because the demo buyer had none. A house
   scoring 87% with one tripped now ranks below a house at 23% with none, shows as out,
   gets the dead card, and names the reason in the summary.

### The defect underneath two of the others

The template's header comment documented every token **by writing the token literally**.
Any build that replaced `{{TOUR}}` filled it twice: once in the real array and once inside
the comment. Every scorecard ever built carried a second copy of every list, the whole
tour and the logo, and the published example shipped with it. It also meant a file that
read itself back got the wrong array, which is what corrupted the demo client and what I
had wrongly blamed on the generator.

The class is "the documentation of a thing is itself an instance of the thing." The fix
removes the class rather than the instance: the header now names each token **without**
braces, so there is nothing for a replace to match whether or not anyone strips the
comment first. SKILL.md says why, at the point where someone would be tempted to put them
back.

### Also found and fixed

- The page still told the buyer a must-have was worth 25 after the weight was made
  derived. Same sentence, third time. It now states the rule rather than a number, which
  stays true at any list length.
- The published example had the previous buyer's name in its deal-breaker note.
- Two group containers rendered `class="grpundefined"`.
- Five British spellings, two of them introduced in this slice.

### Nice-to-have, logged and not done

A client's photo lives in that phone's storage and never reaches the agent's copy. That is
true of every answer on the page and is documented, not solved. The camera icon measures
4.39:1 in dark mode, which clears the 3:1 bar for a graphical control but not the text
bar. The hero band and the Compare table are still the plainest parts of the page.

**Status: DONE** for this slice.

---

## Slice: the frame is the building, v1.2

**Working means:** a buyer can tell a single family from a condo by the shape of the mark,
before reading anything, and both still read as one family of marks rather than two
unrelated drawings.

**Ran the real thing:** served over HTTP, driven in a real browser, both themes, both
accent extremes, phone and laptop width.

**Design pass:** the two elevations share the same walls and the same overhanging eave and
differ only at the roof, pitched for a house and flat with a parapet for anything stacked.
Frame 7:1 light, 5.96:1 dark, 4.29:1 at a pale accent. Number 13.43 and 12.25. Suffix 7.06
and 7.05. Playfair confirmed rendering as itself.

### Break attempts

1. **Two earlier shapes were rejected by looking at them, not by measuring.** A standalone
   pentagon with no eave overhang read as a tent; a projecting cornice over a narrower body
   read as a coat hanger. The overhanging eave is the detail that makes it a building.
2. **A long house number.** Five and six digits overflowed the wall at a fixed size. The
   number now steps down by digit count: 41px wide in a 62px wall at four digits, 48px at
   six.
3. **A long street suffix.** "Parkway", "Highway" and an address with no leading number at
   all ("Corner of Vine and Fountain", which falls back to the stop index). Widest was 48px
   in a 62px wall. No overflow.
4. **The word an agent would actually write.** The field was documented `"house"|"tower"`,
   and nobody types "tower". `condo`, `apartment`, `loft`, `high-rise`, `co-op`, `unit`,
   `townhouse`, `bungalow` and `duplex` now resolve, case and whitespace insensitive, and
   an unrecognized word draws the house rather than nothing.

**Status: DONE** for this slice.

---

## Slice: Compare, v1.3

**Working means:** a buyer sitting in the car after four houses can tell which one is
still in it and why, without reading a table, and can then look at every line for every
home if they want to.

**Ran the real thing:** served over HTTP, driven in a real browser, both themes, phone and
laptop, solo and two buyers, with deal-breakers tripped and disagreements created through
the page's own controls.

**Design:** the six column table was unreadable on a phone, so the cards replace it and
the grid sits under them. The cards group rather than rank, because the buyer's question
is which one, not what is the order: still in the running, short on something you needed,
out, not scored yet. The grid's criterion column is pinned, verified by scrolling it and
re-measuring the label's position.

### Break attempts

1. **A criterion pushed into a sentence.** "Riley has Plenty of natural light, A garage,
   In Los Feliz." The criteria are noun phrases a buyer wrote and they will never sit
   inside a sentence. They are listed now, under a line that carries the grammar.
2. **Counts that disagree with their own sentence.** "You two scored 1 thing differently.
   They are listed below." Numbers under eleven are words now and the verb agrees.
3. **Solo mode.** No partner named anywhere in the cards, no split chips in the grid, a
   single percentage per column, and the legend reads for one person.
4. **A grid of one home**, which is not a comparison. Hidden under two scored homes, and
   on an empty tour.
5. **The group subhead spoke about the buyer in the third person** on a page that speaks
   to them.
6. **Print.** The grid's sticky columns and its sideways scroll both break on paper.
   Position is static, overflow visible, rows do not split across pages, and the
   deal-breaker mark becomes a ring so it survives greyscale.

### The defect underneath the contrast work

`--ink2` and `--ink3` were never defined. `--ink3` was in the shipped template before this
slice; I then used `--ink2` six times, including for the tile's street suffix in v1.1,
which I "verified" at 7.06:1. That number was real but accidental: an undefined custom
property makes the declaration invalid at computed-value time, so the element silently
inherited its parent's color. The measurement was true and meaningless, because it was not
measuring the token I thought I had set.

The tell was two different tokens probing to the identical value, which I saw in v1.1 and
read past. Both now point at `--body`, which is defined in both themes, and a check for
`var(--x)` with no matching `--x:` found nothing else. Measured after: every small label in
the grid is 8.06:1 light and 8.49:1 dark, the row labels 15.34 and 14.74.

**Status: DONE** for this slice. The grid is new surface and has not been seen by anyone
but me.

---

## Slice: the backup code, the one-phone rule, and the delivery section, v1.4

**Working means:** a buyer whose phone is wiped in week six gets every home back, and the
agent does nothing to make that true beyond keeping the message they already receive.

**Ran the real thing:** served over HTTP and driven in a real browser. Every state was
built by clicking the page's own controls, not by writing into storage, then encoded,
decoded, and compared field by field against the original.

**Design:** the code is a compact encoding rather than JSON, because it has to survive
inside a text message. Four fully scored homes with notes and condition is 266 characters
against 1302 for the raw state, and twelve homes is 685. It rides at the bottom of the
summary the buyer already sends, so neither party changes behaviour.

A fingerprint of the criteria lists travels with it. The masks are positional, so a
rebuilt scorecard with a changed list would restore every answer against the wrong
question. The page refuses in that case and says why.

### Break attempts

1. **A note containing a tilde.** The record separator. `encodeURIComponent` leaves `~`
   alone, so a buyer writing "kitchen ~ 25k" split their own backup in half and it decoded
   as incomplete. Found by testing with a realistic note rather than "test". Escaped.
2. **A code from a different criteria list** — refused, with the reason.
3. **Truncated, garbage, empty, null, and a valid prefix with a broken body** — all
   refused with a plain sentence, nothing written.
4. **A code pasted inside a whole text message**, greeting and sign-off around it, which
   is how it will actually arrive. Extracted and restored.
5. **A code carrying a house no longer on the list.** Held, not shown, and the message
   says so rather than silently dropping it.
6. **Restoring over existing scoring.** Arms once and states what it will replace before
   it will do it. A clean phone restores in one tap with no warning.
7. **Round trip, field by field**, across must-haves, nice-to-haves, easy-to-forget,
   deal-breakers, both people's columns, seven condition states, two work states, gut
   scores, skipped flags and a note containing a tilde, quotes, an ampersand, a percent
   and a colon. EXACT, in both solo and two-buyer builds.
8. **A sentence starting with a number word.** "Restored. two homes are back." Added a
   capitalising form.

### The one-phone rule

Nowhere did the page or the skill say this tool assumes one shared phone, and two buyers
on two phones each get a complete-looking page holding half the data, with no warning.
Sarah chose one phone. It is now stated at the top of the stops list whenever there are
two names, hidden for a single buyer, and written into the skill in three places.

### The delivery section

Not missing content, a broken document. The heading promised "pick one of these" and then
a different section ran for fifty lines, with the actual options buried at its end. The
sections are now in the order someone reads them, each delivers what its heading promises,
the permanent link is the recommendation rather than one of three equals, and the doubled
divider is gone.

**Status: DONE** for this slice. Still no buyer has used any of it.

---

## Slice: the first stranger test, v1.5

Sarah ran the scorecard herself in a fresh chat and reported four things. Three had one
cause and one was a real bug nobody had hit because nobody had clicked that button on a
laptop before.

**The preview pane is not a browser.** She opened the finished file in the Claude desktop
app's file viewer, which says so itself: *"This tab shows a single file and can't follow
links."* Every handoff failed there: the maps buttons opened an empty directions page, and
the text and email buttons did nothing. The page was fine the whole time.

Verified by serving her exact file over HTTP and reading the generated hrefs: all three
addresses present, correctly encoded. Then loaded the Google URL itself, which resolved to
*"Your location to 4100 W Sunset Blvd #512"* with both waypoints and the map centred on
Los Feliz. The link was always right.

Fixed by naming the trap in the handoff section, because an agent who hits it will think
the product is broken and never say so.

**Apple Maps multi-stop is a real bug, on every non-Apple device.** The form
`daddr=A+to:B+to:C` is honored only by the Maps app on an iPhone or iPad. Apple's web Maps
silently rewrote the whole chain into a single destination,
`destination=2240 Ronda Vista Dr, Los Angeles, CA to:1842 N Edgemont St...`, and dropped
her into Huntington Park, nowhere near any of it. It would have done that for every agent
on a laptop since the button shipped.

The button now renders only on a device whose Maps app honors it, and Google carries the
route everywhere else. Verified both ways by swapping the user agent and re-wiring: hidden
on desktop, shown with the full chain on iPhone, Google keeping all three stops throughout.

**The decision block was not a bug.** Clicking one records it, shows the line underneath,
and carries it into the summary as `WHERE WE LANDED: One of these is the one`. Confirmed
against the generated summary text.

**Status: DONE** for these findings. The first real test found a shipped bug in forty
minutes, which is the argument for the rest of the field test.

---

## Slice: what the friend test found, v1.6

An agent installed it overnight and reported their AI had caught "a name-display issue"
and "a symbol that could break the page" and fixed them locally. Those fixes exist only on
that machine. Rather than wait to hear what they were, I went looking for the class and
found two, both shipped, both reproducible on the live site.

**Entities reaching plain text.** `SUMMARY_SUBHEAD` is written for HTML and was being used
as text. The buyer's Copy full detail produced, verbatim from the live site:

    Showing day scorecard - Jane
    Los Feliz &middot; up to $1.3M &middot; 3 bed 2 bath

The raw code went in the message to the agent.

**A quote in a name killed the page.** Every name token sat inside a double-quoted
JavaScript string: `name:"{{P1_NAME}}"`. A buyer called `Bob "Buzz" Smith` ended the
string, broke the script and left a blank white page with no error anyone would see.

Both were the same root cause, which is why fixing one at a time would have missed the
other: the template had **two escaping rules**, HTML in most places and JavaScript in a
few, and nothing said which was which. Now there is one. Every token lands in HTML, the
names, agent, date and subhead sit in a hidden block at the top of the body, and the
script reads them back out decoded. `Sam &amp; Riley` is written once and arrives as
`Sam & Riley` everywhere, on screen and in the message.

Verified with a deliberately hostile build: a buyer named `Bob "Buzz" O'Brien-Smith`, a
partner `María José & Co`, a subhead of `O'Hara & Sons · 100% <best>`. Page alive, all
four stops rendered, export correct, console clean. Before the change that was a dead
page.

**The same trap bit me while fixing it.** My first edit anchored on `<body>` and landed
inside the header comment, which mentions the tag in prose, so the block was commented out
and every name came back empty. Identical in shape to the token-inside-its-own-
documentation bug from v1.1. The comment no longer spells the tag with angle brackets, and
the anchor is now the tag at the start of a line.

**Open, not fixed:** the friend's copy has diverged from the repo. Whatever their AI
changed is local, and an `update my showing scorecard` would overwrite it. Sarah needs to
ask what it found.

**Also open:** they built a Spanish version for a Saturday tour. The template is English
throughout and the skill says nothing about other languages, so an AI improvised a
translation of a 65KB file with no checks. Unverified and undesigned.

**Status: DONE** for the two bugs. The divergence and the translation question are open.

