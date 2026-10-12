---
name: showing-scorecard
description: Build a buyer a phone scorecard for a showing day, scored against what that buyer actually told you they want. Two people score independently on one phone so disagreements surface while they are still standing in the house, deal-breakers take a home out regardless of score, and the big systems get logged separately because condition is a different question from fit. No login for the buyer, nothing to host. Use when the agent says "build a tour scorecard for [client]", "showing scorecard for [client]", "we're seeing homes with [client] on [date]", "build the scorecard for [address]", or "add [address] to [client]'s tour".
version: "1.0"
author: Sarah Arlington, Rooster Homes
license: See LICENSE. Use freely in your business; do not redistribute or resell the skill.
---

# Showing Scorecard

A buyer walks four houses on a Saturday. By Tuesday they remember the kitchen from the
second one, the yard from the fourth, and nothing else. Then they decide.

This builds them a page that fixes that, scored against what *that* buyer said they
wanted, not a generic checklist.

It does four things a paper checklist cannot:

1. Scores each home against their own words.
2. Lets two people score independently on one phone, and shows where they disagree while
   they are still in the house.
3. Treats a deal-breaker as a deal-breaker. A hard no takes the home out no matter how
   well it scored.
4. Logs the big systems separately from fit, because a home can hit 95% of what they
   want and still need a $30,000 sewer line.

---

## Trigger

- `Build a tour scorecard for [client]`
- `Showing scorecard for [client]`
- `We're seeing homes with [client] on [date]`
- `Build the scorecard for [address]`
- `Add [address] to [client]'s tour`
- `Set me up` / `Set up my showing scorecard` (first run only, the brand questions)
- `Update my showing scorecard` (pull the newest version, leaving brand and clients alone)

---

---

## Fair housing: what never becomes a scored criterion

**Read this before you take a single must-have from anybody.** This skill's method is to
transcribe what a buyer said and score homes against it. That is also the mechanism that
turns an offhand remark into a written, branded, scored record of homes rejected on an
illegal basis.

The exposure is not only that an agent might steer somebody. It is that **the document
itself is a statement.** Under the Fair Housing Act, 42 U.S.C. section 3604(c), it is
unlawful to make, print or publish any notice, statement or advertisement about the sale
of a dwelling that indicates a preference, a limitation or discrimination on a protected
basis. Two things about that provision decide how this skill has to behave:

**Intent does not matter.** The test is whether an ordinary reader would take the
statement to prefer or disfavor a protected group. Not whether anyone meant it that way.

**"The buyer said it" is not a defense.** The agent made, printed and published it the
moment it went on a page carrying their brand and got emailed back and forth. Spoken
words and text messages have both been held to be statements under this provision.

So the transcription is filtered, always, and the filter is not optional.

### This tool, done right, is a recommended practice

Worth knowing before the rules, because it changes what you are building.

The California Association of Realtors fair housing advisory (Form FHDA, rev. 12/24)
lists examples of **positive** practices. The first one reads:

> "Real estate licensees working with buyers or tenants should apply the same objective
> property selection criteria, such as location/neighborhood, property features, and
> price range and other considerations, to all prospects."

That is a description of this scorecard. Objective criteria, written down, applied the
same way to every property and every client. The filter below is not a disclaimer bolted
onto a risky tool. The filter is what makes the tool an instance of the practice the
advisory recommends. An agent who uses it properly has a written record of exactly that.

The same list warns against the opposite: making any statement or advertisement that
directly or indirectly implies a preference, a limitation or discrimination regarding a
protected characteristic. A scored criterion is a statement.

And one more, which is why the buyer's free-text notes matter: the advisory flags that
asking for or accepting personal information or letters from a buyer can inadvertently
reveal protected status, raising the risk of unconscious bias and of claims by buyers
whose offers were rejected. A notes field is that kind of document.

### The protected classes

**Federal floor, seven.** HUD names race, color, national origin, religion, sex,
familial status and disability. HUD's enforcement position since 2021 is that sex
includes sexual orientation and gender identity.

**States add a great deal, and the agent's state is what they are actually held to.**
California is the author's state and a useful illustration of the gap. Its Realtor
advisory lists twenty, and ends with a catch-all:

