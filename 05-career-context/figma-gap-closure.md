# Figma — gap closure plan

**Started 3 Aug 2026. Target: artefact finished 30 Aug 2026.**

This is not "learn Figma". It is: close the one gap that has cost four applications,
in the narrowest way that actually closes it, and end with something reviewable.

---

## Why this, why now

Figma was a **stated requirement** — not a preference — in four postings screened in
July, and the exact wording matters because it tells you what to learn:

| Role | Wording | What it actually asks for |
|---|---|---|
| **Moss**, Senior/Lead Brand Designer | *"Expertise in Figma, deep understanding of **Auto Layout, components**"* | Named features. Testable in a portfolio review |
| **Mutabor**, Senior Brand Designer | *"**Sehr gute Kenntnisse in Figma**"* — listed **before** Adobe | General fluency, but Figma-first shop |
| **Adyen**, Art Director | *"proficiency in Adobe CC, Keynote, Google slides, and **Figma**"* | One tool among several. Lowest bar |
| **AKQA**, ACD | *"proficiency in… Figma"* | One tool among several |

**The bar to clear is Moss's, because it is the highest and it is specific.** Auto Layout
and components, understood well enough to survive being asked about them by someone who
uses them daily.

**What is NOT in scope.** Monks asked for *"screens, components, and systems… user journeys,
flows, states"* and working prototypes. **That is product/UI design — a different discipline,
not a Figma gap.** Do not try to close it here. Learning Figma will not make her a product
designer and she should not apply as one.

So: **brand-and-design-systems Figma. Not product Figma.**

---

## The account constraint — check this on day one

Her Figma account (`sarahradwan@gmail.com`) sits on **Starter tier** across both teams she
holds a Full seat on. Starter is the free plan, and it is likely to block two things this
plan depends on:

- **Publishing a shared library** — believed to require Professional or above.
- **Variable modes** (more than one mode per collection) — believed to require a paid plan.

⚠️ **Unverified — the egress policy in this session blocks Figma's pricing page, so this is
from memory, not from the source.** Check it in the app in the first ten minutes: try to
publish a library and try to add a second mode to a variable collection. If either is gated:

1. **Figma runs a free Professional trial.** Time it to start in Week 3, when publishing
   is actually needed, not on day one where it will expire before it is useful.
2. There is an **education plan** — she is a registered CIM Level 7 student at Oxford
   College of Marketing, which may qualify. Worth ten minutes.
3. If neither works, **the library still gets built, it just does not get published.** The
   components, variants and variables all work on Starter. Publishing is the last 5% and it
   can be described in interview rather than demonstrated.

Do not let a plan tier stop the work. Find out on day one so it does not surprise her in
Week 3.

---

## The translation table — read this before touching a tutorial

She has 22 years of this. She does not need to learn design systems; she needs to learn
**where Figma keeps the things she already knows**, and the three places where the mental
model genuinely differs. This table is worth more than the first four hours of any course.

| InDesign | Figma | Watch out |
|---|---|---|
| Paragraph / character styles | **Text styles**, or typography variables | Figma's are **flat** — no "based on" inheritance, no nesting. A change to a base style does not cascade. This will feel primitive |
| Swatches | **Colour styles** → now **variables** | Two systems coexist. Variables are the current one. Build in variables |
| Master pages | **Components** | Not a true equivalent. A master page *pushes* onto document pages; a component is *placed* as instances. Closer to a snippet than a master |
| Object styles | Component + **variants** | No direct equivalent |
| CC Library | **Published library** | Same concept, gated by plan tier |
| Layout grids and margins | **Layout grid**, per frame | Attached to frames, not to the document. Set once per component, not once per file |
| Anchored objects | **Auto Layout** | Closest analogue |
| Artboards | **Frames** | Frames nest infinitely, which artboards do not. "Pages" in Figma are file tabs, not document pages |
| **Threaded text frames** | **Nothing** | ⚠️ The biggest shock. Figma has **no text threading and no copy flow**. Text does not reflow from one frame to the next. This is why Figma is bad at long-form editorial and why the rebuild below is scoped the way it is |
| **Baseline grid** | **Nothing native** | No baseline snapping. Expect this to be irritating. Approximate with spacing variables on an 8pt rhythm |
| **Data merge** | Nothing native | Plugins only |
| — | **Auto Layout** | The one genuinely new concept. See below |

