# Releasing (for Sarah)

Agents install and update from **releases**, never from work in progress. GitHub runs the tests on
every push to main and emails you if one fails; a release is published only when the tests pass on
the exact commit you release.

**For now, keep main release-ready.** Agents who installed before releases existed take main one
last time on their next update, and only use releases after that. Until those updates have
happened, push to main only what you are about to release.

**To release:** say **release my showing scorecard**. Your AI will:

1. Confirm `git status` is clean and the tests pass here (`python3 tests/hostile.py`,
   `python3 tests/spanish.py`).
2. Give you `git push` for main, wait for GitHub's run on main to pass
   (`gh run list --workflow tests-and-release.yml --branch main --limit 1`, then
   `gh run watch <id> --exit-status`), and stop if it fails.
3. Write two to four plain-English lines on what changed for agents, and make the tag on that
   exact commit: `git fetch origin && git tag -a v2026.10.15 origin/main -m "<those lines>"`. Name
   it for today; add `.2` for a second release the same day.
4. Give you the one line to push it: `git push origin v2026.10.15`
5. Watch that tag's run (`gh run list --workflow tests-and-release.yml --branch v2026.10.15`, then
   `gh run watch <id> --exit-status`) and confirm the release itself exists:
   `gh release view v2026.10.15 --json assets --jq '.assets[].name'` must print
   `showing-scorecard-skill.tar.gz`. Only then say it is released.

If the tests fail on GitHub, nothing is published and every agent keeps what they have. Fix it and
release with a new tag.

**Never** move, re-push or reuse a tag, and never create a release by hand on GitHub's page:
either one leaves agents a "latest" release with nothing to download.

**Rolling back:** an agent who hits a problem says "go back to the previous version of my showing
scorecard". To pull a bad release for everyone, delete that release on https://github.com/RoosterhomesSarah/showing-scorecard/releases; the one before it
becomes the latest again, and agents on the bad one move back on their next update.

**One-time setup on this computer:** pushing the file that runs the tests needs GitHub's
`workflow` permission: `gh auth refresh -h github.com -s workflow`, approved in the browser.
