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

## What never becomes a scored criterion

**Read this before you take a single must-have from anybody.**

A scorecard scores properties. The moment a criterion describes the people in an area
rather than the house itself, it stops being a property criterion, and it is now written
down, scored and emailed on a page carrying the agent's name.

So the transcription is filtered, every time, including a list the agent hands over
already written. Buyers say these constantly and almost none of them hear a problem in
it. Convert, never score.

| What they say | Why we convert it | What to write instead |
|---|---|---|
| "a safe neighborhood", "low crime" | describes people, not the property | nothing. Point them at the city's or police department's own public crime map and let them read it themselves |
| "good schools", "a good school district" | a reputation, not a property fact | the named attendance boundary as a boundary: "inside the Lincoln Elementary attendance area". Never a rating, never "good" |
| "a family neighborhood", "family friendly" | describes who lives there | the property facts they actually want: a fenced yard, a second bedroom, a park within a ten minute walk |
| "near our church" / "temple" / "mosque" | describes the household, not the home | a drive time to one specific address they give you: "under 15 minutes to 412 Oak Street" |
| "not a lot of renters", "mostly owners" | describes the neighbors | nothing. Who owns the homes nearby is not a feature of this one |
| "people like us", "somewhere we'd fit in" | describes residents | ask what the home needs to have, and write that |
| "up and coming", "the right side of town" | describes an area's people | the specific thing underneath it: new construction nearby, a commute time, a price trend they can look up |
| "quiet, no kids around" | describes the neighbors | the property fact: not backing a playground, a corner lot, double glazing |
| "a walkable, diverse area" | sounds positive, still describes residents | walk score, a named amenity, a drive time |

### How to handle it in the moment

Do not lecture the agent and do not refuse to build. Convert, then say one line so they
learn it too:

> "I left 'good schools' off the scored list and put 'inside the Lincoln Elementary
> attendance boundary' instead. A reputation is not a property fact; a boundary is. If
> they meant something else by it, tell me."

If a stated criterion has no property-fact equivalent, say so plainly and leave it off. A
short list that can be defended beats a long one that cannot.

### The same filter runs on

The eight-question interview, especially question six. The starter sets. The hint text
under any item. The brief line at the top of the page. And the buyer's own free-text
notes, which arrive in the summary: if that language comes back, tell the agent before it
goes into a file or a CRM.

### Your broker is the authority

This is how the tool behaves. It is not advice about the law, and nothing here is legal
advice. Fair housing rules differ by state and most brokerages have their own on top of
them, so run your criteria past your broker and work from your own state association's
current advisory. The agent is responsible for everything that goes out under their
license.

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

**Say this once, at the end of setup, and never again.** An installed copy is a copy on
their computer; it does not change when the original does. So in one line: *"This is
yours now and it stays as it is. When you hear there is a new version, say **update my
showing scorecard** and I will pull it. Your answers here and your client folders are
never touched."* Then stop and build their first scorecard.

---

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

This rebuild is a two-minute job the night before a showing day. Frame it to the agent
that way: it sits in the same slot as the prep they already do, and it replaces printing
listing sheets rather than being added on top of it.

**Where the file goes.** Every scorecard goes to
`clients/<client-slug>/YYYY-MM-DD-scorecard.html`, under whichever `clients/` location
the install check above settled on, and the criteria you worked from go beside it as
`criteria.md`. The date in the filename is a version stamp rather than a separate
scorecard: the newest file is the live one and the earlier ones are history worth
keeping. Create the client folder if it is not there.

When the buyer sends their results back, save those too, as `YYYY-MM-DD-results.md` in
the same folder. **Keep the whole message, including the backup code at the bottom.**
That code is the client's only copy of their own scoring if their phone is ever lost; see
the section below.

---

## One phone between two buyers

**The page saves to whichever phone the tap happened on, and nothing syncs.** With two
buyers, that makes one phone the only correct way to use it. Two people on two phones
each end up with half the picture, and nothing warns them, because each phone looks
complete on its own.

The page says this at the top of the stops list whenever there are two names, so the
agent does not have to remember to. The agent should say it out loud anyway when they
hand the link over: *one phone, pass it back and forth, tap your own initial.*

---

## The backup code

Everything the buyer taps lives in that one phone's storage. A cleared browser, a private
window or a new handset wipes it with nothing to recover from.

So the summary the buyer sends their agent ends with a short backup code, a few hundred
characters, carrying every tick, note, gut score and condition answer. It rides inside a
message they already send, which makes the agent the backup without either of them doing
anything extra.

**What to tell the agent:** keep the whole message, including the ugly line at the
bottom. If the buyer ever loses their phone, send that code back. They paste it into
**If You Lose This Phone** at the end of Compare and the whole search returns.

The code carries a fingerprint of the criteria lists. If the agent has since rebuilt the
scorecard with a changed list, the page refuses the code and says so rather than quietly
restoring the answers against the wrong questions. Photos the buyer added do not travel
in the code; everything else does.

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

