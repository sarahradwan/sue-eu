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

## Session 3 — IELTS Academic

Opened July 2026. **This is a scholarship dependency, not a side project** — Swedish
master's admission closes mid-January 2027 and there is currently no English test.

```
Working on IELTS Academic. This is a requirement for my Route B
scholarship applications, not general English study.

Read CLAUDE.md and 06-ielts/README.md first. The README has the
target scores, the deadline and my profile — do not re-derive them.

This session owns 06-ielts/ ONLY. Do not edit anything in
01-relocation/ — two other sessions write there.

The situation:
- IELTS Academic, computer-delivered. Booking September 2026,
  sitting September-October 2026.
- Sweden needs 6.5 overall, no band below 5.5. I am aiming at 7.0+
  for headroom — some Erasmus Mundus consortia want 7.0.
- Hard downstream deadline: Swedish admission closes mid-January 2027.
- I have never sat IELTS.

About me, so you calibrate correctly: I am C2, native Arabic, and
have worked in English professionally for 22 years at creative
director level, presenting to ministers. My English is not the
problem. The exam format is. Do not waste my time on general
language study.

Start with a DIAGNOSTIC, not a study plan: give me one full timed
section under real exam conditions — start with Writing Task 1,
since Academic Task 1 is the format I have never written and the
most likely place I lose marks. Mark it against the official band
descriptors and tell me the band honestly, not encouragingly.

Then build the study plan around what the diagnostic actually shows,
not around what a generic IELTS course assumes.

Rules:
- Score me against the real band descriptors. An inflated practice
  band is worse than useless — it loses me a year.
- Time everything. Untimed practice does not measure anything.
- Write to 06-ielts/, not just to chat.
- CONFIDENTIALITY: nothing about this test goes anywhere public.
  An IELTS booking signals relocation and my employer watches my
  LinkedIn.
- git pull --rebase before committing, then push to
  claude/proactive-agent-setup-7f6r2m.

Report back: my current band, the single weakest thing, and what to
do this week.
```

**Follow-up lives in the scholarships session.** IELTS is tracked in
`01-relocation/pipeline-scholarships.md` as a hard dependency of the Swedish route. Report
band scores back to that session; the IELTS session does not touch relocation files.

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
