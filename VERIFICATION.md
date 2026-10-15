# Verification log

## Slice: the public skill repo, v1.0

**Working means:** an agent who has never seen this installs it, answers eight questions
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

---

## Slice: language skeleton, v1.7 (walking skeleton only, NOT shippable Spanish)

**Working means:** the buyer taps a toggle in the header, every word on the page changes
language, and nothing they have already scored is lost.

**Ran the real thing:** the example built and served over HTTP, driven in a real browser.
Scored a home, switched to Spanish, compared the stored state byte for byte, switched
back, reloaded.

**Design:** every string lives in one `STRINGS` table keyed by name, with a block per
language. `data-t` and `data-th` mark the static text; `repaintAll()` redraws everything
the script generated. Scores are stored against stop ids and criterion indexes, never
against labels, which is why a language switch cannot disturb them. Adding a third
language is adding a third block.

Spanish is this market's Spanish, which is Mexican usage: cochera rather than garaje.

**Verified:** start English, toggle to Spanish, tab reads "Las casas de hoy", compare
heading reads "Cómo van las cosas", the `html lang` attribute follows, the button flips to
EN, all four stops still render. Stored state identical before and after. Toggle back,
English returns. Preference persists.

### Break attempts

1. **A half-filled table**, which is the real risk of shipping this in stages. A buyer
   cannot tell which half of the page they are missing. Two guards now: a key check that
   refuses any English key without a twin, and an explicit `ES_COMPLETE` flag that a
   person flips only after reading both languages end to end on a phone. The key check
   cannot catch a string that was never lifted into the table, which is why the flag is
   human and not computed.
2. **A stored Spanish preference with the flag off.** Resets to English on load and clears
   the stale preference, so there is no route to a half-translated page.
3. **A Spanish phone.** `navigator.language` is read on first open, so a Spanish-speaking
   buyer would land in Spanish without touching anything. Currently inert behind the flag.

**Tripwire:** `ES_COMPLETE` plus the key check. Both live in the template, so they travel
with every scorecard built from it.

**Status: NOT DONE.** The mechanism is proven and the table holds 11 of roughly 140
strings. The toggle does not render and English is byte-identical to before, so this is
safe to sit in the repo, but there is no usable Spanish yet. Remaining: lift the other
~130 strings, translate, read both languages end to end at phone width, flip the flag.

**Open question for Sarah:** whether she reads Spanish well enough for "show me both to
check" to be a real review. If not, the client becomes the reviewer and the Spanish view
carries a line inviting correction.

---

## Slice: the script-tag break, v1.8 — PARTIAL, one bug open

Vanessa, the first agent to install it, reported that a must-have containing the
characters that close a script tag breaks the page. Reproduced, and worse than reported:
the script dies entirely, no stops render, the hidden blocks spill into view, stylesheet
text appears on screen, and the top of the page still looks finished.

**Cause.** Yesterday I moved the names out of the script element for exactly this reason,
called it "one escaping rule", and left all seven lists behind. Criteria, hints, addresses
and facts were still being written into JavaScript arrays inside the script element, where
termination happens at HTML parse time before any code runs. Nothing inside the page could
defend against it.

**Fixed.** All seven lists now live in a hidden HTML block and the script reads them back
out. Verified with her exact case: a must-have reading `A garage </script> and a yard`.
Page alive, four stops, seven must-haves, one script element, console clean, the hostile
text intact as a label.

### The hostile grid, run for the first time — and it found the next one

Built two scorecards with one payload in every field a person can type into: buyer name,
partner name, agent name, business name, subhead, date, lede, footer, every list's label
and hint, and the first stop's address, facts and area. Payload:
`A" \ </script> <b>x</b> & café 🏠 'q'`, built once correctly HTML-escaped and once raw.

**Both fail the same way: the page survives, every list comes back empty, and the error
banner shows.** Strictly better than a dead page, and still a broken scorecard.

**Cause, and it is the same mistake again in a new place.** The lists are read as JSON.
HTML escaping and JSON escaping are not the same rule: `&quot;` decodes to a bare `"`,
which is exactly what JSON cannot have inside a string, and a backslash is the same story.
I said "one rule" and then built a second one an hour later.