**Never score who lives somewhere.** The criterion filter above runs on every list,
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

## Finish the handoff. Never stop at a file.

**A built file is not a delivered scorecard, and this is where a new agent gives up.** Do
not end a build by naming a path. Walk them all the way to a link their buyer can open,
and then hand them the words to send. Every build, including the first one.

**1. Show them it works, in a real browser.** Open the finished file in their actual
browser, so they see their own colors and their own name before anyone else does. Then
tell them where it is, and offer to reveal it in Finder or Explorer so they can find it
to drag.

**Say this out loud, because it will otherwise cost them an hour:** a preview pane inside
a chat app or an editor is not a browser. It cannot follow a maps link, a text link or an
email link, and it will look like the scorecard is broken when the scorecard is fine. If
they are testing, they open it in Chrome or Safari, or better, they finish step 2 first
and test the real link on a real phone. Those buttons hand off to the phone's own maps,
messages and mail apps, and only a real browser on a real device can do that.

**2. Turn it into a link.** Say these steps in this order:

> - Make a new folder and name it after the client, like `hendersons`.
> - Put the scorecard inside it and rename the file `index.html`. That one rename is what
>   gives you a clean link instead of a long one.
> - Go to **netlify.com** and make a free account. It takes a minute and no card. Do this
>   first, because a site made while signed in stays yours and you can drop updates onto
>   the same address forever.
> - Go to **netlify.com/drop** and drag the whole folder onto the page.
> - It hands you back a link. That is the client's scorecard.

Then ask them to paste that link back to you.

**Then open that live link yourself, on a phone-width screen, before anybody sends it.**
A file that worked on their laptop is not a link that works on a phone until you have
looked.

**If the agent already has a website or a page builder**, it goes there instead, under
their own domain, and that is better still.

**Make it a QR code too.** Half of this is handing a phone to somebody standing next to
you. Any free QR generator takes the link.

**3. Write the message.** With the link in hand, draft the text to the buyer, in the
agent's own voice, ready to send. It has to carry the three things the buyer will not
work out on their own:

> Hi Jo and Pat, here's your scorecard for Saturday. Open it on one phone between the
> two of you and keep that phone handy as we walk through each house. You'll each have
> your own column, so tap your own initial. At the end there's a button to send me the
> results, and please send the whole thing including the code at the bottom. That code is
> your backup if anything ever happens to your phone. Bookmark the link, it's the same
> one all the way through your search.

Say plainly that the agent sends it, not you.

**4. Say what happens next tour.** One line: *"When you book another day with them, say
add the new addresses to the Hendersons' scorecard. I rebuild it, you drag the folder onto
the same Netlify site, and their link never changes."*

**If they will not set up hosting at all,** email or text the file as an attachment
instead. It works, the buyer opens it from their mail app, and the cost is a new
attachment every tour and a buyer hunting for the newest one. Offer it as the fallback,
not the first answer.

---

## Tell every buyer these four things

- **One phone, not two.** The answers live on whichever phone they are tapped into, and
  nothing syncs. Two people on two phones end up with half the picture each.
- **Nothing reaches the agent on its own.** The button at the end is the handoff, and the
  buyer has to press send in their own app.
- **Send the whole message, backup code and all.** The ugly line at the bottom is the
  only copy of their scoring that exists anywhere but that phone. The agent keeps it and
  can hand it back.
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
type:"house"|"condo"},`. `type` draws the tile: both are the same hairline elevation,
walls on an overhanging eave, and they differ at the roof, pitched for a house and flat
with a parapet for anything stacked. That is what makes a condo read differently from a
house before the buyer has read a word. Write the word you would say out loud; `condo`,
`apartment`, `loft`, `high-rise`, `co-op` and `unit` all draw the stacked one, and
`townhouse`, `bungalow`, `duplex` and anything unrecognized draw the house. An optional
`photo:"data:image/jpeg;base64,..."` replaces the elevation, and is only ever a picture
the agent took. **Always fill `area`**, because the route and the per-stop
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

Four things that are not scoring, and they matter as much as the scoring.

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

**A backup.** The summary ends with a code carrying everything they have tapped, and
Compare has a panel to paste one back in. See **The backup code** above. The agent holding
that message is the difference between a lost phone costing an afternoon and costing six
weekends.

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

**Nothing updates on its own.** An installed copy is a copy on that agent's computer. The
original moving does not move it, and there is no phoning home, on purpose: this skill
makes no network request of its own and never reports that it is being used.

On **update my showing scorecard**: clone the repo fresh to a temporary folder, copy
`SKILL.md` and `assets/` over the installed ones, and delete the temporary folder. Never
touch `your-brand.json` or `clients/`. Say in one line what changed, reading the repo's
own recent history rather than guessing.

Scorecards already built and already sent are finished files and do not change either. An
update reaches a client only the next time their scorecard is rebuilt, which is what a new
showing day does anyway.

## Credit

Built by Sarah Arlington, Rooster Homes. Use it in your own business. Keep this line.
See LICENSE.
