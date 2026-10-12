# Showing Scorecard

**Built by Sarah Arlington, Rooster Homes.**

Your buyer walks four houses on a Saturday. By Tuesday they remember the kitchen from the
second one and the yard from the fourth, and then they decide.

This is a skill for Claude Code that builds that buyer a page for their phone, scored
against what *they* told you they wanted. Not a generic checklist. Their list, in their
words.

---

## What the buyer gets

A link. No app, no account, no sign-in. They open it standing in the house.

- **Their own must-haves**, pulled from their consultation, each one worth more than
  every nice-to-have combined.
- **Two people score separately on one phone.** He taps his initial, she taps hers. The
  moment they disagree on something, the row lights up and the page keeps a count.
- **Deal-breakers take a house out.** A hard no marks it OUT no matter how well it scored,
  on the card, in the comparison and in what they send you.
- **The big systems logged separately** from fit: foundation, roof, sewer, plumbing,
  electrical, HVAC, pest, plus whether pre-inspections exist and what has been remodeled.
  None of it touches the score, because a house can hit 95% of what they want and still
  need a $30,000 sewer line.
- **One tap at the end** copies a summary they send you: both scores, what each of them
  found missing, what they disagree on, and every question to take back to the listing
  agent.

---

## What you get

A record of the showing that is better than your memory of it, and two things worth
acting on the same day: every item they marked **Ask**, which is your call list for the
listing agent, and every **disagreement**, which is a conversation that otherwise happens
six weeks later during inspection, badly.

---

## Install

**Needs Node 22 or newer** for the one-line installer. Check with `node -v`. On Node 20
the installer dies with a bare syntax error and no explanation, so use the clone method
below instead.

```bash
npx skills add -g RoosterhomesSarah/showing-scorecard
```

The `-g` matters. Without it the skill installs into whatever project folder you happen
to be in, which means a different copy, and a different set of setup questions, every
time you change folders.

Or clone it, which works on any Node version:

```bash
git clone https://github.com/RoosterhomesSarah/showing-scorecard.git ~/.claude/skills/showing-scorecard
```

Claude Code picks it up on the next session. Then say:

> build a tour scorecard for the Hendersons

**First time only, it asks you five questions:** business name, two colors, your logo,
your phone, your email. It writes those to one small file and never asks again. Every
scorecard after that is one sentence.

---

## You do not need to run buyer consultations to use this

Most agents do not run a formal one, and that is the whole reason this works the way it
does.

If you have consultation notes, point the skill at them, or photograph a handwritten
intake sheet and hand it over. That is the best result and the fastest.

If you do not, it asks you eight questions about the buyer and takes about three minutes.
You get the scorecard, and you also get a buyer consultation on file that you did not
have before. The next tour with that client starts from it.

If the buyer is already in your car, it starts from a buyer-type template, tells them
plainly that it is a starting point, and then asks you one question after the first stop
to sharpen it into their actual list.

Five buyer types ship with it: first-time, move-up family, downsizer, investor,
relocation.

---

## What it does not do

It does not send anything. The page cannot. Your buyer copies the summary and texts or
emails it to you, and the page says so plainly rather than pretending otherwise.

It does not host anything, store anything on a server, or need a database. Everything
lives on your buyer's phone until they send it to you.

It is not a CRM and it does not write to one.

It is not a seller-side or listing-presentation tool.

---

## Before you use it with a real client

Two things, and they are yours, not the skill's.

**Photos.** The template draws its own property tiles. Do not swap in listing photos, a
portal screenshot or street view. Those belong to somebody else. Use a photo only if you
took it.

**Compliance.** You are a licensed agent in a specific state under a specific brokerage.
Run this past your broker before a client sees it, the same as any other client-facing
material. The license is clear that this comes with no warranty and that part is on you.

---

## It stands on its own

It assumes no particular folder layout and no other skill being installed. It will read a
brand file if you point it at one, and it writes its own if you do not have one.

If your setup has a vetting step for skills from outside it, run this through it first.
That is the right habit with any repo you did not write, including this one.

---

## Updating

Pull the repo again. Your `scorecard-brand.json` is yours and is not overwritten.

```bash
cd ~/.claude/skills/showing-scorecard && git pull
```

The version is at the top of `SKILL.md`.

---

## License

Use it in your business, free, including with paying clients and with people you are
trying to win. The scorecards it produces carry your branding and are yours.

What you may not do is redistribute or sell the skill itself as your own work. Keep the
credit line on it. Full terms in [LICENSE](LICENSE).

---

Built by **Sarah Arlington**, Rooster Homes, Los Feliz, Los Angeles.
[roosterhomes.com](https://www.roosterhomes.com)
