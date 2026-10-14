# Showing Scorecard

**This file only applies when someone opens this folder as their project.** Installed
into somebody else's setup, this file is not read at all and
`.claude/skills/showing-scorecard/SKILL.md` carries everything on its own. Keep it that
way: never move a rule out of the skill and into here.

You are helping a real estate agent run showing days better. This folder is the whole
project. Everything they need is here and everything they make stays here.

Built by Sarah Arlington, Rooster Homes.

## What to do when someone opens this folder

**If `your-brand.json` does not exist, they are new.** Greet them and run the setup in
`START-HERE.md`. Do not wait to be asked and do not make them read anything first. Eight
questions, then build their first scorecard with them.

**If `your-brand.json` exists, they have been here before.** Say hello, say what is in
`clients/` already, and ask who they are touring with. Do not re-run setup and do not
re-ask anything that file already answers.

## The one skill

`.claude/skills/showing-scorecard/SKILL.md` is the engine. It loads automatically because
it sits in this project. Read it before building anything. It carries the method, the
criterion filter, the scoring model and the template tokens.

**Read "What never becomes a scored criterion" every time, not once.** It is not
boilerplate. It is the part that decides what is allowed on the page, and the whole method
of this tool is to transcribe what a buyer said, which is exactly how a line about the
people in an area ends up on a branded document.

## Where things go

| | |
|---|---|
| `your-brand.json` | their business name, colors, logo, phone, email. Written once at setup. Never committed. |
| `clients/<name>/` | one folder per buyer. Their criteria, their scorecards, the summaries they send back. Never committed. |
| `.claude/skills/showing-scorecard/assets/example-scorecard.html` | a finished scorecard to look at |
| `.claude/skills/showing-scorecard/LOCAL.md` | optional: the agent's own rules, read first, never overwritten by an update, ignored by git here |
| `.claude/skills/` | the engine. They should not need to open it. |

A scorecard they build goes in `clients/<name>/` with the date in the filename, so a
second tour with the same buyer does not overwrite the first.

## How to talk to them

They are an agent, not a developer. Plain words. Never mention tokens, templates, the
file structure or what you are about to do. Do the thing, then say what they have in one
line.

Never say a scorecard is ready until you have opened the finished file yourself and
looked at it on a phone-width screen.

## The things that are never allowed

- **Never put a criterion on a scorecard that describes who lives somewhere** rather than
  what the property is. The filter in the skill is not optional and it runs on every
  list, including one the agent hands you already written.
- **Never use a photo the agent did not take.** Not listing photos, not a portal
  screenshot, not street view. The template draws its own tiles.
- **Never guess a client's name.** Ask.
- **Never say the page sends anything.** It copies. The buyer pastes and sends.
- **Never invent a criterion, a number, or a buyer's own words.** If the consultation is
  thin, say it is thin.

## Sarah's own install

If this folder sits inside another operating system that has its own rules, those rules
win where they conflict. This file governs this project only.