| | | | | |
|---|---|---|---|---|
| Race (and race traits) | Color | Ancestry | National Origin | Religion |
| Age | Sex, Sexual Orientation | Gender, Gender Identity, Gender expression | Marital Status | Familial Status (a family with a child or children under 18) |
| Citizenship | Immigration Status | Primary Language | Military/Veteran Status | Source of Income (e.g. a Section 8 voucher) |
| Medical Condition | Disability (mental and physical) | Genetic Information | Criminal History (non-relevant convictions) | **Any Arbitrary Characteristic** or Intersectionality |

The advisory adds that other classes, categories or restrictions may also apply.

Read that last cell before you decide a criterion is fine because it is not on a list.
In California the list is open-ended by design.

**If the agent is not in California, get their state's own list** and work from that, not
from this table and not from the federal seven. Their state association publishes it and
their broker has it.

### Never score these, however the buyer phrases it

Anything about **who lives there** rather than **what the property is**. The phrases
buyers actually use, which almost never sound illegal to the buyer saying them:

| What they say | Why it cannot be scored | What to write instead |
|---|---|---|
| "a safe neighborhood", "low crime" | long-established race proxy | nothing. Point them at the local police department's or city's own public crime map and let them read it themselves |
| "good schools", "a good school district" | the most common race proxy in the industry | the named attendance boundary as a boundary: "inside the Lincoln Elementary attendance area". Never a rating, never "good" |
| "a family neighborhood", "family friendly" | familial status | the property facts they actually want: a fenced yard, a second bedroom, a park within a ten minute walk |
| "near our church" / "near our temple" / "near our mosque" | religion, national origin | a drive time to one specific address they give you: "under 15 minutes to 412 Oak Street" |
| "not a lot of renters", "mostly owners" | source of income and familial status proxy | nothing. Owner-occupancy rate is not a property feature |
| "people like us", "somewhere we'd fit in", "our kind of area" | several at once | ask what the home needs to have, and write that |
| "up and coming", "an established area", "the right side of town" | race proxy | the specific thing underneath it: new construction nearby, a commute time, a price trend they can look up |
| "quiet, no kids around" | familial status | the property fact: not backing a playground, a corner lot, double glazing |
| "a walkable, diverse area" | sounds positive, still describes residents | walk score, a named amenity, a drive time |

### How to handle it in the moment

Do not lecture the agent and do not refuse to build. Convert, then say one line so they
learn it too:

> "I left 'good schools' off the scored list and put 'inside the Lincoln Elementary
> attendance boundary' instead. A school's reputation is a fair housing problem on a
> written record; a boundary is a fact. If they meant something else by it, tell me."

If a stated criterion has no lawful property-fact equivalent, say so plainly and leave it
off. A short list that can be defended beats a long one that cannot.

### The same filter applies to

The eight-question interview, especially question six. The starter sets. The hint text
under any item. The brief line at the top of the page. And the buyer's own free-text
notes, which arrive in the summary: if that language comes back, tell the agent before
it goes into a file or a CRM.

### This is a floor, not advice

These are common cases, not the whole of the law, and state and local rules add to them.
Nothing here is legal advice. The agent is responsible for everything that goes out under
their license, and their broker and state association are the authority on what that
requires.

Sources: HUD, Fair Housing Act overview, hud.gov/helping-americans/fair-housing-act-overview.
Statutory text at 42 U.S.C. section 3604. Steering at 24 C.F.R. section 100.70.
California Association of Realtors Form FHDA, Fair Housing and Discrimination Advisory,
revised 12/24, for the state list, the positive practices and the buyer-letter warning.
Every agent should be working from their own state's current advisory, not this summary.

## First run only: seven questions

**Where your files live depends on how this was installed, so work it out first.**

- If there is a `START-HERE.md` beside this skill's own folder, this is its own project.
  `your-brand.json` and `clients/` go at that project root.
- Otherwise this was added into somebody else's setup. `your-brand.json` and `clients/`
  go **inside this skill's own folder**, so nothing of theirs gets touched and nothing
  of this gets scattered through their system.

Either way: if `your-brand.json` is missing, run the questions below. If it exists but a
required field is blank, ask only for the blank ones. Triggers are **"set me up"** or
**"set up my showing scorecard"**, the second being what people say inside a larger
system where "set me up" could mean something else. If it is missing, ask these. If it
exists but a required field is empty, ask only for the empty ones. Never write the file
half-filled and never stop asking while a required field is blank, or the buyer's main
button ends up reading "Copy for " forever.

