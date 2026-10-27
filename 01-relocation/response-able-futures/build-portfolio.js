const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/163d2ec4-4e2f-49a4-9902-1ca376beed2f_fdb25dfc-e774-4288-8ba0-8291ebf1e90f/pptx/scripts/apply_theme.js");

const OUT = process.argv[2];

const INK = "1F2A2A", MUTED = "6B7472", ACCENT = "B4532A", FRAME = "E6E9E8", FRAMETXT = "6F7977", WHITE = "FFFFFF";
const THEME = {
  name: "Response_Able portfolio",
  headFontFace: "Cambria",
  bodyFontFace: "Arial",
  colors: { dk1: INK, lt1: WHITE, dk2: "2F3B3B", lt2: "F2F4F3", accent1: ACCENT, accent2: "2F5D50", accent3: "8A9A96", accent4: "C9A27E", accent5: "5E7A73", accent6: "D9DEDC", hlink: ACCENT, folHlink: "8A4A2E" },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.title = "Sara Radwan, portfolio";
pres.author = "Sara Radwan";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };

const M = 0.6, W = 13.333, H = 7.5, CW = W - 2 * M;

// Split "[...]" segments into orange italic runs so Sara can see what she must fill.
function rich(str, base) {
  return str.split(/(\[[^\]]*\])/).filter(Boolean).map((seg) => ({
    text: seg,
    options: seg.startsWith("[") ? { ...base, color: ACCENT, italic: true } : { ...base },
  }));
}
// Paragraphs: array of strings -> runs with paragraph breaks.
function paras(list, base, gap = 8) {
  const runs = [];
  list.forEach((p, i) => {
    const r = rich(p, base);
    r[r.length - 1].options.breakLine = i < list.length - 1;
    r.forEach((x) => (x.options.paraSpaceAfter = gap));
    runs.push(...r);
  });
  return runs;
}
function text(slide, runs, o) {
  slide.addText(runs, { isTextBox: true, margin: 0, valign: "top", fontFace: "Arial", color: INK, ...o });
}
function frame(slide, label, x, y, w, h, name) {
  slide.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: FRAME }, line: { type: "none" }, objectName: name || "Image frame" });
  slide.addText(label, { isTextBox: true, x: x + 0.15, y: y + 0.12, w: Math.max(w - 0.3, 0.5), h: 0.6, margin: 0, fontFace: "Arial", fontSize: 10, color: FRAMETXT, valign: "top", objectName: "Image label (delete after adding photo)" });
}
function header(slide, kicker, page) {
  text(slide, rich(kicker, { fontSize: 11, color: MUTED, bold: true, charSpacing: 1 }), { x: M, y: 0.42, w: CW - 1.2, h: 0.3 });
  text(slide, [{ text: `${page} / 6`, options: { fontSize: 11, color: MUTED } }], { x: W - M - 1.0, y: 0.42, w: 1.0, h: 0.3, align: "right" });
}
function headline(slide, t, o = {}) {
  text(slide, [{ text: t, options: { fontFace: "Cambria", fontSize: 34, bold: true, color: INK } }], { x: M, y: 0.85, w: 6, h: 0.75, ...o });
}
function role(slide, s, o) {
  text(slide, rich(s, { fontSize: 12, color: INK }), { ...o });
}
const BODY = { fontSize: 14, color: INK };

// ---------- PAGE 1: curriculum, the problem ----------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  text(s, rich("SARA RADWAN   Designer and creative director since 2003, Cairo to Abu Dhabi. Most of my work is for public institutions: schools, ministries, a newspaper.", { fontSize: 11, color: MUTED }), { x: M, y: 0.32, w: CW, h: 0.3 });
  text(s, rich("01   NATIONAL CURRICULUM   UAE Ministry of Education, 2019 to 2021", { fontSize: 11, color: MUTED, bold: true, charSpacing: 1 }), { x: M, y: 0.85, w: 8, h: 0.3 });
  text(s, [{ text: "1 / 6", options: { fontSize: 11, color: MUTED } }], { x: W - M - 1.0, y: 0.85, w: 1.0, h: 0.3, align: "right" });
  headline(s, "One system,\na hundred books", { y: 1.25, w: 4.6, h: 1.2 });
  text(s, paras([
    "I built the visual and typographic system for the UAE's national school curriculum. Social studies for every grade from KG1 to Grade 12, in student and teacher editions. French at three levels. Two philosophy courses. Covers for music.",
    "A child meets a rule in one book and has to meet it again in the next, in another subject, sometimes another script. Consistency is what lets a young reader stop decoding the page and start learning.",
    "A medication leaflet fails the same way a school book does. That is the problem I want to work on in health.",
  ], BODY, 9), { x: M, y: 2.55, w: 4.6, h: 3.6 });
  role(s, "My role: creative director and team lead. I designed the system and led the illustrators, designers and layout specialists who applied it. [Team size]", { x: M, y: 6.2, w: 4.6, h: 0.75 });
  frame(s, "HERO  One open spread from a social studies book", 5.6, 1.25, 7.133, 4.15, "Hero spread");
  const labels = ["Cover: social studies", "Cover: social studies, teacher edition", "Cover: French", "Cover: philosophy", "Cover: music"];
  const gw = (7.133 - 4 * 0.2) / 5;
  labels.forEach((l, i) => frame(s, l, 5.6 + i * (gw + 0.2), 5.6, gw, 1.35, "Cover " + (i + 1)));
}