### Auto Layout, explained for a print person

It is CSS flexbox with a UI. A frame with Auto Layout lays its children out in a **row or a
column**, with a **gap** between them and **padding** around them, and it **re-flows when
content changes**.

**The whole thing is three sizing modes.** Learn these and Auto Layout is done:

- **Fixed** — this dimension is a number and stays that number.
- **Hug** — the frame shrinks to fit its contents. *Container hugs children.*
- **Fill** — the child stretches to fill its parent. *Child fills container.*

Almost every Auto Layout problem anyone ever has is a Hug where it should be Fill, or the
reverse, somewhere up the nesting chain. When something behaves strangely, walk up the layer
tree checking those three settings at each level. That is the debugging method, and knowing
it is most of what "deep understanding of Auto Layout" means in practice.

### Components, variants, properties

- **Component** = master. **Instance** = placed copy, inherits changes from the master.
- **Variants** = related components collapsed into one, with properties. A button with
  `Size: S/M/L` × `State: default/hover/disabled` is one component, not nine.
- **Component properties** = exposed controls on an instance without detaching it:
  **text** (swap the words), **boolean** (show/hide a layer), **instance swap** (change a
  nested icon). This is where the craft is. A component nobody can reconfigure without
  detaching it is a bad component.

### Variables

Four types — **colour, number, string, boolean** — grouped into **collections**. A collection
can have **modes**, and one design can switch mode wholesale.

**Modes are the whole opportunity here — see the artefact below.**

---

## The artefact: the curriculum system, rebuilt as a Figma library

Four weeks of tutorials produces nothing anyone can look at. **Rebuild an existing system
instead** — she is not learning design, so the design work is free, and the output is
simultaneously the practice, the portfolio piece and the interview answer.

**Rebuild: the UAE national curriculum design system.** 100+ titles, five subjects, three
scripts, €500,000 programme.

**But rebuild the *system*, not the *books*.** Figma has no text threading — rebuilding
long-form layout in it would fight the tool and prove nothing. Build the layer underneath:

- **Type scale** as typography variables, across three scripts.
- **Colour** as variables — the five subjects are five colour identities.
- **Spacing** as number variables on a consistent rhythm.
- **The recurring page furniture** as components with variants: chapter openers, exercise
  blocks, callouts, diagram frames, running heads, sidebars.
- **Auto Layout throughout**, so a longer heading or a longer Arabic string reflows the
  block instead of breaking it.

### The differentiator: script as a variable mode

Set up the collection with **a mode per script — Arabic, English, and the third**. Switching
mode switches type family, size, line height, and the spacing that has to change when the
script changes. One component, three scripts, no duplicated artwork.

**This is the piece nobody else in the pile will have.** On generic component craft she is a
beginner competing against people who do it daily. On **multi-script design systems** she has
a credential that is genuinely scarce in the European market — and this expresses it in the
tool they asked about. It converts her strongest existing asset into the format they can read.

⚠️ **Figma's RTL support is limited.** Arabic text shaping works; **automatic layout
mirroring does not**. She will hit real walls. **That is an asset, not a problem** — *"here
is where the tool stops supporting bidirectional systems, and here is how I structured around
it"* is a senior answer to a question most candidates cannot even frame. Document the walls
as she hits them. That commentary is the portfolio piece, more than the artwork is.

⚠️ **Check what she is contractually allowed to show.** This was Ministry of Education work
via Ibtikar. If the actual assets are restricted, rebuild the *principles* with substituted
content — invented subject names, placeholder text. The system is the point; the specific
curriculum is not.

---

## Four weeks

