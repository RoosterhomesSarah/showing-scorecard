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

```bash
git clone --depth 1 https://github.com/RoosterhomesSarah/showing-scorecard /tmp/ssc
mkdir -p .claude/skills/showing-scorecard
cp -R /tmp/ssc/.claude/skills/showing-scorecard/. .claude/skills/showing-scorecard/
cp /tmp/ssc/LICENSE .claude/skills/showing-scorecard/LICENSE
rm -rf /tmp/ssc
```

Your brand answers and your client folders are then created next to the skill, inside
your own setup, and stay on your computer.

---

## Door 2: open it as its own project

**For anyone who would rather keep it separate from everything else,** or who wants to
read it before trusting it.

```bash
git clone https://github.com/RoosterhomesSarah/showing-scorecard.git
```

Open that folder in Claude Code and say:

> set me up

Everything lives in the folder: the engine, your brand answers, and a folder per client.

---

## Updating, either way

Door 1: say **update my showing scorecard** and your AI pulls the newest version over
the old one. Your brand file and your clients are left alone.

Door 2: run `git pull` inside the folder.

---

## What it needs

Claude Code, and that is all. No account anywhere, no server, no subscription, nothing
to host, no dependency on any other system or any other skill. Your clients never leave
your machine.

---

Built by **Sarah Arlington**, Rooster Homes. Keep the credit line. Terms in
[LICENSE](LICENSE).
