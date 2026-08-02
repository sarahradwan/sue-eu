#!/usr/bin/env python3
"""Build the ATS-safe .docx for ADNEC Group - Head of Creative Services.

ATS rules from 05-career-context/cv-template-ats.md:
single column, no tables, contact details in the BODY not the header,
standard headings, standard bullets, Month Year - Month Year dates.
"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = "SaraRadwan_CV_ADNEC_HeadOfCreativeServices.docx"

doc = Document()

# Page + base style. Plain, single column, no tables anywhere.
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


def para(text="", size=10.5, bold=False, italic=False, after=4, before=0, color=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(before)
    if text:
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic
        if color:
            r.font.color.rgb = RGBColor(*color)
    return p


def heading(text):
    """Standard heading - plain text, bold, uppercase. No Word heading styles
    that ATS parsers sometimes mangle, no tables, no text boxes."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text.upper())
    r.bold = True
    r.font.size = Pt(11)
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Inches(0.25)
    r = p.add_run(text)
    r.font.size = Pt(10.5)
    return p


def role(title, employer, dates, note=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(11)

    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    r2 = p2.add_run(employer)
    r2.font.size = Pt(10.5)

    p3 = doc.add_paragraph()
    p3.paragraph_format.space_after = Pt(4)
    r3 = p3.add_run(dates + (f"  |  {note}" if note else ""))
    r3.font.size = Pt(10)
    r3.italic = True


# ---------------------------------------------------------------- NAME
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(1)
r = p.add_run("Sara Radwan")
r.bold = True
r.font.size = Pt(19)

para("Creative Leadership - Brand, Design Systems and Event Experience", size=11.5, after=6)

# Contact details in the BODY. Never the header - parsers skip headers.
para("Abu Dhabi, United Arab Emirates", size=10, after=1)
para("[EMAIL]  |  [+971 - INSERT YOUR UAE NUMBER]", size=10, after=1)
para("sarahradwan.me/case-studies  |  linkedin.com/in/sarahradwan1", size=10, after=2)

# ---------------------------------------------------------------- SUMMARY
heading("Summary")
para(
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

# ---------------------------------------------------------------- EXPERIENCE
heading("Experience")

role("Senior Art Director, Brand and Creative Lead",
     "WeDo Advertising and Publicity - Abu Dhabi, United Arab Emirates",
     "February 2025 - Present")
for b in [
    "Lead creative vision and delivery for UAE government and institutional clients across brand identity, integrated campaigns, event and experience design, corporate publications and digital content, from concept through execution.",
    "Lead and develop a creative team of multiple direct reports, managing workflow, quality and capability across concurrent client programmes.",
    "Own corporate publications end to end - annual and institutional reports, corporate literature and long-form collateral - carrying brand and typographic consistency across bilingual Arabic and English documents.",
    "Lead AI adoption across creative production, including image and video generation in live client delivery, AI-assisted research and proposal development, and AI usage guidelines written into client brand systems, raising team output and consistency.",
    "Led Benet7awel, an integrated internal change and employee experience campaign for Dubai Municipality, carrying the organisation's move to a Work From Anywhere policy across the entire headquarters through phased teaser and reveal campaigns, employee collateral and props, email communications and physical event setups.",
    "Partner with senior stakeholders to translate business objectives into creative solutions, presenting and defending creative direction to ministers and executive leadership.",
    "Direct multidisciplinary vendors, production partners and developers across concurrent programmes, managing workflow, quality and delivery.",
    "Contributed to a 12 percent government tender win rate through structured proposal and creative development.",
]:
    bullet(b)

role("Co-Founder and Creative Director",
     "Social Dar Marketing Management - Dubai, United Arab Emirates",
     "August 2021 - June 2024")
for b in [
    "Led brand architecture across group subsidiary businesses in the United Arab Emirates, Pakistan, Ukraine and Kenya over a four-year retainer, defining how each business expressed a shared parent identity while retaining its own market position.",
    "Delivered a two-day brand experience for Dubai's Roads and Transport Authority end to end: concept, identity, six bilingual activations, touchscreen kiosks, a participatory installation, a registration platform handling more than 250 vacancies, environmental graphics, and on-site creative direction across both days.",
    "Directed full brand creation and investor narrative for Act Air, an interactive hologram technology company, uniting brand identity, digital communications and technology proposition into a single story.",
    "Co-founded and led the studio, owning creative standard, new business and pitching, client relationships, resourcing and profitability.",
]:
    bullet(b)

role("Creative Director and Team Lead, National Curriculum Design System",
     "United Arab Emirates Ministry of Education, via Ibtikar Edu Tech Solutions",
     "2019 - 2021", note="Independent contract")
for b in [
    "Led a multidisciplinary team of illustrators, designers and layout specialists to build and apply the visual and typographic system for the national school curriculum, covering more than 100 books across five subjects and three scripts.",
    "Built the design system, templates and standards that allowed a large team to apply the identity consistently at scale, and maintained quality and consistency across every output.",
    "Directed interactive ePub editions with embedded multimedia across the full series.",
    "Programme value 500,000 euros.",
]:
    bullet(b)

role("Creative Director, Full Event Identity",
     "DAIS 2019, Dubai Sports Council - Dubai, United Arab Emirates",
     "2019", note="Independent project")
bullet("Led creative direction for Dubai's first international AI in Sport conference, developing the event identity and applying it across billboards, press, environmental signage and wayfinding, entry systems and digital touchpoints.")

role("Art Director and Fashion and Beauty Editor",
     "CPI Media Group - Dubai, United Arab Emirates",
     "2015 - 2020")
for b in [
    "Art directed more than 20 consumer and business brands across fashion, beauty, lifestyle and trade, spanning print, social and digital communications.",
    "Led the MBC magazine rebrand, followed by 38 percent subscriber growth.",
]:
    bullet(b)

role("Head of Creative",
     "Al Arab Newspaper - Doha, Qatar and Cairo, Egypt",
     "2010 - 2015")
for b in [
    "Led the creative function of a national newspaper, including a full redesign and weekly supplements.",
    "Managed and developed the design team, setting creative standards and building capability.",
]:
    bullet(b)

# ---------------------------------------------------------------- EDUCATION
heading("Education")
para("Postgraduate Diploma in Professional Marketing, CIM Level 7 - In progress", bold=True, after=1)
para("Oxford College of Marketing, Chartered Institute of Marketing", size=10, after=1)
para("Strategic marketing, brand management, marketing planning and measurement.", size=10, after=6)

para("Bachelor of Advertising and Graphic Design - 2003", bold=True, after=1)
para("Faculty of Applied Arts, Helwan University, Cairo, Egypt", size=10)

# ---------------------------------------------------------------- SKILLS
heading("Skills")
para(
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

# ---------------------------------------------------------------- LANGUAGES
heading("Languages")
para("Arabic - Native", after=1)
para("English - C2, fluent", after=1)
para("French - A2", after=1)
para("German - A2")

# ---------------------------------------------------------------- TOOLS
heading("Tools")
para(
    "Adobe InDesign, Adobe Illustrator, Adobe Photoshop, Keynote, PowerPoint, AI generation and "
    "research platforms, Figma (working knowledge, actively developing)."
)

doc.save(OUT)
print(f"Written: {OUT}")
