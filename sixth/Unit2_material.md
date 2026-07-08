# IT 246 — Unit 2: Ethics for IT Workers and IT Users
### Full Lecturer-Ready Session Material (S6–S10)

**Program:** BIM, 6th Semester · **Unit weight:** 5 lecture hours
**Sessions:** S6–S10 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT246_Unit2.pptx` (92 slides), regenerated via `build_unit2_pptx.py` (imports `deckkit.py`).

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each
> session has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just
> bullets), **worked examples**, a **timed in-class activity**, and lecturer cue cards in
> `> 🎙️` blocks. `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags:
> `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.**

---

## Unit 2 — Learning Outcomes
By the end of this unit, students will be able to:
1. Identify the key relationships an IT worker manages (employer, client, supplier, peers, users, society) and the ethical duties in each.
2. Explain how professional codes, certification, licensing, and professional organizations encourage professionalism.
3. Describe acceptable use policies and the common ethical issues in IT use (software piracy, inappropriate use).
4. Explain key privacy, surveillance, and anonymity/identity issues in IT.
5. Recognize and reason about social-networking ethical issues (cyberbullying, fake news, harassment, defamation).

---
---

# S6 — Managing the IT Worker Relationship
**Lecture hour 1 of 5 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Who are you actually loyal to?"**

> **Deliver (≈2 min):** Put two short scenarios on screen and read them slowly:
> 1. A vendor offers the bank's IT manager a **"free" iPhone** the week before a **Rs 2-crore tender** decision.
> 2. A developer quietly **moonlights for a client's competitor** on weekends.
>
> **Run a quick reaction (≈3 min):** "Has anyone broken a **law** yet?" Most will say no. "Does
> something already feel **wrong**?" Most will say yes. That gap is today's lesson: an IT worker
> doesn't serve one boss — they juggle **many relationships at once**, and each one **pulls on their
> loyalty in a different direction.** Tell them: by the end of today you'll be able to *name* every
> party you owe a duty to, and *spot* when those duties collide.

> 🎙️ Speaker note: Don't resolve the iPhone yet. Ask "Is the free iPhone a gift or a bribe?" and
> **hold the question** — we resolve it in Concept 4. The discomfort students feel *is* the conflict
> of interest. Write the agenda on the board: why IT workers face special pressure → employer →
> client → suppliers/peers/users/society.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Why IT Workers Face Special Relationship Pressures `[THEORY]` `[~8 min]`

[SLIDE] **Access = power = responsibility**

> **Deliver:** Start with the definition and write it on the board. An **IT worker** = a
> professional who **designs, builds, maintains, or manages IT systems — and the data inside them.**
> Then make the central argument of the whole session: what makes IT workers ethically *different*
> from many other employees is **privileged access.** A typical clerk can see their own desk; a
> database administrator can see **everyone's records.** A developer holds the **source code**; a
> sysadmin holds **admin/root rights**; a support technician can read your files "to fix the
> problem."
>
> Land the logic chain slowly, because it's the spine of the session: **access is power, and power
> is responsibility.** The ability to technically *do* something — read a balance, copy a file,
> reset a password — **does not make it right to do.** So every relationship an IT worker has comes
> with a built-in **duty of care**: a duty not to abuse the trust that access represents.

- 🌍 **Global example:** a **system administrator abusing root access** to read executives' private
  emails. Nothing technically stopped them — the system *let* them. Only ethics should have.
- 🇳🇵 **Local example (walk through it):** a **bank IT staffer** with database access **could view
  any customer's balance** — your neighbour's, a celebrity's, an ex's. What stops them is **not lack
  of permission** (the system grants it); it's **trust and ethics.** That gap between "can" and
  "should" is exactly where IT-worker ethics lives.

> ❌ **Common misconception:** *"IT is just a back-office technical job — ethics is for managers."*
> ✅ **Correction — say it out loud:** "Access **is** power. The more you can technically do, the
> more responsibility you carry — *whether or not* you have a manager's title. A junior with admin
> rights holds more trust than a senior manager without them."

> 🖼️ Visual: an **"IT worker at the center"** relationship web — one person in the middle with six
> arrows out to: **Employer, Client, Supplier, Peers, Users, Society.** Keep it on screen for the
> rest of the session; you'll walk around the web concept by concept.

> 🎙️ Speaker note (transition): "We've got six arrows. Let's follow each one and ask: what do you
> owe the person at the other end? Start with the one that signs your paycheck."

**📊 Depth table — Privileged access — what each role CAN do, and the duty it creates**

| IT role | What they can technically do | The duty their access creates |
|---|---|---|
| Database administrator | Read/edit any record — every customer's balance, any citizen's KYC | View only what the job needs; never browse out of curiosity |
| Developer | Hold the full source code and business logic | Not leak, sell, or reuse the employer's/client's code |
| System administrator | Root rights — read anyone's email, reset any password | Not snoop on colleagues or executives; act only on authorised tasks |
| Support technician | Open your files, install software, take remote control | Touch only what fixes the stated problem; keep what they see private |
| Network administrator | See all traffic, block or log any user | Monitor per policy, not to spy on individuals |
| Bank IT staffer (Nepal) | Look up any account — a neighbour's, a celebrity's, an ex's | Look only for a work reason; the system permits it, ethics forbids it |

*ℹ️ Nothing on the right column is enforced by the system — the system GRANTS the access. Only trust and ethics stop the abuse.*

#### Concept 2 — Relationship with the Employer `[THEORY]` `[EXAMPLE]` `[~9 min]`

[SLIDE] **Duty of loyalty and honesty**

> **Deliver:** The first arrow points to your **employer.** Explain the two core duties and *why*
> each exists:
> - **Loyalty** — protect the employer's **assets and intellectual property.** Their source code,
>   client lists, internal data, and systems are things you're trusted *not* to leak, sell, or
>   carry out the door to your next job.
> - **Honesty** — be truthful about your **work and your qualifications.** This is where **resume
>   fraud** lives: claiming a certification you don't hold, or skills you can't deliver, is an
>   ethical breach against your employer *before you've even started.*
>
> Then name the four pressure points where this relationship strains, because students will hit all
> four in real jobs: **conflicts of interest** (a side interest that competes with the employer's),
> **resume fraud**, **software-license compliance** (using unlicensed software on the job — covered
> in S8), and the **whistle-blowing tension** — what do you owe the employer when the employer
> itself is doing wrong? (We treat whistle-blowing fully in Unit 4; today just flag that loyalty
> has a *limit* — it does not extend to covering up harm.)

- 🇳🇵 **Local example:** a **Kathmandu IT-firm staffer copying client source code** to reuse at a
  weekend side gig. Walk it: the code isn't theirs — it belongs to the employer (and contractually
  often to the client). Reusing it is **theft of IP**, a betrayal of *two* relationships at once
  (employer and client), even though "no one will notice" and "I wrote it anyway."

> **Mini case (pose, take 2–3 answers, ≈2 min):** Your employer asks you to **install pirated
> Microsoft / AutoCAD** on all office machines to cut costs. It saves money and "everyone does it."
> Ask two questions: **"What do you do?"** and crucially **"Who is liable if it's discovered?"** Draw
> out that liability can fall on *the company and the individual who installed it* — "I was just
> following orders" is the **blind-obedience trap** from Unit 1, and it doesn't transfer the
> responsibility off you. *(Links forward to S8 piracy and Unit 3 IP.)*

> 🎙️ Speaker note: If a student says "but the boss told me to," connect explicitly to Unit 1's
> decision traps — obedience to authority does not erase personal accountability.

**📊 Depth table — Four pressure points on the employer relationship**

| Pressure point | What it looks like | Why it's an ethical problem |
|---|---|---|
| Conflict of interest | A side interest that competes with the employer (moonlighting for a rival) | Your judgment now serves two masters; the employer can't trust your loyalty |
| Resume fraud | Claiming a certification or skill you don't have | A breach of honesty before you even start — the employer relied on a lie |
| Software-license compliance | Using unlicensed/pirated software on the job (see S8) | Legal liability for the firm AND you; 'orders' don't transfer the blame |
| Whistle-blowing tension | The employer itself is doing wrong; do you stay loyal? | Loyalty has a limit — it never requires covering up harm (Unit 4) |

*ℹ️ Loyalty and honesty are the duties; these four are where they get tested in a real job.*

#### Concept 3 — Relationship with the Client `[THEORY]` `[~8 min]`

[SLIDE] **A professional duty beyond the contract**

> **Deliver:** The next arrow is the **client** — the person or organization you build *for*.
> Explain the three professional duties: give **honest technical advice**, **deliver what was
> promised**, and **disclose risks** (don't hide that a system might fail, leak, or not scale).
>
> Then introduce the concept that makes the client relationship ethically loaded: **information
> asymmetry.** The client usually **cannot judge technical quality** — they can't read your code,
> can't tell secure architecture from a shortcut, can't know if your "it's done" is true. They are
> **forced to rely on your honesty.** That dependency is exactly what creates a *professional* duty,
> the same way a patient must trust a doctor. When one party can't verify and the other can exploit
> that, ethics is the only protection the weaker party has.

- 🇳🇵 **Local example (walk it):** a software vendor **over-promising an e-governance module** to a
  municipality, then quietly **under-delivering.** The municipality **lacks the technical expertise
  to catch it** until the system fails in production — possibly months later, after payment. The
  asymmetry let the vendor sell air. *Good ethics here protects a party who literally cannot protect
  themselves.*

> ❌ **Misconception:** *"If the contract doesn't ban it, it's fine."*
> ✅ **Correction:** "Professional duty goes **beyond the contract's letter.** The contract is a
> **floor, not the limit** of your responsibility — exactly the Unit 1 idea that **law/contract is
> the floor, not the ceiling.** A loophole in the contract is not an ethical permission slip."

> 🎙️ Speaker note (transition): "Two arrows down. The remaining four — suppliers, peers, users,
> society — share a theme: fairness to people who aren't your boss or your client. Let's batch them."

**📊 Depth table — Three duties to the client — and the failure when each is broken**

| Duty to the client | What it means | Failure example (Nepal / IT) |
|---|---|---|
| Honest technical advice | Recommend what the client needs, not what pays you most | Selling an over-sized system a small NGO doesn't need |
| Deliver what was promised | Build the agreed scope to the agreed quality | Marking a half-built e-gov module 'done' to trigger payment |
| Disclose risks | Tell them what might fail, leak, or not scale | Hiding that the system can't handle election-day load |

*ℹ️ All three exploit information asymmetry — the client literally cannot catch the breach until it's too late. That's what makes it a PROFESSIONAL duty.*

#### Concept 4 — Suppliers, Peers, Users & Society `[THEORY]` `[EXAMPLE]` `[~5 min]`

[SLIDE] **The other four relationships**

> **Deliver each arrow with its core duty:**
> - **Suppliers** — deal **fairly**; avoid **bribery and kickbacks.** *(Now resolve the hook: the
>   "free iPhone" is a **bribe disguised as a gift** — it's timed around a tender and meant to
>   **influence the decision.**)*
> - **Other professionals (peers)** — **mutual respect**, no **resume inflation**, no **poaching
>   trade secrets** from a colleague's employer. The profession's reputation is shared; one fraud
>   damages everyone's credibility.
> - **IT users** — **support and train** them; **don't exploit their lack of skill** (e.g. don't
>   bury a customer in jargon to overcharge, or scare a non-technical user into an unneeded purchase).
> - **Society** — build **safe systems**; **don't enable harm.** A system that **leaks citizen
>   data** or powers a scam harms people who never agreed to anything.

> **Gift-vs-bribe test (deliver as a 3-question rule):** "Ask three things — **(1)** Would it survive
> being made **public**? **(2)** Is it **timed** around a decision? **(3)** Could it **influence**
> your judgment? The iPhone **fails all three**, so it's a bribe, not a gift. A pen with the vendor's
> logo at a conference passes all three — that's a gift."

> 🍿 **Fun analogy (deliver it):** "An IT worker is like a **hospital pharmacist** — trusted with
> powerful 'medicine' (access and data) that **heals or harms depending on whose hand holds it.** The
> pharmacist's skill isn't the safeguard; their *ethics* is. Same for you and your admin password."

**📊 Depth table — Gift vs Bribe — the three-question test**

| Test question | A genuine gift | A bribe |
|---|---|---|
| Would it survive being made PUBLIC? | Yes — a logo pen at a conference is fine to disclose | No — you'd hide the 'free iPhone' from your boss |
| Is it TIMED around a decision? | No — unrelated to any pending choice | Yes — arrives the week before the tender |
| Could it INFLUENCE your judgment? | No — token value, no leverage | Yes — that's the entire point of giving it |

*ℹ️ The iPhone fails all three → bribe. The logo pen passes all three → gift. In Nepal, festival ('Dashain') gifting is cultural — the test is what keeps a normal gift from becoming a bribe.*

**📊 Depth table — The six relationships on one page — duty & a concrete Nepal risk**

| Relationship | Core duty | A concrete ethical risk (Nepal / IT) |
|---|---|---|
| Employer | Loyalty + honesty; protect assets/IP | Copying source code to a personal side project |
| Client | Honest advice; deliver; disclose risk | Hiding a security flaw to hit a deadline |
| Suppliers | Deal fairly; no bribes/kickbacks | Accepting a vendor's pre-tender 'gift' |
| Peers | Mutual respect; no poaching/inflation | Blaming a teammate to look better; stealing a rival's trade secrets |
| Users | Support & train; don't exploit skill gaps | Burying a customer in jargon to overcharge |
| Society | Build safe systems; don't enable harm | Shipping a system that leaks citizen data |

*ℹ️ None of these risks required hacking — every one came from ordinary access plus a pull on your loyalty.*

#### 🛠 ACTIVITY — "Map your own six arrows" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Think–Pair–Share**

> **Run it:** In pairs (2 min), students imagine they've just joined a **Nepali bank's or fintech's
> IT team.** For **any three of the six relationships**, they write **one concrete ethical risk**
> they'd face in that role (e.g. supplier → a vendor's Dashain gift; users → a customer who can't
> tell if their problem is fixed). Take **3–4 answers aloud** (3 min) and place each on the
> relationship web on screen. Close: "Notice none of these required hacking — every risk came from
> *ordinary access plus a pull on your loyalty.*"

> 🎙️ Speaker note: If a pair stalls, seed them — employer (copying code to a side project), client
> (hiding a security flaw to hit a deadline), peers (inflating a teammate's mistake to look better).

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A supplier gifting an IT manager a phone right before a tender decision is best described as:
a) good manners b) ✅ **a conflict of interest / bribery** c) a loyalty bonus d) fair dealing

**MCQ 2.** The duty to give honest technical advice applies most directly to the:
a) supplier b) competitor c) ✅ **client** d) regulator

**Discussion prompt:** *Which relationship is hardest for a junior IT worker in Nepal to manage honestly — and why?*

> 🎙️ Speaker note: Expect "employer vs society" (pressure to install pirated software) and "supplier"
> (festival gifts are culturally normal, which blurs the bribe line). For each, name the relationship
> on the web and the duty in tension.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** your first IT job hands you **access and vendor contacts on day one** —
before anyone has tested your character. How you handle gifts, access, and honesty in those first
weeks quietly **sets your reputation for years**, and in a small market like Nepal's IT industry,
reputation travels fast between firms. The "can vs should" judgment you practiced today is exactly
what separates a trusted professional from a technically-skilled liability.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. IT workers manage **six key relationships** (employer, client, supplier, peers, users, society).
2. **Privileged access creates duties** — it's about power, not just permission; "can" ≠ "should."
3. **Loyalty, honesty, and no conflicts of interest** run through all six; the contract is a floor, not the ceiling.

**Next session (S7):** how the *profession itself* encourages good behavior — **codes, certification, and licensing.**

---
---

# S7 — Encouraging Professionalism of IT Workers
**Lecture hour 2 of 5 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"A doctor swears an oath. An engineer signs off on a bridge. But anyone can call themselves an 'IT professional' tomorrow."**

> **Deliver (≈2 min):** Paint the contrast vividly. "A doctor who acts unethically can be **struck
> off the register by the NMC** — they lose the *right to practice.* An engineer who signs off on a
> bridge that collapses faces the **NEC**. Now — what happens to an IT worker who ships dangerous,
> negligent software? Usually… **nothing formal.** There's often **no license to lose.**"
>
> **Set up (≈3 min):** Pose the two questions that drive the session and take a quick show of hands:
> "Given that, **is IT really a *profession*?** And **should** it be regulated like medicine and
> engineering?" Tell them we'll answer the first with a checklist, and they'll argue the second
> themselves at the end.

> 🎙️ Speaker note: Keep the "should IT be licensed?" debate alive as a thread — it returns in the
> CFU discussion and the end-of-unit quiz. Agenda on board: is IT a profession? → codes of ethics →
> certification → licensing → professional bodies.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Is IT a "Profession"? `[THEORY]` `[~7 min]`

[SLIDE] **What makes a profession**

> **Deliver:** Don't assume "profession" just means "a serious job." Give the **four-part test** and
> check IT against each:
> 1. **Specialized education** — a recognized course of study. ✅ IT has degrees like this very one.
> 2. **A recognized body of knowledge** — shared, documented expertise. ✅ IT clearly has this.
> 3. **A code of ethics** — published shared standards. ✅ exists (ACM, IEEE-CS — Concept 2).
> 4. **Self-regulation** — the field can **license and discipline** its own members. ❌ IT **lacks
>    universal licensing.**
>
> Land the verdict: IT **partly qualifies** — it has the knowledge and the codes, but **not the
> self-regulation/licensing** that medicine and law have. That's *why* IT's status as a "profession"
> is genuinely **debated**, not just an exam phrase.

- 🇳🇵 **Local example:** in Nepal, **doctors are licensed by the NMC (Nepal Medical Council)** and
  **engineers by the NEC (Nepal Engineering Council)** — you legally cannot practice without it. **IT
  workers generally are *not* licensed**: you can build banking software tomorrow with no government
  permission. That single fact is the heart of the debate.

> ❌ **Misconception:** *"Anyone who fixes computers is an IT professional."*
> ✅ **Correction:** "Professionalism is about **standards and accountability**, not just technical
> skill. A brilliant coder who hides bugs and pads invoices is *skilled*, not *professional.*"

> 🎙️ Speaker note (transition): "IT has codes even without licensing — so let's look at what a code
> of ethics actually does, because it's the main tool the field *does* have."

**📊 Depth table — The four-part profession test — IT vs medicine/engineering**

| Criterion | Medicine / Engineering | Information Technology |
|---|---|---|
| Specialized education | Medical / engineering degree required | ✅ Yes — IT degrees (like this BIM) |
| Recognized body of knowledge | Established, documented, examined | ✅ Yes — shared, documented expertise |
| Code of ethics | Yes — enforced by the council | ✅ Yes — ACM, IEEE-CS (voluntary) |
| Self-regulation (licensing + discipline) | Yes — NMC / NEC can strike you off | ❌ No universal licensing to lose |

*ℹ️ IT scores 3 of 4. The missing self-regulation — no licence, no strike-off — is the whole reason 'is IT a profession?' is a live debate.*

#### Concept 2 — Professional Codes of Ethics `[THEORY]` `[EXAMPLE]` `[~8 min]`

[SLIDE] **The rules members agree to uphold**

> **Deliver:** A **code of ethics** = a published set of **principles members commit to upholding**.
> The big two in IT are the **ACM Code of Ethics** and **IEEE-CS**. Explain the **four jobs a code
> does** — say *why* each matters:
> - **Sets expectations** — turns "be good" into specific commitments ("avoid harm," "respect
>   privacy," "be honest about limitations").
> - **Builds public trust** — outsiders can see what the field holds itself to.
> - **Guides decisions** — when you're stuck, the code is a reference, not just your gut.
> - **Provides a basis for discipline** — membership/employment can be tied to it, so it has *some*
>   teeth even without a government license.

- 🇳🇵 **Local example:** a Nepali software company **adopting an internal code modeled on ACM**, and
  the community norms around **CAN (Computer Association of Nepal)** — even absent licensing, firms
  *import* professional standards voluntarily because clients and outsourcing partners expect them.

> **Mini case (work it, ≈2 min):** An ACM principle says **"avoid harm."** A developer is asked to
> build a **hidden tracking feature** users don't know about. Ask: **"What does the code tell them to
> do?"** Walk it: undisclosed tracking *harms* users (violates their privacy/autonomy without
> consent) → the code says **object, disclose, or refuse.** Show that a code is only useful if you
> can **apply** it to a concrete ask — which is the skill being tested.

> 🎙️ Speaker note: Connect to S6 — this is the *employer-vs-society* tension again, now with a code
> to lean on. "The code gives you language to say 'no' professionally."

**📊 Depth table — The four jobs a code of ethics does**

| Job of the code | What it achieves | Concrete example |
|---|---|---|
| Sets expectations | Turns vague 'be good' into specific commitments | ACM: 'avoid harm', 'respect privacy', 'be honest about limitations' |
| Builds public trust | Outsiders can see the standard the field holds itself to | Clients/outsourcing partners trust a firm that follows ACM norms |
| Guides decisions | A reference when you're unsure, not just your gut | Asked to build hidden tracking → the code says object/disclose/refuse |
| Basis for discipline | Membership or employment can be tied to it | Breach → lose membership or your job, even with no state licence |

*ℹ️ A code has 'some teeth' without a government licence — the last row is how the field disciplines its own even though IT lacks NMC/NEC-style regulation.*

#### Concept 3 — Certification `[THEORY]` `[~6 min]`

[SLIDE] **Proof of a specific skill**

> **Deliver:** A **certification** = a **vendor or industry credential proving a specific skill** —
> e.g. **CCNA, CISSP, CompTIA, AWS, PMP.** Explain its four defining traits, because students
> routinely over-trust certs:
> - It **signals competence** to employers (a fast, trusted filter on a CV).
> - It is **voluntary** — no law requires it.
> - It can become **outdated** — a 2015 cloud cert may be stale by now.
> - It is **not a license** — passing an exam doesn't grant any legal right to practice.

- 🇳🇵 **Local example:** Nepali IT graduates pursuing **CCNA / CEH** to compete for **jobs and
  remote/outsourcing work** — a cert is often the thing that gets a Kathmandu graduate's CV past a
  foreign client's first filter.

> ❌ **Misconception:** *"Certification = guaranteed ethical behavior."*
> ✅ **Correction:** "Certification proves **skill, not integrity.** A certified ethical hacker (CEH)
> has the *skill* to break into systems — whether they use it ethically is a *separate* question the
> certificate can't answer."

**📊 Depth table — Common IT certifications — what each proves & who issues it**

| Certification | What it proves | Issued by |
|---|---|---|
| CCNA | Cisco networking fundamentals | Cisco (vendor) |
| CISSP | Information-security management expertise | (ISC)² (industry body) |
| CEH | Skill in ethical hacking / penetration testing | EC-Council (industry body) |
| CompTIA A+ | Core IT support / hardware & OS troubleshooting | CompTIA (industry body) |
| AWS Certified | Building/operating on Amazon Web Services | Amazon (vendor) |
| CISA / CISM | IT audit / security governance | ISACA (professional body) |

*ℹ️ All are voluntary, expire over time, and prove SKILL — none grants a legal right to practise. CEH proves the skill to break into systems; whether it's used ethically is a separate question.*

#### Concept 4 — Licensing & Professional Organizations `[THEORY]` `[~9 min]`

[SLIDE] **Government permission with legal force — and the bodies that set standards**

> **Deliver — Part A, Licensing:** A **license** = **government-granted permission to practice,
> legally enforced.** The point of licensing is to **protect the public in high-stakes fields** —
> you can't practice medicine or structural engineering without one *because mistakes kill people.*
> Pose the live debate: **should safety-critical software** (medical devices, aviation, banking core
> systems) **require a licensed engineer** the way a bridge does? Note the cost: licensing adds
> protection but also **gatekeeping, fees, and slower entry** — which is exactly why IT has resisted
> it.

- 🌍 **Global example:** the **"Professional Engineer (PE) — Software"** licensing debate in the US —
  a software PE license was *created* and then **largely discontinued** for lack of demand, which
  tells you how unsettled this question is even in mature markets.

> **Deliver — Part B, Professional Organizations:** These are the **bodies that set standards, run
> certifications, publish codes, and represent members.** Name them:
> - **ACM** and **IEEE-CS** — the global standard-setters and code authors.
> - **ISACA** — governance, audit, and security (the CISA/CISM certs).
> - 🇳🇵 **CAN (Computer Association of Nepal)** and IT professional forums — **advocacy, events, and
>   training** for the Nepali IT community.
>
> Tie the three concepts together explicitly: **organizations** publish the **codes** and run the
> **certifications**, while **government** runs **licensing.** That's the whole map of "who keeps IT
> professional."

> 🍿 **Fun analogy (deliver it):** "A code of ethics is the **'terms of service' you accept** to be
> trusted as a professional. You don't read every line — but the day you violate it, everyone points
> to the clause you agreed to."

**📊 Depth table — Certification vs Licence vs Code vs Professional body — the confusable four**

| Mechanism | Who grants it | Legal force? | What it proves / does | Example |
|---|---|---|---|---|
| Certification | A vendor or industry body | No — voluntary | You have a specific skill | CCNA, CISSP, AWS |
| Licence | Government | Yes — legally enforced | Legal right to practise | NMC doctor reg., driving licence |
| Code of ethics | A professional body | No — but can discipline members | Shared ethical commitments | ACM 'avoid harm' |
| Professional body | (is itself the organization) | No — sets standards | Publishes codes, runs certs, advocates | ACM, IEEE-CS, ISACA, CAN-Nepal |

*ℹ️ The test that separates them: WHO grants it, and does it have LEGAL FORCE? A driving licence is a licence (government, legal). CAN is a body (may run certs, isn't itself a cert).*

**📊 Depth table — The professional bodies that keep IT professional**

| Body | Focus | What it runs / offers |
|---|---|---|
| ACM | Global computing standards & ethics | The ACM Code of Ethics; conferences, digital library |
| IEEE-CS | Computing/engineering standards | Standards, the software-engineering code (with ACM) |
| ISACA | Governance, audit & security | The CISA and CISM certifications |
| CAN (Computer Association of Nepal) | Nepal's IT community | Advocacy, events, training for local professionals |

*ℹ️ Organizations publish the codes and run the certifications; government runs the licensing. That's the whole map of 'who keeps IT professional'.*

#### 🛠 ACTIVITY — "Cert, license, or code?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Sort the cards**

> **Run it:** Read out **six items** and have pairs (2 min) label each as **Certification / License /
> Code of Ethics / Professional Body**: (1) CCNA, (2) NMC doctor registration, (3) the ACM "avoid
> harm" rule, (4) ISACA, (5) a driving licence (analogy anchor), (6) CAN-Nepal. Take answers aloud
> (3 min) and resolve the two that trip people up — a **driving licence is a *license*** (government,
> legal force), and **CAN is a *body*** that may run certs but isn't itself a cert.

> 🎙️ Speaker note: The deliberate confusable is cert-vs-license — keep returning to "**who grants
> it, and does it have legal force?**" as the test.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A government-granted, legally enforced permission to practice is:
a) a certificate b) ✅ **a license** c) a code of ethics d) a degree

**MCQ 2.** ACM and IEEE-CS are examples of:
a) certifications b) laws c) ✅ **professional organizations (with codes of ethics)** d) employers

**Discussion prompt:** *Should IT workers in Nepal be licensed like engineers and doctors? Pick a side and argue it.*

> 🎙️ Speaker note: Push both sides — *for:* safety-critical systems (banking, health) deserve
> accountability; *against:* licensing slows a fast-moving field, raises barriers for self-taught
> talent, and is hard to enforce when software crosses borders. Reward students who name the
> *trade-off*, not just a slogan.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** employers and outsourcing clients increasingly require **certifications +
adherence to a code of conduct**, and these directly shape your **hireability and pay** as a
graduate. Knowing the difference between a cert (proves skill), a license (legal force), and a code
(ethical commitment) lets you build a credential strategy on purpose instead of collecting random
badges — and lets you read what an employer is really asking for.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. IT is a **partial profession** — it has knowledge and codes, but **no universal licensing**.
2. **Codes** guide behavior; **certification** proves a skill (not integrity); **licensing** has legal force.
3. **Professional bodies** (ACM, IEEE-CS, ISACA, CAN-Nepal) set the standards and run the certs.

**Next session (S8):** turning from workers to **users** — keeping everyday IT use ethical.

---
---

# S8 — Encouraging Ethical Use of IT Resources among Users
**Lecture hour 3 of 5 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"One shared Wi-Fi password, three problems."**

> **Deliver (≈2 min):** Set the scene. "The office Wi-Fi password is shared with the whole team.
> Someone uses it to **torrent movies**, another installs a **cracked Photoshop**, a third runs a
> **crypto miner on the server overnight.**"
>
> **Run the question (≈3 min):** "Did any **outsider hack** anything?" — No. "So **whose problem is
> it**?" Take a few answers. Pull them together: the threat came from *inside*, from **ordinary
> users**, doing things they thought were harmless or invisible. The lesson lands in one line:
> **users need rules, not just tools.** A network is only as ethical as the people typing the
> password.

> 🎙️ Speaker note: Resist the urge to call it "a security problem" — frame it as an **ethics +
> responsibility** problem first; the security units (5–8) come later. Agenda on board: who is a
> "user" → Acceptable Use Policy → software piracy → inappropriate use.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Who Is an "IT User" — and Why Their Behavior Matters `[THEORY]` `[~8 min]`

[SLIDE] **The insider risk**

> **Deliver:** Define it broadly and deliberately: an **IT user** = **anyone who uses an
> organization's IT resources** — staff, students, customers, contractors. Not just "the IT
> department." Then deliver the key statistic-shaped idea: **most security and ethics incidents start
> with ordinary users, not hackers.** This is the **"insider" risk** — and it's usually not
> malicious, just careless: a clicked phishing link, a reused password, a USB drive from home, a
> cracked app "to get work done."
>
> Explain why this reframing matters: if most harm starts inside, then **buying more security tools
> won't fix it** — you have to change *user behavior.* That's what the rest of the session
> (AUP, anti-piracy, appropriate-use norms) is actually for.

- 🇳🇵 **Local example (walk it):** a **college computer lab** where students **install games and
  cracked software** on shared PCs — slowing them, filling them with malware, and ruining them for
  the next class. No hacker involved; the damage is **100% insider**, and *every* student who
  installed something contributed.

> ❌ **Misconception:** *"Only the IT department is responsible for misuse."*
> ✅ **Correction:** "**Every user shares responsibility** for safe, ethical use. The IT department
> locks the doors — but if you prop them open, that's on you. Security is a shared duty, not a
> department."

> 🎙️ Speaker note (transition): "If users are the risk, how does an organization set expectations for
> thousands of them at once? With a single document everyone signs — the AUP."

**📊 Depth table — The insider risk — careless (not malicious) acts that cause real harm**

| Everyday user action | The harm it causes | Who is affected |
|---|---|---|
| Clicking a phishing link | Credentials stolen, malware installed | The whole organization's network |
| Reusing one password everywhere | One leak unlocks every account | The user and everyone in shared systems |
| Plugging in a personal USB | Malware jumps onto work machines | Colleagues, shared servers |
| Installing a cracked app 'to get work done' | Malware + licence violation | The firm (legal + security) |
| Installing games on a shared lab PC | Slows the machine, fills it with malware | The next class / every other student |
| Sharing the Wi-Fi/server password freely | Untraceable misuse (torrents, mining) | The organization that owns the network |

*ℹ️ None of these is a 'hacker' — the damage is 100% insider and usually careless, not malicious. That's why the fix is behaviour, not just tools.*

#### Concept 2 — Acceptable Use Policy (AUP) `[THEORY]` `[EXAMPLE]` `[~8 min]`

[SLIDE] **The rulebook users sign**

> **Deliver:** An **AUP (Acceptable Use Policy)** = a document stating **what users may and may not
> do** with the organization's IT resources. Explain the **four things every AUP defines** — and why
> each is there:
> - **Permitted use** — what you *can* do (work tasks, reasonable limited personal use).
> - **Prohibited use** — what you *can't* (piracy, personal USBs, accessing offensive content,
>   side businesses on company email).
> - **Monitoring** — a clear statement that the organization **may monitor** your use (this is what
>   makes later monitoring *fair* — you were told in advance; ties to S9 surveillance).
> - **Consequences** — what happens if you breach it (warning → dismissal → legal action).
>
> Stress the one feature that gives an AUP its ethical force: **users acknowledge/sign it.** That
> signature converts a vague expectation into an **informed, consented agreement** — you can't later
> say "I didn't know."

- 🇳🇵 **Local example:** a **bank or telecom (NTC / Ncell)** staff AUP that **bans personal USB
  drives and unlicensed software**; a **university's IT-use policy** that students agree to at
  enrolment. These are the same insider risks from Concept 1, now governed by a signed rule.

> **Mini activity (≈2 min):** *"Draft 3 rules you'd put in your college lab's AUP."* Collect a few
> aloud and quickly classify each as permitted / prohibited / monitoring / consequence. Reward rules
> that name a **consequence** — students almost always forget that an unenforced rule is just a
> suggestion (echoes Unit 1: enforcement beats the document).

**📊 Depth table — The four things every AUP defines**

| AUP element | What it states | Example clause |
|---|---|---|
| Permitted use | What you may do | Work tasks; reasonable limited personal browsing |
| Prohibited use | What you may not do | No piracy, no personal USBs, no side business on company email |
| Monitoring | That the org may watch use | 'Your email and web use may be monitored' (makes later monitoring fair) |
| Consequences | What happens on breach | Warning → suspension → dismissal → legal action |

*ℹ️ The signature is the ethical hinge: it converts a vague expectation into informed, consented agreement — 'I didn't know' stops being available.*

**📊 Depth table — A lab/office AUP — Allowed vs Prohibited**

| Allowed | Prohibited |
|---|---|
| Using PCs for coursework and assignments | Installing cracked or unlicensed software |
| Reasonable, brief personal use on a break | Torrenting movies or games on the network |
| Saving work to approved storage | Plugging in personal USB drives without scanning |
| Printing documents you need | Accessing offensive or illegal content |
| Reporting a fault to IT | Running a side business on company email/resources |
| Using licensed, provided applications | Crypto-mining or unauthorised background jobs |

*ℹ️ This two-column card IS the AUP for most everyday cases — it draws the line in advance, before anyone can claim ambiguity.*

#### Concept 3 — Software Piracy `[THEORY]` `[EXAMPLE]` `[~9 min]`

[SLIDE] **Using what you didn't license**

> **Deliver:** **Software piracy** = **copying, installing, or distributing software without a valid
> license.** Lay out the **forms** so students see how wide it is:
> - **Counterfeiting** — selling fake copies as genuine.
> - **Unlicensed installs** — putting one purchased copy on ten machines, or installing a cracked
>   version.
> - **License violation** — exceeding what your license actually permits (e.g. a 5-seat license used
>   by 50 people).
>
> Make the dual-harm point explicit: piracy is **both a legal harm** (copyright infringement — full
> treatment in **Unit 3, Intellectual Property**) **and an ethical harm** (you took the value of
> someone's work without paying — a fairness violation). Don't let it collapse into "just illegal";
> the ethics stands on its own even where enforcement is weak.

- 🇳🇵 **Local example:** **high software-piracy rates across Nepal / South Asia**; countless offices
  running **cracked Windows / Office**; and the **"everyone does it" normalization** — the Unit 1
  trap where something stops *feeling* wrong because it's everywhere. Name it as a trap, not an
  excuse.

> ❌ **Misconception:** *"It's only piracy if I sell it."*
> ✅ **Correction:** "**Using an unlicensed copy is already a violation** — no sale required. The
> wrong isn't *profiting*; it's *using value you never paid for.* Installing one cracked copy for
> yourself already crosses the line."

> 🍿 **Fun analogy (deliver it):** "Cracked software is like **sneaking into a movie hall** — the
> film still plays, no one's obviously poorer tonight, it feels victimless. But you were **never
> entitled to the seat.** The harm is real even though it's invisible at the moment you sit down."

**📊 Depth table — Three forms of software piracy**

| Form | What it is | Example |
|---|---|---|
| Counterfeiting | Selling fake copies as if genuine | A shop selling pirated Windows DVDs as 'original' |
| Unlicensed install | One purchased copy on many machines, or a cracked version | Installing cracked AutoCAD across a whole office |
| Licence violation | Exceeding what the licence permits | A 5-seat licence actually used by 50 staff |

*ℹ️ All three are piracy even with no sale involved — the harm is USING value you never paid for, not profiting from it.*

#### Concept 4 — Inappropriate Use of IT Resources `[THEORY]` `[~5 min]`

[SLIDE] **Right tools, wrong purpose**

> **Deliver:** **Inappropriate use** = using **organizational resources for unauthorized, personal,
> or harmful purposes.** Unlike piracy, the software might be perfectly licensed — the problem is the
> **purpose.** Give the spread of examples: **excessive personal browsing / streaming / gaming**,
> **accessing offensive content**, **running a side business on company email**, **installing
> unauthorized apps.** The common thread: resources provided for work, diverted to non-work or
> harmful ends.

- 🇳🇵 **Local example:** a **government-office computer used for personal Facebook and online
  shopping during work hours** — a familiar sight, and a clean example of inappropriate use that
  isn't *illegal* but wastes public resources and time.

> **Mini case (pose, take 2–3 answers, ≈2 min):** Is checking **eSewa / Khalti** and replying to a
> **family message** at work "inappropriate use"? **Where's the line?** Draw out a workable test:
> **reasonableness + the AUP + impact on your work.** A 30-second eSewa payment on a break is
> reasonable; streaming cricket all afternoon isn't. Land it: most real cases are about *degree and
> impact*, which is exactly why the **AUP exists to draw the line in advance.**

> 🖼️ Visual: an AUP **"Allowed vs Prohibited"** two-column card; a **software-piracy types** diagram
> (counterfeiting / unlicensed install / license violation); an illustrative **Nepal / South Asia
> piracy-rate bar.**

**📊 Depth table — Where's the line? — everyday office actions (Nepal AUP)**

| Action | Typical verdict | Why |
|---|---|---|
| Charging your phone on the office PC | Depends | Trivial, but some AUPs restrict USB ports |
| Installing a cracked PDF editor | Prohibited | Software piracy — a clear licence violation |
| A quick eSewa / Khalti payment on a break | Allowed | Reasonable, brief, no impact on work |
| Running a weekend freelance project on the work laptop | Prohibited | Resource misuse + IP conflict with the employer |
| Plugging in a personal USB to print a file | Depends | Malware risk; often needs a scan or is banned outright |
| Streaming cricket all afternoon | Prohibited | Excessive personal use — impacts work and bandwidth |

*ℹ️ The 'depends' rows are exactly the ones an AUP must spell out in advance — ambiguity is where misuse hides. Test each with reasonableness + AUP + impact.*

#### 🛠 ACTIVITY — "Where's the line?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Allowed, prohibited, or 'depends'?**

> **Run it:** In pairs (2 min), students sort **five everyday actions** into **Allowed / Prohibited /
> Depends** for a typical Nepali office AUP: (1) charging your phone on the office PC, (2) installing
> a cracked PDF editor, (3) a quick eSewa payment, (4) running a weekend freelance project on the
> work laptop, (5) plugging in a personal USB to print a file. Take answers aloud (3 min). The point
> they should reach: the "depends" cases are exactly the ones an AUP must **spell out in advance** —
> ambiguity is where misuse hides.

> 🎙️ Speaker note: (2) is clearly prohibited (piracy); (4) is usually prohibited (resource + IP
> issues); (1), (3), (5) are the genuine "depends" — push them to justify with reasonableness +
> impact.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The document defining what users may/may not do with IT resources is the:
a) EULA b) ✅ **Acceptable Use Policy (AUP)** c) invoice d) warranty

**MCQ 2.** Installing a **cracked** copy of Office for office work (not selling it) is:
a) fine if unsold b) ✅ **software piracy** c) fair use d) open source

**Discussion prompt:** *Is software piracy in Nepal mainly an ethics problem, an affordability problem, or an enforcement problem?*

> 🎙️ Speaker note: There's no single right answer — reward students who argue it's **all three
> interacting**: affordability creates the temptation, weak enforcement removes the deterrent, and
> "everyone does it" erodes the ethics. Connect to Unit 1's "situational" view of misbehavior.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** on **day one of any job you'll sign an AUP**, and breaking it — through
**piracy or misuse** — is one of the **most common reasons people are fired or sued.** It's rarely a
dramatic hack that ends a career; it's a cracked install traced back to you, or company resources
caught powering a side hustle. Knowing the line *before* you cross it is cheap insurance.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Users cause most incidents** — the **insider risk** is real, and every user shares responsibility.
2. **AUPs** set the rules everyone signs (permitted, prohibited, monitoring, consequences).
3. **Piracy** (using unlicensed software) and **inappropriate use** (right tools, wrong purpose) are the two biggest user-ethics issues.

**Next session (S9):** the user's flip side — their **privacy and anonymity.**

---
---

# S9 — Key Privacy and Anonymity Issues
**Lecture hour 4 of 5 (Unit 2) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Where did your data go — and did you ever agree?"**

> **Deliver (≈2 min):** Tell it as a sequence the class will recognize. "You fill a **loan form** at
> a bank. You hand your **number to a SIM dealer**. You **scan a QR to enter a mall.** A week later,
> you're flooded with **spam calls about loans you never asked for.**"
>
> **Run the question (≈3 min):** "Your data clearly **traveled somewhere.** So — **when did you
> consent** to *this*?" Take a few answers; most will admit they don't actually know. That uncertainty
> is the whole topic: in a data-driven economy, your information moves constantly, and the ethical
> question is **who controls it, and whether you agreed.**

> 🎙️ Speaker note: Keep it personal and concrete — every student has gotten an unexplained spam
> call. Agenda on board: data privacy → surveillance → online anonymity → identity & identity theft.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Data Privacy `[THEORY]` `[EXAMPLE]` `[~9 min]`

[SLIDE] **Control over your personal data**

> **Deliver:** Define it precisely — **data privacy** = the **right of individuals to control how
> their personal data is collected, used, and shared.** The keyword is **control**: privacy isn't
> *secrecy*, it's *who decides.* Then teach the three principles that make privacy operational, with
> a one-line reason for each:
> - **Consent** — data should be collected *with your informed agreement*, not silently.
> - **Purpose limitation** — data collected for *one* reason (a loan) shouldn't be reused for
>   *another* (selling to marketers) without asking.
> - **Data minimization** — **collect only what you actually need.** A SIM purchase doesn't need
>   your blood group.
>
> Then name the **harms** when these fail: **profiling** (being silently categorized and targeted)
> and **fraud** (leaked data enabling impersonation — Concept 4). Privacy failures aren't abstract;
> they end in spam calls, scams, and discrimination.

- 🇳🇵 **Local example:** **KYC data** held by Nepali banks and telecoms — among the richest personal
  datasets in the country; Nepal's **Individual Privacy Act, 2075 (2018)**, which recognizes a legal
  right to privacy of personal information; and **reported leaks of citizen data**, which show the
  gap between having a law and enforcing it.

> ❌ **Common misconception:** *"I have nothing to hide, so privacy doesn't matter to me."*
> ✅ **Correction — deliver the analogy:** "Privacy is about **control and power**, not hiding
> wrongdoing. You **lock your door** not because you're doing something wrong inside, but because
> **it's yours to control who enters.** 'Nothing to hide' confuses *secrecy* with *control* — you
> still close the curtains."

> 🎙️ Speaker note (transition): "Privacy is about *you* controlling your data. The flip side is when
> someone *systematically watches* — that's surveillance."

**📊 Depth table — The three data-privacy principles — and what breaking each looks like**

| Principle | One-line meaning | Violation example (Nepal / IT) |
|---|---|---|
| Consent | Collect data only with informed agreement | A SIM dealer selling your number to loan marketers |
| Purpose limitation | Use data only for the reason it was collected | Loan-form data reused to target you with ads |
| Data minimization | Collect only what you actually need | A mall QR form demanding your citizenship number |

*ℹ️ Nepal's Individual Privacy Act 2075 recognises these rights; reported citizen-data leaks show the gap between a law existing and being enforced.*

#### Concept 2 — Surveillance `[THEORY]` `[~8 min]`

[SLIDE] **Systematic monitoring**

> **Deliver:** **Surveillance** = the **systematic monitoring of people's activities,
> communications, or location.** The word *systematic* matters — a one-off glance isn't surveillance;
> a system that logs *everyone, always* is. Walk the **forms**: **workplace monitoring** (email,
> screens, keystrokes), **CCTV**, **government surveillance**, and **app/location tracking.**
>
> Then frame the unavoidable tension at the center of every surveillance debate: **security vs
> privacy.** More monitoring *can* mean more safety (catching fraud, deterring crime) — but every
> increment **costs privacy.** There's no free lunch; the ethical work is deciding *how much*
> monitoring is **proportionate** to the actual risk, and whether people were **told.**

- 🇳🇵 **Local example:** **rising CCTV across Kathmandu**; **employers monitoring staff email and
  screens**; and **SIM / biometric registration** that links your identity to your activity. Each
  trades some privacy for some claimed security — ask the class whether the trade is proportionate in
  each case.

> **Mini case (work it, ≈2 min):** Your employer installs software that logs **every keystroke and
> takes screenshots.** Ask two questions in order: **"Is it ethical?"** and then **"Does telling
> staff in advance change your answer?"** Draw out the key ethical lever: **transparency + consent**
> (the S8 AUP!) shifts secret surveillance toward legitimate monitoring. Same technology, very
> different ethics depending on whether people **knew and agreed.**

> 🎙️ Speaker note: Tie back explicitly — this is why the AUP's "monitoring" clause from S8 exists. A
> disclosed policy is the difference between *monitoring* and *spying.*

**📊 Depth table — Same technology, different ethics — spying vs legitimate monitoring**

| Question | Secret surveillance (spying) | Legitimate monitoring |
|---|---|---|
| Were people told in advance? | No — it's hidden | Yes — stated in a signed AUP (S8) |
| Did they consent? | No | Yes — acknowledged the policy |
| Is the scope proportionate? | Often excessive — everything, always | Limited to a stated, work-related purpose |
| Ethical verdict | Violates privacy / autonomy | Fair — transparency + consent make it legitimate |

*ℹ️ Keystroke logging + screenshots can be either — the SAME technology. Transparency and consent (the S8 AUP clause) are what shift it from spying to monitoring.*

#### Concept 3 — Anonymity Online `[THEORY]` `[~8 min]`

[SLIDE] **A double-edged tool**

> **Deliver:** **Anonymity** = **acting online without revealing your real identity.** The whole
> point of this concept is that anonymity is **neither good nor bad — it's a tool with two edges**,
> and the same feature does both jobs:
> - It **protects** whistle-blowers exposing corruption, activists under pressure, and **free
>   speech** for people who'd be punished for speaking openly.
> - It **shields** trolls, scammers, and criminals who use the same cover to harass and defraud
>   without consequence.
>
> The ethical takeaway: you can't simply ban or fully allow anonymity — any rule that silences the
> troll also silences the whistle-blower. That's why real-name policies (the CFU debate) are so
> contested.

- 🇳🇵 **Local example (the same-tool-opposite-uses case):** anonymous Nepali **Facebook / X pages
  exposing corruption** (anonymity protecting public-interest speech) vs anonymous pages **spreading
  rumors and harassment** (anonymity shielding harm). **Same tool, opposite uses** — which is exactly
  why it's hard to regulate.

> ❌ **Misconception:** *"Online, I'm completely anonymous."*
> ✅ **Correction:** "**IP logs, metadata, and device fingerprints** make *true* anonymity rare. You
> almost always **leave a trail** — which is why people *do* get traced and arrested for anonymous
> posts. Feeling anonymous is not the same as being anonymous."

> 🎙️ Speaker note (transition): "If anonymity is fragile, the thing it's protecting — or
> attacking — is your *identity.* Let's define what that even is online."

**📊 Depth table — Anonymity — the same tool, two opposite edges**

| Anonymity... | Protective edge (good) | Harmful edge (bad) |
|---|---|---|
| Who uses it | Whistle-blowers, activists, the vulnerable | Trolls, scammers, harassers |
| What it enables | Exposing corruption; free speech under pressure | Harassment and fraud without consequence |
| Nepal example | Pages exposing corruption safely | Pages spreading rumours and harassing people |
| Why it can't be banned | Silencing the troll also silences the whistle-blower | Allowing it fully shields the criminal too |

*ℹ️ Same tool, opposite uses — which is exactly why real-name registration is so contested (S9 CFU). Note: true anonymity is rare — IP logs, metadata, and device fingerprints leave a trail.*

#### Concept 4 — Identity & Identity Theft `[THEORY]` `[EXAMPLE]` `[~5 min]`

[SLIDE] **You are your data**

> **Deliver:** Online, **identity** = **the data that represents you** — your name, **citizenship
> number**, **bank / eSewa logins**, **biometrics.** Make the unsettling point: to a system, *you
> are not a person — you are a bundle of data fields*, and whoever controls those fields can *be*
> you. That's **identity theft / impersonation**: **fake profiles** and **stolen credentials**, most
> often obtained through **phishing** (tricking you into handing over your own keys — previewed fully
> in **Unit 7**).

- 🇳🇵 **Local example:** **fake Facebook profiles** impersonating Nepali public figures (reputation +
  fraud harm); and **phishing SMS** posing as **eSewa or a bank** to steal your **OTP** — the single
  most common attack ordinary Nepalis actually face.

> 🍿 **Fun analogy (deliver it):** "Your personal data is like your **house key** — **easy to copy**,
> and you usually **don't notice until someone is already inside.** Nobody steals the house; they
> copy the key and walk in the front door."

**📊 Depth table — How identity gets stolen — method, Nepal example, defence**

| Method | How it works | Everyday defence |
|---|---|---|
| Phishing SMS / call | Fake 'eSewa/bank' message tricks you into sharing an OTP | Never share an OTP; banks never ask for it |
| Fake social profile | Impersonates you or a public figure to defraud contacts | Report it; verify before trusting a request |
| Stolen credentials | A leaked/reused password unlocks your accounts | Unique passwords + two-factor authentication |
| Data-leak reuse | Leaked KYC data used to impersonate you elsewhere | Minimise what you share; watch for misuse |

*ℹ️ Phishing is the single most common entry point (full treatment in Unit 7). Nobody 'steals the house' — they copy the key (your data) and walk in the front door.*

#### 🛠 ACTIVITY — "Trace your data trail" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Map one day of data**

> **Run it:** In pairs (2 min), students pick **one routine action from this morning** (bought a SIM
> top-up, scanned a QR, logged into eSewa, posted on TikTok) and map: **(a)** what personal data they
> handed over, **(b)** who *else* might now have it, and **(c)** whether they actually **consented.**
> Take 3 answers aloud (3 min) and plot each on the "data trail" visual. Close: "Most of you couldn't
> fully answer (b) and (c) — and *that uncertainty* is the privacy problem in one sentence."

> 🎙️ Speaker note: This makes the abstract personal. If a pair stalls, use the hook's spam-call
> chain as the model.

> 🖼️ Visual: a **"data trail"** flow (you → form / QR / SIM → company → third parties); a
> **security-vs-privacy seesaw**; an anonymity **double-edged-sword** icon.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** "Collect only the data you actually need" is the principle of:
a) surveillance b) ✅ **data minimization** c) anonymity d) profiling

**MCQ 2.** Online anonymity is best described as:
a) always good b) always harmful c) ✅ **a double-edged tool** d) impossible

**Discussion prompt:** *Should the government require real-name registration to post on social media? What are the trade-offs?*

> 🎙️ Speaker note: Force the trade-off out — *for:* reduces trolling, harassment, and fake-news
> accounts; *against:* the same rule **silences whistle-blowers and dissent**, concentrates a
> dangerous identity database, and is easily evaded by serious criminals while only catching ordinary
> users. Connect to the anonymity "double edge."

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** as a BIM graduate you'll **handle customer data** — KYC records, payment
details, account logins. Mishandling it can **break Nepal's Individual Privacy Act 2075** *and*
destroy customer trust, which is a **business risk, not just a legal one.** The privacy principles
you learned today (consent, purpose limitation, minimization) are exactly the design rules you'll be
expected to build *into* the systems you ship.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Privacy = control** over your data — built on **consent, minimization, and purpose limitation** (not "having nothing to hide").
2. **Surveillance** trades **security for privacy**; transparency and consent are what make monitoring legitimate.
3. **Anonymity** cuts both ways; your **identity** is now the target, and **phishing** is the usual entry point.

**Next session (S10):** where privacy, anonymity, and harm collide most — **social networking.**

---
---

# S10 — Social Networking Ethical Issues
**Lecture hour 5 of 5 (Unit 2) · 50 minutes · CLOSES UNIT 2**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Nobody broke into a server — people just used the apps."**

> **Deliver (≈2 min):** Tell the chain of events. "A **doctored screenshot** of a Nepali celebrity
> goes viral on **TikTok / Facebook before lunch.** By **evening**, a **teenager is being mocked** in
> her school group chat, and a **'breaking news' rumor** has sparked a **panic.**"
>
> **Run the framing (≈3 min):** "How many **servers were hacked** in that story?" — None. "So who
> did all the damage?" — **Ordinary users**, using the apps exactly as designed. Land the unit's
> closing idea: **social media weaponizes everyday people.** The harm isn't in some hacker's
> basement; it's in the share button, the comment, the silent bystander. Ask: "What turns a small,
> careless act into mass harm here?" — that's Concept 1.

> 🎙️ Speaker note: This session ties Unit 1 (scale/speed/permanence) and S9 (privacy/anonymity)
> together into real, recognizable Nepali events. Agenda on board: why it's an ethics hotspot →
> cyberbullying/harassment → fake news → defamation.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Why Social Networking Is an Ethics Hotspot `[THEORY]` `[~8 min]`

[SLIDE] **Small acts, large harm**

> **Deliver:** Define it — **social networking** = **platforms where users create, share, and
> connect** (Facebook, TikTok, Instagram, X, YouTube). Then explain the **four amplifiers** that turn
> ordinary behavior into outsized harm — these are the Unit 1 IT factors, now made personal:
> - **Scale** — one post reaches **thousands instantly**, not the few people in a room.
> - **Speed** — it spreads **before anyone can check or correct it.**
> - **Anonymity** — people say things they'd **never say to your face** (S9's double edge).
> - **Virality** — the platform's algorithm **actively amplifies** the most emotional content.
>
> Add the social layer: the online **"bystander effect"** — in a crowd of thousands watching someone
> get piled on, **everyone assumes someone else will speak up**, so no one does. The harm grows in
> the silence.

- 🇳🇵 **Local example:** Nepal's **very high Facebook / TikTok usage**, where **viral content shapes
  public opinion and even elections** — a scale of influence that ordinary individuals now hold in
  their thumbs.

> ❌ **Misconception:** *"It's just online — it isn't real / it doesn't count."*
> ✅ **Correction:** "Online harm has **real legal, social, and psychological consequences** — lost
> jobs, depression, arrests under the ETA (Concept 4). The screen is not a shield between the act and
> the harm."

> 🎙️ Speaker note (transition): "Let's take the three biggest harms one at a time — starting with the
> one aimed at a *person*: harassment."

**📊 Depth table — The four amplifiers — how a small act becomes mass harm**

| Amplifier | What it does | Everyday example |
|---|---|---|
| Scale | One post reaches thousands, not a roomful | A rumour shared to a 50k-follower page |
| Speed | Spreads before anyone can check or correct | A fake 'breaking news' clip trending in minutes |
| Anonymity | People say what they'd never say to your face | Abusive comments from throwaway accounts |
| Virality | The algorithm boosts the most emotional content | An outrage post pushed to millions of feeds |
| Bystander effect | In a huge crowd, everyone assumes someone else will act | Thousands watch a pile-on; no one intervenes |

*ℹ️ These are Unit 1's scale/speed/permanence factors, now personal. The harm grows in the silence — passive bystanders are part of the mechanism.*

#### Concept 2 — Cyberbullying & Online Harassment `[THEORY]` `[EXAMPLE]` `[~8 min]`

[SLIDE] **Repeated targeting with digital tools**

> **Deliver:** **Cyberbullying / harassment** = using **digital tools to repeatedly threaten,
> humiliate, or target a person.** Stress the word **repeatedly** — a single rude comment is unkind;
> a *pattern* aimed at someone is harassment. Walk the **forms**: **trolling**, **doxxing**
> (publishing someone's private details to expose them to harm), **group pile-ons**, and **gendered
> harassment** aimed especially at women. Name the cost plainly: the **mental-health impact** is
> severe and well-documented — anxiety, withdrawal, in extreme cases self-harm.

- 🇳🇵 **Local example:** **harassment of Nepali women and public figures** in **Facebook / TikTok
  comment sections**, and ordinary **school group-chat bullying** — the same dynamic at national and
  classroom scale.

> **Mini case (pose, take 2–3 answers, ≈2 min):** Your friend group starts **mocking a classmate in
> a shared chat.** You **say nothing.** Ask directly: **"Are you complicit?"** Draw out the online
> **bystander effect** from Concept 1, and the **duty to intervene** — silence in a group chat reads
> as agreement and *fuels* the pile-on. Push them: what's one low-cost thing a bystander could do
> (DM the target, name it as too far, leave the chat)?

> 🎙️ Speaker note: Don't let "I just didn't join in" pass as innocence — the lesson is that passive
> bystanders are part of the mechanism that makes pile-ons hurt.

**📊 Depth table — Forms of cyberbullying & harassment**

| Form | What it is | Example |
|---|---|---|
| Trolling | Deliberately provoking to upset or derail | Posting inflammatory replies to bait a reaction |
| Doxxing | Publishing private details to expose someone to harm | Leaking a person's home address and phone number |
| Group pile-on | Many people targeting one, amplified by scale | A comment section swarming one individual |
| Gendered harassment | Targeting aimed especially at women | Sexualised abuse of women public figures online |
| Group-chat bullying | Repeated mocking in a shared chat | A class group chat mocking one classmate |
| Threats / intimidation | Direct threats of harm | Menacing DMs meant to frighten a target |

*ℹ️ The common thread is a REPEATED pattern aimed at a person — and the well-documented, severe mental-health impact (anxiety, withdrawal, self-harm).*

#### Concept 3 — Fake News & Misinformation `[THEORY]` `[~8 min]`

[SLIDE] **False information, spread**

> **Deliver:** Teach the **key distinction** carefully, because students conflate them:
> - **Misinformation** = false info spread **carelessly** (you believed it and shared without
>   checking — *no intent to deceive*).
> - **Disinformation** = false info spread **deliberately** to mislead (*intent to deceive* — propaganda,
>   scams, coordinated campaigns).
>
> Then explain **why it spreads faster than truth**: it exploits **emotion** (fear, outrage), rides
> **confirmation bias** (we share what fits our existing beliefs), and is rewarded by **engagement
> algorithms** that **boost outrage** because outrage keeps people scrolling. Truth is boring;
> outrage is viral.

- 🇳🇵 **Local example:** false **earthquake / disaster rumors** that trigger panic, **fake health
  cures**, and **election misinformation** circulating on Nepali social media — each one a case where
  a careless share did real damage to real people.

> ❌ **Misconception:** *"Sharing isn't creating it, so I'm not responsible."*
> ✅ **Correction:** "**Forwarding unverified content spreads the harm** — the **share button is an
> act.** You become a link in the chain that delivers the lie to a thousand more people. 'I only
> forwarded it' is not a defence; it's a description of how the harm scaled."

> 🍿 **Fun analogy (deliver it):** "A lie online travels like a **forwarded festival greeting** —
> **cheap to send, impossible to recall.** Once it's out of your hands it copies itself across the
> country, and your correction never reaches everyone who got the original."

**📊 Depth table — Misinformation vs Disinformation**

| Dimension | Misinformation | Disinformation |
|---|---|---|
| Intent | None — believed it, shared carelessly | Deliberate — intent to deceive |
| Typical source | An ordinary user who didn't check | Propagandists, scammers, coordinated campaigns |
| Example (Nepal) | Forwarding a fake 'health cure' you trusted | A staged rumour to sway an election or scam money |
| Are you responsible? | Yes — the share button is an act | Yes — and the intent makes it worse |

*ℹ️ Both spread because they exploit emotion, ride confirmation bias, and are boosted by engagement algorithms — truth is boring, outrage is viral.*

#### Concept 4 — Defamation & Reputation Harm `[THEORY]` `[EXAMPLE]` `[~5 min]`

[SLIDE] **When a false claim damages someone**

> **Deliver:** **Defamation** = a **false statement, presented as fact, that damages someone's
> reputation.** Drill the dividing line, because it's the most exam-relevant and life-relevant point
> in the session: **opinion / criticism is NOT defamation.** "I didn't like this café" is opinion;
> "this café's owner is a thief" is a false statement of fact — and *that's* what crosses into
> defamation. The test is: **fact vs opinion**, and **true vs false.**
>
> Then connect to Nepali law carefully: in Nepal, online defamation **can be treated as a cybercrime
> under the Electronic Transactions Act, 2063** (full legal treatment comes in **Unit 9**). Note the
> live tension: the same law used against genuine defamation has also been **criticized for chilling
> free speech.**

> ⚠️ **Lecturer caution — verify before teaching:** The **ETA 2063** is older legislation and Nepal's
> cyber-law landscape has been evolving (amendments and proposed new bills). **Verify the current
> legal position against up-to-date sources before presenting specifics in class**, and present the
> "arrests for Facebook posts" material as illustrative of the *debate*, not as settled current law.

- 🇳🇵 **Local example:** Nepali cases where people were **arrested under the ETA for defamatory
  Facebook posts** — and the **ongoing public debate over free speech vs misuse of the law** (critics
  argue it's been used to silence criticism, not just punish genuine lies). Present *both* sides.

> **Mini case (work it, ≈2 min):** Compare **"I think shop X overcharges"** vs **"Shop X is a fraud
> that steals money."** Ask which risks defamation and why. Resolve: the first is **opinion /
> personal experience** (lower risk); the second is a **false statement of fact alleging a crime**
> (defamation risk). Land the practical rule: **state experiences and opinions, not invented facts
> about people.**

> 🖼️ Visual: a **"share / don't share" verification flowchart**; a spectrum graphic
> **opinion → criticism → defamation**; a **"1 post → thousands"** virality spread diagram.

**📊 Depth table — Opinion vs Criticism vs Defamation — classify the statement**

| Statement | Classification | Why / legal risk |
|---|---|---|
| 'I didn't enjoy this café's coffee.' | Opinion | Personal taste — not a factual claim; protected |
| 'This café's service is slow and overpriced.' | Criticism | Honest evaluation of experience; low risk |
| 'The owner of this café is a thief.' | Defamation | False statement of fact alleging a crime; high risk |
| 'I think shop X overcharges.' | Opinion | Framed as a personal view; lower risk |
| 'Shop X is a fraud that steals money.' | Defamation | False factual accusation of a crime; high risk |
| Repeatedly posting a classmate's photo with insults | Harassment | Repeated targeting of a person (not defamation) |

*ℹ️ ⚠️ Verify the current legal position (ETA 2063 and later amendments) before teaching specifics. Rule of thumb: state experiences and opinions, not invented facts about people.*

#### 🛠 ACTIVITY — "Verify before you share" `[ACTIVITY]` `[~6 min]`

[SLIDE] **Run a shocking post through 3 checks**

> **Run it:** Give pairs a plausible shocking headline (e.g. *"BREAKING: bank X collapses, withdraw
> your money now"*). In 2 min they apply **three pre-share checks**: **(1)** Who is the **source**,
> and is it credible? **(2)** Is it **reported anywhere reputable**, or only forwarded? **(3)** Does
> it just **trigger emotion / urgency** (a red flag)? Then they decide: **share, hold, or report.**
> Take 3 pairs aloud (4 min). Close by tying it to a **real recent Nepali viral rumor** — "would
> these three checks have stopped it?" — which is also the CFU discussion prompt.

> 🎙️ Speaker note: The "withdraw your money now" urgency is the tell — manufactured urgency is the
> single most common signature of disinformation and scams. Make students name it.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Deliberately spreading false information to mislead is:
a) misinformation b) ✅ **disinformation** c) satire d) opinion

**MCQ 2.** A false **factual** statement that damages someone's reputation is:
a) criticism b) opinion c) ✅ **defamation** d) anonymity

**Discussion prompt:** *Before sharing a shocking post, what 2 checks should you do? Would they have stopped a recent Nepali viral rumor?*

> 🎙️ Speaker note: Expect "check the source" and "check if a reputable outlet reported it." Push them
> to add "does it just trigger emotion?" — and apply it to a concrete recent rumor so the habit feels
> real, not theoretical.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** your public posts are part of your **professional reputation** — recruiters
check them before they interview you. And in Nepal, a careless **defamatory or harassing post can
also lead to arrest under the ETA.** A single bad share can cost you a job *and* land you in a police
station — which is why "verify before you share" is a professional habit, not just politeness.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Social media **scales everyday acts into big harm** (scale + speed + anonymity + virality + bystander effect).
2. The core issues are **cyberbullying/harassment, fake news (mis- vs disinformation), and defamation** (which excludes genuine opinion/criticism).
3. **Verify before you share** — the share button is an ethical act with legal consequences.

**Next unit (Unit 3):** **Intellectual Property** — copyright, patents, trade secrets, trademarks, and IP misuse.

---
---

# 📋 UNIT 2 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. Answer key at the end.*

### Section A — Multiple Choice (1 mark each)
1. Privileged access (admin rights, personal data) means an IT worker has extra:
   a) salary  b) ✅ responsibility  c) holidays  d) immunity
2. A vendor's "free iPhone" before a tender is best described as:
   a) a discount  b) ✅ a conflict of interest / bribery  c) fair dealing  d) etiquette
3. The duty to give honest technical advice applies most directly to the:
   a) supplier  b) ✅ client  c) competitor  d) regulator
4. A government-granted, legally enforced permission to practice is:
   a) certification  b) ✅ a license  c) a code of ethics  d) a degree
5. ACM and IEEE-CS are examples of:
   a) certifications  b) ✅ professional organizations  c) laws  d) employers
6. Certification mainly proves:
   a) integrity  b) ✅ a specific skill  c) honesty  d) licensing
7. The document defining what users may/may not do with IT resources is the:
   a) EULA  b) ✅ Acceptable Use Policy (AUP)  c) invoice  d) warranty
8. Installing a cracked copy of Office for office use (not selling) is:
   a) fair use  b) ✅ software piracy  c) open source  d) legal
9. "Collect only the data you actually need" is the principle of:
   a) surveillance  b) ✅ data minimization  c) anonymity  d) profiling
10. Online anonymity is best described as:
    a) always good  b) always harmful  c) ✅ a double-edged tool  d) impossible
11. Deliberately spreading false information to mislead is:
    a) misinformation  b) ✅ disinformation  c) satire  d) opinion
12. A false factual statement that harms someone's reputation is:
    a) opinion  b) criticism  c) ✅ defamation  d) anonymity

### Section B — Short Answer (2 marks each)
13. List and explain **three** of the six IT-worker relationships, naming one ethical risk in each.
14. Differentiate **certification** and **licensing** (who grants, legal force, what it proves).
15. What four things does an **AUP** typically define?
16. Explain the **"I have nothing to hide"** fallacy in one or two sentences.
17. Distinguish **misinformation, disinformation,** and **defamation** with one example each.

### Section C — Applied Case (3 marks each)
18. Analyze the **"vendor gift before a tender"** scenario: who are the stakeholders, what's the conflict, and what should the IT manager do? (Use the Unit 1 5-step process.)
19. Classify these four posts as **opinion / criticism / harassment / defamation**, with reasons: (a) "I didn't enjoy this café's coffee." (b) "This café's service is slow and overpriced." (c) "The owner of this café is a thief who poisons customers." (d) repeatedly posting a classmate's photo with insulting captions.

### Section D — Discussion (open-ended)
20. "IT workers in Nepal should be licensed like doctors and engineers." Argue **both sides**, then state your own position.

---

### ✅ Answer Key (Section A)
1-b · 2-b · 3-b · 4-b · 5-b · 6-b · 7-b · 8-b · 9-b · 10-c · 11-b · 12-c

> Sections B–D: grade on key terms — e.g. Q14 must note that licensing is government-granted with
> legal force while certification is voluntary and proves skill; Q19(c) = defamation (false
> statement of fact), (d) = harassment (repeated targeting), (a) = opinion, (b) = criticism.

---

## ✅ Unit 2 complete (full lecturer-ready depth)
The deck is built: **IT246_Unit2.pptx** (92 slides) — diagram-rich, self-contained, and PDF-safe,
carrying all **23 §7A depth tables** (comparison, concrete-example, and scaffolding). This Markdown
source now includes those same depth tables inline under each concept, so the source of truth and
the deck stay in sync.
