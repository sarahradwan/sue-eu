---
name: skill-retro
description: Audit and improve the skills in this repo based on what actually worked or failed. Use monthly, or when a skill produced a bad result, or when Sara says a skill should work differently. This is the safe, reviewable alternative to a self-rewriting agent.
---

# Skill retro

How this setup improves over time — deliberately, visibly, and under Sara's control.

## Why it works this way

Sara asked for a self-improving agent that would not cause problems long-term. Systems
that silently rewrite their own instructions fail in a specific and nasty way: they drift.
Small unreviewed edits compound, and by the time the behaviour is obviously wrong, nobody
can tell which change caused it or what the instructions used to say. The failure is
invisible until it is expensive.

So improvement here is **git-based**:

- Every skill is plain markdown in version control.
- Every change is a commit with a reason — visible, attributable, reversible.
- Nothing changes silently. Sara can read the diff, and `git revert` undoes any regression.

This is slower than autonomous self-modification and far more durable. It compounds
without drifting, which is what "no issues in the future" actually requires.

## When to run

- **Monthly**, as a standing review.
- **Immediately** when a skill produces a bad result — that is the highest-signal moment
  and the detail is fresh.
- When Sara says something should work differently.
- When circumstances change: a country decided, an offer landing, CIM completing, German
  reaching a new level, or leaving WeDo (which would retire the confidentiality rule).

## The process

**1. Gather evidence.** What actually happened? Concrete cases only — a lead that wasted
her time, a deadline missed, advice that did not fit, a check-in she ignored. "Could be
better" is not evidence and produces vague edits that make skills worse.

**2. Diagnose honestly.** Was the skill wrong, missing, too vague, or contradicted by
another skill? Or did the skill work correctly and the situation was simply hard? Not
every bad outcome is an instruction defect. Editing a correct skill because of an
unlucky week is how instruction sets rot.

**3. Change one thing.** Small, specific edits. A skill rewritten wholesale cannot be
attributed when the next problem appears.

**4. Commit with the reason.** The commit message records *why*, not just what:

```
skill(eu-opportunity-scout): require explicit sponsorship wording

Three January leads said "international team" and none sponsored.
Sara spent an evening on applications that could not have worked.
```

Six months on, that message explains the rule. Without it the rule looks arbitrary and
someone deletes it.

**5. Tell Sara what changed** and why, in one line. Never make a behavioural change she
does not know about.

## What to check each retro

| Question | Looking for |
|---|---|
| Which skills fired when they should have? | Description fields that fail to trigger |
| Which fired when they shouldn't? | Descriptions too broad |
| Did any leads waste her time? | Filter needs tightening |
| Did anything qualify that was rejected? | Filter too narrow |
| Any near-miss on the LinkedIn rule? | Highest-severity — treat as urgent |
| Is the vault still being written to? | Findings decaying into chat only |
| Are the check-ins useful or ignored? | Cadence or content wrong |

## The one rule that never gets relaxed

The LinkedIn confidentiality rule in `CLAUDE.md` may be **tightened** by a retro, never
loosened — unless Sara explicitly says her situation has changed (she has left WeDo, or
told her employer). The cost of that rule failing is her job. It is not a candidate for
optimisation.

## Adding new skills

Only when a real, repeated need appears. Each skill costs attention every session; a
sprawling set of half-used skills is worse than four sharp ones. A skill earns its place
by being used.

Before adopting anything external, audit it: does it match her actual work, is it
maintained, does it conflict with the confidentiality rule? `superpowers` was rejected at
exactly this step — a coding-team methodology, not a creative-practice system. Fit beats
popularity.
