#!/usr/bin/env python3
"""Build the ATS-safe CV for ADNEC Group - Head of Creative Services.

Produces BOTH .docx and .pdf from one content definition, so the two files
can never drift apart.

ATS rules, from 05-career-context/cv-template-ats.md:
  single column, no tables, contact details in the BODY not the header,
  standard headings, standard bullets, Month Year - Month Year dates.

The PDF is laid out directly rather than converted from the .docx, because
LibreOffice is non-functional in this environment. Both are real text-layer
documents; neither is exported from a design tool, which is the case
application-tailor warns about.

Usage:  set PHONE below, then  python3 build-adnec-cv.py
Deps:   pip install python-docx reportlab
"""

# --------------------------------------------------------------- CONTACT
# Read from the environment, never hard-coded. The vault's standing rule is
# that contact details are not stored in this repo - application-history.md:
# "Contact details are not stored here." Committing them would put them in
# git history permanently.
#
#   CV_EMAIL="..." CV_PHONE="..." python3 build-adnec-cv.py
import os

EMAIL = os.environ.get("CV_EMAIL", "[EMAIL]")
PHONE = os.environ.get("CV_PHONE", "[+971 - PHONE]")

BASENAME = "SaraRadwan_CV_ADNEC_HeadOfCreativeServices"

# --------------------------------------------------------------- CONTENT
# Single source of truth for both builders.

NAME = "Sara Radwan"
TAGLINE = "Creative Leadership - Brand, Design Systems and Event Experience"
LOCATION = "Abu Dhabi, United Arab Emirates"
LINKS = "sarahradwan.me/case-studies  |  linkedin.com/in/sarahradwan1"

SUMMARY = (
    "Creative leader with 22 years across Egypt, Qatar and the United Arab Emirates, currently "
    "leading brand and creative for UAE government and institutional clients, and having held "
    "Creative Director roles across a creative studio, a national education programme and a "
    "major international conference. Defines creative vision across groups and their subsidiary "
    "businesses, having led brand architecture across group companies in four countries. Builds "
    "and governs the design systems and brand guidelines that hold consistency across every "
    "touchpoint, delivers brand experience in physical space for large-scale events, and owns "
    "corporate publications from annual reports to institutional literature. Ten years leading "
    "and developing creative teams, currently with multiple direct reports. Leads AI adoption "
    "in creative production, embedding generation into live delivery and codifying AI usage "
    "standards into client brand documentation. Native Arabic and fluent English. Studying for "
    "the Chartered Institute of Marketing Level 7 Postgraduate Diploma in Professional Marketing."
)

