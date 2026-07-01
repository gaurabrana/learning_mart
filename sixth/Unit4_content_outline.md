# Unit 4 — Ethical Decisions in Software Development & Ethics of IT Organizations · Content Outline

**5 LHs → 5 sessions (S17–S21) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 4 learning outcomes (what students can do after S17–S21)
1. Define software quality and explain why poor quality is costly and sometimes deadly (safety-critical systems).
2. Describe concrete strategies — testing, QA, standards, risk management — for developing quality software.
3. Evaluate the ethical pros and cons of using contingent workers and offshore outsourcing.
4. Explain when, how, and at what risk an IT professional should blow the whistle, and what protections exist.
5. Explain green computing — energy use, e-waste, sustainable IT — and the IT organization's responsibility for it.

---

## S17 — Software Quality and its Importance

**Hook:** "A banking app rounds every transaction down by 1 paisa and quietly pockets the difference; a hospital system shows the wrong patient's blood group. One bug annoys, one kills. So what exactly *is* 'quality' software — and who pays when it's missing?" → quality and its cost.

**Concepts & how each will be filled:**

1. **What is software quality**
   - Definition: the degree to which software meets stated requirements *and* users' real expectations, reliably and safely.
   - Theory: functional vs non-functional quality; correctness, reliability, usability, security, maintainability; "quality = conformance to requirements + fitness for use."
   - Global example: a well-reviewed app vs one with a 1-star "keeps crashing" reputation.
   - Local example: eSewa/Khalti or a NIC Asia mobile-banking release — users abandon a wallet app that drops transactions or double-charges.
   - Misconception: *"Quality just means no bugs / passes the demo."* Correction: quality includes reliability over time, security, and fitness for the user's actual context.

2. **The cost of poor quality**
   - Definition: all costs caused by defects — rework, downtime, lost customers, lawsuits, reputation.
   - Theory: cost-to-fix rises ~10× at each later stage (requirements → design → code → release → post-release); prevention is cheaper than cure.
   - Local example: a glitch in a government e-service (e.g., Nagarik App / online PAN / vehicle tax e-payment) during a deadline rush — citizens flood help desks, trust drops.
   - Mini case: "A Kathmandu fintech rushes a Dashain release to beat a rival; a payment bug refunds the wrong users. Estimate the *real* cost beyond the refund."

3. **Safety-critical software & famous failures**
   - Definition: software whose failure can cause death, injury, or major loss (medical, aviation, transport, power).
   - Theory: higher rigor, redundancy, formal verification, and accountability are ethically required.
   - Global example: Therac-25 radiation overdoses; Boeing 737 MAX MCAS crashes; Ariane 5 launch failure.
   - Local example: load-dispatch / power-grid control software, air-traffic or aviation systems serving TIA, or hospital ICU monitoring — failure here is not "inconvenient," it is dangerous.
   - Fun element: analogy — shipping untested safety-critical software is like opening a Himalayan bridge without checking the cables because "it looked fine."

**Check for understanding:**
- MCQ1: Software quality is best defined as…? → meeting requirements AND fitness for the user's real use ✅
- MCQ2: The cost to fix a defect is generally lowest when found…? → early, in requirements/design ✅
- Discussion: "Name one Nepali app/e-service whose poor quality frustrated you — what did it cost you and the provider?"

**Real-life application:** as future developers/PMs in Nepali software houses and BPOs, your name is attached to releases — quality is your professional reputation and, in some systems, someone's safety.

**Summary:** (1) quality = requirements + fitness for use, reliably and safely; (2) poor quality is expensive and the cost rises later; (3) safety-critical software demands extra rigor. **Next:** the concrete strategies that actually produce quality software.

**Visual cues:** "cost-to-fix escalation" stair/curve across SDLC stages; iceberg graphic (visible bug vs hidden costs below); table of famous failures (system → cause → consequence).

---

## S18 — Strategies for Developing Quality Software

**Hook:** "Two Kathmandu startups build the same app. One 'tests by clicking around before the demo,' the other writes automated tests, has a QA gate, and a release checklist. Six months later only one still has clients. What did the survivor do differently?" → strategies for quality.

**Concepts & how each will be filled:**

1. **Testing**
   - Definition: systematically running software to find defects before users do.
   - Theory: levels (unit → integration → system → acceptance); manual vs automated; black-box vs white-box; regression testing; "testing shows presence of bugs, not their absence."
   - Global example: continuous integration pipelines running thousands of automated tests on every commit.
   - Local example: a Nepali BPO/QA outsourcing firm (e.g., software/QA service companies in Kathmandu/Lalitpur) doing test cycles for foreign clients; UAT with NRB/bank before a digital-banking go-live.
   - Misconception: *"If it works on my machine / passed the demo, it's tested."* Correction: ad-hoc clicking is not testing; you need defined test cases, edge cases, and regression coverage.

