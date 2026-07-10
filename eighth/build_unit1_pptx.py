#!/usr/bin/env python3
"""IT250 (eighth) Unit 1 deck — Introduction to the Digital Economy (S1–S8), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables — each
table on its OWN slide, paginated, never squeezed. Generous slide count by design. Self-contained
& PDF-safe. Imports eighth/deckkit.py. Diagrams in images/. Localised to Nepal's digital economy.
Source: syllabus (course.txt) + instructor lecture PDFs (mapped in Unit1_content_outline.md §0).
Run: python3 build_unit1_pptx.py -> IT250_Unit1.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 1 — Introduction to the Digital Economy",
          "IT 250: Digital Economy  ·  BIM 8th Semester  ·  Sessions S1–S8 (8 lecture hours)",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal-localised) — no abstraction without instances. Exports to PDF with no information lost.")

add_outcomes("Unit 1 — Learning Outcomes","introduction  ·  s1–s8",
    "By the end of this unit, you will be able to:",
    ["Define the digital economy, its drivers, and the four actors in its ecosystem (S1–S2)",
     "Define the knowledge (K-) economy, its features and drivers, and explicit vs tacit knowledge (S3–S4)",
     "Contrast the digital and knowledge economies and explain how they reinforce each other (S5)",
     "Explain the fourth industrial revolution — drivers, opportunities, challenges — on the revolution timeline (S6–S7)",
     "Analyse the digital economy's influence on sustainability, privacy, regulation, and strategy (S8)"],
    "This is Unit 1 of IT 250 — the foundation. It defines the two economies (digital & knowledge) and the 4IR that the rest of the course (platforms, digital markets, transformation, information economics, and Nepal's digitalization) builds on.")

add_roadmap("Unit 1 — Roadmap","Where each session fits (S1–S8)",
    ["S1  What the digital economy is (concepts & characteristics)",
     "S2  Its drivers & ecosystem (who makes it work)",
     "S3  The knowledge economy (workers, firms, know-how)",
     "S4  Drivers of the knowledge economy (+ Nepal challenges)",
     "S5  Digital vs knowledge economy (differences + how they connect)",
     "S6  The 4th industrial revolution (timeline & drivers)",
     "S7  4IR opportunities & challenges (+ Nepal SWOT)",
     "S8  Influence: sustainability · privacy · regulation · strategy"],
    ["Unit 2  Platforms, network effects, monopolies",
     "Unit 3  Digital markets, strategy & innovation",
     "Unit 4  Digital transformation & currencies",
     "Unit 5  Economics of information",
     "Unit 6  Digitalization — the Nepalese perspective"])

# ============================================================ S1
add_divider("Session 1 · Lecture hour 1 (of 8)","What Is the Digital Economy?",
    "Before breakfast today you probably checked Hamro Patro, paid a bill on eSewa, ordered from Foodmandu, and watched a clip on a data pack — five acts in the digital economy before you left the house. So what EXACTLY is this economy, and what makes it different from the shop-and-cash economy your grandparents knew?",
    "OPENING HOOK [~5 min]. Draw out how much daily life is already digital. Agenda: define the digital economy → its 5 core characteristics → how economies evolved into it.")

concept_understand("S1 · Concept 1 · [THEORY]","Defining the Digital Economy",
    "The digital economy is all economic activity that is enabled by — and dependent on — digital technologies: producing, buying, selling, and delivering value through the internet, software, data, and connected devices. Working definition: whenever technology creates value, facilitates a transaction, or delivers a service, that activity is part of the digital economy.",
    ["It is far wider than 'online shopping' — it includes payments, cloud, streaming, gig work, and platforms.",
     "The technology is not just a helper; it IS the activity (e.g. a ride-hailing app is the taxi business).",
     "Coined by Don Tapscott (1995); today it spans almost every sector, not a separate 'tech' corner.",
     "If you removed the internet and software, the activity would stop existing — that's the test."],
    None,"Digital economy = value created and exchanged THROUGH digital technology, not just online shops.",
    "~7 min. Anchor with eSewa/Daraz. Stress that the technology is constitutive, not decorative — take away the app and the service is gone.")
add_table_slide("S1 · Concept 1 · examples","Is it 'the digital economy'? — concrete cases",
    ["Activity","Digital economy?","Why"],
    [["Buying vegetables with cash at the local haat","No","No digital technology creates or mediates the value"],
     ["Paying the same vendor via a Fonepay QR","Yes","A digital payment rail carries the transaction"],
     ["A Daraz order shipped to Butwal","Yes","Platform, catalogue, payment, logistics are all digital"],
     ["A Kathmandu firm coding apps for a US client","Yes","Digitally-delivered service (IT export)"],
     ["Streaming a film on a NetTV / data pack","Yes","A digital good delivered over the network"],
     ["A Pathao rider giving you a lift","Yes","The app IS the business — matching, pricing, payment"],
     ["A farmer ploughing a field by hand","No","Value comes from land & labour, not digital tech"]],
    per_page=7,widths=[3.0,1.3,3.2],fs=11,
    note="The test: remove the digital technology — does the activity still exist? If it disappears (Pathao, Daraz, eSewa), it is the digital economy; if it continues (cash at the haat), it is not.")
concept_apply("S1 · Concept 1 · [THEORY]","Defining the Digital Economy",
    "eSewa is a clean example: it is not a bank branch with a website bolted on — the wallet, the QR, the merchant network, and the settlement all live in software. Remove the technology and there is no eSewa. That is what 'the technology IS the activity' means, and why the digital economy now reaches farmers, shopkeepers, and trekking guides, not only IT firms.",
    "\"The digital economy just means online shopping / e-commerce.\" E-commerce is one slice. The digital economy also includes digital payments, cloud services, streaming, gig/platform work, data-driven advertising, and IT exports — most of the modern economy touches it.",
    "The digital economy is all economic activity enabled by and dependent on digital technologies — creating, buying, selling, and delivering value via the internet, software, data, and connected devices. The technology is constitutive, not decorative: the working test is that removing it would end the activity. Coined by Tapscott (1995), it now spans nearly every sector, far beyond e-commerce.",
    "digital economy · enabled by / dependent on digital tech · technology IS the activity · Tapscott · beyond e-commerce")

concept_understand("S1 · Concept 2 · [THEORY]","The Five Core Characteristics",
    "Five features distinguish the digital economy from the traditional one: it is data-driven, automated, globally connected, platform-based, and highly scalable. The last one is the deepest: once a digital product is built, serving one more customer costs almost nothing (near-zero marginal cost) — the economics that lets a Nepali app reach millions.",
    ["Data-driven — 'data is the new oil': every click and transaction is a reusable asset.",
     "Automated — software does at scale what people once did by hand (matching, pricing, support).",
     "Globally connected — a Bhaktapur seller can reach a buyer in Berlin the same day.",
     "Platform-based & scalable — one more Netflix viewer costs ≈0; one more cinema seat does not.",
     "(Deeper platform economics — network effects, two-sided markets — come in Unit 2.)"],
    None,"Data-driven · automated · connected · platform-based · scalable (near-zero cost to serve one more).",
    "~8 min. Introduce scalability / near-zero marginal cost intuitively (Netflix vs a cinema seat); keep the formal mechanics for Unit 2. Data-as-oil sets up S8 privacy.")
add_table_slide("S1 · Concept 2 · scaffolding","The five characteristics — what each means, and why it matters",
    ["Characteristic","What it means","Nepal example","Why it matters"],
    [["Data-driven","Activity generates reusable data","Khalti sees spending patterns by district","Better targeting — and privacy questions (S8)"],
     ["Automated","Software replaces manual steps","Auto loan-scoring in a bank app","Speed and scale, fewer people per transaction"],
     ["Globally connected","Reaches beyond geography","A Thamel handicraft seller ships to Europe","Small players access world markets"],
     ["Platform-based","Value sits on shared platforms","Daraz hosts thousands of sellers","One platform, many businesses (Unit 2)"],
     ["Scalable","One more user costs ≈ nothing","Hamro Patro serving millions at low cost","Explosive growth possible from Nepal"]],
    per_page=5,widths=[1.5,2.3,2.6,2.4],fs=10.5,
    note="Scalability (near-zero marginal cost) is the economic engine: it is why a digital product built once in Kathmandu can serve millions with little extra cost — impossible for a physical shop.")
concept_apply("S1 · Concept 2 · [THEORY]","The Five Core Characteristics",
    "Hamro Patro shows all five at once: it runs on data (which notifications you open), automation (personalised feeds without staff), global reach (Nepalis abroad use it), a platform (news, calendar, ads, payments in one app), and scalability — going from one user to millions barely changes its cost per user. That mix is exactly what a traditional almanac-seller could never achieve.",
    "\"Digital just means the same business with a website.\" A website is not the point — the difference is structural: data as an asset, automation, global reach, platform leverage, and near-zero cost to serve one more user. These change what is economically possible, not just the sales channel.",
    "The digital economy has five core characteristics: it is data-driven (data is a reusable asset), automated (software replaces manual steps), globally connected (reach beyond geography), platform-based (value built on shared platforms), and highly scalable (near-zero marginal cost to serve one more user). Scalability is the economic engine that lets a product built once serve millions cheaply.",
    "data-driven · automation · global connectivity · platform-based · scalability · near-zero marginal cost")

concept_understand("S1 · Concept 3 · [THEORY]","How Economies Evolved Into the Digital Economy",
    "The digital economy is the latest stage of a long shift in where value comes from: from the traditional economy (land, labour, physical goods) to the information economy (computers and records) to the digital economy (platforms, networks, data, AI). Each stage did not erase the last — farms and factories remain — but the SOURCE of new value moved.",
    ["Traditional: value from land, labour, and trading physical goods (agriculture, manufacturing).",
     "Information: computers store and process records; value from managing information faster.",
     "Digital: value from connected platforms, data, and automation — networks, not just machines.",
     "Nepal is living all three at once: subsistence farming, a growing service sector, and eSewa/Daraz."],
    "s1_evolution.png","Traditional (land/labour) → Information (computers) → Digital (platforms/data/AI).",
    "~7 min. Point out Nepal spans all three stages simultaneously — a useful frame for the whole course.")
add_table_slide("S1 · Concept 3 · comparison","Three economies — where value comes from",
    ["","Traditional economy","Information economy","Digital economy"],
    [["Main resource","Land, labour, capital","Computers, records","Data, platforms, networks"],
     ["Value comes from","Producing/trading goods","Processing information","Connecting users & automating"],
     ["Typical work","Farming, manufacturing, trade","Office/clerical, data entry","Platform, coding, analytics, gig"],
     ["Nepal example","Subsistence farm, retail shop","Bank back-office, records","eSewa, Daraz, Pathao, IT export"],
     ["Reach","Local","Organisational","Global"]],
    per_page=5,widths=[1.5,2.4,2.2,2.6],fs=10.5,
    note="Later stages layer on top of earlier ones rather than replacing them — which is why a single country (Nepal) can have all three economies operating side by side.")
concept_apply("S1 · Concept 3 · [THEORY]","How Economies Evolved Into the Digital Economy",
    "Nepal is a living museum of all three economies: a farmer in Jumla is in the traditional economy, a bank clerk keying records is in the information economy, and a Kathmandu developer shipping code to a US client is in the digital economy — often within one family. Understanding the digital economy means seeing it as the newest layer, not a replacement for the others.",
    "\"The digital economy replaced the old economy.\" It layered on top of it. Agriculture and manufacturing still matter; what changed is that the fastest-growing new value now comes from data, platforms, and networks — so the layers coexist, especially in a developing economy.",
    "Economies evolved from traditional (value from land, labour, and physical goods) to information (value from processing records with computers) to digital (value from connected platforms, data, automation, and AI). Each stage layers on the previous rather than erasing it, which is why Nepal simultaneously contains subsistence farming, a clerical service sector, and platforms like eSewa and Daraz.",
    "traditional → information → digital · source of value shifts · layering not replacement · Nepal spans all three")

add_activity("S1 — 'Your digital-economy morning'  ·  ~5 min",
    ["Individually (1 min): list every digital-economy act you did in the last 24 hours.",
     "In pairs (2 min): for each, name which of the 5 characteristics it shows most.",
     "Take 4–5 answers aloud (2 min); tally the most common characteristic.",
     "Close: notice how much of ordinary daily life is now digital-economy activity."],
    "Seeds: eSewa/Khalti payment (data-driven, scalable), Foodmandu order (platform), YouTube/NetTV (scalable digital good), TikTok (data-driven), a freelance gig (global connectivity). Draw out that 'data-driven' underlies almost all of them.",
    "ACTIVITY [~5 min].")
add_quiz("S1 — Quick Check  ·  ~5 min",
    [("Q1.  The best test of whether something is 'the digital economy' is:","q"),
     ("a) it happens on a phone   b) ✅ remove the digital tech and the activity would stop existing   c) it is new   d) it is expensive","a"),
     ("     Why: the technology is constitutive — Pathao/eSewa vanish without it, while cash-at-the-haat continues.","o"),
     ("Q2.  'Near-zero marginal cost' means:","q"),
     ("a) the product is free   b) ✅ serving one more user costs almost nothing   c) there are no costs   d) it never makes profit","a"),
     ("     Why: the build cost is paid once; each extra user (one more stream, one more app install) adds little — the engine of scalability.","o"),
     ("Discussion: name a Nepali service that is the digital economy and one that is not — justify with the removal test.","o")],
    "QUIZ [~5 min]. Reinforce the removal test and the scalability idea (set up for Unit 2 platform economics).")
add_summary("S1 · Summary  ·  [~2 min]",
    ["Digital economy = value created and exchanged THROUGH digital tech; the tech IS the activity (beyond e-commerce).",
     "Five characteristics: data-driven, automated, globally connected, platform-based, scalable (near-zero marginal cost).",
     "It is the newest layer after the traditional and information economies — Nepal contains all three at once."],
    "You already live and transact in the digital economy daily; naming its characteristics lets you see why a Kathmandu startup can scale to millions, and why 'data' and 'platforms' will run through every later unit of this course.",
    "S2 — the drivers that power the digital economy, and the four actors whose ecosystem makes it work.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S2
add_divider("Session 2 · Lecture hour 2 (of 8)","Drivers & Ecosystem of the Digital Economy",
    "eSewa did not succeed because one clever app appeared. It needed cheap smartphones, 4G coverage, NRB rules that allowed wallets, merchants willing to display a QR, and millions of users ready to trust digital money. Behind every digital service is a whole cast of players. Who are they — and what pushes the whole system forward?",
    "OPENING HOOK [~5 min]. Draw out that no single company 'is' the digital economy. Agenda: the drivers (technological/social/business) → the 4-actor ecosystem → benefits vs challenges.")

concept_understand("S2 · Concept 1 · [THEORY]","What Drives the Digital Economy",
    "The digital economy is pushed forward by three kinds of drivers. Technological drivers (mobile, 4G/5G, cloud, AI, IoT) make it possible; social drivers (digital literacy, youth adoption, changing habits) make people use it; and business drivers (SMEs going online, startups, cost pressure) make firms build it. All three must move together — technology alone is not enough.",
    ["Technological — the five pillars: cloud, mobile, IoT, AI, and digital platforms.",
     "Social — a young, connected population that trusts and adopts digital services.",
     "Business — firms chase reach, lower costs, and new revenue by going digital.",
     "Bottleneck logic: the weakest driver caps growth (great apps + no rural internet = stalled)."],
    None,"Three drivers: technological (possible) · social (adopted) · business (built) — all three must move.",
    "~7 min. Stress the bottleneck idea: Nepal often has the tech and the youth but lags on connectivity/policy — the slowest driver sets the pace.")
add_table_slide("S2 · Concept 1 · scaffolding","The drivers — three forces, with Nepal examples",
    ["Driver type","Key elements","Nepal example","If it is weak…"],
    [["Technological","Mobile, 4G/5G, cloud, AI, IoT, platforms","Ncell/Ntc data, cloud-hosted apps","No infrastructure → no service"],
     ["Social","Digital literacy, youth, trust, habits","Young users adopting wallets fast","No adoption → apps sit empty"],
     ["Business","SMEs online, startups, cost pressure","Shops joining Daraz; fintech startups","No supply → nothing to use"],
     ["(Economic)","Globalization, productivity, data value","IT export earnings, forex","No incentive → slow investment"]],
    per_page=4,widths=[1.5,2.6,2.6,2.3],fs=10.5,
    note="The five technological PILLARS (cloud, mobile, IoT, AI, platforms) sit inside the technological driver. Growth is capped by the weakest driver — often connectivity or policy in Nepal.")
concept_apply("S2 · Concept 1 · [THEORY]","What Drives the Digital Economy",
    "Digital wallets took off in Nepal only when all three drivers aligned: cheap smartphones and 4G (technological), a young population willing to try them (social), and merchants plus NRB rules making them useful and legal (business/regulatory). Where one driver lagged — rural areas with weak internet — adoption stalled regardless of how good the app was.",
    "\"Better technology automatically means a bigger digital economy.\" Technology is necessary but not sufficient. Without digital literacy and trust (social) and firms building services (business), the technology sits unused. Growth is set by the slowest of the three drivers, not the fastest.",
    "The digital economy is driven by technological forces (mobile, 4G/5G, cloud, AI, IoT — the five pillars), social forces (digital literacy, youth adoption, trust, changing habits), and business forces (SMEs going online, startups, cost pressure), often alongside economic forces (globalization, data value). All must advance together; the weakest driver — frequently connectivity or policy in Nepal — caps overall growth.",
    "technological / social / business drivers · five tech pillars · bottleneck: weakest driver caps growth")

concept_understand("S2 · Concept 2 · [THEORY]","The Digital-Economy Ecosystem — four actors",
    "The digital economy is a web of four actors: consumers (users with phones and wallets), businesses/platforms (who build and sell), government/regulators (who set the rules — NRB, Ministry of Communication), and technology providers (ISPs, mobile networks, cloud). Value and data flow both ways between all four; remove any one and the system stalls.",
    ["Consumers — provide demand, money, and data (the fuel).",
     "Businesses/platforms — build services and capture value (Daraz, eSewa, Pathao).",
     "Government/regulators — licence, protect, and tax; enable trust (NRB wallet rules).",
     "Technology providers — the pipes and power: ISPs, Ntc/Ncell, cloud, data centres."],
    "s2_ecosystem.png","Four actors — consumers · businesses/platforms · regulators · tech providers — one web.",
    "~8 min. Use the diagram; have students place eSewa's players in each role. Stress two-way flows (data goes back to businesses).")
add_table_slide("S2 · Concept 2 · scaffolding","The four ecosystem actors — role & what they contribute",
    ["Actor","Role","Nepal example","What they contribute"],
    [["Consumers","Use and pay for services","Anyone with a wallet/app","Demand, money, and data"],
     ["Businesses / platforms","Build and sell digital services","Daraz, eSewa, Pathao, Foodmandu","Products, jobs, innovation"],
     ["Government / regulators","Set rules, licence, protect, tax","NRB, Ministry of Communication","Trust, legality, consumer protection"],
     ["Technology providers","Provide infrastructure","Ntc, Ncell, ISPs, cloud hosts","Connectivity, computing, the 'pipes'"]],
    per_page=4,widths=[1.9,2.2,2.4,2.5],fs=10.5,
    note="It is an interdependent ecosystem, not a hierarchy: businesses need regulators' trust and providers' pipes and consumers' data — the value flows in every direction.")
concept_apply("S2 · Concept 2 · [THEORY]","The Digital-Economy Ecosystem",
    "Trace one Fonepay QR payment: the consumer scans (demand + data), the merchant and eSewa/Fonepay move the money (business/platform), NRB's interoperability rules let any wallet pay any QR (regulator), and Ntc/Ncell carry the data (tech provider). All four are load-bearing — if NRB had not mandated QR interoperability, the payment would fail even with a perfect app and a willing user.",
    "\"The digital economy is just the tech companies.\" Regulators, telecom/ISPs, and ordinary consumers are equally load-bearing. A brilliant platform with no enabling regulation, no network coverage, or no willing users does not function — the ecosystem, not one actor, produces the value.",
    "The digital-economy ecosystem has four interdependent actors: consumers (demand, money, data), businesses/platforms (build and sell services), government/regulators (rules, licensing, protection, tax — e.g. NRB), and technology providers (connectivity and computing — ISPs, mobile networks, cloud). Value and data flow in all directions; removing any one actor stalls the system.",
    "ecosystem · consumers · businesses/platforms · regulators (NRB) · technology providers · interdependence")

concept_understand("S2 · Concept 3 · [THEORY]","Benefits and Challenges — two sides of the coin",
    "The digital economy brings clear benefits — wider reach, faster transactions, new jobs, and data-driven decisions — but each comes with a matching challenge: privacy risk, regulatory compliance, cybersecurity threats, and sustainability (e-waste, energy). Understanding both sides is honest analysis, and it previews the 'influence' discussion that closes the unit (S8).",
    ["Benefits: markets widen, transactions speed up, new kinds of jobs appear, decisions use real data.",
     "Challenges: more data collected → privacy risk; new services → compliance and cybersecurity load.",
     "Sustainability cuts both ways: less paper, but more e-waste and energy use.",
     "The point is not 'good or bad' but 'what do we gain, what do we risk, and how do we manage it?'"],
    None,"Every benefit (reach, speed, jobs, data) has a matching challenge (privacy, compliance, security, e-waste).",
    "~6 min. Keep it as a preview — S8 goes deep. Set the both-sides framing that recurs all unit.")
add_table_slide("S2 · Concept 3 · comparison","Benefits vs challenges of the digital economy",
    ["Benefit","Matching challenge"],
    [["Wider market reach (sell nationwide/abroad)","Intense competition; small players squeezed by platforms"],
     ["Faster, cheaper transactions","Cybersecurity threats (fraud, hacking, scams)"],
     ["New jobs & industries (IT, gig, fintech)","Job displacement; gig workers lack protection"],
     ["Data-driven decisions & personalization","Privacy risk — tracking, consent gaps, misuse"],
     ["Convenient digital public services","Regulatory compliance load; law lags technology"],
     ["Less paper, remote work (greener)","E-waste and data-centre energy (sustainability)"]],
    per_page=6,widths=[1,1.1],fs=11,
    note="Each row is a trade-off, not a free lunch. S8 returns to these as the 'influence' of the digital economy — sustainability, privacy, regulation, and strategy.")
concept_apply("S2 · Concept 3 · [THEORY]","Benefits and Challenges",
    "Digital lending apps in Nepal show both sides at once: they widen access to credit (benefit) but also enable data misuse and aggressive collection when regulation lags (challenge). The same data that lets a lender approve a loan in minutes can be abused if there is no data-protection law — which is exactly why S8 and Unit 6 look at regulation.",
    "\"The digital economy is simply good (or simply dangerous).\" It is a set of trade-offs. Maturity is naming both the benefit and its matching challenge for any digital service, then asking how the challenge is managed — not cheering or fearing the technology wholesale.",
    "The digital economy delivers benefits — wider market reach, faster and cheaper transactions, new jobs and industries, and data-driven decisions — each paired with a challenge: intense competition, cybersecurity threats, job displacement and weak gig protections, privacy risk, compliance load, and sustainability (e-waste, energy). Honest analysis names both sides and asks how each risk is managed (developed further in S8).",
    "benefits vs challenges · reach/speed/jobs/data · privacy · cybersecurity · compliance · sustainability · trade-offs")

add_activity("S2 — 'Map the ecosystem'  ·  ~5 min",
    ["In pairs (2 min): pick a Nepali digital service (Pathao, Daraz, eSewa, Foodmandu).",
     "List one concrete player it depends on in EACH of the 4 actor roles.",
     "Name one benefit it delivers and the matching challenge it creates.",
     "Take 3 answers aloud (3 min); check that all four roles were filled."],
    "Good answer for Pathao: consumers (riders/passengers), business (Pathao), regulator (govt transport/NRB for payments), tech provider (Ntc/Ncell, cloud). Benefit: income for riders + convenience; challenge: rider safety/protection, surge pricing, data privacy.",
    "ACTIVITY [~5 min].")
add_quiz("S2 — Quick Check  ·  ~5 min",
    [("Q1.  In the digital-economy ecosystem, NRB is best classified as a:","q"),
     ("a) technology provider   b) consumer   c) ✅ government/regulator   d) platform","a"),
     ("     Why: NRB sets and enforces the rules (wallet licensing, KYC, QR interoperability) — the regulator role.","o"),
     ("Q2.  4G mobile coverage is which kind of driver?","q"),
     ("a) social   b) ✅ technological   c) business   d) legal","a"),
     ("     Why: connectivity infrastructure is a technological driver (one of the five pillars); adoption of it is social.","o"),
     ("Discussion: pick a Nepali app and name a real player in each of the four ecosystem roles.","o")],
    "QUIZ [~5 min]. Make sure students separate the technological driver (the pipe) from the social driver (adoption of it).")
add_summary("S2 · Summary  ·  [~2 min]",
    ["Three drivers push the digital economy: technological (possible), social (adopted), business (built) — the weakest caps growth.",
     "Four ecosystem actors: consumers, businesses/platforms, regulators (NRB), tech providers — interdependent, value flows both ways.",
     "Every benefit (reach, speed, jobs, data) carries a matching challenge (privacy, security, compliance, e-waste)."],
    "When you build or manage a digital service, you must line up all three drivers and every ecosystem actor — a great app with no regulation, network, or users fails. This systems view is what separates a real business plan from a demo.",
    "S3 — the OTHER economy of the modern era: the knowledge economy, where value lives in people's heads.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S3
add_divider("Session 3 · Lecture hour 3 (of 8)","The Knowledge (K-) Economy",
    "Deerwalk and Fusemachines do not sell a physical product you can hold — they sell what is inside their people's heads: analysis, code, models, ideas. A country with few natural resources can still get rich this way. So how does an economy run on KNOWLEDGE, and how is that different from running on land or machines?",
    "OPENING HOOK [~5 min]. Contrast a factory (machines make value) with an IT firm (minds make value). Agenda: define the K-economy → knowledge workers & companies → knowledge management (explicit vs tacit).")

concept_understand("S3 · Concept 1 · [THEORY]","Defining the Knowledge Economy",
    "The knowledge economy (K-economy) is an economy where the main source of value is knowledge, skills, and innovation rather than physical resources or manual labour. Its raw material is human capital and ideas; its outputs are research, designs, software, and intellectual property. Where the industrial economy ran on machines, the knowledge economy runs on educated minds.",
    ["The evolution: traditional → industrial → service → knowledge economy (labour → machines → skills → ideas).",
     "Five features: human capital, R&D/innovation, information flow, digital infrastructure, collaboration.",
     "Value is intangible: a patent, an algorithm, or a design can be worth more than a factory.",
     "World Bank framing: education, innovation, ICT, and institutions are its pillars."],
    None,"K-economy = value from knowledge, skills & innovation (minds), not land or machines.",
    "~7 min. Anchor with a Nepali IT-outsourcing firm: no factory, high value. Note it overlaps with the digital economy (S5 makes the distinction sharp).")
add_table_slide("S3 · Concept 1 · scaffolding","The five features of a knowledge economy",
    ["Feature","What it means","Nepal example"],
    [["Human capital","Educated, skilled people are the key asset","IT graduates, engineers, doctors, designers"],
     ["Innovation & R&D","New ideas and research create value","Fusemachines' AI work; product startups"],
     ["Information flow","Knowledge moves and is shared freely","Open-source communities, tech meetups"],
     ["Digital infrastructure","Tools to create & share knowledge","Cloud, internet, collaboration software"],
     ["Collaboration & networks","Value grows through connection","University–industry links, dev communities"]],
    per_page=5,widths=[1.9,3.0,2.6],fs=11,
    note="Notice how much depends on people and their connections rather than physical plant — a knowledge economy can grow with little land or heavy machinery, but not without education.")
concept_apply("S3 · Concept 1 · [THEORY]","Defining the Knowledge Economy",
    "Fusemachines and Deerwalk earn foreign exchange for Nepal without any factory: their assets walk out of the office every evening in their employees' heads. That is a knowledge economy in miniature — value from skills, research, and IP. It is also why education and stopping brain drain matter so much for Nepal's growth (developed in S4).",
    "\"The knowledge economy is just the IT/tech sector.\" Knowledge workers include doctors, engineers, architects, researchers, designers, lawyers, and educators — anyone whose main output is expertise. IT is the most visible slice, not the whole thing.",
    "The knowledge economy is one where value comes mainly from knowledge, skills, and innovation rather than physical resources or manual labour: its raw material is human capital and ideas, and its outputs are research, designs, software, and intellectual property. It has five features — human capital, R&D/innovation, information flow, digital infrastructure, and collaboration — and, per the World Bank, rests on education, innovation, ICT, and institutions.",
    "knowledge economy · human capital · innovation & R&D · intellectual property · beyond the IT sector")

concept_understand("S3 · Concept 2 · [THEORY]","Knowledge Workers & Knowledge Companies",
    "A knowledge worker is someone whose main job is to create, analyse, and apply knowledge — developers, data analysts, engineers, designers, educators, researchers. A knowledge company is a firm whose primary resource is knowledge, marked by a learning culture, high R&D, flexible teams, strong digital tools, and rapid innovation. Its balance sheet hides its real asset: people.",
    ["Knowledge workers rely on 7 skills: critical thinking, creativity, digital literacy, problem-solving, communication, collaboration, continuous learning.",
     "Knowledge companies invest in R&D and learning, not just plant and inventory.",
     "The core asset (talent) is mobile — it can resign — so retention and culture are strategic.",
     "Nepal examples: Leapfrog, CloudFactory, Genese, Yarsa Games, bank/telecom analytics teams."],
    None,"Knowledge worker = creates/applies knowledge; knowledge company = knowledge is its main resource.",
    "~7 min. Point out the risk: the main asset goes home each night and can leave — motivating the knowledge-management concept next.")
add_table_slide("S3 · Concept 2 · examples","Knowledge worker vs manual worker — a concrete contrast",
    ["Dimension","Knowledge worker","Manual worker"],
    [["Main input","Education, expertise, judgement","Physical effort, routine skill"],
     ["Main output","Analysis, code, designs, decisions","Goods produced, tasks completed"],
     ["Key tool","Mind + digital tools","Hands + machines/tools"],
     ["How value scales","Ideas reused infinitely (an app, a design)","Output tied to hours & physical limits"],
     ["Nepal example","Developer at Leapfrog; bank data analyst","Factory line worker; construction labour"],
     ["If they leave","Tacit knowledge walks out the door","Replaceable with similar training"]],
    per_page=6,widths=[1.7,2.7,2.6],fs=11,
    note="Both are valuable and dignified; the difference is the SOURCE of value (expertise vs effort) and how it scales. The knowledge worker's output can be copied and reused at near-zero cost — echoing S1's scalability.")
concept_apply("S3 · Concept 2 · [THEORY]","Knowledge Workers & Knowledge Companies",
    "A CloudFactory or Leapfrog team has almost no physical assets worth naming — its value is the skill, judgement, and accumulated experience of its people. That makes culture, learning, and retention strategic, not 'HR nice-to-haves': lose a senior engineer and you lose knowledge that was never written down. This is why knowledge companies fight brain drain so hard.",
    "\"A company's value is its buildings and equipment.\" For a knowledge company the real asset is its people and their expertise — which does not appear on the balance sheet and can resign at any time. Managing and retaining that knowledge is the central challenge (leads into knowledge management).",
    "A knowledge worker's main job is to create, analyse, and apply knowledge (developers, analysts, engineers, designers, educators, researchers), relying on skills like critical thinking, creativity, and continuous learning. A knowledge company is one whose primary resource is knowledge — marked by a learning culture, high R&D, flexible teams, strong digital tools, and rapid innovation. Its core asset is mobile talent, making culture and retention strategic.",
    "knowledge worker · knowledge company · human capital as core asset · learning culture · R&D · retention")

concept_understand("S3 · Concept 3 · [THEORY]","Knowledge Management: Explicit vs Tacit",
    "Knowledge management is capturing, organising, and sharing an organisation's knowledge so it is not lost and can be reused. The key distinction is explicit knowledge — written down and easy to share (manuals, documents, code, procedures) — versus tacit knowledge — living in people's heads as experience and intuition (handling a difficult customer, sensing a bug). Tacit knowledge is the larger, harder-to-capture part.",
    ["Explicit: recorded and transferable — a written SOP, a wiki, documented code.",
     "Tacit: personal know-how — skill, judgement, intuition; hard to write down (like riding a bike).",
     "KM tries to turn tacit into explicit (documentation, mentoring) before an expert leaves.",
     "Why it matters: prevents knowledge loss, avoids repeated mistakes, speeds up innovation."],
    "s3_iceberg.png","Explicit = written & shareable (tip); tacit = in-the-head know-how (the hidden bulk).",
    "~8 min. Use the iceberg image. Nepal example: a bank's written AML manual (explicit) vs a veteran officer's fraud instinct (tacit).")
add_table_slide("S3 · Concept 3 · comparison","Explicit vs tacit knowledge — and why the difference matters",
    ["Question","Explicit knowledge","Tacit knowledge"],
    [["What is it?","Written, recorded, codified","Personal experience, intuition, skill"],
     ["Examples","Manuals, SOPs, documents, code, reports","Handling an angry customer; sensing a risk"],
     ["How stored","Files, wikis, databases","In people's heads"],
     ["Easy to share?","Yes — copy and send","Hard — needs mentoring, practice, time"],
     ["Nepal example","A bank's written AML/KYC manual","A veteran officer's instinct for fraud"],
     ["Risk if the person leaves","Low — it is documented","High — it walks out the door"]],
    per_page=6,widths=[1.8,2.6,2.7],fs=10.5,
    note="Most valuable organisational knowledge is TACIT — which is why documentation, mentoring, and pairing (turning tacit into explicit) are core knowledge-management activities, especially where staff turnover and brain drain are high.")
concept_apply("S3 · Concept 3 · [THEORY]","Knowledge Management: Explicit vs Tacit",
    "When a senior developer leaves a Kathmandu software house, the documented code and manuals (explicit) stay — but the undocumented reasons behind design choices and the feel for which modules are fragile (tacit) leave with them. Firms that survive this practise knowledge management: code reviews, documentation, pairing, and mentoring turn tacit know-how into explicit records before it is lost.",
    "\"If it's not written down, it isn't real knowledge.\" The opposite — the most valuable knowledge is often tacit (experience, judgement) and precisely the hardest to capture. The whole point of knowledge management is to convert as much tacit knowledge as possible into explicit form before the expert leaves.",
    "Knowledge management is capturing, organising, and sharing an organisation's knowledge so it is preserved and reused. It rests on the distinction between explicit knowledge (written, recorded, easy to share — manuals, code, SOPs) and tacit knowledge (personal experience, intuition, skill — hard to codify). Since the most valuable knowledge is often tacit, KM focuses on converting it to explicit form (documentation, mentoring) to prevent loss.",
    "knowledge management · explicit (codified) · tacit (in-the-head) · convert tacit→explicit · prevent knowledge loss")

add_activity("S3 — 'Explicit or tacit?'  ·  ~5 min",
    ["Individually (1 min): list two things you know how to do well.",
     "In pairs (2 min): classify each as mostly explicit (you could write instructions) or mostly tacit (you'd have to show them).",
     "Take 4 answers aloud (2 min).",
     "Close: notice how hard the tacit ones are to write down — that is the KM challenge in one exercise."],
    "Seeds: 'solving a quadratic' (explicit) vs 'knowing when a customer is about to leave' or 'debugging by feel' (tacit). Draw out that expertise is mostly tacit, which is why mentoring and documentation matter.",
    "ACTIVITY [~5 min].")
add_quiz("S3 — Quick Check  ·  ~5 min",
    [("Q1.  A bank's written KYC procedure manual is an example of:","q"),
     ("a) ✅ explicit knowledge   b) tacit knowledge   c) a physical asset   d) manual labour","a"),
     ("     Why: it is codified and easy to copy and share — the definition of explicit knowledge.","o"),
     ("Q2.  The MAIN asset of a knowledge company is:","q"),
     ("a) its buildings   b) its inventory   c) ✅ its people and their expertise   d) its machinery","a"),
     ("     Why: value comes from human capital and know-how, which is mobile — hence culture and retention matter.","o"),
     ("Discussion: name one piece of tacit knowledge in a job you know — how would a firm avoid losing it?","o")],
    "QUIZ [~5 min]. Reinforce that tacit knowledge is the bigger, riskier part and the reason KM exists.")
add_summary("S3 · Summary  ·  [~2 min]",
    ["K-economy = value from knowledge, skills & innovation (human capital, IP) — minds, not land or machines.",
     "Knowledge workers create/apply knowledge; knowledge companies treat people as the core (mobile) asset.",
     "Knowledge management captures & shares knowledge; explicit (written) vs tacit (in-the-head) — tacit is the risk."],
    "As future knowledge workers, YOUR value is your expertise — and as future managers, retaining and documenting your team's tacit knowledge will decide whether your organisation survives turnover and brain drain.",
    "S4 — what makes a knowledge economy grow or stall: its drivers, and Nepal's specific challenges.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S4
add_divider("Session 4 · Lecture hour 4 (of 8)","Drivers of the Knowledge Economy",
    "In 1960 South Korea was poorer than many countries and had few natural resources; today it is a technology giant. Nepal produces skilled IT graduates — and then watches many of them leave. Same raw material (educated people), very different outcomes. What actually makes a knowledge economy grow, and what makes it stall?",
    "OPENING HOOK [~5 min]. Set up the puzzle: education alone is not enough. Agenda: the six drivers → benefits → Nepal's challenges (esp. brain drain).")

concept_understand("S4 · Concept 1 · [THEORY]","The Six Drivers of the Knowledge Economy",
    "A knowledge economy grows on six connected drivers: human-capital development (education & skills), technology & digital infrastructure, innovation & R&D, knowledge workers, knowledge companies, and R&D-backed intellectual property. They form a loop — education produces workers, workers build companies, companies invest in R&D and IP, which funds more education. Break one link and the loop weakens.",
    ["Human capital — schools, universities, and continuous training produce the talent.",
     "Infrastructure — internet, cloud, and tools let knowledge be created and shared.",
     "Innovation & R&D + IP — new ideas are generated AND protected so they pay off.",
     "Workers + companies — the talent and the firms that employ and organise it."],
    None,"Six drivers form a loop: education → workers → companies → R&D/IP → funds more education.",
    "~7 min. Emphasise the loop: a missing link (e.g. no jobs for graduates, or no IP protection) leaks talent out — setting up brain drain.")
add_table_slide("S4 · Concept 1 · scaffolding","The six drivers — and where Nepal stands",
    ["Driver","What it does","Nepal status"],
    [["Human-capital development","Educates and trains the talent","Strong output, but quality & relevance gaps"],
     ["Technology & infrastructure","Enables creating/sharing knowledge","Improving, but rural/power gaps remain"],
     ["Innovation & R&D","Generates new ideas & products","Weak — low R&D spending"],
     ["Knowledge workers","Supply the expertise","Plentiful — but many emigrate"],
     ["Knowledge companies","Employ and organise talent","Growing IT/BPO sector; needs scale"],
     ["R&D + intellectual property","Protects ideas so they pay off","Weak IP enforcement; policy gaps"]],
    per_page=6,widths=[2.0,2.6,2.6],fs=10.5,
    note="Nepal is strong on producing people but weak on R&D, IP protection, and absorbing talent into good jobs — so the loop leaks. Fixing the weak links, not producing more graduates, is the constraint.")
concept_apply("S4 · Concept 1 · [THEORY]","The Six Drivers of the Knowledge Economy",
    "Nepal produces plenty of the first driver (educated people) but is weak on R&D, IP protection, and high-value jobs to absorb them. So the loop leaks: talent trained here is captured by economies with stronger links (better pay, R&D, IP). South Korea closed those links — heavy R&D, strong institutions — and kept the loop turning at home.",
    "\"Producing more graduates automatically builds a knowledge economy.\" Graduates are one driver of six. Without R&D funding, IP protection, and jobs that use their skills, the talent simply emigrates — you have paid to educate another country's workforce. The binding constraint is the weakest driver, not the supply of graduates.",
    "A knowledge economy grows on six connected drivers: human-capital development (education/skills), technology & digital infrastructure, innovation & R&D, knowledge workers, knowledge companies, and R&D-backed intellectual property. They form a reinforcing loop — education produces workers who build companies whose R&D and IP fund more education. Nepal is strong on producing talent but weak on R&D, IP, and absorption, so the loop leaks.",
    "six drivers · human capital · infrastructure · R&D · IP · workers · companies · reinforcing loop · weakest link")

concept_understand("S4 · Concept 2 · [THEORY] [EXAMPLE]","Benefits & Challenges — the Nepal case",
    "A working knowledge economy brings higher productivity, innovation-driven growth, high-value jobs, and a stronger education ecosystem. But building one in Nepal faces sharp challenges: skill gaps between graduates and industry needs, low R&D investment, infrastructure and power gaps, weak policy/IP, and above all brain drain — the emigration of the very talent the economy is built on.",
    ["Benefits: better pay, exportable services (forex), resilient growth not tied to commodities.",
     "Challenge — skill gap: degrees do not always match what employers actually need.",
     "Challenge — brain drain: trained talent leaves for better pay and opportunity abroad.",
     "Challenge — thin R&D & weak IP: little incentive to innovate at home."],
    None,"Benefits: productivity, high-value jobs, forex. Challenges: skill gap, brain drain, thin R&D, weak IP.",
    "~8 min. Brain drain is the emotional core for a Nepali class — make it concrete (classmates abroad). Frame it as a systems failure (weak links), not individual choice.")
add_table_slide("S4 · Concept 2 · comparison","Knowledge economy in Nepal — benefits vs challenges (with consequences)",
    ["Benefit","Challenge","Consequence if unaddressed"],
    [["High-value, well-paid jobs","Skill gap: degrees ≠ industry needs","Graduates underemployed or retrained abroad"],
     ["Exportable services earn forex","Brain drain — talent emigrates","Nepal subsidises other economies' workforces"],
     ["Innovation-driven growth","Low R&D investment","Few new products; dependence on outsourcing"],
     ["Stronger education ecosystem","Infrastructure & power gaps","Uneven access; rural talent left out"],
     ["Ideas can be protected & monetised","Weak IP enforcement, policy gaps","Little incentive to innovate at home"],
     ["Resilience (not commodity-tied)","Small domestic market","Firms depend on foreign clients"]],
    per_page=6,widths=[2.1,2.3,2.7],fs=10.5,
    note="The challenges are linked: weak R&D + weak IP + few high-value jobs → brain drain. Addressing them together (not just 'more education') is what turns the loop from leaking to reinforcing.")
concept_apply("S4 · Concept 2 · [THEORY] [EXAMPLE]","Benefits & Challenges — the Nepal case",
    "Brain drain is Nepal's clearest knowledge-economy challenge: the country pays to educate a developer or doctor, then loses them to an economy that offers better pay, R&D, and IP protection. It is not mainly a failure of individuals — it is a failure of the other five drivers to give talent a reason to stay. Fixing pay, R&D, and jobs retains talent; lecturing about loyalty does not.",
    "\"Brain drain happens because people are unpatriotic.\" It happens because the surrounding drivers are weak — low pay, thin R&D, few high-value jobs, weak IP. Talent responds rationally to incentives. The policy answer is to strengthen the weak drivers so staying is worthwhile, not to blame those who leave.",
    "A functioning knowledge economy brings higher productivity, innovation-driven growth, high-value well-paid jobs, forex from exportable services, and a stronger education ecosystem. Building one in Nepal faces linked challenges — skill gaps, low R&D investment, infrastructure and power gaps, weak policy/IP, and brain drain (emigration of trained talent). Because the challenges reinforce each other, they must be addressed together, not by producing more graduates alone.",
    "benefits: productivity, forex, high-value jobs · challenges: skill gap, brain drain, low R&D, weak IP · systemic, linked")

add_activity("S4 — 'Keep the talent'  ·  ~5 min",
    ["In pairs (3 min): design ONE realistic policy or company practice that would make a skilled Nepali choose to stay.",
     "It must strengthen at least one of the six drivers — say which.",
     "Take 3–4 answers aloud (2 min); map each to the driver it fixes.",
     "Close: notice the best answers fix pay/R&D/jobs (incentives), not 'patriotism'."],
    "Strong answers: R&D tax credits or grants; competitive salaries via IT-export incentives; university–industry internships closing the skill gap; enforceable IP so founders profit at home; remote-work hubs so talent earns global pay from Nepal.",
    "ACTIVITY [~5 min].")
add_quiz("S4 — Quick Check  ·  ~5 min",
    [("Q1.  Brain drain is best understood as:","q"),
     ("a) a benefit   b) ✅ a challenge caused by weak surrounding drivers (pay, R&D, jobs, IP)   c) unpatriotic behaviour   d) a technology gap","a"),
     ("     Why: talent leaves when the other drivers are too weak to reward staying — a systems failure, not a character flaw.","o"),
     ("Q2.  Which driver PROTECTS ideas so innovators profit from them?","q"),
     ("a) human capital   b) infrastructure   c) ✅ R&D + intellectual property   d) collaboration","a"),
     ("     Why: IP protection lets creators capture the value of their ideas, giving a reason to innovate at home.","o"),
     ("Discussion: which single driver, if fixed, would most help Nepal retain talent — and why?","o")],
    "QUIZ [~5 min]. Push students to argue from the six-driver loop, not slogans.")
add_summary("S4 · Summary  ·  [~2 min]",
    ["Six drivers form a reinforcing loop: human capital → workers → companies → R&D/IP → funds more education.",
     "Benefits: productivity, innovation-driven growth, high-value jobs, forex — resilience beyond commodities.",
     "Nepal's challenges (skill gap, low R&D, weak IP, brain drain) are linked — fix the weak links, not just supply."],
    "Your career sits inside these drivers: whether you can build a high-value career in Nepal depends on R&D, IP, and jobs — and as a future leader you may help fix the weak links that currently drive talent away.",
    "S5 — the two economies side by side: how digital and knowledge differ, and how they power each other.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S5
add_divider("Session 5 · Lecture hour 5 (of 8)","Digital Economy vs Knowledge Economy",
    "eSewa is the DIGITAL economy. The programmers who built eSewa are the KNOWLEDGE economy. Same story, two lenses. Students constantly mix these up — so where exactly is the line, and why does the course treat them as two ideas rather than one?",
    "OPENING HOOK [~5 min]. Put both terms on the board and ask 'same or different?' Agenda: the contrast (dimension by dimension) → how they reinforce each other → the WHAT/HOW/NEXT hook.")

concept_understand("S5 · Concept 1 · [THEORY]","The Contrast, Dimension by Dimension",
    "The digital and knowledge economies overlap but are not the same. The digital economy is about the TOOLS and infrastructure — platforms, data, automation — and value from digital transactions at scale. The knowledge economy is about the MINDS — skills, ideas, research — and value from expertise. One is the plumbing; the other is the thinking that designs and uses it.",
    ["Core focus: digital = technology & platforms; knowledge = skills, ideas & innovation.",
     "Value driver: digital = automation & scale; knowledge = problem-solving & research.",
     "Key resource: digital = cloud, apps, data; knowledge = human capital, education.",
     "Output: digital = e-commerce, payments, streaming; knowledge = patents, research, designs."],
    None,"Digital economy = the tools & platforms (HOW); knowledge economy = the minds & ideas (WHAT).",
    "~7 min. Use the master comparison table next. Keep it crisp: same activity can be seen through both lenses (eSewa the platform vs the team that built it).")
add_table_slide("S5 · Concept 1 · comparison","Digital economy vs knowledge economy — the master comparison",
    ["Dimension","Digital economy","Knowledge economy"],
    [["Core focus","Technology, data, digital platforms","Skills, expertise, creativity, innovation"],
     ["What drives value","Automation, online transactions, scale","Ideas, problem-solving, research outputs"],
     ["Key resources","Cloud, mobile apps, big data, AI","Human capital, education, experience"],
     ["Type of work","Operating tools, coding, analytics, content","Designing solutions, research, strategy"],
     ["Economic output","E-commerce, digital payments, streaming","Consulting, research, patents, innovation"],
     ["Nepal examples","eSewa, Khalti, Pathao, Daraz, online banking","IT services (Fusemachines, Deerwalk), engineers, designers"],
     ["Why students confuse them","Both use technology heavily…","…but one is the tool, the other is the thinking"]],
    per_page=7,widths=[1.7,2.7,2.7],fs=10.5,
    note="The last row is the exam trap: both rely on technology, so they look identical. The distinction is the SOURCE of value — digital infrastructure/scale vs human expertise/ideas.")
concept_apply("S5 · Concept 1 · [THEORY]","The Contrast, Dimension by Dimension",
    "eSewa itself is a digital-economy product (a platform moving transactions at scale). The team of engineers, designers, and analysts who conceived and built eSewa are the knowledge economy at work (expertise, problem-solving, IP). Same company, two lenses: the digital lens sees the running platform; the knowledge lens sees the minds that created and improve it.",
    "\"Digital economy and knowledge economy are just two names for the same thing.\" They overlap but differ in the SOURCE of value: digital = infrastructure, platforms, and scale; knowledge = human expertise, ideas, and innovation. Both use technology heavily, which is exactly why they are so easy to confuse.",
    "The digital and knowledge economies overlap but differ by the source of value. The digital economy centres on technology, data, and platforms, with value from automation and transactions at scale (e-commerce, payments, streaming). The knowledge economy centres on skills, ideas, and innovation, with value from expertise and research (consulting, patents, designs). Both rely on technology — the reason they are so often confused — but one is the tool and the other is the thinking.",
    "digital vs knowledge · tools/scale vs minds/ideas · source of value · confusable but distinct")

concept_understand("S5 · Concept 2 · [THEORY]","How the Two Economies Reinforce Each Other",
    "The digital and knowledge economies are not rivals — they power each other in a cycle. Knowledge workers design and build the digital platforms; those platforms generate huge amounts of data; that data feeds better analysis, models, and decisions (more knowledge work); which produces better platforms. A useful memory hook: Knowledge = the WHAT, Digital = the HOW, and 4IR = the NEXT frontier.",
    ["Knowledge → Digital: engineers and analysts BUILD the platforms and the AI.",
     "Digital → Knowledge: platforms GENERATE data that powers research and better decisions.",
     "'Digitized intelligence': the two fused — data-rich services run by expert teams.",
     "WHAT / HOW / NEXT: knowledge (value), digital (infrastructure), 4IR (the coming fusion, S6)."],
    "s5_overlap.png","Knowledge = WHAT (ideas), Digital = HOW (infrastructure), 4IR = NEXT (fusion).",
    "~7 min. Use the overlap diagram; the WHAT/HOW/NEXT hook is a strong exam mnemonic and bridges to S6.")
add_table_slide("S5 · Concept 2 · examples","Which economy is this? — classify the scenario",
    ["Scenario","Digital / Knowledge / Both","Why"],
    [["Paying a shop via Fonepay QR","Digital","A platform transaction at scale"],
     ["A Fusemachines team building an AI model","Knowledge (→ enables digital)","Value from expertise and research"],
     ["Daraz recommending products to you","Both","Platform (digital) driven by data science (knowledge)"],
     ["A university training data analysts","Knowledge","Builds human capital"],
     ["Streaming a movie on a data pack","Digital","A digital good delivered at scale"],
     ["A bank's analysts designing a fraud model","Knowledge (→ runs on digital)","Expertise, later deployed on a platform"],
     ["Khalti analysing spending by district","Both","Digital data + knowledge-work analysis"]],
    per_page=7,widths=[3.0,2.0,2.5],fs=10.5,
    note="Many real cases are BOTH — the platform (digital) and the expertise that designs and improves it (knowledge) working together. That fusion is 'digitized intelligence'.")
concept_apply("S5 · Concept 2 · [THEORY]","How the Two Economies Reinforce Each Other",
    "Daraz shows the cycle: knowledge workers (engineers, data scientists) built the platform; the platform generates data on millions of purchases; analysts turn that data into better recommendations and logistics; which makes the platform more valuable and generates more data. Digital and knowledge economies feed each other — which is why a country wants BOTH strong platforms and strong human capital.",
    "\"A country should focus on either digital OR knowledge economy.\" They are complementary, not either/or. Platforms without skilled people to build and improve them stagnate; skilled people without digital platforms cannot scale their ideas. The strongest economies grow both together (digitized intelligence).",
    "The digital and knowledge economies reinforce each other in a cycle: knowledge workers design and build digital platforms; those platforms generate data; that data powers more analysis and better decisions (knowledge work); which yields better platforms. Their fusion is 'digitized intelligence'. A memory hook captures the roles — Knowledge is the WHAT (value from ideas), Digital is the HOW (infrastructure), and 4IR is the NEXT frontier.",
    "reinforcing cycle · knowledge builds platforms · platforms generate data · digitized intelligence · WHAT/HOW/NEXT")

add_activity("S5 — 'Digital, knowledge, or both?'  ·  ~5 min",
    ["In pairs (2 min): list five Nepali organisations or services.",
     "Classify each as digital-economy, knowledge-economy, or both — and justify in one line.",
     "Take 4 answers aloud (3 min); resolve any disagreements using the 'source of value' test.",
     "Close: most modern successes are BOTH — that is the point."],
    "Seeds: eSewa (digital), Fusemachines (knowledge→digital), Deerwalk (both), a university (knowledge), Daraz (both), Hamro Patro (both). Reward answers that name the SOURCE of value, not just 'it uses computers'.",
    "ACTIVITY [~5 min].")
add_quiz("S5 — Quick Check  ·  ~5 min",
    [("Q1.  A newly granted patent is an economic output of the:","q"),
     ("a) ✅ knowledge economy   b) digital economy   c) traditional economy   d) none","a"),
     ("     Why: a patent is created by expertise and research — the knowledge economy's characteristic output.","o"),
     ("Q2.  In the memory hook, the digital economy is the:","q"),
     ("a) WHAT   b) ✅ HOW   c) NEXT   d) WHY","a"),
     ("     Why: knowledge = WHAT (ideas/value), digital = HOW (infrastructure), 4IR = NEXT (the coming fusion).","o"),
     ("Discussion: give one Nepali example that is clearly BOTH economies and explain each lens.","o")],
    "QUIZ [~5 min]. The WHAT/HOW/NEXT hook and the patent example are common exam items — drill them.")
add_summary("S5 · Summary  ·  [~2 min]",
    ["Digital economy = tools, platforms, scale (the HOW); knowledge economy = skills, ideas, innovation (the WHAT).",
     "They are confusable because both use technology heavily — the distinction is the SOURCE of value.",
     "They reinforce each other: knowledge builds platforms; platforms generate data that powers more knowledge work."],
    "Whether you build platforms or build expertise, you are working in one (or both) of these economies — and understanding that they feed each other explains why the best careers and countries invest in BOTH technology and human capital.",
    "S6 — the NEXT frontier in the hook: the fourth industrial revolution, its timeline and its drivers.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S6
add_divider("Session 6 · Lecture hour 6 (of 8)","The Fourth Industrial Revolution",
    "Steam once replaced muscle, electricity lit the night, computers automated the office — and now AI writes, machines see, and factories diagnose themselves. Each was called a 'revolution' because it changed what an economy could do. Why is what's happening now the FOURTH one, and not just 'more computers'?",
    "OPENING HOOK [~5 min]. Line up the four revolutions on the board. Agenda: define 4IR (the three-world fusion) → the revolution timeline → the five drivers of 4IR.")

concept_understand("S6 · Concept 1 · [THEORY]","What the Fourth Industrial Revolution Is",
    "The fourth industrial revolution (4IR), named by Klaus Schwab of the World Economic Forum, is the fusion of physical, digital, and biological technologies into connected 'cyber-physical' systems. What is new is not any single technology but the blurring of lines between them — machines that sense and think, biology read and edited by software — at unprecedented speed and scale.",
    ["Physical: robotics, 3D printing, autonomous vehicles, drones.",
     "Digital: AI, IoT, cloud, big data — the connective tissue.",
     "Biological: genomics, biometrics, gene editing (the leg most often forgotten).",
     "The novelty is FUSION: a self-diagnosing machine (physical+digital) or AI gene analysis (digital+biological)."],
    "s6_fusion.png","4IR = fusion of physical + digital + biological into cyber-physical systems.",
    "~7 min. Use the fusion diagram. Give one concrete biological example (AI reading a genome / biometric national ID) so the third leg is real, not a slogan.")
add_table_slide("S6 · Concept 1 · scaffolding","The three worlds 4IR fuses — with examples",
    ["World","Example technologies","4IR when fused with the others"],
    [["Physical","Robots, 3D printing, drones, self-driving","A warehouse robot guided by AI + IoT"],
     ["Digital","AI, IoT, cloud, big data","The 'brain' connecting physical & biological"],
     ["Biological","Genomics, biometrics, gene editing","AI reading a genome; biometric national ID"]],
    per_page=3,widths=[1.3,2.8,3.0],fs=11,
    note="Any one alone is not 4IR. 4IR is the FUSION — cyber-physical systems where the digital layer senses, decides, and acts on the physical and biological worlds. That fusion is what makes it a new revolution.")
concept_apply("S6 · Concept 1 · [THEORY]","What the Fourth Industrial Revolution Is",
    "Nepal's biometric national-ID system is a small 4IR example: a biological trait (fingerprint/iris) is read by digital systems and linked to physical services (SIM registration, banking). No single technology is new, but fusing biological identity with digital records and physical service delivery is exactly the cyber-physical blending Schwab described.",
    "\"4IR is just the third revolution with faster computers.\" The third revolution digitised and automated; the fourth FUSES the digital with the physical and biological into systems that sense, decide, and act. The change is qualitative (blurring the lines between worlds), not merely 'more of the same'.",
    "The fourth industrial revolution (4IR), named by Klaus Schwab (WEF), is the fusion of physical (robotics, 3D printing, autonomous vehicles), digital (AI, IoT, cloud, big data), and biological (genomics, biometrics, gene editing) technologies into connected cyber-physical systems. Its novelty is the blurring of lines between these worlds at unprecedented speed and scale — not any single technology, but their fusion.",
    "4IR · Schwab / WEF · physical + digital + biological · cyber-physical systems · fusion, not just faster computers")

concept_understand("S6 · Concept 2 · [THEORY]","The Four Industrial Revolutions — a timeline",
    "Placing 4IR in history makes it clear. The 1st (from ~1760s) used steam and mechanization; the 2nd (~1870s) brought electricity and mass production; the 3rd (~1970s) introduced electronics, computers, and automation; the 4th (2000s–) fuses AI, data, IoT, and smart systems. Each revolution kept the previous gains but changed the fundamental capability of the economy.",
    ["1st — steam & mechanization: muscle replaced by machines (textiles, railways).",
     "2nd — electricity & mass production: the assembly line, mass consumer goods.",
     "3rd — electronics & computers: automation, the internet, digital records.",
     "4th — AI, data, IoT: systems that sense and decide, fusing the three worlds."],
    "s6_timeline.png","1st steam → 2nd electricity → 3rd computers → 4th AI/data/smart systems.",
    "~7 min. Use the timeline image. Ask which revolution Nepal's factories mostly sit in (often 2nd/3rd) to make it concrete and honest.")
add_table_slide("S6 · Concept 2 · comparison","The four industrial revolutions at a glance",
    ["Revolution","Period","Core technology","What it enabled"],
    [["1st","~1760s–1840s","Steam power, mechanization","Factories, railways, mechanised textiles"],
     ["2nd","~1870s–1914","Electricity, mass production","Assembly lines, mass consumer goods"],
     ["3rd","~1970s–2000s","Electronics, computers, automation","Digital records, the internet, automation"],
     ["4th","2000s–present","AI, data, IoT, cyber-physical systems","Smart, self-optimising, connected systems"]],
    per_page=4,widths=[1.2,1.7,2.6,2.9],fs=11,
    note="A useful reality check: much of Nepal's manufacturing operates at the 2nd–3rd revolution level, while its digital-payment and IT-export sectors touch the 4th. A country can span several revolutions at once.")
concept_apply("S6 · Concept 2 · [THEORY]","The Four Industrial Revolutions",
    "Nepal spans revolutions simultaneously: a brick kiln runs on 2nd-revolution logic (manual labour + basic machines), a bank's core system is 3rd-revolution (computers, automation), and its AI fraud detection and biometric KYC reach into the 4th. Placing technologies on this timeline is a practical way to judge how 'advanced' a given sector really is.",
    "\"Every country moves through the revolutions in strict order.\" Developing economies often leapfrog — Nepal skipped widespread landline/credit-card infrastructure and went straight to mobile wallets. So a country can operate in several revolutions at once and jump stages, rather than climbing them one by one.",
    "The four industrial revolutions: 1st (~1760s) steam and mechanization; 2nd (~1870s) electricity and mass production; 3rd (~1970s) electronics, computers, and automation; 4th (2000s–) AI, data, IoT, and cyber-physical systems. Each preserved earlier gains but changed the economy's fundamental capability. Countries can span several revolutions at once and even leapfrog stages, as Nepal did with mobile money.",
    "four revolutions · steam → electricity → computers → AI/IoT · timeline · leapfrogging · spanning stages at once")

concept_understand("S6 · Concept 3 · [THEORY]","The Five Drivers of 4IR",
    "Five technologies drive the fourth industrial revolution: artificial intelligence (systems that learn and decide), the Internet of Things (everyday objects that sense and connect), big data (the fuel AI learns from), automation & robotics (machines that act), and cloud computing (on-demand power and storage). They combine — AI needs big data, which needs IoT sensors and cloud to store it.",
    ["AI — learns patterns and makes decisions (fraud detection, recommendations).",
     "IoT — sensors and devices that generate real-world data continuously.",
     "Big data — the large, fast datasets AI is trained on.",
     "Automation/robotics + cloud — machines that act, and the computing power behind them."],
    None,"Five 4IR drivers: AI · IoT · big data · automation/robotics · cloud — and they combine.",
    "~7 min. Stress the combination: no single driver is 4IR; AI without data or cloud is inert. This mirrors S2's 'drivers move together' logic.")
add_table_slide("S6 · Concept 3 · scaffolding","The five drivers of 4IR — what each does & a Nepal application",
    ["Driver","What it does","Nepal application"],
    [["Artificial intelligence","Learns patterns, makes decisions","Bank fraud detection; chatbots"],
     ["Internet of Things (IoT)","Objects sense & connect","Agri sensors; smart meters"],
     ["Big data","Large fast datasets to learn from","Telecom/wallet usage analytics"],
     ["Automation & robotics","Machines that act physically","Automated warehousing; manufacturing"],
     ["Cloud computing","On-demand compute & storage","Startups hosting on AWS/GCP/Azure"]],
    per_page=5,widths=[1.9,2.6,2.6],fs=11,
    note="The drivers are interlocking: AI is only as good as its big data; big data needs IoT to generate it and cloud to store and process it. 4IR is the STACK working together, not any one layer.")
concept_apply("S6 · Concept 3 · [THEORY]","The Five Drivers of 4IR",
    "A Nepali agri-tech startup putting IoT soil sensors in fields shows the drivers combining: sensors (IoT) stream readings (big data) to the cloud, where AI predicts irrigation or disease, and automated pumps act on the decision. Remove any layer — no sensors, no cloud, no AI — and the 'smart farm' collapses into an ordinary one. The drivers only deliver 4IR together.",
    "\"AI by itself is the fourth industrial revolution.\" AI is one of five interlocking drivers. Without big data to learn from, IoT to generate it, cloud to run on, and automation to act, AI does nothing physical. 4IR is the whole stack combining — echoing S2's lesson that drivers advance together.",
    "Five technologies drive 4IR: artificial intelligence (learns and decides), the Internet of Things (objects that sense and connect), big data (the datasets AI learns from), automation & robotics (machines that act), and cloud computing (on-demand compute and storage). They are interlocking — AI needs big data, which needs IoT and cloud — so 4IR emerges from the stack working together, not any single driver.",
    "AI · IoT · big data · automation/robotics · cloud · interlocking stack · combine to produce 4IR")

add_activity("S6 — 'Which revolution is it?'  ·  ~5 min",
    ["In pairs (2 min): list four technologies or workplaces you know in Nepal.",
     "Place each on the four-revolution timeline (1st–4th) and justify.",
     "Take 3–4 answers aloud (3 min); note anything that leapfrogged.",
     "Close: a single country — even a single company — can span several revolutions."],
    "Seeds: brick kiln (2nd), bank core banking (3rd), AI fraud detection / agri-IoT (4th), mobile wallets (leapfrogged straight to 4th-adjacent). Reward reasoning about WHY, and spotting leapfrogging.",
    "ACTIVITY [~5 min].")
add_quiz("S6 — Quick Check  ·  ~5 min",
    [("Q1.  What makes 4IR different from the third revolution is:","q"),
     ("a) faster computers   b) ✅ fusion of physical, digital & biological into cyber-physical systems   c) more internet   d) cheaper phones","a"),
     ("     Why: the qualitative change is blurring the lines between the three worlds, not just more computing.","o"),
     ("Q2.  Which is NOT one of the five drivers of 4IR?","q"),
     ("a) AI   b) IoT   c) big data   d) ✅ steam power","a"),
     ("     Why: steam powered the FIRST revolution; the 4IR drivers are AI, IoT, big data, automation/robotics, cloud.","o"),
     ("Discussion: give a Nepali example where at least three 4IR drivers combine.","o")],
    "QUIZ [~5 min]. Nail the 'fusion not faster computers' point and the five drivers — both common exam items.")
add_summary("S6 · Summary  ·  [~2 min]",
    ["4IR (Schwab/WEF) = fusion of physical + digital + biological into cyber-physical systems — not 'faster computers'.",
     "Timeline: 1st steam → 2nd electricity → 3rd computers → 4th AI/data/IoT; countries can span & leapfrog stages.",
     "Five interlocking drivers: AI, IoT, big data, automation/robotics, cloud — they deliver 4IR only in combination."],
    "4IR is reshaping the jobs you are training for — some will vanish, others will be created. Knowing what actually drives it (and that it is a fusion, not a gadget) lets you position your skills for the change instead of being blindsided by it.",
    "S7 — what 4IR gives and what it costs: opportunities, challenges, and Nepal's readiness (SWOT).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S7
add_divider("Session 7 · Lecture hour 7 (of 8)","4IR — Opportunities & Challenges",
    "The same AI that could help a Nepali farmer predict crop disease could also erase the data-entry jobs that thousands of Nepalis do today. The 4th industrial revolution is a double-edged sword: it promises leapfrog growth and threatens mass disruption at the same time. For a country like Nepal, which edge wins?",
    "OPENING HOOK [~5 min]. Hold both edges at once. Agenda: opportunities (incl. leapfrogging) → challenges (incl. digital divide) → Nepal's 4IR SWOT & an interconnection example.")

concept_understand("S7 · Concept 1 · [THEORY]","The Opportunities of 4IR",
    "4IR opens real opportunities: economic and business growth, innovation that lets developing economies LEAPFROG old stages, new kinds of jobs (AI, cloud, cybersecurity, UX), better public services (e-governance, telemedicine, smart cities), improved quality of life, and stronger global competitiveness. For Nepal, leapfrogging is the biggest prize — skipping legacy infrastructure straight to modern systems.",
    ["Leapfrogging: Nepal skipped landlines/credit cards and jumped to mobile money.",
     "New jobs: AI engineers, data analysts, cloud and cybersecurity specialists, UX designers.",
     "Better public services: e-governance, telemedicine to remote areas, smart utilities.",
     "Global competitiveness: small firms can serve world markets from Kathmandu."],
    None,"Opportunities: growth, LEAPFROGGING, new jobs, better public services, global reach.",
    "~7 min. Leapfrogging is the hopeful, Nepal-specific angle — make it vivid (mobile money without ever having credit cards).")
add_table_slide("S7 · Concept 1 · scaffolding","4IR opportunities — with Nepal examples",
    ["Opportunity","What it means","Nepal example"],
    [["Leapfrogging","Skip legacy stages to modern tech","Mobile wallets without a credit-card era"],
     ["New industries & jobs","Whole new job categories","AI, data, cloud, cybersecurity, UX roles"],
     ["Better public services","Digital, reachable governance & health","Nagarik App; telemedicine to rural areas"],
     ["Global competitiveness","Serve world markets from Nepal","IT/BPO exports; remote work"],
     ["Innovation & efficiency","Do more with less","Agri-tech, fintech, smart logistics"],
     ["Quality of life","Convenience, access, inclusion","Online education, digital health records"]],
    per_page=6,widths=[1.9,2.6,2.6],fs=10.5,
    note="Leapfrogging is the standout opportunity for Nepal: no need to build the old infrastructure first — but it only pays off if the challenges on the next slide (skills, connectivity, divide) are managed.")
concept_apply("S7 · Concept 1 · [THEORY]","The Opportunities of 4IR",
    "Nepal's mobile-money boom is leapfrogging in action: it never built a nationwide credit-card and cheque infrastructure — it jumped straight to wallets and QR. 4IR lets a developing economy skip expensive legacy stages and adopt the newest systems directly, turning 'being behind' into a chance to build modern from the start.",
    "\"4IR only benefits already-rich, advanced economies.\" Leapfrogging means developing economies can gain the MOST — adopting mobile, cloud, and AI without the cost of legacy systems. Nepal's wallet adoption outpaced many richer countries' card habits precisely because it had less legacy to unwind.",
    "4IR offers opportunities: economic and business growth, innovation enabling developing economies to leapfrog legacy stages, new job categories (AI, cloud, cybersecurity, UX), better public services (e-governance, telemedicine, smart cities), improved quality of life, and stronger global competitiveness. For Nepal, leapfrogging is the biggest prize — as shown by mobile money adopted without ever building a credit-card era — provided the accompanying challenges are managed.",
    "opportunities · leapfrogging · new jobs · e-governance/telemedicine · global competitiveness · Nepal mobile money")

concept_understand("S7 · Concept 2 · [THEORY]","The Challenges of 4IR",
    "4IR's challenges are just as real: a skill gap (workers unready for new tech), job displacement (automation replacing routine work), the high cost of technology, privacy and cybersecurity risks, the digital divide (rural vs urban, older vs younger), and ethical/social issues (AI bias, over-dependence). The honest picture is that 4IR shifts the skill mix — reskilling decides who benefits and who is left behind.",
    ["Job displacement: routine, data-entry, and repetitive roles are most exposed.",
     "Skill gap: demand shifts to AI/data/cloud skills faster than training keeps up.",
     "Digital divide: rural, poorer, and older populations risk being left behind.",
     "Privacy, cybersecurity, and AI bias grow with the technology's reach."],
    None,"Challenges: skill gap, job displacement, cost, privacy/security, digital divide, AI ethics.",
    "~7 min. Frame displacement honestly: 4IR shifts jobs (destroys some, creates others). The variable that decides winners is reskilling and the divide.")
add_table_slide("S7 · Concept 2 · comparison","4IR — opportunities vs matching challenges (Nepal consequence)",
    ["Opportunity","Matching challenge","Nepal consequence"],
    [["New high-skill jobs","Skill gap — training lags demand","Jobs exist but locals may not qualify"],
     ["Automation & efficiency","Job displacement of routine work","Data-entry/BPO roles at risk"],
     ["Digital public services","Digital divide (rural, older, poorer)","Services miss those without access"],
     ["Data-driven everything","Privacy & cybersecurity risk","Weak data law (S8, Unit 6) magnifies harm"],
     ["Powerful AI systems","AI bias & over-dependence","Unfair decisions; loss of local capability"],
     ["Cutting-edge technology","High cost of adoption","Small firms priced out without support"]],
    per_page=6,widths=[2.1,2.3,2.6],fs=10.5,
    note="Every opportunity has a matching challenge. The decisive variable is reskilling and inclusion: manage the divide and the skill gap, and the opportunities win; ignore them and disruption dominates.")
concept_apply("S7 · Concept 2 · [THEORY]","The Challenges of 4IR",
    "Automation threatens the routine data-entry and BPO work that employs thousands of Nepalis — but the same wave creates demand for AI, data, and cloud roles. Whether a displaced worker moves up or falls out depends on reskilling and access. That is why the digital divide (who has connectivity, devices, and training) is the challenge that decides the others.",
    "\"4IR will simply destroy jobs\" OR \"4IR will simply create jobs.\" Both halves are true at once — it destroys routine roles and creates new skilled ones. It SHIFTS the skill mix. The real question is whether people can reskill and access the new opportunities, which is a policy and inclusion problem, not a technology one.",
    "4IR's challenges include a skill gap (training lags new-tech demand), job displacement (automation replacing routine work), the high cost of technology, privacy and cybersecurity risks, the digital divide (rural/urban, age, income), and ethical issues like AI bias and over-dependence. 4IR shifts the skill mix rather than simply adding or removing jobs, so reskilling and inclusion — managing the divide — decide who benefits and who is left behind.",
    "challenges · skill gap · job displacement · digital divide · privacy/cybersecurity · AI bias · reskilling decides")

concept_understand("S7 · Concept 3 · [THEORY] [EXAMPLE]","Nepal's 4IR Readiness — a SWOT & the interconnection",
    "A SWOT captures Nepal's 4IR position: strengths (young, tech-open population, growing IT education, fast digital-payment uptake), weaknesses (weak rural connectivity/power, slow policy, skill/R&D gaps), opportunities (IT/BPO exports, tourism- and agri-tech, leapfrogging), and threats (job loss without reskilling, cyber/privacy risk, a widening divide). The three ideas of this unit — knowledge, digital, and 4IR — fuse in real systems.",
    ["Strengths vs weaknesses are INTERNAL (what Nepal has/lacks now).",
     "Opportunities vs threats are EXTERNAL (what the world offers/imposes).",
     "Interconnection: knowledge (WHAT) + digital (HOW) + 4IR (NEXT) combine in real products.",
     "Example: precision agriculture = agronomy knowledge + digital platform + IoT/AI (4IR)."],
    "s7_swot.png","SWOT: internal strengths/weaknesses × external opportunities/threats; reskilling is the hinge.",
    "~8 min. Use the SWOT image. Close the unit's conceptual arc: knowledge+digital+4IR fuse (the L6 'triple fusion' idea) in things like smart farming and digital twins.")
add_table_slide("S7 · Concept 3 · examples","Triple fusion — knowledge + digital + 4IR in one system",
    ["System","Knowledge leg","Digital leg","4IR leg / impact"],
    [["Precision agriculture","Agronomy expertise","Farm data platform","IoT sensors + AI → higher yield"],
     ["Digital health record","Medical knowledge","Patient data system","AI diagnosis + telemedicine reach"],
     ["Smart logistics (Daraz)","Operations research","E-commerce platform","AI routing + automation → faster delivery"],
     ["Fraud detection (bank)","Risk analysts' expertise","Transaction platform","AI + big data flag fraud in real time"],
     ["Ride-hailing (Pathao)","Pricing & ops know-how","Matching platform","GPS/IoT + algorithms → efficient rides"]],
    per_page=5,widths=[2.0,2.2,2.0,2.6],fs=10.5,
    note="Each real system needs all three: human expertise (knowledge), a digital platform (digital), and 4IR technologies (AI/IoT/automation). This 'digitized intelligence' is where the whole unit's ideas come together.")
concept_apply("S7 · Concept 3 · [THEORY] [EXAMPLE]","Nepal's 4IR Readiness & the Interconnection",
    "A Nepali agri-tech venture fuses all three: agronomy knowledge (which crop, which threat), a digital platform (dashboards, data), and 4IR tech (IoT sensors + AI prediction). The SWOT tells you whether it can scale here — strengths (young talent, mobile uptake) and opportunities (agri-tech demand) push it forward; weaknesses (rural connectivity) and threats (skills, cyber risk) hold it back. Managing the weak side is the strategy.",
    "\"Knowledge economy, digital economy, and 4IR are three separate topics.\" In real systems they fuse: knowledge supplies the WHAT, digital the HOW, and 4IR the NEXT-frontier capability. A smart farm or a fraud-detection system is all three at once — which is why this unit taught them together.",
    "A SWOT frames Nepal's 4IR readiness: strengths (young tech-open population, growing IT education, fast digital-payment uptake), weaknesses (weak rural connectivity/power, slow policy, skill/R&D gaps), opportunities (IT/BPO exports, tourism/agri-tech, leapfrogging), threats (job loss without reskilling, cyber/privacy risk, widening divide). Strengths/weaknesses are internal, opportunities/threats external. Real systems fuse knowledge (WHAT) + digital (HOW) + 4IR (NEXT) — 'digitized intelligence'.",
    "SWOT · internal vs external · strengths/weaknesses/opportunities/threats · triple fusion · knowledge+digital+4IR")

add_activity("S7 — 'Which job, which way?'  ·  ~5 min",
    ["In pairs (2 min): name one Nepali job most AT RISK from 4IR and one most CREATED by it.",
     "For the at-risk job, propose one reskilling path to the created one.",
     "Take 3–4 answers aloud (3 min); place them on the SWOT (threat → opportunity).",
     "Close: reskilling is the bridge that turns a threat into an opportunity."],
    "Seeds: at risk — data entry, basic BPO, routine accounting, toll collection. Created — AI/data roles, cybersecurity, cloud ops, UX, digital marketing. Reward a realistic reskilling bridge, not just naming jobs.",
    "ACTIVITY [~5 min].")
add_quiz("S7 — Quick Check  ·  ~5 min",
    [("Q1.  'Leapfrogging' in the 4IR context means:","q"),
     ("a) falling behind   b) ✅ skipping legacy stages to adopt modern tech directly   c) copying rich countries   d) banning old tech","a"),
     ("     Why: Nepal jumped straight to mobile money without a credit-card era — adopting the new without the old.","o"),
     ("Q2.  In a SWOT, the digital divide is a:","q"),
     ("a) strength   b) opportunity   c) ✅ weakness/threat (it holds readiness back)   d) driver","a"),
     ("     Why: unequal access is a limitation/risk — it prevents opportunities from reaching everyone.","o"),
     ("Discussion: which single Nepali job is most at risk from 4IR, and what would you retrain into?","o")],
    "QUIZ [~5 min]. Draw out both edges (opportunity + challenge) and the reskilling bridge between them.")
add_summary("S7 · Summary  ·  [~2 min]",
    ["Opportunities: growth, LEAPFROGGING (Nepal's biggest prize), new jobs, better public services, global reach.",
     "Challenges: skill gap, job displacement, cost, privacy/security, digital divide, AI ethics — reskilling decides winners.",
     "Nepal 4IR SWOT (internal strengths/weaknesses × external opportunities/threats); knowledge+digital+4IR fuse in real systems."],
    "4IR will reshape your job market within your working life — those who reskill and have access capture the opportunities; those who don't face the disruption. Understanding both edges lets you plan your skills deliberately rather than react.",
    "S8 — stepping back: the digital economy's influence on sustainability, privacy, regulation, and strategy.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S8
add_divider("Session 8 · Lecture hour 8 (of 8) — CLOSES UNIT 1","Influence of the Digital Economy",
    "Going digital saves paper and fuel — but it also fills landfills with dead phones, tracks your every tap, and forces regulators to write brand-new rules faster than they can keep up. Progress sends a bill; the question is who pays it, who regulates it, and how businesses should respond. That is the digital economy's INFLUENCE.",
    "OPENING HOOK [~5 min]. Bust the 'digital = automatically clean & safe' myth. Agenda: sustainability (two-sided) → privacy & regulation (intro; depth in Unit 6) → strategy. Note the deep Nepal policy stack comes in Unit 6.")

concept_understand("S8 · Concept 1 · [THEORY]","Influence on Sustainability — both sides",
    "The digital economy cuts some environmental costs and creates others. On the plus side: paperless offices, remote work (fewer commutes), smart energy systems, and digital public services reduce physical footprint. On the minus side: e-waste (discarded phones, laptops, batteries — often with no safe recycling in Nepal) and the growing energy and water demand of data centres. 'Digital' is not automatically 'green'.",
    ["Positive: less paper, less travel, smarter energy use, efficient logistics.",
     "Negative: e-waste with toxic materials, and Nepal lacks formal recycling infrastructure.",
     "Hidden cost: data centres and AI consume large amounts of electricity and water.",
     "Net effect depends on choices — device lifespan, recycling, and clean energy."],
    "s8_quadrant.png","Sustainability cuts both ways: less paper/travel, but e-waste + data-centre energy.",
    "~7 min. Use the influence quadrant. Kill the 'digital = green' myth with the e-waste/energy counterpoint; net effect depends on design and disposal choices.")
add_table_slide("S8 · Concept 1 · comparison","The digital economy's influence — four fronts, two sides each",
    ["Front","Positive influence","Negative influence","Nepal angle"],
    [["Sustainability","Paperless, remote work, smart energy","E-waste, data-centre energy/water","No formal e-waste recycling yet"],
     ["Privacy","Convenience, personalization","Tracking, consent gaps, data misuse","Weak data-protection law (Unit 6)"],
     ["Regulation","Trust, consumer protection, tax","Law lags technology; grey areas","NRB rules exist; data law pending"],
     ["Strategy","Data-driven, digital-first advantage","Constant disruption; adaptation cost","SMEs must adapt or lose ground"]],
    per_page=4,widths=[1.5,2.4,2.4,2.2],fs=10.5,
    note="This table IS the shape of S8: every front of influence has an upside and a downside. The unit's closing message — 'digital is not automatically green or safe' — is visible across all four rows.")
concept_apply("S8 · Concept 1 · [THEORY]","Influence on Sustainability",
    "Kathmandu's growing pile of discarded phones and laptops has nowhere formal to go — Nepal has little e-waste recycling infrastructure, so toxic materials (lead, mercury) risk leaching into soil and water. Meanwhile the same digital services cut paper and travel. Whether the digital economy is net-green in Nepal depends on choices: longer device life, proper recycling, and cleaner energy for any data centres.",
    "\"Digital automatically means environmentally friendly.\" It shifts the footprint rather than removing it — from paper and fuel to e-waste and electricity. Without recycling and clean energy, 'going digital' can simply hide the smoke somewhere else. Sustainability is a design and disposal choice, not a free gift of technology.",
    "The digital economy influences sustainability both ways: it cuts footprint through paperless offices, remote work, smart energy, and digital services, but creates e-waste (toxic discarded devices, with little safe recycling in Nepal) and rising data-centre energy and water demand. The net effect depends on choices — device lifespan, recycling, and clean energy — so 'digital' is not automatically 'green'.",
    "sustainability · paperless/remote (positive) · e-waste + data-centre energy (negative) · not automatically green")

concept_understand("S8 · Concept 2 · [THEORY]","Influence on Privacy & Regulation",
    "As the economy digitises, services collect vast personal data (location, contacts, spending) — often without clear consent — creating privacy risk and forcing new regulation. Regulators must protect users, tax digital activity, and secure e-commerce, but law tends to LAG technology. In Nepal, NRB regulates wallets/QR, but there is no dedicated data-protection law yet — a gap Unit 6 examines in depth.",
    ["Privacy: apps track location, contacts, and behaviour; consent is often buried or missing.",
     "Regulation exists but lags: NRB wallet rules and e-commerce/VAT rules are in place…",
     "…yet Nepal has only a thin Privacy Act (2075) and no dedicated data-protection law.",
     "Good regulation builds trust; absent regulation lets data misuse and fraud grow."],
    None,"More data collected → privacy risk → new regulation, but law lags tech (Nepal: no data-protection law yet).",
    "~7 min. Keep this INTRODUCTORY — name the privacy risk and the regulation response, flag the data-law gap, and forward-reference Unit 6 for the full Nepal policy stack (IT Policy 2072, Digital Nepal Framework, Startup Act).")
add_table_slide("S8 · Concept 2 · examples","Privacy & regulation — the influence in concrete cases",
    ["Situation","Privacy / regulation issue","What responds (Nepal)"],
    [["App requests contacts & location on install","Consent often unclear or coerced","(No data-protection law yet — Unit 6)"],
     ["A digital wallet handles your money","Needs licensing, KYC, security rules","NRB wallet & KYC regulation"],
     ["Any wallet must pay any merchant QR","Interoperability & fair access","NRB QR-interoperability rule"],
     ["Buying online from an unknown seller","Consumer protection, refunds, fraud","E-commerce rules & VAT (developing)"],
     ["A lending app reuses your data","Data misuse, aggressive collection","Weak safeguards — a live policy gap"]],
    per_page=5,widths=[2.4,2.5,2.4],fs=10.5,
    note="Regulation is catching up unevenly: financial rules (NRB) are relatively strong, but data-protection law is still missing. Unit 6 (Digitalization — Nepalese Perspective) covers the full policy landscape.")
concept_apply("S8 · Concept 2 · [THEORY]","Influence on Privacy & Regulation",
    "When you install a typical Nepali app and it demands your contacts, location, and storage, there is currently no dedicated data-protection law setting limits on what it may do with that data — only a thin Privacy Act (2075). NRB firmly regulates the money side (wallets, KYC, QR interoperability), but the personal-data side lags. That gap between fast technology and slow law is the regulation story in one example.",
    "\"If an app is allowed to operate, my data must be legally protected.\" In Nepal, financial regulation (NRB) is real, but there is no comprehensive data-protection law — so 'allowed to operate' does not mean 'your personal data is protected'. Law lagging technology is the norm, not the exception (full picture in Unit 6).",
    "As the economy digitises, services collect vast personal data (location, contacts, spending) — often without clear consent — creating privacy risk and forcing new regulation to protect users, tax digital activity, and secure e-commerce. But law lags technology: in Nepal, NRB regulates wallets, KYC, and QR interoperability, yet there is only a thin Privacy Act (2075) and no dedicated data-protection law. Good regulation builds trust; its absence lets misuse grow. (Unit 6 goes deep.)",
    "privacy risk · consent gaps · regulation lags tech · NRB (wallets/KYC/QR) · no data-protection law yet · Unit 6")

concept_understand("S8 · Concept 3 · [THEORY]","Influence on Business & National Strategy",
    "The digital economy forces new strategy. For firms: become data-driven (decide on evidence), digital-first (serve customers online), and automation-enabled (cut errors and cost) to win competitive advantage — or lose to rivals who do. For nations: a strategy like 'Digital Nepal' and the push toward a cashless economy aims to modernise the whole system. Standing still is itself a losing strategy.",
    ["Firm strategy: data-driven decisions, digital-first channels, automation for efficiency.",
     "The pressure is competitive — a rival who digitises faster wins customers.",
     "National strategy: Digital Nepal Framework, cashless push, skills agenda (detail in Unit 6).",
     "'Do nothing' is a choice with consequences — disruption reaches those who don't adapt."],
    None,"Strategy shifts: firms go data-driven / digital-first / automated; nations push Digital-Nepal & cashless.",
    "~6 min. Keep national strategy light (name Digital Nepal, forward to Unit 6). Focus on the firm-level shift and the competitive pressure to adapt.")
add_table_slide("S8 · Concept 3 · scaffolding","How the digital economy changes strategy — old vs new posture",
    ["Strategic choice","Old posture","New (digital-economy) posture"],
    [["Decisions","Gut feel, experience","Data-driven, evidence-based"],
     ["Customer channel","Physical branch/shop only","Digital-first (app/web), branch optional"],
     ["Operations","Manual, paper-based","Automated, integrated systems"],
     ["Competition","Local rivals","Platforms & firms anywhere"],
     ["Adaptation","Occasional, slow","Continuous — expect constant change"],
     ["National level","Analog governance","Digital Nepal, cashless push (Unit 6)"]],
    per_page=6,widths=[1.9,2.4,2.8],fs=10.5,
    note="The through-line: the digital economy makes 'do nothing' a losing strategy. Both firms and the country must move from gut-feel, physical-first, occasional adaptation toward data-driven, digital-first, continuous adaptation.")
concept_apply("S8 · Concept 3 · [THEORY]","Influence on Business & National Strategy",
    "A Nepali retailer that ignored online channels and stuck to a single physical shop lost ground to competitors on Daraz and social commerce during and after COVID. The digital economy rewrote the strategy rulebook: data-driven, digital-first, automation-enabled firms pulled ahead, while 'wait and see' businesses shrank. At the national level, the Digital Nepal Framework is the country's version of the same bet.",
    "\"Digital strategy is optional — a business can succeed the traditional way indefinitely.\" In a digitising economy, not adapting is itself a (losing) strategy: rivals who go data-driven and digital-first capture your customers. Adaptation is continuous, not a one-time project — the posture, not just the tools, has to change.",
    "The digital economy forces strategic change. Firms must become data-driven (evidence-based decisions), digital-first (online channels), and automation-enabled (lower cost and errors) to gain competitive advantage, because rivals who digitise faster win customers — making 'do nothing' a losing strategy. Nations respond with strategies like the Digital Nepal Framework and a cashless push (detailed in Unit 6). Adaptation is continuous, not a one-off.",
    "strategy · data-driven · digital-first · automation · competitive advantage · Digital Nepal · continuous adaptation")

add_activity("S8 — 'One rule, one strategy'  ·  ~5 min",
    ["In pairs (3 min): propose ONE regulation you'd add to Nepal's digital economy AND one strategy move for a small business.",
     "Say which front it addresses — sustainability, privacy, regulation, or strategy.",
     "Take 3–4 answers aloud (2 min); check each names a real front and a real trade-off.",
     "Close: influence is managed by choices — regulation and strategy — not left to chance."],
    "Seeds: rule — a data-protection law with consent limits; e-waste take-back rule; strategy — a shop joining Daraz + accepting QR; a firm adopting basic analytics. Reward answers that name the front and acknowledge a cost.",
    "ACTIVITY [~5 min].")
add_quiz("S8 — Quick Check  ·  ~5 min",
    [("Q1.  'Going digital is automatically green' is:","q"),
     ("a) true   b) ✅ false — it shifts the footprint (e-waste, data-centre energy)   c) always true in Nepal   d) true for phones only","a"),
     ("     Why: digital cuts paper/travel but creates e-waste and energy demand; net effect depends on choices.","o"),
     ("Q2.  Nepal's current data-protection situation is best described as:","q"),
     ("a) a strong dedicated law   b) ✅ only a thin Privacy Act (2075), no dedicated data-protection law yet   c) EU-level rules   d) no rules of any kind","a"),
     ("     Why: NRB regulates money (wallets/KYC/QR), but comprehensive personal-data law is still missing (Unit 6).","o"),
     ("Discussion: name one digital-economy influence you have felt personally on each of two fronts.","o")],
    "QUIZ [~5 min]. Reinforce the 'not automatically green/safe' theme and the data-law gap (bridge to Unit 6).")
add_summary("S8 · Summary  ·  [~2 min]",
    ["Sustainability cuts both ways: paperless/remote (greener) vs e-waste + data-centre energy — not automatically green.",
     "Privacy & regulation: more data → more risk → new rules, but law lags tech (Nepal: NRB rules yes, data law not yet).",
     "Strategy shifts: firms go data-driven/digital-first/automated; nations push Digital Nepal — 'do nothing' loses."],
    "You feel the digital economy's influence every day — in your data, your job market, and the environment. Whether that influence is net-positive depends on regulation and strategy, and as future professionals and citizens you will help make those choices.",
    "Next unit — Unit 2: the FUNDAMENTALS — multi-sided platforms, network effects, lock-in, and how digital monopolies form.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 1 · Cheat Sheet","One-page revision reference",
    [("Digital economy (S1–S2)","Value created/exchanged THROUGH digital tech (tech IS the activity; beyond e-commerce). 5 characteristics: data-driven, automated, connected, platform-based, scalable (near-zero marginal cost). Drivers: technological/social/business. Ecosystem: consumers · businesses/platforms · regulators (NRB) · tech providers."),
     ("Knowledge economy (S3–S4)","Value from knowledge, skills, innovation (human capital, IP) — minds not machines. Knowledge workers & companies; KM = capture/share knowledge. Explicit (written) vs tacit (in-the-head). 6 drivers form a loop; Nepal weak on R&D/IP → brain drain."),
     ("Digital vs knowledge (S5)","Digital = tools/platforms/scale (HOW); knowledge = skills/ideas (WHAT). Confusable (both use tech); differ by SOURCE of value. They reinforce each other → 'digitized intelligence'. Hook: knowledge=WHAT, digital=HOW, 4IR=NEXT."),
     ("4IR (S6)","Schwab/WEF: fusion of physical + digital + biological → cyber-physical systems (not 'faster computers'). Timeline: steam→electricity→computers→AI/IoT. 5 drivers: AI, IoT, big data, automation/robotics, cloud (interlocking)."),
     ("4IR opps & challenges (S7)","Opportunities: growth, LEAPFROGGING, new jobs, e-gov/telemedicine, global reach. Challenges: skill gap, job displacement, cost, privacy/security, digital divide, AI bias. Reskilling decides winners. Nepal SWOT (internal vs external)."),
     ("Influence (S8)","Four fronts, two sides each: sustainability (paperless vs e-waste), privacy (convenience vs tracking), regulation (trust vs law-lags-tech), strategy (advantage vs disruption). Not automatically green/safe. Nepal: NRB rules yes, data law not yet (Unit 6).")])

add_glossary("Unit 1 · Glossary","Key terms — quick reference",
    [("Digital economy","economic activity enabled by and dependent on digital technology."),
     ("Marginal cost","the cost of serving one more user; near-zero for digital goods."),
     ("Scalability","ability to serve many more users at little extra cost."),
     ("Platform","a shared digital base on which others build/transact (Daraz, eSewa)."),
     ("Digital-economy ecosystem","consumers, businesses/platforms, regulators, tech providers."),
     ("Knowledge economy","economy where value comes from knowledge, skills & innovation."),
     ("Human capital","the skills, education & experience embodied in people."),
     ("Knowledge worker","someone who creates, analyses & applies knowledge."),
     ("Knowledge company","a firm whose primary resource is knowledge."),
     ("Knowledge management","capturing, organising & sharing knowledge to reuse it."),
     ("Explicit knowledge","written/recorded knowledge — manuals, code, SOPs."),
     ("Tacit knowledge","personal know-how — experience, intuition, skill."),
     ("Intellectual property (IP)","legal rights over creations of the mind."),
     ("Brain drain","emigration of skilled, educated people."),
     ("Digitized intelligence","the fusion of digital platforms and knowledge work."),
     ("Fourth industrial revolution (4IR)","fusion of physical, digital & biological technologies."),
     ("Cyber-physical system","a system where digital control senses and acts on the physical world."),
     ("Internet of Things (IoT)","everyday objects with sensors that connect and share data."),
     ("Big data","very large, fast datasets used to find patterns / train AI."),
     ("Leapfrogging","skipping legacy stages to adopt modern technology directly."),
     ("Digital divide","the gap between those with and without digital access/skills."),
     ("SWOT","strengths, weaknesses (internal) × opportunities, threats (external)."),
     ("E-waste","discarded electronics containing toxic materials."),
     ("Digital-first strategy","serving customers primarily through digital channels."),
     ("Data-protection law","law governing how personal data may be collected & used (pending in Nepal).")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 1 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit1_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review. (Note: no genuine IT 250 past-paper was available — these are built from the syllabus and concept slides.)")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  The digital economy is best defined as   →  ✅ activity enabled by & dependent on digital tech","a"),
     ("2.  'Near-zero marginal cost' means   →  ✅ serving one more user costs almost nothing","a"),
     ("3.  In the ecosystem, NRB is a   →  ✅ government/regulator","a"),
     ("4.  A written KYC manual is   →  ✅ explicit knowledge","a"),
     ("5.  A knowledge company's main asset is   →  ✅ its people & their expertise","a"),
     ("6.  A patent is an output of the   →  ✅ knowledge economy","a"),
     ("7.  Digital = HOW, knowledge = WHAT, 4IR =   →  ✅ NEXT (the coming fusion)","a"),
     ("8.  4IR differs from the 3rd revolution by   →  ✅ fusing physical + digital + biological","a"),
     ("9.  NOT a 4IR driver   →  ✅ steam power (that was the 1st revolution)","a"),
     ("10.  'Leapfrogging' means   →  ✅ skipping legacy stages to adopt modern tech directly","a"),
     ("11.  The digital divide is a   →  ✅ weakness/threat in a SWOT","a"),
     ("12.  Nepal's data-protection law status   →  ✅ thin Privacy Act only, no dedicated law yet","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Define the digital economy + list 3 of its drivers.   14. Explicit vs tacit knowledge, with an example of each.   15. Give 3 differences between the digital and knowledge economies.","o"),
     ("16. List 3 opportunities and 3 challenges of 4IR.   17. Name the four fronts of the digital economy's influence.","o"),
     ("Section C — Applied case","q"),
     ("18. Map a Nepali app (e.g. Pathao) onto the four ecosystem actors, and name one benefit + matching challenge it creates.","o"),
     ("19. Classify five given scenarios as digital-economy, knowledge-economy, or both — justify each by its source of value.","o"),
     ("Section D — Discussion","q"),
     ("20. 'Is Nepal ready for the fourth industrial revolution?' Argue using the SWOT (strengths/weaknesses/opportunities/threats).","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit1_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 1  ·  IT 250",
          "S1–S8 complete: the digital economy (concepts · drivers · ecosystem) · the knowledge economy (workers · KM · drivers) · "
          "digital vs knowledge · the 4th industrial revolution (timeline · drivers · opportunities · challenges) · influence (sustainability · privacy · regulation · strategy)",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe, Nepal-localised · Next: Unit 2 — Fundamentals: platforms, network effects & monopolies.")

_add_page_numbers()
save("IT250_Unit1.pptx")