ROLES = [
    {
        "title": "Senior Art Director, Brand and Creative Lead",
        "employer": "WeDo Advertising and Publicity - Abu Dhabi, United Arab Emirates",
        "dates": "February 2025 - Present",
        "note": None,
        "bullets": [
            "Lead creative vision and delivery for UAE government and institutional clients across brand identity, integrated campaigns, event and experience design, corporate publications and digital content, from concept through execution.",
            "Lead and develop a creative team of multiple direct reports, managing workflow, quality and capability across concurrent client programmes.",
            "Own corporate publications end to end - annual and institutional reports, corporate literature and long-form collateral - carrying brand and typographic consistency across bilingual Arabic and English documents.",
            "Lead AI adoption across creative production, including image and video generation in live client delivery, AI-assisted research and proposal development, and AI usage guidelines written into client brand systems, raising team output and consistency.",
            "Led Benet7awel, an integrated internal change and employee experience campaign for Dubai Municipality, carrying the organisation's move to a Work From Anywhere policy across the entire headquarters through phased teaser and reveal campaigns, employee collateral and props, email communications and physical event setups.",
            "Partner with senior stakeholders to translate business objectives into creative solutions, presenting and defending creative direction to ministers and executive leadership.",
            "Direct multidisciplinary vendors, production partners and developers across concurrent programmes, managing workflow, quality and delivery.",
            "Contributed to a 12 percent government tender win rate through structured proposal and creative development.",
        ],
    },
    {
        "title": "Co-Founder and Creative Director",
        "employer": "Social Dar Marketing Management - Dubai, United Arab Emirates",
        "dates": "August 2021 - June 2024",
        "note": None,
        "bullets": [
            "Led brand architecture across group subsidiary businesses in the United Arab Emirates, Pakistan, Ukraine and Kenya over a four-year retainer, defining how each business expressed a shared parent identity while retaining its own market position.",
            "Delivered a two-day brand experience for Dubai's Roads and Transport Authority end to end: concept, identity, six bilingual activations, touchscreen kiosks, a participatory installation, a registration platform handling more than 250 vacancies, environmental graphics, and on-site creative direction across both days.",
            "Directed full brand creation and investor narrative for Act Air, an interactive hologram technology company, uniting brand identity, digital communications and technology proposition into a single story.",
            "Co-founded and led the studio, owning creative standard, new business and pitching, client relationships, resourcing and profitability.",
        ],
    },
    {
        "title": "Creative Director and Team Lead, National Curriculum Design System",
        "employer": "United Arab Emirates Ministry of Education, via Ibtikar Edu Tech Solutions",
        "dates": "2019 - 2021",
        "note": "Independent contract",
        "bullets": [
            "Led a multidisciplinary team of illustrators, designers and layout specialists to build and apply the visual and typographic system for the national school curriculum, covering more than 100 books across five subjects and three scripts.",
            "Built the design system, templates and standards that allowed a large team to apply the identity consistently at scale, and maintained quality and consistency across every output.",
            "Directed interactive ePub editions with embedded multimedia across the full series.",
            "Programme value 500,000 euros.",
        ],
    },
    {
        "title": "Creative Director, Full Event Identity",
        "employer": "DAIS 2019, Dubai Sports Council - Dubai, United Arab Emirates",
        "dates": "2019",
        "note": "Independent project",
        "bullets": [
            "Led creative direction for Dubai's first international AI in Sport conference, developing the event identity and applying it across billboards, press, environmental signage and wayfinding, entry systems and digital touchpoints.",
        ],
    },
    {
        "title": "Art Director and Fashion and Beauty Editor",
        "employer": "CPI Media Group - Dubai, United Arab Emirates",
        "dates": "2015 - 2020",
        "note": None,
        "bullets": [
            "Art directed more than 20 consumer and business brands across fashion, beauty, lifestyle and trade, spanning print, social and digital communications.",
            "Led the MBC magazine rebrand, followed by 38 percent subscriber growth.",
        ],
    },
    {
        "title": "Head of Creative",
        "employer": "Al Arab Newspaper - Doha, Qatar and Cairo, Egypt",
        "dates": "2010 - 2015",
        "note": None,
        "bullets": [
            "Led the creative function of a national newspaper, including a full redesign and weekly supplements.",
            "Managed and developed the design team, setting creative standards and building capability.",
        ],
    },
]

EDUCATION = [
    ("Postgraduate Diploma in Professional Marketing, CIM Level 7 - In progress",
     ["Oxford College of Marketing, Chartered Institute of Marketing",
      "Strategic marketing, brand management, marketing planning and measurement."]),
    ("Bachelor of Advertising and Graphic Design - 2003",
     ["Faculty of Applied Arts, Helwan University, Cairo, Egypt"]),
]

SKILLS = (
    "Creative vision and direction at group level, brand architecture across subsidiary "
    "businesses, brand identity systems, brand guidelines and governance, design systems and "
    "templates, integrated marketing campaigns, event and experience design, environmental "
    "design and wayfinding, event coverage and collateral, corporate marketing communications, "
    "internal brand and employee experience, digital content direction, corporate publications "
    "and annual reports, editorial and publication design, bilingual Arabic and English brand "
    "systems, multi-script typography, information design and data visualisation, creative team "
    "leadership and line management, workflow and quality management, senior stakeholder "
    "management, new business and tender development, AI-powered content creation, AI "
    "governance in brand systems."
)

LANGUAGES = ["Arabic - Native", "English - C2, fluent", "French - A2", "German - A2"]

TOOLS = (
    "Adobe InDesign, Adobe Illustrator, Adobe Photoshop, Keynote, PowerPoint, AI generation and "
    "research platforms, Figma (working knowledge, actively developing)."
)

CONTACT_LINE = f"{EMAIL}  |  {PHONE}"