**The real fix, not yet made.** Stop using JSON for the lists. One item per element, label
as text and hint as an attribute, and for the tour one element per stop with a data
attribute per field. HTML escaping then governs everything with nothing layered on top,
and a quote or a backslash is just a character. That is a token-format change across
SKILL.md and the rebuild tooling, so it is the first job of the next session rather than a
rushed one at the end of this.

**Open risk, stated plainly:** today a buyer criterion containing a double quote or a
backslash empties the lists and shows the error. An apostrophe, an ampersand, an accent,
an emoji and a script tag are all safe.

**Fresh-eyes review:** none. The grid above is the builder's own, which `app-blueprint`
now says in writing is the weaker option. The two findings that mattered most in this
whole build both came from Vanessa, who did not build it.

**Status: NOT DONE.** The reported bug is closed and verified. The grid found a second one
in the same class and it is open.


---

## Slice: scorecard build 2.0, the list format and Vanessa's five — DONE for these, Spanish still open

**Changed.** The seven lists are no longer JSON. One `<li>` per item, label as text, hint as
`data-hint`; one `<li>` per stop with a `data-*` attribute per field. Agent name, phone,
email and storage key moved out of the script into the hidden block, so no token is written
inside `<script>` at all. `esc()` now escapes quotes (it is used inside `aria-label="…"`).
Names and initials have an HTML-safe twin (`PE`) for the places that build markup. Stop ids
are held to `[A-Za-z0-9_-]`, de-duplicated, and derived from the address when absent.
Vanessa's five: the copy button reads "Copy for [agent]"; no pronoun for the agent; no
timeline promise; eight setup questions everywhere; the duplicated Relocation phrase.

**Fresh-eyes review: a separate reviewer, told to assume it was broken, no access to my
claims.** It found five must-fix items my own pass had missed:

1. The example scorecard double-escaped `&middot;` and showed the letters on every stop.
   Fixed; SKILL.md now says to write an entity once and never escape over one.
2. **Both copy buttons never worked.** Two functions named `copyText` in one script; the
   second silently replaced the first, so the callback never ran, the label never changed
   and the "Copied, now paste it" line never appeared. Present before this session and
   invisible to every earlier test, because none of them pressed the button. Renamed the
   second to `copyWithLabel`.
3. `data-photo` reached an `<img src="…">` unescaped. Now `esc()`.
4. Stop ids: duplicates shared one state; a space, colon, tilde or quote in an id broke
   the backup code or threw. Now sanitized and de-duplicated in `readTour`.
5. SKILL.md told the AI to escape every token, which is wrong for font and colour tokens
   (CSS) and for `LOGO_IMG`/`BRIEF_CELLS` (finished HTML). Carve-out added.

**Tripwire.** `tests/hostile.py` now also covers `data-photo`, hostile duplicate ids, the
copy callback and the backup-code round trip. Watched failing on purpose: quote escaping
removed (fails), `PE` removed (fails), `data-photo` unescaped (fails), duplicate
`copyText` restored (fails). Passes on the current template, escaped and raw.

