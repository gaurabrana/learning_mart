#!/usr/bin/env python3
"""IT250 (eighth) Unit 4 deck — Digital Transformation (S26-S33), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables - each
table on its OWN slide, paginated, never squeezed. Self-contained & PDF-safe. Imports
eighth/deckkit.py. Diagrams in images/. Localised to Nepal (eSewa/Khalti/IME Pay, Daraz/Pathao/
Foodmandu, Nagarik App, remittances, crypto BAN). Source: syllabus + lecture PDFs (mapped in
Unit4_content_outline.md §0).
NOTE: the 4IR / four-industrial-revolutions TIMELINE was taught in Unit 1 S6 - S29 cross-references
it and focuses on the revolution->world-economy LINK, it does NOT re-teach the timeline.
Run: python3 build_unit4_pptx.py -> IT250_Unit4.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 4 — Digital Transformation",
          "IT 250: Digital Economy  ·  BIM 8th Semester  ·  Sessions S26–S33 (8 lecture hours)",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal-localised) — no abstraction without instances. The digital-currency block is the most "
          "exam-weighted. Exports to PDF with no information lost.")

add_outcomes("Unit 4 — Learning Outcomes","digital transformation  ·  s26–s33",
    "By the end of this unit, you will be able to:",
    ["Define digital transformation and distinguish digitization / digitalization / DT (S26)",
     "Identify the drivers of DT — technological, economic, social, and crisis (S27)",
     "Explain how DT accelerates the SDGs (esp. 4, 8, 9, 16) and what ICT4D means (S28)",
     "Explain the technological revolution's role in the world economy — productivity, platform economy, labour (S29)",
     "Distinguish traditional vs digital globalization and explain digital-age economic growth (S30–S31)",
     "Define digital currencies, distinguish digital money vs digital currency, and compare crypto / stablecoin / CBDC — incl. Nepal's ban (S32–S33)"],
    "This is Unit 4 of IT 250. It moves from HOW the digital economy works (Units 1–3) to how it CHANGES organisations, society, and money — ending on the richest, most exam-ready block: digital currencies and Nepal's crypto ban.")

add_roadmap("Unit 4 — Roadmap","Where each session fits (S26–S33)",
    ["S26  DT concepts: digitization → digitalization → transformation",
     "S27  Drivers of digital transformation",
     "S28  Accelerating the SDGs through DT",
     "S29  Technological revolution & the world economy",
     "S30  Globalization in the digital age",
     "S31  Digital transformation & economic growth",
     "S32  Digital currencies: concepts (money ≠ currency) ⭐",
     "S33  Digital currencies: types & future — closes unit ⭐"],
    ["Unit 1  Introduction (digital/K-economy, 4IR) — done",
     "Unit 2  Fundamentals (platforms, network effects) — done",
     "Unit 3  Digital markets, strategy & innovation — done",
     "Unit 5  Economics of information",
     "Unit 6  Digitalization — the Nepalese perspective"])

# ============================================================ S26
add_divider("Session 26 · Lecture hour 1 (of 8)","Digital Transformation: Concepts",
    "A bank that lets you deposit a cheque photo, a shop that puts its catalogue on Facebook, and a company like eSewa that has NO branches at all — are these the same thing? All three are 'going digital', yet only one has truly transformed. This session gives you the three-tier ladder to tell them apart.",
    "OPENING HOOK [~5 min]. Draw out that 'going digital' means three different depths of change. Agenda: what DT is → digitization vs digitalization vs DT → why DT is survival, not fashion.")

concept_understand("S26 · Concept 1 · [THEORY]","What Digital Transformation Is",
    "Digital transformation (DT) is the deep change in how an organisation operates and delivers value by using digital technology — not just adding an app, but rethinking its processes, business model, and culture. It is about doing NEW things in new ways, not doing old things slightly faster. The technology is the tool; the transformation is the changed way of creating value.",
    ["It changes three things: processes (how work is done), the business model (how value is made), and culture (how people think).",
     "It is customer-driven: the goal is better, faster, cheaper value for users — not technology for its own sake.",
     "It is continuous, not a one-off IT project — the organisation keeps adapting.",
     "Doing old things faster is not DT; reinventing WHAT you do and HOW you earn is."],
    None,"DT = rethink processes + business model + culture with digital tools — new value, not old work sped up.",
    "~7 min. Stress: adding software is not automatically transformation. The change is in the value model, not the gadget.")
add_examples_table("S26 · Concept 1 · examples","Before → after: what transformation looks like by domain",
    ["Domain","Before (traditional)","After (transformed)","The gain"],
    [["Banking","Queue at a branch, fill paper forms","Mobile banking, eSewa/Khalti, QR pay","Anytime access, no travel"],
     ["Shopping","Visit shops in New Road","Order on Daraz, delivered home","Wider choice, convenience"],
     ["Taxi","Wave down a taxi, haggle fare","Book on Pathao/InDrive, fixed fare","Transparent price, tracked ride"],
     ["Food","Phone the restaurant, go collect","Order on Foodmandu, live tracking","Speed, more restaurants reachable"],
     ["Education","Only in-person classes","HamroPathshala, online notes & video","Reach beyond the classroom"],
     ["Government","Queue with photocopies","Nagarik App, online passport/PAN","Fewer trips, faster service"]],
    per_page=6,widths=[1.3,2.3,2.4,2.0],fs=10.5,
    note="Notice each 'after' is not the old task done faster — it is a NEW way of delivering the value (self-service, at home, on a phone). That reinvention is what makes it transformation.")
concept_apply("S26 · Concept 1 · [THEORY]","What Digital Transformation Is",
    "eSewa did not just put a bank branch online — it created a way to pay bills, send money, and buy top-ups with no branch, no form, and no cash, reshaping how millions of Nepalis handle money. A shop that merely posts photos on Facebook has added a channel; eSewa changed the whole value model. That difference — new value model vs a new channel — is digital transformation.",
    "\"Digital transformation just means buying new software or making an app.\" Tools alone are not DT: a bank with a clunky app that still forces branch visits has digitized, not transformed. DT is the changed way of creating value — processes, model, and culture — that the tools enable.",
    "Digital transformation is the deep change in how an organisation operates and delivers value using digital technology — rethinking its processes, business model, and culture, not merely adding software. It means doing new things in new ways (self-service, at-home, phone-first) rather than doing old things faster. It is customer-driven and continuous. eSewa handling money with no branches illustrates a changed value model, not just a new channel.",
    "digital transformation · processes · business model · culture · new value not old work sped up · customer-driven")

concept_understand("S26 · Concept 2 · [THEORY]","Digitization vs Digitalization vs DT",
    "Three words look alike but mean different depths of change. Digitization converts information from analog to digital — paper to PDF, a ledger to Excel (about DATA). Digitalization uses digital tech to improve a PROCESS — online booking instead of a phone call (about WORKFLOW). Digital transformation reinvents the whole BUSINESS MODEL and culture around digital (about the ORGANISATION). Each tier builds on the one before.",
    ["Digitization = data: make information machine-readable (scan, type, upload).",
     "Digitalization = process: automate or improve a workflow with that data (e-payment, e-forms).",
     "Digital transformation = model: change what the organisation is and how it earns value.",
     "They are a ladder: you usually digitize before you digitalize before you transform."],
    "s26_three_tier.png","Digitization = DATA · digitalization = PROCESS · transformation = BUSINESS MODEL (ascending ladder).",
    "~8 min. Use the ladder diagram. The exam trap is treating the three as synonyms — hammer data vs process vs model.")
add_comparison_table("S26 · Concept 2 · comparison","Digitization vs digitalization vs digital transformation",
    ["Dimension","Digitization","Digitalization","Digital transformation"],
    [["What changes","Data (analog → digital)","A process / workflow","The whole business model & culture"],
     ["Scope","A single file or record","A department or task","The entire organisation"],
     ["Question it answers","Is our info digital?","Is this process better with tech?","How do we create value now?"],
     ["Nepal example","Scanning land records to PDF","NEA online bill payment","eSewa: banking with no branches"],
     ["Effort / risk","Low","Medium","High — but survival-level"]],
    per_page=5,widths=[1.7,2.0,2.0,2.6],fs=10.5,
    note="A common exam question asks you to place an example in the right tier: 'PDF of a form' = digitization; 'pay that form's fee online' = digitalization; 'the service is redesigned to need no form at all' = transformation.")
concept_apply("S26 · Concept 2 · [THEORY]","Digitization vs Digitalization vs DT",
    "Take a Nepali municipality. Scanning old paper land records into PDFs is digitization (data). Letting citizens pay property tax online instead of queueing is digitalization (process). Redesigning the office so services are delivered end-to-end through the Nagarik App with no paper trip at all would be digital transformation (model). Same office, three depths of change.",
    "\"Digitization, digitalization and transformation are just fancy synonyms.\" They are distinct tiers: data vs process vs business model. Calling a scanned PDF a 'digital transformation' overstates it — it is only digitization. Naming the correct tier is exactly what exam questions test.",
    "The three differ by depth. Digitization converts information from analog to digital (data): scanning records to PDF. Digitalization uses digital tech to improve a process (workflow): online tax payment. Digital transformation reinvents the business model and culture (organisation): a service redesigned to need no paper at all. They form a ladder — digitize, then digitalize, then transform — and misplacing an example on it is the classic error.",
    "digitization (data) · digitalization (process) · digital transformation (model) · the ladder · place the example")

concept_understand("S26 · Concept 3 · [THEORY]","Why DT Is Survival, Not Fashion",
    "Digital transformation is not optional decoration — it is 'transform or die'. Firms that ignored digital shifts were destroyed by ones that embraced them: Kodak invented the digital camera but clung to film; Nokia dominated phones but missed the smartphone platform shift; Blockbuster passed on buying Netflix. The lesson: a strong incumbent that fails to change its model can be wiped out fast by a digital-native rival.",
    ["Technology shifts change WHAT customers want — and how fast they switch.",
     "Incumbents fail not from lack of tech but from failure to change the business MODEL.",
     "Digital-native rivals scale quickly (low marginal cost, network effects — Units 1–2).",
     "'We've always done it this way' is the most dangerous sentence in a digital economy."],
    None,"Transform or die: Kodak, Nokia, Blockbuster had the tech but kept the old model — and were wiped out.",
    "~7 min. Misconception-first works here: students assume big firms are safe. Show that size did not save Kodak/Nokia.")
add_examples_table("S26 · Concept 3 · examples","'Transform or die' — cautionary cases",
    ["Firm","What it dominated","What it missed","Outcome"],
    [["Kodak","Photographic film","Went digital too late (invented the digital camera, buried it)","Bankruptcy (2012)"],
     ["Nokia","Mobile phones","The smartphone / app-platform shift","Phone business collapsed"],
     ["Blockbuster","Video rental stores","Streaming; passed on buying Netflix","Closed almost all stores"],
     ["Yahoo","Early web portal & search","Lost to Google's model; missed key deals","Sold off cheaply"],
     ["Toys R Us","Toy retail","E-commerce; tied itself to Amazon","Bankruptcy"],
     ["Local example","A photo-studio / STD-PCO booth","Smartphones & digital printing","Largely vanished in Nepal"]],
    per_page=6,widths=[1.4,2.0,2.9,1.8],fs=10.5,
    note="Every firm here had money, brand, and often the technology itself. What killed them was refusing to change the business MODEL — the exact thing transformation (not digitization) requires.")
concept_apply("S26 · Concept 3 · [THEORY]","Why DT Is Survival, Not Fashion",
    "Nepal has its own version: neighbourhood photo studios and STD/PCO phone booths were everywhere in the 1990s, then smartphones made both obsolete almost overnight. The ones that survived transformed — a photo studio that moved to event videography and digital printing lived; one that kept waiting for film customers closed. Size and history protect no one when the model stops fitting.",
    "\"Big, established companies are safe from digital disruption.\" Kodak, Nokia, Blockbuster and Yahoo were all giants — and all fell, several while HOLDING the very technology that displaced them. Safety comes from changing the business model in time, not from size or past success.",
    "Digital transformation is survival, not fashion: firms that failed to change their business model were destroyed by digital-native rivals despite dominating their markets — Kodak (film), Nokia (phones), Blockbuster (rental), Yahoo, Toys R Us. Several even owned the disrupting technology (Kodak invented the digital camera) but kept the old model. The lesson is 'transform or die': in a digital economy, size and history do not protect a firm that refuses to reinvent how it creates value.",
    "transform or die · incumbent failure · Kodak / Nokia / Blockbuster · model change > technology · size is no shield")

add_activity("S26 — 'Which tier is it?'  ·  ~5 min",
    ["In pairs (2 min): list three digital changes you have seen in a Nepali organisation (bank, campus, shop, office).",
     "Classify each as digitization, digitalization, or digital transformation — and justify.",
     "Name one organisation that risks 'transform or die' if it does not change.",
     "Take 3–4 answers aloud (3 min); check the tier labels are correct (data vs process vs model)."],
    "Good answers: online result-publishing = digitalization; scanning old files = digitization; a campus that becomes fully online/blended with new delivery = transformation. Reward correctly separating data / process / model.",
    "ACTIVITY [~5 min].")
add_quiz("S26 — Quick Check  ·  ~5 min",
    [("Q1.  Scanning paper forms into PDFs (nothing else) is:","q"),
     ("a) ✅ digitization   b) digitalization   c) digital transformation   d) automation","a"),
     ("     Why: only the DATA is made digital; no process or business model changed — that is digitization.","o"),
     ("Q2.  Kodak and Nokia collapsed mainly because they:","q"),
     ("a) lacked technology   b) ✅ failed to change their business MODEL in time   c) were too small   d) had no customers","a"),
     ("     Why: both had the technology (Kodak invented the digital camera) but clung to the old model — 'transform or die'.","o"),
     ("Discussion: name one Nepali organisation on each tier — digitize, digitalize, transform.","o")],
    "QUIZ [~5 min]. Cement the three-tier distinction and the survival logic — the foundation for the rest of the unit.")
add_summary("S26 · Summary  ·  [~2 min]",
    ["Digital transformation = deep change in processes, business model, and culture — new value, not old work sped up.",
     "Three tiers: digitization (data) → digitalization (process) → digital transformation (business model). Place examples correctly.",
     "DT is survival: Kodak, Nokia, Blockbuster had tech and scale but kept the old model — and were wiped out."],
    "Every Nepali organisation you deal with — your bank, campus, municipality — sits somewhere on this ladder, and where it sits predicts whether it thrives or fades. Knowing the tiers lets you diagnose that, whether you advise, build, or invest.",
    "S27 — WHY this change is happening now: the drivers of digital transformation.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S27
add_divider("Session 27 · Lecture hour 2 (of 8)","Drivers of Digital Transformation",
    "Why is EVERY organisation transforming now, and not ten years ago? Cheap smartphones, fierce competition, impatient customers — and then a pandemic that forced a decade of change into a few months. Something is pushing all of them at once. This session names those forces so you can spot them anywhere.",
    "OPENING HOOK [~5 min]. Ask why the rush is happening NOW. Agenda: technological drivers → economic + social drivers → crisis as accelerator (COVID-19).")

concept_understand("S27 · Concept 1 · [THEORY]","Technological Drivers",
    "Technological drivers are the digital advances that make transformation POSSIBLE and cheap. Six matter most: the internet (connects everyone), mobile (a computer in every pocket), cloud (rent computing instead of buying servers), big data (decisions from data), AI (automation and prediction), and IoT (connected devices/sensors). Each lowers the cost and raises the reach of going digital.",
    ["Internet + mobile: near-universal connectivity — even rural Nepal via smartphones.",
     "Cloud: a startup can rent world-class computing cheaply instead of buying servers.",
     "Big data + AI: turn usage into insight, personalisation, and automation.",
     "IoT: sensors and connected devices extend digital into the physical world."],
    "s27_drivers.png","Tech drivers make DT POSSIBLE & cheap: internet · mobile · cloud · big data · AI · IoT.",
    "~7 min. Use the drivers diagram. Frame technology as the ENABLER — it makes DT feasible, but does not by itself force it.")
add_examples_table("S27 · Concept 1 · examples","Technological drivers — and how each enables DT in Nepal",
    ["Technology","What it enables","Nepal example"],
    [["Internet","Always-on connection to services","4G/broadband growth; online banking"],
     ["Mobile","A computer + wallet in every pocket","eSewa/Khalti on smartphones nationwide"],
     ["Cloud","Rent computing, scale cheaply","Startups running on cloud, no server room"],
     ["Big data","Decisions & personalisation from data","Daraz recommendations; ride demand maps"],
     ["AI","Automation, prediction, chat support","Fraud checks; AI chatbots; Nepali NLP tools"],
     ["IoT","Connected sensors & devices","Smart meters; GPS tracking on Pathao rides"]],
    per_page=6,widths=[1.4,2.6,2.6],fs=10.8,
    note="These technologies are ENABLERS — they make transformation cheap and feasible. On their own they do not force change; the economic and social drivers (next) supply the pressure to actually act.")
concept_apply("S27 · Concept 1 · [THEORY]","Technological Drivers",
    "A Nepali startup today can launch a national app without owning a single server: mobile puts it in every pocket, the cloud rents it computing by the hour, and big-data tools tell it who uses what. Fifteen years ago that needed a costly server room and a landline world. The technology stack collapsed the cost of transforming, which is why even small Nepali firms now can.",
    "\"Technology by itself causes digital transformation.\" Technology only makes DT POSSIBLE and affordable; it does not compel a firm to act. Plenty of firms had internet access and still did nothing. The pressure to actually transform comes from economic competition and social expectations — the drivers in the next concept.",
    "Technological drivers are the digital advances that make transformation possible and cheap: the internet (connectivity), mobile (pocket computing and wallets), cloud (rentable, scalable computing), big data (data-driven decisions), AI (automation and prediction), and IoT (connected sensors). Together they collapsed the cost and raised the reach of going digital, which is why even small Nepali firms can now transform. But they are enablers — they do not by themselves force change.",
    "technological drivers · internet · mobile · cloud · big data · AI · IoT · enabler not cause")

concept_understand("S27 · Concept 2 · [THEORY]","Economic & Social Drivers",
    "If technology makes DT possible, economic and social drivers make it NECESSARY. Economic drivers: competition (a digital rival can undercut you), cost pressure (digital is cheaper to run), and the push for productivity and new revenue. Social drivers: changing customer behaviour (people expect mobile, instant, self-service), a young digital-native population, and government policy (Digital Nepal Framework) nudging everyone online.",
    ["Competition: if your rival goes digital and cheaper, you must follow or lose customers.",
     "Cost & productivity: digital processes cut cost per transaction and free up staff.",
     "Customer expectations: users raised on smartphones expect instant, mobile, self-service.",
     "Demographics + policy: a young population and government initiatives push adoption."],
    None,"Economic drivers make DT NECESSARY (competition, cost); social drivers (behaviour, youth, policy) make it EXPECTED.",
    "~8 min. Contrast with C1: tech = possible, economics/society = necessary & expected. Nepal's young population is a strong social driver.")
add_comparison_table("S27 · Concept 2 · comparison","Economic vs social drivers of digital transformation",
    ["Question","Economic drivers","Social drivers"],
    [["Core force","Money & competition","People & expectations"],
     ["Examples","Rival undercuts you; lower cost; new revenue","Mobile-first users; young population; policy"],
     ["What it pressures","Profit and survival","Customer satisfaction and relevance"],
     ["Nepal example","Banks racing to match eSewa/Khalti","Youth expecting QR pay everywhere"],
     ["If ignored","You are undercut and lose market","Customers drift to rivals that feel modern"]],
    per_page=5,widths=[1.9,2.6,2.6],fs=11,
    note="Economic drivers act on the balance sheet (cost, competition, revenue); social drivers act on demand (what customers and citizens now expect). Together they turn 'we could go digital' into 'we must'.")
concept_apply("S27 · Concept 2 · [THEORY]","Economic & Social Drivers",
    "When eSewa and Khalti made phone-based payment normal, traditional Nepali banks faced both drivers at once: economically, a cheaper digital rival was taking transactions (competition + cost); socially, young customers now expected to pay by QR and app, not by queueing (behaviour). The result was a rush of bank apps and Fonepay integration — driven not by new technology (it already existed) but by competition and changed expectations.",
    "\"Firms transform mainly because exciting new technology appears.\" The trigger is usually pressure, not novelty: a cheaper digital competitor, cost-cutting needs, or customers who now expect mobile self-service. Nepal's banks had the technology for years; they moved when eSewa's competition and young users' expectations made standing still unaffordable.",
    "Economic and social drivers make transformation necessary rather than merely possible. Economic drivers act on money and survival — competition (a digital rival undercuts you), cost pressure (digital is cheaper), and the push for productivity and new revenue. Social drivers act on demand — customers who expect mobile, instant, self-service; a young digital-native population; and government policy (Digital Nepal). Nepali banks transformed when eSewa's competition and young users' expectations made inaction costly.",
    "economic drivers (competition, cost, revenue) · social drivers (behaviour, youth, policy) · necessary not just possible")

concept_understand("S27 · Concept 3 · [THEORY]","Crisis as Accelerator: COVID-19",
    "A crisis can compress years of transformation into weeks. COVID-19 is the clearest case: with movement restricted, organisations that had delayed going digital were forced to do it overnight — schools moved to online classes, shops to home delivery, offices to remote work, and payments shifted from cash to wallets and QR to avoid contact. What years of 'we'll do it later' had stalled, the crisis made non-negotiable.",
    ["A crisis removes the 'later' option — digital becomes the only way to keep operating.",
     "COVID forced online classes (HamroPathshala/Zoom), delivery (Foodmandu), and remote work.",
     "Cash fell and QR/wallet payments jumped as people avoided physical contact.",
     "Much of the change stuck: habits formed under the crisis did not fully reverse."],
    None,"Crisis (COVID-19) = accelerator: compressed years of DT into weeks — online class, delivery, remote work, QR pay.",
    "~7 min. Students lived this. Draw out that COVID did not create new tech — it forced adoption of what already existed, and much of it stuck.")
add_examples_table("S27 · Concept 3 · examples","COVID-19 as accelerator — before vs after (Nepal)",
    ["Area","Before COVID","Forced change during COVID","Stuck after?"],
    [["Education","Mostly in-person classes","Online classes, Zoom, HamroPathshala","Partly — blended learning stayed"],
     ["Payments","Cash common; QR growing slowly","QR/wallet surge to avoid cash contact","Yes — QR now everywhere"],
     ["Shopping","Visit shops; delivery a niche","Daraz/Foodmandu delivery mainstream","Yes — habit formed"],
     ["Work","Office-based","Remote / work-from-home","Partly — hybrid remained"],
     ["Health","In-person visits","Tele-consultation trials","Partly"],
     ["Government","Counter service","Push for online services","Slowly continuing"]],
    per_page=6,widths=[1.3,2.1,2.6,1.9],fs=10.5,
    note="COVID created no new technology — it forced adoption of what already existed. The key insight: crises accelerate transformation that drivers had merely made possible, and much of the forced change becomes permanent.")
concept_apply("S27 · Concept 3 · [THEORY]","Crisis as Accelerator: COVID-19",
    "Before 2020 many Nepali shops treated online delivery as optional and many teachers had never run an online class. Within weeks of lockdown, Foodmandu and Daraz deliveries became normal, campuses ran on Zoom, and QR payments jumped as people avoided handling cash. None of this technology was new — the crisis simply removed the option to wait, and a large share of the new habits (QR pay, blended learning) stayed afterwards.",
    "\"COVID caused Nepal's digital transformation.\" COVID accelerated it; it did not create it. The wallets, delivery apps, and video tools all existed beforehand — the crisis forced rapid ADOPTION by removing alternatives. Crises are accelerators of change the ordinary drivers had already made possible, not the original cause.",
    "A crisis can compress years of transformation into weeks by removing the option to delay. COVID-19 is the clearest case: lockdowns forced schools online (Zoom, HamroPathshala), shopping to delivery (Daraz, Foodmandu), offices to remote work, and payments from cash to QR/wallets to avoid contact. Crucially, it created no new technology — it forced adoption of what already existed, and much of the change (QR pay, blended learning, hybrid work) became permanent.",
    "crisis as accelerator · COVID-19 · forced adoption not new tech · online class / delivery / remote / QR · change stuck")

add_activity("S27 — 'Spot the driver'  ·  ~5 min",
    ["In pairs (2 min): pick a Nepali organisation that transformed recently (a bank, campus, shop, government office).",
     "Identify which drivers pushed it: technological, economic, social, and/or crisis.",
     "Decide which driver was the STRONGEST for that case, and why.",
     "Take 3–4 answers aloud (3 min); check each names at least two distinct driver types."],
    "Good answers: banks = economic (competition) + social (expectations); campuses = crisis (COVID) + social; delivery apps = social (behaviour) + crisis. Reward separating 'possible' (tech) from 'necessary' (economic/social/crisis).",
    "ACTIVITY [~5 min].")
add_quiz("S27 — Quick Check  ·  ~5 min",
    [("Q1.  Cloud, mobile, and AI are examples of which driver type?","q"),
     ("a) ✅ technological (they make DT possible)   b) economic   c) social   d) crisis","a"),
     ("     Why: these are enabling technologies — they make transformation feasible and cheap, but do not by themselves force it.","o"),
     ("Q2.  COVID-19 is best described as a driver that:","q"),
     ("a) invented new technology   b) ✅ ACCELERATED adoption of existing digital tools   c) had no effect   d) reversed digitalisation","a"),
     ("     Why: the technology already existed; the crisis forced rapid adoption and much of it became permanent.","o"),
     ("Discussion: which single driver most changed how YOU use digital services?","o")],
    "QUIZ [~5 min]. Separate 'possible' (tech) from 'necessary' (economic/social) and 'accelerated' (crisis).")
add_summary("S27 · Summary  ·  [~2 min]",
    ["Technological drivers (internet, mobile, cloud, big data, AI, IoT) make DT POSSIBLE and cheap — they are enablers.",
     "Economic drivers (competition, cost, revenue) make it NECESSARY; social drivers (behaviour, youth, policy) make it EXPECTED.",
     "Crisis (COVID-19) ACCELERATES it: it forced rapid adoption of existing tools, and much of the change stuck."],
    "These drivers explain why the transformation you see around you is happening now and all at once — and spotting which driver is strongest tells a manager where the pressure (and opportunity) really lies.",
    "S28 — from business change to social good: how DT accelerates the Sustainable Development Goals.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S28
add_divider("Session 28 · Lecture hour 3 (of 8)","Accelerating the SDGs through Digital Transformation",
    "Can a mobile phone help end poverty, improve schooling, or clean up government? The UN's 17 Sustainable Development Goals are the world's to-do list for 2030 — and digital transformation is one of the fastest ways to hit them. But the same technology can leave the unconnected further behind. This session shows both edges.",
    "OPENING HOOK [~5 min]. Ask how a phone could help reach a global goal. Agenda: why DT accelerates the SDGs (5 mechanisms) → the four mapped SDGs → ICT4D and the digital divide.")

concept_understand("S28 · Concept 1 · [THEORY]","Why DT Accelerates the SDGs",
    "The Sustainable Development Goals (SDGs) are 17 UN goals for 2030 (no poverty, quality education, decent work, and so on). Digital transformation accelerates them through five mechanisms: speed (services delivered instantly), reach (services get to remote areas), efficiency (do more with less cost), transparency (digital records reduce corruption), and scalability (one platform serves millions cheaply). These make development goals reachable faster and cheaper than physical-only methods.",
    ["Speed: a payment, a lesson, or a form that once took days now takes seconds.",
     "Reach: mobile networks deliver services to villages with no bank or office.",
     "Efficiency & scalability: one digital platform serves millions at near-zero extra cost.",
     "Transparency: digital records and payments make leakage and corruption harder to hide."],
    "s28_sdg.png","DT accelerates SDGs via 5 mechanisms: speed · reach · efficiency · transparency · scalability.",
    "~7 min. Use the SDG diagram. Anchor each mechanism to a concrete Nepal service before mapping specific goals.")
add_examples_table("S28 · Concept 1 · examples","The five mechanisms — how DT speeds development (Nepal)",
    ["Mechanism","What it does","Nepal example"],
    [["Speed","Delivers a service instantly","Remittance received in minutes via wallet"],
     ["Reach","Extends services to remote areas","Mobile banking where there is no branch"],
     ["Efficiency","More output for less cost/effort","Online tax filing cuts staff & travel"],
     ["Transparency","Digital records reduce leakage","Digital payment of salaries/benefits"],
     ["Scalability","One platform serves millions","HamroPathshala reaching many schools"]],
    per_page=5,widths=[1.6,2.7,2.7],fs=11,
    note="These five mechanisms are WHY digital tools help hit development goals faster than physical-only methods: a village gets a bank, a lesson, or a benefit without a building being built for it.")
concept_apply("S28 · Concept 1 · [THEORY]","Why DT Accelerates the SDGs",
    "A migrant worker's remittance from Malaysia once took days through an agent; via a wallet it now arrives in minutes (speed), reaches a village with no bank (reach), costs less to send (efficiency), leaves a clean record (transparency), and works for millions at once (scalability). That single money transfer touches SDG 1 (poverty) and SDG 8 (decent work) — showing how one digital service advances several goals.",
    "\"Reaching the SDGs mainly needs more buildings — schools, banks, offices.\" Physical build-out is slow and costly; digital delivery reaches people faster and cheaper by removing the need for a physical branch in every village. Digital transformation is a development multiplier, not a substitute for all physical investment but a faster path to reach.",
    "The SDGs are 17 UN goals for 2030. Digital transformation accelerates them through five mechanisms: speed (instant delivery), reach (services to remote areas without a physical branch), efficiency (more output for less cost), transparency (digital records reduce corruption/leakage), and scalability (one platform serves millions at near-zero extra cost). A single digital service — like a wallet remittance — can advance several goals at once (poverty, decent work), making development goals reachable faster and cheaper than physical-only methods.",
    "SDGs · speed · reach · efficiency · transparency · scalability · development multiplier")

concept_understand("S28 · Concept 2 · [THEORY]","The Four Mapped SDGs",
    "Four SDGs connect most directly to digital transformation. SDG 4 (Quality Education): e-learning and online resources widen access — HamroPathshala, online notes. SDG 8 (Decent Work & Growth): the digital economy creates jobs — freelancing, IT services, gig work. SDG 9 (Industry, Innovation & Infrastructure): digital infrastructure and startups build innovation capacity. SDG 16 (Peace, Justice & Strong Institutions): e-governance and digital records improve transparency and service.",
    ["SDG 4 Education: online courses and materials reach students beyond the classroom.",
     "SDG 8 Decent work: IT jobs, freelancing, and platform work expand income.",
     "SDG 9 Innovation: digital infrastructure and startups grow the innovation base.",
     "SDG 16 Institutions: e-governance (Nagarik App) improves transparency and access."],
    None,"Four DT-linked SDGs: 4 education · 8 decent work · 9 innovation · 16 governance.",
    "~8 min. Use the mapping table. For each SDG give the mechanism (from C1) AND the Nepal example so it is concrete.")
add_examples_table("S28 · Concept 2 · examples","SDG × DT mechanism × Nepal example",
    ["SDG","DT mechanism used","Nepal example"],
    [["SDG 4 — Quality education","Reach + scalability","HamroPathshala, online classes & notes"],
     ["SDG 8 — Decent work & growth","Reach + new markets","IT freelancing, gig work, digital jobs"],
     ["SDG 9 — Innovation & infrastructure","Efficiency + scalability","Startup ecosystem; broadband rollout"],
     ["SDG 16 — Strong institutions","Transparency + speed","Nagarik App; online passport/PAN"],
     ["SDG 1 — No poverty (bonus)","Reach + efficiency","Wallet remittances to rural households"],
     ["SDG 3 — Good health (bonus)","Reach","Tele-medicine trials in remote districts"]],
    per_page=6,widths=[2.1,2.2,2.7],fs=10.5,
    note="The syllabus focuses on SDGs 4, 8, 9, 16 — but the mechanisms also touch 1, 3, 5, 10. In an exam, map a goal to a mechanism AND a real Nepal service; a bare list of goals earns fewer marks.")
concept_apply("S28 · Concept 2 · [THEORY]","The Four Mapped SDGs",
    "Nepal's IT-freelancing boom is a live SDG 8 case: young Nepalis earn foreign income on Upwork/Fiverr from home, creating decent work without a factory or emigration. HamroPathshala's online lessons advance SDG 4 by reaching students beyond city classrooms, and the Nagarik App advances SDG 16 by making government records and services accessible and traceable. Each pairs a specific goal with a specific digital service.",
    "\"The SDGs are about aid and charity, not technology.\" Digital transformation is one of the most direct SDG accelerators: it creates decent work (8), widens education (4), builds innovation (9), and strengthens institutions (16). Naming the goal, the mechanism, and a real service is what turns a vague answer into a strong one.",
    "Four SDGs link most directly to digital transformation: SDG 4 (Quality Education) via e-learning reaching students (HamroPathshala); SDG 8 (Decent Work & Growth) via digital jobs and freelancing; SDG 9 (Industry, Innovation & Infrastructure) via digital infrastructure and startups; and SDG 16 (Strong Institutions) via e-governance and digital records (Nagarik App). The mechanisms also touch SDGs 1, 3, 5, 10. A strong answer maps each goal to a mechanism and a real Nepal service.",
    "SDG 4 education · SDG 8 decent work · SDG 9 innovation · SDG 16 institutions · map goal → mechanism → service")

concept_understand("S28 · Concept 3 · [THEORY]","ICT4D and the Digital Divide",
    "ICT4D (Information & Communication Technology for Development) is the deliberate use of digital tools to solve development problems — in education, health, governance, agriculture, and entrepreneurship. But there is a catch: the digital divide. If only the connected and literate benefit, digital transformation can WIDEN inequality — leaving behind those without internet, devices, electricity, or digital skills, especially in rural areas and among women and the poor.",
    ["ICT4D focus areas: education, health, government, agriculture, entrepreneurship.",
     "The digital divide: gaps in access (internet, devices, electricity) and in skills/literacy.",
     "Risk: DT can widen inequality if only the already-connected can use the new services.",
     "Fix: affordable access, local-language content, digital-literacy programs, rural infrastructure."],
    None,"ICT4D = tech FOR development; the digital divide (access + skills gap) can WIDEN inequality if ignored.",
    "~7 min. Balance the optimism of C1–C2: the same tools that accelerate SDGs can exclude the unconnected. Nepal's rural/urban and gender gaps are the local anchor.")
add_comparison_table("S28 · Concept 3 · comparison","DT for the SDGs — benefits vs challenges",
    ["Dimension","Benefit (if done well)","Challenge / risk (if ignored)"],
    [["Access","Services reach remote areas","No internet/electricity excludes rural areas"],
     ["Skills","New digital jobs & literacy","Low digital literacy leaves people behind"],
     ["Equality","Level playing field online","Divide widens between connected & not"],
     ["Cost","Cheaper delivery at scale","Devices & data still unaffordable for many"],
     ["Gender / inclusion","Wider participation possible","Women & marginalised may have less access"]],
    per_page=5,widths=[1.6,2.6,2.8],fs=10.8,
    note="This is the exam nuance: DT is a development ACCELERATOR only if the digital divide is closed. Ignore access and skills, and the same tools deepen the very inequality the SDGs aim to reduce.")
concept_apply("S28 · Concept 3 · [THEORY]","ICT4D and the Digital Divide",
    "An ICT4D win in Nepal: mobile money lets a farmer in a remote district receive payment and check prices without a bank branch. But the divide bites — a household with no smartphone, no reliable electricity, or a member who cannot read the app is excluded, and studies show rural and women users lag in access. So the same wallet that advances SDG 1/8 for the connected can widen the gap for the unconnected unless access and literacy are addressed.",
    "\"Digital transformation automatically reduces inequality.\" It can do the opposite: if only the connected and literate benefit, DT widens the digital divide. Real ICT4D pairs the technology with affordable access, local-language content, and digital-literacy programs so the unconnected are not left further behind.",
    "ICT4D (ICT for Development) is the deliberate use of digital tools to solve development problems across education, health, governance, agriculture, and entrepreneurship. Its key caveat is the digital divide — gaps in access (internet, devices, electricity) and in digital skills/literacy. If only the already-connected benefit, DT can widen inequality, especially for rural, poor, and women users. The fix is affordable access, local-language content, digital-literacy programs, and rural infrastructure, so DT accelerates the SDGs rather than deepening the divide.",
    "ICT4D · focus areas · digital divide (access + skills) · can widen inequality · fix: access, literacy, local content")

add_activity("S28 — 'One phone, three goals'  ·  ~5 min",
    ["In pairs (2 min): pick one digital service used in Nepal (a wallet, HamroPathshala, Nagarik App).",
     "Map it to at least two SDGs, naming the DT mechanism it uses for each.",
     "Name one way the digital divide could stop it from reaching everyone.",
     "Take 3–4 answers aloud (3 min); check each pairs a goal with a mechanism AND names a divide risk."],
    "Good answer: wallet → SDG 1 (reach: rural remittance) + SDG 8 (efficiency: income); divide risk = no smartphone/electricity in remote homes. Reward goal + mechanism + a concrete exclusion.",
    "ACTIVITY [~5 min].")
add_quiz("S28 — Quick Check  ·  ~5 min",
    [("Q1.  Digital records making it harder to hide corruption is which DT mechanism?","q"),
     ("a) speed   b) reach   c) ✅ transparency   d) scalability","a"),
     ("     Why: digital records and payments leave a traceable trail, reducing leakage — the transparency mechanism (SDG 16).","o"),
     ("Q2.  The digital divide means digital transformation can:","q"),
     ("a) always reduce inequality   b) ✅ WIDEN inequality if the unconnected are left out   c) has no effect   d) only helps government","a"),
     ("     Why: if only the connected and literate benefit, gaps in access and skills deepen inequality.","o"),
     ("Discussion: which SDG do you think DT helps Nepal reach fastest, and why?","o")],
    "QUIZ [~5 min]. Reinforce the five mechanisms, the four mapped SDGs, and the digital-divide nuance.")
add_summary("S28 · Summary  ·  [~2 min]",
    ["DT accelerates the SDGs via five mechanisms: speed, reach, efficiency, transparency, scalability.",
     "Four SDGs map most directly: 4 (education), 8 (decent work), 9 (innovation), 16 (institutions) — with real Nepal services.",
     "ICT4D uses tech for development, but the digital divide (access + skills) can WIDEN inequality if ignored."],
    "Whether you work in government, an NGO, or a startup, framing a digital service by the goal it advances and the divide it must close is how you argue for its value — and avoid building something that only helps the already-connected.",
    "S29 — zooming out to the whole economy: how the technological revolution reshapes the world economy.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S29
add_divider("Session 29 · Lecture hour 4 (of 8)","Technological Revolution & the World Economy",
    "You already met the four industrial revolutions in Unit 1 (S6) — steam, electricity, computers, and now the digital/AI Fourth Industrial Revolution. We will NOT re-teach that timeline. The question here is different: HOW does a technological revolution actually rewire the whole world economy — its productivity, its industries, and its jobs?",
    "OPENING HOOK [~5 min]. CROSS-REFERENCE Unit 1 S6 for the 4IR timeline; do NOT re-teach it. Agenda: the revolution→economy link → the platform economy & supply chains → the labour-market shift.")

concept_understand("S29 · Concept 1 · [THEORY]","The Revolution → Economy Link",
    "A technological revolution reshapes the world economy in three linked ways. It raises productivity (the same workers produce far more with digital tools and automation). It creates whole new industries (software, e-commerce, cloud, data, streaming) that did not exist before. And it disrupts or destroys old ones (film, print newspapers, video rental). The economy does not just grow — its STRUCTURE changes, shifting where value and jobs come from.",
    ["Productivity: automation and software let the same labour produce much more.",
     "New industries: entire sectors (cloud, e-commerce, app economy) are born.",
     "Disruption: old industries shrink or vanish (film, print, physical rental).",
     "The structure shifts: value moves from making things to information & services."],
    None,"Revolution → economy: raises productivity + creates NEW industries + disrupts OLD ones → the structure shifts.",
    "~7 min. Cross-ref Unit 1 S6 for the 4IR timeline; here focus on the mechanism linking a revolution to economic change. Contrast old vs new value sources.")
add_examples_table("S29 · Concept 1 · examples","Sector-by-sector: how the digital revolution reshaped Nepal",
    ["Sector","Old model","Digital-era model","Effect"],
    [["Banking","Branch, passbook, cash","Mobile banking, wallets, QR","More access, fewer branch visits"],
     ["Retail","Physical shops only","Daraz, SastoDeal, social commerce","Wider reach, new sellers"],
     ["Transport","Metered / haggled taxis","Pathao, InDrive ride-hailing","Transparent price, gig income"],
     ["Media","Print newspapers, TV","Online news, YouTube, social media","Print declines, creators rise"],
     ["Education","Classroom only","Online courses, HamroPathshala","Reach beyond the classroom"],
     ["Work","Local employment","Global freelancing / remote IT","New foreign-income jobs"]],
    per_page=6,widths=[1.3,2.1,2.4,2.0],fs=10.5,
    note="Each row shows the revolution's three effects at once: productivity up, a new digital industry born, and an old model disrupted. The economy's structure — where income comes from — is what changes.")
concept_apply("S29 · Concept 1 · [THEORY]","The Revolution → Economy Link",
    "Nepal's media sector shows all three effects: online news and YouTube raised how much content one person can produce and distribute (productivity), a creator/streaming industry appeared (new industry), and print-newspaper circulation and classified-ad revenue fell (disruption). The people and money did not vanish — they shifted from printing presses to laptops and phones. That shift in structure, not just growth, is what a revolution does.",
    "\"A technological revolution just makes the economy bigger.\" It changes the economy's STRUCTURE, not only its size: value and jobs move from old sectors (film, print) to new ones (software, e-commerce, streaming). Some industries shrink even as the economy grows — which is why disruption and new-job creation happen together.",
    "A technological revolution reshapes the world economy in three linked ways: it raises productivity (digital tools and automation let the same labour produce much more), creates entirely new industries (cloud, e-commerce, the app economy, streaming), and disrupts or destroys old ones (film, print newspapers, physical rental). The economy does not merely grow — its structure changes, shifting where value and income come from (from making things to information and services), which is why growth and disruption occur together.",
    "revolution → economy · productivity · new industries · disruption of old · structural change not just growth")

concept_understand("S29 · Concept 2 · [THEORY]","The Platform Economy & Global Supply Chains",
    "The digital revolution's signature economic form is the platform economy — value created by connecting groups rather than producing goods (Unit 2). Platforms lower transaction costs and exploit network effects so a few firms coordinate huge global activity: Amazon, Uber, and app stores organise millions of sellers and workers worldwide. Digital tools also rewired global supply chains — orders, tracking, and payments flow instantly across borders, so production is coordinated globally in real time.",
    ["Platform economy: firms create value by MATCHING groups, not making goods (link Unit 2).",
     "Low transaction cost + network effects let a few platforms coordinate global activity.",
     "Global supply chains: digital tracking and payments coordinate production across borders.",
     "A Nepali seller or freelancer can plug into a global platform with just internet."],
    None,"Platform economy = value by connecting, not producing (Unit 2); digital tools coordinate global supply chains in real time.",
    "~8 min. Explicitly link back to Unit 2 (network effects, transaction cost). The new point: platforms and digital supply chains globalise coordination.")
add_comparison_table("S29 · Concept 2 · comparison","Traditional firm vs digital-economy (platform) firm",
    ["Dimension","Traditional firm","Digital-economy / platform firm"],
    [["Source of value","Makes & sells its own goods","Connects groups; users create value"],
     ["Scale limit","Factories, geography, inventory","Software copies freely — near-limitless"],
     ["Reach","Local / national","Global from day one via internet"],
     ["Main asset","Physical plant & stock","Network of users, data, algorithms"],
     ["Nepal example","A manufacturer or retail chain","Daraz / Pathao; a Nepali app going global"]],
    per_page=5,widths=[1.7,2.6,2.8],fs=10.8,
    note="This is Unit 2's platform logic applied at the scale of the whole economy: the revolution's most valuable firms coordinate global activity while owning few physical assets — which is why they scale and globalise so fast.")
concept_apply("S29 · Concept 2 · [THEORY]","The Platform Economy & Global Supply Chains",
    "A Nepali handicraft seller can now list on a global marketplace, receive an order from Europe, and have it tracked and paid for automatically — plugging into a digital supply chain that once needed exporters, agents, and banks. The platform coordinates the matching, payment, and logistics (Unit 2's transaction-cost and network-effect logic), so a tiny producer reaches a global buyer. That coordination, not any factory, is the platform economy's engine.",
    "\"The platform economy is just online shopping.\" It is a structural shift in how value is coordinated: platforms use network effects and low transaction costs (Unit 2) to organise millions of independent sellers, workers, and buyers across borders in real time — something no single traditional firm could do. Online shops are one visible piece of a much larger reorganisation.",
    "The digital revolution's signature economic form is the platform economy — value created by connecting groups rather than producing goods (Unit 2). Low transaction costs and network effects let a few platforms coordinate huge global activity (Amazon, Uber, app stores organising millions of sellers and workers). Digital tools also rewired global supply chains, with orders, tracking, and payments flowing instantly across borders so production is coordinated globally in real time — letting even a small Nepali seller or freelancer plug into global markets with just internet.",
    "platform economy · value by connecting (Unit 2) · low transaction cost + network effects · global supply chains · small player goes global")

concept_understand("S29 · Concept 3 · [THEORY]","The Labour-Market Shift",
    "A revolution reshuffles work: some jobs vanish, new ones appear, and the skills demanded change. Routine and manual jobs (bank tellers, print workers, some clerical roles) shrink through automation; new roles appear (app developers, digital marketers, data analysts, ride/delivery gig workers, freelancers). Work also becomes more flexible and platform-based (the gig economy). The constant demand is for digital skills — those who reskill move up; those who cannot are left behind.",
    ["Jobs vanish: routine, manual, and clerical roles are automated away.",
     "Jobs appear: developers, digital marketers, data analysts, gig & freelance work.",
     "The gig economy: flexible, platform-mediated work (Pathao riders, freelancers).",
     "Digital skills become the dividing line — reskilling decides who gains or loses."],
    None,"Labour shift: routine jobs vanish, digital/gig jobs appear; digital skills decide who gains or loses.",
    "~7 min. Balance: automation destroys AND creates jobs. The net effect depends on reskilling. Nepal's freelancing/gig growth is the local anchor.")
add_examples_table("S29 · Concept 3 · examples","Jobs disappearing vs jobs appearing",
    ["Disappearing / shrinking","Appearing / growing","Why the shift"],
    [["Bank tellers, cashiers","App developers, mobile-bank engineers","Automation moves routine tasks to software"],
     ["Print-press & typesetting","Digital-content creators, YouTubers","Media goes online"],
     ["Travel agents","Digital marketers, SEO/social managers","Booking & promotion move online"],
     ["Manual data-entry clerks","Data analysts, data engineers","Data is captured & processed digitally"],
     ["Traditional taxi dispatch","Ride-hailing gig drivers (Pathao)","Platforms match riders & drivers"],
     ["Local-only jobs","Global freelancers (Upwork/Fiverr)","Internet opens global labour markets"]],
    per_page=6,widths=[2.2,2.5,2.3],fs=10.5,
    note="Automation both destroys and creates jobs — the net outcome for a worker depends on REskilling. This is why digital-skills training is the core policy response to the labour-market shift.")
concept_apply("S29 · Concept 3 · [THEORY]","The Labour-Market Shift",
    "In Nepal the shift is visible: demand for bank-teller and manual data-entry roles is falling, while IT freelancing, digital marketing, and ride/delivery gig work are rising fast. A young person who learns coding, design, or digital marketing can earn foreign income from home; one whose only skill is a now-automated clerical task is squeezed. The technology did not simply cut jobs — it moved them to those with digital skills.",
    "\"Automation and the digital revolution just destroy jobs.\" They destroy some AND create others: routine roles shrink while developer, analyst, creator, and gig roles grow. The real risk is not fewer jobs overall but a SKILLS mismatch — which is why reskilling and digital literacy decide who gains from the shift.",
    "A technological revolution reshuffles the labour market: routine, manual, and clerical jobs (bank tellers, print workers, data-entry clerks) shrink through automation, while new roles appear (app developers, digital marketers, data analysts, gig drivers, global freelancers). Work becomes more flexible and platform-based (the gig economy). The constant demand is for digital skills, which become the dividing line — those who reskill move up, those who cannot are left behind — so reskilling is the key policy response.",
    "labour shift · jobs vanish (routine) · jobs appear (digital/gig) · gig economy · digital skills decide · reskilling")

add_activity("S29 — 'Reshape a sector'  ·  ~5 min",
    ["In pairs (3 min): pick one Nepali sector (banking, media, transport, retail, education).",
     "Name the revolution's three effects there: a productivity gain, a NEW industry/role, and an OLD one disrupted.",
     "Name one job disappearing and one appearing in that sector.",
     "Take 3–4 answers aloud (2 min); check all three effects and the job shift are named."],
    "Good answer (media): productivity = one creator reaches millions; new = YouTube/creator economy; disrupted = print newspapers; job gone = typesetter, job new = content creator. Reward naming all three structural effects.",
    "ACTIVITY [~5 min].")
add_quiz("S29 — Quick Check  ·  ~5 min",
    [("Q1.  A technological revolution changes the economy mainly by:","q"),
     ("a) only making it bigger   b) ✅ changing its STRUCTURE — new industries rise, old ones are disrupted   c) removing all jobs   d) nothing","a"),
     ("     Why: value and jobs shift from old sectors (film, print) to new ones (software, e-commerce) — a structural change.","o"),
     ("Q2.  The platform economy creates value mainly by:","q"),
     ("a) manufacturing goods   b) ✅ connecting groups (network effects, low transaction cost — Unit 2)   c) mining   d) farming","a"),
     ("     Why: platforms match groups rather than produce goods, coordinating global activity — the Unit 2 logic at economy scale.","o"),
     ("Discussion: which Nepali job do you think will change most in the next 5 years?","o")],
    "QUIZ [~5 min]. Reinforce structural change, the Unit 2 platform link, and the destroy-and-create labour shift.")
add_summary("S29 · Summary  ·  [~2 min]",
    ["A revolution reshapes the economy's STRUCTURE: raises productivity, creates new industries, disrupts old ones (4IR timeline is in Unit 1 S6).",
     "The platform economy creates value by connecting groups (Unit 2), and digital supply chains coordinate production globally in real time.",
     "The labour market shifts: routine jobs vanish, digital/gig jobs appear; digital skills and reskilling decide who gains."],
    "This explains why some careers are booming while others fade, and why 'digital skills' appears in every job ad — knowing the direction of the shift lets you position yourself (and any business) on the growing side of it.",
    "S30 — the revolution goes global: traditional vs digital globalization.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S30
add_divider("Session 30 · Lecture hour 5 (of 8)","Globalization in the Digital Age",
    "For centuries, going global meant ships, containers, factories, and huge firms — the preserve of the powerful. Today a single Nepali student with a laptop and internet can sell a service to a client in New York this afternoon. Globalization has changed shape. This session contrasts the old and new kinds and shows where Nepal fits.",
    "OPENING HOOK [~5 min]. Contrast a shipping container with a freelancer's laptop. Agenda: traditional vs digital globalization → e-commerce & digital trade → opportunities, risks, and Nepal's position.")

concept_understand("S30 · Concept 1 · [THEORY]","Traditional vs Digital Globalization",
    "Globalization is the growing interconnection of the world's economies. Traditional globalization moved physical GOODS across borders — slow, costly, dominated by large firms with ships, factories, and trade deals. Digital globalization moves SERVICES, DATA, and SOFTWARE instantly and cheaply, so even individuals and small firms can go global. The barrier fell from 'own a factory and shipping' to 'have a skill and internet'.",
    ["Traditional: physical goods, slow (weeks), costly (shipping, tariffs), big firms.",
     "Digital: services/data/software, instant, near-zero cost, open to individuals.",
     "The gatekeeper changed: capital & logistics → skills & connectivity.",
     "Both coexist — but the digital kind grows fastest and includes the smallest players."],
    "s30_globalization.png","Traditional globalization = physical goods, slow, big firms; digital = services/data, instant, anyone.",
    "~7 min. Use the contrast diagram. The headline: digital globalization lets a small player go global with skills + internet, not capital + factories.")
add_comparison_table("S30 · Concept 1 · comparison","Traditional vs digital globalization",
    ["Dimension","Traditional globalization","Digital globalization"],
    [["What crosses borders","Physical goods","Services, data, software"],
     ["Speed","Weeks to months","Instant / seconds"],
     ["Cost to participate","High (shipping, tariffs, capital)","Low (internet + a skill)"],
     ["Who can play","Large firms with resources","Individuals & small firms too"],
     ["Main enabler","Ships, ports, trade deals","Internet, platforms, digital payments"],
     ["Nepal example","Carpet / garment export","IT freelancing; software export"]],
    per_page=6,widths=[1.8,2.5,2.6],fs=10.8,
    note="The core shift: the ticket to global markets changed from capital + logistics to skills + connectivity — which is exactly why digital globalization is a chance for a small, landlocked economy like Nepal.")
concept_apply("S30 · Concept 1 · [THEORY]","Traditional vs Digital Globalization",
    "Nepal's exports show both kinds. Traditional: carpets and garments shipped abroad — valuable but slow, capital-heavy, and hard for a small player to enter. Digital: a Nepali freelancer designs a logo for a US client and delivers it online the same day, with no container, customs, or factory. The second needs only a skill and internet — which is why digital globalization opens the world economy to Nepalis who could never afford the traditional route.",
    "\"Globalization is only for big exporting companies.\" That was traditional globalization. Digital globalization lets an individual with a skill and internet trade services worldwide instantly — the barrier fell from capital and logistics to connectivity. This is why 'go global' is now realistic advice for a Nepali student, not just a corporation.",
    "Globalization is the growing interconnection of the world's economies. Traditional globalization moved physical goods across borders — slow, costly, and dominated by large firms with ships, factories, and trade deals. Digital globalization moves services, data, and software instantly and cheaply, so individuals and small firms can go global. The gatekeeper changed from capital and logistics to skills and connectivity. Both coexist, but the digital kind grows fastest and includes the smallest players — a real opening for landlocked Nepal.",
    "globalization · traditional (goods, slow, big firms) · digital (services/data, instant, anyone) · skills + internet")

concept_understand("S30 · Concept 2 · [THEORY]","E-commerce & Digital Trade",
    "E-commerce is buying and selling online, and it comes in three main types by who trades with whom: B2C (business to consumer — Daraz to a shopper), B2B (business to business — a wholesaler supplying retailers online), and C2C (consumer to consumer — Hamrobazar between individuals). Digital trade is the broader flow across borders — not just goods, but services (freelancing), digital products (software, e-books), and data.",
    ["B2C: a business sells to consumers (Daraz, SastoDeal, Foodmandu).",
     "B2B: a business sells to another business (online wholesale, supplier portals).",
     "C2C: consumers sell to each other via a platform (Hamrobazar, marketplace groups).",
     "Digital trade = cross-border flow of goods + services + digital products + data."],
    None,"E-commerce types: B2C · B2B · C2C. Digital trade = cross-border flow of goods, services, digital products & data.",
    "~8 min. Use the types table. Distinguish e-commerce (transactions) from digital trade (the broader cross-border flow, incl. services & data).")
add_examples_table("S30 · Concept 2 · examples","E-commerce types & digital trade — Nepal examples",
    ["Type","Who trades","Nepal example","What flows"],
    [["B2C","Business → consumer","Daraz, SastoDeal, Foodmandu","Goods, food to shoppers"],
     ["B2B","Business → business","Wholesale/supplier portals","Bulk goods between firms"],
     ["C2C","Consumer → consumer","Hamrobazar, marketplace groups","Second-hand goods"],
     ["Services trade","Freelancer → global client","Upwork/Fiverr Nepali freelancers","IT, design, writing services"],
     ["Digital products","Creator → buyer","Apps, e-books, online courses","Software & content"],
     ["Data flow","Platform ↔ platform","Cloud, payment, analytics data","Data across borders"]],
    per_page=6,widths=[1.5,1.9,2.3,2.0],fs=10.5,
    note="E-commerce is the transaction (B2C/B2B/C2C); digital trade is the wider cross-border flow that also includes services, digital products, and data — the part where Nepal earns foreign income without exporting a single physical good.")
concept_apply("S30 · Concept 2 · [THEORY]","E-commerce & Digital Trade",
    "In one week a Nepali might buy shoes on Daraz (B2C), sell an old phone on Hamrobazar (C2C), and complete a freelance design job for a foreign client (services trade). The first two are domestic e-commerce; the third is cross-border digital trade that brings foreign currency into Nepal with no shipping. Recognising which type is which matters for policy — services and digital-product trade is where a landlocked country can compete.",
    "\"E-commerce and digital trade are the same thing.\" E-commerce is the online transaction (B2C, B2B, C2C); digital trade is the broader cross-border flow that also covers services (freelancing), digital products, and data. Nepal's biggest digital opportunity is in services trade — which a narrow 'e-commerce = online shops' view would miss.",
    "E-commerce is buying and selling online, in three main types by who trades: B2C (business to consumer — Daraz), B2B (business to business — online wholesale), and C2C (consumer to consumer — Hamrobazar). Digital trade is the broader cross-border flow — not just goods, but services (freelancing), digital products (software, e-books, courses), and data. For a landlocked economy like Nepal, cross-border services and digital-product trade is the biggest opportunity, earning foreign income without exporting physical goods.",
    "e-commerce · B2C · B2B · C2C · digital trade · services & data flow · services trade is Nepal's opening")

concept_understand("S30 · Concept 3 · [THEORY]","Opportunities, Risks & Nepal's Position",
    "For a developing, landlocked country, digital globalization is a rare equaliser: Nepalis can earn foreign income through IT freelancing and software export with 'skills and internet, no factory' — no port or heavy capital needed. But there are risks: dependence on foreign platforms and payment systems, exposure to global competition, data and privacy concerns, and the digital divide leaving many unable to participate. Nepal's position is a service-provider with real potential if skills and connectivity spread.",
    ["Opportunity: 'growth without factories' — IT/BPO/freelancing export foreign income.",
     "Nepal as a service-provider: BIM/IT graduates fill developer, design, support roles.",
     "Risks: platform & payment dependence, global competition, data/privacy, the divide.",
     "Verdict: strong potential IF digital skills, connectivity, and payment access spread."],
    None,"Nepal's chance: 'skills + internet, no factory' foreign income; risks: platform dependence, competition, divide.",
    "~7 min. This is the hopeful-but-balanced close. Tie 'growth without factories' to BIM-graduate careers; note the risks so it is not naive optimism.")
add_comparison_table("S30 · Concept 3 · comparison","Digital globalization for Nepal — opportunity vs risk",
    ["Area","Opportunity","Risk / challenge"],
    [["Income","Foreign earnings via IT & freelancing","Volatile, platform-dependent income"],
     ["Entry cost","No factory/port needed — skills + internet","Requires reliable internet & electricity"],
     ["Jobs","New roles for BIM/IT graduates","Global competition undercuts local rates"],
     ["Payments","Access to global clients","Hard to receive money (limited gateways)"],
     ["Inclusion","Rural youth can participate","Digital divide excludes the unconnected"],
     ["Control","Reach global markets","Dependence on foreign platforms & rules"]],
    per_page=6,widths=[1.5,2.6,2.7],fs=10.8,
    note="Digital globalization is a genuine equaliser for a landlocked economy — but the opportunity is only realised if the risks (payment access, connectivity, the divide, platform dependence) are managed. This frames Nepal's realistic position.")
concept_apply("S30 · Concept 3 · [THEORY]","Opportunities, Risks & Nepal's Position",
    "A BIM or IT graduate in Kathmandu can build a career serving foreign clients — coding, design, digital marketing, support — bringing foreign currency into Nepal without any factory or export licence: 'growth without factories'. But the same graduate faces real friction: getting paid from abroad is hard with limited payment gateways, global freelancers undercut rates, and a classmate in a village with poor internet may be shut out entirely. Nepal's position is promising but conditional.",
    "\"Digital globalization automatically lifts a poor country's economy.\" The opportunity is real but conditional: it needs digital skills, reliable connectivity and electricity, and working cross-border payments, and it carries risks (platform dependence, competition, the divide). Nepal benefits only if it builds the enablers — otherwise the gains concentrate among the already-connected.",
    "For a developing, landlocked country, digital globalization is a rare equaliser: Nepalis can earn foreign income through IT freelancing and software/service export with 'skills and internet, no factory' — no port or heavy capital needed, opening careers for BIM/IT graduates as a service-provider economy. But it carries risks: dependence on foreign platforms and payment systems, exposure to global competition, data/privacy concerns, and a digital divide excluding many. Nepal's position holds strong potential conditional on spreading skills, connectivity, and payment access.",
    "developing-country opportunity · growth without factories · service-provider · risks: dependence, competition, divide · conditional")

add_activity("S30 — 'Nepal goes global'  ·  ~5 min",
    ["In pairs (3 min): design a way a Nepali could earn foreign income digitally (a service, product, or platform).",
     "Classify it: is it services trade, digital-product trade, or e-commerce? Which e-commerce type if any?",
     "Name one opportunity and one risk for Nepal in your idea.",
     "Take 3–4 answers aloud (2 min); check the trade type and a real risk are named."],
    "Good answers: freelance app development (services trade; opportunity = foreign income, risk = payment gateways); selling handicrafts abroad on a marketplace (B2C/cross-border; risk = logistics). Reward naming the trade type + a concrete risk.",
    "ACTIVITY [~5 min].")
add_quiz("S30 — Quick Check  ·  ~5 min",
    [("Q1.  The key difference between traditional and digital globalization is that digital:","q"),
     ("a) is slower   b) ✅ moves services/data instantly and is open to individuals & small firms   c) needs bigger factories   d) is only for rich countries","a"),
     ("     Why: digital globalization moves services/data/software cheaply and instantly, so even a small player with internet can go global.","o"),
     ("Q2.  A Nepali freelancer coding for a US client is an example of:","q"),
     ("a) B2C e-commerce   b) traditional export   c) ✅ cross-border digital (services) trade   d) C2C","a"),
     ("     Why: it is a service delivered across borders online — digital trade in services, Nepal's biggest digital opportunity.","o"),
     ("Discussion: what is Nepal's single best digital-export opportunity, and its biggest risk?","o")],
    "QUIZ [~5 min]. Reinforce traditional vs digital, the e-commerce/digital-trade distinction, and Nepal's service-provider position.")
add_summary("S30 · Summary  ·  [~2 min]",
    ["Traditional globalization moves physical goods (slow, costly, big firms); digital moves services/data instantly and includes individuals.",
     "E-commerce comes in B2C / B2B / C2C; digital trade is the wider cross-border flow of goods, services, digital products, and data.",
     "Nepal's chance is 'growth without factories' (IT/freelancing foreign income); risks are platform dependence, competition, and the divide."],
    "For a landlocked country with a young, English-capable workforce, digital globalization is one of the most realistic paths to prosperity — and understanding it shapes your own career choices as much as national policy.",
    "S31 — from global reach to national wealth: how digital transformation drives economic growth.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S31
add_divider("Session 31 · Lecture hour 6 (of 8)","Digital Transformation & Economic Growth",
    "eSewa owns no bank vaults, Pathao owns no cars, and a freelancer owns no factory — yet together they add real money to Nepal's economy. How does an economy GROW when so little of it is physical? This session traces the path from digital skills to GDP, and the engines that make digital growth scale.",
    "OPENING HOOK [~5 min]. Ask how the economy grows without factories. Agenda: the digital economy & GDP → the growth engines (low marginal cost + network effects) → government's role & the digital divide.")

concept_understand("S31 · Concept 1 · [THEORY]","The Digital Economy & GDP",
    "GDP is the total value of goods and services a country produces. The digital economy adds to GDP through a chain: digital skills create jobs and businesses → those generate income and exports → income is spent and reinvested → GDP grows. Crucially, this value is often intangible (services, software, data) rather than physical goods, so an economy can grow without building more factories — which suits a small, landlocked country.",
    ["Chain: skills → jobs & businesses → income & exports → spending/reinvestment → GDP.",
     "Digital value is often intangible: services, software, data — not physical output.",
     "Foreign income (IT export, freelancing, remittance via wallets) adds directly to GDP.",
     "Growth can happen without heavy physical investment — an advantage for Nepal."],
    "s31_growth_flow.png","Growth chain: digital skills → jobs → income & exports → GDP. Value is often intangible, not physical.",
    "~7 min. Use the growth-flow diagram. Emphasise the intangible-value point: GDP can rise from services/software, not only factories.")
add_examples_table("S31 · Concept 1 · examples","How digital activity adds to Nepal's GDP",
    ["Digital activity","How it adds value","GDP contribution"],
    [["IT freelancing / BPO","Foreign clients pay Nepali workers","Foreign-currency income"],
     ["E-commerce (Daraz etc.)","New sales, delivery & seller jobs","Trade + employment"],
     ["Digital payments (eSewa)","Faster, cheaper transactions","Efficiency + financial inclusion"],
     ["Ride/delivery platforms","Gig income for many workers","New employment & spending"],
     ["Remittance via wallets","Migrant income reaches households fast","Large inflow to households/GDP"],
     ["Software / app startups","Products sold at home & abroad","New industry & exports"]],
    per_page=6,widths=[2.0,2.6,2.0],fs=10.5,
    note="Most of these add value WITHOUT producing a physical good — services, payments, and software. That is why the digital economy lets a country grow GDP faster than its factory capacity alone would allow.")
concept_apply("S31 · Concept 1 · [THEORY]","The Digital Economy & GDP",
    "Trace one Nepali freelancer: she learns web development (skill), takes foreign clients (job/export), earns dollars paid into Nepal (income), and spends locally on rent, food, and a new laptop (reinvestment/spending). Multiply by thousands of freelancers, Pathao drivers, and Daraz sellers, and the digital economy is adding measurable value to GDP — none of it from a new factory. That is how an economy grows on skills and services.",
    "\"An economy can only grow by producing more physical goods.\" Much of modern GDP is services, software, and data — intangible value. A country can raise GDP through digital skills, IT export, and platform activity without building factories, which is exactly why the digital economy matters most to small, resource-limited nations like Nepal.",
    "GDP is the total value of goods and services a country produces. The digital economy adds to it through a chain: digital skills create jobs and businesses; these generate income and exports; income is spent and reinvested; GDP grows. Much of this value is intangible — services, software, data, digital payments — rather than physical output, so an economy can grow without building more factories. Foreign income from IT export, freelancing, and wallet-based remittances adds directly to GDP, which particularly suits a small, landlocked country.",
    "GDP · skills → jobs → income → GDP chain · intangible value · growth without factories · foreign income adds directly")

concept_understand("S31 · Concept 2 · [THEORY]","Growth Engines: Low Marginal Cost & Network Effects",
    "Digital growth scales because of engines you met in Unit 2. Low marginal cost: once built, serving one more user costs almost nothing, so a digital business can grow revenue far faster than costs. Network effects: each new user makes the platform more valuable, pulling in more users. Add continuous innovation (new products cheaply) and digital finance (wallets bring the unbanked into the economy), and digital growth compounds in a way physical growth cannot.",
    ["Low marginal cost: revenue can scale while cost barely rises (Unit 2).",
     "Network effects: more users → more value → more users — growth feeds itself (Unit 2).",
     "Innovation: new digital products/services launch cheaply and fast.",
     "Digital finance: wallets bring the unbanked in, widening the economy's base."],
    None,"Digital-growth engines: low marginal cost + network effects (Unit 2) + innovation + digital finance → growth compounds.",
    "~8 min. Explicitly recall Unit 2 (marginal cost, network effects) as the ENGINES of macro growth. Digital finance/inclusion is the fresh addition.")
add_examples_table("S31 · Concept 2 · scaffolding","Growth engine × how it works × Nepal example",
    ["Growth engine","How it drives growth","Nepal example"],
    [["Low marginal cost","Revenue scales while cost barely rises","eSewa: one more user is near-free to serve"],
     ["Network effects","More users → more value → more users","Fonepay accepted almost everywhere"],
     ["Innovation","New digital products launch cheaply","New app features, fintech services"],
     ["Digital finance","Brings the unbanked into the economy","Wallets reaching rural/unbanked users"],
     ["Data","Better products & targeting from usage","Daraz recommendations lift sales"]],
    per_page=5,widths=[1.8,2.6,2.6],fs=11,
    note="These are Unit 2's platform economics acting as MACRO growth engines: they let digital output — and therefore GDP contribution — expand far faster than the physical inputs, which is the essence of digital-age growth.")
concept_apply("S31 · Concept 2 · [THEORY]","Growth Engines: Low Marginal Cost & Network Effects",
    "eSewa shows the engines compounding: after the platform is built, each new Nepali user costs almost nothing to serve (low marginal cost), yet each one makes the wallet more useful to merchants and vice versa (network effects), while new features (payments, credit, remittance) add revenue cheaply (innovation) and bringing unbanked users in widens the whole market (digital finance). Revenue and economic contribution scale far faster than costs — growth a physical business could never match.",
    "\"Digital businesses grow just like any other business — a bit at a time.\" Digital growth COMPOUNDS: near-zero marginal cost plus network effects mean value and revenue can scale explosively while costs barely move. This is why a digital firm can contribute to GDP out of all proportion to its physical size — the Unit 2 engines operating at economy scale.",
    "Digital growth scales because of engines from Unit 2. Low marginal cost means serving one more user costs almost nothing, so revenue scales far faster than cost. Network effects mean each new user makes the platform more valuable, pulling in more users so growth feeds itself. Continuous innovation launches new digital products cheaply, and digital finance (wallets) brings the unbanked into the economy, widening its base. Together these make digital growth compound in a way physical growth cannot — the essence of digital-age economic growth.",
    "growth engines · low marginal cost · network effects (Unit 2) · innovation · digital finance/inclusion · growth compounds")

concept_understand("S31 · Concept 3 · [THEORY]","Government's Role & the Digital Divide",
    "Digital growth is not automatic — government must build the enablers and manage the risks. It provides infrastructure (broadband, electricity, digital ID, payment rails) and policy (the Digital Nepal Framework, e-governance, skills programs) that let the private engines run. But growth can be uneven: the digital divide means the connected and skilled capture most gains while the rural, poor, and unconnected are left behind — so inclusive growth requires deliberately closing that divide.",
    ["Government supplies infrastructure: broadband, electricity, digital ID, payment rails.",
     "Policy: Digital Nepal Framework, e-governance, and digital-skills programs.",
     "Without inclusion, growth concentrates among the already-connected (the divide).",
     "Inclusive digital growth = private engines + public infrastructure + closing the divide."],
    None,"Government builds enablers (broadband, ID, policy — Digital Nepal); the digital divide can make growth uneven.",
    "~7 min. Tie growth to the enabling role of the state and to inclusion. Note Digital Nepal Framework here but keep policy DEPTH for Unit 6.")
add_comparison_table("S31 · Concept 3 · comparison","Who benefits from digital growth — and the digital divide",
    ["Group","Gains from digital growth","Left behind by the divide"],
    [["Urban, connected youth","Freelancing, gig, e-commerce income","—"],
     ["Rural households","Wallet remittance, mobile banking","Poor internet/electricity limits access"],
     ["Women & marginalised","New online participation possible","Lower device access & digital literacy"],
     ["Small businesses","Reach customers online cheaply","Lack skills/tools to go digital"],
     ["Unconnected / illiterate","—","Excluded from most digital gains"]],
    per_page=5,widths=[1.9,2.5,2.6],fs=10.8,
    note="Digital growth is real but not automatically inclusive. Government infrastructure and skills programs exist precisely to widen who benefits — otherwise the divide concentrates gains among the already-connected.")
concept_apply("S31 · Concept 3 · [THEORY]","Government's Role & the Digital Divide",
    "Nepal's growth story needs both sides: private engines (eSewa, Pathao, freelancers) generate value, but they only reach a village if the government has extended broadband and electricity, issued a usable digital ID, and enabled cross-border payments — the Digital Nepal Framework's aim. Where those enablers are missing, growth pools in Kathmandu and among the connected, and a rural or unconnected household is left out. Inclusive growth is a public-plus-private job.",
    "\"Digital economic growth happens on its own once businesses go digital.\" Private platforms need public rails — broadband, electricity, digital ID, payments — and deliberate inclusion, or growth concentrates among the connected and the divide widens. Government is not a bystander to digital growth; it builds the foundation the engines run on.",
    "Digital growth is not automatic — government must build the enablers and manage the risks. It provides infrastructure (broadband, electricity, digital ID, payment rails) and policy (the Digital Nepal Framework, e-governance, digital-skills programs) that let the private growth engines run. But growth can be uneven: the digital divide means the connected and skilled capture most gains while rural, poor, and unconnected people are left behind. Inclusive digital growth therefore requires private engines plus public infrastructure plus deliberately closing the divide.",
    "government role · infrastructure (broadband, ID, payments) · Digital Nepal Framework · digital divide · inclusive growth")

add_activity("S31 — 'Trace the growth'  ·  ~5 min",
    ["In pairs (3 min): pick a Nepali digital business (eSewa, Pathao, a freelancer, a startup).",
     "Trace its growth chain: skills → jobs → income → GDP, naming each step for that case.",
     "Name which growth engine it relies on most, and one government enabler it needs.",
     "Take 3–4 answers aloud (2 min); check the chain and an engine are named."],
    "Good answer (freelancer): skill = coding; job = foreign client; income = dollars into Nepal; GDP = spending/export; engine = low marginal cost of a laptop service; enabler = internet + payment gateway. Reward the full chain + an engine.",
    "ACTIVITY [~5 min].")
add_quiz("S31 — Quick Check  ·  ~5 min",
    [("Q1.  The digital economy lets a country grow GDP without:","q"),
     ("a) any workers   b) ✅ building more physical factories (much value is intangible services/software)   c) money   d) skills","a"),
     ("     Why: services, software, and data are intangible value — GDP can rise from them without physical production.","o"),
     ("Q2.  'Serving one more user costs almost nothing' is which growth engine?","q"),
     ("a) network effects   b) ✅ low marginal cost   c) digital divide   d) taxation","a"),
     ("     Why: near-zero marginal cost lets revenue scale far faster than cost — a core digital-growth engine (Unit 2).","o"),
     ("Discussion: what single government enabler would most boost Nepal's digital growth?","o")],
    "QUIZ [~5 min]. Reinforce the growth chain, the Unit 2 engines, and the public-plus-private inclusion point.")
add_summary("S31 · Summary  ·  [~2 min]",
    ["The digital economy grows GDP via skills → jobs → income → GDP, and much of the value is intangible — growth without factories.",
     "Growth engines are low marginal cost + network effects (Unit 2), plus innovation and digital finance — so digital growth compounds.",
     "Government builds the enablers (broadband, ID, payments, Digital Nepal); the digital divide can make growth uneven and must be closed."],
    "This is why 'digital economy' appears in national plans: for Nepal it is a realistic growth path that needs skills and public infrastructure more than capital — and knowing the engines tells you where growth and policy should focus.",
    "S32 — the unit's richest block begins: digital currencies, and why eSewa is money but not a currency.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S32
add_divider("Session 32 · Lecture hour 7 (of 8) — the most exam-weighted block","Digital Currencies: Concepts",
    "You pay with eSewa every day — so is eSewa a 'digital currency'? Almost everyone says yes, and almost everyone is WRONG. The distinction between digital MONEY and a digital CURRENCY is the single most exam-worthy idea in this unit. This session builds it from the ground up: the story of money, then the precise definitions.",
    "OPENING HOOK [~5 min]. Provoke: 'is eSewa a digital currency?' Most say yes — hold it. Agenda: the evolution of money → what a digital currency is → digital money ≠ digital currency (eSewa vs crypto).")

concept_understand("S32 · Concept 1 · [THEORY]","The Evolution of Money",
    "Money evolved through five stages, each less physical than the last. Barter (goods swapped for goods — needs a 'double coincidence of wants'). Commodity/coins (metal with agreed value). Paper money (notes issued by a central authority — Nepal's NRB rupee). Bank money (account balances, cheques, cards — money as a record). Digital money (electronic balances in wallets and apps — eSewa, mobile banking). The form kept changing; what backs it — trust in the issuer — stayed the point.",
    ["Barter → coins → paper → bank money → digital money: steadily less physical.",
     "Each stage solved a problem of the last (barter's double-coincidence, coins' weight).",
     "Money is anything widely accepted as a medium of exchange, store of value, unit of account.",
     "Digital money is the newest FORM — but it still represents the same issued currency."],
    "s32_money_evolution.png","Money's evolution: barter → coins → paper → bank → digital. Less physical, same core: trusted issuer.",
    "~7 min. Use the evolution timeline. Land the theme: form changed (physical → digital), but a wallet still holds the SAME NRB rupee — the bridge to Concept 3.")
add_examples_table("S32 · Concept 1 · scaffolding","Stages of money — and why each emerged",
    ["Stage","What it is","Problem it solved","Nepal link"],
    [["Barter","Goods swapped for goods","—","Traditional village exchange"],
     ["Coins","Metal with set value","Barter's double-coincidence of wants","Historic coins"],
     ["Paper money","Notes from an authority","Coins heavy & scarce","NRB rupee notes"],
     ["Bank money","Account balances, cheques, cards","Carrying/storing cash safely","Bank accounts, debit cards"],
     ["Digital money","Electronic balances in wallets","Speed, distance, convenience","eSewa, Khalti, mobile banking"]],
    per_page=5,widths=[1.4,2.1,2.3,2.0],fs=10.8,
    note="Each stage made money less physical and easier to move. Digital money is the latest step — but note it still represents the central bank's currency, which sets up the money-vs-currency distinction.")
concept_apply("S32 · Concept 1 · [THEORY]","The Evolution of Money",
    "When a Nepali sends money via eSewa, they are using the newest stage of a long evolution: the same rupee that was once coins, then NRB paper notes, then a bank balance, now moves as an electronic entry in a wallet. Nothing about the rupee itself changed — only its FORM, from metal you carry to a number on a screen. Seeing money as 'evolving form, constant issuer' is the key to the next distinction.",
    "\"Digital money is a brand-new kind of money, different from cash.\" It is the same currency in a new form. The rupee in your eSewa wallet is the identical NRB-issued rupee that exists as notes and bank balances — only the medium changed. Treating digital money as a separate 'currency' is exactly the confusion Concept 3 corrects.",
    "Money evolved through five stages, each less physical: barter (goods for goods, needing a double coincidence of wants), commodity/coins (metal with agreed value), paper money (notes from a central authority — the NRB rupee), bank money (account balances, cheques, cards — money as a record), and digital money (electronic balances in wallets and apps — eSewa, mobile banking). Money is anything widely accepted as a medium of exchange, store of value, and unit of account. The form kept changing, but digital money still represents the same issued currency.",
    "evolution of money · barter → coins → paper → bank → digital · medium of exchange/store/unit · form changes, issuer constant")

concept_understand("S32 · Concept 2 · [THEORY]","What a Digital Currency Is (Physical vs Digital Money)",
    "A digital currency is money that exists ONLY in electronic form — there is no physical note or coin; it is held and transferred over a network via wallets or accounts. Physical money you can touch (notes, coins); digital money is a balance you access through a device. The important sub-point: 'digital money' (electronic form of existing currency, like your bank balance or eSewa) is broad, while a 'digital currency' in the strict sense may be a NEW currency (like a cryptocurrency) not issued by any central bank.",
    ["Digital currency = value that exists only electronically, moved over a network.",
     "Physical money = notes and coins you can hold; digital money = a balance on a device.",
     "Digital money (broad) = electronic form of existing currency (bank balance, eSewa).",
     "A cryptocurrency is a digital currency that is also a NEW unit, issued by no central bank."],
    None,"Digital currency = money in electronic form only. Physical = notes/coins; digital = a balance on a device.",
    "~8 min. Use the physical-vs-digital table. Carefully separate 'digital money' (existing currency, electronic) from a 'new digital currency' (crypto) — the bridge to Concept 3.")
add_comparison_table("S32 · Concept 2 · comparison","Physical money vs digital money",
    ["Dimension","Physical money","Digital money"],
    [["Form","Notes & coins you can touch","Electronic balance on a device"],
     ["How you hold it","Wallet, pocket, safe","App, bank account, e-wallet"],
     ["How it moves","Handed over in person","Transferred over a network instantly"],
     ["Issuer","Central bank (NRB)","Same currency, electronic form"],
     ["Example","NRB rupee notes","eSewa balance, bank app, debit card"],
     ["Works without internet?","Yes","Usually needs a network"]],
    per_page=6,widths=[1.9,2.4,2.6],fs=10.8,
    note="Key point for the next concept: digital MONEY here is still the NRB's rupee, just in electronic form. That is different from a new digital CURRENCY (like crypto) that no central bank issues.")
concept_apply("S32 · Concept 2 · [THEORY]","What a Digital Currency Is",
    "Your eSewa balance is digital money: it is the NRB rupee in electronic form, held in an app and moved over a network — no physical note involved, but the same national currency. Bitcoin, by contrast, is a digital currency in the strict sense: it exists only electronically AND is a new unit of value that no central bank issues. Both are 'digital', but one is a form of existing money and the other is a currency of its own.",
    "\"Any money on a phone is a 'digital currency'.\" Being electronic does not make something a new currency. Your eSewa/bank balance is digital MONEY — the existing NRB rupee in electronic form. A digital CURRENCY in the strict sense (like crypto) is a new unit of value issued by no central bank. The electronic form is shared; the 'new currency' part is not.",
    "A digital currency is money that exists only in electronic form — no physical note or coin — held and transferred over a network via wallets or accounts. Physical money you can touch (notes, coins); digital money is a balance accessed through a device. Importantly, 'digital money' broadly means the electronic form of an existing currency (a bank balance, eSewa — still the NRB rupee), whereas a digital currency in the strict sense can be a NEW unit of value (a cryptocurrency) issued by no central bank. Both are electronic; only one is a new currency.",
    "digital currency (electronic only) · physical vs digital money · digital money = existing currency electronic · new currency = crypto")

concept_understand("S32 · Concept 3 · [THEORY]","Digital Money ≠ Digital Currency (eSewa vs Crypto)",
    "Here is the signature distinction. eSewa is digital MONEY, NOT a digital CURRENCY. Why? eSewa does not create any new currency — every rupee in your eSewa wallet is an NRB-issued Nepali rupee, backed by the central bank, just stored and moved electronically. eSewa is a wallet/payment platform for existing money. A digital CURRENCY (a cryptocurrency) creates a NEW unit of value that no central bank issues or backs. Same 'digital', completely different thing.",
    ["eSewa = a digital WALLET holding existing NRB rupees electronically — digital money.",
     "It creates NO new currency; NRB still issues and backs every rupee it moves.",
     "A cryptocurrency IS a new currency: a new unit, issued/backed by no central bank.",
     "Test: does it create a new unit of value? No → digital money. Yes → digital currency."],
    None,"eSewa = digital MONEY (NRB rupees, electronic); crypto = digital CURRENCY (a new unit). It creates no new currency.",
    "~7 min. THE exam question. Drill the reason: eSewa moves existing NRB rupees; it does not issue a new currency. Use the eSewa-vs-crypto table.")
add_comparison_table("S32 · Concept 3 · comparison","eSewa (digital money) vs cryptocurrency (digital currency)",
    ["Dimension","eSewa — digital money","Cryptocurrency — digital currency"],
    [["What it holds","Existing NRB rupees, electronically","A new unit of value (e.g. Bitcoin)"],
     ["Who issues it","NRB issues the rupee; eSewa just moves it","No central bank — decentralised"],
     ["Backed by","The central bank / the state","Nothing official — market demand"],
     ["Creates new currency?","No — it is a wallet/platform","Yes — it IS a new currency"],
     ["Value stability","Stable (it is the rupee)","Volatile"],
     ["Legal in Nepal?","Yes — regulated payment service","No — crypto is BANNED by NRB"]],
    per_page=6,widths=[1.7,2.5,2.6],fs=10.5,
    note="The exam answer in one line: eSewa is digital MONEY because it only stores and moves existing NRB rupees electronically — it creates no new currency; a cryptocurrency is a digital CURRENCY because it IS a new unit no central bank issues.")
concept_apply("S32 · Concept 3 · [THEORY]","Digital Money ≠ Digital Currency",
    "Ask 'where did the value come from?' In eSewa, every rupee came from the NRB — eSewa only stores and moves it electronically, so it is digital money, not a currency (it is a wallet, like a digital purse for existing rupees). In Bitcoin, the value is a new unit the network itself created, issued by no central bank — so it is a digital currency. eSewa is a container for the rupee; crypto is a new kind of money altogether.",
    "\"eSewa (or Khalti) is Nepal's digital currency.\" No — eSewa is digital MONEY: it holds and transfers the existing NRB rupee electronically and creates no new currency. A digital currency (crypto) is itself a new unit of value issued by no central bank. Calling eSewa a 'currency' is the exact error examiners test with this question.",
    "eSewa is digital MONEY, not a digital CURRENCY. It creates no new currency: every rupee in an eSewa wallet is an NRB-issued Nepali rupee, backed by the central bank, merely stored and moved electronically — eSewa is a wallet/payment platform for existing money. A digital currency (a cryptocurrency) creates a NEW unit of value that no central bank issues or backs. The test is simple: if it creates a new unit of value it is a digital currency; if it only moves existing currency electronically it is digital money.",
    "eSewa = digital money · creates no new currency · NRB rupee electronic · crypto = digital currency (new unit) · the test")

add_activity("S32 — 'Money or currency?'  ·  ~5 min",
    ["Individually (1 min): write whether each is digital MONEY or a digital CURRENCY — eSewa, Bitcoin, a bank balance, Khalti, a hypothetical NRB coin.",
     "In pairs (2 min): give the REASON for each (does it create a new unit of value?).",
     "Take 3–4 answers aloud (2 min); correct any that call eSewa/Khalti a 'currency'.",
     "Close: the test is 'new unit of value?' — no = money, yes = currency."],
    "Answers: eSewa/Khalti/bank balance = digital MONEY (existing NRB rupees, no new unit); Bitcoin = digital CURRENCY (new unit); a hypothetical NRB digital coin = a digital currency (CBDC). Reward the REASON, not just the label.",
    "ACTIVITY [~5 min].")
add_quiz("S32 — Quick Check  ·  ~5 min",
    [("Q1.  eSewa is best described as:","q"),
     ("a) a digital currency   b) ✅ digital money — a wallet holding existing NRB rupees electronically   c) a cryptocurrency   d) a bank","a"),
     ("     Why: eSewa creates no new currency; every rupee is NRB-issued, just moved electronically — that is digital money.","o"),
     ("Q2.  The test for whether something is a digital CURRENCY is:","q"),
     ("a) is it on a phone   b) is it fast   c) ✅ does it create a NEW unit of value (issued by no central bank)   d) is it popular","a"),
     ("     Why: a digital currency IS a new unit of value; moving existing currency electronically is only digital money.","o"),
     ("Discussion: why do so many people wrongly call eSewa a 'digital currency'?","o")],
    "QUIZ [~5 min]. This is THE signature exam distinction — make sure every student can state the reason, not just the label.")
add_summary("S32 · Summary  ·  [~2 min]",
    ["Money evolved barter → coins → paper → bank → digital: steadily less physical, but always a trusted issuer's currency.",
     "A digital currency exists only electronically; digital money (broad) is existing currency in electronic form (eSewa, bank balance).",
     "SIGNATURE POINT: eSewa is digital MONEY, not a digital CURRENCY — it moves existing NRB rupees and creates no new unit of value."],
    "This distinction is the most exam-tested idea in the unit and clears up an error almost everyone makes. It also sets up S33: the actual digital CURRENCIES — cryptocurrency, stablecoins, and central-bank digital currencies.",
    "S33 — the three digital currency TYPES (crypto / stablecoin / CBDC), Nepal's ban, and the future.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S33
add_divider("Session 33 · Lecture hour 8 (of 8) — CLOSES UNIT 4","Digital Currencies: Types & the Future",
    "If eSewa isn't a digital currency, what IS? There are three real kinds — cryptocurrency, stablecoins, and central-bank digital currencies — and they differ on one thing: who issues them and what backs them. And in Nepal, one of them is outright BANNED. This closing session maps all three and looks at where money is heading.",
    "OPENING HOOK [~5 min]. Recall S32's distinction; now name the actual currencies. Agenda: cryptocurrency & Nepal's ban → stablecoin & CBDC → regulation approaches & the future.")

concept_understand("S33 · Concept 1 · [THEORY]","Cryptocurrency — and Nepal's Ban",
    "A cryptocurrency is a decentralised digital currency recorded on a blockchain (a shared, tamper-resistant ledger), issued and backed by no central bank — its value comes only from market demand, so it is highly volatile (Bitcoin, Ethereum). Nepal has BANNED cryptocurrency: Nepal Rastra Bank declared trading, mining, and dealing in crypto illegal, grounding the ban in the Foreign Exchange (Regulation) Act and its notices, citing capital-flight, fraud, money-laundering, and consumer-protection risks. [Dates/notice numbers should be verified against the current NRB source.]",
    ["Decentralised: no central bank; recorded on a blockchain (shared public ledger).",
     "Backed by nothing official — value is pure market demand, hence volatile.",
     "Nepal's ban: NRB declared crypto trading/mining/dealing illegal (verify exact dates).",
     "Legal basis: the Foreign Exchange (Regulation) Act + NRB notices; reasons = capital flight, fraud, laundering."],
    None,"Cryptocurrency = decentralised, blockchain-based, volatile, no issuer. BANNED in Nepal by NRB (verify dates).",
    "~7 min. State the ban plainly WITH its legal grounding (Foreign Exchange Regulation Act + NRB notice) and note dates need verifying. Reasons: capital flight, fraud, laundering, consumer protection.")
add_examples_table("S33 · Concept 1 · comparison","Cryptocurrency — advantages vs risks",
    ["Dimension","Advantage (claimed)","Risk / reason for Nepal's ban"],
    [["Control","No bank/government control","No recourse if funds lost/stolen"],
     ["Cross-border","Fast, cheap global transfers","Capital flight — money leaves the country untracked"],
     ["Transparency","Blockchain is auditable","Used for fraud, scams, money-laundering"],
     ["Access","Open to anyone with internet","No consumer protection; easy to defraud"],
     ["Value","Potential high returns","Extreme volatility — prices crash fast"],
     ["Innovation","New financial models","Undermines monetary policy & the rupee"]],
    per_page=6,widths=[1.5,2.4,2.9],fs=10.5,
    note="Nepal's NRB weighed these and judged the risks (capital flight, fraud, laundering, loss of monetary control) to outweigh the benefits for a small, remittance-dependent economy — hence the outright ban rather than regulation.")
concept_apply("S33 · Concept 1 · [THEORY]","Cryptocurrency — and Nepal's Ban",
    "Despite the ban, some Nepalis have traded crypto through foreign exchanges — which is exactly the capital-flight and enforcement problem NRB cites: money leaves the country untracked, users have no legal protection if a platform collapses, and scams have cost people real savings. NRB's position, grounded in the Foreign Exchange (Regulation) Act, is that for a small, remittance-reliant economy the risks to the rupee and to consumers outweigh crypto's benefits. (Exact notice dates should be verified.)",
    "\"Cryptocurrency is legal in Nepal, just not common.\" It is explicitly BANNED — NRB has declared trading, mining, and dealing illegal, citing the Foreign Exchange (Regulation) Act. Assuming it is merely rare (rather than prohibited) is a factual error; the exam expects you to state the ban and its legal/risk basis.",
    "A cryptocurrency is a decentralised digital currency recorded on a blockchain (a shared, tamper-resistant ledger), issued and backed by no central bank, so its value comes only from market demand and is highly volatile (Bitcoin, Ethereum). Nepal has BANNED it: Nepal Rastra Bank declared crypto trading, mining, and dealing illegal, grounded in the Foreign Exchange (Regulation) Act and NRB notices, citing capital flight, fraud, money-laundering, and consumer-protection risks for a small, remittance-dependent economy. (Exact notice dates should be verified against the current NRB source.)",
    "cryptocurrency · decentralised · blockchain · volatile · BANNED in Nepal (NRB) · Foreign Exchange Regulation Act · capital flight/fraud")

concept_understand("S33 · Concept 2 · [THEORY]","Stablecoins & CBDCs",
    "Two other digital currencies fix crypto's problems differently. A stablecoin is pegged to a stable asset (usually the US dollar) so it holds steady value — issued by a private company (e.g. USDT/Tether), useful for fast, low-cost cross-border transfers and remittances. A CBDC (Central Bank Digital Currency) is a digital form of a country's official money, issued and backed by the CENTRAL BANK itself — the national currency, just digital. Examples: China's e-CNY (Digital Yuan), Nigeria's eNaira, India's e-rupee pilot; NRB has studied a possible Nepali CBDC.",
    ["Stablecoin: pegged to a stable asset (USD) → steady value; issued by a private firm.",
     "Stablecoin use: fast, cheap cross-border transfers and remittances.",
     "CBDC: official national currency in digital form, issued/backed by the central bank.",
     "Examples: e-CNY, eNaira, India's e-rupee pilot; NRB has studied a CBDC (verify status)."],
    "s33_currency_types.png","Stablecoin = pegged (USD), private-issued, steady. CBDC = official currency, central-bank-issued, digital.",
    "~8 min. Use the three-currency-types diagram. Contrast on issuer + backing: crypto (none) vs stablecoin (private/pegged) vs CBDC (central bank). Note NRB CBDC study, verify status.")
add_comparison_table("S33 · Concept 2 · comparison","Crypto vs stablecoin vs CBDC",
    ["Dimension","Cryptocurrency","Stablecoin","CBDC"],
    [["Issuer","No one (decentralised)","Private company","Central bank"],
     ["Backing","Nothing official","Pegged to a stable asset (USD)","The state / official currency"],
     ["Value stability","Volatile","Stable (if peg holds)","Stable (it is the currency)"],
     ["Legal status (Nepal)","Banned","Not permitted (crypto rules)","Under study by NRB"],
     ["Example","Bitcoin, Ethereum","USDT / Tether","e-CNY, eNaira, India e-rupee"],
     ["Main use","Speculation, transfer","Cross-border remittance","Official digital cash"]],
    per_page=6,widths=[1.6,2.2,2.2,2.3],fs=10.2,
    note="The single dividing line is ISSUER + BACKING: crypto (nobody / nothing), stablecoin (a company / a pegged asset), CBDC (the central bank / the state). That is the comparison examiners most want to see.")
concept_apply("S33 · Concept 2 · [THEORY]","Stablecoins & CBDCs",
    "For a remittance-heavy country like Nepal the contrast matters: a stablecoin could in theory move a worker's earnings home cheaply and instantly with steady value — but it is private and falls under the crypto ban. A CBDC would be different: a digital rupee issued by NRB itself, official and stable, giving the benefits of digital money without leaving the state's control. That is why NRB has reportedly studied a CBDC even while banning crypto. (Verify the current study status.)",
    "\"A stablecoin and a CBDC are basically the same because both are stable.\" They differ on issuer and backing: a stablecoin is issued by a private company and pegged to an asset like the dollar; a CBDC is issued and backed by the central bank as official money. Stability alone does not make them equivalent — who stands behind them is the whole point.",
    "Two digital currencies address crypto's volatility differently. A stablecoin is pegged to a stable asset (usually the US dollar) so it holds steady value, issued by a private company (e.g. USDT/Tether), and is used for fast, low-cost cross-border transfers and remittances. A CBDC (Central Bank Digital Currency) is the official national currency in digital form, issued and backed by the central bank itself — examples include China's e-CNY, Nigeria's eNaira, and India's e-rupee pilot. NRB has reportedly studied a Nepali CBDC (status to be verified).",
    "stablecoin (pegged, private, remittance) · CBDC (central-bank official digital money) · e-CNY/eNaira/e-rupee · NRB CBDC study")

concept_understand("S33 · Concept 3 · [THEORY]","Regulation Approaches & the Future",
    "Countries respond to digital currencies in four broad ways: BAN (prohibit crypto outright — Nepal, China); REGULATE (allow with licensing, tax, and rules — much of the EU, Japan); SANDBOX (permit limited trials under supervision to learn safely); and issue a CBDC (build the state's own digital currency instead). Looking ahead: cash use is declining, payments keep going digital, and 'tokenization' (representing assets digitally) is emerging — but volatility, security, and control keep regulation cautious.",
    ["Ban: outright prohibition (Nepal, China) — safest for control, blocks innovation.",
     "Regulate: legalise with licensing, tax, and consumer rules (EU, Japan).",
     "Sandbox: supervised trials to test safely before wider rules.",
     "CBDC route: the state issues its own digital money; future = less cash, more tokenization."],
    None,"Four responses: BAN · REGULATE · SANDBOX · issue a CBDC. Future: cash declines, payments digitise, tokenization emerges.",
    "~7 min. Place Nepal on the spectrum (ban) and contrast with regulate/sandbox/CBDC. Close the unit forward-looking: cash decline, CBDCs, tokenization — with caution noted.")
add_comparison_table("S33 · Concept 3 · comparison","Regulatory approaches to digital currencies",
    ["Approach","What the country does","Example","Trade-off"],
    [["Ban","Prohibit crypto outright","Nepal, China","Max control; blocks innovation & drives it underground"],
     ["Regulate","Allow with licences, tax, rules","EU (MiCA), Japan","Innovation with safeguards; needs capacity"],
     ["Sandbox","Supervised limited trials","Various regulators","Learn safely before full rules"],
     ["Issue a CBDC","Build the state's own digital money","China e-CNY, India pilot","Keeps benefits under central-bank control"]],
    per_page=4,widths=[1.5,2.3,1.9,2.8],fs=10.5,
    note="Nepal currently sits at the BAN end. The live policy debate — reflected in NRB's CBDC study — is whether to keep banning or move toward a controlled option (regulate, sandbox, or a CBDC) as the technology matures.")
concept_apply("S33 · Concept 3 · [THEORY]","Regulation Approaches & the Future",
    "Nepal's choice is a live exam question: keep the crypto ban (maximum control, but innovation and remittance savings go elsewhere and trading continues underground) or move toward a controlled path — regulate, run a sandbox, or issue a digital rupee CBDC that captures the benefits under NRB's control. Globally, cash is declining and CBDCs are spreading, so 'ban forever' looks harder to sustain; a Nepali CBDC is the option NRB appears to be studying. (Confirm current status.)",
    "\"The only choice is to ban crypto or allow it freely.\" There is a spectrum: outright ban, regulate with rules, run supervised sandboxes, or issue a state CBDC. Framing it as all-or-nothing misses the realistic middle paths — and a CBDC lets a country gain digital-currency benefits while keeping central-bank control.",
    "Countries respond to digital currencies in four ways: BAN (prohibit crypto outright — Nepal, China), REGULATE (allow with licensing, tax, rules — EU's MiCA, Japan), SANDBOX (supervised limited trials to learn safely), and issue a CBDC (the state builds its own digital money — China's e-CNY, India's pilot). Nepal currently bans crypto. The future points to declining cash, increasingly digital payments, and emerging tokenization, though volatility, security, and control keep regulators cautious — which is why NRB is studying a CBDC while maintaining the ban.",
    "regulation approaches · ban · regulate · sandbox · CBDC · Nepal bans · future: less cash, CBDCs, tokenization")

add_activity("S33 — 'Ban, regulate, or build a CBDC?'  ·  ~5 min",
    ["In pairs (3 min): should Nepal keep banning crypto, regulate it, run a sandbox, or issue a digital-rupee CBDC?",
     "Name one benefit and one risk of your chosen approach for Nepal specifically.",
     "State which of the three currency types (crypto/stablecoin/CBDC) your policy targets.",
     "Take 3–4 answers aloud (2 min); require a reason grounded in Nepal's economy (remittance, capital flight, control)."],
    "Good reasoning: keep-ban = protects rupee & consumers but forgoes remittance savings; CBDC = digital benefits under NRB control but costly to build. Reward using Nepal's remittance-dependence and capital-flight risk explicitly.",
    "ACTIVITY [~5 min].")
add_quiz("S33 — Quick Check  ·  ~5 min",
    [("Q1.  The three digital-currency types differ mainly by:","q"),
     ("a) speed   b) ✅ who ISSUES them and what BACKS them (nobody / a company / the central bank)   c) colour   d) app design","a"),
     ("     Why: crypto (no issuer), stablecoin (private, pegged), CBDC (central bank) — issuer and backing is the dividing line.","o"),
     ("Q2.  Cryptocurrency in Nepal is:","q"),
     ("a) legal and common   b) ✅ banned by NRB (Foreign Exchange Regulation Act basis)   c) taxed but allowed   d) issued by NRB","a"),
     ("     Why: NRB has declared crypto trading/mining/dealing illegal, citing capital flight, fraud, and laundering risks.","o"),
     ("Discussion: should Nepal move from banning crypto toward a CBDC? Argue both sides.","o")],
    "QUIZ [~5 min]. Cement the crypto/stablecoin/CBDC comparison and Nepal's ban + its legal basis — the unit's most exam-weighted content.")
add_summary("S33 · Summary  ·  [~2 min]",
    ["Three digital-currency types differ by issuer + backing: crypto (nobody / nothing, volatile), stablecoin (private / pegged), CBDC (central bank / official).",
     "Nepal BANS cryptocurrency (NRB, grounded in the Foreign Exchange Regulation Act) citing capital flight, fraud, and laundering; it has studied a CBDC.",
     "Regulatory approaches: ban / regulate / sandbox / CBDC; the future points to less cash, more digital payments, and tokenization."],
    "Digital money is where the digital economy meets your daily life and national policy most directly — and Nepal's live debate over crypto and a possible digital rupee is one you can now argue with the correct concepts and the real legal grounding.",
    "End of Unit 4 — next comes the end-of-unit revision aids: cheat sheet, glossary, and consolidated quiz.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 4 · Cheat Sheet","One-page revision reference",
    [("DT concepts (S26)","DT = deep change in processes + business model + culture (new value, not old work sped up). Three tiers: digitization (DATA) → digitalization (PROCESS) → transformation (MODEL). Transform or die: Kodak, Nokia, Blockbuster."),
     ("Drivers (S27)","Technological (internet, mobile, cloud, big data, AI, IoT) = POSSIBLE. Economic (competition, cost) = NECESSARY. Social (behaviour, youth, policy) = EXPECTED. Crisis (COVID-19) = ACCELERATOR (forced adoption, much stuck)."),
     ("SDGs & growth (S28–S31)","DT accelerates SDGs via 5 mechanisms: speed, reach, efficiency, transparency, scalability. Maps to SDG 4/8/9/16. ICT4D vs the digital divide. Growth chain: skills→jobs→income→GDP; engines = low marginal cost + network effects (Unit 2). Revolution changes economy STRUCTURE + labour shift."),
     ("Globalization (S30)","Traditional = physical goods, slow, big firms; digital = services/data, instant, anyone (skills + internet). E-commerce: B2C / B2B / C2C. Digital trade = cross-border goods+services+data. Nepal: 'growth without factories', service-provider."),
     ("Money vs currency (S32)","Money evolved barter→coins→paper→bank→digital. Digital currency = electronic-only. SIGNATURE: eSewa = digital MONEY (existing NRB rupees, electronic; creates NO new currency), NOT a digital CURRENCY. Test: creates a new unit of value? No=money, Yes=currency."),
     ("Currency types (S33)","Crypto (decentralised, blockchain, volatile, no issuer — BANNED in Nepal by NRB via Foreign Exchange Regulation Act) · Stablecoin (private, pegged to USD, remittance) · CBDC (central-bank official digital money — e-CNY/eNaira/India; NRB studying). Approaches: ban/regulate/sandbox/CBDC.")])

add_glossary("Unit 4 · Glossary","Key terms — quick reference",
    [("Digital transformation (DT)","deep change in an organisation's processes, business model & culture using digital tech."),
     ("Digitization","converting information from analog to digital (paper → PDF) — about DATA."),
     ("Digitalization","using digital tech to improve a process/workflow — about PROCESS."),
     ("Transform or die","incumbents that fail to change their model are wiped out (Kodak, Nokia)."),
     ("Technological driver","tech (internet, mobile, cloud, AI, IoT) that makes DT possible & cheap."),
     ("Economic driver","competition, cost, revenue pressure that makes DT necessary."),
     ("Social driver","user behaviour, young population, policy that makes DT expected."),
     ("Crisis accelerator","a shock (COVID-19) that forces rapid adoption of existing tools."),
     ("SDGs","17 UN Sustainable Development Goals for 2030."),
     ("Five SDG mechanisms","speed, reach, efficiency, transparency, scalability."),
     ("ICT4D","Information & Communication Technology for Development."),
     ("Digital divide","gaps in access (internet, devices) and skills that exclude people."),
     ("Platform economy","value created by connecting groups rather than producing goods (Unit 2)."),
     ("Labour-market shift","routine jobs vanish, digital/gig jobs appear; digital skills decide."),
     ("Gig economy","flexible, platform-mediated work (Pathao riders, freelancers)."),
     ("Globalization","the growing interconnection of the world's economies."),
     ("Traditional globalization","cross-border flow of physical goods — slow, costly, big firms."),
     ("Digital globalization","instant cross-border flow of services, data & software — open to all."),
     ("E-commerce","buying/selling online: B2C, B2B, C2C."),
     ("Digital trade","cross-border flow of goods, services, digital products & data."),
     ("Growth without factories","raising GDP via skills/services, not physical production."),
     ("Low marginal cost","serving one more user costs almost nothing (growth engine, Unit 2)."),
     ("Network effect","each new user makes the platform more valuable (Unit 2)."),
     ("Digital Nepal Framework","government's policy plan for a digital economy (detail in Unit 6)."),
     ("Money","anything widely accepted as a medium of exchange/store of value/unit of account."),
     ("Digital money","existing currency (NRB rupee) held & moved in electronic form (eSewa)."),
     ("Digital currency","money that exists only electronically; strict sense = a new unit of value."),
     ("eSewa","a digital WALLET/payment platform holding existing NRB rupees — digital money, NOT a currency."),
     ("Cryptocurrency","decentralised, blockchain-based digital currency; no issuer; volatile — BANNED in Nepal."),
     ("Blockchain","a shared, tamper-resistant ledger recording transactions."),
     ("Stablecoin","a digital currency pegged to a stable asset (USD); issued by a private firm."),
     ("CBDC","Central Bank Digital Currency — official national money in digital form."),
     ("Foreign Exchange (Regulation) Act","the legal basis NRB cites for banning cryptocurrency."),
     ("Regulatory approaches","ban / regulate / sandbox / issue a CBDC."),
     ("Tokenization","representing real-world assets digitally on a ledger.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 4 · Revision","Consolidated end-of-unit quiz",
    "Twelve MCQs across the whole unit (answers shown, correct option varied a/b/c/d), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit4_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review. (No genuine IT 250 past-paper exists — built from the syllabus + the concept slides.)")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Digital transformation means changing an organisation's:   a) logo   b) ✅ processes, business model & culture   c) office   d) name","a"),
     ("2.  Scanning paper forms into PDFs (only) is:   a) ✅ digitization   b) digitalization   c) transformation   d) automation","a"),
     ("3.  Cloud, mobile and AI are which driver type:   a) social   b) economic   c) ✅ technological   d) crisis","a"),
     ("4.  COVID-19 acted as a driver that:   a) invented new tech   b) had no effect   c) ✅ accelerated adoption of existing tools   d) reversed it","a"),
     ("5.  An SDG that digital transformation directly accelerates is:   a) ✅ SDG 4 (quality education)   b) none   c) only SDG 17   d) SDG 14 only","a"),
     ("6.  ICT4D means using technology:   a) for war   b) for profit only   c) ✅ for development   d) for gaming","a"),
     ("7.  The platform economy creates value by:   a) mining   b) ✅ connecting groups (network effects)   c) farming   d) printing","a"),
     ("8.  Compared with traditional globalization, digital globalization is:   a) slower   b) only for big firms   c) ✅ instant and open to individuals   d) physical","a"),
     ("9.  'Serving one more user costs almost nothing' is:   a) network effect   b) ✅ low marginal cost   c) a tariff   d) inflation","a"),
     ("10.  eSewa is best described as:   a) a cryptocurrency   b) ✅ digital money (existing NRB rupees, electronic)   c) a digital currency   d) a stablecoin","a"),
     ("11.  Crypto / stablecoin / CBDC differ mainly by:   a) colour   b) ✅ who issues them & what backs them   c) speed   d) app design","a"),
     ("12.  Nepal bans cryptocurrency mainly because of:   a) it is too slow   b) ✅ capital flight, fraud & laundering risks (NRB)   c) no internet   d) no reason","a")],
    "Consolidated quiz Section A. Correct-answer position is varied; see the answer key in Unit4_material.md.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("13. Distinguish digitization, digitalization and digital transformation with an example each.   14. Name the four drivers of DT.   15. Map TWO SDGs to DT with Nepal examples.","o"),
     ("16. Distinguish traditional vs digital globalization.   17. Compare cryptocurrency, stablecoin and CBDC.","o"),
     ("Section C — Applied case","q"),
     ("18. Why is eSewa digital MONEY but NOT a digital currency? Give the reason, not just the label.","o"),
     ("19. Argue whether Nepal should keep banning crypto or move to a CBDC — use remittance, capital flight, and control.","o"),
     ("Section D — Discussion","q"),
     ("20. 'Is digital transformation net-positive for Nepal's economy?' Use SDGs, growth engines, and the digital divide.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit4_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 4  ·  IT 250",
          "S26–S33 complete: digital transformation concepts (digitization/digitalization/DT) · drivers · accelerating the SDGs · "
          "technological revolution & the world economy · globalization in the digital age · DT & economic growth · "
          "digital currencies (money ≠ currency) · types & future (crypto/stablecoin/CBDC + Nepal's ban)",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe, Nepal-localised · Next: Unit 5 — Economics of Information.")

_add_page_numbers()
save("IT250_Unit4.pptx")
