#!/usr/bin/env python3
"""Etihad Airways - Brand Manager, Abu Dhabi.

Variant `brand-governance-inhouse`. Wording source of truth:
08-uae-income/cv-etihad-brand-manager.md - update both together.

    CV_EMAIL="..." CV_PHONE="..." python3 build-etihad-cv.py
"""
from cv_builder import build_both

CONTENT = {
    "name": "Sara Radwan",
    "tagline": "Brand Management and Brand Governance",
    "location": "Abu Dhabi, United Arab Emirates",
    "links": "sarahradwan.me/case-studies  |  linkedin.com/in/sarahradwan1",

    "summary": (
        "Brand practitioner with 22 years across Egypt, Qatar and the United Arab Emirates, "
        "currently leading brand for UAE government and institutional clients. Works as a brand "
        "custodian: builds and evolves brand guidelines, design systems and templates, and "
        "governs their consistent application across physical environments, print, digital and "
        "service touchpoints. Led brand architecture across group subsidiary businesses in four "
        "countries, defining how each business expressed a shared parent identity while holding "
        "its own market position. Delivers brand campaigns end to end, from customer insight and "
        "agency briefing through production to post-campaign evaluation. Builds brand systems "
        "bilingually in Arabic and English. Studying for the Chartered Institute of Marketing "
        "Level 7 Postgraduate Diploma in Professional Marketing."
    ),

    "roles": [
        {
            "title": "Senior Art Director, Brand and Creative Lead",
            "employer": "WeDo Advertising and Publicity - Abu Dhabi, United Arab Emirates",
            "dates": "February 2025 - Present",
            "bullets": [
                "Act as brand guardian for UAE government and institutional clients: develop and evolve brand guidelines and templates, review brand-facing assets, and give brand guidance and approvals across campaigns, publications, environments and digital channels.",
                "Lead brand campaign development end to end, from brief and creative development through production to delivery, across brand identity, integrated campaigns, event and experience design, corporate publications and digital content.",
                "Led Benet7awel, an integrated brand and change campaign for Dubai Municipality, carrying the organisation's move to a Work From Anywhere policy across the entire headquarters through phased teaser and reveal campaigns, employee collateral and props, email communications and physical event setups.",
                "Manage stakeholders across briefing, feedback, approvals and delivery, presenting and defending brand direction to ministers and executive leadership.",
                "Lead and develop a team of multiple direct reports, and direct external agencies, production partners and vendors across concurrent programmes.",
                "Own corporate publications end to end, including annual and institutional reports, carrying brand and typographic consistency across bilingual Arabic and English documents.",
                "Lead AI adoption in content production, including image and video generation in live delivery and AI usage standards written into client brand documentation.",
                "Contributed to a 12 percent government tender win rate through structured proposal and brand development.",
            ],
        },
        {
            "title": "Co-Founder and Creative Director",
            "employer": "Social Dar Marketing Management - Dubai, United Arab Emirates",
            "dates": "August 2021 - June 2024",
            "bullets": [
                "Led brand architecture across group subsidiary businesses in the United Arab Emirates, Pakistan, Ukraine and Kenya over a four-year retainer, defining how each business expressed a shared parent identity while retaining its own position in its own market.",
                "Carried commercial responsibility for the studio: new business, pricing, resourcing, budget management and profitability.",
                "Delivered a two-day brand experience for Dubai's Roads and Transport Authority end to end, applying the brand across six bilingual activations, touchscreen kiosks, a participatory installation, environmental graphics and wayfinding, and a registration platform handling more than 250 vacancies.",
                "Directed brand creation and investor narrative for Act Air, an interactive hologram technology company, uniting brand identity, digital communications and product proposition.",
            ],
        },
        {
            "title": "Brand and Design Lead, National Curriculum Design System",
            "employer": "United Arab Emirates Ministry of Education, via Ibtikar Edu Tech Solutions",
            "dates": "2019 - 2021",
            "note": "Independent contract",
            "bullets": [
                "Built the brand and typographic system, templates and standards for the national school curriculum, and governed their application across more than 100 books, five subjects and three scripts by a large multidisciplinary team.",
                "Maintained quality and consistency across every output, working through a team that did not report to a single function.",
                "Programme value 500,000 euros.",
            ],
        },
        {
            "title": "Brand Lead, Event Identity",
            "employer": "DAIS 2019, Dubai Sports Council - Dubai, United Arab Emirates",
            "dates": "2019",
            "note": "Independent project",
            "bullets": [
                "Developed the brand identity for Dubai's first international AI in Sport conference and applied it across billboards, press, environmental signage and wayfinding, entry systems and digital touchpoints.",
            ],
        },
        {
            "title": "Art Director and Fashion and Beauty Editor",
            "employer": "CPI Media Group - Dubai, United Arab Emirates",
            "dates": "2015 - 2020",
            "bullets": [
                "Led the MBC magazine rebrand, repositioning the title in market, followed by 38 percent subscriber growth.",
                "Managed brand and visual consistency across more than 20 consumer and business brands in fashion, beauty, lifestyle and trade, spanning print, social and digital.",
            ],
        },
        {
            "title": "Head of Creative",
            "employer": "Al Arab Newspaper - Doha, Qatar and Cairo, Egypt",
            "dates": "2010 - 2015",
            "bullets": [
                "Led the creative function of a national newspaper, including a full brand redesign and weekly supplements.",
                "Managed and developed the design team, setting and holding brand standards.",
            ],
        },
    ],

    "education": [
        ("Postgraduate Diploma in Professional Marketing, CIM Level 7 - In progress",
         ["Oxford College of Marketing, Chartered Institute of Marketing",
          "Strategic marketing, brand management, marketing planning, customer insight and "
          "marketing measurement and evaluation."]),
        ("Bachelor of Advertising and Graphic Design - 2003",
         ["Faculty of Applied Arts, Helwan University, Cairo, Egypt"]),
    ],

    "skills": (
        "Brand management, brand governance and custodianship, brand guidelines and templates, "
        "brand architecture across group businesses, brand strategy and positioning, design "
        "systems and standards, brand consistency across touchpoints, integrated campaign "
        "development, agency briefing and management, content production management, brand "
        "performance and post-campaign evaluation, budget management, senior stakeholder "
        "management, bilingual Arabic and English brand systems, physical and environmental "
        "brand application, internal brand and employee engagement, corporate publications and "
        "annual reports, AI-powered content creation."
    ),

    "languages": ["Arabic - Native", "English - C2, fluent", "French - A2", "German - A2"],

    "tools": (
        "Adobe InDesign, Adobe Illustrator, Adobe Photoshop, Keynote, PowerPoint, AI generation "
        "and research platforms, Figma (working knowledge, actively developing)."
    ),
}

if __name__ == "__main__":
    build_both(CONTENT, "SaraRadwan_CV_Etihad_BrandManager")