**Left open, logged not fixed (reviewer's nice-to-haves):** identical labels attribute
wrongly in the disagreement panel; label whitespace is not collapsed (collapsing would
change the backup fingerprint and invalidate old codes); an item with no label is dropped
silently; empty lists still draw empty section headings; solo mode still shows some
two-person copy; `sms:`/`mailto:` values are not URL-encoded; `your-brand.example.json`
lacks `agent_full_name` and `license_line`; `hostile.py` hardcodes the macOS Chrome path
and is not shipped with an installed copy.

**Not covered by the test:** UI handlers beyond copy, solo mode, empty and identical-label
cases. Those are the reviewer's, run once by hand.

**Status: DONE** for jobs 1 and 2 (zero open must-fix after the reviewer's list). The
Spanish (job 3) is NOT DONE.

---

## Slice: Spanish (job 3) — STARTED, NOT DONE, safe to leave

**Done so far (stage 1).** The machinery and every piece of static text. `t(key, vars, html)` now
substitutes `{agent}` and other placeholders, escapes in HTML mode, and uses a `key_1` variant
when there is one buyer (usted) and the plain key for a couple (ustedes). English for anything
marked in the HTML is read off the page itself into `STATIC_EN` before painting, so English is
never stored twice. `count()` returns digits in Spanish to avoid gender agreement. About 40
static strings are tagged (`data-t`, `data-th`, `data-tp`, `data-ta`) and translated in both forms.
`ES_COMPLETE` is still false, so the toggle is hidden and English is unchanged. `tests/hostile.py`
still passes.

**Not done (stage 2, the strings the script draws).** Photo messages, tile flags, stop cards and
skip, the six criteria groups and their subtitles, the condition state labels, gut-feel aria,
the dock, all of Compare (missing, disagreements, grid, group headings), the four closing
decisions, send and copy messages, and the restore messages. Each needs a `STRINGS` entry in
both languages (with `_1` where the verb changes) and its call site changed to `t()`.
Plurals use `count()` and two keys (one / many).

**Decisions made.** The text message and summary the buyer sends the agent stay in English,
because the agent reads them. Criteria, hero, lede and the deal-breaker sentence are the
agent's own words and show in whatever language the agent wrote them.

**Before flipping `ES_COMPLETE`.** Add `tests/spanish.py`: force Spanish, open every view, and
fail on any visible English. Then a separate reviewer, and a read of both languages on a phone.

---

## Slice: Spanish (job 3) — BUILT AND REVIEWED, toggle still OFF pending a Spanish read

**Built.** Every word the page itself says is now in both languages: about 170 phrases, each
with a one-buyer (usted) form where the grammar differs. Static text is tagged in the HTML and
its English is read off the page (never stored twice); text the script draws goes through
`t()`. Counts are digits in Spanish. `ES_COMPLETE` is still false, so buyers see no toggle and
English is unchanged.

**Tripwires.** `tests/spanish.py` forces Spanish for a couple and for a single buyer, opens
every view and presses every button that writes a message, and fails on: visible English
(by word list AND by any Spanish line identical to its English line), English that changes
after a Spanish round trip, a message or armed label left in the wrong language after a
switch, and a key with no Spanish twin. Watched failing on purpose for: a skipped label left
untranslated, an untranslated "Tap again to clear", and the message-redraw fix removed.
`tests/hostile.py` still passes.

**Fresh-eyes review: a separate reviewer, not told it worked.** It found, and these are fixed:
a language switch left the copy and restore messages and the armed labels in the old
language; a copy-code label could stick in the wrong language; a single buyer was addressed
as ustedes in two headings; "parado" assumed a man; "las 1 del código" in the restore text;
a doubled agent name when it contained `{agent}`; "factores descartantes" is not how anyone
speaks (now "motivos para descartar"), plus several regional words ("fuentes", "fila",
"Cancelar"). The solo dock no longer shows a partner's percentage.

**Open, by design or deferred.**
- Agent-supplied text (hero, lede, brief cells, stops heading, deal-breaker sentence,
  criteria, dates, facts, page title) stays in the language the agent wrote. SKILL.md now says
  to write them in Spanish for a Spanish-speaking buyer. Bilingual criteria are not wired.
- The summary the buyer sends the agent is English on purpose. The page does not say so.
- "teléfono" is used throughout; many Latin American buyers say "celular". Every stop is
  "Casa N", including condos.
- English closing messages also have no one-buyer wording ("We want a second look").

**Before switching it on.** Someone who reads Spanish should read `tests/spanish-review-sheet.md`
(every phrase, English beside Spanish), then the live page on a phone in both modes. Then set
`var ES_COMPLETE = true;` in the template. If nobody can read it first, ship it on with the
Spanish view carrying a line inviting the client to correct it.

**Status: DONE as built, NOT LIVE.** Everything the tests and the reviewer could reach passes.
No native-speaker read has happened.

---

## Slice: Spanish ON, with the correction line — final pass

**Changed.** `ES_COMPLETE = true`. In Spanish mode a line under the tabs says the page was
translated with a tool, may sound wrong, and to tell the agent. New `DEFAULT_LANG` token (`es`,
`en` or empty) so an agent can open a Spanish buyer's page in Spanish whatever their phone is
set to; the buyer's own choice still wins after that.

**Verification.** Phone width checked in a 360 and a 390 px frame, both languages, three views:
no horizontal overflow, no clipped button. Screenshots read by eye in Spanish. `tests/spanish.py`
and `tests/hostile.py` pass.

**Fresh-eyes review, a second separate reviewer** (told to build a scorecard from SKILL.md alone,
then break it). It found, and these are fixed:
1. "Clear this tour" left the buyer's last "where we landed" decision behind, and it was sent to
   the agent on the next tour. Present before this session.
2. The summary said "Agreed on everything" for a solo buyer and for an unscored stop.
3. A Spanish-speaking buyer on an English phone got a half-English page, and nothing let the
   agent prevent it (now `DEFAULT_LANG`).
Also fixed: the print layout carried the language button and the correction line; the example
brand file lacked `agent_full_name` and `license_line`; SKILL.md now maps every brand value to
its token, defines STORAGE_KEY and DEFAULT_LANG, and says agent values reach the agent's message;
"wasted Saturday" and "Saturday afternoon" no longer assume a day; the dead `cl()` is gone; the
English one-buyer closing buttons read "I want / I need".
Each of the three real defects now has a test that fails when the fix is removed (watched failing).

**Not covered.** No native Spanish speaker has read it (`tests/spanish-review-sheet.md` is the
sheet for that). The reviewer read the Spanish for English leaks, not for quality; the earlier
reviewer did the quality pass. A real PDF print was read from the CSS, not rendered.

**Status: DONE and LIVE** for jobs 1 to 3, with the correction line as the standing safeguard.

---

## Slice: rebuilding an old client scorecard with the new template

**Question.** An agent who updates the skill still has scorecards built in the older formats.
When she rebuilds one, does the client's progress survive?

**Ran** `tests/rebuild_old.py` on the three real scorecards for one client, covering both older
formats (lists as script arrays; lists as JSON-style text). Each old page was loaded so its own
code read its lists; answers were seeded; the page was rebuilt from the current template.
**All three pass:** same list counts, same stop ids, same storage key, identical scores computed
from the buyer's stored answers, an identical backup code, and a backup code made by the old
page was restored by the new page with every house recognised.

**Differences found, all intended.** The summary no longer says "Agreed on everything" for a
solo buyer or an unscored stop. The old subhead carried a literal `&middot;`.

**Gap closed.** SKILL.md's rebuild step described only one of the two older formats. It now
covers both and says to write `&middot;` once.

**Not covered.** The rebuild was done by a script standing in for the AI, not by an AI
following SKILL.md. The earlier fresh-eyes review built from SKILL.md for a new client, not
from an old file. The "update my showing scorecard" command itself (clone, copy, delete) was
not run.

**Status: DONE for the data path; the update command and an AI-led rebuild are UNTESTED.**

---

## Slice: the update command

**Why.** The update was never run. A fresh AI was given an install at the old version, a brand
file and one finished client scorecard, and told only "update my showing scorecard". Separately,
Sarah's own AI, told "update my scorecard", was blocked on the download and asked whether she
meant the tool or a client's scorecard.

**Found.**
1. The old instructions download to a system temp folder and then delete it. Some setups refuse
   exactly that, and Sarah's did, which stalls the update half way.
2. They never named the repository address.
3. "update my scorecard" is ambiguous (the tool, or a client's scorecard).
4. Nothing said what to do in the original repo, or what to tell the agent when a command is refused.
5. An installed copy has no `tests/`, though SKILL.md mentions them.

**Fixed.** The update now downloads into the agent's own folder as one file, checks it is whole,
extracts only the skill over the installed one, and has no delete step. It names the address,
handles "update my scorecard" with one question, runs `git pull` in the original, and says what
to do when a command is refused (stop, change nothing, say which step, offer a manual route).

**Verified.** The old-instructions run by a fresh AI: brand file and client scorecard unchanged
(fingerprints), skill files identical to GitHub afterwards, nothing left behind. The new
commands run literally on a fresh old-version install: download whole, extract, brand and
client unchanged, template identical to GitHub, only the one tarball left.

**Not covered.** A fresh AI following the NEW wording (the new text is not on GitHub until
pushed, and the first update on any existing install runs on the old text). Whether Vanessa's
permission settings allow `curl` and `tar`. The refusal path is documented, not exercised.

**Status: DONE for the commands; the AI-led run of the new text is UNTESTED.**

---

## Slice: "What happens next" above the send buttons, and the open-header bug it exposed

**Asked for by Sarah** after she scored a whole scorecard herself and sent the report without
noticing the section, which sat below Text, Email, Copy and Clear.

**Changed.** The section now sits in Compare, after "Every Home, Every Line" and before the
send buttons. The decision is in the text, email and copy report (it already was) and now also
in "Copy full detail". Spanish unchanged.

**Found while looking at it.** In light mode the section was unreadable: dark gray on a navy
page. Cause, present before this change: the last header cell in the example and in the 10-12
Jane scorecard was missing its closing `</div>`, so the header stayed open and the entire page
rendered inside it. In dark mode nobody notices. The header cells and the logo were raw HTML the
AI writes by hand, the same class as the lists. Both are now text (`BRIEF_CELLS` as list items,
`LOGO_SRC` as a data address) that the page turns into elements itself, so a mistake can only
produce a wrong word. The earlier reviewer's note that BRIEF_CELLS and LOGO_IMG were never
filled in the tests was right and was not acted on; they are filled now, with malformed values.

**Tripwires.** `hostile.py` fills the brief (deliberately unclosed) and the logo and fails if
the header swallows the page or the brief or logos do not build. `spanish.py` fails if the
section is not between the grid and the send buttons, or if the decision is missing from either
report. All watched failing on the previous template.

**Verified.** Light-mode screenshot at 390 px: readable, in the right order. Rebuild test on
the four real Jane scorecards still passes.

**Not covered.** No separate reviewer has looked at this change; only the builder has. The real
Jane 10-12 scorecard still has the open header (it is a finished client file and was not edited).

**Status: BUILT, tested by the builder, NOT independently reviewed.**

**Fresh-eyes review of this slice** (a separate reviewer; no page-breaking bug found, but
real gaps). Fixed: SKILL.md said a header mistake "can only produce a wrong word", false for a
raw `<script>`/`<img>` (now says to escape like every list); rebuilding an old scorecard lost
its header strip silently and `rebuild_old.py` could not notice (SKILL.md now says to carry the
cells forward; the test now compares them and was watched failing); the decision section stayed
visible when the only scored home was skipped (now hidden); a logo with line breaks in its
base64 was rejected silently (whitespace is stripped; SKILL.md says one line); the example's
header comment still documented the old tokens.
Left, by choice: the section is now on the Compare tab only, so a buyer who taps "Done here"
reaches it only through Compare; a solo buyer's report line uses the couple wording ("We
want"); the "Copy full detail" box does not refresh if the decision changes after copying.
Not edited: the real Jane 10-12 scorecard still has its open header.

**Status: DONE, independently reviewed.**

---

## Slice: install steps as 1, 2, 3, and the install no longer deletes anything

**Asked for by Sarah** so a stranger, or her Krista and mastermind groups, can see the whole path
at a glance. README and INSTALL now read: 1) paste the install line into the Claude chat where
scorecards will run, 2) say "set up my showing scorecard", 3) say "build a tour scorecard for
[client]"; to update later, "update my showing scorecard".

