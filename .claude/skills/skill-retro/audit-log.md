# Skill audit log

Every external skill considered, and why it was adopted or rejected. Kept so the reasoning
survives — a rule with no recorded reason looks arbitrary later and gets deleted by someone
who does not know what it was protecting against.

---

## 2026-07-25 — First external audit

Sources reviewed: [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
(ComposioHQ), [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)
(Paramchoudhary, MIT, ~1.3k stars, 20 skills),
[proficiently-claude-skills](https://github.com/proficientlyjobs/proficiently-claude-skills)
(MIT, ~300 stars), [obra/superpowers](https://github.com/obra/superpowers),
[mksglu/context-mode](https://github.com/mksglu/context-mode),
[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian).

### Rejected

**`linkedin-profile-optimizer`** (ResumeSkills) — **conflicts with a safety rule.**
Generic LinkedIn optimisers push "open to opportunities", `#OpenToWork`, and
location changes. Sara's employer monitors her LinkedIn; that advice could cost her
her job. The capability she needs is the inverse — visibility to recruiters *without*
intent signals — which `stealth-positioning` already does. Do not reconsider while she
is still at WeDo.

**`resume-quantifier`** (ResumeSkills) — partially rejected. Bullet quantification is
sound, but the skill explicitly offers to "estimate when numbers unknown". Estimated
metrics on a CV are fabrication, and checkable. Her real numbers are strong enough.
The honest half was folded into `application-tailor`.

**`proficiently-claude-skills`** — mostly rejected. Requires the Claude in Chrome
extension and a Telegram loop; heavy external dependency for uncertain benefit.
`apply` auto-fills Greenhouse/Lever/Workday forms — inappropriate for applications she
must be able to stand behind. `network-scan` works through LinkedIn contacts, which is
the exact surface her employer watches.

**`obra/superpowers`** — rejected on fit. Presented as a self-improving skills system;
it is a software-engineering methodology (TDD, RED-GREEN-REFACTOR, PR workflows, subagent
code review). Nothing maps to brand strategy, relocation or study. Its genuinely good
idea — that process should be explicit and versioned rather than ad hoc — was taken and
applied in `skill-retro`.

**`mksglu/context-mode`** — rejected on fit. Token/context-window optimisation for coding
agents (sandboxed tool output, SQLite session persistence). Real engineering, wrong domain.

**`obsidianmd/obsidian-releases`** — not applicable. It is the official plugin/theme
*directory*, not a knowledge-base tool. Nothing to adopt.

### Adopted, adapted

**ATS optimisation** → `application-tailor`. Genuine gap. Audit of her actual CV file
found **two 2-column tables** (the "Across Brand, Experience & Technology" panels and the
Skills grid) plus contact details in a header — all common ATS parse failures. No text
boxes or images, so it is fixable. Resolved with a two-document rule: designed CV for
humans, single-column CV for parsers.

**Job-description analysis and CV tailoring** → `application-tailor`, tightened to her
eligibility filter and with an explicit no-fabrication rule.

**Interview prep / STAR** → `interview-prep`, plus the questions generic skills never
cover: why leave the UAE, sponsorship needs, no EU experience, scholarship at 22 years'
experience, and the UAE-vs-EU salary trap (tax-free gross figures are not comparable).

**Portfolio case study writing** → `case-study-translator`. The highest-value adaptation.
Generic versions assume the reader recognises the client. Hers will not — the skill exists
to make MENA-institutional work legible to EU readers without inflating it.

**`AgriciDaniel/claude-obsidian`** — pattern adopted, code not installed. Actively
maintained (~9.8k stars, MIT, tested). Its structure — plain-markdown vault, index, session
cache — is what this repo already implements. Installing the full plugin is worth
revisiting only if the vault grows past what plain files handle well. Adding a dependency
now would cost more than it returns.

### Net result

Five skills → eight. New: `application-tailor`, `interview-prep`, `case-study-translator`.

### Notes for the next retro

- Watch whether `application-tailor` and `case-study-translator` overlap in practice. If
  she keeps invoking both together, merge them.
- The ATS-safe CV variant does not exist yet — it is a described standard, not a file.
  Build it before the first online application, not during one.
- Revisit `salary-negotiation-prep` (ResumeSkills) at offer stage. Not needed yet, and
  skills that sit unused cost attention every session.
