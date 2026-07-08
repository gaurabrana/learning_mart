#!/usr/bin/env python3
"""IT246 (sixth) Unit 4 deck — Ethical Decisions in Software Development & Ethics of IT
Organizations (S17–S21), built to COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule:
every confusable set is a comparison table, every 'X vs not-X' concept a concrete-example table,
claims get scaffolding tables — each table on its OWN slide, paginated, never squeezed. Generous
slide count by design. Self-contained & PDF-safe. Imports deckkit.py. Diagrams in images/.
Run: python3 build_unit4_pptx.py -> IT246_Unit4.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 4 — Ethical Decisions in Software Development & IT Organizations",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S17–S21",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised) — no abstraction without instances. Exports to PDF with no information lost.")

add_outcomes("Unit 4 — Learning Outcomes","software & organizations  ·  s17–s21",
    "By the end of this unit, you will be able to:",
    ["Define software quality and explain why poor quality is costly and sometimes deadly (S17)",
     "Describe concrete strategies — testing, QA, standards, risk management — for quality software (S18)",
     "Evaluate the ethical pros and cons of contingent workers and offshore outsourcing (S19)",
     "Explain when, how, and at what risk to blow the whistle, and what protections exist (S20)",
     "Explain green computing — energy, e-waste, sustainable IT — and the IT org's responsibility (S21)"],
    "This is Unit 4 of IT 246. It turns Unit 1's ethical reasoning and Unit 2's professional duties toward how software is actually BUILT and how IT organizations behave — quality, labour, courage, and sustainability.")

add_roadmap("Unit 4 — Roadmap","Where each session fits (S17–S21)",
    ["S17  Software quality & its importance (incl. safety-critical)",
     "S18  Strategies for quality (testing · QA/QC · standards · risk)",
     "S19  Contingent workers & outsourcing (the ethics)",
     "S20  Whistle-blowing (when, how, at what risk)",
     "S21  Green computing (energy · e-waste · CSR) — closes unit"],
    ["Units 5–8   Cybersecurity & digital forensics",
     "Unit 9   Cyber law in Nepal (ETA, Privacy Act)"])

# ============================================================ S17
add_divider("Session 17 · Lecture hour 1 (of 5)","Software Quality and its Importance",
    "A banking app rounds every transaction down by 1 paisa and quietly pockets the difference; a hospital system shows the wrong patient's blood group. One bug annoys, one kills. So what exactly IS 'quality' software — and who pays when it's missing?",
    "OPENING HOOK [~5 min]. Draw out that 'quality' is more than 'no crash on the demo'. Agenda: what quality is → the cost of poor quality → safety-critical software & famous failures.")

concept_understand("S17 · Concept 1 · [THEORY]","What Is Software Quality",
    "Software quality = the degree to which software meets its stated requirements AND users' real expectations — reliably and safely. A working slogan: quality = conformance to requirements + fitness for use. It has functional and non-functional dimensions.",
    ["Functional quality: it does what the spec says (correctness).",
     "Non-functional quality: reliability over time, usability, security, maintainability.",
     "'Passes the demo' is not quality — it must hold up under real load, over time, for real users.",
     "Fitness for use means it works in the user's actual context, not just the developer's laptop."],
    None,"Quality = does what's required + fit for real use, reliably and safely.",
    "~7 min. Users abandon a wallet app that drops transactions or double-charges, however slick the demo was. Quality is judged in production, not in the pitch.")
add_table_slide("S17 · Concept 1 · scaffolding","The attributes that make up software quality",
    ["Attribute","What it means","Failure example (Nepal / IT)"],
    [["Correctness","Does what the requirements say","A wallet that miscalculates a balance"],
     ["Reliability","Works consistently over time & load","A banking app that crashes every Dashain rush"],
     ["Usability","Real users can actually use it","A govt e-service no ordinary citizen can navigate"],
     ["Security","Protects data & resists attack","An app that leaks KYC data (Unit 2/9)"],
     ["Maintainability","Can be fixed & extended safely","Spaghetti code where each fix breaks two things"],
     ["Performance","Fast enough under real conditions","A tax portal that times out on the deadline day"]],
    per_page=6,widths=[1.6,2.6,2.8],fs=11,
    note="Quality is the WHOLE set, not just 'no visible bug'. A correct app that's insecure or unusable still fails its users.")
concept_apply("S17 · Concept 1 · [THEORY]","What Is Software Quality",
    "An eSewa/Khalti or NIC Asia mobile-banking release is judged on quality in the real world: users abandon a wallet that drops transactions, double-charges, or can't be navigated — no matter how good the launch demo looked. Fitness for the user's actual context (poor network, low-end phones) is part of quality.",
    "\"Quality just means no bugs / it passed the demo.\" Quality includes reliability over time, security, usability, and maintainability — fitness for the user's real context, not a one-off green demo. An app that works once for the developer can still be low-quality for thousands of users on weak networks.",
    "Software quality is the degree to which software meets its stated requirements and users' real expectations, reliably and safely — captured as conformance to requirements plus fitness for use. It spans functional correctness and non-functional attributes (reliability, usability, security, maintainability, performance), and is judged in real production use, not in a demo.",
    "software quality · conformance + fitness for use · functional vs non-functional · reliability · fitness for context")

concept_understand("S17 · Concept 2 · [THEORY]","The Cost of Poor Quality",
    "The cost of poor quality is every cost caused by defects — rework, downtime, lost customers, lawsuits, and reputation damage. The key rule: the cost to fix a defect rises roughly 10× at each later stage (requirements → design → code → release → post-release). Prevention is far cheaper than cure.",
    ["A bug caught while writing requirements is trivial; the same bug found after release is enormously expensive.",
     "The visible cost (a refund, a patch) is the small part; hidden costs (lost trust, support load) dwarf it.",
     "This is why testing and QA (S18) pay for themselves — they move defect-finding earlier.",
     "'We'll fix it in production' is usually the most expensive plan available."],
    "s17_costcurve.png","Fix it in requirements = 1×; fix it after release = 1000×+.",
    "~8 min. Work the Dashain fintech bug: the refund is trivial next to the lost customers, support surge, and reputation hit. That's the real cost.")
add_table_slide("S17 · Concept 2 · examples","The real cost of a defect — visible vs hidden",
    ["Cost","Visible / obvious part","Hidden / larger part"],
    [["A payment bug refunds the wrong users","The refunded amount","Support surge, manual reconciliation, audit"],
     ["An app crashes at peak (Dashain rush)","A patch release","Lost transactions, users switch to a rival"],
     ["A data field is wrong (blood group)","The correction","Possible harm, liability, loss of trust"],
     ["A government e-service glitches on deadline","A hotfix","Citizens flood help desks; trust in e-gov drops"],
     ["A security defect leaks data","The fix + disclosure","Lawsuits, regulatory penalty, brand damage"],
     ["Rushed release with no tests","The rework","Cascading bugs, missed deadline, burnt-out team"]],
    per_page=6,widths=[2.6,2.2,2.6],fs=11,
    note="The visible cost is the tip; the hidden costs (trust, churn, liability, rework) are the iceberg — and they land later, when the fix is 10×–1000× dearer.")
concept_apply("S17 · Concept 2 · [THEORY]","The Cost of Poor Quality",
    "A Kathmandu fintech rushes a Dashain release to beat a rival; a payment bug refunds the wrong users. The refund is the smallest cost: the real bill is the support surge, manual reconciliation, an emergency audit, and — worst — customers who lose trust and switch to a competitor during the busiest season of the year.",
    "\"We'll ship now and fix it in production — it's cheaper.\" The cost to fix rises ~10× per stage, so 'fix it later' is usually the most expensive option. Prevention (early testing, QA) is cheaper than cure, and the hidden costs of a live defect (lost trust, churn) dwarf the visible patch.",
    "The cost of poor quality includes rework, downtime, lost customers, lawsuits, and reputation damage — and it escalates roughly 10× at each later stage of development. Because the hidden costs of a released defect dwarf the visible fix, prevention through early testing and QA is far cheaper than cure. 'Fix it in production' is typically the costliest plan.",
    "cost of poor quality · 10× escalation · prevention vs cure · hidden costs · fix-it-early")

concept_understand("S17 · Concept 3 · [THEORY] [EXAMPLE]","Safety-Critical Software & Famous Failures",
    "Safety-critical software is software whose failure can cause death, injury, or major loss — medical, aviation, transport, power. It ethically demands higher rigour: redundancy, formal verification, and clear accountability. Here 'quality' is not a preference; it is a duty.",
    ["The stakes change the ethics: a bug is no longer 'inconvenient', it is dangerous.",
     "Higher rigour: independent review, redundancy, formal methods, exhaustive testing.",
     "Famous failures show what's at stake: Therac-25, the Boeing 737 MAX MCAS crashes, Ariane 5.",
     "Nepal has safety-critical systems too: power-grid/load-dispatch control, aviation serving TIA, ICU monitoring."],
    None,"Shipping untested safety-critical code = opening a bridge without checking the cables.",
    "~8 min. Therac-25 (radiation overdoses), 737 MAX (MCAS), Ariane 5 (unit-conversion overflow) — each a software failure that killed or cost hugely. The rigour is proportional to the stakes.")
add_table_slide("S17 · Concept 3 · examples","Famous safety-critical software failures — cause & consequence",
    ["System","What went wrong","Consequence"],
    [["Therac-25 (medical)","A race-condition bug + removed hardware interlocks","Patients received massive radiation overdoses; deaths"],
     ["Boeing 737 MAX (aviation)","MCAS acted on one faulty sensor; poor disclosure","Two crashes; 346 deaths; global grounding"],
     ["Ariane 5 (space)","A 64-bit value forced into 16 bits → overflow","Rocket self-destructed seconds after launch"],
     ["Power-grid control (general)","Control-software failure / mis-configuration","Cascading blackouts across regions"],
     ["ICU / patient monitoring","Wrong data shown or alarm missed","Direct risk to patient life"]],
    per_page=5,widths=[1.9,3.0,2.4],fs=11,
    note="Each was a SOFTWARE decision with a physical, sometimes fatal, consequence — the reason safety-critical systems demand redundancy, formal verification, and accountability.")
concept_apply("S17 · Concept 3 · [THEORY] [EXAMPLE]","Safety-Critical Software & Famous Failures",
    "Nepal's safety-critical systems include power load-dispatch/grid control, aviation systems serving TIA, and hospital ICU monitoring. A failure here isn't 'inconvenient' — it's dangerous, exactly like Therac-25 or the 737 MAX. That's why such software ethically requires redundancy, independent verification, and someone accountable for sign-off.",
    "\"A bug is just a bug — we can always patch it.\" In safety-critical software a bug can kill before any patch ships. Shipping untested safety-critical code is like opening a Himalayan bridge without checking the cables because 'it looked fine' — the rigour must match the stakes.",
    "Safety-critical software is software whose failure can cause death, injury, or major loss (medical, aviation, transport, power). It ethically demands higher rigour — redundancy, formal verification, exhaustive testing, and clear accountability — because a defect is dangerous, not merely inconvenient. Famous failures (Therac-25, 737 MAX, Ariane 5) show the human cost of getting it wrong.",
    "safety-critical · redundancy · formal verification · accountability · Therac-25 · 737 MAX · rigour matches stakes")

add_activity("S17 — 'Name the cost'  ·  ~5 min",
    ["In pairs (2 min): name one Nepali app or e-service whose poor quality frustrated you.",
     "List what it cost YOU (time, money, trust) and what it likely cost the PROVIDER.",
     "Take 3–4 answers aloud (3 min); separate visible cost from hidden cost.",
     "Close: notice the hidden costs (lost trust, churn, support load) almost always exceed the visible one."],
    "Seeds: a wallet that double-charged; a tax/PAN portal that timed out on deadline day; a banking app down during a festival. Push students to quantify the hidden cost, not just the visible glitch.",
    "ACTIVITY [~5 min].")
add_quiz("S17 — Quick Check  ·  ~5 min",
    [("Q1.  Software quality is best defined as:","q"),
     ("a) no visible bugs   b) ✅ meeting requirements AND fitness for the user's real use   c) a fast demo   d) nice UI","a"),
     ("     Why: quality spans correctness plus reliability, security, usability — fitness for real use, not just a clean demo.","o"),
     ("Q2.  The cost to fix a defect is generally lowest when found:","q"),
     ("a) after release   b) during the festival rush   c) ✅ early, in requirements/design   d) by users","a"),
     ("     Why: fix-cost rises ~10× per stage, so catching it early is far cheaper — prevention beats cure.","o"),
     ("Discussion: name one Nepali app/e-service whose poor quality frustrated you — what did it cost you and the provider?","o")],
    "QUIZ [~5 min]. Draw out the hidden-cost point and the safety-critical distinction — some failures are annoyances, some are dangers.")
add_summary("S17 · Summary  ·  [~2 min]",
    ["Quality = conformance to requirements + fitness for real use, reliably and safely (not just 'no demo crash').",
     "Poor quality is expensive and the cost rises ~10× per later stage — prevention beats cure.",
     "Safety-critical software (medical, aviation, power) demands extra rigour: failure can kill, not just annoy."],
    "As future developers and PMs in Nepali software houses and BPOs, your name is attached to releases — quality is your professional reputation and, in some systems, someone's safety. The habits you build now decide whether your releases are trusted.",
    "S18 — the concrete strategies that actually produce quality software.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S18
add_divider("Session 18 · Lecture hour 2 (of 5)","Strategies for Developing Quality Software",
    "Two Kathmandu startups build the same app. One 'tests by clicking around before the demo'; the other writes automated tests, has a QA gate, and a release checklist. Six months later only one still has clients. What did the survivor do differently?",
    "OPENING HOOK [~5 min]. Draw out that quality is engineered by process, not hoped for. Agenda: testing → QA vs QC → standards & process models → risk management.")

concept_understand("S18 · Concept 1 · [THEORY]","Testing",
    "Testing is systematically running software to find defects before users do. It has levels — unit → integration → system → acceptance — and can be manual or automated, black-box or white-box. A key truth: testing shows the PRESENCE of bugs, not their absence.",
    ["Unit (each function) → integration (modules together) → system (whole app) → acceptance (user signs off).",
     "Automated tests run on every change (continuous integration), catching regressions instantly.",
     "Black-box tests behaviour (no code view); white-box tests internal logic.",
     "Regression testing re-checks old features so a new fix doesn't silently break them."],
    "s18_pyramid.png","Unit → integration → system → acceptance; automate the base.",
    "~8 min. A Nepali QA/BPO firm runs test cycles for foreign clients; UAT with NRB/the bank precedes a digital-banking go-live. Ad-hoc clicking is not testing.")
add_table_slide("S18 · Concept 1 · scaffolding","The levels of testing",
    ["Level","What it checks","Who / when"],
    [["Unit","Each function/module in isolation","Developer, continuously (often automated)"],
     ["Integration","Modules working together correctly","Developers/QA as parts are joined"],
     ["System","The whole application end-to-end","QA team before release"],
     ["Acceptance (UAT)","Meets the user's real needs","The client/user signs off (e.g. NRB/bank UAT)"]],
    per_page=4,widths=[1.5,2.9,2.9],fs=11.5,
    note="Automate the base (many fast unit tests); reserve slow manual effort for higher levels. 'It works on my machine' is not any of these levels.")
concept_apply("S18 · Concept 1 · [THEORY]","Testing",
    "A Nepali software/QA outsourcing firm in Kathmandu/Lalitpur runs structured test cycles — defined test cases, edge cases, regression suites — for foreign clients, and a bank runs UAT with NRB before a digital-banking go-live. This discipline is exactly what turns 'seems to work' into 'verified to work'.",
    "\"If it works on my machine / passed the demo, it's tested.\" Ad-hoc clicking is not testing: you need defined test cases, edge cases, and regression coverage. A demo exercises the happy path once; real testing hunts the failures users will hit — and proves you looked.",
    "Testing is systematically running software to find defects before users do, across levels (unit, integration, system, acceptance), manual or automated, black-box or white-box, with regression testing guarding old features. Because testing shows the presence of bugs (never proves their absence), it must be structured — defined cases and edge cases — not ad-hoc clicking.",
    "testing · unit/integration/system/acceptance · automated · regression · presence not absence of bugs")

concept_understand("S18 · Concept 2 · [THEORY]","Quality Assurance (QA) vs Quality Control (QC)",
    "QA and QC are different jobs. QA builds the PROCESS that prevents defects (proactive: standards, reviews, audits). QC inspects the PRODUCT to catch defects (reactive: testing, inspection). You need both — one stops defects being made, the other stops them shipping.",
    ["QA is proactive and about the process: coding standards, code reviews, checklists, audits.",
     "QC is reactive and about the product: running tests, inspecting outputs, finding actual defects.",
     "QA reduces how many defects are created; QC catches those that slip through anyway.",
     "Relying on a single heroic manual tester at the end (QC only, no QA) is fragile and unethical."],
    None,"QA prevents defects (process); QC catches them (product). Need both.",
    "~7 min. The 'heroic tester at the end' has no safety net — one sick day and defects ship. QA makes quality repeatable, not dependent on a hero.")
add_table_slide("S18 · Concept 2 · comparison","QA vs QC — process vs product",
    ["Question","Quality Assurance (QA)","Quality Control (QC)"],
    [["Focus","The process that builds software","The finished product"],
     ["Stance","Proactive — prevent defects","Reactive — catch defects"],
     ["Activities","Standards, code reviews, audits, checklists","Testing, inspection, defect logging"],
     ["Goal","Fewer defects are created","Defects don't reach the user"],
     ["Analogy","Designing a clean kitchen & recipes","Tasting each dish before it leaves"]],
    per_page=5,widths=[1.6,2.7,2.7],fs=11,
    note="They are complementary, not alternatives: QA shrinks the defect stream; QC filters what's left. A team with only QC (a heroic end-of-line tester) has no prevention and no safety net.")
concept_apply("S18 · Concept 2 · [THEORY]","Quality Assurance vs Quality Control",
    "A team with zero QA process but one heroic tester who finds everything manually at the end is dangerously fragile: there's no prevention, no documentation, and the whole quality story collapses the day that person is on leave or leaves the company. It's also unethical to rest users' safety on one unsupported individual.",
    "\"We have a great tester, so we have quality covered.\" That's QC only — catching defects, not preventing them. Without QA (standards, reviews, repeatable process), quality is a lottery dependent on one person. Real quality is engineered into the process so it survives any single person leaving.",
    "Quality Assurance (QA) is the proactive process that prevents defects — standards, reviews, audits, checklists — while Quality Control (QC) is the reactive inspection of the product to catch defects through testing and inspection. Both are needed: QA reduces defects created, QC stops those that slip through from reaching users. Relying on QC alone is fragile.",
    "QA (process, preventive) · QC (product, reactive) · both needed · repeatable not heroic")

concept_understand("S18 · Concept 3 · [THEORY]","Software Development Standards & Process Models",
    "Standards and process models are agreed frameworks guiding how software is built and assessed. Quality standards: ISO 9001, ISO/IEC 25010 (a quality model), CMMI maturity levels, IEEE standards. Process models: Waterfall vs Agile/Scrum. Code reviews and documentation run through all of them.",
    ["ISO/IEC 25010 defines the quality attributes; CMMI rates how mature/repeatable your process is.",
     "Waterfall plans everything up front; Agile/Scrum builds in short iterations with continuous feedback.",
     "For Nepali outsourcing firms, ISO/CMMI certification is a BUSINESS requirement to win Western contracts.",
     "Agile changes HOW quality is built in — it does not remove standards, reviews, or documentation."],
    None,"Standards make quality repeatable; certification makes it sellable.",
    "~8 min. Certification is often the ticket to a foreign contract — quality becomes a business asset, not just an ethical one. Bust the 'Agile = no docs' myth.")
add_table_slide("S18 · Concept 3 · scaffolding","Standards & models that guide quality",
    ["Standard / model","What it does","Why it matters"],
    [["ISO 9001","General quality-management system","Signals a disciplined organization"],
     ["ISO/IEC 25010","A software product-quality model","Defines the quality attributes to measure"],
     ["CMMI","Rates process maturity (levels 1–5)","Western clients often require a CMMI level"],
     ["IEEE standards","Engineering practices & documentation","Shared professional baseline"],
     ["Waterfall","Sequential, plan-everything-up-front","Suits stable, well-known requirements"],
     ["Agile / Scrum","Short iterations, continuous feedback","Suits changing requirements; still needs quality practices"]],
    per_page=6,widths=[1.8,2.7,2.5],fs=11,
    note="For Nepali IT-outsourcing firms, ISO/CMMI certification is how you win and keep international contracts — quality becomes a business requirement, not just an ethical one.")
concept_apply("S18 · Concept 3 · [THEORY]","Standards & Process Models",
    "Nepali outsourcing firms pursue ISO / CMMI certification specifically to win Western contracts — foreign clients often won't sign without it. Here quality standards become a business requirement: certification is the entry ticket to higher-value work, and the disciplined process it forces genuinely raises the software's quality.",
    "\"Agile means no documentation and no standards.\" Agile changes HOW quality is built in (short iterations, continuous feedback) but does not remove the need for it — Agile teams still write tests, review code, and document. 'Move fast' is not 'skip quality'; the best Agile teams are rigorous.",
    "Software standards and process models are agreed frameworks for building and assessing software: quality standards (ISO 9001, ISO/IEC 25010, CMMI, IEEE) and process models (Waterfall vs Agile/Scrum), with code reviews and documentation throughout. They make quality repeatable, and for Nepali outsourcing firms ISO/CMMI certification is a business requirement to win international work.",
    "ISO 9001 · ISO/IEC 25010 · CMMI · Waterfall vs Agile · certification as a business asset")

concept_understand("S18 · Concept 4 · [THEORY]","Risk Management",
    "Risk management is identifying, assessing, and mitigating things that could cause failure. Risk is assessed as likelihood × impact; you keep a risk register, plan mitigation and contingency, and prioritise safety-critical risks. It forces the honest ethical question: 'how good is good enough?'",
    ["List risks, score each by likelihood × impact, and rank them (a risk matrix).",
     "For each high risk: a mitigation (reduce it) and a contingency/rollback (if it happens anyway).",
     "Safety-critical risks jump the queue — impact is catastrophic even at low likelihood.",
     "Timing is a mitigation: a bank defers a risky migration off peak festival/remittance days."],
    "s18_riskmatrix.png","Risk = likelihood × impact; mitigate the top-right first.",
    "~7 min. Risk management is checking the weather and carrying a torch BEFORE the trek, not after you're stuck on the pass. Plan the rollback before you need it.")
add_table_slide("S18 · Concept 4 · scaffolding","A risk register in action (likelihood × impact → mitigation)",
    ["Risk","Likelihood × impact","Mitigation / contingency"],
    [["Core-system migration corrupts data","Low × Critical","Test on a copy; schedule off-peak; rollback plan ready"],
     ["Festival-day traffic spike crashes the app","High × High","Load-test early; auto-scale; a caching fallback"],
     ["A third-party payment API goes down","Medium × High","Retry + queue; a secondary provider; user messaging"],
     ["Key developer leaves mid-project","Medium × High","Documentation; pairing; no single point of knowledge"],
     ["Security defect ships to production","Low × Critical","Security review + pen-test gate before release"]],
    per_page=5,widths=[2.6,1.7,2.9],fs=11,
    note="Prioritise by likelihood × impact, but let safety-critical/high-impact risks jump the queue. Every high risk needs BOTH a mitigation and a contingency (rollback).")
concept_apply("S18 · Concept 4 · [THEORY]","Risk Management",
    "A Nepali bank defers a risky core-system migration off peak festival and remittance days, and plans a tested rollback for a Nagarik App update before shipping it. That's risk management: they scored the risk (low likelihood, critical impact), mitigated it (timing, testing), and prepared a contingency in case it fails anyway.",
    "\"We'll deal with problems if they come up.\" Risk management is deciding what could fail BEFORE it does — scoring likelihood × impact, mitigating the worst, and planning rollback in advance. Reacting after a live failure (during the festival rush) is exactly the expensive, dangerous position it exists to avoid.",
    "Risk management identifies, assesses (likelihood × impact), and mitigates things that could cause failure, using a risk register with mitigation and contingency plans and prioritising safety-critical risks. It answers the ethical question 'how good is good enough?' deliberately, before release — for example deferring a risky migration off peak days and preparing a rollback.",
    "risk management · likelihood × impact · risk register · mitigation + contingency · rollback · plan before, not after")

add_activity("S18 — 'Skip testing to hit the deadline?'  ·  ~5 min",
    ["In pairs (2 min): your client demands you skip testing to hit a deadline. Decide the three things you do.",
     "Consider: what you say to the client, what you refuse, and what minimum quality gate you hold.",
     "Take 3 answers aloud (3 min).",
     "Close: link to Unit 1/2 — 'the client told me to' does not transfer the responsibility for a harmful release."],
    "Strong answers: (1) explain the real cost/risk (10× later, possible harm), (2) propose a risk-based minimum (test the critical paths, defer low-risk features), (3) document the decision and who owns the risk. Refusing to skip safety-critical testing is the ethical floor.",
    "ACTIVITY [~5 min].")
add_quiz("S18 — Quick Check  ·  ~5 min",
    [("Q1.  QA differs from QC in that QA is:","q"),
     ("a) product inspection   b) ✅ process-focused / preventive (QC is product/inspection)   c) only testing   d) the same thing","a"),
     ("     Why: QA prevents defects by shaping the process; QC catches them by inspecting the product.","o"),
     ("Q2.  'Risk' in risk management is usually assessed as:","q"),
     ("a) cost only   b) ✅ likelihood × impact   c) number of bugs   d) team size","a"),
     ("     Why: scoring likelihood × impact ranks risks so you mitigate the most dangerous first.","o"),
     ("Discussion: your client demands you skip testing to hit a deadline — what three things do you do?","o")],
    "QUIZ [~5 min]. Reward answers that hold a quality floor for safety-critical paths and document who owns the accepted risk.")
add_summary("S18 · Summary  ·  [~2 min]",
    ["Layered testing (unit→integration→system→acceptance) finds defects early; automate the base.",
     "QA prevents defects (process); QC catches them (product) — you need both, not a lone hero.",
     "Standards (ISO/CMMI) + risk management (likelihood × impact, mitigation + rollback) make quality repeatable."],
    "These are the exact practices Nepali IT-outsourcing firms use to land and keep international clients — knowing them makes you employable, not just ethical. A candidate who can talk testing, QA, and risk stands out immediately.",
    "S19 — the people who build software: contingent workers and outsourcing.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S19
add_divider("Session 19 · Lecture hour 3 (of 5)","Use of Contingent Workers · Outsourcing",
    "A US company posts a job. It's filled by a contractor in Bangalore at one-third the cost, a 'temp' on a 3-month renewable contract in New York, and a small Kathmandu firm doing the back-end. Everyone saved money — but who carries the risk, and is anyone treated unfairly?",
    "OPENING HOOK [~5 min]. Note that most students here will BE the contingent/offshore worker. Agenda: contingent workers → outsourcing & offshoring → the ethical balance (both sides).")

concept_understand("S19 · Concept 1 · [THEORY]","Contingent Workers",
    "Contingent workers are hired on a non-permanent basis — contractors, temps, consultants, gig/freelance, and visa-based (e.g. H-1B) staff. Firms use them for flexibility, cost, and scarce skills. The trade-offs: less loyalty, knowledge loss, under-investment in training, and weaker benefits/protections.",
    ["Why firms like them: scale up/down fast, pay only for what's needed, buy rare skills on demand.",
     "The costs: the worker has little security, few benefits, and no paid leave — the risk shifts to them.",
     "The firm loses too: lower commitment, and institutional knowledge walks out when the contract ends.",
     "There's an ethical duty to treat contingent workers fairly, not just as a cheaper input."],
    "s19_spectrum.png","Permanent → contractor → freelancer → offshore: security ↓, flexibility ↑.",
    "~8 min. Many Nepali developers ARE contingent workers (Upwork/Fiverr, contract-to-foreign-firm): flexible income, but no job security, benefits, or paid leave. Make it personal.")
add_table_slide("S19 · Concept 1 · comparison","Permanent vs contingent — what each side gains and loses",
    ["Dimension","Permanent employee","Contingent worker"],
    [["Job security","High — ongoing role","Low — ends with the contract/gig"],
     ["Benefits / paid leave","Usually provided","Usually none"],
     ["Pay rate","Steady salary","Often higher hourly, but no safety net"],
     ["Loyalty / commitment","Higher","Lower — no long-term stake"],
     ["Institutional knowledge","Retained","Walks out when the contract ends"],
     ["Who carries the risk","Shared with employer","Mostly the worker"]],
    per_page=6,widths=[1.9,2.5,2.6],fs=11,
    note="The model shifts risk from the firm to the worker. That shift is the ethical heart of the debate — flexibility for the firm, insecurity for the person.")
concept_apply("S19 · Concept 1 · [THEORY]","Contingent Workers",
    "Many Nepali developers work as remote contractors or freelancers (Upwork, Fiverr, or contract-to-a-foreign-firm): the income is flexible and often good by local standards, but there's no job security, no benefits, no paid leave, and no protection if the client vanishes. The flexibility the client enjoys is the insecurity the worker absorbs.",
    "\"Contractors are cheaper, so a firm should always use them.\" The hidden costs bite: lost institutional knowledge, lower commitment, constant re-hiring/onboarding, and an ethical duty to treat contingent workers fairly. 'Cheaper per hour' is not 'cheaper overall', and it externalises risk onto people.",
    "Contingent workers are hired non-permanently (contractors, temps, consultants, gig/freelance, visa-based). Firms use them for flexibility, cost, and scarce skills, but the model shifts risk to the worker (weak security, few benefits) and costs the firm loyalty and institutional knowledge. There is an ethical duty to treat them fairly, not merely as a cheaper input.",
    "contingent workers · flexibility vs security · hidden costs · lost institutional knowledge · fair treatment")

concept_understand("S19 · Concept 2 · [THEORY] [EXAMPLE]","Outsourcing & Offshore Outsourcing",
    "Outsourcing is contracting work to an outside firm; offshoring is doing so in another (often lower-cost) country. Benefits: cost savings, 24/7 follow-the-sun work, access to talent. Risks: quality control, communication/timezone gaps, data-security and confidentiality across borders, and dependency.",
    ["Nepal is an outsourcing DESTINATION: Kathmandu IT/BPO/KPO firms serve Western clients — the 'IT export' story.",
     "Follow-the-sun: work continues across time zones, but coordination and quality control get harder.",
     "The sharp risk is data: sending customer data to a country with weaker data-protection law.",
     "Over-dependency on one vendor or client is itself a business risk."],
    None,"Offshoring trades cost for control — and sends your data across a legal border.",
    "~8 min. Nepal both receives outsourcing (as a destination) and sometimes outsources pieces onward. The cross-border data question is the ethical/security crux.")
add_table_slide("S19 · Concept 2 · scaffolding","Offshore outsourcing — benefits vs risks",
    ["Benefit","Matching risk"],
    [["Lower cost","Quality control is harder at a distance"],
     ["24/7 follow-the-sun work","Timezone & communication gaps"],
     ["Access to global talent","Data security/confidentiality across borders"],
     ["Scale up/down quickly","Dependency on one vendor/client"],
     ["Jobs & forex for Nepal","Night shifts, burnout in BPOs"]],
    per_page=5,widths=[1,1],fs=12,
    note="Every benefit has a matching risk. The cross-border DATA risk is the sharpest: obligations to protect customer data don't stop at the border, even if the destination's law is weaker.")
concept_apply("S19 · Concept 2 · [THEORY] [EXAMPLE]","Outsourcing & Offshore Outsourcing",
    "A Western client offshores customer data to a Kathmandu BPO operating under weaker data-protection law. Ethical and security obligations cross the border WITH that data: the client still owes its customers protection, and the Nepali firm inherits a duty to handle KYC/personal data as carefully as if it were local — regardless of what the weaker local law strictly requires.",
    "\"Once we offshore it, the risk and responsibility are the vendor's problem.\" Responsibility travels with the data. If a Kathmandu BPO leaks a Western client's customer data, the client's name and liability are on the line too — outsourcing the work does not outsource the duty of care (echoing S6's client relationship).",
    "Outsourcing contracts work to an outside firm; offshoring does so in another country for cost, follow-the-sun coverage, and talent — with risks of weaker quality control, timezone/communication gaps, cross-border data-security exposure, and dependency. Nepal is a major destination (IT/BPO/KPO export). Crucially, obligations to protect data cross the border with it.",
    "outsourcing · offshoring · follow-the-sun · cross-border data risk · Nepal as destination · duty travels with data")

concept_understand("S19 · Concept 3 · [THEORY]","The Ethical Balance — both sides",
    "The ethics of outsourcing means weighing benefits and harms to ALL stakeholders — home-country workers, offshore workers, clients, and end-users. Pros: jobs and income for developing economies like Nepal, lower prices, efficiency. Cons: home-country job loss, worker exploitation, race-to-the-bottom wages, accountability gaps.",
    ["For Nepal, outsourcing brings genuine high-value jobs and foreign exchange — a real development good.",
     "But it can also mean long night-shift hours for foreign time zones, low pay, and BPO burnout.",
     "For the home country, it can mean job losses and downward wage pressure.",
     "The honest answer isn't 'good' or 'bad' — it's 'good for whom, at what cost, and is it fair?'"],
    None,"Outsourcing is good for whom, at what cost — and is it fair to everyone affected?",
    "~5 min. Analogy: outsourcing is hiring a kitchen across town — cheaper and scalable, but if hygiene slips there, YOUR customers get sick and YOUR name takes the blame.")
add_table_slide("S19 · Concept 3 · comparison","Outsourcing — who benefits and who bears the cost",
    ["Stakeholder","Benefit","Cost / harm"],
    [["Offshore worker (Nepal)","High-value jobs, forex, skills","Night shifts, burnout, lower pay than the client's country"],
     ["Home-country worker","(few)","Job loss, downward wage pressure"],
     ["Client / company","Lower cost, scale, 24/7 coverage","Quality/control risk, accountability gaps"],
     ["End-user / customer","Cheaper products","Their data crosses borders; support quality varies"],
     ["Developing economy","Growth, forex, IT-export industry","Race-to-the-bottom wage pressure"]],
    per_page=5,widths=[2.0,2.3,2.7],fs=11,
    note="A stakeholder view (Unit 1) shows there's no single verdict — outsourcing genuinely helps some and harms others. The ethics is making the trade fair, not pretending there's no cost.")
concept_apply("S19 · Concept 3 · [THEORY]","The Ethical Balance",
    "Nepal's IT-outsourcing industry brings genuine high-value jobs and foreign exchange — a real good for the economy and for individual developers. But it also raises hard questions: fair pay relative to the client's country, long night-shift hours to match foreign time zones, and burnout in BPOs. Both truths hold at once.",
    "\"Outsourcing is simply exploitation\" OR \"outsourcing is simply opportunity.\" Neither is the whole truth. A stakeholder analysis shows it helps some (Nepali developers, clients, the economy) and can harm others (home-country workers, over-worked BPO staff). The ethical task is to make the arrangement fair, not to pick one slogan.",
    "The ethics of outsourcing requires weighing all stakeholders: it brings jobs, income, and forex to developing economies like Nepal and lower prices to clients, while risking home-country job loss, worker exploitation, race-to-the-bottom wages, and accountability gaps. The honest question is not 'good or bad?' but 'good for whom, at what cost, and is it fair?'",
    "ethical balance · stakeholders · jobs + forex vs exploitation · race to the bottom · fairness to all sides")

add_activity("S19 — 'Net good or exploitative?'  ·  ~5 min",
    ["In pairs (2 min): is Nepal being an IT-outsourcing hub mostly good or mostly exploitative for Nepali workers?",
     "List one concrete benefit and one concrete harm, with a real example.",
     "Take 3–4 answers aloud (3 min); place each on a stakeholder map.",
     "Close: the strongest answers name WHO benefits and WHO pays, rather than a one-word verdict."],
    "Benefits: high-value jobs, forex, skills transfer, remote careers from Kathmandu. Harms: night shifts, burnout, pay below the client's country, weak worker protections. Reward stakeholder-aware, both-sides reasoning.",
    "ACTIVITY [~5 min].")
add_quiz("S19 — Quick Check  ·  ~5 min",
    [("Q1.  A key ETHICAL downside of relying on contingent workers is:","q"),
     ("a) they cost more   b) ✅ weaker protections/benefits + lost institutional knowledge   c) they're too loyal   d) none","a"),
     ("     Why: the model shifts risk to the worker (no security/benefits) and drains the firm's retained knowledge.","o"),
     ("Q2.  A major risk specific to OFFSHORE outsourcing is:","q"),
     ("a) higher taxes   b) ✅ data security/confidentiality across borders (+ timezone/quality gaps)   c) too much control   d) none","a"),
     ("     Why: data crosses into a jurisdiction with possibly weaker law, and distance strains quality/coordination.","o"),
     ("Discussion: is Nepal being an IT-outsourcing hub mostly good or mostly exploitative? Argue with examples.","o")],
    "QUIZ [~5 min]. Push for stakeholder reasoning — the point is that outsourcing helps some and harms others simultaneously.")
add_summary("S19 · Summary  ·  [~2 min]",
    ["Contingent work trades the worker's security for the firm's flexibility — and shifts risk onto the worker.",
     "Offshore outsourcing trades cost for control and data-security risk; the duty of care travels with the data.",
     "The ethics means weighing ALL stakeholders — including the offshore worker — not a one-word verdict."],
    "Most of you will BE the contingent or offshore worker — knowing your rights, the risks you carry, and the ethics of the model protects you and shapes how you treat others when you're the one hiring. This is your own career, not an abstraction.",
    "S20 — what to do when you see your organization doing wrong: whistle-blowing.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S20
add_divider("Session 20 · Lecture hour 4 (of 5)","Whistle-Blowing",
    "You discover your company is shipping software you KNOW will leak customers' national-ID data, and management says 'ship it anyway.' Do you stay quiet, quit, or go public — and what happens to YOU if you speak up?",
    "OPENING HOOK [~5 min]. Hold the tension: loyalty to employer vs duty to the public. Agenda: what whistle-blowing is → when/how to do it responsibly → the risks, protections & famous cases.")

concept_understand("S20 · Concept 1 · [THEORY]","What Whistle-Blowing Is",
    "Whistle-blowing is an insider revealing wrongdoing — illegal, unethical, or dangerous conduct — within an organization. It can be INTERNAL (report up the chain or to an ethics officer) or EXTERNAL (regulator, press, public). At its core is a clash: the duty of loyalty to your employer vs the duty to protect the public.",
    ["Internal first: manager, ethics officer, internal audit — give the organization a chance to fix it.",
     "External: a regulator, the press, or the public — when internal channels fail or are the problem.",
     "It resolves the Unit 2 tension: loyalty has a LIMIT — it never requires covering up harm.",
     "It is a considered act to protect stakeholders, not an impulsive betrayal."],
    None,"Whistle-blowing = an insider exposing wrongdoing when loyalty would mean covering up harm.",
    "~7 min. Snowden (NSA surveillance) and Frances Haugen (the Facebook/Meta files) are the canonical public-interest disclosures — note the very different fallout each faced.")
add_table_slide("S20 · Concept 1 · comparison","Internal vs external whistle-blowing — and the 'snitch' myth",
    ["Question","Internal whistle-blowing","External whistle-blowing"],
    [["Who do you tell?","Manager, ethics officer, internal audit","Regulator, press, or the public"],
     ["When?","First — give the org a chance to fix it","When internal channels fail or are complicit"],
     ["Risk to you","Lower, but retaliation still possible","Higher — public exposure, legal risk"],
     ["Is it disloyalty?","No — it protects the org too","No — it protects the public when the org won't"]],
    per_page=4,widths=[1.9,2.6,2.6],fs=11.5,
    note="A whistle-blower is not a disloyal 'snitch' — ethical whistle-blowing protects the public and stakeholders precisely when internal channels have failed.")
concept_apply("S20 · Concept 1 · [THEORY]","What Whistle-Blowing Is",
    "Edward Snowden (NSA mass surveillance) and Frances Haugen (leaking internal Facebook/Meta research on known harms) are the defining public-interest disclosures of the era — insiders who judged that the public's right to know outweighed their duty of loyalty. Their very different receptions show how contested and personally costly the act is.",
    "\"A whistle-blower is just a disloyal snitch.\" Ethical whistle-blowing protects the public and stakeholders when internal channels have failed — it's an act of responsibility, not betrayal. Loyalty to an employer never extends to helping it conceal serious harm (the Unit 2 'loyalty has a limit' idea).",
    "Whistle-blowing is an insider revealing illegal, unethical, or dangerous conduct within an organization — internally (up the chain or to an ethics officer) or externally (regulator, press, public). It resolves the clash between loyalty to the employer and duty to the public: loyalty has a limit and never requires covering up harm, so responsible whistle-blowing is protection, not betrayal.",
    "whistle-blowing · internal vs external · loyalty vs public interest · not a 'snitch' · Snowden · Haugen")

concept_understand("S20 · Concept 2 · [THEORY]","When and How to Blow the Whistle — responsibly",
    "Responsible whistle-blowing is a disciplined, last-resort process — not an impulsive leak. The steps: be sure of the facts and have evidence; confirm the harm is serious; exhaust internal channels first; keep records; seek advice; and go external only when internal routes fail.",
    ["Be sure of the FACTS — reason on evidence, not suspicion; keep dated records.",
     "Confirm the harm is SERIOUS (illegal, dangerous) — not a minor grievance.",
     "Report INTERNALLY first — manager, ethics officer, compliance/audit.",
     "Escalate externally (regulator, then press) only as a last resort when internal routes fail."],
    "s20_flow.png","Evidence-first, internal-first; external is the last step, not the first.",
    "~8 min. A developer at a Nepali bank/gov project escalates to the compliance officer / internal audit before considering the CIAA or the press. The order matters — and protects you.")
add_table_slide("S20 · Concept 2 · scaffolding","The responsible whistle-blowing process",
    ["Step","What you do","Why this order"],
    [["1. Get the facts","Gather evidence; keep dated records","Acting on suspicion alone can be wrong and unprovable"],
     ["2. Weigh the harm","Confirm it's serious (illegal/dangerous)","Whistle-blowing is for real harm, not minor gripes"],
     ["3. Report internally","Manager, ethics officer, internal audit","Give the org a chance to fix it; builds your record"],
     ["4. Escalate to a regulator","e.g. CIAA / the relevant authority","When internal routes are ignored or complicit"],
     ["5. Go public","Press / public — last resort","Highest risk; use only when all else fails"]],
    per_page=5,widths=[1.9,2.6,2.6],fs=11,
    note="Following the order protects both the public AND you — a documented, internal-first attempt is what distinguishes a responsible whistle-blower from a reckless leaker.")
concept_apply("S20 · Concept 2 · [THEORY]","When and How to Blow the Whistle",
    "You suspect, but can't yet prove, that customer data is being sold. The responsible path: gather concrete evidence and keep dated records; confirm the harm is serious; report to your manager, then the ethics/compliance officer or internal audit; if ignored, escalate to a regulator such as the CIAA; and only as a last resort go to the press.",
    "\"If something's wrong, I should immediately post it online / tell the media.\" An impulsive public leak can be legally dangerous, unprovable, and can let the wrongdoer escape on a technicality. Evidence-first and internal-first is both more effective and more defensible — external disclosure is the final step, not the first.",
    "Responsible whistle-blowing is a disciplined, last-resort process: be sure of the facts with evidence, confirm the harm is serious, exhaust internal channels (manager, ethics officer, audit) first, keep records and seek advice, and go external (regulator, then press) only when internal routes fail. The order protects the public and the whistle-blower alike.",
    "responsible process · evidence-first · internal-first · escalate · CIAA · external as last resort")

concept_understand("S20 · Concept 3 · [THEORY] [EXAMPLE]","Risks, Protections & Famous Cases",
    "Whistle-blowing carries real personal cost, and legal shields are limited. Risks: retaliation, firing, blacklisting, lawsuits, and severe stress. Protections: whistle-blower laws/policies, anonymous hotlines, and regulators — but their strength varies hugely by country.",
    ["Common retaliation: being fired, sidelined, blacklisted in a small industry, or sued.",
     "Protections where they exist: statutory whistle-blower laws, anonymous reporting hotlines, regulators.",
     "Nepal's protection is weaker (limited safeguards via anti-corruption/CIAA mechanisms) — real personal risk.",
     "Contrast with stronger US/EU statutes — the same act is far riskier in a weak-protection environment."],
    None,"A whistle-blower is a smoke alarm — annoying until there's a real fire.",
    "~7 min. In a small market like Nepal's, blacklisting is a real threat. Be honest that courage here costs more because the legal net is thinner.")
add_table_slide("S20 · Concept 3 · comparison","Whistle-blowing — the risks vs the (limited) protections",
    ["Risk to the whistle-blower","Protection that may help"],
    [["Being fired or forced out","Whistle-blower laws / employment protections (where they exist)"],
     ["Blacklisting in a small industry","Anonymous reporting hotlines"],
     ["Lawsuits (e.g. defamation)","Solid evidence + legal advice beforehand"],
     ["Retaliation from management","An independent regulator (e.g. CIAA)"],
     ["Severe personal stress","Support networks; documented internal-first record"]],
    per_page=5,widths=[1,1],fs=11.5,
    note="Nepal's protections are limited (anti-corruption/CIAA mechanisms) versus stronger US/EU statutes — so the personal risk is real. Evidence + an internal-first record are your best practical shield.")
concept_apply("S20 · Concept 3 · [THEORY] [EXAMPLE]","Risks, Protections & Famous Cases",
    "In Nepal, whistle-blower protection is limited — safeguards run mainly through anti-corruption/CIAA mechanisms — so a Nepali employee exposing wrongdoing faces real risk of firing and blacklisting, with a thinner legal net than a counterpart in the US or EU. That doesn't make the act wrong; it makes documentation, evidence, and internal-first steps even more important.",
    "\"Whistle-blowers are always protected by law.\" Protection is limited and varies by country — in Nepal it is weak, so retaliation (firing, blacklisting) is a genuine risk. Knowing this lets you act with both courage AND care: strong evidence, an internal-first record, and advice reduce (not eliminate) the danger.",
    "Whistle-blowing carries real risks — retaliation, firing, blacklisting, lawsuits, stress — against limited protections (whistle-blower laws, anonymous hotlines, regulators) whose strength varies by country. Nepal's protections are weaker than US/EU statutes, so the personal risk is significant; evidence and a documented internal-first process are the most reliable practical safeguards.",
    "retaliation · blacklisting · whistle-blower laws · anonymous hotline · weak Nepal protection · courage + care")

add_activity("S20 — 'Would weak protection change your choice?'  ·  ~5 min",
    ["In pairs (2 min): if you found serious wrongdoing at a Nepali employer, would weak legal protection change what you'd do? Be honest.",
     "Map the responsible steps you'd take before going public.",
     "Take 3–4 answers aloud (3 min); discuss the gap between the ideal and the real personal cost.",
     "Close: courage and care aren't opposites — evidence and internal-first steps let you have both."],
    "There's no 'right' answer — reward honesty about the real risk plus a responsible process (evidence, internal-first, seek advice). The point is to think it through BEFORE you're ever in the moment.",
    "ACTIVITY [~5 min].")
add_quiz("S20 — Quick Check  ·  ~5 min",
    [("Q1.  The recommended FIRST step before external whistle-blowing is usually:","q"),
     ("a) call the press   b) ✅ exhaust internal reporting channels with evidence   c) post online   d) quit quietly","a"),
     ("     Why: internal-first (with evidence) gives the org a chance to fix it and builds a defensible record.","o"),
     ("Q2.  A common consequence whistle-blowers face is:","q"),
     ("a) a promotion   b) ✅ retaliation (firing / blacklisting)   c) legal immunity   d) nothing","a"),
     ("     Why: retaliation is the typical cost, and protections are limited — especially in Nepal.","o"),
     ("Discussion: if you found serious wrongdoing at a Nepali employer, would weak legal protection change what you'd do?","o")],
    "QUIZ [~5 min]. Draw out the honest tension between the ethical ideal and the real personal risk under weak protection.")
add_summary("S20 · Summary  ·  [~2 min]",
    ["Whistle-blowing = an insider exposing wrongdoing, internal or external; loyalty has a limit (never cover up harm).",
     "Do it responsibly: evidence-first, internal-first, escalate to a regulator, go public only as a last resort.",
     "Expect real personal risk (retaliation, blacklisting) and know the (limited) protections — weaker in Nepal."],
    "You may one day be the only person who KNOWS — understanding the responsible process and the real risks helps you act with both courage and care, instead of freezing or leaking recklessly. Thinking it through now is what lets you act well later.",
    "S21 — the organization's responsibility to the planet: green computing.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S21
add_divider("Session 21 · Lecture hour 5 (of 5) — CLOSES UNIT 4","Green Computing",
    "Every Google search, every crypto transaction, every old laptop dumped behind a shop in New Road — IT runs on electricity and leaves behind toxic waste. Is 'going digital' actually green, or are we just hiding the smoke?",
    "OPENING HOOK [~5 min]. Bust the 'digital = clean' myth up front. Agenda: what green computing is → energy & sustainable IT → e-waste → corporate responsibility (links to Unit 1 CSR).")

concept_understand("S21 · Concept 1 · [THEORY]","What Green Computing Is",
    "Green computing is designing, using, and disposing of IT in environmentally responsible, energy-efficient ways. It covers the FULL lifecycle — manufacture → use (energy) → disposal — with the goals of lower energy, lower emissions, and less waste.",
    ["It's not just 'buy an efficient laptop' — it spans making, running, and retiring every device.",
     "Manufacture consumes materials and energy; use consumes power; disposal creates e-waste.",
     "Global practice: efficient data centres (good PUE), renewable-powered cloud, ENERGY STAR / EPEAT devices.",
     "'The cloud' is not weightless — it's physical data centres burning real power and water somewhere."],
    "s21_lifecycle.png","Green IT spans the whole lifecycle: make → use → dispose → recycle.",
    "~7 min. The key myth to kill: 'digital has no footprint'. Every search and transaction runs on a physical data centre consuming real electricity.")
add_table_slide("S21 · Concept 1 · scaffolding","The IT lifecycle — environmental impact at each stage",
    ["Lifecycle stage","Environmental impact","Green response"],
    [["Manufacture","Raw materials, water, energy, mining","Durable design; buy only what's needed"],
     ["Use","Electricity for devices, servers, cooling","Efficient hardware, power management, renewables"],
     ["Disposal","Toxic e-waste (lead, mercury, cadmium)","Reduce, reuse, refurbish, recycle safely"],
     ["Recycle / reuse","(closes the loop)","Recover materials; refurbish for a second life"]],
    per_page=4,widths=[1.7,2.9,2.7],fs=11.5,
    note="Green computing addresses ALL stages, not just energy in use. Ignoring manufacture and disposal just hides the footprint elsewhere.")
concept_apply("S21 · Concept 1 · [THEORY]","What Green Computing Is",
    "Nepal has a genuine green-IT opportunity: data centres powered by clean hydro-electricity could be a real 'green data center' selling point for attracting international clients. But the gain is erased if diesel generators kick in during load-shedding — showing green computing must be measured across the real, full lifecycle, not claimed on paper.",
    "\"Software / digital has no environmental footprint — it's 'in the cloud'.\" The cloud is physical data centres burning real electricity and water somewhere. A crypto transaction or an always-on server has a measurable energy and carbon cost. 'Digital' relocates the footprint; it doesn't remove it.",
    "Green computing is designing, using, and disposing of IT in environmentally responsible, energy-efficient ways across the full lifecycle — manufacture, use, and disposal — aiming for lower energy, emissions, and waste. Its foundational point is that IT (including 'the cloud') has a real physical footprint, so responsibility spans making, running, and retiring every device.",
    "green computing · full lifecycle · manufacture/use/disposal · the cloud is physical · lower energy/emissions/waste")

concept_understand("S21 · Concept 2 · [THEORY]","Energy Use & Sustainable IT",
    "Sustainable IT means reducing the power consumed by devices, servers, and data centres. The levers: energy-efficient hardware, virtualization/consolidation, sleep/power management, efficient code, renewable energy, and cooling efficiency.",
    ["Virtualization/consolidation runs many workloads on fewer physical servers — big energy savings.",
     "Power management (sleep, auto-shutdown) cuts the waste of always-on idle machines.",
     "Even efficient code helps: less compute per task means less energy at data-centre scale.",
     "Renewable power and efficient cooling shrink the footprint of the energy that is used."],
    None,"Consolidate servers, sleep idle machines, use clean power, write efficient code.",
    "~8 min. Work the always-on-desktops case: 50 machines left on overnight 'for convenience' is a measurable, avoidable energy and emissions cost.")
add_table_slide("S21 · Concept 2 · scaffolding","Ways to cut IT energy use",
    ["Measure","How it saves energy","Example"],
    [["Efficient hardware","Less power per unit of work","ENERGY STAR / EPEAT-rated devices"],
     ["Virtualization / consolidation","Fewer physical servers running","10 VMs on 1 server instead of 10 boxes"],
     ["Power management","No power wasted on idle machines","Auto-sleep/shutdown of overnight desktops"],
     ["Efficient code","Less compute per task","Optimising a hot query at data-centre scale"],
     ["Renewable energy","Cleaner power for the same use","Hydro-powered data centre (Nepal)"],
     ["Cooling efficiency","Less energy spent removing heat","Better airflow / free-cooling design"]],
    per_page=6,widths=[1.9,2.5,2.6],fs=11,
    note="Nepal's hydropower is a real advantage — but only if backup diesel generators during outages don't erase the gain. Measure the whole picture.")
concept_apply("S21 · Concept 2 · [THEORY]","Energy Use & Sustainable IT",
    "A Kathmandu firm runs 50 always-on desktops overnight 'for convenience'. That's a measurable, needless energy and emissions cost — three easy fixes: enable auto-sleep/shutdown, consolidate what must stay on onto fewer machines/VMs, and switch to efficient (ENERGY STAR) hardware on the next refresh. Convenience was quietly buying a yearly power bill nobody looked at.",
    "\"One office's computers can't matter to the environment.\" At scale, defaults matter enormously — 50 idle machines overnight, multiplied across every office, is real power and real emissions. As the IT decision-maker, your default settings (sleep, consolidation, efficient hardware) shape an organization's whole energy footprint.",
    "Sustainable IT reduces the power consumed by devices, servers, and data centres through efficient hardware, virtualization/consolidation, power management, efficient code, renewable energy, and cooling efficiency. Small defaults scale: idle machines and unoptimised systems waste measurable energy, so an IT decision-maker's choices materially shape an organization's energy and emissions.",
    "sustainable IT · efficient hardware · virtualization · power management · efficient code · renewables · defaults scale")

concept_understand("S21 · Concept 3 · [THEORY] [EXAMPLE]","E-Waste & Responsible Disposal",
    "E-waste is discarded electronics containing toxic materials — lead, mercury, cadmium — that harm health and the environment. Responsible handling follows a ladder: reduce → reuse → refurbish → recycle, plus safe disposal, extended producer responsibility, and data-wiping before disposal.",
    ["Toxins (lead, mercury, cadmium) leach into soil and water when e-waste is dumped or burned.",
     "The ladder: first reduce and reuse/refurbish (extend life), then recycle to recover materials.",
     "Extended producer responsibility: makers take back and handle end-of-life devices.",
     "Wipe data before disposal — a discarded device is also a data-privacy risk (Unit 2)."],
    None,"Reduce → reuse → refurbish → recycle — and wipe your data first.",
    "~8 min. E-waste piles up in Kathmandu with little formal recycling; informal dumping/burning in the valley releases toxins. Weak e-waste regulation makes personal/organizational responsibility matter more.")
add_table_slide("S21 · Concept 3 · examples","E-waste — the toxins and the responsible-disposal ladder",
    ["Item","Why it's hazardous","Responsible handling"],
    [["Old laptop / phone battery","Lead, cadmium, lithium — toxic & fire risk","Reuse/refurbish; recycle via proper handler"],
     ["CRT / old monitor","Contains lead","Never bin/burn; dedicated e-waste recycler"],
     ["Circuit boards","Mercury, heavy metals","Recover materials; specialist recycling"],
     ["Any device with your data","Data-privacy risk on disposal","Wipe/destroy data BEFORE disposal (Unit 2)"],
     ["Still-working old PC","Wasted embodied energy if binned","Donate / refurbish for a second life"],
     ["Imported second-hand device near end-of-life","Becomes junk fast → local e-waste","Reduce imports; plan for disposal"]],
    per_page=6,widths=[2.3,2.3,2.4],fs=11,
    note="The ladder is ordered: reduce → reuse → refurbish → recycle. Dumping or burning e-waste (common in Kathmandu) leaches toxins into soil and water and wastes recoverable materials.")
concept_apply("S21 · Concept 3 · [THEORY] [EXAMPLE]","E-Waste & Responsible Disposal",
    "E-waste accumulates in Kathmandu with little formal recycling — informal dumping and burning in the valley releases lead, mercury, and cadmium into soil and air, and imported second-hand electronics quickly become junk. With weak e-waste regulation in Nepal, responsible disposal falls heavily on organizations and individuals doing the right thing voluntarily.",
    "\"Throwing old electronics in the regular bin is fine.\" E-waste leaches toxins (lead, mercury, cadmium) into soil and water and wastes recoverable materials — it needs dedicated handling. And a binned device is a data-privacy leak too; wipe or destroy the data first, then reduce/reuse/refurbish/recycle.",
    "E-waste is discarded electronics containing toxic materials (lead, mercury, cadmium) that harm health and the environment. Responsible handling follows the ladder reduce → reuse → refurbish → recycle, with safe disposal, extended producer responsibility, and data-wiping first. In Nepal, weak regulation and informal dumping/burning make organizational and individual responsibility especially important.",
    "e-waste · toxic materials · reduce/reuse/refurbish/recycle · extended producer responsibility · wipe data first")

concept_understand("S21 · Concept 4 · [THEORY]","Corporate Responsibility & the IT Organization",
    "An IT organization has a duty to manage its IT footprint as part of CSR — the direct link back to Unit 1. The levers: green procurement policies, take-back/recycling programs, sustainability reporting, telecommuting to cut commute emissions, and cloud right-sizing.",
    ["Green procurement: buy efficient, certified hardware by default — a policy, not a one-off choice.",
     "Take-back/recycling programs give devices a responsible end-of-life.",
     "Sustainability reporting creates accountability you can't quietly walk back (Unit 1's CSR reporting).",
     "Telecommuting and cloud right-sizing cut emissions from commuting and over-provisioned servers."],
    None,"Green IT is CSR in action — policy and reporting, not a one-off gesture.",
    "~5 min. Analogy: ignoring e-waste is like trekkers leaving plastic on the trail to Everest — invisible once you've moved on, but it piles up and poisons the place for everyone after.")
add_table_slide("S21 · Concept 4 · scaffolding","How an IT organization acts green (CSR in practice)",
    ["Measure","What it does","Nepal example"],
    [["Green procurement policy","Buy efficient, certified hardware by default","Govt/bank IT tenders favouring efficient devices"],
     ["Take-back / recycling program","Responsible end-of-life for devices","Telecoms' device take-back schemes"],
     ["Sustainability reporting","Public accountability for the footprint","Reporting energy/e-waste as part of CSR"],
     ["Telecommuting","Cuts commute emissions","Remote/hybrid work reducing daily travel"],
     ["Cloud right-sizing","No paying/powering idle capacity","Scaling servers to actual demand"],
     ["Renewable-powered facilities","Cleaner energy for operations","Solar/hydro-powered data centres"]],
    per_page=6,widths=[2.0,2.5,2.5],fs=11,
    note="This closes the loop to Unit 1: managing the IT footprint IS corporate social responsibility, made real through policy and public reporting rather than one-off gestures.")
concept_apply("S21 · Concept 4 · [THEORY]","Corporate Responsibility & the IT Organization",
    "Telecoms and banks in Nepal adopting solar/energy-efficient data centres and device take-back schemes, and government IT procurement favouring efficient hardware, are green computing as CSR (Unit 1). These are policy-level commitments — defaults for the whole organization — not one-off gestures, which is exactly what makes them credible.",
    "\"Going green is just marketing / a one-off gesture.\" Real green IT is embedded in operations — procurement policy, take-back programs, sustainability reporting, right-sized infrastructure — exactly the genuine-vs-greenwashing test from Unit 1. A single tree-planting photo op isn't green computing; changed defaults and public reporting are.",
    "An IT organization's environmental duty is part of its corporate social responsibility (Unit 1), enacted through green procurement policies, take-back/recycling programs, sustainability reporting, telecommuting, cloud right-sizing, and renewable-powered facilities. Like all CSR, it must be embedded in operations and reported publicly to be genuine rather than greenwashing.",
    "corporate responsibility · CSR · green procurement · take-back · sustainability reporting · embedded not gesture")

add_activity("S21 — 'Trace one device'  ·  ~5 min",
    ["In pairs (2 min): where do your old phones and laptops go right now? Trace one device's likely end-of-life in Nepal.",
     "Note whether the data was wiped, and whether it was reused, recycled, dumped, or burned.",
     "Take 3–4 answers aloud (3 min).",
     "Close: propose one better step for the next device (donate/refurbish, use an e-waste handler, wipe data first)."],
    "Most devices end up in a drawer, resold informally, or dumped — rarely properly recycled or data-wiped. Reward tracing the real path honestly and naming one concrete improvement.",
    "ACTIVITY [~5 min].")
add_quiz("S21 — Quick Check  ·  ~5 min",
    [("Q1.  Green computing covers a device's:","q"),
     ("a) use only   b) purchase only   c) ✅ entire lifecycle: manufacture, use, AND disposal   d) marketing","a"),
     ("     Why: the footprint spans making, running, and retiring a device — not just the energy it uses.","o"),
     ("Q2.  The safest way to handle old electronics is:","q"),
     ("a) the regular bin   b) burn it   c) ✅ reduce/reuse/refurbish/recycle via proper e-waste handling   d) bury it","a"),
     ("     Why: e-waste toxins (lead, mercury, cadmium) need dedicated handling; follow the disposal ladder.","o"),
     ("Discussion: where do your old phones and laptops go right now? Trace one device's likely end-of-life in Nepal.","o")],
    "QUIZ [~5 min]. Connect to Unit 1 CSR and Unit 2 data-privacy (wipe before disposal) — green computing ties the whole course together.")
add_summary("S21 · Summary  ·  [~2 min]",
    ["Green computing spans the whole IT lifecycle (manufacture → use → disposal); 'the cloud' is physical.",
     "Cut energy (efficient hardware, virtualization, power management, renewables) and handle e-waste responsibly.",
     "It's part of an IT organization's CSR — embedded in policy and reporting, not a one-off gesture."],
    "As IT decision-makers you'll choose hardware, run servers, and dispose of devices for whole organizations — your defaults will shape real energy bills and real e-waste in Kathmandu. Green computing is where your professional choices meet the physical world.",
    "Next unit — we shift from ethics to defence: the fundamentals of cybersecurity (Units 5–8).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 4 · Cheat Sheet","One-page revision reference",
    [("Software quality (S17)","Quality = conformance to requirements + fitness for use (reliable, safe). Cost to fix rises ~10× per stage. Safety-critical software (medical/aviation/power) demands extra rigour."),
     ("Quality strategies (S18)","Testing: unit→integration→system→acceptance (automate base). QA = process/preventive; QC = product/reactive. Standards: ISO/CMMI. Risk = likelihood × impact + mitigation/rollback."),
     ("Contingent workers (S19)","Contractors/temps/freelancers/offshore: flexibility for the firm, insecurity for the worker. Hidden costs: lost knowledge, weak protections."),
     ("Outsourcing (S19)","Offshoring trades cost for control + cross-border DATA risk. Duty of care travels with the data. Weigh ALL stakeholders — good for whom, at what cost?"),
     ("Whistle-blowing (S20)","Insider exposing wrongdoing; loyalty has a limit. Responsible = evidence-first, internal-first, escalate, public last. Real risk (retaliation); weak protection in Nepal."),
     ("Green computing (S21)","Whole lifecycle (make→use→dispose). Cut energy (efficient HW, virtualization, renewables); e-waste ladder reduce→reuse→refurbish→recycle (wipe data first). Part of CSR.")])

add_glossary("Unit 4 · Glossary","Key terms — quick reference",
    [("Software quality","conformance to requirements + fitness for real use, reliably and safely."),
     ("Functional vs non-functional","does-what-it-should vs reliability/usability/security/maintainability."),
     ("Cost-to-fix escalation","defect cost rises ~10× at each later stage."),
     ("Safety-critical software","software whose failure can cause death, injury, or major loss."),
     ("Testing","systematically running software to find defects before users do."),
     ("Testing levels","unit → integration → system → acceptance (UAT)."),
     ("Regression testing","re-checking old features so a fix doesn't break them."),
     ("Quality Assurance (QA)","the preventive PROCESS that stops defects being created."),
     ("Quality Control (QC)","the reactive INSPECTION that catches defects in the product."),
     ("ISO/IEC 25010","a software product-quality model."),
     ("CMMI","a process-maturity rating (levels 1–5)."),
     ("Risk (in risk mgmt)","likelihood × impact of something that could cause failure."),
     ("Risk register","a logged, ranked list of risks with mitigation & contingency."),
     ("Contingent worker","a non-permanent worker (contractor, temp, freelancer, visa-based)."),
     ("Outsourcing / offshoring","contracting work to an outside firm / in another country."),
     ("Follow-the-sun","work handed across time zones for 24/7 progress."),
     ("Whistle-blowing","an insider revealing wrongdoing, internally or externally."),
     ("Internal vs external","report up the chain / to an ethics officer vs to a regulator/press."),
     ("Retaliation","firing, blacklisting, or lawsuits against a whistle-blower."),
     ("CIAA","Nepal's Commission for Investigation of Abuse of Authority."),
     ("Green computing","environmentally responsible design/use/disposal of IT."),
     ("IT lifecycle","manufacture → use → disposal → recycle."),
     ("E-waste","discarded electronics with toxic materials (lead, mercury, cadmium)."),
     ("Disposal ladder","reduce → reuse → refurbish → recycle."),
     ("Extended producer responsibility","makers handle their products' end-of-life.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 4 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit4_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Software quality is best defined as   →  ✅ meeting requirements AND fitness for real use","a"),
     ("2.  The cost to fix a defect is lowest when found   →  ✅ early, in requirements/design","a"),
     ("3.  Software whose failure can kill/injure is   →  ✅ safety-critical software","a"),
     ("4.  The testing levels are   →  ✅ unit → integration → system → acceptance","a"),
     ("5.  QA vs QC: QA is   →  ✅ process-focused / preventive (QC is product/inspection)","a"),
     ("6.  In risk management, risk is assessed as   →  ✅ likelihood × impact","a"),
     ("7.  A key ethical downside of contingent workers is   →  ✅ weaker protections + lost knowledge","a"),
     ("8.  A major risk specific to offshore outsourcing is   →  ✅ cross-border data security/confidentiality","a"),
     ("9.  The recommended first step before external whistle-blowing is   →  ✅ exhaust internal channels with evidence","a"),
     ("10.  A common consequence whistle-blowers face is   →  ✅ retaliation (firing/blacklisting)","a"),
     ("11.  Green computing covers a device's   →  ✅ entire lifecycle (manufacture, use, disposal)","a"),
     ("12.  The safest way to handle old electronics is   →  ✅ reduce/reuse/refurbish/recycle via proper e-waste handling","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define software quality + list 3 quality attributes.   14. QA vs QC with one example each.   15. 3 ethical pros + 3 cons of offshore outsourcing.","o"),
     ("16. Outline the responsible steps for whistle-blowing.   17. Why does e-waste need special disposal?","o"),
     ("Section C — Applied case","q"),
     ("18. A Nepali fintech rushes a Dashain release with no QA — identify the quality/risk failures and recommend strategies.","o"),
     ("19. A developer discovers a national-ID data leak at their employer — map the responsible whistle-blowing path and the risks under Nepal's weak protections.","o"),
     ("Section D — Discussion","q"),
     ("20. Is Nepal's growth as an IT-outsourcing destination a net good for Nepali workers AND the environment? Argue both sides, citing outsourcing ethics and green/e-waste concerns.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit4_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 4  ·  IT 246",
          "S17–S21 complete: software quality & its cost · strategies (testing, QA/QC, standards, risk) · contingent workers & outsourcing · whistle-blowing · green computing",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe · Next: Units 5–8 — Cybersecurity & Digital Forensics.")

_add_page_numbers()
save("IT246_Unit4.pptx")