1. **Your business name**, as it should read on the page.
2. **Your first name**, as a client would say it, for the buttons and the sentences.
   Also **your full name** as it should read on a signature, which is what goes on the
   sign-off card at the bottom of every scorecard.
3. **Two colors**, as hex codes. One for headings and accents, one for the single action
   button. Ask for **mid-tone** colors, not pastels and not near-black: the heading color
   sits on a dark band and on white, so an extreme at either end disappears on one of
   them. No colors is fine. Use `#1F6F8B` and `#B33A2B`, say so, and tell them where to
   change it.
4. **A logo file path.** Square or near-square reads best at phone size. No logo is fine;
   the masthead then shows the business name on its own.
5. **The phone number** a client should text. Store it twice: as they would read it, and
   in `+15550102030` form for the tap-to-call link. Derive the second from the first.
6. **The email** a client should send results to.
7. **A footer line.** One line, usually the business name and the website.
8. **The license line your broker or state requires** on client-facing material. Ask
   what it should say rather than guessing: in some states it is the agent's own license
   number, in others the brokerage's, in others both. Empty is fine and the card hides
   the line, but ask once rather than silently leaving it off.

Then compute two more and write them in. Do not ask for these:

- `on_accent` and `on_action` are the label colors that sit on top of each brand color.
  Work out the relative luminance of each. Above about 0.45 take `#1A1A1A`, below it take
  `#FFFFFF`. White text on a pale yellow button is the single most common way a branded
  page looks broken.

```json
{
  "business_name": "",
  "agent_first_name": "",
  "agent_full_name": "",
  "color_accent": "#1F6F8B",
  "color_action": "#B33A2B",
  "on_accent": "#FFFFFF",
  "on_action": "#FFFFFF",
  "logo_path": "",
  "phone_display": "",
  "phone_raw": "",
  "email": "",
  "footer_line": "",
  "license_line": ""
}
```

Required before anything is built: `business_name`, `agent_first_name`, `agent_full_name`, `color_accent`,
`color_action`, `phone_display`, `phone_raw`, `email`. The logo, the footer and the license line are
optional and the page handles their absence.

A logo is embedded directly into the page as a data URI, resized to roughly 200px on its
long edge first. A published page can only display an image that ships inside it, so a
linked logo will not render.

---

## Getting the finished page onto the buyer's phone

The skill produces one HTML file. Nothing about it is finished until the buyer can open
it, so pick one of these and tell the agent which you used.

## One scorecard per client, not one per tour

**This is the thing to get right and the easy thing to get wrong.**

A buyer does not look at four houses once. They look at four this Saturday, three the
next, two the week after, and by week three the question that actually matters is how
this one compares to the eleven they have already seen. That comparison is the point of
the tool, and it only exists if every outing writes into the same scorecard.

So: **one living scorecard per client, rebuilt as the search goes.** Never a fresh one
per tour.

When the agent books another showing day with a client who already has one:

1. Open their existing scorecard and read its `{{TOUR}}` list and its `{{STORAGE_KEY}}`.
2. **Keep that storage key exactly.** It belongs to the client, not the tour. Everything
   scored over weeks is stored against it, and a changed key erases all of it.
3. **Keep every existing stop, with its existing `id`.** Scores are stored against those
   ids, so a renamed id is a wiped house.
4. Add the new stops at the **top**, each carrying this outing's `date`.
5. Rebuild and give them the same link. Everything scored before is still there, and
   Compare now ranks the whole search.

The list groups by date on its own once there is more than one, newest first, so today
sits at the top and earlier outings stay underneath. Compare ignores dates entirely and
ranks every house they have walked. **That running shortlist is the deliverable**, and
it is the thing a buyer cannot build for themselves after six weekends.

Houses they have ruled out get skipped rather than removed, which takes them out of the
ranking and the route while keeping the record that they were seen and rejected.

**Where the file goes.** Every scorecard goes to
`clients/<client-slug>/YYYY-MM-DD-scorecard.html`, under whichever `clients/` location
the install check above settled on, and the criteria
you worked from go beside it as `criteria.md`. The date in the filename is a version stamp rather than a separate scorecard: the
newest file is the live one and the earlier ones are history worth keeping. Create the client folder if it is not there.

