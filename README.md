# Showing Scorecard

**Built by Sarah Arlington, Rooster Homes.**

A page for your buyer's phone that they open standing inside a house, and score that
house against what *they* told you they wanted. Not a generic checklist. Their list, in
their words.

---

## Get it

**Paste this one line into the Claude Code chat you already have open.** The whole line,
link included.

**1. Paste this into the Claude chat where you want to run scorecards** (your BOSS chat works):

```
Install the Showing Scorecard for me from https://github.com/RoosterhomesSarah/showing-scorecard (its INSTALL.md says how)
```

**2. Then say:**

```
set up my showing scorecard
```

Eight questions, about three minutes. Then, when you have a tour coming up, it builds your
first scorecard with you in your own colors and your own name. You never touch GitHub again and you never leave your chat.

**3. For any buyer, say:**

```
build a tour scorecard for the Hendersons
```

**To update later**, say **update my showing scorecard**. Your settings and your clients are
left alone. Nothing updates on its own.

**Forgot the words?** You do not need them exactly. Once it is installed, say what you are
actually doing, like *"I'm showing houses to the Hendersons on Saturday, make them a
scorecard"*, and it will know. If you are stuck, ask *"how do I use my showing
scorecard?"* and it will tell you.

**Prefer it as its own folder?** Clone this repo, open that folder in Claude Code, and say
**set up my showing scorecard**. Both doors are in [INSTALL.md](INSTALL.md).

---

## Questions people ask

**How do my buyers get it?** Your AI walks you through it, one step at a time: a free Netlify
account in your name, dragging one zip file it makes for you onto a web page, renaming the site, and making the link public so your
buyer does not hit a login screen. You get back a link to text your buyer. Each buyer keeps the
same link for their whole search.

**What do I give my AI for a buyer?** The tour date, each home's address and city, beds, baths and
list price, and whether each is a house or a condo. It uses what the buyer told you they want. If
you do not have that written down, it asks you eight quick questions about the buyer.

**Can I do it in Spanish?** Yes. Tell your AI the buyer prefers Spanish and the page opens in
Spanish; buyers can switch with the ES / EN button at the top. The summary they send you stays in
English. The page says the Spanish was translated with a tool; once a Spanish speaker has read it
you can turn that line off (the `ES_NOTE` setting).

**What does it look like?** Say **show me the example scorecard**. It has a made-up couple and
made-up homes, so you can tap anything.

**My system warns that the page "sends email".** That is the Text and Email buttons. They open the
buyer's own messaging app with the summary filled in; the buyer is the one who presses send. The
page cannot send anything on its own.

**How do I tell Sarah what's working and what isn't?** Say **send feedback on my showing
scorecard**. Your AI writes up what it noticed, with nothing about your clients, shows it to you,
and opens a form on GitHub for you to send. It goes on a public page, so it never carries anything about your clients. It also offers, at most once a week, if it noticed
something worth sending. Say **stop asking about feedback** and it won't.

**If I update it, do I lose my settings?** No. Your brand answers and your client files stay. If
you want your own rules for how it works, put them in a file called `LOCAL.md` in the skill folder:
it is read first, wins where it disagrees (it cannot weaken the safety rules), and an update never touches it.

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

A self-contained project folder. No server, no subscription, and the only host is a free Netlify site in your name,
and no dependency on any other system. Your clients and your brand answers stay on your
machine.

If your setup has a vetting step for repos from outside it, run this through it first.
That is the right habit with any repo you did not write, including this one.

---

## Updating

Say **update my showing scorecard**. Your brand answers and your client folders are left
alone.

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
