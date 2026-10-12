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