2. **Quality Assurance (QA) vs Quality Control (QC)**
   - Definition: QA = building the *process* that prevents defects; QC = inspecting the *product* to catch them.
   - Theory: QA is proactive (standards, reviews, audits), QC is reactive (testing, inspection); both needed.
   - Mini case: "A team has zero QA process but a heroic tester who finds everything manually at the end. Why is this fragile and unethical to rely on?"

3. **Software development standards & process models**
   - Definition: agreed frameworks/standards guiding how software is built and assessed.
   - Theory: ISO 9001 / ISO/IEC 25010 (quality model), CMMI maturity levels, IEEE standards; SDLC models (Waterfall vs Agile/Scrum); code reviews and documentation.
   - Local example: Nepali outsourcing firms pursuing ISO/CMMI certification to win Western contracts — quality standards become a *business* requirement, not just an ethical one.
   - Misconception: *"Agile means no documentation and no standards."* Correction: Agile changes *how* quality is built in, it does not remove the need for it.

4. **Risk management**
   - Definition: identifying, assessing, and mitigating things that could cause failure.
   - Theory: risk = likelihood × impact; risk register, mitigation/contingency, prioritizing safety-critical risks; deciding "how good is good enough" ethically.
   - Local example: a bank deferring a risky core-system migration off peak festival/remittance days; planning rollback for a Nagarik App update.
   - Fun element: analogy — risk management is checking the weather and carrying a torch *before* the trek, not after you're stuck on the pass.

**Check for understanding:**
- MCQ1: QA differs from QC in that QA is…? → process-focused/preventive, QC is product/inspection ✅
- MCQ2: "Risk" in risk management is usually assessed as…? → likelihood × impact ✅
- Discussion: "Your client demands you skip testing to hit a deadline. What three things do you do?"

**Real-life application:** these are the exact practices Nepali IT-outsourcing firms use to land and keep international clients — knowing them makes you employable, not just ethical.

**Summary:** (1) layered testing finds defects early; (2) QA prevents, QC catches; (3) standards + risk management make quality repeatable. **Next:** the people who build software — contingent workers and outsourcing.

**Visual cues:** testing pyramid (unit → integration → system → acceptance); QA-vs-QC two-column table; simple risk matrix (likelihood × impact, color-coded).

---

## S19 — Use of Contingent Workers; Outsourcing

**Hook:** "A US company posts a job. It's filled by a contractor in Bangalore at one-third the cost, a 'temp' on a 3-month renewable contract in New York, and a small Kathmandu firm doing the back-end. Everyone saved money — but who carries the risk, and is anyone treated unfairly?" → contingent work and outsourcing.

**Concepts & how each will be filled:**

1. **Contingent workers**
   - Definition: workers hired on a non-permanent basis — contractors, temps, consultants, gig/freelance, visa-based (e.g., H-1B) staff.
   - Theory: why firms use them (flexibility, cost, scarce skills); trade-offs (less loyalty, knowledge loss, training under-investment, weaker benefits/protections).
   - Global example: H-1B visa debate in the US — accusations of using contract/visa workers to undercut local wages vs genuine skills shortage.
   - Local example: Nepali developers working as remote contractors/freelancers (Upwork, Fiverr, or contract-to-foreign-firm) — flexible income but no job security, benefits, or paid leave.
   - Misconception: *"Contractors are cheaper, so always use them."* Correction: hidden costs — lost institutional knowledge, lower commitment, and ethical duties to fair treatment.