When the buyer sends their results back, save those too, as
`YYYY-MM-DD-results.md` in the same folder.

Then get it onto the buyer's phone, one of these ways.

**The file itself.** Email or text it as an attachment. Works everywhere, needs nothing,
and is the right answer for an agent who is not going to set anything up. The buyer opens
it from their mail app and it behaves like a page.

**Free static hosting, for a real link.** Netlify Drop, Cloudflare Pages, or GitHub Pages
all take a single HTML file and hand back a URL, free, no card. This is the best result:
a short link the agent can text, and one the buyer can reopen. Walk them through it once
and every tour after that is a drag and drop.

**Wherever they already publish.** If the agent already has a website or a page builder,
it goes there, under their own domain.

**Then make it a QR code**, because half of this is handing a phone to somebody standing
next to you. Any free QR generator takes the URL.

Open the finished link yourself, on a phone, before the agent sends it to anybody.

---

---

## Then: three ways to get the buyer's list

**This is the part that matters.** The scorecard is only better than a checklist because
the list is theirs. Pick the first path that applies.

### Path A, they have a consultation on file

Fastest, and the best result. Ask where it is: a notes file, a document, a photograph of
a handwritten intake sheet. Read it and pull:

- their stated must-haves, exactly as written
- anything they called a deal-breaker, an absolute no, or "avoid"
- price range, bedroom and bathroom count, property types they will consider
- their own words for why they are buying and what success looks like
- how they described their day-to-day life in the home

Take must-haves **literally and separately**. "AC, tub, dishwasher, parking, in-unit
laundry" is five scored items, not one line called "features". Their price range and
their bed and bath counts each become their own must-have.

### Path B, no consultation, three minutes to make one

Most agents do not run a formal buyer consultation, and this is where the skill earns its
keep. Do not offer them a generic template as the easy way out. Ask these eight and build
the real thing:

1. What made them decide to buy now?
2. What are the three or four things this home absolutely has to have?
3. What is an instant no? The thing that takes a house out of the running on the spot.
4. What is the price range they are actually comfortable at, not what they qualify for?
5. Beds, baths, and what kind of property will they consider?
6. Which areas, and what matters about the area?
7. What does a normal weekday look like for them in this home?
8. How long do they see themselves staying?

That is three minutes of the agent's time and it produces a buyer consultation. **Offer
to save it** as a notes file next to the scorecard so the next tour uses Path A, and so
they have a record they did not have before.

### Path C, the buyer is already in the car

Start from the starter set for their buyer type below, say plainly that it is a starting
point rather than their list, and build. Then after the first stop, come back and ask the
one question that sharpens it: **"What did they react to in that first house, good or
bad?"** Add what comes out as must-haves or deal-breakers and rebuild. The list converges
on theirs within a stop or two.

Never leave a scorecard on Path C permanently. A generic list is the thing this replaces.

---

## Starter sets, by buyer type

For Path C only. Each is a starting point to be edited, never shipped as-is without
saying so.

**First-time buyer.** Must: in budget all-in including taxes and any dues; a real
bedroom with a door; somewhere to put a washer and dryer; parking that comes with it;
move-in ready enough to sleep there night one. Breakers: special assessment pending;
monthly dues above their stated ceiling. Nice: outdoor space; second bathroom; storage;
walkable to something they would actually use.

**Move-up family.** Must: bedroom count; a second full bathroom; a yard the kids can use
unsupervised; inside the specific school attendance boundary they named, by boundary, never by school reputation; a place to work from home.
Breakers: busy street frontage; a pool they did not ask for. Nice: separate dining;
primary on the same floor as the kids; garage that fits two; flat lot.

**Downsizer.** Must: single level or a working elevator; primary bedroom on the entry
level; low maintenance outside; parking close to the door; in budget without touching
retirement funds. Breakers: stairs to the front door; a yard needing weekly work. Nice:
guest room; a spot for the grandkids; walkable to errands; a clubhouse, or organized activities on site.

**Investor.** Must: the number works at their stated return; condition they are willing
to carry; rentable as-is or after the work they have budgeted; permitted square footage
matches the listing. Breakers: unpermitted additions; an HOA that restricts rentals;
pending litigation. Nice: separate entrance; existing tenant in place; room to add a unit.