**Found.** Door 1 told the AI to download to a temp folder and delete it, the same step that
Sarah's setup refused for the update. Rewritten to download the archive into the agent's own
folder, check it, extract only the skill plus LICENSE, and leave the download in place.

**Verified.** The commands, run literally in an empty scratch install: download whole, skill
and LICENSE extracted, nothing deleted, one download file left. The first attempt was also
refused by the build gate (the scratch path looked like a new skill folder); the scan and
app-blueprint were run first, not worked around.

**Not covered.** A fresh AI following the new INSTALL wording (it is not on GitHub until pushed).
"Set me up" is documented as working only in a standalone install; inside a larger setup the
safe phrase is "set up my showing scorecard", which is what every document now says.

**Status: DONE for the commands and the wording; AI-led install of the new text UNTESTED.**

**Follow-up: a fresh AI followed the live install wording.** Given only the one-line install
request in an empty setup folder, it read INSTALL.md, downloaded the archive into its own
folder, checked it by listing it, extracted only the skill, placed LICENSE inside it, deleted
nothing and was refused nothing. It flagged three wording gaps (says "zip" for a .tar.gz, did not
say how to check the download, "beside" for LICENSE was ambiguous), now fixed. Not yet tested:
an install into a setup whose skills folder already holds other skills (the usual case).

