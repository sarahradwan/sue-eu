#!/usr/bin/env python3
"""Breuninger Senior Art Director Image CV. ATS-safe: single column, no tables."""

from docx import Document
from docx.shared import Pt, Inches

EMAIL = "hello@sarahradwan.me"
PHONE = "+971 52 870 2003"
OUT = ("/tmp/claude-0/-home-user-sue-eu/a614d373-7f21-52dd-b6d2-bd7c13427802/scratchpad/"
       "SaraRadwan_CV_Breuninger_SeniorArtDirectorImage.docx")


def base_doc():
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.6); s.bottom_margin = Inches(0.6)
        s.left_margin = Inches(0.75); s.right_margin = Inches(0.75)
    st = doc.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(10)
    st.paragraph_format.space_after = Pt(3)
    st.paragraph_format.line_spacing = 1.05
    return doc


def para(doc, text, size=10, bold=False, italic=False, before=0, after=3):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.size = Pt(size); r.bold = bold; r.italic = italic
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    return p


def heading(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text.upper())
    r.font.size = Pt(10.5); r.bold = True
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    return p


def bullet(doc, text, lead=None):
    p = doc.add_paragraph(style="List Bullet")
    if lead:
        r = p.add_run(lead); r.bold = True; r.font.size = Pt(10)
    r2 = p.add_run(text); r2.font.size = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    return p


def role(doc, title, meta):
    para(doc, title, bold=True, before=6, after=0)
    para(doc, meta, size=9.5, italic=True, after=2)


doc = base_doc()

p = doc.add_paragraph()
r = p.add_run("Sara Radwan"); r.bold = True; r.font.size = Pt(18)
p.paragraph_format.space_after = Pt(1)

para(doc, "Senior Art Director. Editorial Image Direction, Visual Identity and AI-Led Image Workflows",
     size=11, after=3)
para(doc, "Abu Dhabi, United Arab Emirates. Umzugsbereit nach Stuttgart.", size=9.5, after=1)
para(doc, f"{EMAIL} | {PHONE} | sarahradwan.me/case-studies | linkedin.com/in/sarahradwan1",
     size=9.5, after=2)

heading(doc, "Summary")
para(doc,
     "Senior art director with 22 years, fifteen of them in editorial. Built image worlds and "
     "visual identity across more than 20 consumer and B2B titles at CPI Media Group, where she "
     "was also Fashion and Beauty Editor, directing cover and interview shoots with photographers "
     "and production teams. Led the creative function of a national daily newspaper through a full "
     "redesign. Deep print production knowledge, from daily newspaper deadlines to a 100-title "
     "curriculum series across three scripts. Uses generative AI as part of live production, "
     "including image generation and prompting workflows, and writes AI usage guidelines into "
     "client brand systems. German A2 and actively improving.")

heading(doc, "Experience")

role(doc, "Senior Art Director, Brand and Creative Lead",
     "WeDo Advertising and Publicity, Abu Dhabi, United Arab Emirates. February 2025 to present")
bullet(doc, "for government and institutional clients: typography, colour, imagery and the "
            "standards that hold a brand together across print, digital and environmental touchpoints.",
       lead="Develop and sharpen visual identity ")
bullet(doc, "generative image and video in live production, image prompting workflows, and AI usage "
            "guidelines written into client brand systems defining where AI belongs and what needs "
            "human judgement.",
       lead="AI-supported image processes: ")
bullet(doc, "Art directed the 2025 Annual Report for the UAE Ministry of Foreign Affairs aid agency, "
            "an editorial publication produced in separate Arabic and English editions.")
bullet(doc, "Steer external creative partners: photographers, illustrators, motion designers, "
            "retouchers and print production houses.")
bullet(doc, "Present and defend creative direction to ministers and executive stakeholders, and "
            "contribute to a 12 percent competitive tender win rate.")

role(doc, "Co-Founder and Creative Director",
     "Social Dar Marketing Management, Dubai, United Arab Emirates. August 2021 to June 2024")
bullet(doc, "Created full brand identities and campaign worlds, including Act Air, an interactive "
            "hologram technology company with no existing visual language.")
bullet(doc, "Built and held brand architecture across group subsidiaries in the United Arab Emirates, "
            "Pakistan, Ukraine and Kenya over a four-year retainer, keeping one visual system "
            "consistent across four markets.")