**Relocation.** Must: commute they can live with on a real weekday; in budget; move-in
ready; enough bedrooms for whoever is arriving. Breakers: anything needing work before
they can move in; a commute over the number they named. Nice: furnished or partly;
short-term flexibility; furnished or partly furnished.

---

## How it scores

Three buckets plus a gate.

**Deal-breakers. Not scored.** Their hard no's. Any check here marks the home OUT no
matter what the number says, and the card, the comparison and the summary all say so.
These are facts about the home, so one tap covers both people.

**Must-haves. 25 points each, scored per person.** What they said they cannot live
without, plus their price range and bed and bath counts as their own items.

**Nice to have. 4 points each, scored per person.** Lifestyle and style, from how they
described their day and what they said about homes they like.

**Easy to forget. 2 points each, shared.** The factual checks nobody makes while standing
in a staged room. Pick the library that matches the property type.

A must-have is worth more than every nice-to-have combined, and the template keeps that
true on its own: the must-have weight derives from the length of the nice-to-have list
rather than being a fixed number. Add a tenth nice-to-have and the must-have weight rises
with it. Do not replace that line with a constant, or a long consultation will quietly
invert the thing the page tells the buyer.

**Must-haves and nice-to-haves are tapped per person** because they carry judgment.
Deal-breakers and the easy-to-forget list are facts about the house, so one tap covers
both and it halves the tapping on the longest list.

**A missed must-have is flagged by count, not buried in the percentage.**

**Disagreements are the point.** Anything one person counted and the other did not lights
up on the spot, keeps a running count, and gets named in a "Where You Two Don't Agree"
section with who counted what. Two people quietly scoring the same house differently and
never saying so out loud is how couples make a decision they regret.

**Solo buyer:** one column, no initials, no disagreement panel. Read it from the client's
own file or from question 1 of Path B. Do not ship a two-column layout with one name in
both.

---

## The two "easy to forget" libraries

Pick by property type.

**House or small lot.** Which way it faces and the light at 6pm; street parking after
6pm; where a garden would go and its sun hours; whether outdoor space is private or
overlooked; noise from the nearest main street; whether an addition or conversion was
permitted; roof age and visible patching; whether the electrical panel can carry central
air; water pressure; foundation and where water goes in a storm; shared driveway or lot
and who controls what; cell signal in the back room; how close the neighbors' windows
are; the commute at 8am.

**High-rise or condo.** Light at the hour they are actually home; noise with a window
open; cell signal in the bedroom; water pressure; storage beyond the closets; elevator
wait; distance from the elevator and the trash chute; the view from lying on the bed
rather than from the doorway; guest parking; hallway and lobby upkeep; what the dues
cover and what has been specially assessed; the dog route at 6am in the rain.

---

## Condition and upgrades

Seven systems, four states each (Updated / Original / Issue / Ask): foundation, roof,
sewer line, plumbing, electrical, HVAC, termite and pest. Three work items, same four
states (Yes / Partly / No / Ask): pre-inspections already done, kitchen remodeled,
bathrooms remodeled.

**None of it touches the score.** Fit and condition are different questions and the more
expensive one is condition. Say so on the page.

**"Ask" is a flag, not a shrug.** Everything marked Ask becomes the agent's follow-up
list with the listing agent, and it shows on the card as "3 to ask".

**Write the prompts for the local market, not generically.** Ask whether the foundation
is bolted and whether there is retrofit paperwork where that matters. Name the local
sewer pipe problem where there is one. Ask the panel amperage and say what it needs to
be. Ask who pays for pest clearance under the local custom. A generic prompt gets a
generic answer.

---

## Before it goes out

Four things stop a build. Each one has cost somebody something.

**Never score who lives somewhere.** The fair housing filter above runs on every list,
every time, including lists that arrive already written. An intake sheet handed to you is
not pre-cleared.

**Never guess a client's name.** If handwriting is unclear, leave names off the page and
ask. A wrong name in front of a client is worse than no name.

**Never use a photo you do not own.** Not the listing photos, not the portal, not street
view. All of those belong to somebody else and carry a visible or invisible claim.

