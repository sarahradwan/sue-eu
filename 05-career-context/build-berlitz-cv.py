#!/usr/bin/env python3
"""Berlitz Brand Design Lead CV. ATS-safe: single column, no tables, no text boxes."""

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

EMAIL = "hello@sarahradwan.me"
PHONE = "+971 52 870 2003"


def base_doc():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10)
    style.paragraph_format.space_after = Pt(3)
    style.paragraph_format.line_spacing = 1.05
    return doc


def para(doc, text, size=10, bold=False, italic=False, space_before=0, space_after=3):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    return p


def heading(doc, text):
    p = doc.add_paragraph()
    run = p.add_run(text.upper())
    run.font.size = Pt(10.5)
    run.bold = True
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    return p


def bullet(doc, text, bold_lead=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_lead:
        r = p.add_run(bold_lead)
        r.bold = True
        r.font.size = Pt(10)
    r2 = p.add_run(text)
    r2.font.size = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    return p


doc = base_doc()

# Header
p = doc.add_paragraph()
r = p.add_run("Sara Radwan")
r.bold = True
r.font.size = Pt(18)
p.paragraph_format.space_after = Pt(1)

para(doc, "Brand Design Lead. Identity Systems for Distributed, Multi-Country Organisations",
     size=11, space_after=3)
para(doc, "Abu Dhabi, United Arab Emirates. Available to relocate to Europe.", size=9.5, space_after=1)
para(doc, f"{EMAIL} | {PHONE} | sarahradwan.me/case-studies | linkedin.com/in/sarahradwan1",
     size=9.5, space_after=2)

# Summary
heading(doc, "Summary")
para(doc,
     "Brand designer and creative lead with 22 years building visual identity systems and the "
     "guidelines that keep them intact across markets. Held one brand architecture across group "
     "subsidiaries in four countries over a four-year retainer, in an organisation where regional "
     "teams had drifted in their own directions. Builds identities rather than maintaining them: "
     "the design and typographic system behind a national school curriculum of 100+ titles across "
     "three scripts, and the full identity and investor story for a technology company that had no "
     "visual language at all. Works daily with government ministries who buy through formal "
     "multi-stage procurement, contributing to a 12 percent tender win rate. Uses AI in live "
     "production and writes AI usage governance into client brand systems.")

# Experience
heading(doc, "Experience")

para(doc, "Senior Art Director, Brand and Creative Lead", bold=True, space_before=4, space_after=0)
para(doc, "WeDo Advertising and Publicity, Abu Dhabi, United Arab Emirates. February 2025 to present",
     size=9.5, italic=True, space_after=2)
bullet(doc, "for UAE government and institutional clients: typography, colour, imagery and the "
            "standards that hold them together across print, digital and environmental touchpoints.",
       bold_lead="Own brand identity systems and guidelines ")
bullet(doc, "present and defend brand decisions to ministers and executive committees, and shape "
            "creative narratives for competitive government tenders, contributing to a 12 percent win rate.",
       bold_lead="Enterprise and institutional buyers: ")
bullet(doc, "generative image and video in live production, AI-assisted research, and AI usage "
            "guidelines written into client brand systems defining where AI is appropriate, what "
            "needs human sign-off, and the quality threshold before anything ships.",
       bold_lead="AI in practice and in governance: ")
bullet(doc, "Direct freelancers, motion designers, illustrators, developers and production partners "
            "across concurrent programmes without losing ownership of quality or direction.")
bullet(doc, "Art directed the 2025 Annual Report for the UAE Ministry of Foreign Affairs aid agency, "
            "produced in separate Arabic and English editions inside government brand guidelines.")

para(doc, "Co-Founder and Creative Director", bold=True, space_before=6, space_after=0)
para(doc, "Social Dar Marketing Management, Dubai, United Arab Emirates. August 2021 to June 2024",
     size=9.5, italic=True, space_after=2)
bullet(doc, "over a four-year retainer. One system, four markets, and regional teams with their own "
            "histories and preferences. Consistency came from guidelines specific enough to be usable "
            "and enough local buy-in that following them was easier than not.",
       bold_lead="Built and held brand architecture across group subsidiaries in the United Arab "
                 "Emirates, Pakistan, Ukraine and Kenya ")
bullet(doc, "for Act Air, an interactive hologram technology company with no existing visual "
            "language, working inside a fixed name and making everything else carry the positioning.",
       bold_lead="Created the full brand identity and investor narrative ")
bullet(doc, "Delivered a two-day brand experience for Dubai's Roads and Transport Authority: identity, "
            "six bilingual activations, touchscreen kiosks, environmental graphics and a registration "
            "platform handling more than 250 vacancies.")
bullet(doc, "Owned the commercial side alongside creative direction: new business, scoping, pricing "
            "and margin.")

para(doc, "Creative Director and Team Lead, National Curriculum Design System", bold=True,
     space_before=6, space_after=0)
para(doc, "UAE Ministry of Education, via Ibtikar Edu Tech Solutions. 2019 to 2021. Project value 500,000 euro",
     size=9.5, italic=True, space_after=2)
bullet(doc, "for the national school curriculum: 100+ titles, five subjects, three scripts, and the "
            "templates and standards that let a large team apply it consistently without the author "
            "in the room.",
       bold_lead="Built the visual and typographic system ")
bullet(doc, "Led designers, illustrators and layout specialists, reviewing output against the system "
            "and mentoring on the thinking behind it rather than policing the output.")
bullet(doc, "Directed interactive digital editions with embedded multimedia across the full series.")

para(doc, "Art Director and Fashion and Beauty Editor", bold=True, space_before=6, space_after=0)
para(doc, "CPI Media Group, Dubai, United Arab Emirates. 2015 to 2020", size=9.5, italic=True, space_after=2)
bullet(doc, "Held design direction across more than 20 consumer and B2B titles in print, digital and "
            "social, to fixed publication cycles.")
bullet(doc, "Led the rebrand of Mother, Baby and Child, followed by 38 percent subscriber growth.")

para(doc, "Head of Creative", bold=True, space_before=6, space_after=0)
para(doc, "Al Arab Newspaper, Doha, Qatar and Cairo, Egypt. 2010 to 2015", size=9.5, italic=True, space_after=2)
bullet(doc, "Led the creative function of a national daily newspaper: full redesign, weekly "
            "supplements, and management and development of the design team under daily deadline.")

# Education
heading(doc, "Education")
para(doc, "Postgraduate Diploma in Professional Marketing, CIM Level 7. In progress", bold=True, space_after=0)
para(doc, "Oxford College of Marketing, Chartered Institute of Marketing", size=9.5, italic=True, space_after=3)
para(doc, "BSc Advertising and Graphic Design. 2003", bold=True, space_after=0)
para(doc, "Faculty of Applied Arts, Helwan University, Cairo, Egypt", size=9.5, italic=True, space_after=2)

# Skills
heading(doc, "Skills")
p = doc.add_paragraph()
r = p.add_run("Brand systems. ")
r.bold = True
r.font.size = Pt(10)
p.add_run("Brand identity and architecture across markets · Guidelines and standards written to be "
          "used by distributed teams · Design systems, templates and patterns · Typography, colour "
          "and imagery direction · Multi-script systems in Arabic and Latin · Holding a fixed "
          "constraint and making everything around it work harder").font.size = Pt(10)
p.paragraph_format.space_after = Pt(3)

p = doc.add_paragraph()
r = p.add_run("Enterprise and institutional. ")
r.bold = True
r.font.size = Pt(10)
p.add_run("Ministerial and executive stakeholder relationships · Formal procurement and tender "
          "narratives · Brand governance and compliance across regions · Internal brand and employee "
          "experience · Mentoring designers on brand thinking").font.size = Pt(10)
p.paragraph_format.space_after = Pt(3)

p = doc.add_paragraph()
r = p.add_run("AI in practice. ")
r.bold = True
r.font.size = Pt(10)
p.add_run("Generative image and video in live production · AI usage guidelines and governance written "
          "into client brand systems · AI-assisted research and concept development · Judgement on "
          "where AI adds value and where it does not").font.size = Pt(10)
p.paragraph_format.space_after = Pt(3)

# Languages
heading(doc, "Languages")
para(doc, "English, fluent (C2) · Arabic, native · German, A2 and actively improving · French, A2. "
          "Has art directed and set publications in Arabic, English and French.", space_after=2)

# Tools
heading(doc, "Tools")
para(doc, "Adobe Creative Suite (InDesign, Illustrator, Photoshop), expert · Figma, in active "
          "development · Keynote and PowerPoint · AI platforms including Midjourney, Firefly and ChatGPT",
     space_after=2)

out = "/tmp/claude-0/-home-user-sue-eu/a614d373-7f21-52dd-b6d2-bd7c13427802/scratchpad/SaraRadwan_CV_Berlitz_BrandDesignLead.docx"
doc.save(out)

# Verify ATS-safety
from docx import Document as D
d = D(out)
assert len(d.tables) == 0, "ATS FAIL: tables present"
words = sum(len(p.text.split()) for p in d.paragraphs)
print(f"Saved: {out}")
print(f"Tables: {len(d.tables)} (must be 0)")
print(f"Paragraphs: {len(d.paragraphs)}, words: {words}")
assert EMAIL in "\n".join(p.text for p in d.paragraphs), "contact missing"
print("Contact details present. ATS checks passed.")
