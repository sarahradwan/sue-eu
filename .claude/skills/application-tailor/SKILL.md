---
name: application-tailor
description: Tailor Sara's CV and write cover letters for a specific EU job or scholarship application, including ATS-safe formatting. Use when she is applying to a role or programme, adapting her CV, writing a cover letter or motivation letter, or asking whether her CV will pass an applicant tracking system.
---

# Application tailor

Turns the master CV into a targeted application. Master:
`05-career-context/cv-source-of-truth.md`. Log every send in
`05-career-context/application-history.md`.

Adapted from public resume skills, with the fabrication-prone and LinkedIn-risky parts
removed — see `skill-retro` for the audit.

## The two-document rule

Sara is a creative director. Her CV is a designed artefact, and it should be — it is
evidence of craft. But **a designed CV and a machine-readable CV cannot be the same file.**

So every application uses one or both of:

| Document | For | Format |
|---|---|---|
| **Designed CV** | Human readers, portfolio, direct email to a named person, creative director roles where craft is the point | Her existing layout |
| **ATS-safe CV** | Any online form, job board, large-agency or corporate portal, university application system | Single column, no tables |

When in doubt, send the ATS-safe version and link the portfolio. A beautiful CV that
parses into nonsense loses to a plain one that parses cleanly.

## Verified: her current CV has an ATS problem

Checked directly against the source file. It contains **two tables, each with two equal
columns** — the four-panel "Across Brand, Experience & Technology" section and the Skills
grid.

Many ATS parsers read tables cell-by-cell across rows. Two-column panels can come out
interleaved, so "Brand & Design Systems" merges into "Experience Design" and the Skills
section arrives as scrambled fragments. Those are the two sections carrying her
positioning and her keywords — the worst possible ones to lose.

Good news from the same check: **no text boxes and no images**, which are the harder
failures. This is fixable by rebuilding those two sections as linear content.

### ATS-safe rules

- **Single column throughout.** No tables, no side-by-side panels, no columns.
- Contact details in the **body**, never in the header or footer — parsers routinely skip
  header content, and hers currently uses one.
- Standard section headings: `Experience`, `Education`, `Skills`, `Languages`. Not
  "Across Brand, Experience & Technology" — a parser has no idea what that is. Keep the
  creative headings for the designed version.
- Standard bullets. Not `▸`.
- Dates in a consistent `Month Year – Month Year` form.
- Job title, employer, location, dates on separate parseable lines.
- **.docx** unless the posting demands PDF. Text-layer PDFs are usually fine; exported-
  from-design PDFs frequently are not.
- No fancy ligatures or glyphs in body text.

## Tailoring method

**1. Read the posting properly.** Pull out: must-haves vs nice-to-haves, exact keyword
phrasing, seniority, language requirement, and **whether sponsorship or funding is stated**.
If it is not stated, it goes in the pipeline as unverified — see `eu-opportunity-scout`.

**2. Match honestly.** Map each must-have to real evidence from the master CV. Be blunt
with her about genuine gaps. A tailored CV that hides a missing must-have wastes an
application; knowing the gap lets her address it in the letter or skip the role.

**3. Mirror their language, don't invent.** If they say "design systems" use "design
systems", not "visual frameworks". She has done the work — the point is naming it the way
they name it. Never restate a responsibility she did not hold.

**4. Reorder, don't inflate.** Lead with whatever the posting prioritises. A brand systems
role leads with the national curriculum system and brand architecture. An experience
design role leads with RTA. A tech-brand role leads with Act Air and the AI governance work.

**5. Never fabricate.** No invented metrics, employers, tools or dates. If a number is
unknown, leave it out — do **not** estimate. Her real numbers are strong enough:

€500,000 · 100+ books · 5 subjects · 3 scripts · 22 years · +38% · 4 countries ·
20+ brands · 12% tender win rate · 250+ vacancies

## Cover and motivation letters

Different jobs, do not blur them:

- **Cover letter (Route A)** — why this employer, why her, what she brings. Concrete
  evidence over adjectives.
- **Motivation letter (Route B)** — why this programme, why now, what she will do with it.
  Scholarship panels weight motivation and trajectory heavily; a 22-year career pivoting
  into formal study needs an explicit, coherent reason.

Structure that works for both:

1. **Specific opening** — the actual role or programme, and one real reason it fits. Never
   "I am writing to apply for."
2. **Strongest proof** — one project told properly, with scale and outcome.
3. **The distinctive angle** — AI governance in brand systems, multi-script design systems,
   or MENA fluency, depending on the target.
4. **Why them** — evidence she has actually read about them.
5. **Close** — direct, no pleading.

**Length:** one page. Scholarship motivation letters follow the stated word count exactly —
panels do disqualify over it.

## The relocation question — handle it directly

She is applying from outside the EU with no current right to work. Employers and panels
will notice. Silence reads as either naivety or evasion.

- **Private applications are not public content.** The `stealth-positioning` rule protects
  LinkedIn and her website. In a direct application she should be completely straightforward
  about wanting to move and about needing sponsorship. Confidentiality applies to what her
  employer can see, not to the people she is applying to.
- **Lead with the motivation, not the mechanism.** The reason is the work — European brand
  practice, design systems culture, the market she wants to build in. Not "I need a visa."
- **Be accurate about status.** If she has researched the specific permit route, name it.
  Employers unfamiliar with sponsorship are often reassured by a candidate who understands
  the process better than they do.
- **Never ask her to lie** about right to work. It is checkable, and being caught ends the
  application and the relationship.

## References and the current-employer problem

Her current employer must not learn she is looking. So:

- **Never** offer a WeDo colleague as a referee without her explicit say-so.
- Prefer referees from Social Dar, the Ministry of Education programme, DAIS, or CPI — all
  past, all safe.
- If an employer wants to contact her current employer, that is a conversation for offer
  stage. Flag it before she agrees to anything.

## Before sending — checklist

- [ ] Which version — designed or ATS-safe? Matches the channel?
- [ ] Every must-have addressed, or the gap consciously accepted
- [ ] Nothing fabricated; every number real
- [ ] Their vocabulary used
- [ ] Letter within the stated word count
- [ ] No current-employer referee without permission
- [ ] Deadline confirmed, not assumed
- [ ] Logged in `application-history.md`