**Never ask the agent for photos, and never leave an empty slot waiting for one.** The
tile is finished without a photograph. It draws a plate: the house number in the display
face inside a hairline frame, under a pediment for a house or a flat cornice for anything
stacked. That is the shipped look and a scorecard with no photograph anywhere on it is
complete.

Agent and buyer can each add one later if they want to, by tapping the small camera on a
tile and choosing a picture from the phone. The page resizes it and keeps it. Two things
to say plainly when it comes up, and never imply otherwise: a photo added on a phone
stays on that phone, so the agent's copy will not show the buyer's, and the agent adding
one is adding a photograph they took themselves.

**Never invent a criterion.** Everything scored traces to something the buyer actually
said. If a bucket is thin, say it is thin.

**Never say it is sent when it is copied.** The page cannot send anything. The button
copies and the page tells the buyer to paste it. Any wording that implies otherwise will
have a client believing their agent has the results while the agent has nothing.

---

## Tell every buyer these three things

- The answers live on whichever phone they are tapped into. **One phone, not two.**
  Private browsing or clearing site data wipes them.
- Nothing reaches the agent on its own. The copy button is the handoff.
- If the page is published through a hosted link, the viewer may see that host's banner
  above it.

---

## Building the page

`.claude/skills/showing-scorecard/assets/template.html` carries the whole page: scoring, two-person columns, deal-breaker
logic, the disagreement panel, the condition section, and the copy handoff. Replace every
`{{TOKEN}}`. The list below is in the template's own header comment, where the names are
written WITHOUT braces on purpose. Leave them that way. A token inside its own
documentation gets filled by the same replace that fills the real one, which quietly
writes a second copy of every list, the whole tour and the logo into that comment, and
corrupts anything that later reads the file back.

Array tokens take entries shaped `["Label","Hint, or an empty string"],`. The tour token
takes `{id:"slug", n:"123 Example St", facts:"Area · 3 bd 2 ba · listed $X", area:"City, ST",
type:"house"|"tower"},`. `type` decides the tile's mark: `"house"` draws a pediment,
`"tower"` a flat cornice, which is what makes a condo read differently from a house at a
glance. An optional `photo:"data:image/jpeg;base64,..."` replaces the plate, and is only
ever a picture the agent took. **Always fill `area`**, because the route and the per-stop
navigation links are built from the address plus the area, and an address alone sends
the buyer to the wrong city.
**The storage key is one per client and never changes.** Not per tour. It is what makes
their shortlist accumulate across weeks, and changing it erases everything they have
scored.

Mobile first. It is used standing up, one-handed, in somebody else's house. Check it at
phone width before handing it over, and open the finished link yourself once before
sending it.

---

## What the page does at the end of a tour

Three things that are not scoring, and they matter as much as the scoring.

**A route.** Every stop, in order, opened in Google Maps from one button. Per stop there
is also a Directions link and a Waze link, because Waze takes one destination at a time.
Order the tour in `{{TOUR}}` the way the agent is actually driving it.

**Skip.** A stop they drove past and did not go into gets skipped rather than deleted:
grayed on the list, out of the ranking, out of the route, out of the summary, and
reversible. The record that it was considered survives, which a delete would lose.

**A decision.** The page closes by asking which of four things today was: write on one,
see one again, keep looking, or sit with it. Whichever they pick travels in the summary
the agent receives. A tour that ends without a decision is the one that drifts into next
month.

## After the tour

The summary the buyer sends back is a record. Save it wherever that agent keeps notes on
the client. Two things in it are worth acting on the same day:

- Everything marked **Ask** is a question for the listing agent while the home is still
  fresh.
- Everything in the **disagreement** list is a conversation between the two buyers that
  will otherwise happen six weeks from now, during an inspection, badly.

---

## A worked example

`examples/example-scorecard.html` in the repository is a finished scorecard with every token filled, two
buyers, three stops, and one home knocked out by a deal-breaker. Open it before you
build your first one.

## Updating an installed copy

On **update my showing scorecard**: clone the repo fresh to a temporary folder, copy
`SKILL.md` and `assets/` over the installed ones, and delete the temporary folder. Never
touch `your-brand.json` or `clients/`. Say in one line what changed, reading the repo's
own recent history rather than guessing.

## Credit

Built by Sarah Arlington, Rooster Homes. Use it in your own business. Keep this line.
See LICENSE.
