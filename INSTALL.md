# Install

Two ways in. Pick by how you work, not by how technical you are.

---

## Door 1: add it to the AI you already use

**For anyone who already has Claude Code open on a folder and does not want to think
about GitHub.** This is most people.

1. **Paste this into the Claude chat where you want to run scorecards:**

> Install the Showing Scorecard for me from
> https://github.com/RoosterhomesSarah/showing-scorecard

   Your AI fetches it and puts the skill where your setup keeps skills. About twenty seconds.

2. **Then say:**

> set up my showing scorecard

   Eight questions, about three minutes, and it builds your first one with you. It never
   asks again.

3. **For every buyer, say:**

> build a tour scorecard for the Hendersons

**To update later**, say **update my showing scorecard**.

### What your AI should actually do, if it asks

Describe the outcome, not the commands, so your AI uses whatever it is allowed to use:

> Download the repository archive (a `.tar.gz` file) into my setup folder and check it by
> listing what is inside it. Then extract only `.claude/skills/showing-scorecard/` into
> `.claude/skills/showing-scorecard/` in my setup (creating it if it is not there yet), and put
> the `LICENSE` file inside that same skill folder. Do not use a system temp folder and do not
> delete anything; leave the download where it is.

(The download is `https://github.com/RoosterhomesSarah/showing-scorecard/archive/refs/heads/main.tar.gz`.
Some setups refuse to delete files or to write outside your folder, which is why nothing here
needs either.)

Your brand answers and your client folders are then created next to the skill, inside
your own setup, and stay on your computer.

---

## Door 2: open it as its own project

**For anyone who would rather keep it separate from everything else,** or who wants to
read it before trusting it.

Clone the repository, open that folder in Claude Code, and say:

> set up my showing scorecard

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
