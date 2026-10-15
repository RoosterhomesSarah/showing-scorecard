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

   Eight questions, about three minutes, then it builds your first one with you when you
   have a tour coming up (or shows you the example). It never asks again.

3. **For every buyer, say:**

> build a tour scorecard for the Hendersons

**To update later**, say **update my showing scorecard**.

### What your AI should actually do, if it asks

Describe the outcome, not the commands, so your AI uses whatever it is allowed to use:

> Create `.claude/skills/showing-scorecard/` in my setup. Working inside that folder, download
> the repository archive (a `.tar.gz` file) there as `showing-scorecard-install.tar.gz`, check
> it by listing what is inside it, then extract only the archive's
> `.claude/skills/showing-scorecard/` contents into that folder, plus the `LICENSE` file. Do
> not use a system temp folder and do not delete anything; leave the download where it is.

(The download is `https://github.com/RoosterhomesSarah/showing-scorecard/archive/refs/heads/main.tar.gz`.
Some setups refuse to delete files or to write outside your folder, which is why nothing here
needs either.)

Your brand answers and your client folders are then created inside the skill's own folder,
and stay on your computer.

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

Want your own rules for how it works? Put them in a file called `LOCAL.md` in the skill folder. It is read first and an update never touches it.

## If your setup vets incoming skills

Good. It should, and this one is written to pass. It has no hooks, no scheduled jobs,
nothing that sends anything anywhere, and the only outbound request any page makes is
for the Google Fonts stylesheet, which the page discloses to the buyer.

Nothing in the install or the update deletes anything, and both write only inside your own
folder.

---

## What it needs

Claude Code, and that is all. No server, no subscription, no dependency on any other system or
any other skill. Your client files stay on your computer, and a new install keeps them out
of a git backup your setup makes. The one thing that goes online is the scorecard page itself, on a free Netlify site in
your name, when you choose to share it.

---

Built by **Sarah Arlington**, Rooster Homes. Keep the credit line. Terms in
[LICENSE](LICENSE).