// ---------- PAGE 2: curriculum, the decisions ----------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  header(s, "01   NATIONAL CURRICULUM   The decisions", 2);
  headline(s, "Rules a child can rely on", { w: 8 });
  frame(s, "DIAGRAM  One rule set feeding many books: grid, type, colour per subject, student and teacher editions", M, 1.85, 4.3, 3.0, "System diagram");
  frame(s, "Type specimen: hierarchy in both scripts", M, 5.05, 2.05, 1.85, "Type specimen");
  frame(s, "ePub screen", M + 2.25, 5.05, 2.05, 1.85, "ePub screen");
  const cards = [
    ["Two readers, one book", "The student book and the teacher book carry the same content for two different people. [What changed between the editions, and why.]"],
    ["Hierarchy", "[How headings, instructions and activities were told apart, and why.]"],
    ["Two scripts, one grid", "[How Arabic and Latin text shared a page: direction, baseline, what had to give.]"],
    ["Print and screen", "The same system ran in interactive ePub editions with embedded media. [One change you made for screen.]"],
  ];
  const cx = 5.2, cwid = (W - M - cx - 0.3) / 2, ch = 1.95;
  cards.forEach(([t, b], i) => {
    const x = cx + (i % 2) * (cwid + 0.3), y = 1.85 + Math.floor(i / 2) * (ch + 0.2);
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: cwid, h: ch, fill: { color: "F2F4F3" }, line: { type: "none" }, objectName: "Card " + (i + 1) });
    text(s, [{ text: t, options: { fontSize: 15, bold: true, color: INK } }], { x: x + 0.25, y: y + 0.22, w: cwid - 0.5, h: 0.35 });
    text(s, rich(b, BODY), { x: x + 0.25, y: y + 0.65, w: cwid - 0.5, h: ch - 0.8 });
  });
  text(s, rich("What I would do differently now:  [One honest sentence, for example what you would now test with children and teachers.]", { fontSize: 14, color: INK, bold: false }), { x: cx, y: 6.25, w: W - M - cx, h: 0.65 });
}

// ---------- PAGE 3: public experience, the problem ----------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  header(s, "02   PUBLIC EXPERIENCE   Dubai roads and transport authority, [year]", 3);
  frame(s, "HERO  Wide photo of people inside the space, using it. Not the empty set-up.", M, 0.9, 8.0, 3.85, "Hero photo");
  frame(s, "Participatory installation, with people at it", M + 8.2, 0.9, CW - 8.2, 3.85, "Installation photo");
  headline(s, "A government building, opened up", { y: 4.95, w: 6.0, h: 1.3 });
  text(s, paras([
    "The authority wanted [the purpose of the event]. It ran for two days inside their own building, with a registration platform for more than 250 vacancies.",
    "Government buildings tell visitors where they stand before anyone speaks. [Who the visitors were.] I read the brief as a question about how people feel in that building, and what would make them take part.",
  ], { fontSize: 14, color: INK }, 8), { x: 6.85, y: 4.95, w: 5.88, h: 2.0 });
  role(s, "My role: co-founder and creative lead of the studio that delivered it. Concept, identity, on-site direction on both days. [What you designed yourself.]", { x: M, y: 6.3, w: 6.0, h: 0.7 });
}

