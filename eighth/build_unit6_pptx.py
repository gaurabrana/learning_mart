#!/usr/bin/env python3
"""IT250 (eighth) Unit 6 deck — Digitalization in the Nepalese Perspective (S42–S48), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables — each
table on its OWN slide, paginated, never squeezed. Self-contained & PDF-safe. Imports deckkit.py.
Diagrams in images/. Localised to Nepal (Nagarik App, ConnectIPS, eSewa/Khalti/IME Pay, NepalPay QR,
Daraz, TelePlantDoctor, Pashupatinath QR ticketing) with the lecture's characters (Raju, Sita in
Humla, Kanchhi Maiya, Bikash, the vegetable farmer). This unit CLOSES IT 250 (all 6 units).

Adds FRESH the Nepal policy stack deferred from Unit 1 (IT Policy 2072; Digital Nepal Framework 2019
& its 8 sectors; National ID; proposed Startup Act; NRB Payment & Settlement Act 2075 + National
Payment Switch + NepalPay QR interoperability + KYC; the data-protection gap — Privacy Act 2075 +
Electronic Transactions Act 2063 + NO dedicated Data Protection Act; NTA). Presented as accurate but
with a light 'verify current status' framing; contested lecture statistics are flagged 'reported'.
Source: syllabus + instructor lecture PDFs (mapped in Unit6_content_outline.md §0).
Run: python3 build_unit6_pptx.py -> IT250_Unit6.pptx
"""
from deckkit import *

# ============================================================
#                        FRONT MATTER
# ============================================================
add_title("Unit 6 — Digitalization in the Nepalese Perspective",
          "IT 250: Digital Economy  ·  BIM 8th Semester  ·  Sessions S42–S48 (7 lecture hours)  ·  CLOSES THE COURSE",
          "Nepal deep-dive: e-governance, digital financial inclusion, public-sector opportunity vs challenge, and "
          "sector performance (trade, tourism, agriculture, SMEs). Self-contained, PDF-safe, §7A depth tables. "
          "Policy/figures flagged 'verify current status' / 'reported' — do not over-claim precision.")

add_outcomes("Unit 6 — Learning Outcomes","nepal perspective  ·  s42–s48",
    "By the end of this unit, you will be able to:",
    ["Define e-governance and explain its goals, its G2C/G2B/G2G/G2E types, process, and structure (S42–S43)",
     "Describe Nepal's e-governance practices and policy framework — IT Policy 2072, Digital Nepal Framework, National ID (S44)",
     "Explain digital financial inclusion in Nepal, its ecosystem, and its regulation — NRB, NTA, NepalPay QR (S45)",
     "Analyse the opportunities and challenges of public-sector digital transformation, incl. the data-protection gap (S46)",
     "Assess digital transformation's impact on trade, tourism, agriculture, and SMEs in Nepal (S47–S48)",
     "Synthesise Nepal's digital-economy trajectory across all six units of IT 250 (S48)"],
    "This is the final unit of IT 250. It grounds the whole course in Nepal: it applies platforms, network effects, pricing, transformation and the economics of information to Nepal's own state, money, and sectors — and closes with an honest, whole-course verdict.")

add_roadmap("Unit 6 — Roadmap","Where each session fits (S42–S48)",
    ["S42  E-governance: concepts & goals (G2C/G2B/G2G/G2E)",
     "S43  E-governance: process, structure & maturity",
     "S44  E-gov practices & policy in Nepal (policy stack) ⭐",
     "S45  Digital financial inclusion & its regulation",
     "S46  Opportunities, challenges & the data-protection gap",
     "S47  Economic performance: trade & tourism",
     "S48  Economic performance: agriculture & SMEs (closes course)"],
    ["Unit 1  Introduction (digital/K-economy, 4IR) — done",
     "Unit 2  Fundamentals (platforms, network effects) — done",
     "Unit 3  Digital markets, strategy & innovation — done",
     "Unit 4  Digital transformation & currencies — done",
     "Unit 5  Economics of information — done",
     "Unit 6  THIS UNIT — the Nepalese perspective (final)"])

# ============================================================ S42
add_divider("Session 42 · Lecture hour 1 (of 7)","E-Governance: Concepts & Goals",
    "You renew a passport online at midnight, pay the electricity bill from a tea shop in Jumla, and check a citizenship record on your phone — no queue, no ministry visit, no 'aaja hudaina, bholi aaunus'. That shift, from counters to code, is e-governance. This unit asks how far Nepal has actually travelled — and where it is stuck.",
    "OPENING HOOK [~5 min]. Draw out the counter-to-code shift. Agenda: what e-governance is -> its four goals -> the G2C/G2B/G2G/G2E types.")

concept_understand("S42 · Concept 1 · [THEORY]","What E-Governance Is",
    "E-governance is the use of ICT — websites, apps, databases, networks — by government to deliver public services, share information, and interact with citizens more efficiently and transparently. It is the digitalization of government: moving service delivery from paper counters to digital channels, and redesigning the service, not just computerising the old queue.",
    ["Digitalizes services: forms, records, payments and applications move online.",
     "Connects the state to four groups: citizens, businesses, other agencies, and its own staff.",
     "Aim is redesigned, accessible service — not merely 'computers in the office'.",
     "Broader than e-government: also covers participation and decision-making (e-democracy)."],
    None,"E-governance = using ICT to run and deliver government — counters become code.",
    "~7 min. Stress it is redesign, not just scanning old forms. Nagarik App as the anchor example.")
add_examples_table("S42 · Concept 1 · examples","Traditional service vs e-governed service in Nepal",
    ["Service","Traditional (before)","E-governed (after)","Benefit"],
    [["Passport","Queue at the passport dept, forms by hand","Online application + booked appointment","Less time, smaller crowd"],
     ["Electricity bill","Queue at the NEA counter","Pay via eSewa/Khalti/ConnectIPS","Pay anytime, anywhere"],
     ["Vehicle tax (Bluebook)","Queue at transport office, agents","Online / wallet tax payment","Faster, fewer touts"],
     ["PAN / VAT filing","Visit the IRD office","IRD online portal e-filing","Businesses register/file remotely"],
     ["Citizenship/vital records","Ward-office visit, paper ledgers","Nagarik App digital records","Fewer trips to the office"],
     ["Exam results","Notice board / newspaper","Online results portal","Instant, from anywhere"]],
    per_page=6,widths=[1.5,2.5,2.4,1.7],fs=10.5,
    note="E-governance is judged by the 'after' being genuinely easier — not by a scanned PDF of the old form sitting on a website.")
concept_apply("S42 · Concept 1 · [THEORY]","What E-Governance Is",
    "Nepal's Nagarik App is e-governance in one place: a citizen can view PAN details, EPF/CIT balances, vehicle records and more from a phone, instead of visiting several offices. The online passport system lets you apply and book a slot without camping outside the department at dawn. The state's job (identity, records, payment) is being delivered through digital channels.",
    "\"E-governance just means the government has a website.\" A website is a channel; e-governance is redesigning the SERVICE for digital delivery — application, verification, payment and record all online. A scanned paper form you must still submit in person is not e-governance; it is a webpage.",
    "E-governance is the use of ICT (websites, apps, databases, networks) by government to deliver public services, share information and interact with citizens more efficiently and transparently — the digitalization of government from paper counters to digital channels. It is broader than e-government: it also covers citizen participation and decision-making. Nepal examples: Nagarik App, online passport, IRD e-filing.",
    "e-governance · digitalization of government · ICT for public service · e-government vs e-democracy · redesign not scanning")

concept_understand("S42 · Concept 2 · [THEORY]","The Four Goals of E-Governance",
    "E-governance pursues four goals. Transparency: information and processes are open, so citizens can see how decisions and money flow. Efficiency: services are faster and cheaper (no queues, less paper). Accountability: digital records create a trail, so officials can be held answerable. Participation: citizens can give feedback, complain and take part in decisions. Together they aim at cleaner, faster, answerable government.",
    ["Transparency — open information & processes (budgets, tenders, status visible).",
     "Efficiency — faster, cheaper service; less queuing, less paper.",
     "Accountability — digital records leave a trail; responsibility can be traced.",
     "Participation — feedback, grievances and consultation channels for citizens."],
    None,"Four goals: Transparency, Efficiency, Accountability, Participation (T-E-A-P).",
    "~7 min. Link each goal to a Nepal example (e-procurement = transparency + accountability). Use the table.")
add_table_slide("S42 · Concept 2 · scaffolding","The four goals — mechanism & Nepal example",
    ["Goal","How e-governance delivers it","Nepal example"],
    [["Transparency","Open data, visible status & processes","PPMO e-procurement tenders published online"],
     ["Efficiency","Automation, self-service, no queues","eSewa/ConnectIPS bill & tax payment"],
     ["Accountability","Every action logged; auditable trail","Digital records make bribes harder to hide"],
     ["Participation","Feedback, grievance & consultation channels","Online grievance portals; ward feedback"]],
    per_page=4,widths=[1.6,2.9,2.5],fs=11,
    note="The four goals reinforce each other: a transparent, logged process is also more accountable, and a self-service one is more efficient. Weakness in one (e.g. no data-protection law) undermines trust in the rest.")
concept_apply("S42 · Concept 2 · [THEORY]","The Four Goals of E-Governance",
    "Nepal's e-procurement system (PPMO) shows the goals together: tenders are published and submitted online (transparency), bids are processed faster (efficiency), every step is logged (accountability), and vendors can query the process (participation). Where a bribe once greased a paper tender behind a counter, the digital trail makes the same trick far harder — the goals working as one.",
    "\"E-governance is only about doing things faster.\" Speed (efficiency) is just one of four goals. Transparency, accountability and participation matter as much: a fast service that hides its decisions and answers to no one fails the point. Good e-governance is faster AND cleaner AND answerable AND participatory.",
    "E-governance pursues four goals: transparency (open information and processes), efficiency (faster, cheaper, queue-free service), accountability (digital records create an auditable trail so officials can be held answerable), and participation (feedback, grievance and consultation channels for citizens). They reinforce one another — Nepal's e-procurement delivers all four at once — so a system strong on speed but weak on transparency still fails.",
    "transparency · efficiency · accountability · participation · goals reinforce each other · T-E-A-P")

concept_understand("S42 · Concept 3 · [THEORY]","The Four Types: G2C, G2B, G2G, G2E",
    "E-governance is classified by WHO the state connects with. G2C (Government-to-Citizen): services and information to the public. G2B (Government-to-Business): licences, tax, procurement for firms. G2G (Government-to-Government): data and coordination between agencies and tiers (federal, province, local). G2E (Government-to-Employee): internal HR, payroll and records for civil servants. Each flows both ways — citizens/firms also send data back.",
    ["G2C — citizen services & information (the most visible type).",
     "G2B — business-facing: registration, tax, e-procurement, permits.",
     "G2G — agency-to-agency and tier-to-tier data sharing & coordination.",
     "G2E — the government as an employer: staff HR, payroll, records."],
    "s42_egov_types.png","Four types by counterpart: Citizen (G2C), Business (G2B), Government (G2G), Employee (G2E).",
    "~8 min. Use the diagram. Have students place Nagarik App (G2C), IRD e-VAT (G2B), budget system (G2G), payroll (G2E).")
add_examples_table("S42 · Concept 3 · examples","The four e-governance types — what each connects, Nepal example",
    ["Type","Connects","What flows","Nepal example"],
    [["G2C","State <-> Citizens","Services & information to people","Nagarik App, online passport, PAN"],
     ["G2B","State <-> Business","Licences, tax, procurement","IRD e-VAT filing, PPMO e-procurement, OCR company reg."],
     ["G2G","State <-> Government","Data & coordination across agencies/tiers","Federal-province-local data sharing, LMBIS budget system"],
     ["G2E","State <-> Employees","Internal HR, payroll, records","Civil-service payroll & personnel records"]],
    per_page=4,widths=[0.9,1.7,2.6,3.0],fs=10.5,
    note="Same platform can serve several types: Nagarik App is mainly G2C but touches G2B (business records) and G2G (shared registries) behind the scenes.")
