# Session starter prompts

Copy-paste these when opening a new session on this repo.

## What you do NOT need to explain

Any session started **in this repo** reads `CLAUDE.md` automatically. It already knows:

- Who you are, your career history, the full CV
- The goal, both routes, and your country preferences
- **The confidentiality rule** — that your employer monitors your LinkedIn
- Your eligibility filter and the €2,000 tuition ceiling
- The 2027 timeline
- All eight skills

So do not re-explain your situation. Just say what you want done. If a session ever seems
unaware of any of the above, it is not reading `CLAUDE.md` — tell it to read that file first.

---

## Session 1 — Jobs (Route A)

```
Working on Route A: EU jobs with visa sponsorship.

Read CLAUDE.md, 01-relocation/eligibility-filter.md and
01-relocation/timeline-to-2027.md first.

This session owns 01-relocation/pipeline-jobs.md — do not edit
pipeline-scholarships.md, another session owns it.

Priority order:
1. Permit routes that do NOT require an employer sponsor (job-seeker
   visas, orientation-year permits, talent routes). Highest leverage —
   these change what I can even apply to. Netherlands first.
2. Employers that verifiably sponsor — national sponsor registers are
   more reliable than job boards.
3. Specific roles at director/senior level in English.

Rules:
- Never call something sponsored unless the source says so explicitly.
  Mark anything unstated as unverified.
- Capture every deadline.
- Write findings to pipeline-jobs.md and country-notes.md.
- git pull --rebase before committing, then push to
  claude/proactive-agent-setup-7f6r2m.

Start with the highest-leverage item and report back short:
what's new, what's closing, one next action.
```

---

## Session 2 — Scholarships (Route B)

```
Working on Route B: funded study in the EU.

Read CLAUDE.md, 01-relocation/eligibility-filter.md and
01-relocation/timeline-to-2027.md first.

This session owns 01-relocation/pipeline-scholarships.md — do not edit
pipeline-jobs.md, another session owns it.

Qualifies if: fully funded, or first year covered, or housing + some
food, or tuition under EUR 2,000/year for non-EU students.

Priority order:
1. Scholarship schemes that fund MID-CAREER professionals, not just
   recent graduates. Check age and experience criteria explicitly —
   my 22 years disqualifies me from some schemes and favours me in
   others. This is what kills most leads, so check it first.
2. Public universities where NON-EU tuition is at or under EUR 2,000/year
   (check the non-EU fee, not the EU fee — they differ a lot).
3. English-taught master's relevant to brand, marketing, design or
   creative leadership.

Timeline pressure: Sept 2027 intake applications generally open
Oct-Nov 2026 with deadlines Nov 2026 - Jan 2027. Flag anything whose
window opens within 60 days.

Rules:
- Never call something funded unless the source states the scheme,
  amount and deadline. Otherwise mark unverified.
- Confirm the programme leads to a residence permit.
- Write findings to pipeline-scholarships.md and country-notes.md.
- git pull --rebase before committing, then push to
  claude/proactive-agent-setup-7f6r2m.

Start with priority 1 and report back short.
```

---

## Why the split

Both sessions push to the same branch. Two things prevent collisions:

1. **Separate files.** Jobs session owns `pipeline-jobs.md`; scholarships session owns
   `pipeline-scholarships.md`. Both may add to `country-notes.md` — that is the one shared
   file, so pull before editing it.
2. **`git pull --rebase` before every commit.** Both prompts include this. If a push is
   rejected, that is the fix.

## Other sessions worth opening

**CIM** — `Working on my CIM Level 7. Read CLAUDE.md, then
02-cim-level-7/module-tracker.md. [what you need]`

**Applications** — `I'm applying to [X]. Read CLAUDE.md and use the application-tailor
skill. Here's the posting: [paste]`

**Portfolio / LinkedIn** — `Working on my [website / LinkedIn]. Read CLAUDE.md and use the
stealth-positioning skill. Remember my employer watches LinkedIn.`

**Interview** — `I have an interview with [X] on [date]. Read CLAUDE.md and use the
interview-prep skill.`

## One rule for every session

Anything public — LinkedIn, portfolio, bios — follows `stealth-positioning`. Nothing may
suggest you are planning to leave. Private applications are different: there, be completely
straightforward about needing sponsorship.
