# Install

Two ways in. Pick by how you work, not by how technical you are.

---

## Door 1: add it to the AI you already use

**For anyone who already has Claude Code open on a folder and does not want to think
about GitHub.** This is most people.

Paste this one line into your chat:

> Install the Showing Scorecard for me from
> https://github.com/RoosterhomesSarah/showing-scorecard

Your AI does the rest: it fetches the repo, puts the skill where your setup keeps skills,
and cleans up after itself. Takes about twenty seconds.

Then say:

> set up my showing scorecard

Seven questions, about three minutes, and it builds your first one with you. It never
asks again.

After that, for every buyer:

> build a tour scorecard for the Hendersons

### What your AI should actually do, if it asks

Describe the outcome, not the commands, so your AI uses whatever it is allowed to use:

> Shallow-clone the repository to a temporary folder. Copy the contents of
> `.claude/skills/showing-scorecard/` into `.claude/skills/showing-scorecard/` in my
> setup, plus the `LICENSE` file beside it. Delete the temporary folder.

Your brand answers and your client folders are then created next to the skill, inside
your own setup, and stay on your computer.

---

## Door 2: open it as its own project

**For anyone who would rather keep it separate from everything else,** or who wants to
read it before trusting it.

Clone the repository, open that folder in Claude Code, and say:

> set me up

Everything lives in the folder: the engine, your brand answers, and a folder per client.

---

## Updating, either way

Say **update my showing scorecard**. Your brand file and your clients are left alone.

## If your setup vets incoming skills

Good. It should, and this one is written to pass. It has no hooks, no scheduled jobs,
nothing that sends anything anywhere, and the only outbound request any page makes is
for the Google Fonts stylesheet, which the page discloses to the buyer.

The one thing a scanner may flag is the deletion of the temporary download folder during
install. That is housekeeping, and it is also why the step above is written as an
instruction rather than a command to paste, so your own setup decides how to do it.

---

## What it needs

Claude Code, and that is all. No account anywhere, no server, no subscription, nothing
to host, no dependency on any other system or any other skill. Your clients never leave
your machine.

---

Built by **Sarah Arlington**, Rooster Homes. Keep the credit line. Terms in
[LICENSE](LICENSE).