2. **Outsourcing & offshore outsourcing**
   - Definition: contracting work to an outside firm; offshoring = doing so in another country (often lower-cost).
   - Theory: cost savings, 24/7 follow-the-sun work, access to talent vs quality control, communication/timezone gaps, data-security and confidentiality risks, dependency.
   - Local example: Nepal as an outsourcing *destination* — IT/BPO firms in Kathmandu doing software, data entry, KPO and support for Western clients (Nepal's "IT export" story); also Nepali firms outsourcing pieces onward.
   - Mini case: "A Western client offshores customer data to a Kathmandu BPO with weaker data-protection laws. What ethical and security obligations cross the border with that data?"

3. **The ethical balance (both sides)**
   - Definition: weighing benefits and harms to all stakeholders — home workers, offshore workers, clients, end-users.
   - Theory: pros (jobs/income for developing economies like Nepal, lower prices, efficiency) vs cons (home-country job loss, worker exploitation, race-to-the-bottom wages, accountability gaps).
   - Local example: outsourcing brings genuine high-value jobs and forex to Nepal — but raises questions of fair pay, long night-shift hours for foreign timezones, and burnout in BPOs.
   - Fun element: analogy — outsourcing is like hiring a kitchen across town to cook your restaurant's food: cheaper and scalable, but if hygiene slips there, *your* customers get sick and *your* name takes the blame.

**Check for understanding:**
- MCQ1: A key *ethical* downside of relying on contingent workers is…? → weaker protections/benefits + lost institutional knowledge ✅
- MCQ2: A major risk specific to *offshore* outsourcing is…? → data security/confidentiality across borders (+ timezone/quality gaps) ✅
- Discussion: "Is Nepal being an IT-outsourcing hub mostly good or mostly exploitative for Nepali workers? Argue with examples."

**Real-life application:** most of you will *be* the contingent/offshore worker — knowing your rights, the risks you carry, and the ethics of the model protects you and shapes how you treat others.

**Summary:** (1) contingent work trades security for flexibility; (2) offshore outsourcing trades cost for control/security risk; (3) ethics means weighing all stakeholders, including the offshore worker. **Next:** what to do when you see your organization doing something wrong — whistle-blowing.

**Visual cues:** spectrum graphic (permanent ↔ contractor ↔ freelancer ↔ offshore); "who bears the risk?" stakeholder table; world map arrow showing work flowing to Nepal as a destination.

---

## S20 — Whistle-Blowing

**Hook:** "You discover your company is shipping software you *know* will leak customers' national-ID data, and management says 'ship it anyway.' Do you stay quiet, quit, or go public — and what happens to *you* if you speak up?" → whistle-blowing.

**Concepts & how each will be filled:**

1. **What whistle-blowing is**
   - Definition: an insider revealing wrongdoing (illegal, unethical, or dangerous conduct) within an organization.
   - Theory: internal (report up the chain / to an ethics officer) vs external (regulator, press, public); duty of loyalty to employer *vs* duty to protect the public.
   - Global example: Edward Snowden (NSA surveillance) and Frances Haugen (Facebook/Meta internal documents) — public-interest disclosures and their fallout.
   - Misconception: *"A whistle-blower is just a disloyal snitch."* Correction: ethical whistle-blowing protects the public/stakeholders when internal channels fail.

2. **When and how to blow the whistle (responsibly)**
   - Definition: a disciplined, last-resort process — not an impulsive leak.
   - Theory: be sure of the facts and evidence; the harm is serious; exhaust internal channels first; keep records; seek advice; go external only when internal routes fail.
   - Local example: a developer at a Nepali bank/govt project who first escalates to the compliance officer / internal audit before considering CIAA (Commission for Investigation of Abuse of Authority) or the press.
   - Mini case: "You suspect, but can't yet prove, that data is being sold. Walk through the responsible steps before going public."

3. **Risks, protections, and famous cases**
   - Definition: the personal cost of whistle-blowing and the (limited) legal shields.
   - Theory: risks = retaliation, firing, blacklisting, lawsuits, stress; protections = whistle-blower laws/policies, anonymous hotlines, regulators.
   - Local example: Nepal's weaker whistle-blower protection — limited safeguards under anti-corruption/CIAA mechanisms means real personal risk; contrast with stronger US/EU statutes.
   - Fun element: analogy — a whistle-blower is the smoke alarm in a building: annoying when it goes off, but you're glad it exists when there's a real fire — and nobody should rip it off the wall for beeping.

**Check for understanding:**
- MCQ1: The recommended *first* step before external whistle-blowing is usually…? → exhaust internal reporting channels with evidence ✅
- MCQ2: A common consequence whistle-blowers face is…? → retaliation (firing/blacklisting) ✅
- Discussion: "If you found serious wrongdoing at a Nepali employer, would weak legal protection change what you'd do? Be honest."

**Real-life application:** you may one day be the only person who *knows* — understanding the responsible process and the real risks helps you act with both courage and care.

**Summary:** (1) whistle-blowing = exposing wrongdoing, internal or external; (2) do it responsibly, evidence-first, internal-first; (3) expect personal risk and know the (limited) protections. **Next:** the organization's responsibility to the *planet* — green computing.

**Visual cues:** decision flowchart (gather evidence → internal report → escalate → external as last resort); "loyalty vs public interest" balance scale; risk-vs-protection two-column table.

---

## S21 — Green Computing (closes Unit 4)

**Hook:** "Every Google search, every crypto transaction, every old laptop dumped behind a shop in New Road — IT runs on electricity and leaves behind toxic waste. Is 'going digital' actually green, or are we just hiding the smoke?" → green computing.

**Concepts & how each will be filled:**

1. **What green computing is**
   - Definition: designing, using, and disposing of IT in environmentally responsible, energy-efficient ways.
   - Theory: covers the full lifecycle — manufacture → use (energy) → disposal; goals = lower energy, lower emissions, less waste.
   - Global example: hyperscale data centers chasing PEU/PUE efficiency, renewable-powered cloud regions, ENERGY STAR / EPEAT-rated devices.
   - Misconception: *"Software/digital has no environmental footprint — it's 'in the cloud.'"* Correction: the cloud is physical data centers burning real power and water somewhere.

2. **Energy use & sustainable IT**
   - Definition: reducing the power consumed by devices, servers, and data centers.
   - Theory: energy-efficient hardware, virtualization/consolidation, sleep/power management, efficient code, renewable energy, cooling efficiency.
   - Local example: Nepal's hydropower advantage — data centers powered by clean hydro could be a genuine "green data center" selling point; but diesel-generator backup during outages erases the gain.
   - Mini case: "A Kathmandu firm runs 50 always-on desktops overnight 'for convenience.' Estimate the yearly cost and emissions, and propose three fixes."

3. **E-waste & responsible disposal**
   - Definition: discarded electronics containing toxic materials (lead, mercury, cadmium) that harm health and environment.
   - Theory: reduce, reuse, refurbish, recycle; safe disposal; extended producer responsibility; data-wiping before disposal.
   - Local example: e-waste accumulating in Kathmandu with little formal recycling — informal dumping/burning in the valley, and imported second-hand electronics shortening to junk; weak e-waste regulation in Nepal.
   - Misconception: *"Throwing old electronics in the regular bin is fine."* Correction: e-waste leaches toxins into soil/water and wastes recoverable materials — it needs dedicated handling.

4. **Corporate responsibility & the IT organization**
   - Definition: an organization's duty to manage its IT footprint as part of CSR (links back to Unit 1).
   - Theory: green procurement policies, take-back/recycling programs, sustainability reporting, telecommuting to cut commute emissions, cloud right-sizing.
   - Local example: telecoms/banks in Nepal adopting solar/energy-efficient data centers and device take-back schemes; government IT procurement favoring efficient hardware.
   - Fun element: analogy — ignoring e-waste is like trekkers leaving plastic on the trail to Everest: invisible to you once you've moved on, but it piles up and poisons the place for everyone after.

**Check for understanding:**
- MCQ1: Green computing covers a device's…? → entire lifecycle: manufacture, use, AND disposal ✅
- MCQ2: The safest way to handle old electronics is…? → reduce/reuse/refurbish/recycle via proper e-waste handling ✅
- Discussion: "Where do your old phones and laptops go right now? Trace one device's likely end-of-life in Nepal."

**Real-life application:** as IT decision-makers you'll choose hardware, run servers, and dispose of devices for whole organizations — your defaults will shape real energy bills and real e-waste in Kathmandu.

**Summary:** (1) green computing spans the whole IT lifecycle; (2) cut energy and handle e-waste responsibly; (3) it's part of an IT organization's CSR. **Next unit:** we shift from ethics to defense — the fundamentals of cybersecurity.

**Visual cues:** IT lifecycle loop (manufacture → use → dispose → recycle); e-waste hazard infographic (toxic elements → health/soil effects); Nepal "hydro-powered data center" concept graphic.

---

## 📋 Unit 4 — End-of-Unit Quiz (added per your preference)

**Section A — MCQ (10):** definition of software quality; cost-to-fix escalation; safety-critical software examples; testing levels; QA vs QC; risk = likelihood × impact; contingent worker downsides; offshore outsourcing risks; whistle-blowing first step; green computing lifecycle / e-waste handling.
**Section B — Short answer (5):** define software quality and list 3 quality attributes; explain QA vs QC with one example each; list 3 ethical pros and 3 cons of offshore outsourcing; outline the responsible steps for whistle-blowing; explain why e-waste needs special disposal.
**Section C — Applied case (2):** (i) a Nepali fintech rushing a Dashain release with no QA — identify the quality/risk failures and recommend strategies; (ii) a developer who discovers a national-ID data leak at their employer — map the responsible whistle-blowing path and the risks under Nepal's weak protections.
**Section D — Discussion (1):** "Is Nepal's growth as an IT-outsourcing destination a net good for Nepali workers and the environment? Argue both sides, citing outsourcing ethics AND green/e-waste concerns."
*(Full questions + answer key generated with the material.)*

---

## Open questions before I generate Unit 4 material
1. Keep the Nepali examples above (eSewa/Khalti, Nagarik App, Kathmandu BPO/QA firms, CIAA, New Road e-waste, hydro-powered data centers)?
2. For famous failures (S17) and whistle-blower cases (S20), keep the global set (Therac-25, 737 MAX, Snowden, Haugen) or trim to fewer?
3. Same as the other units: keep 2-MCQ + discussion per session **and** the end-of-unit quiz?
