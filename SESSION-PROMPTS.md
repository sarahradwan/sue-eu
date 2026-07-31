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

## Session 4 — LinkedIn reach (UAE + EU)

The hardest brief in the repo. Maximum discoverability in two markets at once, with an
employer reading over her shoulder. Generic growth advice **will** get her caught — the
prompt is written to prevent that.

```
Be my LinkedIn strategist. I want maximum reach and discoverability in
TWO markets at once: the UAE, where I work now, and the EU, where I
want recruiters to find me.

Read these BEFORE advising anything:
- CLAUDE.md
- 04-portfolio-positioning/linkedin-content-system.md  <- READ FIRST
- 04-portfolio-positioning/linkedin-strategy.md
- the stealth-positioning skill

linkedin-content-system.md holds MEASURED performance data from my own
account, plus my voice rules and my posting schedule. It is not theory.
Where generic LinkedIn advice conflicts with it, it wins. Do not make
me re-explain any of it, and do not restate it back to me as if it
were your recommendation.

From that file, the four things you must respect from your first reply:
- NO EM DASHES, ever. Commas, full stops or a colon instead.
- No corporate language, no tip lists. Written like a person.
- Every post needs a genuine image. No-image posts underperform badly.
- Verify any brand or news claim before I post it. I was publicly
  corrected on a LEGO claim once and it was expensive.

This session owns 04-portfolio-positioning/. Do not edit
01-relocation/ or 06-ielts/ — other sessions write there.

THE CONSTRAINT THAT OVERRIDES EVERYTHING:
My employer monitors my LinkedIn. My boss watches what I post and
what I change. So the entire brief is:

  Be maximally findable by EU recruiters while looking, to anyone at
  my company, like a senior creative doing normal professional
  visibility in her current job.

Standard LinkedIn growth advice would end my job. NEVER suggest:
#OpenToWork, "open to opportunities", "seeking new challenges", an EU
city in my location field, a headline implying availability, or
announcing anything about relocating, studying abroad or language
exams. If a tactic would raise my reach but signal intent, tell me it
exists, tell me why it is unsafe, and give me the safe equivalent.
Do not quietly include it.

WHAT I ACTUALLY NEED, in priority order:

1. RECRUITER-SEARCH OPTIMISATION FIRST, CONTENT SECOND.
   Most EU recruiters will find me through LinkedIn Recruiter keyword
   search, not through my posts. That search runs on my headline,
   About, Experience text and Skills. Skills in particular are a
   filter recruiters apply directly — and edits there are far less
   visible to a colleague than a headline change or a new post.
   Audit all of it against the vocabulary EU employers actually use
   (design systems, brand governance, employer brand, service design,
   design ops, multi-market brand architecture) versus the Gulf
   agency vocabulary I default to. Tell me which exact terms I am
   missing and where to put them.

2. CLOSE THE EUROPEAN AUDIENCE GAP.
   My audience is currently mostly MENA. I already know posting alone
   will not fix that: European reach needs me commenting on European
   institutional and creative profiles. Build me an actual working
   list, not a principle. Which specific Belgian, Dutch, Irish and
   EU-institutional studios, agencies, design leaders and
   organisations should I be in the comments of, and what do I say
   that is worth reading rather than "great post". This is the
   highest-value thing you can produce for me, and it is also the
   lowest-risk, since a comment on a Brussels studio's post is far
   less likely to reach my boss than a post is.

3. THE DUAL-AUDIENCE UNLOCK.
   Find the content that reads as completely natural to my UAE
   employer AND lands hardest with EU recruiters. My government and
   institutional work is the obvious candidate: large-scale design
   systems and public-sector brand work is normal professional pride
   in Abu Dhabi, and it is exactly what European institutional
   employers want to see. Build the strategy around that overlap.
   Two posts already in my schedule fit this and should be treated as
   templates for more: "Arabic first" (Aug 6) and "Tour & Taxis
   Brussels" (Aug 10).

4. ALGORITHM MECHANICS, applied properly.
   Tell me what currently drives distribution and what is folklore.
   Cover at minimum: what suppresses reach (external links in the
   post body, edits after posting, low early engagement), what the
   first 60-90 minutes do, dwell time versus likes, which formats
   carry for a visual creative (carousel/document posts, native
   video, image), realistic cadence, and whether commenting on other
   people's posts outperforms posting for someone with my follower
   count. Be specific about what is verified versus what is
   widely-believed-but-unproven, and say which is which.

5. THE TIMEZONE PROBLEM.
   I am UTC+4. My EU targets are UTC+1/+2, a two-to-three hour gap.
   I post Mondays and Thursdays. Give me actual posting windows on
   those days that catch both audiences, not a generic "post at 9am".

6. LANGUAGE AND FRAMING.
   How do I describe MENA work so European readers grasp the scale?
   Use the case-study-translator skill — RTA and the Ministry of
   Education curriculum mean nothing in Amsterdam or Dublin.

CONTEXT THAT SHOULD SHAPE YOUR ADVICE:
- Creative Director, 22 years, Egypt/Qatar/UAE. Native Arabic, C2
  English. Currently at a UAE agency doing government work.
- Two live routes: an EU job with visa sponsorship, and remote work
  for a non-EU employer leading to a Spanish digital nomad visa.
  The remote route means "findable by distributed UK/US/Gulf
  employers" matters as much as "findable by EU agencies" — do not
  optimise only for on-site EU roles.
- Brussels is the one EU market where native Arabic is a scarce,
  commercially valuable asset. Worth weighting.
- My portfolio site sarahradwan.me may currently be broken on the
  /case-studies path. A dead link from my profile costs me every
  recruiter who clicks it. Check it early and tell me.

RULES:
- Show me the actual copy, not a description of the copy. Draft the
  headline, the About section, the post. I will edit words, not
  briefs.
- Every public-facing suggestion gets checked against
  stealth-positioning before you show it to me.
- If you are unsure whether something is a relocation tell, assume it
  is and flag it.
- Write the strategy to 04-portfolio-positioning/, not just to chat.
- git pull --rebase before committing, then push to
  claude/proactive-agent-setup-7f6r2m.

START HERE: audit my current profile against EU recruiter search,
meaning headline, About and Skills. Tell me the three highest-impact
changes that carry the LOWEST risk of my employer noticing, and draft
the actual copy. My posting engine already works. The profile it
points at is the part I have not optimised.
```