concept_apply("S42 · Concept 3 · [THEORY]","The Four Types: G2C, G2B, G2G, G2E",
    "Raju uses G2C when he books a passport slot; his shop uses G2B when it files VAT on the IRD portal and bids on PPMO; the two offices that verify his citizenship use G2G when they share a registry; and the clerk who serves him is paid through G2E payroll. One citizen's morning can touch all four types — which is why joining them up (interoperability) matters so much.",
    "\"E-governance is only citizens using government websites (G2C).\" That is the most visible type, but three others matter: G2B (business services), G2G (agencies sharing data), and G2E (managing staff). Much of the value — and many of Nepal's gaps — lie in G2G: if agencies don't share data, the citizen re-submits the same paper everywhere.",
    "E-governance is classified by counterpart: G2C (Government-to-Citizen — services/info to the public), G2B (Government-to-Business — licences, tax, procurement), G2G (Government-to-Government — data and coordination across agencies and tiers), and G2E (Government-to-Employee — internal HR, payroll, records). Each is two-way. Nepal examples: Nagarik App (G2C), IRD e-VAT (G2B), the LMBIS budget system (G2G), civil-service payroll (G2E).",
    "G2C · G2B · G2G · G2E · classified by counterpart · two-way flows · G2G = interoperability")

add_activity("S42 — 'Sort the service'  ·  ~5 min",
    ["In pairs (2 min): list five Nepali government services you or your family have used.",
     "Classify each as G2C, G2B, G2G or G2E, and name which of the 4 goals it best serves.",
     "Take 3–4 answers aloud (3 min); resolve any that touch more than one type.",
     "Close: note how many are still only 'partly' online — a preview of S46's honest scorecard."],
    "Good sorting: online passport = G2C (efficiency); IRD e-VAT = G2B (transparency/efficiency); PPMO e-procurement = G2B/G2G (accountability); payroll = G2E. Reward spotting services that span types.",
    "ACTIVITY [~5 min].")
add_quiz("S42 — Quick Check  ·  ~5 min",
    [("Q1.  E-governance is best defined as:","q"),
     ("a) government websites only   b) ✅ using ICT to deliver & run public services   c) buying office computers   d) the internet","a"),
     ("     Why: it is the digitalization of government service and interaction, not merely owning computers or a website.","o"),
     ("Q2.  A citizen filing VAT on the IRD portal is which type?","q"),
     ("a) G2C   b) ✅ G2B   c) G2G   d) G2E","a"),
     ("     Why: the state is serving a business (tax filing) — Government-to-Business.","o"),
     ("Discussion: name a Nepali e-service and the goal (transparency/efficiency/accountability/participation) it serves.","o")],
    "QUIZ [~5 min]. Cement the definition, the four goals (T-E-A-P) and the four types (G2C/G2B/G2G/G2E).")
