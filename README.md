# sue-eu

Sara Radwan's working vault and agent setup. Goal: **relocate to the EU** via a job with
visa sponsorship or a funded scholarship.

Plain markdown throughout — open this folder directly as an Obsidian vault, or work in it
through Claude. Both read and write the same files.

## Start here

- **`CLAUDE.md`** — how the agent works, and the confidentiality rule. Read first.
- **`01-relocation/eligibility-filter.md`** — what counts as a real opportunity.
- **`05-career-context/cv-source-of-truth.md`** — the master CV.

## Structure

| Folder | Contents | Track |
|---|---|---|
| `01-relocation/` | Eligibility filter, roadmap, job and scholarship pipelines, country notes | **Primary** |
| `02-cim-level-7/` | Module tracker, assignments, marketing theory | Secondary |
| `03-german/` | Learning log, vocabulary | Secondary |
| `04-portfolio-positioning/` | Website plan, LinkedIn strategy and content system | Supporting |
| `05-career-context/` | CV source of truth, tailored CVs, application history | Supporting |
| `06-ielts/` | English test prep, where a programme or permit requires it | Supporting |
| `07-afrilink/` | Venture evaluation. Feasibility and profit potential | Side |
| `08-uae-income/` | The UAE salary track. Raise, or a better-paying UAE role | Income |
| `09-egypt-and-remote/` | Egypt roles, and remote work paid in USD | Income |
| `10-book/` | *Notes from a Life I Didn't Plan*. Memoir in essays | **Separate from career by her own framing** |
| `SESSION-PROMPTS.md` | Starting prompts for each parallel session | — |
| `.claude/skills/` | The agent's skills | — |

**One session owns one folder.** Parallel sessions collide in git otherwise. Pull with
`git pull --rebase` before every commit.

## Skills

| Skill | Does |
|---|---|
| `eu-opportunity-scout` | Finds and **verifies** jobs with sponsorship and funded scholarships |
| `application-tailor` | Tailors CV and letters per application, incl. ATS-safe formatting |
| `interview-prep` | STAR stories, portfolio presentation, the hard visa questions |
| `case-study-translator` | Makes MENA work legible to EU readers without inflating it |
| `stealth-positioning` | Public content that attracts EU recruiters without tipping off her employer |
| `cim-study-partner` | CIM Level 7 assignments, theory, planning |
| `german-practice` | German from A1, spaced repetition |
| `plain-writing` | **Strips AI tells from anything carrying her name. Runs on everything** |
| `linkedin-writer` | Drafts posts and articles in her actual voice |
| `ghostwriter` | Finishes the book. Interview, then shape. Never generate |
| `skill-retro` | Audits and improves the skills above. Git-based, reviewable |

External skills considered and why they were adopted or rejected:
`.claude/skills/skill-retro/audit-log.md`.

## One rule above all

Her employer monitors her LinkedIn. Nothing public may suggest she is planning to leave.
This is not a preference — it is a constraint on her livelihood. Details in `CLAUDE.md`
and `.claude/skills/stealth-positioning/SKILL.md`.

## Rhythm

Weekly check-in, Mondays: new leads tested against the filter, deadlines inside 60 days
flagged, one concrete next action. Monthly `skill-retro` to keep the setup sharp.

## On self-improvement

Improvement happens through **version-controlled edits with reasons**, not silent
self-rewriting. Every change to how the agent behaves is a commit that can be read,
questioned and reverted. This compounds without drifting — which is what "no issues in
the future" actually requires. See `.claude/skills/skill-retro/SKILL.md`.
