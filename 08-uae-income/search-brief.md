# Active search brief

Sara asked the UAE income session to stop waiting for her to supply postings and go find
them. This is the standing brief. Send it into that session; it already holds the numbers.

Written 31 July 2026.

## The shift

`leads-screened.md` currently says *"Sara supplies the postings; this file holds the
verdicts."* That inverts now. The session searches, screens, and reports a shortlist. Sara
still supplies anything she finds, but she is no longer the only source.

---

## The prompt to send

```
Switch from screening to searching. Go and find live roles yourself.
Do not wait for me to send postings.

You already hold the criteria. Re-read savings-target.md,
market-rate.md, target-employers.md, move-or-stay.md and
stealth-search-uae.md before you start, and use them. Do not
re-derive the numbers.

WHAT I AM LOOKING FOR
- Creative Director, Senior Art Director, Head of Brand, Brand Lead,
  Design Lead, or in-house senior creative. Also annual reporting and
  corporate communications roles, since that is now proven ground.
- Abu Dhabi or Dubai. Remote or hybrid also counts, including for
  employers outside the UAE, because remote work for a non-UAE
  employer feeds Route A2.
- AED 23,000 to 25,000 per month is my floor. Where a posting hides
  the salary, say so and estimate from the employer type using
  market-rate.md, labelled as an estimate.
- Weight employers with European offices heavily, per
  target-employers.md. An intra-company transfer route is worth real
  money to me beyond the salary.
- Corporate and semi-government in-house pays materially better than
  agency. Bias the search that way.

WHERE TO LOOK
Search company career pages directly wherever possible. That is the
safest channel and the least visible.
- The named targets: Serviceplan Middle East, Accenture Song,
  PepsiCo AMESA, Radisson Hotel Group. Also Emperor Middle East,
  who already approached me.
- Large UAE corporates and semi-government: Aldar, Mubadala, Etihad,
  Emirates, ADNOC, Emirates NBD, DP World, e&, Majid Al Futtaim,
  Emaar, Miral, ADQ, Masdar.
- Network agencies in the UAE: Publicis, WPP, Omnicom, Havas,
  Dentsu, MCN, Leo Burnett, Impact BBDO, Serviceplan.
- Reporting and corporate communications specialists in the Gulf,
  since the MoFA annual report makes that a live track.
- Recruiter listings: Michael Page, Robert Walters, Cooper Fitch,
  Hays, Nadia, Charterhouse.

CONFIDENTIALITY, AND ONE HARD RULE
Follow stealth-search-uae.md. Browsing job boards is fine. Do NOT
create profiles, upload my CV, or register me anywhere. Gulf boards
run employer-searchable CV databases and my employer can search them.
Nothing about this search becomes public or discoverable.

DO NOT INVENT LISTINGS. This matters more than volume.
- Every lead needs a real, working URL that you actually fetched.
- If a site blocks you or returns 403, say so plainly and move on.
  Report what you could not reach. A short verified list beats a long
  plausible one.
- Never state a salary a posting does not state. Estimates must be
  labelled as estimates with the reasoning shown.
- If you find nothing that clears my floor, tell me that. A null
  result is a finding.

OUTPUT
Write verdicts into leads-screened.md in the format already there.
For each lead: employer, role, location, salary if stated, whether
they have European offices, which of the six conditions in
move-or-stay.md it passes or fails, and a plain apply or skip.

Then report back short: the three best, what is closing soonest, and
what you want me to do this week. Not a list of everything you saw.

git pull --rebase before committing, then push to
claude/proactive-agent-setup-7f6r2m.
```

---

## Why the fabrication guard is written that hard

An agent told to "find jobs" will produce jobs. The failure mode is a confident list of
plausible-sounding roles at real companies that were never posted, which wastes application
effort and destroys trust in the whole pipeline.

`pipeline-scholarships.md` already recorded that this environment's network policy returned
**403 at the egress proxy** for several primary sources. Job boards are likely to block too.
So the brief demands a fetched URL per lead and an explicit list of what could not be
reached.

## Cadence

Worth re-sending weekly rather than once. Postings turn over fast, and the Monday relocation
check-in does not cover UAE income roles.