bullet(doc, "Delivered a two-day brand experience for Dubai's Roads and Transport Authority: identity, "
            "six bilingual activations, environmental graphics and on-site creative direction.")

role(doc, "Creative Director and Team Lead, National Curriculum Design System",
     "UAE Ministry of Education, via Ibtikar Edu Tech Solutions. 2019 to 2021. Project value 500,000 euro")
bullet(doc, "for a national school curriculum: 100+ titles, five subjects, three scripts, and the "
            "templates that let a large team apply one system consistently.",
       lead="Built the visual and typographic system ")
bullet(doc, "Ran print production at volume, and directed interactive digital editions with embedded "
            "multimedia across the full series.")

role(doc, "Art Director and Fashion and Beauty Editor",
     "CPI Media Group, Dubai, United Arab Emirates. 2015 to 2020")
bullet(doc, "across more than 20 consumer and B2B titles in fashion, beauty, lifestyle and trade, "
            "in print, digital and social, to fixed publication cycles.",
       lead="Held image direction and design direction ")
bullet(doc, "briefing photographers, setting the visual direction and making the creative calls on "
            "set. A cover is the single most exposed image a title produces.",
       lead="Directed cover shoots and interview shoots: ")
bullet(doc, "Held editorial ownership of fashion and beauty content alongside art direction, "
            "connecting image and words rather than treating them separately.")
bullet(doc, "Led the rebrand of Mother, Baby and Child, followed by 38 percent subscriber growth.")

role(doc, "Head of Creative",
     "Al Arab Newspaper, Doha, Qatar and Cairo, Egypt. 2010 to 2015")
bullet(doc, "Led the creative function of a national daily newspaper through a full redesign, plus "
            "weekly supplements, managing and developing the design team under daily print deadlines.")

heading(doc, "Education")
para(doc, "Postgraduate Diploma in Professional Marketing, CIM Level 7. In progress", bold=True, after=0)
para(doc, "Oxford College of Marketing, Chartered Institute of Marketing", size=9.5, italic=True, after=3)
para(doc, "BSc Advertising and Graphic Design. 2003", bold=True, after=0)
para(doc, "Faculty of Applied Arts, Helwan University, Cairo, Egypt", size=9.5, italic=True, after=2)

heading(doc, "Skills")
for lead, body in [
    ("Editorial and image. ",
     "Image worlds, campaign looks and editorial concepts · Direction of cover and interview shoots · "
     "Briefing and steering photographers, retouchers and production partners · Typography, layout, "
     "grid and image composition · Print production at volume · Multi-script typography in Arabic and Latin"),
    ("Brand and identity. ",
     "Development and establishment of visual identities · Brand guidelines and standards · Brand "
     "architecture across markets · Translating brand strategy into image direction · Stakeholder "
     "management at executive level"),
    ("AI in practice. ",
     "Generative image and video in live production · Image prompting and AI-supported creative "
     "workflows · AI usage guidelines written into brand systems · Judgement on where AI adds value "
     "and where it does not"),
]:
    p = doc.add_paragraph()
    r = p.add_run(lead); r.bold = True; r.font.size = Pt(10)
    p.add_run(body).font.size = Pt(10)
    p.paragraph_format.space_after = Pt(3)

heading(doc, "Languages")
para(doc, "English, fluent (C2) · Arabic, native · German, A2 and actively improving · French, A2. "
          "Has art directed and set publications in Arabic, English and French.", after=2)

heading(doc, "Tools")
para(doc, "Adobe Creative Suite (InDesign, Illustrator, Photoshop), expert · Figma, in active "
          "development · Keynote and PowerPoint · Generative AI platforms including Midjourney, "
          "Firefly and ChatGPT", after=2)

doc.save(OUT)

from docx import Document as D
d = D(OUT)
assert len(d.tables) == 0, "ATS FAIL: tables present"
text = "\n".join(p.text for p in d.paragraphs)
assert EMAIL in text and PHONE in text, "contact missing"
print(f"Saved: {OUT}")
print(f"Tables: {len(d.tables)} | paragraphs: {len(d.paragraphs)} | words: {len(text.split())}")
print("ATS checks passed.")