add_summary("S42 · Summary  ·  [~2 min]",
    ["E-governance = using ICT to deliver and run government; it redesigns the service, not just scans old forms.",
     "Four goals: transparency, efficiency, accountability, participation — they reinforce one another.",
     "Four types by counterpart: G2C (citizens), G2B (business), G2G (agencies/tiers), G2E (employees) — all two-way."],
    "Every Nepali digital-government story — Nagarik App, e-passport, e-procurement — fits this frame. Naming the goal and the type is how you diagnose whether a service is real e-governance or just a webpage.",
    "S43 — what happens behind the glass: the process model, the 4-layer architecture, and how mature Nepal's e-governance is.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S43
add_divider("Session 43 · Lecture hour 2 (of 7)","E-Governance: Process, Structure & Maturity",
    "When you tap 'renew' in the Nagarik App, what actually happens behind the glass? Your request travels through layers — a screen, a rules engine, a database, and the servers and wires beneath — then returns as a result you can act on. Understanding that pipeline explains why e-services sometimes work beautifully and sometimes just say 'the server is down'.",
    "OPENING HOOK [~5 min]. Trace one tap through the system. Agenda: the process model -> the 4-layer architecture + security -> maturity stages and where Nepal sits.")

concept_understand("S43 · Concept 1 · [THEORY]","The Process Model: Input → Process → Output → Feedback",
    "E-governance runs on a four-step cycle. Input: the citizen submits a request or data (an application, a payment). Process: the system validates it and applies rules against its databases. Output: the service or result is delivered (a receipt, an approval, a document). Feedback: the citizen rates, complains or the system logs the outcome — and that feeds improvement. It is a loop, not a one-off.",
    ["Input — citizen submits a request/data through the app or portal.",
     "Process — the system validates, checks rules, queries registries.",
     "Output — the result is delivered: receipt, approval, certificate.",
     "Feedback — ratings/grievances/logs close the loop and drive improvement."],
    None,"Cycle: INPUT -> PROCESS -> OUTPUT -> FEEDBACK (a loop, not a one-shot).",
    "~7 min. Emphasise feedback — the step Nepal most often skips, so services don't improve. Use the table.")
add_table_slide("S43 · Concept 1 · scaffolding","The process model — each stage with a Nepal example",
    ["Stage","What happens","Nepal example (paying vehicle tax)"],
    [["Input","Citizen submits request/data","Enter Bluebook & vehicle details, choose to pay"],
     ["Process","Validate, apply rules, query registries","System checks records, computes tax + penalty"],
     ["Output","Deliver the service/result","Digital receipt & updated tax status issued"],
     ["Feedback","Rate, complain, log for improvement","Rating/grievance; logs flag repeated errors"]],
    per_page=4,widths=[1.3,2.8,3.0],fs=11,
    note="Skipping feedback is why some Nepali e-services never improve: without ratings and logs feeding back, the same friction repeats every year.")
concept_apply("S43 · Concept 1 · [THEORY]","The Process Model",
    "When Kanchhi Maiya renews her scooter tax online: she enters the vehicle details (input), the system checks her records and calculates tax plus any penalty (process), issues a digital receipt and updates her status (output), and she can rate the experience or file a grievance if it failed (feedback). If the department reads that feedback, next year's flow gets smoother — that is the loop working.",
    "\"An e-service ends when you get your receipt.\" The output is not the end — feedback is. Without capturing ratings, complaints and error logs, a service cannot improve, and citizens hit the same problem every year. The loop, not the transaction, is the model.",
    "E-governance follows a four-step process cycle: Input (the citizen submits a request or data), Process (the system validates and applies rules against its databases), Output (the service or result is delivered — receipt, approval, certificate), and Feedback (ratings, grievances and logs close the loop and drive improvement). It is a loop, not a one-off; skipping feedback is why services stop improving.",
    "input · process · output · feedback · a loop not a one-shot · feedback drives improvement")

concept_understand("S43 · Concept 2 · [THEORY]","The 4-Layer Architecture & Security",
    "An e-governance system is built in four layers. Presentation: the app/website/portal you see and touch. Application: the business logic — rules, workflows, validation. Data: the databases and registries (citizen, PAN, vehicle, land). Infrastructure: the servers, network and data centre underneath. Security wraps every layer: National-ID login, encryption of data, and 2FA/OTP to confirm identity.",
    ["Presentation — the interface: Nagarik App screen, e-passport portal.",
     "Application — rules & workflows: validates forms, routes requests.",
     "Data — registries & databases: citizen, PAN, vehicle, land records.",
     "Infrastructure — servers, network, the Govt Integrated Data Centre; security wraps all four."],
    "s43_egov_architecture.png","Four layers: Presentation / Application / Data / Infrastructure; security wraps all.",
    "~8 min. Use the stack diagram. 'Server down' = infrastructure layer failed. Security is not a 5th layer — it crosses all.")
add_table_slide("S43 · Concept 2 · scaffolding","The four architecture layers — role & Nepal example",
    ["Layer","Role","Nepal example"],
    [["Presentation","What the citizen sees & touches","Nagarik App screen; e-passport portal"],
     ["Application","Business logic — rules, workflows, validation","Checks eligibility, computes fees, routes requests"],
     ["Data","Databases & registries that hold records","Citizen, PAN, vehicle, land registries"],
     ["Infrastructure","Servers, network, hosting","Government Integrated Data Centre, fibre, cloud"],
     ["Security (all layers)","Protects every layer","National-ID login, encryption, 2FA/OTP"]],
    per_page=5,widths=[1.4,2.7,2.6],fs=11,
    note="Layering lets one layer change without breaking the others (a new app UI can reuse the same data layer). Security is drawn as crossing all four, not sitting inside one.")
concept_apply("S43 · Concept 2 · [THEORY]","The 4-Layer Architecture",
    "Renewing a passport touches all four layers: the portal you fill in (presentation), the rules that check your eligibility and slot (application), the citizenship and passport registries it reads (data), and the data-centre servers hosting it (infrastructure) — while National-ID login, encryption and OTP keep it secure. When people say 'the site is down', it is usually the infrastructure layer, not the app design, that failed.",
    "\"Security is just one more layer on top.\" Security is not a layer — it crosses ALL four: the login (presentation), authorised workflows (application), encrypted registries (data), and hardened servers (infrastructure). Bolt it onto only one and the others leak.",
    "An e-governance system has four layers: Presentation (the app/website interface), Application (business logic — rules, workflows, validation), Data (databases and registries: citizen, PAN, vehicle, land), and Infrastructure (servers, network, data centre). Security — National-ID login, encryption, 2FA/OTP — wraps every layer rather than being a separate one. Layering lets one layer change without breaking the others.",
    "presentation · application · data · infrastructure · security across all layers · Govt Integrated Data Centre")

concept_understand("S43 · Concept 3 · [THEORY]","E-Governance Maturity (the UN 4 stages)",
    "E-governance grows through maturity stages. The UN model has four: Emerging (static information only — read a webpage), Enhanced (downloadable forms and richer content), Transactional (do a two-way transaction — pay, apply, submit online), and Connected (services joined up across agencies around one identity, proactive and seamless). Countries climb this ladder; Nepal is reportedly around the transactional stage for many services, not yet connected.",
    ["Emerging — information only; you can read but not act.",
     "Enhanced — download forms, more content; still no online transaction.",
     "Transactional — pay, apply, submit fully online (two-way).",
     "Connected — services integrated across agencies around one identity; proactive."],
    None,"Maturity ladder: Emerging -> Enhanced -> Transactional -> Connected. Nepal ~ transactional.",
    "~7 min. Nepal has transactional services (pay tax, apply passport) but they are not 'connected' (siloed). Use the table.")
add_comparison_table("S43 · Concept 3 · comparison","The four maturity stages — what a citizen can do, and Nepal's position",
    ["Stage","What the citizen can do","Nepal position (reported)"],
    [["Emerging","Read static information on a page","Long past this stage"],
     ["Enhanced","Download forms, richer content","Achieved widely"],
     ["Transactional","Pay, apply, submit fully online","Reached for many services (tax, passport)"],
     ["Connected","One identity, services joined across agencies, proactive","Not yet — systems remain siloed (the main gap)"]],
    per_page=4,widths=[1.4,3.0,2.6],fs=11,
    note="Reported positioning — treat as indicative, not an official score. Nepal's leap from 'transactional' to 'connected' needs shared identity (National ID) and data sharing (G2G interoperability).")
concept_apply("S43 · Concept 3 · [THEORY]","E-Governance Maturity",
    "Nepal can already do transactional e-governance — pay vehicle tax, apply for a passport, file VAT online. But it is not yet 'connected': the passport office, tax office and citizenship registry run on separate systems that don't share one identity, so a citizen re-submits the same documents to each. Reaching the connected stage is exactly what National ID + G2G data sharing (S44) is meant to unlock.",
    "\"Once services are online, e-governance is complete.\" Being online (transactional) is stage 3 of 4. The hardest, highest stage is 'connected' — one identity, agencies sharing data, government acting proactively. Nepal's real gap is not putting services online but joining them up.",
    "E-governance maturity is often modelled in four UN stages: Emerging (static information only), Enhanced (downloadable forms, richer content), Transactional (pay/apply/submit fully online, two-way), and Connected (services integrated across agencies around one identity, proactive and seamless). Nepal is reportedly around the transactional stage for many services but not yet connected — systems remain siloed, which is its central e-governance gap.",
    "maturity stages · emerging · enhanced · transactional · connected · Nepal ~ transactional · 'connected' needs data sharing")

add_activity("S43 — 'Rate the maturity'  ·  ~5 min",
    ["In pairs (3 min): pick one Nepali e-service (passport, vehicle tax, PAN, exam results).",
     "Place it on the maturity ladder (emerging/enhanced/transactional/connected) with a reason.",
     "Name the ONE change that would push it up a stage.",
     "Take 3–4 answers aloud (2 min); most will land at transactional, not connected."],
    "Expected: most services rate 'transactional' (you can pay/apply) but not 'connected' (they don't share data). The upgrade is usually shared identity + inter-agency data sharing. Reward naming the specific missing link.",
    "ACTIVITY [~5 min].")
add_quiz("S43 — Quick Check  ·  ~5 min",
    [("Q1.  The correct order of the e-governance process model is:","q"),
     ("a) output-input-process-feedback   b) ✅ input-process-output-feedback   c) process-input-feedback-output   d) input-output-process-feedback","a"),
     ("     Why: the citizen submits (input), the system processes, delivers the result (output), then feedback closes the loop.","o"),
     ("Q2.  Which architecture layer holds citizen, PAN and vehicle registries?","q"),
     ("a) presentation   b) application   c) ✅ data   d) infrastructure","a"),
     ("     Why: the data layer is the databases/registries; infrastructure is the servers/network beneath them.","o"),
     ("Discussion: at which maturity stage is Nepal, and what would move it to 'connected'?","o")],
    "QUIZ [~5 min]. Drill the process order, the four layers, and the transactional-vs-connected distinction.")
add_summary("S43 · Summary  ·  [~2 min]",
    ["Process model: input -> process -> output -> feedback — a loop; skipping feedback stops improvement.",
     "Four layers: presentation, application, data, infrastructure; security wraps all four (not a 5th layer).",
     "Maturity ladder: emerging -> enhanced -> transactional -> connected; Nepal is ~transactional, not yet connected."],
    "This is the engineering reality behind every e-service. Knowing the layers tells you what 'the server is down' means, and the maturity ladder tells you Nepal's real task is joining services up, not just putting them online.",
    "S44 — from architecture to reality: Nepal's actual e-gov initiatives and the policy stack (IT Policy 2072, Digital Nepal Framework, National ID).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S44
add_divider("Session 44 · Lecture hour 3 (of 7) — the Nepal policy stack, added fresh","E-Governance Practices & Policy in Nepal",
    "Nepal has a citizen-services app, an interbank payment rail, online passports, a national data centre — plus a Digital Nepal Framework promising ~80 initiatives across 8 sectors. On paper, an e-state. So why does Sita in Humla still travel two days for a document? This session separates what is built from what is only written — and pins down the policy stack behind it.",
    "OPENING HOOK [~5 min]. Contrast the policy promise with the Humla reality. Agenda: named initiatives -> the policy framework (fresh) -> the 8 sectors & the integration gap. NOTE: policy names/dates from general knowledge — flag 'verify current status'.")

concept_understand("S44 · Concept 1 · [EXAMPLE]","Nepal's E-Governance Initiatives",
    "Nepal has launched several concrete e-governance systems. Nagarik App bundles citizen services (PAN, EPF/CIT, vehicle records) in one app. ConnectIPS (run by NCHL) moves money between banks and pays bills. The online passport system handles applications. The Government Integrated Data Centre (GIDC) hosts government systems. Broadband/rural connectivity programmes extend the network. Together they are Nepal's working e-gov, unevenly built.",
    ["Nagarik App — single citizen-services app (records, payments, certificates).",
     "ConnectIPS / NepalPay — interbank transfers and bill payment rails.",
     "Online passport & IRD e-filing — transactional G2C/G2B services.",
     "Government Integrated Data Centre + broadband expansion — the hosting & connectivity base."],
    None,"Working initiatives: Nagarik App · ConnectIPS · online passport · IRD e-filing · GIDC · broadband.",
    "~7 min. These are real and used — but uneven. Use the table; note the integration gap comes in Concept 3.")
add_examples_table("S44 · Concept 1 · examples","Nepal's e-governance initiatives — purpose & status",
    ["Initiative","Purpose","Status (reported — verify)"],
    [["Nagarik App","One app for citizen services & records","Live; more services being integrated"],
     ["ConnectIPS (NCHL)","Interbank transfer & bill payment","Live and widely used"],
     ["Online passport (DoP)","Apply / book slot for passport","Live; reduces queues"],
     ["IRD online (PAN/VAT)","Register & file tax online","Live for many tax processes"],
     ["Govt Integrated Data Centre","Hosts government systems & sites","Operational hosting base"],
     ["Broadband / rural connectivity","Extend network to rural areas","Ongoing; coverage uneven"]],
    per_page=6,widths=[1.9,2.4,2.4],fs=10.5,
    note="These are genuine, in-use systems — but their reach and integration are uneven, which is the whole tension of this session. Statuses are reported; confirm before quoting.")
concept_apply("S44 · Concept 1 · [EXAMPLE]","Nepal's E-Governance Initiatives",
    "Bikash, a Kathmandu shopkeeper, lives inside these initiatives: he checks PAN and files VAT via IRD online, pays suppliers through ConnectIPS, renews his passport online, and views records on Nagarik App — all hosted in the Government Integrated Data Centre. For him the e-state is real. The catch (Concept 3) is that these systems barely talk to each other, so he still re-enters the same details in each.",
    "\"Nepal has no real e-governance.\" It clearly does — Nagarik App, ConnectIPS, online passport and IRD e-filing are live and heavily used. The honest critique is not absence but unevenness: strong in the cities and for the connected, thin in places like Humla, and poorly integrated across agencies.",
    "Nepal has several working e-governance initiatives: Nagarik App (a single citizen-services app for records and payments), ConnectIPS/NepalPay (interbank transfer and bill-payment rails run by NCHL), the online passport system, IRD online (PAN/VAT filing), the Government Integrated Data Centre (hosting), and broadband/rural connectivity programmes. They are real and widely used but uneven in reach and weakly integrated across agencies.",
    "Nagarik App · ConnectIPS · online passport · IRD online · GIDC · broadband · real but uneven")

concept_understand("S44 · Concept 2 · [THEORY]","The Policy Framework (deferred from Unit 1)",
    "Behind the apps sits a policy stack. IT Policy 2072 (2015) is the framework to promote IT, e-government and IT parks. The Digital Nepal Framework (2019) is the roadmap of ~80 initiatives across 8 sectors. The National ID (Rastriya Parichaya Patra) programme aims to give every citizen one digital identity. A proposed Startup Act would offer tax holidays and seed funding. A reported 'IT Decade 2024–2034' signals a long-term push. Verify current status before quoting.",
    ["IT Policy 2072 (2015) — promote IT industry, e-government, IT parks (being updated).",
     "Digital Nepal Framework 2019 — ~80 initiatives across 8 sectors (see Concept 3).",
     "National ID (Rastriya Parichaya Patra) — one biometric digital identity per citizen (rollout ongoing).",
     "Proposed Startup Act + reported 'IT Decade 2024–2034' — incentives & long-term ambition (verify)."],
    None,"Policy stack: IT Policy 2072 · Digital Nepal Framework 2019 · National ID · proposed Startup Act.",
    "~8 min. FLAG: names/dates from general knowledge — say 'verify current status'. Use the policy-instrument table.")
add_table_slide("S44 · Concept 2 · scaffolding","Nepal's digital policy instruments — what each does & status",
    ["Instrument","What it does","Status (verify current)"],
    [["IT Policy 2072 (2015)","Framework to promote IT, e-gov, IT parks","In effect; being updated"],
     ["Digital Nepal Framework (2019)","Roadmap: ~80 initiatives, 8 sectors","Adopted; implementation partial"],
     ["National ID (Rastriya Parichaya Patra)","One biometric digital identity per citizen","Rollout ongoing"],
     ["Proposed Startup Act / policy","Tax holiday, seed funding for startups","Proposed / partly via startup fund"],
     ["Electronic Transactions Act 2063 (2008)","Legal validity of e-records, e-signature, cybercrime","In force (dated)"],
     ["IT Decade 2024–2034 (reported)","Long-term push to grow IT sector & exports","Announced ambition"]],
    per_page=6,widths=[2.0,2.6,2.2],fs=10.5,
    note="These policy names and dates are assembled from general knowledge for teaching — confirm against current Nepal law before final use. The gap is less about policy on paper than delivery on the ground.")
concept_apply("S44 · Concept 2 · [THEORY]","The Policy Framework",
    "The policy stack explains what the apps are meant to add up to: IT Policy 2072 set the direction, the Digital Nepal Framework (2019) is the concrete roadmap, and National ID is the missing keystone — one identity that would let Nagarik App, tax, passport and health records finally connect (the 'connected' maturity stage from S43). A Startup Act would push the private digital economy the framework relies on.",
    "\"Nepal has no digital policy.\" It has several — IT Policy 2072, the Digital Nepal Framework 2019, National ID, a proposed Startup Act. The real gap is implementation and integration, not the absence of paper. (Caveat: verify exact names, dates and current status — these are taught from general knowledge.)",
    "Nepal's digital policy stack includes: IT Policy 2072 (2015 — framework to promote IT, e-gov and IT parks), the Digital Nepal Framework (2019 — a roadmap of ~80 initiatives across 8 sectors), the National ID programme (one biometric digital identity per citizen — the keystone for 'connected' e-gov), a proposed Startup Act (tax holiday, seed funding), and the Electronic Transactions Act 2063. Present these as accurate but verify current status; the gap is delivery, not policy on paper.",
    "IT Policy 2072 · Digital Nepal Framework 2019 · National ID · Startup Act · verify current status · gap = delivery")

concept_understand("S44 · Concept 3 · [THEORY]","The Digital Nepal Framework's 8 Sectors & the Integration Gap",
    "The Digital Nepal Framework (2019) organises its ~80 initiatives into 8 sectors: Digital Foundation (the base — connectivity, digital ID, payment rails, data centres) plus seven service sectors — Agriculture, Health, Education, Energy, Tourism, Finance, and Urban Infrastructure/Connectivity. The framework is ambitious and adopted, but the honest verdict is partial delivery: e.g. Nagarik App reportedly promised ~60 services but integrated fewer, because agencies don't share data.",
    ["One Digital Foundation underpins seven service sectors.",
     "Seven sectors: Agriculture, Health, Education, Energy, Tourism, Finance, Urban Infra/Connectivity.",
     "Adopted 2019; implementation is partial — the framework outpaces delivery.",
     "Integration gap: siloed systems (Nagarik App reportedly ~60 promised vs ~45 integrated — reported)."],
    "s44_digital_nepal.png","8 sectors: Digital Foundation (base) + 7 service sectors; delivery is partial.",
    "~7 min. Use the 8-sector diagram. The '60 vs 45' figure is reported — flag it. This is the 'built vs written' verdict.")
add_table_slide("S44 · Concept 3 · scaffolding","The Digital Nepal Framework — the 8 sectors & their focus",
    ["Sector","Focus"],
    [["Digital Foundation","The base: connectivity, digital ID, payment rails, data centres"],
     ["Agriculture","E-markets, digital advisory, smart/precision farming"],
     ["Health","Telemedicine, e-health records, supply-chain tracking"],
     ["Education","E-learning, digital content, school connectivity"],
     ["Energy","Smart grid, digital metering & billing"],
     ["Tourism","Online promotion, e-ticketing, digital payments"],
     ["Finance","Digital payments, wallets, financial inclusion"],
     ["Urban Infrastructure & Connectivity","Smart cities, broadband, urban e-services"]],
    per_page=8,widths=[2.3,4.5],fs=11,
    note="Sectors are reported from the 2019 framework — verify before quoting. Note the logic: everything depends on the Digital Foundation; weak foundations (rural internet, ID) cap all seven service sectors.")
concept_apply("S44 · Concept 3 · [THEORY]","The 8 Sectors & the Integration Gap",
    "The framework is why Sita in Humla should, in theory, get health, finance and citizen services digitally. In practice, the Digital Foundation is thin where she lives (weak internet, no cash-out point), so the seven service sectors can't reach her. Even in Kathmandu, the reported gap — Nagarik App promising ~60 services but integrating far fewer — shows the same story: ambition on paper outrunning integration on the ground.",
    "\"The Digital Nepal Framework means Nepal is digitally transformed.\" A framework is a plan, not a finished state. Adopted in 2019 with ~80 initiatives, it is only partly delivered, and its service sectors are capped by a weak Digital Foundation (rural connectivity, ID). Judge by delivery, not by the document. (Figures reported — verify.)",
    "The Digital Nepal Framework (2019) organises ~80 initiatives into 8 sectors: Digital Foundation (connectivity, digital ID, payment rails, data centres) plus seven service sectors — Agriculture, Health, Education, Energy, Tourism, Finance, and Urban Infrastructure/Connectivity. It is adopted but only partly delivered: the service sectors depend on the Digital Foundation, and siloed systems (Nagarik App reportedly ~60 services promised vs fewer integrated) reveal the integration gap.",
    "Digital Foundation + 7 sectors · ~80 initiatives · adopted 2019 · partial delivery · integration/silo gap · reported figures")

add_activity("S44 — 'Built or written?'  ·  ~5 min",
    ["In pairs (2 min): list three items from Nepal's policy stack or the 8 sectors.",
     "For each, mark BUILT (working today) or WRITTEN (planned/partial), with a reason.",
     "Take 3–4 answers aloud (3 min); debate any disputed calls.",
     "Close: most agree the foundation & finance sectors are furthest 'built'; verify statuses."],
    "Good calls: Finance/payments = largely BUILT (eSewa, ConnectIPS, QR); National ID & full integration = still WRITTEN/partial; rural connectivity = partial. Reward using the built-vs-written test and flagging 'verify'.",
    "ACTIVITY [~5 min].")
add_quiz("S44 — Quick Check  ·  ~5 min",
    [("Q1.  The Digital Nepal Framework (2019) is best described as:","q"),
     ("a) a bank   b) a wallet   c) ✅ a roadmap of ~80 initiatives across 8 sectors   d) a law banning cash","a"),
     ("     Why: it is a national roadmap; the '8 sectors / ~80 initiatives' figures are reported — verify current status.","o"),
     ("Q2.  Which is the 'base' sector every other sector depends on?","q"),
     ("a) Tourism   b) ✅ Digital Foundation   c) Energy   d) Health","a"),
     ("     Why: Digital Foundation = connectivity, digital ID, payment rails, data centres — the base for the other seven.","o"),
     ("Discussion: name one policy that is 'built' and one that is still 'written', and why.","o")],
    "QUIZ [~5 min]. Cement the policy stack, the 8 sectors, and the built-vs-written / integration-gap idea.")
add_summary("S44 · Summary  ·  [~2 min]",
    ["Real initiatives: Nagarik App, ConnectIPS, online passport, IRD e-filing, GIDC, broadband — used but uneven.",
     "Policy stack (verify status): IT Policy 2072, Digital Nepal Framework 2019, National ID, proposed Startup Act.",
     "8 sectors = Digital Foundation + 7 services; adopted but partly delivered — a real integration/silo gap."],
    "This is the whole 'built vs written' verdict on digital Nepal. It tells you why the same country can host a slick payment app and still make Sita travel two days for a document — the foundation and integration lag the ambition.",
    "S45 — the sector that is furthest 'built': digital financial inclusion, its ecosystem, and how NRB & NTA regulate it.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S45
add_divider("Session 45 · Lecture hour 4 (of 7) — financial regulation added fresh","Digital Financial Inclusion",
    "A domestic worker in Kathmandu sends money home to Humla in seconds; a vegetable seller in Kalimati accepts a QR scan instead of counting notes; a farmer gets a loan because his wallet history proves he can repay. Digital financial inclusion is pulling the unbanked into the formal economy — but who is still left out, and who keeps the money safe?",
    "OPENING HOOK [~5 min]. Three vignettes of inclusion. Agenda: what inclusion is & why it matters -> the ecosystem, wallet flow & regulation (NRB/NTA, fresh) -> rural gaps & impact.")

concept_understand("S45 · Concept 1 · [THEORY]","Digital Financial Inclusion & Why It Matters",
    "Digital financial inclusion means giving people — especially the previously excluded (rural, unbanked, women, informal workers) — access to and effective use of affordable formal financial services (payments, savings, credit, insurance) through digital channels. It matters because it pulls the cash economy into the formal system: creating records, enabling credit, making remittances cheaper and safer, and widening the tax base.",
    ["Access + USE of formal services (payments, savings, credit, insurance) via digital channels.",
     "Targets the excluded: rural, unbanked, women, informal and daily-wage workers.",
     "Turns cash into records -> credit history -> access to loans previously impossible.",
     "Cheaper, faster, safer remittances; a wider formal economy and tax base."],
    None,"Financial inclusion = affordable formal finance, used, via digital channels — cash economy -> formal.",
    "~7 min. Stress access AND use. Credit access via wallet history is the underrated benefit. Use the stakeholder table.")
add_table_slide("S45 · Concept 1 · scaffolding","Who benefits from digital financial inclusion — by stakeholder",
    ["Stakeholder","Benefit","Nepal example"],
    [["Individual / household","Safe payments, savings, credit history, cheap remittance","Domestic worker sends money home via wallet in seconds"],
     ["Small business / merchant","Accept QR, track sales, access working capital","Kalimati vendor takes NepalPay QR instead of cash"],
     ["Government","Direct benefit transfer, records, wider tax base","Social allowances paid digitally; formalised transactions"],
     ["Economy","More formal activity, data, financial depth","Cash economy shrinks; credit reaches new borrowers"]],
    per_page=4,widths=[1.7,2.8,2.7],fs=10.5,
    note="Inclusion is not charity: each stakeholder gains. The individual gets a credit history from wallet use, the merchant gets working capital, and the state gets records and a wider tax base.")
concept_apply("S45 · Concept 1 · [THEORY]","Digital Financial Inclusion",
    "A vegetable farmer who once dealt only in cash now takes payment by QR, so his sales leave a record. That record becomes a credit history, and a lender who would never have touched an 'invisible' cash trader can now offer him a small loan for seeds. Inclusion turned his cash into data, and data into credit — the mechanism that lifts households and small firms into the formal economy.",
    "\"Financial inclusion just means having a bank account.\" Access is only half — the goal is USE of affordable services (payments, savings, credit, insurance). A dormant account excludes; an actively used wallet that builds a credit history includes. Inclusion is measured by usage and benefit, not by ownership alone.",
    "Digital financial inclusion means giving people — especially the previously excluded (rural, unbanked, women, informal workers) — access to and effective USE of affordable formal financial services (payments, savings, credit, insurance) through digital channels. It matters because it pulls the cash economy into the formal system: creating records, enabling credit (via transaction history), making remittances cheaper and safer, and widening the tax base. It is judged by usage and benefit, not account ownership alone.",
    "financial inclusion · access AND use · formal services · cash -> records -> credit · remittance · unbanked")

concept_understand("S45 · Concept 2 · [THEORY]","The Ecosystem, Wallet Flow & Regulation (NRB, NTA)",
    "Nepal's digital-finance ecosystem has wallets (eSewa — first and largest, Khalti, IME Pay), bank mobile apps, and the interoperable NepalPay QR, riding on rails like ConnectIPS/Fonepay. A payment flows: User -> wallet/platform -> bank -> receiver, settled in seconds. It is regulated: Nepal Rastra Bank (NRB) licenses providers under the Payment & Settlement Act 2075, runs the National Payment Switch, mandates NepalPay QR interoperability and KYC. NTA regulates the telecom/internet it rides on.",
    ["Ecosystem: wallets (eSewa/Khalti/IME Pay) + bank apps + interoperable NepalPay QR.",
     "Wallet flow: User -> platform -> bank -> receiver (settled in seconds).",
     "NRB — central bank: licenses PSPs/PSOs, Payment & Settlement Act 2075, National Payment Switch, KYC.",
     "NepalPay QR interoperability = any wallet pays any merchant's QR; NTA regulates the connectivity."],
    "s45_fin_inclusion.png","Flow: User -> wallet -> bank -> receiver. NRB regulates the money; NTA the connectivity.",
    "~8 min. FRESH regulation content — flag 'verify status'. Interoperability (NepalPay QR) is the key modern win. Use diagram + table.")
add_table_slide("S45 · Concept 2 · scaffolding","The digital-finance ecosystem — each part's role",
    ["Part","Role","Nepal example"],
    [["Wallet / PSP","Holds balance, lets users pay & transfer","eSewa (first & largest), Khalti, IME Pay"],
     ["Bank / bank app","Holds deposits; source & destination of funds","Commercial-bank mobile banking apps"],
     ["Payment switch","Routes & settles between banks/wallets","National Payment Switch (via NCHL)"],
     ["QR standard","One interoperable QR any wallet can pay","NepalPay QR interoperability"],
     ["Regulator — NRB","Licenses providers, sets rules, KYC","Payment & Settlement Act 2075"],
     ["Regulator — NTA","Regulates telecom/internet it rides on","Spectrum, ISPs, mobile data"]],
    per_page=6,widths=[1.6,2.6,2.6],fs=10.5,
    note="Interoperability is the modern leap: before NepalPay QR, a merchant needed a separate QR per wallet; now one QR takes them all. Regulatory details are reported — verify current status.")
concept_apply("S45 · Concept 2 · [THEORY]","The Ecosystem & Regulation",
    "When Kanchhi Maiya scans a NepalPay QR at a shop, her eSewa balance moves through the National Payment Switch to the merchant's bank in seconds — and it works whichever wallet the shop signed up with, because NRB mandates interoperability. NRB licensed eSewa and sets the KYC and limits; NTA keeps the mobile data flowing that carries the scan. Two regulators, two halves: money and connectivity.",
    "\"eSewa and the banks just do whatever they like.\" They operate under NRB rules — licensing, the Payment & Settlement Act 2075, KYC, transaction limits and mandated NepalPay QR interoperability — while NTA governs the connectivity. Digital money in Nepal is regulated on two fronts, not a free-for-all. (Verify current rules before quoting.)",
    "Nepal's digital-finance ecosystem has wallets (eSewa — first and largest, Khalti, IME Pay), bank apps, and the interoperable NepalPay QR, riding on rails such as ConnectIPS/Fonepay. A payment flows User -> platform -> bank -> receiver in seconds. It is regulated on two fronts: NRB (central bank) licenses providers under the Payment & Settlement Act 2075, runs the National Payment Switch, and mandates NepalPay QR interoperability and KYC; NTA regulates the telecom/internet it rides on. (Verify current status.)",
    "eSewa/Khalti/IME Pay · NepalPay QR interoperability · National Payment Switch · NRB (money) · NTA (connectivity) · KYC")

concept_understand("S45 · Concept 3 · [THEORY]","Rural Inclusion Challenges & Economic Impact",
    "Digital finance reaches Kathmandu easily; the hard part is the last mile. Rural inclusion is blocked by unreliable internet, low smartphone ownership and digital literacy, few cash-in/cash-out agents, missing KYC documents, and fraud/trust fears. A reported figure puts reliable rural internet near 41%. Yet the impact where it does reach is large — cheaper remittances, credit from transaction history, and less cash risk. Bridging the last mile is the inclusion agenda.",
    ["Barriers: patchy internet, low smartphone/literacy, few agents, KYC docs, fraud fears.",
     "Reported: ~41% rural reliable internet, and gendered/age-skewed usage — treat as indicative.",
     "Where it reaches: cheaper remittance, credit via wallet history, safety from cash theft.",
     "The agenda: agent networks, simple KYC, offline/USSD options, literacy, and reliable connectivity."],
    None,"Rural gap is the last mile: internet, devices, agents, KYC, trust — but impact is large where it reaches.",
    "~7 min. The 41% figure is reported — flag it. Solutions are concrete (agents, USSD, simplified KYC). Use the challenge->solution table.")
add_table_slide("S45 · Concept 3 · payoff","Rural inclusion — challenge and the matching solution",
    ["Challenge","Why it blocks inclusion","Solution"],
    [["Unreliable internet","Can't complete a transaction","Offline/USSD payments; better rural connectivity"],
     ["Low smartphone / literacy","Can't use the app","Simple UIs, local language, USSD, assisted onboarding"],
     ["Few cash-in/out points","Can't turn digital money into cash","Agent networks, bank/co-op branchless banking"],
     ["Missing KYC documents","Can't open a compliant account","Tiered/simplified KYC for low-value accounts"],
     ["Fraud & trust fears","People avoid digital money","Consumer protection, OTP, awareness campaigns"],
     ["Uneven usage (gender/age)","Excludes women, older & remote users","Targeted programmes; women-agent networks"]],
    per_page=6,widths=[1.9,2.4,2.7],fs=10.5,
    note="Every barrier has a known fix — inclusion is a delivery problem, not a mystery. Usage figures (e.g. skew by gender/age) are reported; verify before quoting.")
concept_apply("S45 · Concept 3 · [THEORY]","Rural Inclusion Challenges",
    "Sita in Humla has a phone but shaky 2G, no nearby agent to cash out a wallet, and no easy way to complete KYC — so the same app that transformed Kathmandu barely helps her. Yet if an agent network and offline/USSD payments reached her, she could receive remittances instantly and build a credit history. The barriers are concrete and the fixes are known; the gap is delivery to the last mile.",
    "\"Digital finance has already included everyone with a phone.\" Owning a phone is not inclusion: without reliable internet, cash-out agents, KYC and trust, rural users like Sita stay excluded. Inclusion is measured at the last mile, and a reported ~41% rural reliable-internet figure shows how far that mile still is.",
    "Rural digital-finance inclusion is blocked by unreliable internet, low smartphone ownership and digital literacy, few cash-in/cash-out agents, missing KYC documents, and fraud/trust fears (a reported ~41% rural reliable-internet figure and gender/age-skewed usage — treat as indicative). Yet the impact where it reaches is large: cheaper remittances, credit from transaction history, and safety from cash. Each barrier has a known fix (agent networks, simplified KYC, offline/USSD, literacy) — inclusion is a last-mile delivery problem.",
    "last mile · rural barriers · agents · simplified KYC · USSD/offline · ~41% (reported) · delivery problem")

add_activity("S45 — 'Include Sita'  ·  ~5 min",
    ["In pairs (3 min): Sita in Humla has a basic phone and shaky internet, no bank branch nearby.",
     "List the barriers stopping her from using a wallet, and match each with one concrete solution.",
     "Name which stakeholder (individual/business/govt) gains most if she is included.",
     "Take 3–4 answers aloud (2 min); check each barrier has a matched fix."],
    "Good answer: barriers = internet, no agent, KYC, literacy; fixes = USSD/offline, agent network, simplified KYC, local-language UI. She gains cheap remittance + credit history; the economy gains formalisation. Reward barrier->fix matching.",
    "ACTIVITY [~5 min].")
add_quiz("S45 — Quick Check  ·  ~5 min",
    [("Q1.  Who is Nepal's regulator that licenses wallets and mandates NepalPay QR interoperability?","q"),
     ("a) NTA   b) ✅ NRB (Nepal Rastra Bank)   c) Daraz   d) the ward office","a"),
     ("     Why: NRB regulates payments/money (Payment & Settlement Act 2075); NTA regulates the telecom/internet it rides on.","o"),
     ("Q2.  Digital financial inclusion is best measured by:","q"),
     ("a) how many own a phone   b) how many have an account   c) ✅ effective USE of affordable formal services   d) number of banks","a"),
     ("     Why: inclusion is about access AND use/benefit — a dormant account is not inclusion.","o"),
     ("Discussion: name one rural inclusion barrier and its concrete solution.","o")],
    "QUIZ [~5 min]. Cement NRB-vs-NTA roles, inclusion = use (not ownership), and one barrier->solution pair.")
add_summary("S45 · Summary  ·  [~2 min]",
    ["Financial inclusion = affordable formal finance, actually USED, via digital channels — turning cash into records & credit.",
     "Ecosystem: eSewa/Khalti/IME Pay + bank apps + interoperable NepalPay QR; flow User->platform->bank->receiver.",
     "Regulated on two fronts: NRB (money — Payment & Settlement Act 2075, switch, KYC) & NTA (connectivity); rural last-mile gap remains."],
    "This is Nepal's furthest-built digital sector and a template for the rest: clear regulation (NRB/NTA), an interoperable standard (NepalPay QR), and a known list of last-mile fixes. It shows what 'connected' delivery can look like when foundation and rules line up.",
    "S46 — the honest scorecard: the opportunities and challenges of public-sector digital transformation, and Nepal's data-protection gap.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S46
add_divider("Session 46 · Lecture hour 5 (of 7) — the data-protection gap added fresh","Opportunities & Challenges in the Public Sector",
    "COVID forced Nepal's offices online almost overnight — and some never went back to paper. E-procurement made bribes harder; ward services went digital. Yet 'the system is online' too often means a PDF nobody can actually submit. This session is an honest scorecard: every win has a matching gap — and one gap, the missing data-protection law, threatens them all.",
    "OPENING HOOK [~5 min]. Set up the honest-scorecard framing. Agenda: the opportunities (with matching gaps) -> the digital divide -> the cybersecurity & data-protection gap (fresh).")

concept_understand("S46 · Concept 1 · [THEORY]","The Opportunities — the Honest Scorecard",
    "Public-sector digitalization brought real wins in Nepal: no-queue 24/7 services, e-procurement that makes bribery harder, a COVID push that moved offices online fast, and ward offices going digital. But an honest analysis pairs each win with its matching gap — services only reach where internet and devices do, e-procurement systems still don't share data, many 'online' services still need a paper visit. The scorecard keeps optimism honest.",
    ["Wins: no queues / 24-7 access; e-procurement curbs bribes; COVID push; ward offices online.",
     "But each win has a matching gap — reach, integration, and 'fake online' undercut them.",
     "Honest scorecard = list the win AND the gap side by side, not just the brochure.",
     "The verdict is 'real progress, unevenly delivered' — not triumph and not failure."],
    None,"Every digital win has a matching gap — judge the public sector by the honest scorecard.",
    "~7 min. Model the scorecard method: never a win without its gap. Use the comparison table.")
add_comparison_table("S46 · Concept 1 · comparison","The honest scorecard — each opportunity vs its matching challenge",
    ["Opportunity (win)","Matching challenge (gap)"],
    [["No queues, 24/7 self-service","Only where internet & devices reach"],
     ["E-procurement makes bribes harder","Systems don't share data; loopholes remain"],
     ["COVID pushed offices online fast","Many 'online' services still need a paper visit"],
     ["Ward offices digitized","Uneven — rural wards lag far behind"],
     ["Faster info & transparency","No data-protection law to safeguard that data"],
     ["Cost & time savings","Staff resistance + political instability stall projects"]],
    per_page=6,widths=[3.0,3.2],fs=11,
    note="This side-by-side is the unit's signature method: for every digital-government claim, ask 'and what's the matching gap?'. Optimism and honesty in one table.")
concept_apply("S46 · Concept 1 · [THEORY]","The Opportunities — Honest Scorecard",
    "Nepal's e-procurement is a genuine win: publishing and processing tenders online makes the old counter-bribe harder and speeds things up. The matching gap: the procurement system doesn't share data with tax or company registries, so other loopholes stay open, and rural offices with weak internet can't always use it. Real progress, real gap — stated together, which is how a professional assesses digital government.",
    "\"Nepal's public sector has either succeeded or failed at going digital.\" Neither — it is uneven. The honest scorecard pairs each real win (e-procurement, COVID push, ward services) with its real gap (reach, integration, fake-online). Refusing to pick a slogan and listing both is the mature assessment.",
    "Public-sector digitalization in Nepal brought real opportunities: no-queue 24/7 services, e-procurement that makes bribery harder, a COVID-driven push that moved offices online quickly, and ward offices going digital. But an honest assessment pairs each win with its matching gap — services reach only where internet/devices do, systems don't share data, many 'online' services still need a paper visit. The verdict is 'real progress, unevenly delivered'.",
    "no-queue services · e-procurement / anti-corruption · COVID push · ward offices online · honest scorecard · win + gap")

concept_understand("S46 · Concept 2 · [THEORY]","The Challenges & the Digital Divide",
    "The gaps have names. Fake 'online' (a web page that still needs a paper visit), unreliable rural internet, no interoperability (systems don't share data), staff resistance plus political instability (frequent changes of government stall projects — a reported 13+ PMs in 16 years), and low digital literacy. Underlying them all is the digital divide: who is left out — by geography (rural), income, age, gender, disability and language.",
    ["Fake 'online' — a webpage, not a completable service.",
     "Rural internet gap + no interoperability (siloed systems, re-submit everywhere).",
     "Staff resistance + political instability stall long projects (reported 13+ PMs / 16 yrs).",
     "The digital divide: rural, poor, old, women, disabled, and non-dominant-language users left out."],
    None,"Challenges: fake-online, rural internet, no interoperability, instability — over a digital divide.",
    "~7 min. The '13+ PMs' figure is reported — flag it. The divide is multi-dimensional. Use the divide table.")
add_table_slide("S46 · Concept 2 · scaffolding","The digital divide — who is left out, and why",
    ["Dimension","Who is left out","Example"],
    [["Geography","Rural & remote citizens","Sita in Humla: shaky 2G, no service point"],
     ["Income","The poor who can't afford a device/data","A daily-wage worker with no smartphone"],
     ["Age","Older citizens unfamiliar with apps","A 70-year-old pensioner facing an app-only form"],
     ["Gender","Women with less device access","Lower reported wallet use by women"],
     ["Disability","Users needing accessible design","No screen-reader support on a portal"],
     ["Language / literacy","Non-Nepali/English or low-literacy users","English-only forms exclude many"]],
    per_page=6,widths=[1.5,2.4,3.0],fs=10.5,
    note="The divide is not one line but several overlapping ones — a poor, older, rural woman faces four at once. 'Digital-by-default' without addressing these excludes exactly the people e-governance should reach. Usage figures are reported.")
concept_apply("S46 · Concept 2 · [THEORY]","The Challenges & Digital Divide",
    "A pension scheme moved 'online' assumes a smartphone, data, literacy and Nepali/English reading — so a poor, older, rural woman can be excluded on four dimensions at once, even though she is exactly who the scheme is for. Add siloed systems (she re-submits the same documents to each office) and frequent government changes stalling fixes, and the challenges compound. Digital-by-default without inclusion widens the very gap it should close.",
    "\"Everyone benefits equally from digital government.\" The digital divide means the opposite risk: making services digital-only can EXCLUDE the poor, rural, old, women, disabled and low-literacy users — sometimes the intended beneficiaries. Good design keeps an assisted/offline path so 'digital-first' doesn't become 'digital-only, some-excluded'.",
    "Public-sector digitalization faces named challenges: fake 'online' (a webpage that still needs a paper visit), unreliable rural internet, no interoperability (siloed systems force re-submission), staff resistance plus political instability (a reported 13+ PMs in 16 years stalling projects), and low digital literacy. Beneath them is the multi-dimensional digital divide — geography, income, age, gender, disability and language — so digital-by-default can exclude the very people it should serve.",
    "fake online · rural internet · no interoperability · instability · digital divide (geography/income/age/gender/disability/language)")

concept_understand("S46 · Concept 3 · [THEORY]","The Cybersecurity & Data-Protection Gap",
    "Digital government collects vast personal data — but Nepal's legal shield is thin. The Individual Privacy Act 2075 (2018) gives a basic privacy right; the Electronic Transactions Act 2063 (2008) covers e-records, e-signatures and cybercrime but is dated; the Constitution recognises privacy. Crucially, Nepal has NO dedicated Data Protection Act setting how agencies must collect, store, share and secure citizen data. This gap threatens every other e-gov win. (Verify current status.)",
    ["Individual Privacy Act 2075 (2018) — a basic privacy right, thin on data handling.",
     "Electronic Transactions Act 2063 (2008) — e-records, e-signature, cybercrime; dated.",
     "The gap: NO dedicated Data Protection Act governing collection/storage/sharing/security.",
     "Consequence: breaches, misuse and low trust undercut adoption of every service above."],
    None,"Nepal's data shield is thin: Privacy Act 2075 + ETA 2063, but NO Data Protection Act (the gap).",
    "~7 min. FRESH content — flag 'verify current status'. This gap threatens all the wins. Use the legal-stack table.")
add_table_slide("S46 · Concept 3 · scaffolding","Nepal's data-protection legal stack — what it covers & the gap",
    ["Instrument","What it covers","Gap / limitation"],
    [["Constitution (Art. 28)","Recognises a right to privacy","A principle, not operational data rules"],
     ["Individual Privacy Act 2075 (2018)","Basic personal-privacy right","Thin on how agencies must handle data"],
     ["Electronic Transactions Act 2063 (2008)","E-records, e-signature, cybercrime","Dated; not a modern data-protection law"],
     ["Sectoral rules (e.g. NRB directives)","Data rules within one sector (finance)","Patchy; no economy-wide standard"],
     ["Dedicated Data Protection Act","— (does not yet exist)","THE GAP: no unified collection/sharing/security law"]],
    per_page=5,widths=[2.1,2.5,2.5],fs=10.5,
    note="Names and dates are taught from general knowledge — verify current Nepal law. The pattern: several partial instruments, but no single modern Data Protection Act, so citizen data lacks economy-wide safeguards.")
concept_apply("S46 · Concept 3 · [THEORY]","The Data-Protection Gap",
    "As Nagarik App, health records and tax data go digital, the state holds a citizen's whole life in databases — yet no dedicated Data Protection Act says how that data must be secured, who may share it, or what happens after a breach. So a leak has weak legal remedy, and cautious citizens hesitate to adopt. This single gap quietly undercuts every win on the scorecard: trust is the foundation digital government stands on.",
    "\"If a service is online and encrypted, citizen data is protected.\" Encryption is a control, not a law. Without a dedicated Data Protection Act governing collection, sharing, retention and breach response, there is no economy-wide legal safeguard — the Privacy Act 2075 and ETA 2063 are thin and dated. Nepal's gap is legal, not just technical. (Verify status.)",
    "Digital government collects vast personal data, but Nepal's legal shield is thin: the Individual Privacy Act 2075 (2018) gives a basic privacy right, the Electronic Transactions Act 2063 (2008) covers e-records/e-signature/cybercrime but is dated, and the Constitution recognises privacy — yet there is NO dedicated Data Protection Act governing how agencies collect, store, share and secure citizen data. This gap enables breaches and misuse, erodes trust, and undercuts adoption of every e-gov service. (Verify current status.)",
    "Privacy Act 2075 · Electronic Transactions Act 2063 · NO dedicated Data Protection Act · the gap · trust · verify status")

add_activity("S46 — 'Win, gap, fix'  ·  ~5 min",
    ["In pairs (3 min): pick one public-sector digital win (e-procurement, COVID push, ward services).",
     "State its matching gap, and say who on the digital divide it risks excluding.",
     "Propose one fix — and say whether the data-protection gap affects it.",
     "Take 3–4 answers aloud (2 min); insist every win is paired with its gap."],
    "Model: e-procurement (win: harder bribes) / gap (no data sharing) / excludes rural offices / fix: interoperability + a Data Protection Act for the data it exposes. Reward win-gap-fix discipline and naming the divide dimension.",
    "ACTIVITY [~5 min].")
add_quiz("S46 — Quick Check  ·  ~5 min",
    [("Q1.  Nepal's biggest legal gap for protecting citizens' digital data is:","q"),
     ("a) too many privacy laws   b) no internet   c) ✅ no dedicated Data Protection Act   d) no computers","a"),
     ("     Why: Privacy Act 2075 & ETA 2063 exist but are thin/dated; there is no unified modern data-protection law. (Verify status.)","o"),
     ("Q2.  Making a service 'digital-only' can widen the:","q"),
     ("a) budget   b) ✅ digital divide (excludes rural/poor/old/etc.)   c) internet speed   d) tax base","a"),
     ("     Why: without an assisted/offline path, digital-only excludes those on the wrong side of the divide.","o"),
     ("Discussion: pick a digital win and state its matching gap and one fix.","o")],
    "QUIZ [~5 min]. Cement the honest scorecard, the multi-dimensional digital divide, and the data-protection gap.")
add_summary("S46 · Summary  ·  [~2 min]",
    ["Honest scorecard: every public-sector digital win (e-procurement, COVID push, ward services) has a matching gap.",
     "The digital divide is multi-dimensional (geography, income, age, gender, disability, language) — digital-only can exclude.",
     "The data-protection gap: Privacy Act 2075 + ETA 2063 exist, but NO dedicated Data Protection Act — it threatens every win."],
    "This is how to assess ANY digital-government claim: pair the win with its gap, ask who's excluded, and check the legal foundation. The missing Data Protection Act is the quiet risk under all of Nepal's e-gov progress.",
    "S47 — from the state to the economy: how digital transformation is reshaping Nepal's trade and tourism (and the LDC-2026 clock).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S47
add_divider("Session 47 · Lecture hour 6 (of 7)","Economic Performance: Trade & Tourism",
    "A pashmina weaver in Bhaktapur sells to a buyer in Berlin through Instagram; a trekking guide fills his season from Booking.com reviews, not a Thamel middleman; you scan a QR to enter Pashupatinath. Digital trade and tourism are rewriting who captures the value — and Nepal's LDC graduation in 2026 makes getting this right urgent.",
    "OPENING HOOK [~5 min]. Value moving from middlemen to producers. Agenda: digital trade + LDC-2026 clock -> digital tourism -> the win-vs-gap beyond the cities.")

concept_understand("S47 · Concept 1 · [THEORY]","Digital Trade, E-Commerce & the LDC-2026 Clock",
    "Digital transformation lets Nepali sellers reach buyers directly. E-commerce (Daraz, HamroBazaar, SastoDeal) and social commerce cut out layers of middlemen; digital payments and UPI-Nepal (cross-border with India, reported from 2024) settle trade instantly. This matters now because Nepal is reported to graduate from Least-Developed-Country status around 2026, losing some trade preferences — so competing on efficient, digital trade becomes urgent, not optional.",
    ["E-commerce + social commerce: producers reach buyers directly, fewer middlemen.",
     "Digital payments & UPI-Nepal (cross-border, reported 2024) settle trade fast.",
     "LDC graduation ~2026 (reported) -> loss of some trade preferences -> digital-trade urgency.",
     "The win is reach & margin; the gap is cash-only and logistics beyond the cities."],
    None,"Digital trade cuts middlemen & speeds payment; LDC-2026 makes efficient digital trade urgent.",
    "~7 min. LDC-2026 & UPI figures are reported — flag them. The win/gap comes next in the table.")
add_comparison_table("S47 · Concept 1 · comparison","Digital trade in Nepal — the win vs the gap",
    ["Dimension","Digital win","The gap"],
    [["Reach","Sell nationwide/abroad online","Rural sellers lack reliable internet"],
     ["Middlemen","Producer-to-buyer, better margins","Trust & returns still favour big platforms"],
     ["Payments","Instant digital / UPI-Nepal settlement","Cash-on-delivery still dominates outside cities"],
     ["Logistics","Courier & tracking in cities","Weak last-mile delivery to remote areas"],
     ["Competitiveness","Efficient trade ahead of LDC-2026","Preference loss hits if trade stays informal"],
     ["Formality","Digital sales leave records","Much trade stays informal/untaxed"]],
    per_page=6,widths=[1.5,2.8,2.6],fs=10.5,
    note="Figures (LDC 2026, UPI-Nepal volumes) are reported — verify. The pattern repeats across sectors: a real digital win capped by an access/logistics/informality gap.")
concept_apply("S47 · Concept 1 · [THEORY]","Digital Trade & the LDC-2026 Clock",
    "A Bhaktapur pashmina workshop that once sold only through an exporter now ships directly to overseas buyers via a website and Instagram, keeping the exporter's margin and settling by digital payment. But a weaver in a hill district with cash-only customers and no courier can't. As Nepal is reported to graduate from LDC status around 2026 and lose some trade preferences, closing that access gap is what keeps Nepali trade competitive.",
    "\"E-commerce automatically makes Nepali trade competitive.\" Only where the foundation reaches: reliable internet, digital payments and last-mile logistics. Beyond the cities, cash-only and weak delivery cap the win — and with LDC-2026 removing preferences, the informal, offline seller is most exposed. The win is real but access-limited.",
    "Digital transformation lets Nepali sellers reach buyers directly: e-commerce (Daraz, HamroBazaar, SastoDeal) and social commerce cut middlemen, while digital payments and UPI-Nepal (cross-border with India, reported from 2024) settle trade instantly. It is urgent because Nepal is reported to graduate from Least-Developed-Country status around 2026, losing some trade preferences — so efficient digital trade becomes essential. The win (reach, margin, speed) is capped by a gap (cash-only, weak logistics, informality) beyond the cities.",
    "e-commerce · social commerce · UPI-Nepal · no middleman · LDC graduation ~2026 (reported) · win capped by access gap")

concept_understand("S47 · Concept 2 · [THEORY]","Digital Tourism",
    "Tourism is one of Nepal's most digital-ready sectors. Operators promote globally at near-zero cost on Instagram and YouTube; travellers book directly via Booking.com and Airbnb, bypassing agents; reviews build trust across borders; and QR ticketing/digital payments (reported at sites like Pashupatinath and Bhaktapur) speed entry and cut leakage. The win is global reach for a small operator; the gap is seasonality and cash-only service beyond the main trails.",
    ["Near-zero-cost global promotion (Instagram, YouTube) for even small operators.",
     "Direct booking (Booking.com, Airbnb) bypasses agents -> more margin to the operator.",
     "Reviews = cross-border trust; QR ticketing & digital payment (Pashupatinath/Bhaktapur, reported).",
     "Gap: seasonality, cash-only beyond main trails, uneven connectivity in remote areas."],
    None,"Digital tourism: near-zero-cost global reach, direct booking, QR ticketing — capped by seasonality & cash.",
    "~7 min. QR-ticketing sites are reported examples — flag. Small operator + global reach is the key story. Use the table.")
add_comparison_table("S47 · Concept 2 · comparison","Digital tourism in Nepal — the win vs the gap",
    ["Dimension","Digital win","The gap"],
    [["Promotion","Global reach at near-zero cost","Needs digital skills & good content"],
     ["Booking","Direct via Booking.com/Airbnb, less agent cut","Commission & platform dependence"],
     ["Trust","Reviews build cross-border confidence","Fake reviews; reputation risk"],
     ["Ticketing","QR entry & digital payment at sites","Reported rollout; cash still common"],
     ["Payments","Cards/wallets for tourists","Rural teahouses often cash-only"],
     ["Resilience","Digital diversifies marketing","Seasonality & shocks (quake, COVID) still bite"]],
    per_page=6,widths=[1.4,2.8,2.7],fs=10.5,
    note="QR-ticketing sites (Pashupatinath, Bhaktapur) are reported — verify. Same shape again: a genuine digital win limited by skills, connectivity and cash beyond the main destinations.")
concept_apply("S47 · Concept 2 · [THEORY]","Digital Tourism",
    "A homestay in Ghandruk that once waited for a Pokhara agent to send trekkers now lists on Booking.com, posts photos on Instagram, and fills its rooms on the strength of reviews — capturing the agent's margin itself. But it takes only cash, its internet drops in peak season, and one shock (a quake or a pandemic) empties the trail. Global reach is real; the access and resilience gaps are just as real.",
    "\"Digital tourism just means having a website.\" The win is direct global reach and trust — promotion, booking and reviews that let a tiny operator sell worldwide without an agent. But without digital skills, reliable connectivity and cashless payment, and against seasonality, the reach is capped. It is a marketing-and-trust transformation, not merely a homepage.",
    "Digital tourism gives Nepali operators near-zero-cost global promotion (Instagram, YouTube), direct booking (Booking.com, Airbnb) that bypasses agents, review-based cross-border trust, and QR ticketing/digital payments at sites (reported: Pashupatinath, Bhaktapur). The win is global reach and margin for even a small operator; the gap is seasonality, cash-only service and uneven connectivity beyond the main trails, plus platform commission and reputation risk.",
    "near-zero-cost promotion · direct booking · reviews = trust · QR ticketing · win = global reach · gap = seasonality/cash")

concept_understand("S47 · Concept 3 · [THEORY]","Beyond the Cities: the Access Barrier",
    "Trade and tourism share one shape: a genuine digital win in Kathmandu, Pokhara and the main trails, capped by an access barrier beyond them. The barrier is concrete — cash-only customers, weak last-mile logistics, unreliable connectivity, seasonality, and low digital skills. So the benefit concentrates where the Digital Foundation (S44) already reaches. Widening the win means fixing the foundation, not adding more apps.",
    ["Both sectors: strong digital win in the cities, thin beyond them.",
     "Barrier = cash-only, weak logistics, patchy internet, seasonality, low skills.",
     "Benefit concentrates where the Digital Foundation already reaches (link to S44).",
     "Fix = foundation (connectivity, payments, logistics, skills), not more apps."],
    None,"Trade & tourism: real digital win in cities, capped beyond by cash, logistics & connectivity.",
    "~6 min. Tie back to S44's Digital Foundation. Use the barrier table; keep it concrete.")
add_table_slide("S47 · Concept 3 · scaffolding","The access barrier beyond the cities — who it hits & the fix",
    ["Barrier","Who it hits","Fix"],
    [["Cash-only customers","Rural sellers & teahouses","Expand QR/agent acceptance rurally"],
     ["Weak last-mile logistics","Remote e-commerce sellers","Courier partnerships, pickup points"],
     ["Unreliable connectivity","All rural digital trade/tourism","Rural broadband, offline-capable tools"],
     ["Seasonality","Tourism operators","Diversify markets & off-season digital promo"],
     ["Low digital skills","Small & older operators","Local-language training, simple tools"]],
    per_page=5,widths=[1.9,2.3,2.6],fs=11,
    note="The fix list is the Digital Foundation from S44 wearing a sector hat — connectivity, payments, logistics and skills. Sector apps can't outrun a missing foundation.")
concept_apply("S47 · Concept 3 · [THEORY]","Beyond the Cities: the Access Barrier",
    "In Kathmandu a shop sells online, takes QR and ships next-day; two hills away an identical shop deals only in cash, has no courier, and loses signal for hours. Same country, same apps, opposite outcomes — because the Digital Foundation reaches one and not the other. That is why 'more apps' won't close the gap: trade and tourism can only go as far digitally as connectivity, payments and logistics have already gone.",
    "\"Adding e-commerce and booking apps will spread the benefit everywhere.\" Apps ride on a foundation. Where connectivity, digital payments and logistics are missing, no app helps — the win stays in the cities. Spreading the benefit means fixing the foundation (S44), which is why sector performance and e-gov foundation are the same problem.",
    "Trade and tourism share one shape: a genuine digital win in the cities and main trails, capped beyond them by a concrete access barrier — cash-only customers, weak last-mile logistics, unreliable connectivity, seasonality, and low digital skills. The benefit therefore concentrates where the Digital Foundation (S44) already reaches. Widening it requires fixing that foundation (connectivity, payments, logistics, skills), not adding more sector apps.",
    "access barrier · cash-only · last-mile logistics · connectivity · Digital Foundation link · win concentrates in cities")

add_activity("S47 — 'City vs hills'  ·  ~5 min",
    ["In pairs (3 min): take one business (a handicraft seller OR a homestay).",
     "Describe its digital win in Kathmandu/Pokhara, then the SAME business two hills away.",
     "Name the specific access barrier and the foundation fix that would close it.",
     "Take 3–4 answers aloud (2 min); connect each fix back to S44's Digital Foundation."],
    "Model: handicraft seller — city (online sales, QR, courier) vs hills (cash-only, no courier, weak net); fix = rural connectivity + QR/agents + logistics. Reward tying the fix to the Digital Foundation, not 'another app'.",
    "ACTIVITY [~5 min].")
add_quiz("S47 — Quick Check  ·  ~5 min",
    [("Q1.  Nepal's reported LDC graduation around 2026 matters for digital trade because it:","q"),
     ("a) bans e-commerce   b) ✅ removes some trade preferences, so efficient digital trade becomes urgent   c) closes Daraz   d) adds tariffs on wallets","a"),
     ("     Why: losing preferences raises the pressure to compete on efficient, formal, digital trade. (Figure reported.)","o"),
     ("Q2.  Digital tourism's core win for a small operator is:","q"),
     ("a) free hotels   b) ✅ near-zero-cost global reach & direct booking   c) no tourists   d) government subsidy","a"),
     ("     Why: promotion, direct booking and reviews let a tiny operator sell worldwide without an agent.","o"),
     ("Discussion: name one trade/tourism digital win and its matching gap beyond the cities.","o")],
    "QUIZ [~5 min]. Cement the LDC-2026 clock, digital tourism's reach win, and the city-vs-hills access gap.")
add_summary("S47 · Summary  ·  [~2 min]",
    ["Digital trade cuts middlemen & speeds payment (UPI-Nepal); LDC graduation ~2026 (reported) makes it urgent.",
     "Digital tourism gives small operators near-zero-cost global reach, direct booking, QR ticketing & review-based trust.",
     "Both share one shape: a real digital win in the cities, capped beyond by cash, logistics & connectivity (the foundation)."],
    "Sector performance is the e-gov foundation seen from the market side: trade and tourism go digital only as far as connectivity, payments and logistics already reach. Fixing the foundation is what turns a city win into a national one.",
    "S48 — closing the unit and the course: agriculture & SMEs, the '4-sector scorecard', and Nepal's whole digital-economy trajectory.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S48
add_divider("Session 48 · Lecture hour 7 (of 7) — closes Unit 6 AND the whole course","Economic Performance: Agriculture & SMEs",
    "TelePlantDoctor lets a farmer photograph a sick crop and get AI advice; a Palpa pickle-maker runs her whole business on a Facebook page and a QR code. The tools are world-class — but a 60-year-old farmer on a 2G phone can't reach them. As we close the course, the theme is 'great tool, broken access' — and whether Nepal can bridge it by 2035.",
    "OPENING HOOK [~5 min]. 'Great tool, broken access.' Agenda: agriculture (tool vs access) -> SMEs (win vs barriers) -> the 4-sector scorecard & the whole-course synthesis.")

concept_understand("S48 · Concept 1 · [THEORY]","Agriculture: Great Tool, Broken Access",
    "Digital tools are transforming what is possible in Nepali agriculture: AI crop advice (TelePlantDoctor, reported with FAO from 2024), mobile banking to buy inputs and receive payment, digital weather and market-price information, and e-markets that connect farmers to buyers. The catch is access: many farmers are older, on 2G phones, with low digital literacy and thin rural connectivity — so the world-class tool can't reach the person who needs it. 'Great tool, broken access.'",
    ["Tools: AI crop advice (TelePlantDoctor, reported 2024), mobile banking, digital weather & prices, e-markets.",
     "Win: better decisions, fair prices, inputs & payments without travelling to town.",
     "Access barrier: older farmers, 2G phones, low literacy, patchy rural internet & data cost.",
     "The theme: the tool is excellent; the access is broken — bridging it is the task."],
    None,"Agriculture: world-class digital tools (TelePlantDoctor, m-banking) held back by broken rural access.",
    "~7 min. TelePlantDoctor/FAO 2024 is reported — flag. 'Great tool, broken access' is the memory line. Use the table.")
add_comparison_table("S48 · Concept 1 · comparison","Digital agriculture in Nepal — the win vs the gap",
    ["Dimension","Digital win","The gap"],
    [["Crop health","AI advice from a photo (TelePlantDoctor)","Older farmers on 2G can't run the app"],
     ["Finance","Mobile banking for inputs & payments","Few rural agents; missing KYC"],
     ["Information","Digital weather & market prices","Low literacy; language barriers"],
     ["Markets","E-markets link farmers to buyers","Weak logistics; cash-only buyers"],
     ["Connectivity","Enables all of the above","Patchy rural internet, data cost"],
     ["Adoption","Younger farmers adopt fast","Ageing farm population lags"]],
    per_page=6,widths=[1.4,2.8,2.7],fs=10.5,
    note="TelePlantDoctor/FAO (2024) is reported — verify. The gap here is sharper than in trade/tourism because the farm population skews older and more rural — access, not tools, is the binding constraint.")
concept_apply("S48 · Concept 1 · [THEORY]","Agriculture: Great Tool, Broken Access",
    "A vegetable farmer photographs a diseased tomato plant, and TelePlantDoctor returns a likely cause and treatment — advice that once needed a rare visiting technician. But his 60-year-old neighbour, on a 2G phone and unable to read the app, never benefits, even though his crop is failing too. The technology is genuinely world-class; the access — device, literacy, connectivity — is broken. Closing that gap, not inventing new apps, is the agenda.",
    "\"Nepal's farmers lack good digital tools.\" The tools are excellent — AI advice, mobile banking, digital markets. The problem is the opposite: access. An ageing, rural, lower-literacy farm population on weak networks can't reach world-class tools. 'Great tool, broken access' names the real constraint. (TelePlantDoctor figure reported — verify.)",
    "Digital tools are transforming Nepali agriculture: AI crop advice (TelePlantDoctor, reported with FAO from 2024), mobile banking for inputs and payments, digital weather and market-price information, and e-markets linking farmers to buyers. But access is the binding constraint — many farmers are older, on 2G phones, with low digital literacy and patchy rural internet, so the excellent tool can't reach the person who needs it. The theme is 'great tool, broken access': the task is bridging access, not inventing more tools.",
    "TelePlantDoctor (reported) · mobile banking · digital weather/prices · e-markets · 'great tool, broken access' · older/2G")

concept_understand("S48 · Concept 2 · [THEORY]","SMEs: the Backbone Goes Digital",
    "Small and medium enterprises are the backbone of Nepal's economy — reported at ~90% of businesses and 50%+ of employment. Digital transformation lets a tiny firm punch above its weight: accept payments by QR, sell through social commerce (Instagram, Facebook Marketplace), reach customers online, and manage stock with cheap apps. But barriers bite: collateral requirements block credit, a digital-skills gap limits adoption, and informality keeps many SMEs outside the formal system.",
    ["SMEs = reported ~90% of businesses, 50%+ of jobs — the economy's backbone.",
     "Digital wins: QR payments, social commerce, online reach, cheap management tools.",
     "Barriers: collateral for credit, digital-skills gap, informality/formalisation cost.",
     "Digital sales history can itself unlock credit — if lenders and rules use it."],
    None,"SMEs (~90% of firms, reported) go digital via QR & social commerce — capped by credit, skills, informality.",
    "~7 min. SME figures are reported — flag. Link back to S45: wallet history as credit is the bridge. Use the table.")
add_comparison_table("S48 · Concept 2 · comparison","Digital SMEs in Nepal — the win vs the gap",
    ["Dimension","Digital win","The gap"],
    [["Payments","Accept QR (NepalPay), fast settlement","Rural customers still cash-only"],
     ["Sales channel","Social commerce (Insta/FB Marketplace)","Platform dependence; ad costs"],
     ["Reach","Sell beyond the local street","Logistics & delivery limits"],
     ["Credit","Sales history can support a loan","Collateral still demanded; thin credit scoring"],
     ["Skills","Cheap apps for stock & accounts","Digital-skills gap, especially older owners"],
     ["Formality","Digital records ease formalisation","Informality persists; formalising has cost"]],
    per_page=6,widths=[1.4,2.8,2.7],fs=10.5,
    note="Figures (~90% of businesses, 50%+ of jobs) are reported — verify. The credit gap is the key one: digital sales history could replace collateral, linking back to S45's inclusion story.")
concept_apply("S48 · Concept 2 · [THEORY]","SMEs: the Backbone Goes Digital",
    "A Palpa pickle-maker sells nationwide from a Facebook page, takes NepalPay QR, and packs orders from phone messages — a one-person firm with a national market. But when she wants a loan to scale, the bank asks for land collateral she doesn't have and ignores her visible digital sales history. Multiply her by the reported ~90% of businesses that are SMEs, and the credit-and-skills gap becomes the economy's gap.",
    "\"SMEs are too small to matter to the digital economy.\" The reverse — SMEs are reported at ~90% of Nepal's businesses and half its jobs, so their digital adoption IS the digital economy. Their binding constraints are credit (collateral over sales history) and skills, not size. Fixing those scales the whole economy. (Figures reported.)",
    "SMEs are the backbone of Nepal's economy (reported ~90% of businesses, 50%+ of employment). Digital transformation lets a tiny firm accept QR payments, sell via social commerce (Instagram, Facebook Marketplace), reach customers online, and manage stock cheaply. But barriers bite: collateral requirements block credit (despite visible digital sales history), a digital-skills gap limits adoption, and informality keeps many outside the formal system. Using digital sales history for credit is the key bridge, linking to financial inclusion (S45).",
    "SMEs ~90% of firms (reported) · QR + social commerce · barriers: collateral, skills, informality · sales history -> credit")

concept_understand("S48 · Concept 3 · [SYNTHESIS]","The 4-Sector Scorecard & the Whole-Course Verdict",
    "Close the unit and the course with one picture. Across all four sectors — trade, tourism, agriculture, SMEs — the pattern is identical: a genuine digital WIN, capped by an access/foundation GAP. That mirrors the whole course: platforms and network effects (U2), markets and strategy (U3), transformation and currencies (U4), and the economics of information (U5) all deliver in Nepal only as far as the Digital Foundation and enabling rules reach. The verdict: real, uneven, foundation-limited progress.",
    ["Four sectors, one shape: real digital win + access/foundation gap (the scorecard).",
     "Course arc: U2 platforms · U3 markets · U4 transformation/currencies · U5 information -> U6 applies them to Nepal.",
     "Nepal's binding constraint is the Digital Foundation + rules (connectivity, ID, data law), not ideas or tools.",
     "Verdict: genuine, uneven, foundation-limited progress — a cashless, e-governed 2035 is possible but not guaranteed."],
    "s48_sme_scorecard.png","4-sector scorecard: each sector = a real win capped by an access/foundation gap.",
    "~7 min. Use the scorecard image to synthesise the whole course. Land the honest verdict; feed the closing discussion.")
add_table_slide("S48 · Concept 3 · scaffolding","The 4-sector digital scorecard — win vs gap",
    ["Sector","Digital win","Main gap"],
    [["Trade","E-commerce, UPI-Nepal, no middleman","Cash-only & logistics beyond cities; LDC-2026"],
     ["Tourism","Near-zero-cost global reach, QR ticketing","Seasonality; rural cash-only"],
     ["Agriculture","AI advice (TelePlantDoctor), m-banking","2G, older farmers, low literacy"],
     ["SMEs","QR + social commerce; national reach","Collateral for credit; skills gap; informality"]],
    per_page=4,widths=[1.3,2.8,2.8],fs=11,
    note="One shape across all four sectors: a genuine digital win capped by an access/foundation gap. Fixing the Digital Foundation (S44) is the single lever that widens every win. Figures reported — verify.")
concept_apply("S48 · Concept 3 · [SYNTHESIS]","The Whole-Course Verdict",
    "Zoom out across IT 250: platforms and network effects (U2) explain eSewa and Daraz; markets and strategy (U3) explain how they compete; transformation and digital currency (U4) explain the payment rails; the economics of information (U5) explain data-driven value — and Unit 6 shows all of it landing in Nepal only as far as connectivity, identity and data law reach. The four-sector scorecard is the course in one table: real wins, real gaps, one foundation to fix.",
    "\"Nepal is either a digital success or a digital failure.\" The whole course rejects the binary. Every sector and every unit shows the same honest shape — genuine progress, capped by the Digital Foundation and missing rules (e.g. a Data Protection Act). A cashless, e-governed Nepal by 2035 is achievable IF the foundation and rules are fixed; it is not automatic.",
    "The four-sector scorecard (trade, tourism, agriculture, SMEs) shows one shape everywhere: a genuine digital WIN capped by an access/foundation GAP. This mirrors the whole course — platforms/network effects (U2), markets/strategy (U3), transformation/currencies (U4), economics of information (U5) all deliver in Nepal only as far as the Digital Foundation (connectivity, digital ID, payment rails) and enabling rules (incl. a Data Protection Act) reach. Verdict: real, uneven, foundation-limited progress — 2035 possible, not guaranteed.",
    "4-sector scorecard · one shape: win + gap · course synthesis (U2–U6) · Digital Foundation is the lever · 2035 possible not certain")

add_activity("S48 — 'Nepal 2035' (capstone)  ·  ~5 min",
    ["In pairs (3 min): using the 4-sector scorecard, argue whether Nepal can be cashless & e-governed by 2035.",
     "Cite one win, one gap, and the single foundation fix that would matter most.",
     "State your verdict (yes / no / conditional) and your one key condition.",
     "Take 3–4 answers aloud (2 min); most land on 'conditional on fixing the foundation & data law'."],
    "Strong capstone answers pair scorecard evidence with the data-protection gap (S46) and the Digital Foundation (S44), ending 'possible IF connectivity, ID and a Data Protection Act are delivered'. Reward a reasoned conditional verdict over a slogan.",
    "ACTIVITY [~5 min] — capstone.")
add_quiz("S48 — Quick Check  ·  ~5 min",
    [("Q1.  The single phrase that best captures Nepali digital agriculture is:","q"),
     ("a) no tools exist   b) fully digital   c) ✅ great tool, broken access   d) illegal","a"),
     ("     Why: the AI/mobile tools are excellent, but older, rural, 2G, low-literacy farmers can't reach them.","o"),
     ("Q2.  SMEs matter to Nepal's digital economy because they are reported to be:","q"),
     ("a) 5% of firms   b) foreign-owned   c) ✅ ~90% of businesses & 50%+ of jobs   d) all in Kathmandu","a"),
     ("     Why: SMEs are the backbone, so their digital adoption largely IS the digital economy. (Figures reported.)","o"),
     ("Discussion: using the 4-sector scorecard, can Nepal be cashless & e-governed by 2035? Defend a verdict.","o")],
    "QUIZ [~5 min]. Close on 'great tool, broken access', SMEs as the backbone, and the whole-course 2035 verdict.")
add_summary("S48 · Summary  ·  [~2 min]",
    ["Agriculture: world-class digital tools (TelePlantDoctor, m-banking) held back by broken rural access.",
     "SMEs (reported ~90% of firms, 50%+ jobs) go digital via QR & social commerce — capped by credit, skills, informality.",
     "The 4-sector scorecard = the whole course in one table: real wins, real gaps, one Digital Foundation to fix."],
    "This closes IT 250: every unit and every Nepali sector shows genuine, uneven, foundation-limited progress. Whether Nepal reaches a cashless, e-governed 2035 depends on delivering the foundation, closing the divide, and passing a data-protection law — not on new ideas.",
    "End of Unit 6 and end of IT 250. Next: consolidate with the cheat sheet, glossary, and end-of-course revision quiz.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min]. This is the final teaching session of the course.")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 6 · Cheat Sheet","One-page revision reference",
    [("E-gov concepts & goals (S42)","E-governance = ICT to run/deliver government (redesign, not scanning). 4 goals: Transparency, Efficiency, Accountability, Participation (T-E-A-P). 4 types by counterpart: G2C (citizens), G2B (business), G2G (agencies), G2E (employees). Nagarik App, IRD e-VAT, PPMO."),
     ("Process, structure, maturity (S43)","Process: Input->Process->Output->Feedback (a loop). Architecture: Presentation/Application/Data/Infrastructure; security wraps all. Maturity ladder: emerging->enhanced->transactional->connected. Nepal ~transactional (siloed), not yet connected."),
     ("Practices & policy (S44)","Initiatives: Nagarik App, ConnectIPS, online passport, IRD, GIDC, broadband. Policy stack (verify): IT Policy 2072; Digital Nepal Framework 2019 (8 sectors: Digital Foundation + Agriculture/Health/Education/Energy/Tourism/Finance/Urban); National ID; proposed Startup Act. Gap = delivery & integration."),
     ("Financial inclusion (S45)","Inclusion = affordable formal finance, USED, digitally (cash->records->credit). Ecosystem: eSewa/Khalti/IME Pay + bank apps + NepalPay QR. Flow: User->platform->bank->receiver. Regulators: NRB (money — Payment & Settlement Act 2075, switch, KYC) + NTA (connectivity). Rural last-mile gap."),
     ("Opportunities, challenges, data gap (S46)","Honest scorecard: each win (no-queue, e-procurement, COVID push, ward services) has a matching gap. Digital divide: geography/income/age/gender/disability/language. Data-protection gap: Privacy Act 2075 + ETA 2063 exist, but NO dedicated Data Protection Act (threatens all wins)."),
     ("Sector performance (S47–S48)","One shape across trade/tourism/agriculture/SMEs: real digital WIN + access/foundation GAP. Trade: e-commerce, UPI-Nepal, LDC-2026. Tourism: global reach, QR ticketing. Agriculture: 'great tool, broken access' (TelePlantDoctor). SMEs ~90% of firms. Fix = Digital Foundation. Figures reported.")])

add_glossary("Unit 6 · Glossary","Key terms — quick reference",
    [("E-governance","Using ICT to deliver and run government services and interaction."),
     ("E-government vs e-democracy","Service delivery vs participation/decision-making online."),
     ("G2C / G2B / G2G / G2E","Government to Citizen / Business / Government / Employee."),
     ("Transparency","Open information and processes citizens can see."),
     ("Accountability","Digital records create an auditable, traceable trail."),
     ("Participation","Feedback, grievance and consultation channels for citizens."),
     ("Process model","Input -> Process -> Output -> Feedback (a loop)."),
     ("Presentation layer","The app/website/portal the citizen sees."),
     ("Application layer","Business logic — rules, workflows, validation."),
     ("Data layer","Databases and registries (citizen, PAN, vehicle, land)."),
     ("Infrastructure layer","Servers, network, data centre (e.g. GIDC)."),
     ("Maturity stages","Emerging -> enhanced -> transactional -> connected."),
     ("Connected government","Services joined across agencies around one identity."),
     ("Nagarik App","Nepal's single citizen-services app (records, payments)."),
     ("ConnectIPS","NCHL interbank transfer & bill-payment rail."),
     ("IT Policy 2072 (2015)","Framework to promote IT, e-gov and IT parks."),
     ("Digital Nepal Framework 2019","Roadmap of ~80 initiatives across 8 sectors."),
     ("Digital Foundation","The base sector: connectivity, ID, payment rails, data centres."),
     ("National ID","Rastriya Parichaya Patra — one digital identity per citizen."),
     ("Startup Act (proposed)","Proposed tax holiday & seed funding for startups."),
     ("Digital financial inclusion","Affordable formal finance, used, via digital channels."),
     ("NepalPay QR","Interoperable QR standard — any wallet pays any merchant."),
     ("National Payment Switch","Routes & settles payments between banks/wallets (NCHL)."),
     ("NRB","Nepal Rastra Bank — regulates payments/money (Act 2075, KYC)."),
     ("NTA","Nepal Telecommunications Authority — regulates telecom/internet."),
     ("KYC","Know Your Customer — identity checks for financial accounts."),
     ("Digital divide","Who is left out — geography, income, age, gender, disability, language."),
     ("Individual Privacy Act 2075","Nepal's basic privacy right (thin on data handling)."),
     ("Electronic Transactions Act 2063","E-records, e-signature, cybercrime (dated)."),
     ("Data Protection Act (missing)","The absent unified law on data collection/sharing/security."),
     ("Honest scorecard","Pairing each digital win with its matching gap."),
     ("LDC graduation (~2026)","Reported loss of some trade preferences -> digital-trade urgency."),
     ("UPI-Nepal","Reported cross-border (with India) instant-payment link."),
     ("Social commerce","Selling via Instagram / Facebook Marketplace."),
     ("TelePlantDoctor","Reported AI crop-advice tool (FAO, 2024)."),
     ("'Great tool, broken access'","Excellent digital tools that access barriers keep out of reach.")])

# ============= CONSOLIDATED END-OF-UNIT / END-OF-COURSE QUIZ =============
add_divider("Unit 6 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (a/b/c/d, answers marked and keyed), then short-answer, applied-case and discussion questions to work from the concept slides and Unit6_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review. (No genuine IT 250 past-paper exists — built from the syllabus + the in-lecture character scenarios.)")
add_quiz("Section A — Multiple choice (answers marked; key below)",
    [("1. E-governance means:  a) govt websites only  b) ✅ using ICT to deliver/run public services  c) buying computers  d) the internet","q"),
     ("2. Filing VAT on the IRD portal is:  a) G2C  b) ✅ G2B  c) G2G  d) G2E","q"),
     ("3. The process model order is:  a) output-input-process-feedback  b) ✅ input-process-output-feedback  c) process-input-output-feedback  d) input-output-feedback-process","q"),
     ("4. Citizen/PAN/vehicle registries live in the:  a) presentation layer  b) application layer  c) ✅ data layer  d) — none","q"),
     ("5. Nepal's e-gov maturity is reportedly around:  a) emerging  b) enhanced  c) ✅ transactional  d) connected","q"),
     ("6. The Digital Nepal Framework (2019) is:  a) a bank  b) a wallet  c) a law  d) ✅ a roadmap of ~80 initiatives / 8 sectors","q"),
     ("7. Nepal's payments regulator (licenses wallets, NepalPay QR) is:  a) NTA  b) ✅ NRB  c) Daraz  d) the ward office","q"),
     ("8. Nepal's key data-protection gap is:  a) too many laws  b) ✅ no dedicated Data Protection Act  c) no internet  d) no computers","q"),
     ("9. The digital divide is mainly about:  a) app colours  b) ✅ who is left out (rural/poor/old/etc.)  c) server brands  d) tax rates","q"),
     ("10. Nepal's reported LDC graduation ~2026 implies:  a) e-commerce ban  b) ✅ loss of some trade preferences  c) closing Daraz  d) wallet tariffs","q"),
     ("11. 'Great tool, broken access' best describes Nepali:  a) tourism  b) ✅ agriculture  c) banking apps  d) e-procurement","q"),
     ("12. SMEs are reported to be roughly:  a) 5% of firms  b) foreign-owned  c) all in Kathmandu  d) ✅ 90% of businesses / 50%+ of jobs","q"),
     ("ANSWER KEY:  1-b · 2-b · 3-b · 4-c · 5-c · 6-d · 7-b · 8-b · 9-b · 10-b · 11-b · 12-d","a")],
    "Consolidated quiz Section A. Correct-answer positions vary across b/c/d; key matches.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define e-governance + its 4 goals.   14. Name the G2C/G2B/G2G/G2E types with a Nepal example each.   15. Define digital financial inclusion + 2 benefits.","o"),
     ("16. State Nepal's data-protection gap.   17. What is the Digital Nepal Framework's purpose (and its 8 sectors)?","o"),
     ("Section C — Applied case (use the lecture characters)","q"),
     ("18. Sita in Humla / Kanchhi Maiya: identify the challenge she faces with a digital service and propose a concrete solution.","o"),
     ("19. Pick ONE sector (trade / tourism / agriculture / SMEs) and assess its digital win vs its gap using the scorecard.","o"),
     ("Section D — Discussion","q"),
     ("20. 'Can Nepal be a fully digital, cashless, e-governed society by 2035?' Argue using the scorecard, the data-protection gap, and the digital divide.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit6_material.md.",compact=True)

# ---- close: END OF UNIT 6 AND END OF THE COURSE ----
add_title("End of Unit 6 — and End of IT 250",
          "S42–S48 complete: e-governance concepts/goals · process, structure & maturity · Nepal practices & the policy stack · "
          "digital financial inclusion & its regulation · public-sector opportunities, challenges & the data-protection gap · "
          "trade, tourism, agriculture & SMEs — the 4-sector scorecard.  THE COURSE IS COMPLETE: Units 1–6 done.",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe, Nepal-localised · policy/figures flagged 'verify current status' / 'reported'. "
          "Verdict: real, uneven, foundation-limited progress — a cashless, e-governed 2035 is possible, not guaranteed.")

_add_page_numbers()
save("IT250_Unit6.pptx")
