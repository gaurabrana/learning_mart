# IT 246 — Unit 4: Ethical Decisions in Software Development & Ethics of IT Organizations
### Full Lecturer-Ready Session Material (S17–S21)

**Program:** BIM, 6th Semester · **Unit weight:** 5 lecture hours
**Sessions:** S17–S21 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT246_Unit4.pptx` (80 slides), regenerated via `build_unit4_pptx.py` (imports `deckkit.py`).

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each
> session has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just
> bullets), **worked examples**, a **timed in-class activity**, and lecturer cue cards in
> `> 🎙️` blocks. `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags:
> `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.**

---

## Unit 4 — Learning Outcomes
By the end of this unit, students will be able to:
1. Define software quality and explain why poor quality is costly and sometimes deadly (safety-critical systems).
2. Describe concrete strategies — testing, QA, standards, risk management — for developing quality software.
3. Evaluate the ethical pros and cons of using contingent workers and offshore outsourcing.
4. Explain when, how, and at what risk an IT professional should blow the whistle, and what protections exist.
5. Explain green computing — energy use, e-waste, sustainable IT — and the IT organization's responsibility for it.

---
---

# S17 — Software Quality and its Importance
**Lecture hour 1 of 5 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"One bug annoys, one kills"**

> **Deliver (≈2 min):** Put two failures side by side and read them slowly.
> 1. A **banking app rounds every transaction down by 1 paisa** and quietly pockets the difference.
> 2. A **hospital system shows the wrong patient's blood group.**
>
> **Run a quick reaction (≈3 min):** "Both are 'just software bugs.' But **one annoys and one
> kills** — so what exactly *is* 'quality' software, and **who pays when it's missing?**" Take a few
> answers. Most students say "quality = no bugs" or "it passed the demo." Land the surprise: **quality
> is far more than surviving a demo** — it's reliability over time, security, usability, and, in some
> systems, **someone's life.** That's the theme of today: **what quality is → the cost of poor
> quality → safety-critical software and famous failures.**

> 🎙️ Speaker note: Don't resolve "what is quality" yet — the point is to shake the "no visible bug =
> quality" reflex. Write the agenda on the board: what quality is → cost of poor quality →
> safety-critical software & famous failures.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Is Software Quality `[THEORY]` `[~10 min]`

[SLIDE] **Conformance + fitness for use**

> **Deliver:** Give the definition and write it on the board. **Software quality = the degree to
> which software meets its stated requirements AND users' real expectations — reliably and safely.**
> The working slogan students should memorise: **quality = conformance to requirements + fitness for
> use.** Then split it into two dimensions:
> - **Functional quality** — it **does what the spec says** (correctness).
> - **Non-functional quality** — **reliability over time, usability, security, maintainability,
>   performance.**
>
> Hammer the key move: **"passes the demo" is NOT quality.** A demo exercises the happy path once, on
> the developer's laptop. Quality is judged **in production** — under real load, over time, for real
> users on weak networks and low-end phones. **Fitness for use** means it works in the **user's actual
> context**, not the developer's ideal one.

- 🇳🇵 **Local example (walk through it):** an **eSewa / Khalti** or **NIC Asia mobile-banking**
  release is judged on quality **in the real world.** Users abandon a wallet that **drops
  transactions, double-charges, or can't be navigated** — no matter how slick the launch demo looked.
  Fitness for the user's context (poor network, cheap phone) **is** part of quality.

> ❌ **Common misconception:** *"Quality just means no bugs / it passed the demo."*
> ✅ **Correction — say it out loud:** "Quality includes **reliability over time, security, usability,
> and maintainability** — fitness for the user's real context, not a one-off green demo. An app that
> works **once** for the developer can still be **low-quality** for thousands of users on weak
> networks."

> 🎙️ Speaker note: Quality is judged **in production, not in the pitch.** Keep returning to the
> conformance-plus-fitness slogan — it's the frame for the whole unit.

**📊 Depth table — The attributes that make up software quality**

| Attribute | What it means | Failure example (Nepal / IT) |
|---|---|---|
| Correctness | Does what the requirements say | A wallet that miscalculates a balance |
| Reliability | Works consistently over time & load | A banking app that crashes every Dashain rush |
| Usability | Real users can actually use it | A govt e-service no ordinary citizen can navigate |
| Security | Protects data & resists attack | An app that leaks KYC data (Unit 2/9) |
| Maintainability | Can be fixed & extended safely | Spaghetti code where each fix breaks two things |
| Performance | Fast enough under real conditions | A tax portal that times out on the deadline day |

*ℹ️ Quality is the WHOLE set, not just 'no visible bug'. A correct app that's insecure or unusable still fails its users.*

#### Concept 2 — The Cost of Poor Quality `[THEORY]` `[EXAMPLE]` `[~10 min]`

[SLIDE] **The iceberg — visible fix, hidden cost**

> **Deliver:** Define it plainly. **The cost of poor quality is every cost caused by defects** —
> **rework, downtime, lost customers, lawsuits, and reputation damage.** Then teach the single rule
> students must remember: **the cost to fix a defect rises roughly 10× at each later stage**
> (requirements → design → code → release → post-release). A bug caught **while writing requirements
> is trivial**; the **same bug found after release is enormously expensive.**
>
> Draw the iceberg: the **visible cost** (a refund, a patch) is the **small tip**; the **hidden
> costs** — lost trust, support surge, churn, liability — are the **huge mass below the water**, and
> they **land later, when the fix is dearest.** This is exactly **why testing and QA (S18) pay for
> themselves** — they move defect-finding **earlier.** "We'll fix it in production" is usually the
> **most expensive plan available.**

- 🇳🇵 **Mini case (work it, ≈2 min):** a **Kathmandu fintech rushes a Dashain release to beat a
  rival**; a payment bug **refunds the wrong users.** Ask: "estimate the *real* cost." Draw it out —
  the **refund is the smallest cost.** The real bill is the **support surge, manual reconciliation, an
  emergency audit**, and — worst — **customers who lose trust and switch to a competitor during the
  busiest season of the year.**
- 🇳🇵 **Local example:** a glitch in a **government e-service** (Nagarik App / online PAN / vehicle
  tax e-payment) during a **deadline rush** — citizens **flood the help desks** and **trust in
  e-government drops.** The hotfix is cheap; the lost trust is not.

> ❌ **Misconception:** *"We'll ship now and fix it in production — it's cheaper."*
> ✅ **Correction:** "The cost to fix rises **~10× per stage**, so 'fix it later' is usually the **most
> expensive** option. **Prevention (early testing, QA) is cheaper than cure**, and the **hidden costs**
> of a live defect (lost trust, churn) **dwarf the visible patch.**"

> 🖼️ Visual: a **cost-to-fix escalation** stair/curve — fix in requirements = 1×, fix after release =
> 1000×+ — with the iceberg overlay (visible fix above the water, hidden costs below).

> 🎙️ Speaker note: Anchor everything on the Dashain fintech case. The refund is the tip; the surge,
> reconciliation, audit, and churn are the iceberg — and they arrive when the fix is 10×–1000× dearer.

**📊 Depth table — The real cost of a defect — visible vs hidden**

| Cost | Visible / obvious part | Hidden / larger part |
|---|---|---|
| A payment bug refunds the wrong users | The refunded amount | Support surge, manual reconciliation, audit |
| An app crashes at peak (Dashain rush) | A patch release | Lost transactions, users switch to a rival |
| A data field is wrong (blood group) | The correction | Possible harm, liability, loss of trust |
| A government e-service glitches on deadline | A hotfix | Citizens flood help desks; trust in e-gov drops |
| A security defect leaks data | The fix + disclosure | Lawsuits, regulatory penalty, brand damage |
| Rushed release with no tests | The rework | Cascading bugs, missed deadline, burnt-out team |

*ℹ️ The visible cost is the tip; the hidden costs (trust, churn, liability, rework) are the iceberg — and they land later, when the fix is 10×–1000× dearer.*

#### Concept 3 — Safety-Critical Software & Famous Failures `[THEORY]` `[EXAMPLE]` `[~10 min]`

[SLIDE] **When a bug is dangerous, not inconvenient**

> **Deliver:** Define the category. **Safety-critical software is software whose failure can cause
> death, injury, or major loss** — **medical, aviation, transport, power.** Here the ethics **changes**:
> a bug is **no longer 'inconvenient' — it is dangerous.** So safety-critical software **ethically
> demands higher rigour**: **redundancy, formal verification, exhaustive testing, independent review,
> and clear accountability.** In this class of system, **"quality" is not a preference; it is a duty.**
>
> Then make the stakes concrete with the famous failures — each a **software decision with a physical,
> sometimes fatal, consequence**: **Therac-25**, the **Boeing 737 MAX MCAS** crashes, and **Ariane 5.**
> The rigour must be **proportional to the stakes.**

- 🌍 **Global examples:** **Therac-25** (a race-condition bug plus removed hardware interlocks →
  massive radiation overdoses, deaths); **Boeing 737 MAX** (MCAS acted on **one faulty sensor** with
  poor disclosure → two crashes, **346 deaths**, global grounding); **Ariane 5** (a 64-bit value
  forced into 16 bits → overflow → rocket self-destructed seconds after launch).
- 🇳🇵 **Local example:** Nepal has safety-critical systems too — **power load-dispatch / grid
  control** software, **aviation systems serving TIA**, and **hospital ICU / patient monitoring.** A
  failure here isn't "inconvenient" — it's **dangerous**, exactly like Therac-25 or the 737 MAX. That
  is why such software **ethically requires** redundancy, independent verification, and **someone
  accountable for sign-off.**

> ❌ **Misconception:** *"A bug is just a bug — we can always patch it."*
> ✅ **Correction:** "In safety-critical software a bug can **kill before any patch ships.** The rigour
> must **match the stakes** — you can't 'fix it in production' when production is an ICU or a cockpit."

> 🍿 **Fun analogy (deliver it):** "Shipping untested safety-critical software is like **opening a
> Himalayan bridge without checking the cables because 'it looked fine.'** It probably will look fine —
> right up until the moment it doesn't, and by then people are on it."

> 🖼️ Visual: a **famous-failures table** graphic (system → cause → consequence) — Therac-25, 737 MAX,
> Ariane 5 — driving home that each was a *software* decision with a physical outcome.

> 🎙️ Speaker note: Therac-25 (radiation overdoses), 737 MAX (MCAS on one sensor), Ariane 5 (overflow).
> Each killed or cost hugely. Keep repeating: the rigour is **proportional to the stakes.**

**📊 Depth table — Famous safety-critical software failures — cause & consequence**

| System | What went wrong | Consequence |
|---|---|---|
| Therac-25 (medical) | A race-condition bug + removed hardware interlocks | Patients received massive radiation overdoses; deaths |
| Boeing 737 MAX (aviation) | MCAS acted on one faulty sensor; poor disclosure | Two crashes; 346 deaths; global grounding |
| Ariane 5 (space) | A 64-bit value forced into 16 bits → overflow | Rocket self-destructed seconds after launch |
| Power-grid control (general) | Control-software failure / mis-configuration | Cascading blackouts across regions |
| ICU / patient monitoring | Wrong data shown or alarm missed | Direct risk to patient life |

*ℹ️ Each was a SOFTWARE decision with a physical, sometimes fatal, consequence — the reason safety-critical systems demand redundancy, formal verification, and accountability.*

#### 🛠 ACTIVITY — "Name the cost" `[ACTIVITY]` `[~5 min]`

[SLIDE] **A Nepali app whose poor quality frustrated you**

> **Run it:** In pairs (2 min), each student names **one Nepali app or e-service whose poor quality
> frustrated them.** They list what it cost **YOU** (time, money, trust) and what it likely cost the
> **PROVIDER.** Take **3–4 answers aloud** (3 min) and, for each, **separate the visible cost from the
> hidden cost.** Seeds: a **wallet that double-charged**; a **tax/PAN portal that timed out on deadline
> day**; a **banking app down during a festival.** Close: "Notice the **hidden costs (lost trust,
> churn, support load) almost always exceed the visible one.**"

> 🎙️ Speaker note: Push students to **quantify the hidden cost**, not just describe the visible glitch.
> The recurring lesson — hidden cost > visible cost — sets up why S18's strategies pay for themselves.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Software quality is best defined as:
a) no visible bugs b) ✅ **meeting requirements AND fitness for the user's real use** c) a fast demo d) nice UI

**MCQ 2.** The cost to fix a defect is generally lowest when found:
a) after release b) during the festival rush c) ✅ **early, in requirements/design** d) by users

**Discussion prompt:** *Name one Nepali app / e-service whose poor quality frustrated you — what did it cost you and the provider?*

> 🎙️ Speaker note: Draw out the **hidden-cost** point and the **safety-critical distinction** — some
> failures are annoyances, some are dangers. Reward students who separate visible from hidden cost.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** as future **developers and PMs in Nepali software houses and BPOs**, your
**name is attached to releases** — quality is your **professional reputation** and, in some systems,
**someone's safety.** The habits you build now decide whether your releases are **trusted or dreaded**:
a track record of solid, well-tested work follows you across a small IT market, and so does a
reputation for shipping breakage.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Quality = conformance to requirements + fitness for real use**, reliably and safely — **not just "no demo crash."**
2. **Poor quality is expensive** and the cost rises **~10× per later stage** — **prevention beats cure**; hidden costs dwarf the visible fix.
3. **Safety-critical software** (medical, aviation, power) demands **extra rigour** — failure can **kill, not just annoy.**

**Next session (S18):** the concrete **strategies** that actually **produce** quality software.

---
---

# S18 — Strategies for Developing Quality Software
**Lecture hour 2 of 5 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Two startups, same app — only one survives"**

> **Deliver (≈2 min):** Set up the contrast. "**Two Kathmandu startups build the same app.** One
> **'tests by clicking around before the demo.'** The other **writes automated tests, has a QA gate,
> and a release checklist.**"
>
> **Run the question (≈3 min):** "Six months later, **only one still has clients.** What did the
> survivor do **differently?**" Take a few answers. Land it: **quality is engineered by process, not
> hoped for.** The survivor didn't get lucky — it built **testing, QA, standards, and risk management**
> into how it works. Those four are today's agenda: **testing → QA vs QC → standards & process models
> → risk management.**

> 🎙️ Speaker note: The theme is that quality is **built in deliberately**, never left to luck or a
> hero. Agenda on the board: testing → QA vs QC → standards & process models → risk management.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Testing `[THEORY]` `[~8 min]`

[SLIDE] **Levels: unit → integration → system → acceptance**

> **Deliver:** Define it. **Testing is systematically running software to find defects before users
> do.** Teach the **levels** as a ladder:
> - **Unit** — each function/module in isolation (developer, continuously, often automated).
> - **Integration** — modules working together correctly.
> - **System** — the whole application end-to-end.
> - **Acceptance (UAT)** — meets the user's real needs; the **client/user signs off.**
>
> Then the distinctions: tests can be **manual or automated** (automated tests run on **every change**
> — continuous integration — catching **regressions** instantly); **black-box** (tests behaviour, no
> code view) vs **white-box** (tests internal logic); and **regression testing** re-checks old features
> so a new fix **doesn't silently break them.** Deliver the famous truth: **testing shows the PRESENCE
> of bugs, not their absence** — so it must be **structured**, not ad-hoc.

- 🇳🇵 **Local example:** a **Nepali software / QA outsourcing firm in Kathmandu / Lalitpur** runs
  **structured test cycles** — defined test cases, edge cases, regression suites — for **foreign
  clients**, and a **bank runs UAT with the NRB** before a **digital-banking go-live.** This discipline
  is exactly what turns **"seems to work" into "verified to work."**

> ❌ **Common misconception:** *"If it works on my machine / passed the demo, it's tested."*
> ✅ **Correction:** "**Ad-hoc clicking is not testing.** You need **defined test cases, edge cases,
> and regression coverage.** A demo exercises the happy path **once**; real testing **hunts the
> failures users will hit** — and **proves you looked.**"

> 🖼️ Visual: the **testing pyramid** — many fast **unit** tests at the base, then **integration**,
> **system**, and a thin **acceptance** tip; automate the base.

> 🎙️ Speaker note: "It works on my machine" is **none** of the four levels. Automate the base so slow
> manual effort is reserved for higher levels.

**📊 Depth table — The levels of testing**

| Level | What it checks | Who / when |
|---|---|---|
| Unit | Each function/module in isolation | Developer, continuously (often automated) |
| Integration | Modules working together correctly | Developers/QA as parts are joined |
| System | The whole application end-to-end | QA team before release |
| Acceptance (UAT) | Meets the user's real needs | The client/user signs off (e.g. NRB/bank UAT) |

*ℹ️ Automate the base (many fast unit tests); reserve slow manual effort for higher levels. 'It works on my machine' is not any of these levels.*

#### Concept 2 — Quality Assurance (QA) vs Quality Control (QC) `[THEORY]` `[~7 min]`

[SLIDE] **Process vs product — prevent vs catch**

> **Deliver:** These are **different jobs**, and students constantly conflate them.
> - **QA (Quality Assurance)** builds the **PROCESS that PREVENTS defects** — **proactive**: coding
>   standards, code reviews, checklists, audits.
> - **QC (Quality Control)** inspects the **PRODUCT to CATCH defects** — **reactive**: running tests,
>   inspection, defect logging.
>
> Say the one-liner: **QA reduces how many defects are created; QC catches those that slip through
> anyway.** You need **both** — one stops defects being *made*, the other stops them *shipping.* Then
> deliver the warning: relying on a **single heroic manual tester at the end** (QC only, no QA) is
> **fragile and unethical** — one sick day and defects ship.

- 🇳🇵 **Mini case (work it, ≈2 min):** a team has **zero QA process** but **one heroic tester** who
  finds everything manually at the end. Ask: "why is this **fragile and unethical** to rely on?" Draw
  it out — there's **no prevention, no documentation**, and the whole quality story **collapses the
  day that person is on leave or leaves the company.** It is also **unethical** to rest users' safety
  on **one unsupported individual.**

> ❌ **Misconception:** *"We have a great tester, so we have quality covered."*
> ✅ **Correction:** "That's **QC only** — catching defects, not **preventing** them. Without **QA**
> (standards, reviews, a repeatable process), quality is a **lottery dependent on one person.** Real
> quality is **engineered into the process** so it **survives any single person leaving.**"

> 🎙️ Speaker note: The "heroic tester" has **no safety net.** QA makes quality **repeatable**, not
> **heroic.** Use the kitchen analogy from the table: QA designs a clean kitchen; QC tastes each dish.

**📊 Depth table — QA vs QC — process vs product**

| Question | Quality Assurance (QA) | Quality Control (QC) |
|---|---|---|
| Focus | The process that builds software | The finished product |
| Stance | Proactive — prevent defects | Reactive — catch defects |
| Activities | Standards, code reviews, audits, checklists | Testing, inspection, defect logging |
| Goal | Fewer defects are created | Defects don't reach the user |
| Analogy | Designing a clean kitchen & recipes | Tasting each dish before it leaves |

*ℹ️ They are complementary, not alternatives: QA shrinks the defect stream; QC filters what's left. A team with only QC (a heroic end-of-line tester) has no prevention and no safety net.*

#### Concept 3 — Software Development Standards & Process Models `[THEORY]` `[~8 min]`

[SLIDE] **Standards make quality repeatable — and sellable**

> **Deliver:** Define them. **Standards and process models are agreed frameworks guiding how software
> is built and assessed.** Split them:
> - **Quality standards:** **ISO 9001** (a general quality-management system), **ISO/IEC 25010** (a
>   software product-quality model that defines the quality attributes to measure), **CMMI** (rates
>   process maturity, levels 1–5), and **IEEE standards** (engineering practices & documentation).
> - **Process models:** **Waterfall** (sequential, plan everything up front — suits stable
>   requirements) vs **Agile / Scrum** (short iterations, continuous feedback — suits changing
>   requirements). **Code reviews and documentation** run through **all** of them.
>
> Land the business point: for **Nepali outsourcing firms, ISO / CMMI certification is a BUSINESS
> requirement to win Western contracts** — quality becomes a **business asset**, not just an ethical
> one. Standards make quality **repeatable**; certification makes it **sellable.**

- 🇳🇵 **Local example:** **Nepali outsourcing firms pursue ISO / CMMI certification specifically to
  win Western contracts** — foreign clients often **won't sign without it.** Here quality standards are
  the **entry ticket** to higher-value work, and the **disciplined process** certification forces
  **genuinely raises** the software's quality.

> ❌ **Common misconception:** *"Agile means no documentation and no standards."*
> ✅ **Correction:** "**Agile changes HOW quality is built in** (short iterations, continuous feedback)
> — it does **not remove** the need for it. Agile teams still **write tests, review code, and
> document.** 'Move fast' is **not** 'skip quality'; the best Agile teams are **rigorous.**"

> 🎙️ Speaker note: Certification is often the **ticket to a foreign contract** — quality becomes a
> business asset. Bust the "Agile = no docs" myth explicitly; it's the most common misconception here.

**📊 Depth table — Standards & models that guide quality**

| Standard / model | What it does | Why it matters |
|---|---|---|
| ISO 9001 | General quality-management system | Signals a disciplined organization |
| ISO/IEC 25010 | A software product-quality model | Defines the quality attributes to measure |
| CMMI | Rates process maturity (levels 1–5) | Western clients often require a CMMI level |
| IEEE standards | Engineering practices & documentation | Shared professional baseline |
| Waterfall | Sequential, plan-everything-up-front | Suits stable, well-known requirements |
| Agile / Scrum | Short iterations, continuous feedback | Suits changing requirements; still needs quality practices |

*ℹ️ For Nepali IT-outsourcing firms, ISO/CMMI certification is how you win and keep international contracts — quality becomes a business requirement, not just an ethical one.*

#### Concept 4 — Risk Management `[THEORY]` `[~7 min]`

[SLIDE] **Risk = likelihood × impact — plan before, not after**

> **Deliver:** Define it. **Risk management is identifying, assessing, and mitigating things that could
> cause failure.** Teach the scoring: **risk = likelihood × impact.** You keep a **risk register**
> (a logged, ranked list), plan **mitigation** (reduce the risk) and **contingency / rollback** (what
> you do if it happens anyway), and **prioritise safety-critical risks.** Walk the mechanics:
> - **List** the risks; **score** each by likelihood × impact; **rank** them (a risk matrix).
> - For each **high** risk: a **mitigation** AND a **contingency/rollback.**
> - **Safety-critical risks jump the queue** — impact is catastrophic even at low likelihood.
> - **Timing is a mitigation:** a bank **defers a risky migration off peak festival/remittance days.**
>
> Land the ethical framing: risk management forces the honest question **"how good is good enough?"** —
> answered **deliberately, before release**, not discovered during a live crash.

- 🇳🇵 **Local example:** a **Nepali bank defers a risky core-system migration off peak festival and
  remittance days**, and plans a **tested rollback for a Nagarik App update before shipping it.** That
  is risk management in action: they **scored** the risk (low likelihood, critical impact),
  **mitigated** it (timing, testing), and **prepared a contingency** in case it fails anyway.

> ❌ **Misconception:** *"We'll deal with problems if they come up."*
> ✅ **Correction:** "Risk management is deciding **what could fail BEFORE it does** — scoring
> **likelihood × impact**, mitigating the worst, and **planning rollback in advance.** Reacting after a
> live failure (during the festival rush) is exactly the **expensive, dangerous position** it exists to
> **avoid.**"

> 🍿 **Fun analogy (deliver it):** "Risk management is **checking the weather and carrying a torch
> BEFORE the trek** — not after you're already **stuck on the pass** in the dark. You plan the escape
> route while you still have the luxury of planning."

> 🖼️ Visual: a **risk matrix** — likelihood on one axis, impact on the other, colour-coded — with the
> top-right (high × high) flagged "mitigate first."

> 🎙️ Speaker note: Every high risk needs **both** a mitigation and a contingency (rollback). Plan the
> rollback **before** you need it — that's the whole point.

**📊 Depth table — A risk register in action (likelihood × impact → mitigation)**

| Risk | Likelihood × impact | Mitigation / contingency |
|---|---|---|
| Core-system migration corrupts data | Low × Critical | Test on a copy; schedule off-peak; rollback plan ready |
| Festival-day traffic spike crashes the app | High × High | Load-test early; auto-scale; a caching fallback |
| A third-party payment API goes down | Medium × High | Retry + queue; a secondary provider; user messaging |
| Key developer leaves mid-project | Medium × High | Documentation; pairing; no single point of knowledge |
| Security defect ships to production | Low × Critical | Security review + pen-test gate before release |

*ℹ️ Prioritise by likelihood × impact, but let safety-critical/high-impact risks jump the queue. Every high risk needs BOTH a mitigation and a contingency (rollback).*

#### 🛠 ACTIVITY — "Skip testing to hit the deadline?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Your client demands you skip testing — what three things do you do?**

> **Run it:** In pairs (2 min), the scenario: **your client demands you skip testing to hit a
> deadline.** Students decide the **three things they do** — considering **what they say to the client,
> what they refuse, and what minimum quality gate they hold.** Take **3 answers aloud** (3 min). Strong
> answers: (1) **explain the real cost/risk** (10× later, possible harm); (2) **propose a risk-based
> minimum** (test the critical paths, defer low-risk features); (3) **document the decision and who
> owns the risk.** Close: "Link back to Unit 1/2 — **'the client told me to' does not transfer the
> responsibility** for a harmful release."

> 🎙️ Speaker note: **Refusing to skip safety-critical testing is the ethical floor.** Reward answers
> that hold a quality floor for critical paths and **document who owns the accepted risk.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** QA differs from QC in that QA is:
a) product inspection b) ✅ **process-focused / preventive** (QC is product/inspection) c) only testing d) the same thing

**MCQ 2.** "Risk" in risk management is usually assessed as:
a) cost only b) ✅ **likelihood × impact** c) number of bugs d) team size

**Discussion prompt:** *Your client demands you skip testing to hit a deadline — what three things do you do?*

> 🎙️ Speaker note: Reward answers that hold a **quality floor** for safety-critical paths and
> **document who owns the accepted risk.** QA = prevent (process); QC = catch (product).

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** these are the **exact practices Nepali IT-outsourcing firms use to land and
keep international clients** — knowing them makes you **employable, not just ethical.** A candidate who
can talk **testing, QA, and risk** stands out immediately in an interview, and a team that has them
survives the six-month cliff from the hook while the "click-around" team loses its clients.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Layered testing** (unit → integration → system → acceptance) finds defects early — **automate the base**; testing shows presence, not absence, of bugs.
2. **QA prevents defects** (process); **QC catches them** (product) — you need **both**, not a lone hero.
3. **Standards** (ISO/CMMI) **+ risk management** (likelihood × impact, mitigation + rollback) make quality **repeatable.**

**Next session (S19):** the **people** who build software — **contingent workers and outsourcing.**

---
---

# S19 — Use of Contingent Workers · Outsourcing
**Lecture hour 3 of 5 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Everyone saved money — but who carries the risk?"**

> **Deliver (≈2 min):** Make it concrete. "A **US company posts a job.** It's filled by a **contractor
> in Bangalore at one-third the cost**, a **'temp' on a 3-month renewable contract in New York**, and a
> **small Kathmandu firm doing the back-end.**"
>
> **Run the question (≈3 min):** "**Everyone saved money** — but **who carries the risk**, and **is
> anyone treated unfairly?**" Take a few answers. Land the personal angle: **most of you in this room
> will BE the contingent or offshore worker** — the Bangalore contractor, the Kathmandu back-end team.
> So this isn't an abstraction about "them"; it's about **your own career, your rights, and the ethics
> of a model you'll live inside.** Today: **contingent workers → outsourcing & offshoring → the ethical
> balance (both sides).**

> 🎙️ Speaker note: Keep it personal — students here will **be** the contingent/offshore worker. Agenda
> on the board: contingent workers → outsourcing & offshoring → the ethical balance.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Contingent Workers `[THEORY]` `[~12 min]`

[SLIDE] **Flexibility for the firm, insecurity for the worker**

> **Deliver:** Define the term. **Contingent workers are hired on a non-permanent basis** —
> **contractors, temps, consultants, gig/freelance, and visa-based (e.g. H-1B) staff.** Explain **why
> firms use them**: **flexibility** (scale up/down fast), **cost** (pay only for what's needed), and
> **scarce skills** (buy rare skills on demand). Then the **trade-offs** — and be even-handed:
> - The **worker** has **little security, few benefits, and no paid leave** — the **risk shifts to
>   them.**
> - The **firm loses too**: **lower commitment**, and **institutional knowledge walks out** when the
>   contract ends.
>
> Land the ethical point: there is an **ethical duty to treat contingent workers fairly**, not merely
> as a **cheaper input.**

- 🌍 **Global example:** the **H-1B visa debate in the US** — accusations of using **contract/visa
  workers to undercut local wages** versus a **genuine skills shortage.** The same worker is framed as
  both a bargain and a threat, depending on who's talking.
- 🇳🇵 **Local example (make it personal):** many **Nepali developers work as remote contractors or
  freelancers** — **Upwork, Fiverr, or contract-to-a-foreign-firm.** The income is **flexible and often
  good by local standards**, but there's **no job security, no benefits, no paid leave**, and **no
  protection if the client vanishes.** The **flexibility the client enjoys is the insecurity the worker
  absorbs.**

> ❌ **Common misconception:** *"Contractors are cheaper, so a firm should always use them."*
> ✅ **Correction:** "The **hidden costs** bite: **lost institutional knowledge, lower commitment,
> constant re-hiring/onboarding**, and an **ethical duty to treat them fairly.** 'Cheaper per hour' is
> **not** 'cheaper overall', and it **externalises risk onto people.**"

> 🖼️ Visual: a **spectrum** graphic — **permanent → contractor → freelancer → offshore** — with
> **security ↓** and **flexibility ↑** as you move right.

> 🎙️ Speaker note: Make it personal — many students here **are** contingent workers already. The model
> **shifts risk from the firm to the worker**; that shift is the ethical heart of the session.

**📊 Depth table — Permanent vs contingent — what each side gains and loses**

| Dimension | Permanent employee | Contingent worker |
|---|---|---|
| Job security | High — ongoing role | Low — ends with the contract/gig |
| Benefits / paid leave | Usually provided | Usually none |
| Pay rate | Steady salary | Often higher hourly, but no safety net |
| Loyalty / commitment | Higher | Lower — no long-term stake |
| Institutional knowledge | Retained | Walks out when the contract ends |
| Who carries the risk | Shared with employer | Mostly the worker |

*ℹ️ The model shifts risk from the firm to the worker. That shift is the ethical heart of the debate — flexibility for the firm, insecurity for the person.*

#### Concept 2 — Outsourcing & Offshore Outsourcing `[THEORY]` `[EXAMPLE]` `[~12 min]`

[SLIDE] **Trades cost for control — and sends data across a border**

> **Deliver:** Define both. **Outsourcing is contracting work to an outside firm; offshoring is doing
> so in another (often lower-cost) country.** Give the **benefits**: **cost savings, 24/7
> follow-the-sun work, access to talent.** Then the **matching risks**: **quality control,
> communication/timezone gaps, data-security and confidentiality across borders, and dependency.** Walk
> the key points:
> - **Nepal is an outsourcing DESTINATION** — **Kathmandu IT / BPO / KPO firms serve Western clients**
>   (the "IT export" story) — and Nepali firms sometimes **outsource pieces onward.**
> - **Follow-the-sun**: work continues across time zones, but **coordination and quality control get
>   harder.**
> - The **sharpest risk is DATA**: sending **customer data to a country with weaker data-protection
>   law.**
> - **Over-dependency** on one vendor or client is itself a **business risk.**

- 🇳🇵 **Mini case (work it, ≈2 min):** a **Western client offshores customer data to a Kathmandu BPO**
  operating under **weaker data-protection law.** Ask: "what ethical and security obligations **cross
  the border** with that data?" Draw it out — the **obligations travel WITH the data.** The client
  **still owes its customers protection**, and the **Nepali firm inherits a duty** to handle
  **KYC/personal data as carefully as if it were local** — **regardless of what the weaker local law
  strictly requires.**

> ❌ **Misconception:** *"Once we offshore it, the risk and responsibility are the vendor's problem."*
> ✅ **Correction:** "**Responsibility travels with the data.** If a Kathmandu BPO **leaks a Western
> client's customer data**, the **client's name and liability are on the line too** — **outsourcing the
> work does not outsource the duty of care.**"

> 🖼️ Visual: a **world-map arrow** graphic showing work **flowing to Nepal as a destination**, with a
> "data crosses a legal border" flag on the arrow.

> 🎙️ Speaker note: Nepal both **receives** outsourcing (as a destination) and sometimes **outsources
> onward.** The **cross-border DATA question** is the ethical/security crux — echoes S6's client
> relationship: the duty of care doesn't stop at the border.

**📊 Depth table — Offshore outsourcing — benefits vs risks**

| Benefit | Matching risk |
|---|---|
| Lower cost | Quality control is harder at a distance |
| 24/7 follow-the-sun work | Timezone & communication gaps |
| Access to global talent | Data security/confidentiality across borders |
| Scale up/down quickly | Dependency on one vendor/client |
| Jobs & forex for Nepal | Night shifts, burnout in BPOs |

*ℹ️ Every benefit has a matching risk. The cross-border DATA risk is the sharpest: obligations to protect customer data don't stop at the border, even if the destination's law is weaker.*

#### Concept 3 — The Ethical Balance — both sides `[THEORY]` `[~6 min]`

[SLIDE] **Good for whom, at what cost — and is it fair?**

> **Deliver:** Frame it as a **stakeholder question** (Unit 1). **The ethics of outsourcing means
> weighing benefits and harms to ALL stakeholders** — **home-country workers, offshore workers,
> clients, and end-users.** Lay out both sides:
> - **Pros:** **jobs and income for developing economies like Nepal, lower prices, efficiency.**
> - **Cons:** **home-country job loss, worker exploitation, race-to-the-bottom wages, accountability
>   gaps.**
>
> For **Nepal specifically**: outsourcing brings **genuine high-value jobs and foreign exchange** — a
> real **development good** — but it can also mean **long night-shift hours for foreign time zones, low
> pay, and BPO burnout.** Land the honest answer: it isn't **"good"** or **"bad"** — it's **"good for
> whom, at what cost, and is it fair?"**

- 🇳🇵 **Local example:** Nepal's **IT-outsourcing industry** brings **real high-value jobs and forex** —
  good for the economy and for individual developers. But it also raises hard questions: **fair pay
  relative to the client's country, long night-shift hours to match foreign time zones, and burnout in
  BPOs.** **Both truths hold at once.**

> ❌ **Misconception:** *"Outsourcing is simply exploitation"* — OR — *"outsourcing is simply
> opportunity."*
> ✅ **Correction:** "**Neither is the whole truth.** A stakeholder analysis shows it **helps some**
> (Nepali developers, clients, the economy) and can **harm others** (home-country workers, over-worked
> BPO staff). The ethical task is to **make the arrangement fair**, not to pick one **slogan.**"

> 🍿 **Fun analogy (deliver it):** "Outsourcing is like **hiring a kitchen across town to cook your
> restaurant's food** — **cheaper and scalable.** But if **hygiene slips there**, **YOUR** customers get
> sick and **YOUR** name takes the blame. The distance saves money; it doesn't move the
> responsibility."

> 🎙️ Speaker note: There is **no single verdict.** Push students to name **WHO benefits and WHO
> pays** — that's the stakeholder view (Unit 1), and it's the mark of a strong answer.

**📊 Depth table — Outsourcing — who benefits and who bears the cost**

| Stakeholder | Benefit | Cost / harm |
|---|---|---|
| Offshore worker (Nepal) | High-value jobs, forex, skills | Night shifts, burnout, lower pay than the client's country |
| Home-country worker | (few) | Job loss, downward wage pressure |
| Client / company | Lower cost, scale, 24/7 coverage | Quality/control risk, accountability gaps |
| End-user / customer | Cheaper products | Their data crosses borders; support quality varies |
| Developing economy | Growth, forex, IT-export industry | Race-to-the-bottom wage pressure |

*ℹ️ A stakeholder view (Unit 1) shows there's no single verdict — outsourcing genuinely helps some and harms others. The ethics is making the trade fair, not pretending there's no cost.*

#### 🛠 ACTIVITY — "Net good or exploitative?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Is Nepal being an IT-outsourcing hub good or exploitative?**

> **Run it:** In pairs (2 min), students decide: **is Nepal being an IT-outsourcing hub mostly good or
> mostly exploitative for Nepali workers?** They list **one concrete benefit and one concrete harm,
> with a real example.** Take **3–4 answers aloud** (3 min) and **place each on a stakeholder map.**
> Benefits: **high-value jobs, forex, skills transfer, remote careers from Kathmandu.** Harms: **night
> shifts, burnout, pay below the client's country, weak worker protections.** Close: "The strongest
> answers name **WHO benefits and WHO pays**, rather than a one-word verdict."

> 🎙️ Speaker note: Reward **stakeholder-aware, both-sides reasoning.** The point is that outsourcing
> helps some and harms others **simultaneously** — a one-word verdict is a weak answer.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A key *ethical* downside of relying on contingent workers is:
a) they cost more b) ✅ **weaker protections/benefits + lost institutional knowledge** c) they're too loyal d) none

**MCQ 2.** A major risk specific to *offshore* outsourcing is:
a) higher taxes b) ✅ **data security/confidentiality across borders** (+ timezone/quality gaps) c) too much control d) none

**Discussion prompt:** *Is Nepal being an IT-outsourcing hub mostly good or mostly exploitative? Argue with examples.*

> 🎙️ Speaker note: Push for **stakeholder reasoning** — the point is that outsourcing **helps some and
> harms others at the same time.** Reward answers that name specific beneficiaries and specific
> bearers of the cost.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** **most of you will BE the contingent or offshore worker** — knowing your
**rights, the risks you carry, and the ethics of the model** protects you now, and **shapes how you
treat others** when you're the one hiring. This is **your own career, not an abstraction**: the
Upwork contract, the night-shift BPO seat, the "we'll renew if there's budget" — you'll meet all of
them, and understanding the model is how you negotiate it instead of just absorbing its risk.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Contingent work** trades the worker's **security** for the firm's **flexibility** — and **shifts risk onto the worker** (hidden costs: lost knowledge, weak protections).
2. **Offshore outsourcing** trades **cost** for **control and data-security risk** — the **duty of care travels with the data.**
3. **The ethics** means weighing **ALL stakeholders** — including the offshore worker — not a **one-word verdict.**

**Next session (S20):** what to do when you see your organization doing wrong — **whistle-blowing.**

---
---

# S20 — Whistle-Blowing
**Lecture hour 4 of 5 (Unit 4) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Stay quiet, quit, or go public?"**

> **Deliver (≈2 min):** Put the students in the seat. "You discover your company is **shipping software
> you KNOW will leak customers' national-ID data**, and management says **'ship it anyway.'**"
>
> **Run the question (≈3 min):** "Do you **stay quiet, quit, or go public** — and **what happens to YOU
> if you speak up?**" Take a few answers. Hold the tension deliberately: this is a **clash between
> loyalty to your employer and duty to the public**, with **real personal risk** on the line. Land the
> agenda: **what whistle-blowing is → when and how to do it responsibly → the risks, protections, and
> famous cases.**

> 🎙️ Speaker note: Hold the tension — don't resolve it in the hook. The whole session is about turning
> a panicky "stay quiet, quit, or leak" into a **disciplined, defensible process.** Agenda on the
> board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Whistle-Blowing Is `[THEORY]` `[~10 min]`

[SLIDE] **An insider exposing wrongdoing — not a 'snitch'**

> **Deliver:** Define it. **Whistle-blowing is an insider revealing wrongdoing** — **illegal,
> unethical, or dangerous conduct** — **within an organization.** It comes in two forms:
> - **Internal** — report **up the chain or to an ethics officer / internal audit** (give the
>   organization a chance to fix it).
> - **External** — a **regulator, the press, or the public** — when internal channels **fail or are the
>   problem.**
>
> At its core is a **clash: the duty of loyalty to your employer vs the duty to protect the public.**
> Resolve the Unit 2 tension explicitly: **loyalty has a LIMIT — it never requires covering up harm.**
> So whistle-blowing is a **considered act to protect stakeholders**, **not an impulsive betrayal.**

- 🌍 **Global examples:** **Edward Snowden** (NSA mass surveillance) and **Frances Haugen** (leaking
  internal **Facebook/Meta** research on known harms) are the **defining public-interest disclosures**
  of the era — insiders who judged that the **public's right to know outweighed their duty of
  loyalty.** Their **very different receptions** show how **contested and personally costly** the act
  is.

> ❌ **Common misconception:** *"A whistle-blower is just a disloyal snitch."*
> ✅ **Correction:** "**Ethical whistle-blowing protects the public and stakeholders when internal
> channels have failed** — it's an act of **responsibility, not betrayal.** Loyalty to an employer
> **never extends to helping it conceal serious harm** (the Unit 2 'loyalty has a limit' idea)."

> 🎙️ Speaker note: Snowden and Haugen are the canonical cases — note the **very different fallout** each
> faced. Whistle-blowing = an insider exposing wrongdoing **when loyalty would mean covering up harm.**

**📊 Depth table — Internal vs external whistle-blowing — and the 'snitch' myth**

| Question | Internal whistle-blowing | External whistle-blowing |
|---|---|---|
| Who do you tell? | Manager, ethics officer, internal audit | Regulator, press, or the public |
| When? | First — give the org a chance to fix it | When internal channels fail or are complicit |
| Risk to you | Lower, but retaliation still possible | Higher — public exposure, legal risk |
| Is it disloyalty? | No — it protects the org too | No — it protects the public when the org won't |

*ℹ️ A whistle-blower is not a disloyal 'snitch' — ethical whistle-blowing protects the public and stakeholders precisely when internal channels have failed.*

#### Concept 2 — When and How to Blow the Whistle — responsibly `[THEORY]` `[~10 min]`

[SLIDE] **Evidence-first, internal-first — external is the last step**

> **Deliver:** Frame it as a **disciplined, last-resort process — NOT an impulsive leak.** Walk the
> steps in order, and explain **why the order matters**:
> 1. **Get the facts** — reason on **evidence, not suspicion**; keep **dated records.** (Acting on
>    suspicion alone can be wrong and unprovable.)
> 2. **Weigh the harm** — confirm it's **serious (illegal / dangerous)**, not a minor grievance.
> 3. **Report internally** — manager, ethics officer, compliance/audit. (Gives the org a chance to fix
>    it; builds your record.)
> 4. **Escalate to a regulator** — e.g. the **CIAA** or the relevant authority — when internal routes
>    are **ignored or complicit.**
> 5. **Go public** — press / the public — as a **last resort** (highest risk).
>
> Land the point: **following the order protects both the public AND you** — a **documented,
> internal-first attempt** is what distinguishes a **responsible whistle-blower from a reckless
> leaker.**

- 🇳🇵 **Mini case (work it, ≈2 min):** "You **suspect, but can't yet prove**, that customer data is
  being **sold.** Walk through the **responsible steps before going public.**" Draw it out: **gather
  concrete evidence and keep dated records**; **confirm the harm is serious**; report to your
  **manager**, then the **ethics/compliance officer or internal audit**; if ignored, **escalate to a
  regulator such as the CIAA**; and **only as a last resort** go to the **press.**

> ❌ **Misconception:** *"If something's wrong, I should immediately post it online / tell the media."*
> ✅ **Correction:** "An **impulsive public leak** can be **legally dangerous, unprovable**, and can let
> the **wrongdoer escape on a technicality.** **Evidence-first and internal-first** is both **more
> effective and more defensible** — external disclosure is the **final step, not the first.**"

> 🖼️ Visual: a **decision flowchart** — gather evidence → internal report → escalate to a regulator →
> external (press/public) as a last resort.

> 🎙️ Speaker note: A developer at a Nepali **bank / gov project** escalates to the **compliance officer
> / internal audit** before considering the **CIAA or the press.** The **order matters — and protects
> you.**

**📊 Depth table — The responsible whistle-blowing process**

| Step | What you do | Why this order |
|---|---|---|
| 1. Get the facts | Gather evidence; keep dated records | Acting on suspicion alone can be wrong and unprovable |
| 2. Weigh the harm | Confirm it's serious (illegal/dangerous) | Whistle-blowing is for real harm, not minor gripes |
| 3. Report internally | Manager, ethics officer, internal audit | Give the org a chance to fix it; builds your record |
| 4. Escalate to a regulator | e.g. CIAA / the relevant authority | When internal routes are ignored or complicit |
| 5. Go public | Press / public — last resort | Highest risk; use only when all else fails |

*ℹ️ Following the order protects both the public AND you — a documented, internal-first attempt is what distinguishes a responsible whistle-blower from a reckless leaker.*

#### Concept 3 — Risks, Protections & Famous Cases `[THEORY]` `[EXAMPLE]` `[~10 min]`

[SLIDE] **Real personal cost, limited protection — courage + care**

> **Deliver:** Be honest about the price. **Whistle-blowing carries real personal cost, and legal
> shields are limited.** Name the **risks**: **retaliation, firing, blacklisting, lawsuits, and severe
> stress.** Name the **protections**: **whistle-blower laws/policies, anonymous hotlines, and
> regulators** — but their **strength varies hugely by country.** Walk the points:
> - Common **retaliation**: being **fired, sidelined, blacklisted** in a small industry, or **sued.**
> - **Protections where they exist**: statutory whistle-blower laws, anonymous reporting hotlines,
>   independent regulators.
> - **Nepal's protection is weaker** — limited safeguards via **anti-corruption / CIAA mechanisms** —
>   so there's **real personal risk.**
> - **Contrast with stronger US / EU statutes** — the **same act is far riskier** in a weak-protection
>   environment.

- 🇳🇵 **Local example:** in **Nepal, whistle-blower protection is limited** — safeguards run mainly
  through **anti-corruption / CIAA mechanisms** — so a **Nepali employee exposing wrongdoing** faces
  **real risk of firing and blacklisting**, with a **thinner legal net** than a counterpart in the US
  or EU. That **doesn't make the act wrong**; it makes **documentation, evidence, and internal-first
  steps even more important.** In a **small market**, blacklisting is a genuine threat.

> ❌ **Misconception:** *"Whistle-blowers are always protected by law."*
> ✅ **Correction:** "**Protection is limited and varies by country** — in **Nepal it is weak**, so
> **retaliation (firing, blacklisting) is a genuine risk.** Knowing this lets you act with both
> **courage AND care**: **strong evidence, an internal-first record, and advice reduce (not eliminate)
> the danger.**"

> 🍿 **Fun analogy (deliver it):** "A whistle-blower is the **smoke alarm in a building** — **annoying
> when it goes off**, but you're **glad it exists when there's a real fire.** And **nobody should rip it
> off the wall for beeping.**"

> 🖼️ Visual: a **risk-vs-protection two-column** graphic, and a **loyalty vs public-interest balance
> scale** tipping when the harm is serious.

> 🎙️ Speaker note: In a small market like Nepal's, **blacklisting is a real threat.** Be honest that
> **courage here costs more** because the legal net is thinner — evidence + an internal-first record are
> the best practical shield.

**📊 Depth table — Whistle-blowing — the risks vs the (limited) protections**

| Risk to the whistle-blower | Protection that may help |
|---|---|
| Being fired or forced out | Whistle-blower laws / employment protections (where they exist) |
| Blacklisting in a small industry | Anonymous reporting hotlines |
| Lawsuits (e.g. defamation) | Solid evidence + legal advice beforehand |
| Retaliation from management | An independent regulator (e.g. CIAA) |
| Severe personal stress | Support networks; documented internal-first record |

*ℹ️ Nepal's protections are limited (anti-corruption/CIAA mechanisms) versus stronger US/EU statutes — so the personal risk is real. Evidence + an internal-first record are your best practical shield.*

#### 🛠 ACTIVITY — "Would weak protection change your choice?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Be honest: does weak legal protection change what you'd do?**

> **Run it:** In pairs (2 min): "**If you found serious wrongdoing at a Nepali employer, would weak
> legal protection change what you'd do? Be honest.**" Students **map the responsible steps** they'd
> take before going public. Take **3–4 answers aloud** (3 min) and **discuss the gap between the ideal
> and the real personal cost.** Close: "**Courage and care aren't opposites** — evidence and
> internal-first steps let you have **both.**"

> 🎙️ Speaker note: There's **no 'right' answer** — reward **honesty about the real risk** plus a
> **responsible process** (evidence, internal-first, seek advice). The point is to **think it through
> BEFORE** you're ever in the moment.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The recommended *first* step before external whistle-blowing is usually:
a) call the press b) ✅ **exhaust internal reporting channels with evidence** c) post online d) quit quietly

**MCQ 2.** A common consequence whistle-blowers face is:
a) a promotion b) ✅ **retaliation (firing / blacklisting)** c) legal immunity d) nothing

**Discussion prompt:** *If you found serious wrongdoing at a Nepali employer, would weak legal protection change what you'd do? Be honest.*

> 🎙️ Speaker note: Draw out the **honest tension** between the ethical ideal and the real personal risk
> under weak protection. Internal-first with evidence is both more effective and more defensible.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** you may **one day be the only person who KNOWS** — understanding the
**responsible process and the real risks** helps you act with **both courage and care**, instead of
**freezing or leaking recklessly.** Thinking it through **now**, in a classroom with no stakes, is what
lets you **act well later**, when the stakes are your job and someone else's data.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Whistle-blowing = an insider exposing wrongdoing**, internal or external; **loyalty has a limit** (never cover up harm) — it's not being a "snitch."
2. **Do it responsibly:** **evidence-first, internal-first**, escalate to a regulator, **go public only as a last resort.**
3. Expect **real personal risk** (retaliation, blacklisting) and know the **(limited) protections** — **weaker in Nepal** than US/EU.

**Next session (S21):** the organization's responsibility to the **planet** — **green computing** (closes the unit).

---
---

# S21 — Green Computing
**Lecture hour 5 of 5 (Unit 4) · 50 minutes · CLOSES UNIT 4**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Is 'going digital' actually green — or just hiding the smoke?"**

> **Deliver (≈2 min):** Make it vivid. "**Every Google search, every crypto transaction, every old
> laptop dumped behind a shop in New Road** — IT runs on **electricity** and leaves behind **toxic
> waste.**"
>
> **Run the question (≈3 min):** "So is **'going digital' actually green**, or are we just **hiding the
> smoke?**" Take a few answers. Bust the myth up front: **'the cloud' is not weightless** — it's
> **physical data centres burning real power and water somewhere.** Land the agenda, and note this
> **closes the unit** by tying back to Unit 1's CSR: **what green computing is → energy & sustainable
> IT → e-waste & disposal → corporate responsibility.**

> 🎙️ Speaker note: Kill the "**digital = clean**" myth in the hook. Every search and transaction runs
> on a physical data centre consuming real electricity. Agenda on the board; flag that this closes
> Unit 4 and links to Unit 1 CSR.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Green Computing Is `[THEORY]` `[~8 min]`

[SLIDE] **The whole lifecycle: make → use → dispose → recycle**

> **Deliver:** Define it. **Green computing is designing, using, and disposing of IT in environmentally
> responsible, energy-efficient ways.** The foundational point: it covers the **FULL lifecycle** —
> **manufacture → use (energy) → disposal** — with the goals of **lower energy, lower emissions, and
> less waste.** Walk it:
> - It's **not just "buy an efficient laptop"** — it spans **making, running, and retiring** every
>   device.
> - **Manufacture** consumes materials and energy; **use** consumes power; **disposal** creates
>   e-waste.
> - **Global practice:** efficient **data centres** (good PUE), **renewable-powered cloud**, and
>   **ENERGY STAR / EPEAT-rated** devices.
>
> Deliver the key correction: **'the cloud' is not weightless** — it's **physical data centres burning
> real power and water somewhere.** 'Digital' **relocates** the footprint; it doesn't **remove** it.

- 🇳🇵 **Local example:** Nepal has a **genuine green-IT opportunity** — data centres powered by **clean
  hydro-electricity** could be a real **'green data center' selling point** for attracting
  international clients. **But** the gain is **erased if diesel generators kick in during
  load-shedding** — showing green computing must be **measured across the real, full lifecycle**, not
  **claimed on paper.**

> ❌ **Common misconception:** *"Software / digital has no environmental footprint — it's 'in the
> cloud.'"*
> ✅ **Correction:** "The cloud is **physical data centres burning real electricity and water
> somewhere.** A crypto transaction or an always-on server has a **measurable energy and carbon cost.**
> 'Digital' **relocates** the footprint; it **doesn't remove it.**"

> 🖼️ Visual: an **IT lifecycle loop** graphic — **manufacture → use → dispose → recycle** — closing the
> loop.

> 🎙️ Speaker note: The key myth to kill is "**digital has no footprint.**" Every search and transaction
> runs on a physical data centre consuming real electricity. Green computing addresses **all** stages.

**📊 Depth table — The IT lifecycle — environmental impact at each stage**

| Lifecycle stage | Environmental impact | Green response |
|---|---|---|
| Manufacture | Raw materials, water, energy, mining | Durable design; buy only what's needed |
| Use | Electricity for devices, servers, cooling | Efficient hardware, power management, renewables |
| Disposal | Toxic e-waste (lead, mercury, cadmium) | Reduce, reuse, refurbish, recycle safely |
| Recycle / reuse | (closes the loop) | Recover materials; refurbish for a second life |

*ℹ️ Green computing addresses ALL stages, not just energy in use. Ignoring manufacture and disposal just hides the footprint elsewhere.*

#### Concept 2 — Energy Use & Sustainable IT `[THEORY]` `[~8 min]`

[SLIDE] **Consolidate, sleep, clean power, efficient code**

> **Deliver:** Define it. **Sustainable IT means reducing the power consumed by devices, servers, and
> data centres.** Walk the **levers** and why each helps:
> - **Efficient hardware** — less power per unit of work (ENERGY STAR / EPEAT devices).
> - **Virtualization / consolidation** — many workloads on **fewer physical servers** (10 VMs on 1 box
>   instead of 10 boxes) — big energy savings.
> - **Power management** — **sleep / auto-shutdown** cuts the waste of always-on **idle machines.**
> - **Efficient code** — **less compute per task** means less energy **at data-centre scale.**
> - **Renewable energy** and **cooling efficiency** — shrink the footprint of the energy that *is*
>   used.
>
> Land the point: **small defaults scale.** Idle machines and unoptimised systems waste **measurable**
> energy, so an **IT decision-maker's choices materially shape** an organization's energy and
> emissions.

- 🇳🇵 **Mini case (work it, ≈2 min):** a **Kathmandu firm runs 50 always-on desktops overnight 'for
  convenience.'** Ask: "estimate the yearly cost and emissions, and propose **three fixes.**" Draw it
  out — it's a **measurable, needless** energy and emissions cost. Three fixes: **enable
  auto-sleep/shutdown**; **consolidate** what must stay on onto fewer machines/VMs; and **switch to
  efficient (ENERGY STAR) hardware** on the next refresh. Convenience was quietly buying a **yearly
  power bill nobody looked at.**
- 🇳🇵 **Local example:** Nepal's **hydropower advantage** — data centres powered by **clean hydro**
  could be a real green selling point — **but** the gain is **erased if diesel-generator backup during
  outages** takes over. Measure the **whole** picture.

> ❌ **Misconception:** *"One office's computers can't matter to the environment."*
> ✅ **Correction:** "At scale, **defaults matter enormously** — **50 idle machines overnight**,
> multiplied across every office, is **real power and real emissions.** As the IT decision-maker, your
> **default settings (sleep, consolidation, efficient hardware)** shape an organization's **whole energy
> footprint.**"

> 🖼️ Visual: a **Nepal 'hydro-powered data center'** concept graphic — clean hydro in, with a warning
> flag on the diesel-generator backup line.

> 🎙️ Speaker note: Work the always-on-desktops case — 50 machines left on overnight "for convenience"
> is a **measurable, avoidable** cost. Small defaults scale to the whole organization.

**📊 Depth table — Ways to cut IT energy use**

| Measure | How it saves energy | Example |
|---|---|---|
| Efficient hardware | Less power per unit of work | ENERGY STAR / EPEAT-rated devices |
| Virtualization / consolidation | Fewer physical servers running | 10 VMs on 1 server instead of 10 boxes |
| Power management | No power wasted on idle machines | Auto-sleep/shutdown of overnight desktops |
| Efficient code | Less compute per task | Optimising a hot query at data-centre scale |
| Renewable energy | Cleaner power for the same use | Hydro-powered data centre (Nepal) |
| Cooling efficiency | Less energy spent removing heat | Better airflow / free-cooling design |

*ℹ️ Nepal's hydropower is a real advantage — but only if backup diesel generators during outages don't erase the gain. Measure the whole picture.*

#### Concept 3 — E-Waste & Responsible Disposal `[THEORY]` `[EXAMPLE]` `[~8 min]`

[SLIDE] **Reduce → reuse → refurbish → recycle (and wipe your data first)**

> **Deliver:** Define it. **E-waste is discarded electronics containing toxic materials — lead,
> mercury, cadmium — that harm health and the environment.** Teach the **ladder** (it's **ordered**):
> **reduce → reuse → refurbish → recycle**, plus **safe disposal**, **extended producer
> responsibility**, and **data-wiping before disposal.** Walk the points:
> - **Toxins** (lead, mercury, cadmium) **leach into soil and water** when e-waste is **dumped or
>   burned.**
> - The **ladder**: first **reduce** and **reuse/refurbish** (extend life), then **recycle** to recover
>   materials.
> - **Extended producer responsibility:** **makers take back** and handle **end-of-life** devices.
> - **Wipe data before disposal** — a discarded device is also a **data-privacy risk** (Unit 2).

- 🇳🇵 **Local example:** **e-waste accumulates in Kathmandu with little formal recycling** — **informal
  dumping and burning in the valley** releases **lead, mercury, and cadmium** into soil and air, and
  **imported second-hand electronics quickly become junk.** With **weak e-waste regulation in Nepal**,
  responsible disposal falls heavily on **organizations and individuals doing the right thing
  voluntarily.**

> ❌ **Common misconception:** *"Throwing old electronics in the regular bin is fine."*
> ✅ **Correction:** "E-waste **leaches toxins (lead, mercury, cadmium) into soil and water** and
> **wastes recoverable materials** — it needs **dedicated handling.** And a **binned device is a
> data-privacy leak** too; **wipe or destroy the data first**, then **reduce/reuse/refurbish/recycle.**"

> 🖼️ Visual: an **e-waste hazard infographic** — toxic elements (lead, mercury, cadmium) → health and
> soil/water effects — beside the disposal ladder.

> 🎙️ Speaker note: E-waste piles up in Kathmandu with little formal recycling; informal dumping/burning
> releases toxins. **Weak regulation makes personal/organizational responsibility matter more.** The
> ladder is **ordered** — reduce first, recycle last.

**📊 Depth table — E-waste — the toxins and the responsible-disposal ladder**

| Item | Why it's hazardous | Responsible handling |
|---|---|---|
| Old laptop / phone battery | Lead, cadmium, lithium — toxic & fire risk | Reuse/refurbish; recycle via proper handler |
| CRT / old monitor | Contains lead | Never bin/burn; dedicated e-waste recycler |
| Circuit boards | Mercury, heavy metals | Recover materials; specialist recycling |
| Any device with your data | Data-privacy risk on disposal | Wipe/destroy data BEFORE disposal (Unit 2) |
| Still-working old PC | Wasted embodied energy if binned | Donate / refurbish for a second life |
| Imported second-hand device near end-of-life | Becomes junk fast → local e-waste | Reduce imports; plan for disposal |

*ℹ️ The ladder is ordered: reduce → reuse → refurbish → recycle. Dumping or burning e-waste (common in Kathmandu) leaches toxins into soil and water and wastes recoverable materials.*

#### Concept 4 — Corporate Responsibility & the IT Organization `[THEORY]` `[~6 min]`

[SLIDE] **Green IT is CSR in action — policy and reporting, not a gesture**

> **Deliver:** Tie it back to Unit 1. **An IT organization has a duty to manage its IT footprint as
> part of CSR** — the **direct link back to Unit 1.** Walk the **levers**:
> - **Green procurement policy** — buy **efficient, certified hardware by default** (a **policy**, not a
>   one-off choice).
> - **Take-back / recycling programs** — a **responsible end-of-life** for devices.
> - **Sustainability reporting** — **public accountability** you can't quietly walk back (Unit 1's CSR
>   reporting).
> - **Telecommuting** and **cloud right-sizing** — cut emissions from **commuting** and
>   **over-provisioned servers.**
>
> Land the closing point: like all CSR, green IT must be **embedded in operations and reported
> publicly to be genuine rather than greenwashing.** It's **policy and reporting, not a one-off
> gesture.**

- 🇳🇵 **Local example:** **telecoms and banks in Nepal adopting solar / energy-efficient data centres
  and device take-back schemes**, and **government IT procurement favouring efficient hardware**, are
  **green computing as CSR** (Unit 1). These are **policy-level commitments** — defaults for the whole
  organization — **not one-off gestures**, which is **exactly what makes them credible.**

> ❌ **Misconception:** *"Going green is just marketing / a one-off gesture."*
> ✅ **Correction:** "Real green IT is **embedded in operations** — **procurement policy, take-back
> programs, sustainability reporting, right-sized infrastructure** — exactly the
> **genuine-vs-greenwashing test from Unit 1.** A single **tree-planting photo op** isn't green
> computing; **changed defaults and public reporting** are."

> 🍿 **Fun analogy (deliver it):** "Ignoring e-waste is like **trekkers leaving plastic on the trail to
> Everest** — **invisible to you once you've moved on**, but it **piles up and poisons the place for
> everyone after.** CSR is refusing to be the trekker who walks away."

> 🎙️ Speaker note: This **closes the loop to Unit 1** — managing the IT footprint **IS** corporate
> social responsibility, made real through **policy and public reporting** rather than one-off gestures.

**📊 Depth table — How an IT organization acts green (CSR in practice)**

| Measure | What it does | Nepal example |
|---|---|---|
| Green procurement policy | Buy efficient, certified hardware by default | Govt/bank IT tenders favouring efficient devices |
| Take-back / recycling program | Responsible end-of-life for devices | Telecoms' device take-back schemes |
| Sustainability reporting | Public accountability for the footprint | Reporting energy/e-waste as part of CSR |
| Telecommuting | Cuts commute emissions | Remote/hybrid work reducing daily travel |
| Cloud right-sizing | No paying/powering idle capacity | Scaling servers to actual demand |
| Renewable-powered facilities | Cleaner energy for operations | Solar/hydro-powered data centres |

*ℹ️ This closes the loop to Unit 1: managing the IT footprint IS corporate social responsibility, made real through policy and public reporting rather than one-off gestures.*

#### 🛠 ACTIVITY — "Trace one device" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Where do your old phones and laptops actually go?**

> **Run it:** In pairs (2 min): "**Where do your old phones and laptops go right now?** Trace **one
> device's likely end-of-life in Nepal.**" Students **note whether the data was wiped**, and whether it
> was **reused, recycled, dumped, or burned.** Take **3–4 answers aloud** (3 min). Close: "Propose
> **one better step** for the next device — **donate/refurbish, use an e-waste handler, or wipe data
> first.**"

> 🎙️ Speaker note: Most devices end up **in a drawer, resold informally, or dumped** — rarely properly
> recycled or data-wiped. Reward **tracing the real path honestly** and **naming one concrete
> improvement.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Green computing covers a device's:
a) use only b) purchase only c) ✅ **entire lifecycle: manufacture, use, AND disposal** d) marketing

**MCQ 2.** The safest way to handle old electronics is:
a) the regular bin b) burn it c) ✅ **reduce/reuse/refurbish/recycle via proper e-waste handling** d) bury it

**Discussion prompt:** *Where do your old phones and laptops go right now? Trace one device's likely end-of-life in Nepal.*

> 🎙️ Speaker note: Connect to **Unit 1 CSR** and **Unit 2 data-privacy** (wipe before disposal) — green
> computing ties the whole course together.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** as **IT decision-makers** you'll **choose hardware, run servers, and dispose
of devices for whole organizations** — your **defaults** will shape **real energy bills and real
e-waste in Kathmandu.** Green computing is where your **professional choices meet the physical world**:
the sleep policy you set, the hardware you spec, and the disposal route you pick add up across an
organization to real electricity and real toxins in the valley.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Green computing spans the whole IT lifecycle** (manufacture → use → disposal); **'the cloud' is physical.**
2. **Cut energy** (efficient hardware, virtualization, power management, renewables) and **handle e-waste responsibly** (reduce → reuse → refurbish → recycle; **wipe data first**).
3. It's part of an IT organization's **CSR** — **embedded in policy and reporting**, not a one-off gesture.

**Next unit (Units 5–8):** we shift from **ethics to defence** — the fundamentals of **cybersecurity.**

---
---

# 📋 UNIT 4 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. Answer key at the end.*

### Section A — Multiple Choice (1 mark each)
1. Software quality is best defined as:
   a) no visible bugs  b) ✅ meeting requirements AND fitness for the user's real use  c) a fast demo  d) nice UI
2. The cost to fix a defect is generally lowest when found:
   a) after release  b) during the festival rush  c) ✅ early, in requirements/design  d) by users
3. Software whose failure can cause death or injury is called:
   a) legacy software  b) ✅ safety-critical software  c) freeware  d) beta software
4. The testing levels, in order, are:
   a) system → unit → acceptance  b) ✅ unit → integration → system → acceptance  c) acceptance → unit  d) demo → release
5. QA differs from QC in that QA is:
   a) product inspection  b) ✅ process-focused / preventive (QC is product/inspection)  c) only testing  d) the same thing
6. In risk management, risk is usually assessed as:
   a) cost only  b) ✅ likelihood × impact  c) number of bugs  d) team size
7. A key ethical downside of relying on contingent workers is:
   a) they cost more  b) ✅ weaker protections/benefits + lost institutional knowledge  c) they're too loyal  d) none
8. A major risk specific to offshore outsourcing is:
   a) higher taxes  b) ✅ data security/confidentiality across borders  c) too much control  d) none
9. The recommended first step before external whistle-blowing is usually:
   a) call the press  b) ✅ exhaust internal reporting channels with evidence  c) post online  d) quit quietly
10. A common consequence whistle-blowers face is:
    a) a promotion  b) ✅ retaliation (firing / blacklisting)  c) legal immunity  d) nothing
11. Green computing covers a device's:
    a) use only  b) purchase only  c) ✅ entire lifecycle: manufacture, use, AND disposal  d) marketing
12. The safest way to handle old electronics is:
    a) the regular bin  b) burn it  c) ✅ reduce/reuse/refurbish/recycle via proper e-waste handling  d) bury it

### Section B — Short Answer (2 marks each)
13. Define **software quality** and list **three** quality attributes.
14. Explain **QA vs QC** with **one example each**.
15. List **three ethical pros and three cons** of offshore outsourcing.
16. Outline the **responsible steps** for whistle-blowing (in order).
17. Explain **why e-waste needs special disposal** (and why you must wipe data first).

### Section C — Applied Case (3 marks each)
18. A **Nepali fintech rushes a Dashain release with no QA.** Identify the **quality and risk failures** and recommend the **strategies** (from S17–S18) that would have prevented them.
19. A developer **discovers a national-ID data leak** at their employer, and management says "ship it anyway." Map the **responsible whistle-blowing path** and the **risks** the developer faces under **Nepal's weak protections.**

### Section D — Discussion (open-ended)
20. "**Is Nepal's growth as an IT-outsourcing destination a net good for Nepali workers AND the environment?**" Argue **both sides**, citing **outsourcing ethics** (S19) **and green / e-waste concerns** (S21), then state your own position.

---

### ✅ Answer Key (Section A)
1-b · 2-c · 3-b · 4-b · 5-b · 6-b · 7-b · 8-b · 9-b · 10-b · 11-c · 12-c

> **Sections B–D: grade on key terms.** Q13 must give conformance-to-requirements + fitness-for-use and
> name three of: correctness, reliability, usability, security, maintainability, performance. Q14 must
> contrast QA (process/preventive — standards, reviews) with QC (product/reactive — testing,
> inspection), each with an example. Q15 — pros: jobs/forex for Nepal, lower prices, efficiency,
> skills; cons: home-country job loss, exploitation/burnout, race-to-the-bottom wages, cross-border
> data risk. Q16 must be **evidence-first → weigh harm → internal-first → regulator (CIAA) → public as
> last resort.** Q17 must note toxins (lead/mercury/cadmium) leaching into soil/water + recoverable
> materials + data-privacy leak (wipe first). Q18 — name missing testing/QA + no risk register/rollback
> + ~10× cost escalation and hidden costs; recommend layered testing, a QA gate, off-peak scheduling,
> and a rollback plan. Q19 — reward the ordered internal-first process AND honesty about retaliation /
> blacklisting under Nepal's limited (CIAA) protections. Q20 — reward students who weigh **all
> stakeholders** (jobs + forex vs burnout + wage pressure) **and** the environmental cost (energy +
> e-waste), not a one-sided slogan.

---

## ✅ Unit 4 complete (full lecturer-ready depth)
The deck is built: **IT246_Unit4.pptx** (80 slides) — diagram-rich, self-contained, and PDF-safe,
carrying all **17 §7A depth tables** (comparison, concrete-example, and scaffolding) and **6
diagrams** (cost-to-fix escalation curve, testing pyramid, risk matrix, permanent-to-offshore worker
spectrum, whistle-blowing decision flow, IT lifecycle loop). This Markdown source now carries those
**same 17 depth tables inline** under each concept, so the source of truth and the deck stay in sync.