// ---------- PAGE 4: public experience, the route ----------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  header(s, "02   PUBLIC EXPERIENCE   How it worked", 4);
  headline(s, "Door to registration", { w: 6 });
  text(s, paras([
    "Six bilingual activations, touchscreen kiosks, a secure registration platform, environmental graphics, and a participatory installation where visitors [what visitors did].",
    "Everything was in Arabic and English. [One decision about bilingual signage and screens, and why.] The kiosks had to be [one constraint, for example usable by someone who had never used one].",
  ], BODY, 8), { x: M, y: 1.75, w: 6.6, h: 1.9 });
  frame(s, "Concept sketch or early board", 7.73, 0.85, 5.0, 2.8, "Concept sketch");
  const steps = ["[Arrival]", "[Orientation]", "[Activations]", "[Installation]", "[Registration]"];
  const sw = (CW - 4 * 0.2) / 5;
  steps.forEach((t, i) => {
    const x = M + i * (sw + 0.2);
    frame(s, "Photo for this step", x, 3.95, sw, 1.55, "Step photo " + (i + 1));
    text(s, [{ text: String(i + 1).padStart(2, "0") + "  ", options: { fontSize: 13, bold: true, color: ACCENT } }, ...rich(t, { fontSize: 13, bold: true, color: INK })], { x, y: 5.62, w: sw, h: 0.32 });
  });
  text(s, rich("[Rename the five steps to match the real visitor route. If you draw this route now rather than from the original plans, say so: \"Visitor route, mapped after the event.\"]", { fontSize: 11, color: MUTED }), { x: M, y: 6.0, w: CW, h: 0.35 });
  text(s, rich("Result:  [Registrations, attendance, or what you saw on the day. If there is no figure, one honest observation.]", { fontSize: 14, color: INK }), { x: M, y: 6.45, w: CW, h: 0.5 });
}

// ---------- PAGE 5: Mother, Baby & Child, the problem ----------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  header(s, "03   MOTHER, BABY & CHILD   Consumer health magazine, CPI Media Group, [year]", 5);
  headline(s, "Health information, redesigned for parents", { w: 5.2, h: 1.3 });
  text(s, paras([
    "Mother, Baby & Child is a health magazine for [who the readers were, where, in which language]. I led its rebrand.",
    "[What was wrong before: what made it hard to read, find or trust.]",
    "[What you set out to change, and why.]",
  ], BODY, 9), { x: M, y: 2.3, w: 5.2, h: 2.4 });
  text(s, [{ text: "+38%", options: { fontFace: "Cambria", fontSize: 60, bold: true, color: ACCENT } }], { x: M, y: 4.75, w: 3.0, h: 1.0 });
  text(s, rich("subscriber growth in the period after the rebrand [period]", { fontSize: 12, color: MUTED }), { x: M, y: 5.75, w: 3.6, h: 0.5 });
  role(s, "My role: art director. I led the rebrand. [What you designed yourself, and who else worked on it.]", { x: M, y: 6.3, w: 5.2, h: 0.7 });
  frame(s, "BEFORE  Cover of the old magazine", 6.2, 0.85, 3.165, 6.1, "Before cover");
  frame(s, "AFTER  Cover after the rebrand", 9.565, 0.85, 3.165, 6.1, "After cover");
}

// ---------- PAGE 6: Mother, Baby & Child, inside ----------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  header(s, "03   MOTHER, BABY & CHILD   What changed", 6);
  headline(s, "Inside the pages", { w: 6 });
  frame(s, "BEFORE  An inside spread from the old magazine", M, 1.85, 5.95, 2.6, "Before spread");
  frame(s, "AFTER  The same kind of spread after the rebrand", M + 6.18, 1.85, 5.95, 2.6, "After spread");
  const dec = [
    ["[Decision 1]", "[For example: how a parent finds the section they need.]"],
    ["[Decision 2]", "[For example: how advice, warnings and facts were told apart.]"],
    ["[Decision 3]", "[For example: how the photography or illustration changed.]"],
  ];
  const dw = (CW - 2 * 0.3) / 3;
  dec.forEach(([t, b], i) => {
    const x = M + i * (dw + 0.3);
    text(s, rich(t, { fontSize: 15, bold: true, color: INK }), { x, y: 4.7, w: dw, h: 0.35 });
    text(s, rich(b, BODY), { x, y: 5.1, w: dw, h: 0.9 });
  });
  text(s, rich("What I learned:  [One sentence in your words. What this project taught you about designing health information, and what you would now test with readers.]", { fontSize: 14, color: INK }), { x: M, y: 6.2, w: CW, h: 0.7 });
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
