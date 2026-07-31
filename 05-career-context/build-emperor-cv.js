const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle, LevelFormat
} = require('docx');
const fs = require('fs');

const NAVY = '1A1A1A';
const GREY = '555555';

// ---------- helpers ----------
const name = (t) => new Paragraph({
  spacing: { after: 40 },
  children: [new TextRun({ text: t, bold: true, size: 40, font: 'Calibri', color: NAVY })]
});

const tagline = (t) => new Paragraph({
  spacing: { after: 100 },
  children: [new TextRun({ text: t, size: 22, font: 'Calibri', color: GREY })]
});

const contact = (t) => new Paragraph({
  spacing: { after: 60 },
  children: [new TextRun({ text: t, size: 19, font: 'Calibri', color: NAVY })]
});

const h = (t) => new Paragraph({
  spacing: { before: 260, after: 100 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'BFBFBF', space: 4 } },
  children: [new TextRun({ text: t, bold: true, size: 24, font: 'Calibri', color: NAVY })]
});

const body = (t, after = 90) => new Paragraph({
  spacing: { after, line: 264 },
  children: [new TextRun({ text: t, size: 20, font: 'Calibri', color: NAVY })]
});

const roleTitle = (t) => new Paragraph({
  spacing: { before: 150, after: 20 },
  children: [new TextRun({ text: t, bold: true, size: 21, font: 'Calibri', color: NAVY })]
});

const roleMeta = (t) => new Paragraph({
  spacing: { after: 20 },
  children: [new TextRun({ text: t, size: 19, font: 'Calibri', color: GREY })]
});

const roleDates = (t) => new Paragraph({
  spacing: { after: 70 },
  children: [new TextRun({ text: t, size: 19, font: 'Calibri', color: GREY })]
});

const bullet = (t) => new Paragraph({
  numbering: { reference: 'cv-bullets', level: 0 },
  spacing: { after: 55, line: 264 },
  children: [new TextRun({ text: t, size: 20, font: 'Calibri', color: NAVY })]
});