**Why this order.** Her content system is already producing results, so posting harder is
not the gap. Two things are: a **profile that may not surface in EU recruiter keyword
search**, which wastes every impression the content earns, and an **audience that is still
mostly MENA**. Profile text and skills are also the safest things to change, because they
are far less conspicuous to a colleague than a shift in posting behaviour.

**The convenient part.** The tactic that actually opens the European audience — commenting
on European profiles — is also the least visible to her employer. Worth exploiting
deliberately, while watching the rate of change: occasional European content reads as
professional interest, a sudden pivot to majority-European activity is a pattern.

---

## Session 5 — Afrilink venture evaluation

A community/empowerment venture Sara is planning with a co-founder. The brief is in
`07-afrilink/README.md`. This session **tests** it — it does not help build it yet.

```
I want a hard-nosed evaluation of a venture I am planning with a
co-founder. Effectiveness, feasibility, and profit potential. Not
encouragement.

Read CLAUDE.md and 07-afrilink/README.md first. The README has the
full brief and the questions I already know it does not answer.

This session owns 07-afrilink/ ONLY. Do not edit 01-relocation/,
04-portfolio-positioning/ or 06-ielts/ — other sessions write there.

I need your honest assessment, not validation. If this is a bad idea,
or a good idea at the wrong time, say so plainly and tell me why. I
would rather hear it now than after I have announced it publicly and
brought my co-founder, three collaborators and a community along.

ANSWER IN THIS ORDER. Do not skip ahead to market sizing.

1. IS IT LEGAL FOR ME, RIGHT NOW? This can kill the venture, so it
   goes first.
   - I am on a UAE employment visa sponsored by my current employer.
     What do UAE law and a standard UAE employment contract allow
     regarding outside commercial activity? What are the actual
     consequences of breaching that, given my visa is tied to my job?
   - Charging for workshops, training or consultations is commercial
     activity and needs a licence. Which licence, what does it cost,
     and can it be held by someone on another employer's visa?
   - What is genuinely involved for expatriates registering a
     community organisation or association in the UAE?
   - Does cost-covering ticketing already count as commercial
     activity, or is there a threshold?
   - If the answer is "not as currently structured", tell me what
     structure WOULD be legal. My co-founder's visa status may differ
     from mine and that may matter.

2. DOES IT SURVIVE CONTACT WITH MY CALENDAR?
   Between now and the EU scholarship window I already have: a
   full-time job, CIM Level 7, an IELTS exam I have never sat
   (Sept-Oct 2026), and a document legalisation chain of 6-10 weeks
   that gates BOTH my relocation routes. Plus LinkedIn twice weekly.
   A monthly event is a monthly deadline. Tell me honestly whether
   that fits, or what it displaces. "It fits if you drop X" is a
   useful answer. "It fits" with no analysis is not.

3. THE RELOCATION QUESTION, BOTH WAYS.
   I plan to leave the UAE by mid-2027. Year 1 of this plan is "UAE
   only".
   - Against: what does it mean to found a UAE community and leave
     12-18 months in? What happens to the members and my co-founder?
     What is the responsible handover, and when must it start?
   - For: founding and running an organisation is exactly what my
     strongest scholarship route selects on. Sweden's SI Global
     Professionals weighs leadership and professional experience and
     has no GPA threshold. My Year 3 plan already names the
     Netherlands, France, Germany and Belgium — my target countries.
     Could this venture be the thing that makes my scholarship
     application compelling rather than a distraction from it? Be
     rigorous, not optimistic: does the timing actually work, and
     would a panel find it credible or contrived?

4. THE MONEY, WITH REAL NUMBERS.
   No vibes. Model it:
   - Realistic attendance for a first event and a sixth event
   - Actual Abu Dhabi and Dubai venue costs, or the real terms cafés
     and coworking spaces offer for this kind of partnership
   - What corporate training, workshops and branding consultations
     genuinely command in this market
   - Where the revenue actually comes from in year 1, and whether it
     breaks even
   - Which of the later streams (memberships, marketplace
     commissions, digital products) need scale we will not have, and
     when they realistically start
   Then tell me: is this a profit business, a credibility and network
   asset, or a non-profit that needs sponsorship? All three are valid.
   Pretending it is the first when it is the second is not.

5. THE CONCEPT ITSELF.
   - Is the five-pillar model focused or overextended? We already
     flagged "trying to be everything" as a risk. Are we doing it?
   - Who else serves African professional women in the UAE? Name
     them. If nobody does, ask why not — an empty market is sometimes
     empty for a reason.
   - Is there real demand, or is this a good idea nobody pays for?
   - The youth programme (girls 14-22) involves minors. What does
     that add in terms of safeguarding, consent and regulation?

6. THE NAME.
   "Afrilink" or "She Afrika". Note that we already decided NOT to
   limit the brand to women so we could add mixed programmes later
   without rebranding — so tell me straight whether "She Afrika"
   contradicts our own decision. Also check trademark conflicts,
   domain and social handle availability, and how each name reads in
   Arabic.

RULES:
- Verify claims. Do not tell me UAE licensing rules from memory —
  find the source and cite it. If you cannot verify something, say
  so and mark it unverified.
- Real numbers with sources, or explicitly labelled estimates. Never
  invented precision.
- Write findings to 07-afrilink/, not just to chat.
- CONFIDENTIALITY: my employer monitors my LinkedIn. Anything public
  about this venture follows the stealth-positioning skill, and note
  that a public launch is visible to my employer even though it says
  nothing about relocation. Flag that trade-off.
- git pull --rebase before committing, then push to
  claude/proactive-agent-setup-7f6r2m.

START WITH QUESTION 1. If the legal answer changes the shape of the
venture, everything after it needs rethinking anyway, so do not spend
effort on market analysis until that is settled.
```

