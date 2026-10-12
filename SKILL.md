---
name: showing-scorecard
description: Build a buyer a phone scorecard for a showing day, scored against what that buyer actually told you they want. Two people score independently on one phone so disagreements surface while they are still standing in the house, deal-breakers take a home out regardless of score, and the big systems get logged separately because condition is a different question from fit. No login for the buyer, nothing to host. Use when the agent says "build a tour scorecard for [client]", "showing scorecard for [client]", "we're seeing homes with [client] on [date]", "build the scorecard for [address]", or "add [address] to [client]'s tour".
version: 1.0
author: Sarah Arlington, Rooster Homes
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

---

## First run only: five questions

Check for `scorecard-brand.json` next to this skill. If it is missing, ask these five
and write the file. Never ask again.

1. What is your business name, as it should read on the page?
2. Two colors, as hex codes if you have them. One for headings and accents, one for the
   single action button. ("I don't know" is fine. Say so and use near-black `#1A1A1A`
   for headings and a deep blue `#1F4E79` for the button, and tell them where to change
   it later.)
3. Do you have a logo file? Give me the path. Square or near-square works best at phone
   size. (No logo is fine. The page sets your business name in type instead.)
4. The phone number a client should text you on.
5. The email address a client should send their results to.

```json
{
  "business_name": "",
  "agent_first_name": "",
  "color_accent": "#1A1A1A",
  "color_action": "#1F4E79",
  "logo_path": "",
  "phone_display": "",
  "phone_raw": "",
  "email": "",
  "footer_line": ""
}
```

A logo is embedded directly into the page as a data URI, resized to about 200px on its
long edge. A published page can only display an image that ships inside it, so a linked
logo will not render.

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
unsupervised; in the school attendance area they named; a place to work from home.
Breakers: busy street frontage; a pool they did not ask for. Nice: separate dining;
primary on the same floor as the kids; garage that fits two; flat lot.

**Downsizer.** Must: single level or a working elevator; primary bedroom on the entry
level; low maintenance outside; parking close to the door; in budget without touching
retirement funds. Breakers: stairs to the front door; a yard needing weekly work. Nice:
guest room; a spot for the grandkids; walkable to errands; a community with people around.

**Investor.** Must: the number works at their stated return; condition they are willing
to carry; rentable as-is or after the work they have budgeted; permitted square footage
matches the listing. Breakers: unpermitted additions; an HOA that restricts rentals;
pending litigation. Nice: separate entrance; existing tenant in place; room to add a unit.

**Relocation.** Must: commute they can live with on a real weekday; in budget; move-in
ready; enough bedrooms for whoever is arriving. Breakers: anything needing work before
they can move in; a commute over the number they named. Nice: furnished or partly;
short-term flexibility; near others who moved for the same reason.

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

A must-have is worth more than every nice-to-have combined, on purpose. If you change
these weights, keep that true, or the page will tell the buyer one thing while the number
tells them the opposite.

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

**Never guess a client's name.** If handwriting is unclear, leave names off the page and
ask. A wrong name in front of a client is worse than no name.

**Never use a photo you do not own.** Not the listing photos, not the portal, not street
view. All of those belong to somebody else and carry a visible or invisible claim. The
template draws its own property tiles. Use a real photo only when the agent took it
themselves, and then resize it before embedding.

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

`assets/template.html` carries the whole page: scoring, two-person columns, deal-breaker
logic, the disagreement panel, the condition section, and the copy handoff. Replace every
`{{TOKEN}}`. The list below is in the template's own header comment.

Array tokens take entries shaped `["Label","Hint, or an empty string"],`. The tour token
takes `{id:"slug", n:"Address", facts:"Area · type · detail", type:"house"|"tower"},`.
**The storage key must be unique per buyer per tour**, or two tours share one set of
checkmarks.

Mobile first. It is used standing up, one-handed, in somebody else's house. Check it at
phone width before handing it over, and open the finished link yourself once before
sending it.

---

## After the tour

The summary the buyer sends back is a record. Save it wherever that agent keeps notes on
the client. Two things in it are worth acting on the same day:

- Everything marked **Ask** is a question for the listing agent while the home is still
  fresh.
- Everything in the **disagreement** list is a conversation between the two buyers that
  will otherwise happen six weeks from now, during an inspection, badly.

---

## Credit

Built by Sarah Arlington, Rooster Homes. Use it in your own business. Keep this line.
See LICENSE.