Assume **5–6 hours a week**. She has a full-time senior job and CIM Level 7 running. This is
built to survive a bad week, not to be heroic.

### Week 1 — 3–9 Aug · Mechanics
- Day one, first ten minutes: **test the plan-tier limits** (publish a library, add a second
  variable mode). Resolve before Week 3.
- Frames, nesting, constraints, the layers panel.
- **Auto Layout until Fixed/Hug/Fill is automatic.** This is the week's real objective.
  Do not move on while it still feels uncertain — everything after this sits on it.
- Set up the file structure: pages for Foundations / Components / Documentation.
- *Output: type scale and colour set up as variables.*

### Week 2 — 10–16 Aug · Components
- Build the page-furniture components. Start with the simplest recurring block.
- **Variants** for the five subjects.
- **Component properties** — text, boolean, instance swap. Make each component
  reconfigurable without detaching.
- *Output: six to eight working components.*

### Week 3 — 17–23 Aug · Variables and modes
- The script modes. Expect this to be the hardest and most interesting week.
- Spacing variables; get the rhythm consistent.
- **Publish as a library** if the plan allows; start the Professional trial now if needed.
- *Output: mode switching works across the whole component set.*

### Week 4 — 24–30 Aug · Finish and document
- A documentation page inside the file: how the system is used, what the modes do, what the
  rules are. **She already writes brand guidelines — this is that, in Figma.**
- Write up the RTL constraints and how she worked around them.
- Two or three clean presentation frames for the portfolio.
- *Output: a shareable Figma link, and a case-study section for sarahradwan.me.*

**30 Aug lands two days before the 1 Sept follow-up round.** That is deliberate — a follow-up
email that says *"since applying I have rebuilt a multi-script design system as a Figma
library, here it is"* is a reason to reopen a file, which a plain chase is not.

---

## What she can honestly claim, and when

The vault's rule is that a claim never runs ahead of the evidence. Applies here too.

| Stage | CV wording | Interview answer |
|---|---|---|
| **Now (pre-Week 1)** | *"Figma — working knowledge, actively developing"* | *"My depth is Adobe. I'm building Figma properly now."* Unchanged from what has already been sent |
| **After Week 2** | Same. **Do not upgrade yet** | *"I'm rebuilding one of my design systems as a Figma library — components and variants are done, variables next."* An in-progress specific beats a vague claim |
| **After Week 4, artefact live** | *"Figma — design systems, components and variables"* | Send the link. **A file they can open ends the question.** No adjective can do what the link does |

**Do not change `cv-source-of-truth.md` until the artefact exists.** The current honest
wording has already gone out on nine applications; changing it early would make those
inconsistent with a later CV, and the honesty is doing real work in her favour.

**What never gets claimed:** *expertise*. Four weeks is competence, not expertise, and the
people interviewing at Moss-tier use this daily and will know within two questions. The
position that wins is *"beginner in the tool, twenty-two years in the discipline, and here is
a system I built in it"* — which is true, unusual, and stronger than a claim she would have
to defend.

---

## The feedback loop

**Her Figma account is connected to this session.** That means the file can be read directly
and critiqued as she builds — component structure, variable definitions, whether Auto Layout
is doing the work or whether things are being positioned by hand.

**Use it weekly.** Paste the file link and ask for a review. The failure mode for someone
coming from print is building something that *looks* right but is structurally hand-placed —
which passes a screenshot and fails a portfolio review the moment someone drags a text frame
wider. Catching that in Week 2 costs nothing; catching it in an interview costs the role.

---

## Motion — the other gap, deliberately not being fixed yet

Motion was the second recurring gap. **Leave it.** Doing both at once does neither properly,
and the honest line already holds:

> *"I direct motion, I don't build it, and the hands-on side is what I'm developing."*

That is defensible against *"solid foundation and willingness to develop"*. It is not
defensible against *"create motion-driven assets in After Effects"* — and those roles should
simply be skipped rather than stretched for. **Revisit in September**, once Figma is closed.
