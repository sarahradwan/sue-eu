#!/usr/bin/env python3
"""ADNEC Group - Head of Creative Services, Abu Dhabi.

Variant `group-creative-leadership`. Wording source of truth:
08-uae-income/cv-adnec-head-of-creative.md - update both together.

    CV_EMAIL="..." CV_PHONE="..." python3 build-adnec-cv.py
"""
from cv_builder import build_both

CONTENT = {
    "name": "Sara Radwan",
    "tagline": "Creative Leadership - Brand, Design Systems and Event Experience",
    "location": "Abu Dhabi, United Arab Emirates",
    "links": "sarahradwan.me/case-studies  |  linkedin.com/in/sarahradwan1",

    "summary": (
        "Creative leader with 22 years across Egypt, Qatar and the United Arab Emirates, "
        "currently leading brand and creative for UAE government and institutional clients, and "
        "having held Creative Director roles across a creative studio, a national education "
        "programme and a major international conference. Defines creative vision across groups "
        "and their subsidiary businesses, having led brand architecture across group companies "
        "in four countries. Builds and governs the design systems and brand guidelines that hold "
        "consistency across every touchpoint, delivers brand experience in physical space for "
        "large-scale events, and owns corporate publications from annual reports to "
        "institutional literature. Ten years leading and developing creative teams, currently "
        "with multiple direct reports. Leads AI adoption in creative production, embedding "
        "generation into live delivery and codifying AI usage standards into client brand "
        "documentation. Native Arabic and fluent English. Studying for the Chartered Institute "
        "of Marketing Level 7 Postgraduate Diploma in Professional Marketing."
    ),

    "roles": [
        {
            "title": "Senior Art Director, Brand and Creative Lead",
            "employer": "WeDo Advertising and Publicity - Abu Dhabi, United Arab Emirates",
            "dates": "February 2025 - Present",
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
            "bullets": [
                "Art directed more than 20 consumer and business brands across fashion, beauty, lifestyle and trade, spanning print, social and digital communications.",
                "Led the MBC magazine rebrand, followed by 38 percent subscriber growth.",
            ],
        },
        {
            "title": "Head of Creative",
            "employer": "Al Arab Newspaper - Doha, Qatar and Cairo, Egypt",
            "dates": "2010 - 2015",
            "bullets": [
                "Led the creative function of a national newspaper, including a full redesign and weekly supplements.",
                "Managed and developed the design team, setting creative standards and building capability.",
            ],
        },
    ],

    "education": [
        ("Postgraduate Diploma in Professional Marketing, CIM Level 7 - In progress",
         ["Oxford College of Marketing, Chartered Institute of Marketing",
          "Strategic marketing, brand management, marketing planning and measurement."]),
        ("Bachelor of Advertising and Graphic Design - 2003",
         ["Faculty of Applied Arts, Helwan University, Cairo, Egypt"]),
    ],

    "skills": (
        "Creative vision and direction at group level, brand architecture across subsidiary "
        "businesses, brand identity systems, brand guidelines and governance, design systems and "
        "templates, integrated marketing campaigns, event and experience design, environmental "
        "design and wayfinding, event coverage and collateral, corporate marketing "
        "communications, internal brand and employee experience, digital content direction, "
        "corporate publications and annual reports, editorial and publication design, bilingual "
        "Arabic and English brand systems, multi-script typography, information design and data "
        "visualisation, creative team leadership and line management, workflow and quality "
        "management, senior stakeholder management, new business and tender development, "
        "AI-powered content creation, AI governance in brand systems."
    ),

    "languages": ["Arabic - Native", "English - C2, fluent", "French - A2", "German - A2"],

    "tools": (
        "Adobe InDesign, Adobe Illustrator, Adobe Photoshop, Keynote, PowerPoint, AI generation "
        "and research platforms, Figma (working knowledge, actively developing)."
    ),
}

if __name__ == "__main__":
    build_both(CONTENT, "SaraRadwan_CV_ADNEC_HeadOfCreativeServices")