// ---------- content ----------
const doc = new Document({
  numbering: {
    config: [{
      reference: 'cv-bullets',
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: '•',
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 260, hanging: 180 } } }
      }]
    }]
  },
  sections: [{
    properties: { page: { margin: { top: 850, right: 900, bottom: 850, left: 900 } } },
    children: [

      name('Sara Radwan'),
      tagline('Creative Director  |  Brand, Editorial Systems and Corporate Reporting'),
      contact('Abu Dhabi, United Arab Emirates'),
      contact('[EMAIL]  |  [PHONE]'),
      contact('sarahradwan.me  |  linkedin.com/in/sarahradwan1'),

      h('Profile'),
      body('Creative director with 22 years across Egypt, Qatar and the United Arab Emirates, working where brand, editorial systems and corporate communications meet. Builds and runs publication and typographic systems at national scale, leads multidisciplinary teams across long institutional programmes, and presents and defends creative direction to ministers and executive stakeholders.'),
      body('Native Arabic speaker with hands-on bilingual and multi-script typographic practice: built and applied a national curriculum design system spanning three scripts, and has art directed and set publications in Arabic, English and French. Currently completing CIM Level 7, Postgraduate Diploma in Professional Marketing.', 40),

      h('Selected Capability'),
      body('Arabic and bilingual publishing. Native Arabic, with typographic and layout craft across Arabic, English and French. Built the visual and typographic system for the UAE national curriculum: more than 100 books, five subjects, three scripts, delivered with a large multidisciplinary team.'),
      body('Editorial and publication systems. Twenty-plus consumer and business titles art directed at CPI Media Group. Full redesign and weekly supplements for a national daily newspaper. Interactive ePub editions with embedded multimedia across a full series.'),
      body('Corporate and investor narrative. Brand and investor story for Act Air, an interactive hologram technology company, uniting identity, digital communications and the technology proposition into a single investor-facing narrative.'),
      body('Internal and change communications. Benet7awel for Dubai Municipality: a phased teaser and reveal campaign carrying an entire headquarters through a change of working policy.', 40),

      h('Experience'),

      roleTitle('Senior Art Director, Brand and Creative Lead'),
      roleMeta('WeDo Advertising and Publicity, Abu Dhabi, United Arab Emirates'),
      roleDates('February 2025 to present'),
      bullet('Lead creative vision and delivery for UAE government and institutional clients across brand identity, publications, campaigns and experience, from concept to final delivery.'),
      bullet('Led Benet7awel for Dubai Municipality, an internal change and employee experience campaign carrying the organisation through a move to a Work From Anywhere policy across the entire headquarters: phased teaser and reveal campaigns, employee collateral and props, email communications and physical event setups.'),
      bullet('Own senior client relationships, and present and defend creative direction to ministers and executive stakeholders.'),
      bullet('Contributed to a 12 percent government tender win rate through structured proposal and creative development.'),
      bullet('Lead AI adoption in creative production, including AI usage guidelines written into client brand systems.'),
      bullet('Direct multidisciplinary vendors, production partners and developers across concurrent programmes.'),

      roleTitle('Co-Founder and Creative Director'),
      roleMeta('Social Dar Marketing Management, Dubai, United Arab Emirates'),
      roleDates('August 2021 to June 2024'),
      bullet('Co-founded and led a creative studio, owning creative vision, new business development, pitching and client presentation.'),
      bullet('Directed brand creation and the investor narrative for Act Air, uniting brand identity, digital communications and the technology proposition into a single investor-facing story.'),
      bullet('Led brand architecture across group subsidiaries in the United Arab Emirates, Pakistan, Ukraine and Kenya across a four-year retainer.'),
      bullet('Delivered a two-day brand experience for Dubai’s roads and transport authority end to end, including six bilingual Arabic and English activations, touchscreen kiosks, a registration platform handling more than 250 vacancies, and environmental graphics.'),

      roleTitle('Creative Director and Team Lead, National Curriculum Design System'),
      roleMeta('UAE Ministry of Education, via Ibtikar Edu Tech Solutions'),
      roleDates('2019 to 2021  |  Independent contract, programme value 500,000 euros'),
      bullet('Led a large multidisciplinary team of illustrators, designers and layout specialists to build and apply the visual and typographic system for the national school curriculum: more than 100 books across five subjects and three scripts.'),
      bullet('Held typographic and layout consistency across scripts and subjects at national scale, across print and digital.'),
      bullet('Directed interactive ePub editions with embedded multimedia across the full series.'),

      roleTitle('Creative Director, Event Identity'),
      roleMeta('DAIS 2019, Dubai Sports Council, Dubai, United Arab Emirates'),
      roleDates('2019  |  Independent project'),
      bullet('Led creative direction for the first international AI in Sport conference held in Dubai, applying the identity across environmental signage, press, entry systems and digital touchpoints.'),

      roleTitle('Art Director, Fashion and Beauty Editor'),
      roleMeta('CPI Media Group, Dubai, United Arab Emirates'),
      roleDates('2015 to 2020'),
      bullet('Art directed more than 20 consumer and business titles across fashion, beauty, lifestyle and trade, covering print, social and digital communications.'),
      bullet('Led the MBC magazine rebrand, followed by 38 percent subscriber growth.'),

      roleTitle('Head of Creative'),
      roleMeta('Al Arab Newspaper, Doha, Qatar and Cairo, Egypt'),
      roleDates('2010 to 2015'),
      bullet('Led the creative function of a national daily newspaper, including a full redesign, weekly supplements, and the management and development of the design team.'),

      h('Education'),
      body('Postgraduate Diploma in Professional Marketing, CIM Level 7. In progress.', 30),
      body('Oxford College of Marketing, Chartered Institute of Marketing.'),
      body('Bachelor of Advertising and Graphic Design, 2003.', 30),
      body('Faculty of Applied Arts, Helwan University, Cairo, Egypt.', 40),

      h('Skills'),
      body('Editorial and publication design. Bilingual and multi-script typography. Arabic and English layout. Design systems. Information design and data visualisation. Brand identity systems. Brand architecture. Corporate and investor narrative. Internal communications and employee experience. Change communication campaigns. Creative direction. Multidisciplinary team leadership. Senior stakeholder and executive presentation. New business and pitching. AI usage governance in brand systems.', 40),

      h('Languages'),
      body('Arabic, native. English, C2 fluent. French, A2, with publication and layout experience in French. German, A2 and improving.', 40),

      h('Tools'),
      body('Adobe InDesign, Illustrator and Photoshop. Keynote and PowerPoint. Figma, in active development. AI generation and research platforms.', 40)
    ]
  }]
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync('Sara_Radwan_CV_Emperor.docx', buf);
  console.log('written');
});