---

## Slice: Vanessa's feedback (LOCAL.md, ES_NOTE, the example, a Questions section)

**Evaluated.** Her two fixes were sound and cheap: updates replace SKILL.md, and the Spanish note
could not be turned off. Her group FAQ was mostly accurate, with one false claim: "ask your AI to
open the example" would find nothing, because the example lived in `examples/` and an install
only carries the skill folder. Context from Vanessa: many people who install this are not
technical and get lost easily, so plain wording in README and in what the AI says matters most.

**Changed.** `LOCAL.md` (read first, wins on preferences, cannot weaken any "never" rule or the
fair-housing filter, never touched by an update, ignored by git in the original repo).
`ES_NOTE` (only "off" hides the Spanish note; default on). Couple grammar fixed ("Si lo notan,
díganselo"). The example now lives in `assets/` so an install and an update carry it, with a
"show me the example scorecard" trigger. A Questions section in README.

**Fresh-eyes review, a separate reviewer.** Found, and fixed: the LOCAL.md carve-out listed only
three rules, so an AI could read a LOCAL.md line as overriding the fair-housing filter, the
no-network rule and others (now covers all of them, bars sending client files to a published
folder, and says to ignore a conflicting line and tell the agent); SKILL.md described the example
as having three stops and a knocked-out home (it has four, nothing scored). Also fixed: ES_NOTE
doc says false/no keep it on; a rebuild now keeps ES_NOTE and DEFAULT_LANG; INSTALL and CLAUDE.md
mention LOCAL.md; the Netlify answer now mentions making the link public.

**Tests.** `spanish.py` now checks every ES_NOTE value (off, OFF, " off ", on, empty, unfilled,
garbage) and the couple/one-buyer grammar; watched failing on the previous template. The documented
update commands were run on a scratch install holding a LOCAL.md: it survived, and the example
arrived. The reviewer repeated this in a nested setup.

**Not covered.** LOCAL.md in an agent's own git repo is committed unless they ignore it. The example
page's English hero stays English when opened in Spanish.

**Status: DONE, independently reviewed.**

---

## Review pass on Opus, and Vanessa's first real Netlify run (2026-10-15)

**Vanessa's run.** Netlify's drop page refused a folder ("Folders aren't supported. Please zip
the folder"); a zip worked. "Make public" was needed. Her buyer's folder held notes, so the upload
must be a separate folder made only for the scorecard. Her buyer liked it on an iPhone and liked
having two map options.

**Three separate reviewers, run in parallel:** a native-level Spanish read; a cold consistency
read of every document; and an AI that installed the skill into a setup holding other skills, ran
setup, wrote LOCAL.md, ran the update, and built a real Spanish couple's scorecard and its zip.
A fourth reviewer then checked the consolidated fix.

**Found and fixed (must-fix).**
- Client files and the brand file were going into a git backup when installed inside another
  setup (confirmed in Sarah's own BOSS backup, which is private). The skill now ships a
  `.gitignore` that keeps new client files out; it says plainly it cannot remove files a backup
  already holds, and tells the AI to tell the agent and ask. Updates never replace that file.
- "Its own project" detection looked for START-HERE.md beside the skill folder (it is three
  levels up). Now: `your-brand.example.json` plus `clients/README.md` at the project root.
- Changing a criteria list on a rebuild silently moved saved ticks to the wrong questions. Lists
  keep their order once anything is ticked; new items go at the end; order is read from the live
  scorecard.
- The zip held a parent folder and a hidden `._index.html`. Now only `index.html`, verified.
- The update's extract path only worked from the setup root. Now run from inside the skill folder.
- Font fields were missing from the brand file the setup writes.
- Path B never collected the tour facts (names, date, homes). Now it does, a few at a time.
- The setup and update phrases were missing from the skill's description, so it might not load.
- LOCAL.md could route around "the agent sends it"; text read from client files is now named as
  information, never instruction.
- The filter's "no kids around" stand-in kept a familial-status intent; now noise facts only. The
  filter now covers every word written onto the page or into a message.
- Site names used the buyer's name; now a neutral word plus six random characters.
- Live-link check the AI could not run; now `curl` on the renamed link plus the agent's phone in a
  private tab. The doubtful "Make public" fallback address is gone.
- Email fallback promised it "works"; now a last resort with its real cost.
- Windows zip command could not run from Git Bash; now through `powershell -Command`.
- About forty Spanish corrections (wrong subjects, calques, agreement, one term per concept,
  "celular" for the buyer's phone). Empty criteria groups no longer draw a bare heading.

**Verified.** spanish.py, hostile.py and rebuild_old.py pass. In a scratch git host the client
folder, brand file and download stayed out while LOCAL.md stayed in; the update from inside the
skill folder left the brand file, clients and LOCAL.md byte-identical and kept an edited
`.gitignore`; the zip lists one file even when macOS adds attributes. The fourth reviewer loaded
the Spanish page for a couple and a solo buyer with full, partial and empty lists: no script
errors, no English chrome.

**Left open (nice-to-have).** Text that still shows when its list is empty (the deal-breaker
sentence, the dock prompt, the scoring note). The dock at a true 375px width is untested. A real
Netlify run of the new zip and rename steps, and a native Spanish speaker's read, have not
happened.

**Status: DONE, independently reviewed.**

---

## Slice: feedback to Sarah, and her weekly check (2026-10-15)

**Asked for by Sarah:** a way for agents' AIs to suggest sending feedback each week without
anyone texting her, and a weekly reminder on her side to read it. No app, no background job: the
skill only runs when used, so the ask is event-driven (at most once a week, at the end of a
finished task) and the report goes to a pre-filled public GitHub form the agent reviews and
submits. Agents without GitHub get the same report as text to paste to Sarah. Sarah's side: a
weekly item in her Action Items and the "check my scorecard feedback" routine in her own
`LOCAL.md` (reads open reports with `gh`, sorts them, proposes fixes, re-sets the reminder).

**Two separate reviewers played the agent's AI through the whole flow** (eight moments: ask,
show, send, confirm, a showing tomorrow, a failed task, stop asking, send anyway and cancel),
with notes seeded on purpose with client names, an address, a price, a site name and a file path.
First run found: "open the form" contradicted "never open anything"; notes were wiped before
anyone knew they were sent; sending once undid "stop asking"; it could ask twice; it never said
the agent's GitHub name shows; the cleaning rule was vague; the length limit was on the wrong
thing. Second run, on the rewrite: no leaks (checked by decoding both links and searching them),
no double asks, "Do not ask" held; found that sent and unsent notes could mix and that the
encoder was unnamed (an apostrophe could break the Windows open command). All fixed.
The issue template was removed so the pre-filled form is not replaced by a template chooser.

**Verified.** A realistic report with quotes, accents and an emoji round-trips through the link
intact; GitHub sends a signed-out visitor to sign in, then back to the form.

**Not covered.** Sarah has not yet opened a pre-filled link while signed in to confirm the form
shows filled; no real agent has sent feedback.

**Status: DONE, independently reviewed.**