**Why the legal question comes first.** Everything downstream — pricing, licensing, whether
Sara can be a named founder at all — depends on it, and it is the one question where the
answer could be "not in this form". Market sizing done before that is wasted work.

---

## Session 6 — UAE income (the funding engine)

Raising UAE earnings to fund the move. Not a career pivot: savings reopen the EU routes
that "no capital to self-fund" currently closes. Context in `08-uae-income/README.md`.

```
I want to move to a higher-paying job in the UAE, and apply. The
purpose is to save money for my EU migration, so treat salary as
infrastructure for that plan, not as an end in itself.

Read CLAUDE.md, 08-uae-income/README.md, 01-relocation/pipeline-jobs.md
and 01-relocation/timeline-to-2027.md first.

This session owns 08-uae-income/ ONLY. Do not edit 01-relocation/,
04-portfolio-positioning/, 06-ielts/ or 07-afrilink/ — other sessions
write there.

WHY THIS MATTERS MORE THAN IT LOOKS, so you optimise for the right
thing: my pipeline-jobs.md file records that I have no capital to
self-fund. That one constraint rules out Germany's Opportunity Card,
the Dutch orientation year, and every EU route needing proof of funds.
Savings do not just make the move comfortable, they reopen routes that
are currently closed to me. Optimise for that, not for the biggest
number.

WORK IN THIS ORDER.

1. TELL ME THE TARGET NUMBER FIRST.
   "Earn more" is not a plan. Before any job search, calculate what I
   actually need saved and by when:
   - For the scholarship route: what a stipend does NOT cover, plus
     flights, first rent and deposit, and a buffer
   - For the sponsored-job route: relocation costs, deposits (Dutch
     landlords often want several months), shipping, the gap before
     the first salary
   - For the Spanish digital nomad route: what that visa requires
     financially on top of monthly income
   Give me one figure with a date on it. Then work backwards: what
   monthly salary, from what month, gets me there by mid-2027? That
   number is the brief for everything below.

2. WHAT AM I ACTUALLY WORTH HERE?
   22 years, Creative Director, brand and experience, government and
   institutional work, currently at an Abu Dhabi agency. Native Arabic,
   C2 English, CIM Level 7 in progress. What do Dubai and Abu Dhabi
   multinationals, in-house brand teams and larger agencies genuinely
   pay for that? Give me ranges with sources, and say plainly whether
   I am currently underpaid. Note that UAE salaries are tax-free, so
   do not compare them to European gross figures.

3. RANK EMPLOYERS BY TWO THINGS, NOT ONE.
   Money AND whether they have European offices. A multinational with
   an Amsterdam, Dublin, London or Brussels office gives me an
   internal-transfer route, which is often the easiest way for a
   non-EU national to reach Europe, because the employer already knows
   me and the paperwork is routine for them. A slightly lower offer
   from a company with EU offices can beat the highest local bidder.
   Build me a ranked target list that scores both. Name real
   companies, not categories.

4. IS MOVING JOBS ACTUALLY NET POSITIVE?
   Be honest, including if the answer is no. I intend to leave the UAE
   by mid-2027, so a role starting late 2026 gives me months, not
   years. Cover: notice periods, probation, any relocation or training
   clawback clauses common in UAE contracts, whether leaving quickly
   burns the reference I will need, and whether UAE labour rules
   create any ban or penalty on a short tenure. Then tell me whether
   a new job, a raise where I am, or freelance income on top is the
   better route to the number in step 1.

5. HOW DO I SEARCH WITHOUT BEING CAUGHT?
   My employer monitors my LinkedIn. UAE job hunting is as visible as
   EU job hunting. Tell me which channels are safe (recruiters,
   direct approaches, referrals) and which are not, and how to handle
   the fact that UAE recruitment runs heavily through LinkedIn.
   Follow the stealth-positioning skill for anything public.

6. THEN APPLY.
   Use the application-tailor skill. Note that my CV has a known ATS
   problem, and 05-career-context/cv-template-ats.md exists for that.
   Track everything in 05-career-context/application-history.md.

RULES:
- Salary figures need sources or an explicit "estimate" label. Never
  invent precision about pay.
- If the honest answer to step 4 is "stay and negotiate", say so.
- Write findings to 08-uae-income/, not just to chat.
- git pull --rebase before committing, then push to
  claude/proactive-agent-setup-7f6r2m.

START WITH STEP 1. Without the target number, everything after it is
guesswork.
```

**Why the number comes first.** Without a figure and a date, "higher salary" has no stopping
condition, and there is no way to judge whether a given offer is worth the disruption of
changing employers 12–18 months before leaving the country.

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