# ------------------------------------------------------------------ DOCX
def build_docx(path):
    from docx import Document
    from docx.shared import Pt, Inches

    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.6)
        s.bottom_margin = Inches(0.6)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.05

    def para(text="", size=10.5, bold=False, italic=False, after=4, before=0):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.space_before = Pt(before)
        if text:
            r = p.add_run(text)
            r.font.size = Pt(size)
            r.bold = bold
            r.italic = italic
        return p

    def heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text.upper())
        r.bold = True
        r.font.size = Pt(11)

    def bullet(text):
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Inches(0.25)
        p.add_run(text).font.size = Pt(10.5)

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    r = p.add_run(NAME)
    r.bold = True
    r.font.size = Pt(19)

    para(TAGLINE, size=11.5, after=6)
    para(LOCATION, size=10, after=1)
    para(CONTACT_LINE, size=10, after=1)
    para(LINKS, size=10, after=2)

    heading("Summary")
    para(SUMMARY)

    heading("Experience")
    for role in ROLES:
        pp = doc.add_paragraph()
        pp.paragraph_format.space_before = Pt(9)
        pp.paragraph_format.space_after = Pt(0)
        rr = pp.add_run(role["title"])
        rr.bold = True
        rr.font.size = Pt(11)

        p2 = doc.add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        p2.add_run(role["employer"]).font.size = Pt(10.5)

        p3 = doc.add_paragraph()
        p3.paragraph_format.space_after = Pt(4)
        r3 = p3.add_run(role["dates"] + (f"  |  {role['note']}" if role["note"] else ""))
        r3.font.size = Pt(10)
        r3.italic = True

        for b in role["bullets"]:
            bullet(b)

    heading("Education")
    for title, lines in EDUCATION:
        para(title, bold=True, after=1)
        for i, ln in enumerate(lines):
            para(ln, size=10, after=6 if i == len(lines) - 1 else 1)

    heading("Skills")
    para(SKILLS)

    heading("Languages")
    for i, ln in enumerate(LANGUAGES):
        para(ln, after=1 if i < len(LANGUAGES) - 1 else 4)

    heading("Tools")
    para(TOOLS)

    doc.save(path)
    return path


# ------------------------------------------------------------------- PDF
def build_pdf(path):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                    ListFlowable, ListItem)

    # Tuned to land on two pages. cv-template-ats.md: "Two pages is fine at
    # 22 years. Do not compress to one and lose the evidence." Three pages
    # with a four-line orphan is worse than either.
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=11.8,
                          spaceAfter=3)
    small = ParagraphStyle("small", parent=body, fontSize=9, leading=11, spaceAfter=1)
    ital = ParagraphStyle("ital", parent=small, fontName="Helvetica-Oblique", spaceAfter=3)
    name = ParagraphStyle("name", parent=body, fontName="Helvetica-Bold", fontSize=18,
                          leading=20, spaceAfter=2)
    tag = ParagraphStyle("tag", parent=body, fontSize=10.5, leading=12.5, spaceAfter=5)
    head = ParagraphStyle("head", parent=body, fontName="Helvetica-Bold", fontSize=10,
                          leading=12, spaceBefore=9, spaceAfter=3)
    rtitle = ParagraphStyle("rtitle", parent=body, fontName="Helvetica-Bold", fontSize=10,
                            leading=12, spaceBefore=6.5, spaceAfter=1)
    bul = ParagraphStyle("bul", parent=body, fontSize=9.5, leading=11.8, spaceAfter=2.5)

    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=0.8 * inch, rightMargin=0.8 * inch,
                            topMargin=0.6 * inch, bottomMargin=0.6 * inch,
                            title=f"{NAME} - CV", author=NAME)

    def esc(t):
        return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    f = [Paragraph(esc(NAME), name),
         Paragraph(esc(TAGLINE), tag),
         Paragraph(esc(LOCATION), small),
         Paragraph(esc(CONTACT_LINE), small),
         Paragraph(esc(LINKS), small)]

    f += [Paragraph("SUMMARY", head), Paragraph(esc(SUMMARY), body)]

    f.append(Paragraph("EXPERIENCE", head))
    for role in ROLES:
        f.append(Paragraph(esc(role["title"]), rtitle))
        f.append(Paragraph(esc(role["employer"]), small))
        f.append(Paragraph(esc(role["dates"] +
                               (f"  |  {role['note']}" if role["note"] else "")), ital))
        f.append(ListFlowable(
            [ListItem(Paragraph(esc(b), bul), leftIndent=14, value="bulletchar")
             for b in role["bullets"]],
            bulletType="bullet", bulletFontSize=7, leftIndent=14, start="•"))

    f.append(Paragraph("EDUCATION", head))
    for title, lines in EDUCATION:
        f.append(Paragraph(f"<b>{esc(title)}</b>", body))
        for ln in lines:
            f.append(Paragraph(esc(ln), small))
        f.append(Spacer(1, 5))

    f += [Paragraph("SKILLS", head), Paragraph(esc(SKILLS), body)]

    f.append(Paragraph("LANGUAGES", head))
    for ln in LANGUAGES:
        f.append(Paragraph(esc(ln), small))

    f += [Paragraph("TOOLS", head), Paragraph(esc(TOOLS), body)]

    doc.build(f)
    return path


if __name__ == "__main__":
    print("Written:", build_docx(f"{BASENAME}.docx"))
    print("Written:", build_pdf(f"{BASENAME}.pdf"))
    if PHONE.startswith("[") or EMAIL.startswith("["):
        print("\n!! Contact details are placeholders. Re-run with:")
        print('   CV_EMAIL="..." CV_PHONE="..." python3 build-adnec-cv.py')
