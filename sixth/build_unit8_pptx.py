#!/usr/bin/env python3
"""IT246 (sixth) Unit 8 deck — Digital Forensics (S38–S44), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a comparison
table, every 'X vs not-X' concept a concrete-example table, claims get scaffolding tables — each
table on its OWN slide, paginated, never squeezed. Self-contained & PDF-safe. Imports deckkit.py.
Diagrams in images/. Localised to Nepal (ETA 2063, Nepal Police Cyber Bureau, NTC/Ncell CDRs,
eSewa/Khalti, Facebook/TikTok/WhatsApp). Emphasis: integrity, chain of custody, lawful practice.
Run: python3 build_unit8_pptx.py -> IT246_Unit8.pptx
"""
from deckkit import *

# ============================================================
#                        FRONT MATTER
# ============================================================
add_title("Unit 8 — Digital Forensics",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S38–S44",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised) — no abstraction without instances. Chain of custody & evidence integrity run "
          "through the whole unit. Exports to PDF with no information lost.")

add_outcomes("Unit 8 — Learning Outcomes","digital forensics  ·  s38–s44",
    "By the end of this unit, you will be able to:",
    ["Define digital forensics and explain how it grew from 'computer forensics', plus its core principles (S38)",
     "Describe the six-stage forensic process: identify → preserve → collect → examine → analyse → report (S39)",
     "Explain what counts as digital evidence and describe a forensic lab's setup and tool categories (S40)",
     "Explain chain of custody and the techniques that protect integrity — write blockers, hashing, sealed storage (S41)",
     "Describe conceptually how deleted data is recovered via disk imaging and file carving (S42)",
     "Explain mobile forensics — extraction levels, challenges, and app-data sources (S43)",
     "Explain the legal admissibility of digital evidence and the state of cyber forensics in Nepal (S44)"],
    "This is Unit 8 of IT 246 — the investigative side of cybersecurity. It turns the defence mindset of Units 5–7 toward what happens AFTER an incident: recovering evidence lawfully so it stands up in court.")

add_roadmap("Unit 8 — Roadmap","Where each session fits (S38–S44)",
    ["S38  Intro — from computer to digital forensics",
     "S39  The six stages of digital forensics",
     "S40  Digital evidence · methods · the forensic lab",
     "S41  Collecting, seizing & protecting evidence",
     "S42  Recovering data (imaging · carving)",
     "S43  Mobile forensics",
     "S44  Legal aspects · cyber forensics in Nepal"],
    ["Unit 9   Cyber law in Nepal (ETA 2063, IT policy)",
     "(Unit 8 closes the cybersecurity block; Unit 9 is the legal deep-dive)"])

# ============================================================ S38
add_divider("Session 38 · Lecture hour 1 (of 7)","Introduction — From Computer Forensics to Digital Forensics",
    "A suspect's laptop is seized in a fraud case. An officer 'just opens it to check' — and the case collapses in court. One click destroyed the evidence. How can looking at a file BREAK it?",
    "OPENING HOOK [~5 min]. Draw out that forensics is a disciplined science, not casual snooping. Agenda: what digital forensics is -> how the field grew -> the core principles.")

concept_understand("S38 · Concept 1 · [THEORY]","What Is Digital Forensics",
    "Digital forensics is the scientific process of identifying, preserving, analysing and presenting digital evidence in a way that is legally admissible. Forensics = applying science to legal questions; 'digital' = any device that stores or transmits data.",
    ["The GOAL is court-admissible proof — not just retrieving a file.",
     "It applies a repeatable, documented, scientific method so results can be defended.",
     "'Digital' now covers PCs, phones, servers, cloud accounts, IoT and vehicles.",
     "The original must be protected; investigators reason from evidence, not hunches."],
    None,"Forensics = science applied to law; the target is admissible proof, not just recovered data.",
    "~8 min. BTK killer caught via Word-document metadata on a floppy. Land that the discipline exists to make evidence trustworthy in court.")
add_table_slide("S38 · Concept 1 · scaffolding","Data recovery vs digital forensics — same file, different discipline",
    ["Dimension","Plain data recovery","Digital forensics"],
    [["Goal","Get the file back","Court-admissible proof"],
     ["Original","May write to / repair it","Never alter — work on a hashed copy"],
     ["Documentation","Optional","Every step logged (chain of custody)"],
     ["Method","Whatever works","Repeatable, defensible, scientific"],
     ["Output","The recovered data","A report a judge can rely on"],
     ["Who uses it","IT support","Cyber Bureau, courts, investigators"]],
    per_page=6,widths=[1.5,2.6,2.9],fs=11,
    note="Forensics is NOT 'IT support that finds files'. The extra discipline — no alteration, full documentation, repeatability — is exactly what makes the result usable in court.")
concept_apply("S38 · Concept 1 · [THEORY]","What Is Digital Forensics",
    "Nepal Police Cyber Bureau (established 2018, Bhotahity, Kathmandu) analyses seized devices in online-fraud and social-media-abuse cases. It does not merely 'recover files' — it preserves, hashes and documents so the evidence survives a courtroom challenge.",
    "\"Forensics is just data recovery / IT support.\" No — the goal is legally admissible proof, not simply retrieving files. Casual recovery that alters the original or skips documentation destroys the evidential value even when the data is found.",
    "Digital forensics is the scientific process of identifying, preserving, analysing and presenting digital evidence in a legally admissible way. It applies science to legal questions across any device that stores or transmits data, and its defining goal is court-admissible proof — achieved through a repeatable, documented method that never alters the original.",
    "digital forensics · admissible evidence · science + law · do not alter the original · Cyber Bureau")

concept_understand("S38 · Concept 2 · [THEORY]","From Computer Forensics to Digital Forensics",
    "The field broadened from desktop hard disks to phones, cloud, IoT, network traffic and vehicles. 'Computer forensics' (1980s–90s, a single PC) grew into 'digital forensics' — multi-device, networked, cloud-connected, and mobile-dominant today.",
    ["Early era: one PC, one hard disk, seized and imaged in a lab.",
     "Then networks, email and servers added remote and volatile evidence.",
     "Today evidence is mostly on phones and apps, with cloud copies elsewhere.",
     "New sources keep arriving: IoT devices, smart TVs, cars and wearables."],
    "s38_timeline.png","Computer forensics (one PC) grew into digital forensics (phones, cloud, IoT, networks).",
    "~7 min. Old textbook says 'image the hard drive' — but the suspect only owns a smartphone. Ask what changed. The device landscape did.")
add_table_slide("S38 · Concept 2 · concrete examples","How the evidence source shifted — old assumption vs today (Nepal)",
    ["Case type","Old assumption (computer era)","Today's reality (digital era)"],
    [["Online fraud","Desktop PC with account files","eSewa/Khalti + phone + bank app data"],
     ["Harassment / abuse","Emails on a work PC","Facebook, Messenger, TikTok, WhatsApp chats"],
     ["Blackmail / sextortion","Local image files on a disk","Phone gallery + cloud backup + chat apps"],
     ["Financial scam","Spreadsheet on one computer","Mobile wallets, SMS OTPs, CDRs from NTC/Ncell"],
     ["Fake profile / defamation","A single machine's browser history","Social-media accounts hosted abroad (cloud)"],
     ["Data theft by an insider","USB copied at a desk","Cloud sync, personal phone, webmail"]],
    per_page=6,widths=[1.9,2.6,2.9],fs=11,
    note="In Nepal most cases now hinge on phones, apps and cloud — not desktop PCs. 'Image the hard drive' is no longer the default; the investigator must follow the data wherever it now lives.")
concept_apply("S38 · Concept 2 · [THEORY]","From Computer Forensics to Digital Forensics",
    "Nepali cases now hinge far more on Facebook/TikTok/WhatsApp/Viber and mobile phones than on desktop PCs. A single seized smartphone can hold chats, location history, wallet transactions and cloud-linked backups — the crime scene moved into the pocket.",
    "\"Digital forensics just means examining a computer's hard drive.\" That was the 1990s. Evidence now lives on phones, in the cloud, and across networks and IoT — a modern investigator who only knows disk imaging misses most of the evidence.",
    "The field broadened from 'computer forensics' (1980s–90s, a single desktop hard disk) to 'digital forensics' — multi-device, networked, cloud-connected and mobile-dominant. The shift happened because evidence moved off the PC and onto phones, apps, cloud accounts, IoT and vehicles, so investigators must follow data wherever it lives, not just image a hard drive.",
    "computer→digital forensics · multi-device · mobile-dominant · cloud & IoT · follow the data")

concept_understand("S38 · Concept 3 · [THEORY]","Core Principles of Digital Forensics",
    "The core principles: don't alter the original; work on copies; document everything; maintain chain of custody; and ensure repeatability. ACPO-style rules say actions taken must not change the data — and if originals must be accessed, the person must be competent and explain why.",
    ["Principle 1: no action should change the evidence (the golden rule).",
     "Principle 2: if you must access the original, be competent and record why.",
     "Principle 3: keep an audit trail — another expert could repeat your steps.",
     "Principle 4: the lead investigator is responsible for compliance throughout."],
    None,"A digital crime scene is a footprint in sand — walking over it to 'look closer' destroys it.",
    "~7 min. Deliver the ACPO principles plainly. The footprint analogy is the retention hook — looking can be destroying.")
add_table_slide("S38 · Concept 3 · scaffolding","The core principles — what each means and why it matters",
    ["Principle","What it means in practice","Why it matters"],
    [["Don't alter the original","Use write blockers; never open files on the seized device","A changed byte makes the evidence challengeable"],
     ["Work on copies","Image the device; analyse the hashed image","The sealed original stays pristine for court"],
     ["Document everything","Log who, what, when, why for every action","Undocumented steps can't be defended"],
     ["Chain of custody","Record every handoff of the evidence","A gap suggests possible tampering"],
     ["Repeatability","Another expert can redo your steps & agree","Science, not opinion — this is what convinces a court"],
     ["Competence","Only trained people touch originals","An untrained click can destroy a case"]],
    per_page=6,widths=[1.9,3.0,2.5],fs=11,
    note="These principles are not bureaucracy — each one exists to keep the evidence trustworthy and defensible. Break one and even genuine, damning evidence can be thrown out.")
concept_apply("S38 · Concept 3 · [THEORY]","Core Principles of Digital Forensics",
    "When the Cyber Bureau seizes a phone in a fraud case, an officer who 'just opens the gallery to check' has already changed timestamps and access records — violating principle 1. The correct move is to isolate, image and analyse a hashed copy, logging every step.",
    "\"Taking a quick look at the file can't hurt.\" Opening a file changes access times, can trigger syncs, and breaks the 'don't alter the original' principle — one of the most dangerous things an investigator can do. Look only at a forensic copy, never the seized original.",
    "The core principles of digital forensics are: don't alter the original, work on copies, document everything, maintain chain of custody, and ensure repeatability — with the lead investigator responsible throughout and only competent people accessing originals. They exist so evidence stays trustworthy and defensible; violating even one can make genuine evidence inadmissible.",
    "core principles · do not alter · work on copies · document · chain of custody · repeatability · competence")

add_activity("S38 — 'Why is a quick look dangerous?'  ·  ~5 min",
    ["In pairs (2 min): an officer wants to 'just open one file' on a seized laptop to check it.",
     "List everything that could change on the device the moment a file is opened.",
     "Take 3–4 answers aloud (3 min); connect each to a broken core principle.",
     "Close: looking can be destroying — the footprint-in-sand rule. Image first, then examine the copy."],
    "Seeds: last-accessed timestamps change; auto-sync/cloud upload triggers; antivirus/OS writes; 'recent files' updates; the hash of the disk changes. Each breaks 'don't alter the original' and gives the defence a challenge.",
    "ACTIVITY [~5 min].")
add_quiz("S38 — Quick Check  ·  ~5 min",
    [("Q1.  The defining GOAL of digital forensics is:","q"),
     ("a) recover deleted files   b) ✅ produce legally admissible evidence   c) fix the device   d) back up data","a"),
     ("     Why: forensics applies science to law — the aim is proof a court will accept, not mere recovery.","o"),
     ("Q2.  'Computer forensics' grew into 'digital forensics' mainly because:","q"),
     ("a) PCs got faster   b) ✅ evidence now lives on phones, cloud and networks, not just PCs   c) laws changed   d) disks shrank","a"),
     ("     Why: the device landscape shifted to mobile-dominant, cloud-connected, multi-device evidence.","o"),
     ("Discussion: why is 'just take a quick look at the file' one of the most dangerous things an investigator can do?","o")],
    "QUIZ [~5 min]. Draw out that opening a file alters the original and breaks admissibility — the whole discipline is built to prevent exactly that.")
add_summary("S38 · Summary  ·  [~2 min]",
    ["Digital forensics = science + law applied to digital evidence; the goal is legally admissible proof.",
     "The field expanded far beyond the single PC — phones, cloud, networks and IoT dominate today.",
     "Core principles: preserve the original, work on hashed copies, document, keep custody, stay repeatable."],
    "Anyone in IT may one day hold a device that is evidence. Knowing not to touch it — to isolate and hand it over properly — can make or break a case and protect your own liability.",
    "S39 — the staged forensic process that turns a scene into courtroom-ready evidence.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S39
add_divider("Session 39 · Lecture hour 2 (of 7)","Stages of Digital Forensics",
    "Two investigators find the same incriminating photo on a phone. One follows a documented process; the other 'just found it.' Only one will hold up in court. Why?",
    "OPENING HOOK [~5 min]. Draw out that process is what makes evidence trustworthy. Agenda: the process model -> walking the six stages -> integrity & custody through all of them.")

concept_understand("S39 · Concept 1 · [THEORY]","The Forensic Process Model",
    "The forensic process is a repeatable, documented sequence from scene to courtroom: identification → preservation → collection → examination → analysis → reporting. It follows standard models such as NIST SP 800-86 (collection, examination, analysis, reporting).",
    ["It is a fixed, ordered sequence — not an ad-hoc 'poke around and see'.",
     "Each stage has a defined purpose and hands a clean result to the next.",
     "The model exists so different investigators reach the same, defensible result.",
     "Preservation and custody are what make the later analysis usable at all."],
    "s39_process.png","Identify → preserve → collect → examine → analyse → report — a fixed, documented pipeline.",
    "~8 min. Present the six-stage pipeline with the custody band. Stress that the order is deliberate, not decorative.")
add_table_slide("S39 · Concept 1 · scaffolding","The six stages — purpose and output of each",
    ["Stage","What happens","Output handed on"],
    [["Identify","Find which devices/accounts/data matter","A list of evidence sources"],
     ["Preserve","Isolate & prevent any change (airplane mode/Faraday)","An unaltered, protected source"],
     ["Collect","Image/seize the evidence; hash it","A verified forensic copy"],
     ["Examine","Extract the relevant data from the copy","Filtered, relevant data"],
     ["Analyse","Interpret it; reconstruct the timeline of events","A reasoned account of what happened"],
     ["Report","Explain it clearly for a non-technical judge","A defensible written report"]],
    per_page=6,widths=[1.5,3.0,2.6],fs=11,
    note="Analysis grabs the attention, but preservation and collection are what make it admissible. The report must convince a judge or lawyer — not another engineer.")
concept_apply("S39 · Concept 1 · [THEORY]","The Forensic Process Model",
    "For a cyberbullying complaint, the Cyber Bureau identifies the account/phone, preserves it by isolating the device, images and hashes it, examines the messages, analyses the timeline, and reports for the prosecutor. Each stage feeds a clean, documented result into the next.",
    "\"Analysis is the real work; the rest is just paperwork.\" Preservation and chain of custody are what make the analysis usable at all — brilliant analysis of contaminated evidence is worthless in court. The 'paperwork' is the admissibility.",
    "The forensic process is a repeatable, documented sequence from scene to courtroom — identification, preservation, collection, examination, analysis, reporting — following standard models like NIST SP 800-86. The fixed order matters because preservation and custody make the downstream analysis defensible, and the final report must be understandable by a non-technical judge.",
    "forensic process model · six stages · NIST SP 800-86 · fixed order · report for a non-technical judge")

concept_understand("S39 · Concept 2 · [THEORY]","Walking the Stages",
    "Walking the pipeline: Identification (what devices/data matter) → Preservation (isolate, prevent change) → Collection (image/seize) → Examination (extract relevant data) → Analysis (interpret, reconstruct events) → Reporting (clear, defensible, for non-technical readers).",
    ["Identify before you touch: know what you're looking for and where it lives.",
     "Preserve immediately: airplane mode / Faraday bag stops remote wiping and syncing.",
     "Collect by imaging and hashing, then examine and analyse only the copy.",
     "A skipped stage silently poisons everything after it."],
    None,"Each stage feeds the next; skip one and the whole chain downstream is contaminated.",
    "~7 min. Mini case: investigators skip preservation, the phone keeps syncing overnight, the cloud deletes the key chat. Ask which stage failed — preservation.")
add_table_slide("S39 · Concept 2 · concrete examples","What goes wrong when a stage is skipped (Nepal cases)",
    ["Stage skipped / done badly","What happens","Consequence (verdict)"],
    [["Identification","Miss the suspect's second phone","Key evidence never collected — case weakened"],
     ["Preservation","Phone left online; cloud deletes the chat overnight","Irreplaceable evidence lost — preservation failed"],
     ["Collection","Copy files by hand instead of imaging","No hash, no slack space — challengeable & incomplete"],
     ["Examination","Analyst wades through everything unfiltered","Slow, error-prone; may miss the relevant data"],
     ["Analysis","Report a chat with no timeline/context","A judge can't see what actually happened"],
     ["Reporting","Hand the court a raw technical dump","Non-technical judge can't use it — impact lost"]],
    per_page=6,widths=[1.9,3.0,2.5],fs=11,
    note="Errors compound downstream: a preservation failure can't be fixed by brilliant analysis. The single most case-ending skip is usually preservation — lost data can't be re-collected.")
concept_apply("S39 · Concept 2 · [THEORY]","Walking the Stages",
    "A seized phone is left switched on 'just for now' while officers finish paperwork; overnight it keeps syncing and the suspect's remote account deletes the key chat. Preservation failed — the device should have gone into a Faraday bag / airplane mode immediately at collection.",
    "\"We can always go back and re-collect if we miss something.\" Volatile evidence (RAM, live syncs, cloud-deletable chats) can vanish permanently within minutes. Preservation is a one-shot chance — you cannot re-collect what has been overwritten or wiped.",
    "Walking the stages: identify what data matters, preserve it by isolating the device (airplane mode/Faraday) to prevent change, collect it by imaging and hashing, examine to extract the relevant data, analyse to reconstruct the timeline, and report clearly for non-technical readers. Because each stage feeds the next, skipping preservation in particular can destroy evidence permanently.",
    "walk the stages · isolate immediately · Faraday/airplane mode · image + hash · reconstruct timeline · one-shot preservation")

concept_understand("S39 · Concept 3 · [THEORY]","Integrity & Chain of Custody Run Through Every Stage",
    "Chain of custody and integrity thread through all six stages: documentation, hashing at collection, sealed evidence bags, and a custody log. Every handoff is recorded; any gap becomes a challenge in court. Integrity is not a stage — it is a band under all stages.",
    ["Hash at collection; re-hash later to prove nothing changed.",
     "Seal and label evidence; store it in a locked, access-controlled place.",
     "Log every transfer: who took it, when, why, and how.",
     "A single unexplained gap can make the whole exhibit inadmissible."],
    None,"Custody is a relay baton — every handoff is recorded, and dropping it disqualifies the team.",
    "~7 min. The relay-baton analogy carries the intuition. Integrity is continuous, not a checkbox at the end.")
add_table_slide("S39 · Concept 3 · concrete examples","How integrity is maintained at each stage",
    ["Stage","Integrity action taken","Why it protects the case"],
    [["Preservation","Seal in a labelled, tamper-evident bag","Proves no one accessed it in transit"],
     ["Collection","Compute a SHA-256 hash of the image","Later re-hash proves the copy is unchanged"],
     ["Storage","Lock in an access-controlled evidence locker","Limits who could have tampered"],
     ["Every handoff","Sign the custody log (who/when/why/how)","No gap for the defence to exploit"],
     ["Examination","Work only on the hashed copy, never the original","The sealed original stays court-ready"],
     ["Reporting","Cite hashes & custody log in the report","Shows the court the evidence is trustworthy"]],
    per_page=6,widths=[1.7,2.9,2.7],fs=11,
    note="Integrity is continuous, not a final checkbox. The custody log plus matching hashes are what let an expert testify, credibly, that the evidence is exactly what was seized.")
concept_apply("S39 · Concept 3 · [THEORY]","Integrity & Chain of Custody Run Through Every Stage",
    "In a Nepali fraud case, the Cyber Bureau tags and seals the seized phone, hashes the image at collection, logs every handoff to the lab and back, and cites those hashes in the report. If challenged, the expert can show the analysed copy still matches the seized original bit-for-bit.",
    "\"Chain of custody is just bureaucratic paperwork.\" It is the proof the evidence wasn't tampered with — without it, even perfect data is worthless in court. The log and the hashes are what let the evidence be believed at all.",
    "Integrity and chain of custody run through every stage: hashing at collection, sealed and labelled evidence bags, locked storage, and a custody log that records every handoff (who, when, why, how). Any unexplained gap becomes a challenge in court, so integrity is a continuous band under all six stages — not a final formality — and it is what makes the evidence believable.",
    "chain of custody · integrity · hashing · sealed evidence · custody log · continuous not a checkbox")

add_activity("S39 — 'Order the stages'  ·  ~5 min",
    ["In pairs (2 min): I give you the six stages shuffled — put them in the correct order.",
     "For each stage, write one sentence on what it produces for the next stage.",
     "Take answers aloud (3 min); fix any that swap collection/examination.",
     "Close: point to which single stage, if skipped, most often destroys a case (preservation)."],
    "Correct order: identify -> preserve -> collect -> examine -> analyse -> report. Common error is merging collection and examination. Draw out that preservation is the one-shot, case-ending stage.",
    "ACTIVITY [~5 min].")
add_quiz("S39 — Quick Check  ·  ~5 min",
    [("Q1.  Which is the correct order of the forensic process?","q"),
     ("a) collect→identify→report   b) ✅ identify→preserve→collect→examine→analyse→report   c) analyse→collect→report   d) report→collect","a"),
     ("     Why: it is a fixed, documented sequence; preservation and collection make the later analysis admissible.","o"),
     ("Q2.  The forensic report must be written primarily for:","q"),
     ("a) other engineers   b) ✅ a non-technical audience such as a judge/lawyer   c) the suspect   d) the media","a"),
     ("     Why: the court decides the case, so the report must be clear and defensible to non-technical readers.","o"),
     ("Discussion: which single stage, if skipped, most often destroys a case — and why?","o")],
    "QUIZ [~5 min]. Land that preservation is usually the case-ending skip — lost volatile evidence cannot be re-collected.")
add_summary("S39 · Summary  ·  [~2 min]",
    ["Forensics follows a fixed, documented sequence: identify → preserve → collect → examine → analyse → report.",
     "Preservation protects everything downstream; a skipped stage silently poisons the rest.",
     "Integrity and chain of custody thread through all six stages — a continuous band, not a final checkbox."],
    "The same disciplined-process thinking applies to incident response in any company breach, not just police work — a clean, documented process is what turns a mess into a defensible account.",
    "S40 — what actually counts as digital evidence, and the lab that handles it.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S40
add_divider("Session 40 · Lecture hour 3 (of 7)","Role of Digital Evidence · Methods and the Forensic Lab",
    "A deleted message, a GPS log, a thumbnail cache, a router log — which of these convicted someone? All of them have. What turns ordinary data into EVIDENCE?",
    "OPENING HOOK [~5 min]. Draw out what makes data 'evidence'. Agenda: what counts as digital evidence -> methods & tools -> the forensic lab.")

concept_understand("S40 · Concept 1 · [THEORY]","What Counts as Digital Evidence",
    "Digital evidence is any data stored or transmitted in digital form that can support or refute a fact in a case. Types include files, metadata, logs, chats/email, images/video, location data, and deleted/residual data. Good evidence is admissible, authentic, complete, reliable and believable.",
    ["Evidence can be visible (a chat) or hidden (metadata, a thumbnail cache, a log).",
     "Five properties of good evidence: admissible, authentic, complete, reliable, believable.",
     "It must be lawfully obtained and unaltered to keep those properties.",
     "Encryption is NOT a required property — it's how you protect it, not what makes it evidence."],
    "s40_evidence.png","Evidence = data that supports/refutes a fact; good = admissible, authentic, complete, reliable, believable.",
    "~8 min. Use the evidence-sources map. Stress the five properties — and that a bare screenshot fails 'reliable/authentic'.")
add_table_slide("S40 · Concept 1 · scaffolding","Types of digital evidence — where it lives and what it proves",
    ["Type","Where it lives","What it can prove (Nepal example)"],
    [["Files / documents","Disk, phone, cloud","A forged invoice in a fraud case"],
     ["Metadata","Inside the file (author, timestamps, GPS)","When/where a photo was really taken"],
     ["Logs","System, router, server, app","Which account logged in, and when"],
     ["Chats / email","App databases, mail servers","A blackmail or harassment conversation"],
     ["Location / GPS","Phone, app history, CDRs (NTC/Ncell)","A suspect's movements at a key time"],
     ["Deleted / residual","Slack & unallocated space","Data a suspect tried to destroy"]],
    per_page=6,widths=[1.7,2.5,3.1],fs=11,
    note="Much of the strongest evidence is hidden (metadata, logs, deleted residue) — not the obvious visible file. That is why forensic imaging captures the whole device, not just what's on screen.")
concept_apply("S40 · Concept 1 · [THEORY]","What Counts as Digital Evidence",
    "In Nepali fraud and harassment cases, chat screenshots, call detail records (CDRs) from NTC/Ncell, and mobile photos with metadata are used as evidence — but only the forensically extracted originals carry the authenticity a court needs. A CDR from the telco is far stronger than a phone screenshot.",
    "\"A screenshot is solid proof.\" Screenshots are easily faked and lack metadata, so they are weak on their own. They become strong only when backed by a forensically extracted original (the actual message record, with metadata and a chain of custody).",
    "Digital evidence is any data stored or transmitted digitally that can support or refute a fact in a case — files, metadata, logs, chats, images, location data, and deleted/residual data. Good evidence is admissible, authentic, complete, reliable and believable (encryption is not one of these). A bare screenshot is weak because it is fakeable and lacks metadata; a forensically extracted original is strong.",
    "digital evidence · admissible/authentic/complete/reliable/believable · metadata · CDR · screenshots are weak")

concept_understand("S40 · Concept 2 · [THEORY]","Methods & Tools Overview",
    "The standard methods are imaging, hashing, keyword search, and timeline/artifact analysis, supported by tool categories: imaging tools, write blockers, analysis suites, and mobile tools. Tools are introduced by CATEGORY — the methodology matters far more than the brand.",
    ["Imaging tools make the bit-for-bit copy; write blockers protect the original.",
     "Analysis suites: Autopsy/The Sleuth Kit (open source); EnCase, FTK (commercial).",
     "Mobile tools (e.g. Cellebrite) extract data from phones.",
     "A valid method with a free tool beats a sloppy method with an expensive one."],
    None,"Methodology, not brand, decides admissibility — a free tool used well is fully valid.",
    "~7 min. Mini case: a team has only Autopsy and a tight budget. Can they do valid forensics? Yes — sound method matters more than the tool's price tag.")
add_table_slide("S40 · Concept 2 · scaffolding","Forensic tool → what it is used for",
    ["Tool / category","What it does","Open / commercial"],
    [["Write blocker","Read a drive while blocking any write","Hardware or software"],
     ["Imaging tool (dd, FTK Imager)","Make a bit-for-bit forensic copy","Free & commercial"],
     ["Autopsy / The Sleuth Kit","Analyse disk images, timelines, carving","Open source (free)"],
     ["EnCase","Commercial analysis suite, court-tested","Commercial"],
     ["FTK","Commercial analysis & indexing suite","Commercial"],
     ["Cellebrite / mobile kit","Extract data from phones & SIMs","Commercial"]],
    per_page=6,widths=[2.1,3.0,1.7],fs=11,
    note="Know these by CATEGORY, not deep operation. A court cares that the method is sound, documented and repeatable — not which brand's logo is on the tool.")
concept_apply("S40 · Concept 2 · [THEORY]","Methods & Tools Overview",
    "A small Nepali investigation team with only free tools (Autopsy/The Sleuth Kit, FTK Imager) and a tight budget can still do fully valid forensics — because admissibility rests on the method (write-blocked imaging, hashing, documentation, repeatability), not on owning EnCase or FTK.",
    "\"Real forensics needs expensive commercial software.\" Admissibility depends on sound, documented, repeatable methodology — not the price of the tool. A free tool used with discipline is just as admissible as a costly one used sloppily.",
    "The standard forensic methods are imaging, hashing, keyword search, and timeline/artifact analysis, supported by tool categories: write blockers, imaging tools, analysis suites (Autopsy/Sleuth Kit open-source; EnCase, FTK commercial) and mobile tools (Cellebrite). Tools are chosen by category, and admissibility rests on the soundness of the method — not the brand or cost of the software.",
    "imaging · hashing · keyword search · timeline analysis · Autopsy/EnCase/FTK/Cellebrite · method over brand")

concept_understand("S40 · Concept 3 · [THEORY]","The Forensic Lab",
    "A forensic lab is a controlled environment ensuring integrity, security and accreditation. It needs physical security, access control, evidence storage/lockers, isolated (air-gapped) analysis machines, thorough documentation, and ideally accreditation such as ISO/IEC 17025.",
    ["Physical security & access control: only authorised staff reach evidence.",
     "Locked evidence storage keeps exhibits sealed and logged.",
     "Air-gapped analysis machines stop contamination, malware and remote wiping.",
     "Accreditation (ISO/IEC 17025) signals the lab's results are trustworthy."],
    None,"A forensic lab is a 'clean room for truth' — it avoids contaminating the data, as a hospital lab avoids contaminating a blood sample.",
    "~7 min. Contrast the Cyber Bureau lab with a district thana that lacks any lab access. The clean-room analogy carries the intuition.")
add_table_slide("S40 · Concept 3 · scaffolding","What a forensic lab needs — and why",
    ["Lab feature","What it provides","Why it matters"],
    [["Physical security","Locked, monitored premises","Stops unauthorised access to evidence"],
     ["Access control","Only trained staff enter","Narrows who could contaminate/tamper"],
     ["Evidence lockers","Sealed, logged storage","Preserves chain of custody"],
     ["Air-gapped machines","Analysis PCs off the network","No malware, remote wipe, or contamination"],
     ["Documentation","Full records of every action","Repeatability & defensibility"],
     ["ISO/IEC 17025","Accreditation of competence","Court trust in the lab's results"]],
    per_page=6,widths=[1.9,2.6,2.8],fs=11,
    note="Nepal's Cyber Bureau runs the central lab; many district-level investigations lack lab access entirely — a real capacity gap that pushes work back to the Bureau and slows cases.")
concept_apply("S40 · Concept 3 · [THEORY]","The Forensic Lab",
    "The Nepal Police Cyber Bureau operates the central forensic lab; district-level investigations that lack lab access must route devices to it, creating delay and backlog. A proper lab (locked storage, air-gapped machines, documentation) is what keeps analysis from contaminating the evidence.",
    "\"Any IT technician with a good PC can do forensic analysis.\" Without a controlled lab — access control, sealed storage, air-gapped machines, accreditation — the evidence can be contaminated or challenged. The environment is part of the integrity, not an optional extra.",
    "A forensic lab is a controlled environment that guarantees integrity, security and (ideally) accreditation: physical security, access control, sealed evidence lockers, air-gapped analysis machines, full documentation, and ISO/IEC 17025 accreditation. It is a 'clean room for truth' — like a hospital lab avoiding a contaminated blood sample. In Nepal the Cyber Bureau runs the central lab, and district capacity is limited.",
    "forensic lab · access control · air-gapped machines · sealed lockers · ISO/IEC 17025 · Cyber Bureau central lab")

add_activity("S40 — 'Screenshot vs extracted original'  ·  ~5 min",
    ["In pairs (2 min): a complainant brings a chat screenshot. List why it is weak evidence on its own.",
     "Then list what a forensic extraction would add that a screenshot lacks.",
     "Take 3–4 answers aloud (3 min).",
     "Close: name the five properties of good evidence and check the screenshot against them."],
    "Screenshot weaknesses: easily edited, no metadata, no proof of source/time, no chain of custody. Extraction adds the original record, metadata, hashes and a custody log — moving it from 'believable maybe' to authentic/reliable.",
    "ACTIVITY [~5 min].")
add_quiz("S40 — Quick Check  ·  ~5 min",
    [("Q1.  Which property is NOT required of good digital evidence?","q"),
     ("a) authentic   b) complete   c) reliable   d) ✅ that it be encrypted","a"),
     ("     Why: good evidence is admissible, authentic, complete, reliable and believable — encryption isn't a property of it.","o"),
     ("Q2.  A bare screenshot is considered weak evidence mainly because:","q"),
     ("a) it's too large   b) ✅ it can be faked and lacks original metadata   c) it's in colour   d) courts ban images","a"),
     ("     Why: without metadata and a chain of custody a screenshot can't prove it is authentic and unaltered.","o"),
     ("Discussion: why might a free tool like Autopsy be just as admissible as expensive commercial software?","o")],
    "QUIZ [~5 min]. Land that admissibility rests on method (imaging, hashing, documentation, repeatability), not on the tool's brand or price.")
add_summary("S40 · Summary  ·  [~2 min]",
    ["Digital evidence = data that supports/refutes a fact; good evidence is admissible, authentic, complete, reliable, believable.",
     "Methods (imaging, hashing, keyword search, timeline analysis) and tools matter by category — method beats brand.",
     "A forensic lab (access control, sealed storage, air-gapped machines, accreditation) keeps evidence uncontaminated."],
    "Understanding evidence quality helps you, as a future IT professional, log and preserve data correctly when something goes wrong on your own systems — good logs today are the evidence you'll need tomorrow.",
    "S41 — how to collect, seize and protect evidence without altering it.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S41
add_divider("Session 41 · Lecture hour 4 (of 7)","Collecting, Seizing and Protecting Evidence",
    "A phone is seized still switched on, screen unlocked, connected to Wi-Fi. Do you turn it off? Leave it on? Either choice can destroy evidence. What's the rule?",
    "OPENING HOOK [~5 min]. This session is the unit's spine — integrity. Agenda: chain of custody -> seizing devices correctly (order of volatility) -> write blockers & hashing.")

concept_understand("S41 · Concept 1 · [THEORY]","Chain of Custody — the Unit's Spine",
    "Chain of custody is the documented, unbroken record of who handled evidence, when, why and how — from seizure to court. Every transfer is logged; evidence is sealed in labelled bags with a custody form; any gap becomes a challenge in court.",
    ["Record every handoff: who, when, why, how — no undocumented gaps.",
     "Seal and label evidence in tamper-evident bags at seizure.",
     "A custody form travels with the exhibit through the whole journey.",
     "An unexplained gap lets the defence argue the evidence was tampered with."],
    "s41_custody.png","Chain of custody = an unbroken, logged handoff from seizure to court; a gap is challengeable.",
    "~8 min. Present the custody handoff chain. The relay-baton idea from S39 returns — every handoff signed.")
add_table_slide("S41 · Concept 1 · scaffolding","A chain-of-custody log — what each entry records",
    ["Log field","What it captures","Why the court needs it"],
    [["Who","Every person who held the exhibit","Names each link in the chain"],
     ["When","Date & time of each transfer","Shows no unexplained time gaps"],
     ["Why","Reason for the handoff","Justifies each access to the evidence"],
     ["How","Sealed bag, hash, transport method","Proves it couldn't be altered in transit"],
     ["Seal / label","Tamper-evident bag & unique ID","Any broken seal is immediately visible"],
     ["Signature","Sign-off at each handoff","Makes each person accountable"]],
    per_page=6,widths=[1.6,2.8,2.9],fs=11,
    note="A complete log is the proof of integrity. In Nepal, untrained officers seizing phones at a local thana without tagging/sealing/logging is a common weakness that hands the defence an easy challenge.")
concept_apply("S41 · Concept 1 · [THEORY]","Chain of Custody — the Unit's Spine",
    "The Cyber Bureau's procedure tags, seals and logs a seized device before transport. The weakness appears earlier: an untrained officer at a local thana who seizes a phone without tagging or logging it creates a custody gap that can sink an otherwise strong case.",
    "\"Chain of custody is just bureaucratic paperwork.\" It is the proof the evidence wasn't tampered with — without it, even perfect data is worthless. A single unexplained gap can make damning evidence inadmissible.",
    "Chain of custody is the documented, unbroken record of who handled evidence, when, why and how, from seizure to court — every transfer logged, evidence sealed in labelled tamper-evident bags, a custody form travelling with the exhibit. Any unexplained gap becomes a court challenge, so it is the proof of integrity, not mere paperwork — without it even perfect data is worthless.",
    "chain of custody · who/when/why/how · sealed & labelled · custody form · a gap = challengeable · proof of integrity")

concept_understand("S41 · Concept 2 · [THEORY]","Seizing Devices Correctly (Order of Volatility)",
    "Seizing correctly means capturing a device in a state that preserves its data. Photograph the scene and screen; decide power-on vs power-off (live RAM data vs remote-wipe risk); isolate from networks (Faraday bag/airplane mode); and follow the order of volatility — capture the most fragile data first.",
    ["Photograph everything first: the scene, the screen, cables, what's running.",
     "Order of volatility: RAM & live connections vanish first — capture before disk.",
     "Isolate immediately (Faraday bag/airplane mode) to stop remote wipe and syncing.",
     "Power-off can re-lock an encrypted disk; power-on risks a remote wipe — decide deliberately."],
    "s41_volatility.png","Isolate the device, photograph it, and collect most-volatile data (RAM) before durable data (disk).",
    "~8 min. Present the order-of-volatility ladder. Mini case: powering down a running, full-disk-encrypted laptop re-locks it with an unknown password.")
add_table_slide("S41 · Concept 2 · concrete examples","Seizure decisions — what's at stake either way",
    ["Situation at the scene","Wrong move","Right move (why)"],
    [["Laptop on, full-disk encryption unlocked","Power it off → disk re-locks","Live-acquire RAM/keys first, then image"],
     ["Phone on, connected to Wi-Fi","Leave it online","Airplane mode / Faraday bag → stop remote wipe"],
     ["Suspect's screen shows an open app","Close it 'to be tidy'","Photograph it first — that state is evidence"],
     ["Running processes / network connections","Ignore (grab disk only)","Capture RAM first — most volatile"],
     ["Device warm, possibly syncing to cloud","Wait and finish paperwork","Isolate now — cloud may delete the chat"],
     ["USB/SD card in the device","Forget it","Log, seize and image it too"]],
    per_page=6,widths=[2.4,2.2,3.0],fs=11,
    note="Order of volatility: RAM and live network state vanish first, disk survives longer, backups longest. Powering down first can destroy live evidence AND re-lock an encrypted disk — decide power state deliberately.")
concept_apply("S41 · Concept 2 · [THEORY]","Seizing Devices Correctly",
    "An officer powers down a running laptop protected by full-disk encryption; the disk re-locks and the password is unknown, so the live-acquisition opportunity — capturing the decrypted data and RAM while it was unlocked — is lost forever. The right move was to isolate it from networks and acquire live first.",
    "\"Always switch a seized device off to be safe.\" Powering down destroys volatile RAM evidence and can re-lock an encrypted disk you'll never get back into. Power decisions must be deliberate — isolate from networks first (Faraday/airplane mode), then choose based on encryption and what's running.",
    "Seizing a device correctly means preserving its data state: photograph the scene and screen, isolate from networks (Faraday bag/airplane mode) to stop remote wiping and syncing, and follow the order of volatility — capture the most fragile data (RAM, live connections) before durable data (disk, backups). Power-on vs power-off is a deliberate choice, since powering down can lose live data and re-lock encryption.",
    "seize correctly · photograph first · Faraday/airplane mode · order of volatility · live acquisition · power decision")

concept_understand("S41 · Concept 3 · [THEORY]","Protecting Integrity — Write Blockers & Hashing",
    "A write blocker is hardware/software that lets you read a drive but blocks any write to it. Hashing (MD5/SHA-256) is a digital fingerprint proving data is unchanged. Hash the original at collection and hash the copy — matching hashes prove the image is an identical, untouched duplicate.",
    ["Write blocker: one-way — read the original, never write back to it.",
     "Hash the original at collection; hash the forensic image afterwards.",
     "Matching hashes = the copy is bit-for-bit identical and unaltered.",
     "Change one byte and the hash changes visibly — tampering is detectable."],
    "s41_hashing.png","Write blocker keeps the original read-only; matching hashes prove the copy is identical & untouched.",
    "~8 min. Present the write-blocker + hash-match diagram. A Nepali expert in court shows identical SHA-256 hashes to prove the analysed copy equals the seized original.")
add_table_slide("S41 · Concept 3 · comparison","Write blocker vs hashing — two different integrity guards",
    ["Question","Write blocker","Hashing (MD5/SHA-256)"],
    [["What it is","Hardware/software that blocks writes","A mathematical fingerprint of the data"],
     ["When used","During imaging of the original","At collection, then re-checked later"],
     ["Protects against","Accidentally altering the original","Undetected change to the copy"],
     ["Proves","The original was never written to","The copy is identical, bit-for-bit"],
     ["Analogy","A one-way valve","A tamper-evident seal on a bottle"],
     ["If it fails","The original could be altered","A mismatch flags tampering/corruption"]],
    per_page=6,widths=[1.7,2.6,3.0],fs=11,
    note="They work together: the write blocker prevents alteration during imaging; the hash proves, afterwards and in court, that the copy still equals the original. Neither alone is enough.")
concept_apply("S41 · Concept 3 · [THEORY]","Protecting Integrity — Write Blockers & Hashing",
    "In a Nepali court, a forensic expert demonstrates identical SHA-256 hashes for the seized original and the analysed copy — visual proof that the copy is an exact, unaltered duplicate. A write blocker ensured the original was never written to while that image was made.",
    "\"If the analyst is careful, hashing and write blockers aren't really needed.\" Care is not proof. Only a write blocker guarantees the original wasn't altered, and only a matching hash proves it to a court — 'trust me, I was careful' is not defensible evidence.",
    "A write blocker is hardware/software that allows reading a drive while blocking any write to it, and hashing (MD5/SHA-256) is a digital fingerprint that proves data is unchanged. You hash the original at collection and hash the copy: matching hashes prove the image is an exact, unaltered duplicate, while the write blocker guarantees the original was never modified during imaging.",
    "write blocker · read-only · hashing · MD5/SHA-256 · matching hashes = identical copy · technical proof of integrity")

add_activity("S41 — 'A minute online — what could go wrong?'  ·  ~5 min",
    ["In pairs (2 min): a seized phone is left connected to the internet 'just for a minute.'",
     "List everything that could go wrong in that minute.",
     "Take 3–4 answers aloud (3 min); sort them into remote-wipe, sync/delete, and tamper.",
     "Close: this is exactly why isolation (Faraday/airplane mode) is the first protective step."],
    "Seeds: remote wipe triggered; cloud deletes/edits a chat; new messages overwrite old ones; location updates; someone signs the account out. Each is irreversible — the reason to isolate immediately at seizure.",
    "ACTIVITY [~5 min].")
add_quiz("S41 — Quick Check  ·  ~5 min",
    [("Q1.  The purpose of a write blocker is to:","q"),
     ("a) speed up copying   b) ✅ allow reading a drive while preventing any change to it   c) encrypt the disk   d) delete data","a"),
     ("     Why: it is a one-way guard so imaging never alters the original evidence.","o"),
     ("Q2.  Identical hash values of the original and the copy prove that:","q"),
     ("a) the data is encrypted   b) ✅ the copy is an exact, unaltered duplicate   c) the drive is empty   d) nothing","a"),
     ("     Why: a hash is a fingerprint — matching hashes mean not one byte differs.","o"),
     ("Discussion: a seized phone is left connected to the internet 'just for a minute' — list everything that could go wrong.","o")],
    "QUIZ [~5 min]. Draw out that isolation is the first protective step and that write blocker + hash together are the technical proof of integrity.")
add_summary("S41 · Summary  ·  [~2 min]",
    ["Chain of custody is the proof of integrity — an unbroken, logged handoff — not mere paperwork.",
     "Seize devices without altering them: photograph, isolate networks, follow order of volatility, decide power carefully.",
     "Write blockers + hashing guarantee and prove the original is untouched and the copy is identical."],
    "The same hashing idea verifies the downloads and backups you use daily, and a custody mindset protects you whenever you handle sensitive company data — integrity habits transfer straight into professional IT work.",
    "S42 — how investigators recover data that someone tried to delete.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S42
add_divider("Session 42 · Lecture hour 5 (of 7)","Recovering Data (conceptual)",
    "A suspect 'deletes everything' and empties the recycle bin, confident it's gone. Investigators recover it in an hour. Where was it hiding?",
    "OPENING HOOK [~5 min]. Land that deletion ≠ erasure. Agenda: why 'deleted' isn't gone -> disk imaging -> file carving.")

concept_understand("S42 · Concept 1 · [THEORY]","Why 'Deleted' Isn't Gone",
    "Deleting a file usually removes the pointer/index entry, not the actual data — the bytes stay until overwritten. The file system just marks that space as 'free'; until it's reused, the data remains recoverable. (SSD TRIM and full-disk encryption complicate this.)",
    ["Delete = remove the label from the box; the box (data) stays until reused.",
     "A quick format or empty-recycle-bin leaves most data recoverable.",
     "Only overwriting or a secure wipe truly destroys data.",
     "SSD TRIM and full-disk encryption can make recovery harder — a real nuance."],
    None,"'Delete' removes the label, not the box — the data stays until something overwrites it.",
    "~8 min. Misconception-first: students believe emptying the bin erases data. Land that it only frees the space; recovery is routine until overwrite.")
add_table_slide("S42 · Concept 1 · concrete examples","Does this really destroy the data? (Nepal / IT)",
    ["Action taken","Really destroyed?","Why (verdict)"],
    [["Delete a file & empty the recycle bin","No","Only the pointer is gone; bytes remain"],
     ["Quick format a USB drive","No","Rebuilds the index; most data still recoverable"],
     ["Factory reset an old phone (then sell it)","Often no","Traces + cloud backup can remain → data leak"],
     ["Overwrite the whole drive (secure wipe)","Yes","Every byte is replaced — nothing to recover"],
     ["Physically destroy / shred the disk","Yes","No medium left to read"],
     ["Full-disk encryption + destroy the key","Effectively yes","Data is unreadable without the key"]],
    per_page=6,widths=[2.6,1.7,3.0],fs=11,
    note="'Deleted' and 'formatted' are recoverable; only overwriting, secure-wipe, physical destruction, or discarding the encryption key truly destroys data. This is why a factory-reset resold phone can still leak your photos.")
concept_apply("S42 · Concept 1 · [THEORY]","Why 'Deleted' Isn't Gone",
    "In Nepali cases, suspects who 'delete everything' and empty the recycle bin are routinely undone: until the space is overwritten, the bytes remain and are recoverable in an hour. The same fact means a resold, factory-reset phone can still leak the previous owner's photos.",
    "\"Emptying the recycle bin / formatting permanently destroys data.\" A quick format and a delete leave most data recoverable — only overwriting, secure-wiping, or destroying the disk (or its encryption key) truly erases it.",
    "Deleting a file usually removes only the pointer/index entry, not the data itself; the file system marks the space 'free' and the bytes stay until overwritten, so 'deleted' and 'quick-formatted' data is normally recoverable. Only overwriting, secure-wiping, physical destruction, or discarding the encryption key truly destroys it. SSD TRIM and full-disk encryption complicate recovery.",
    "deletion ≠ erasure · pointer removed, data stays · until overwritten · secure wipe · SSD TRIM · encryption")

concept_understand("S42 · Concept 2 · [THEORY]","Disk Imaging (Forensic Copy)",
    "A disk image is a bit-for-bit copy of an entire drive — including slack and unallocated space, not just the visible files. You image first (with a write blocker, then hash), then analyse the image — never the original. A physical image copies everything; a logical copy takes only chosen files.",
    ["Bit-for-bit: every sector, including 'empty' space where deleted data hides.",
     "Image with a write blocker, hash it, then work only on the copy.",
     "Physical image = the whole disk; logical copy = selected files/folders only.",
     "Imaging the whole disk is what makes deleted-data recovery possible."],
    "s42_imaging.png","Image the WHOLE disk bit-for-bit (incl. slack/unallocated), hash it, and analyse the copy — never the original.",
    "~8 min. Present the imaging diagram. Mini case: why image the whole disk, including 'empty' space, rather than just copy the visible files?")
add_table_slide("S42 · Concept 2 · comparison","Physical image vs logical copy — and why forensics prefers the image",
    ["Dimension","Physical (bit-for-bit) image","Logical copy"],
    [["What it captures","Every sector, incl. slack & unallocated","Only chosen files/folders"],
     ["Deleted data","Preserved (recoverable)","Lost — not copied"],
     ["Hash verification","Whole-disk hash proves integrity","Weaker — misses hidden areas"],
     ["Size / effort","Large, slower","Small, quick"],
     ["Forensic value","High — the standard for evidence","Limited — triage only"],
     ["Nepal example","Image a seized fraud-case hard disk/USB","Grab a few named files for a quick check"]],
    per_page=6,widths=[1.8,3.0,2.6],fs=11,
    note="Forensics prefers the physical image because deleted/residual data lives in slack and unallocated space — exactly what a logical copy of 'visible files' would miss. Image first, keep the original sealed.")
concept_apply("S42 · Concept 2 · [THEORY]","Disk Imaging (Forensic Copy)",
    "In a Nepali financial-fraud investigation, the seized hard disk/USB is imaged bit-for-bit and hashed so the original stays sealed, and all analysis runs on the copy. Imaging the WHOLE disk — including 'empty' space — is what preserves the deleted records the suspect hoped were gone.",
    "\"Just copy the important files off the disk — that's enough.\" Copying only visible files misses deleted data in slack and unallocated space and produces no whole-disk hash. A forensic physical image captures everything and proves integrity; a file copy doesn't.",
    "A disk image is a bit-for-bit copy of an entire drive, including slack and unallocated space — made with a write blocker, hashed, and then analysed in place of the original. A physical image captures every sector (so deleted data is preserved and integrity is provable); a logical copy takes only selected files and misses hidden areas. Imaging the whole disk is what makes deleted-data recovery possible.",
    "disk image · bit-for-bit · slack & unallocated space · physical vs logical · hash · analyse the copy")

concept_understand("S42 · Concept 3 · [THEORY]","File Carving",
    "File carving reconstructs files from raw data using file signatures (headers/footers) when the file-system metadata is gone. For example a JPEG always starts with a known header and ends with a known footer; carving scans unallocated space for these signatures to rebuild files without the index.",
    ["Every file type has a signature: e.g. a JPEG header (FF D8) and footer (FF D9).",
     "Carving scans raw bytes for these markers, ignoring the missing index.",
     "It rebuilds files even when the file system no longer lists them.",
     "It's how deleted photos/documents are recovered from unallocated space."],
    "s42_carving.png","File carving rebuilds files by their header/footer signatures — no file-system index needed.",
    "~7 min. Present the carving diagram. The shredded-document analogy: reassemble by recognising edges and patterns even though the labelled folder is gone.")
add_table_slide("S42 · Concept 3 · scaffolding","File carving — signatures rebuild files without an index",
    ["File type","Signature clue","What carving recovers"],
    [["JPEG image","Header FF D8 … footer FF D9","Deleted photos from unallocated space"],
     ["PNG image","Header 89 50 4E 47","Deleted screenshots/graphics"],
     ["PDF document","Header %PDF … trailer %%EOF","Deleted documents/receipts"],
     ["ZIP / Office file","Header PK\\x03\\x04","Deleted archives & docx/xlsx"],
     ["MP4 video","'ftyp' box near the start","Deleted video clips"],
     ["No index needed","Scans raw bytes for signatures","Files the file system no longer lists"]],
    per_page=6,widths=[1.8,2.6,3.0],fs=11,
    note="Carving relies on content signatures, not the file-system index — so it works precisely when 'delete' or a format has removed the index but left the bytes behind.")
concept_apply("S42 · Concept 3 · [THEORY]","File Carving",
    "When a suspect deletes photos and the file-system index no longer lists them, an analyst carves the unallocated space of the disk image — scanning for JPEG headers (FF D8) and footers (FF D9) — and rebuilds the images without any index. It is how 'deleted' media is routinely recovered.",
    "\"If the file isn't in the index, it's gone.\" File carving recovers files by recognising their signatures in raw data, with no reliance on the file-system index — so data can be rebuilt even after the index entry is deleted, as long as the bytes aren't overwritten.",
    "File carving reconstructs files from raw data using file signatures (headers/footers) when the file-system metadata is gone — for example scanning unallocated space for a JPEG's FF D8 header and FF D9 footer to rebuild the image without any index. It is like reassembling a shredded document by its edges, and it is how deleted photos and documents are recovered.",
    "file carving · file signatures · header/footer · unallocated space · no index needed · JPEG FF D8/FF D9")

add_activity("S42 — 'Dispose of your old device'  ·  ~5 min",
    ["In pairs (2 min): if deletion rarely erases data, how should you properly dispose of an old laptop or phone?",
     "List the steps that would actually stop your data being recovered.",
     "Take 3–4 answers aloud (3 min); rank them from weak (delete) to strong (destroy/encrypt+wipe).",
     "Close: connect to Unit 2 privacy — a resold factory-reset phone can still leak photos."],
    "Strong answers: full secure-wipe/overwrite, or full-disk encryption then wipe/destroy the key, or physical destruction for sensitive media. Weak: delete, empty bin, quick format, plain factory reset. Always wipe BEFORE resale/disposal.",
    "ACTIVITY [~5 min].")
add_quiz("S42 — Quick Check  ·  ~5 min",
    [("Q1.  When a file is 'deleted', what usually happens?","q"),
     ("a) bytes are overwritten instantly   b) ✅ the pointer is removed but the data remains until overwritten   c) the disk shrinks   d) nothing at all","a"),
     ("     Why: the file system just marks the space free; recovery works until that space is reused.","o"),
     ("Q2.  File carving recovers files by:","q"),
     ("a) reading the index   b) ✅ recognising file signatures in raw data, without the file-system index   c) asking the OS   d) decrypting them","a"),
     ("     Why: signatures (e.g. a JPEG header/footer) let carving rebuild files even when the index is gone.","o"),
     ("Discussion: if deletion rarely erases data, how should you properly dispose of an old laptop or phone?","o")],
    "QUIZ [~5 min]. Land deletion ≠ erasure and connect to privacy — secure-wipe or destroy before disposal, never just delete or factory-reset.")
add_summary("S42 · Summary  ·  [~2 min]",
    ["Deletion removes the pointer, not the data — 'deleted' and 'formatted' stay recoverable until overwritten.",
     "Always work from a hashed, bit-for-bit disk image (incl. slack/unallocated), never the original.",
     "File carving rebuilds files from their header/footer signatures, without the file-system index."],
    "This is why selling a phone after a factory reset can still leak your photos — and why secure-wiping (or destroying the encryption key) matters before you dispose of any device.",
    "S43 — the device at the centre of most Nepali cases: the mobile phone.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S43
add_divider("Session 43 · Lecture hour 6 (of 7)","Mobile Forensics",
    "Your phone knows where you slept, who you texted at 2am, what you searched, and which photos you 'deleted.' In most Nepali cyber cases today the phone IS the crime scene. How do investigators get evidence out of it — legally?",
    "OPENING HOOK [~5 min]. Land that the phone is today's primary crime scene. Agenda: why mobile is its own discipline -> extraction methods & app data -> challenges & integrity.")

concept_understand("S43 · Concept 1 · [THEORY]","Why Mobile Forensics Is Its Own Discipline",
    "Mobile forensics is extracting and analysing evidence from smartphones, tablets, SIMs and their apps. Phones are always-on, networked, encrypted, OS-locked, and store extraordinarily rich data — location, messages, app data, media and call logs — which makes them a distinct discipline from disk forensics.",
    ["Always-on & networked: constant risk of remote wipe and cloud sync.",
     "Encrypted & OS-locked: getting in is often the hardest part.",
     "Rich data: location history, chats, media metadata, app databases, call logs.",
     "Rapid change: new OS versions and apps break yesterday's techniques."],
    None,"A smartphone is a diary that writes and locks itself — read it without destroying the page.",
    "~8 min. Land that most Cyber Bureau complaints centre on phones. The self-writing-diary analogy carries why mobile is uniquely hard.")
add_table_slide("S43 · Concept 1 · concrete examples","Nepali cyber complaints — the phone as the crime scene",
    ["Complaint type (Nepal)","Where the evidence lives","What the phone reveals"],
    [["Online fraud / scam","eSewa/Khalti, SMS OTPs, bank app","Transactions, payee, timing"],
     ["Harassment / cyberbullying","Messenger, WhatsApp, Viber, TikTok","The abusive messages & who sent them"],
     ["Blackmail / sextortion","Gallery, chat apps, cloud backup","Images, threats, contact history"],
     ["Fake profile / impersonation","Facebook/Instagram app + logins","Account access, device linkage"],
     ["Financial dispute","Call logs + CDRs (NTC/Ncell)","Who contacted whom, and when"],
     ["Location alibi","Maps/app location history","Where the phone was at a key time"]],
    per_page=6,widths=[2.1,2.6,2.7],fs=11,
    note="Most Nepal Police Cyber Bureau complaints centre on mobile phones and apps (Facebook, Messenger, TikTok, WhatsApp, Viber, eSewa/Khalti) — the phone, not a PC, is the crime scene today.")
concept_apply("S43 · Concept 1 · [THEORY]","Why Mobile Forensics Is Its Own Discipline",
    "Most Nepal Police Cyber Bureau complaints — online fraud, harassment, blackmail, fake profiles — centre on mobile phones and apps like Facebook, Messenger, TikTok, WhatsApp, Viber and eSewa/Khalti. A single phone holds chats, location, media and wallet data, so mobile forensics is its own specialised field.",
    "\"A factory reset wipes the phone clean.\" Resets and 'deleted' chats can still leave recoverable traces, and cloud backups may persist entirely — so a reset is not a guarantee the data is gone, for investigators or for your own privacy.",
    "Mobile forensics is extracting and analysing evidence from smartphones, tablets, SIMs and apps. Phones are always-on, networked, encrypted, OS-locked, and hold uniquely rich data (location, messages, app data, media, call logs), which makes it a distinct discipline. In Nepal most Cyber Bureau complaints centre on phones and apps — the phone is today's primary crime scene.",
    "mobile forensics · always-on/networked/encrypted · rich data · SIM & apps · phone = crime scene · reset ≠ clean")

concept_understand("S43 · Concept 2 · [THEORY]","Extraction Methods & App Data",
    "There are levels of extraction: manual (scrolling/photographing), logical (via APIs/backups), file-system, and physical (a full image). More invasive levels yield more data but are harder. Key sources: chat/app databases (often SQLite), call logs, location history, media metadata, and cloud-synced data.",
    ["Manual: scroll and photograph — least data, no tools, but changes the device.",
     "Logical: use the phone's APIs/backups — moderate data, less invasive.",
     "File-system & physical: app databases and a full bit-for-bit image — most data.",
     "App data often lives in SQLite databases; cloud backups may hold the rest."],
    "s43_extraction.png","Extraction levels: manual → logical → file-system → physical (more data, but harder and more invasive).",
    "~8 min. Present the extraction pyramid. Mini case: a deleted WhatsApp chat — local DB fragments + cloud backup — how many places to check?")
add_table_slide("S43 · Concept 2 · comparison","The four extraction levels — data vs difficulty",
    ["Level","How it works","Data yield / trade-off"],
    [["Manual","Scroll & photograph the screen","Least data; quick but alters the device"],
     ["Logical","Via device APIs / backups","Moderate; less invasive, may miss deleted data"],
     ["File-system","Pull app databases & system files","More — reaches SQLite chat databases"],
     ["Physical","Full bit-for-bit image of storage","Most data (incl. deleted); hardest, needs access"],
     ["App databases","Read SQLite chat/app stores","Fragments of 'deleted' chats"],
     ["Cloud-synced","Lawfully obtain the backup","What the phone itself no longer holds"]],
    per_page=6,widths=[1.7,2.7,3.0],fs=11,
    note="The rule: the more invasive the level, the more data — but the harder it is (encryption, locks, access). Deleted chat evidence often survives in the app's SQLite database AND in the cloud backup.")
concept_apply("S43 · Concept 2 · [THEORY]","Extraction Methods & App Data",
    "A suspect deleted a WhatsApp chat, but the app's local SQLite database still holds fragments and the cloud backup has the rest. The investigator must check multiple places — device storage, the app database, and (lawfully) the cloud backup — because 'deleted from the chat view' rarely means deleted everywhere.",
    "\"If it's deleted in the app, it's gone from the phone.\" App data lives in local SQLite databases and often syncs to a cloud backup, so fragments and full copies commonly survive a chat 'deletion'. An investigator (and a privacy-conscious user) must think about every place the data was copied to.",
    "Extraction has levels — manual (scroll/photograph), logical (APIs/backups), file-system, and physical (full image) — where more invasive levels yield more data but are harder. Key sources are app databases (often SQLite), call logs, location history, media metadata, and cloud-synced data. Because a 'deleted' chat often survives in the local database and the cloud, investigators check multiple places.",
    "extraction levels · manual/logical/file-system/physical · SQLite app databases · cloud backup · more data = harder")

concept_understand("S43 · Concept 3 · [THEORY]","Challenges & Integrity in Mobile Forensics",
    "Mobile forensics faces unique obstacles: encryption, lock screens, constant connectivity (remote-wipe risk), OS/version diversity, and rapid app changes. Despite these, the integrity rules are unchanged — isolate immediately (Faraday bag/airplane mode), document, hash extractions, and maintain chain of custody as with disks.",
    ["Encryption & lock screens can block access entirely.",
     "Constant connectivity means remote wipe/sync — isolate first, always.",
     "OS and app diversity means no single technique fits every phone.",
     "The same integrity rules apply: isolate, document, hash, keep custody."],
    None,"New obstacles, same rules: isolate, hash, and keep custody exactly as with a disk.",
    "~7 min. Land that mobile is harder technically but the integrity discipline is identical — the Faraday bag from S41 returns here.")
add_table_slide("S43 · Concept 3 · scaffolding","Mobile-specific challenges — and the integrity response",
    ["Challenge","Why it's hard on mobile","Integrity response"],
    [["Encryption","Data unreadable without the key","Live-acquire while unlocked; lawful access"],
     ["Lock screen","Can't get in without the passcode","Isolate; document; use lawful means"],
     ["Constant connectivity","Remote wipe / cloud sync risk","Faraday bag / airplane mode immediately"],
     ["OS / version diversity","No single technique fits all","Document tool & method used; repeatability"],
     ["Rapid app changes","Yesterday's method breaks","Validate the tool; note versions"],
     ["Rich, mixed data","Easy to alter or miss","Hash extractions; work on copies; custody log"]],
    per_page=6,widths=[1.9,2.7,2.8],fs=11,
    note="The obstacles are new but the discipline is the same as disk forensics: isolate first, document everything, hash the extraction, and keep an unbroken chain of custody. Integrity does not get a mobile exemption.")
concept_apply("S43 · Concept 3 · [THEORY]","Challenges & Integrity in Mobile Forensics",
    "A seized phone in Kathmandu is placed in a Faraday bag the moment it's collected — blocking all signals so it can't be remotely wiped or synced — then documented, its extraction hashed, and every handoff logged. The obstacles (encryption, locks, connectivity) are new; the integrity rules are exactly those from S41.",
    "\"Mobile evidence is so messy that strict integrity rules don't really apply.\" They apply fully — isolate, document, hash, keep custody — precisely because phones are volatile and connected. If anything, the remote-wipe risk makes immediate isolation more urgent than with a disk.",
    "Mobile forensics faces unique challenges — encryption, lock screens, constant connectivity (remote-wipe risk), OS/version diversity and rapid app changes — but the integrity rules are unchanged: isolate immediately (Faraday bag/airplane mode), document, hash extractions, and maintain chain of custody just as with disks. The obstacles are new; the discipline is the same.",
    "mobile challenges · encryption/locks · remote-wipe risk · Faraday bag · same integrity rules · hash & custody")

add_activity("S43 — 'Where else does the chat live?'  ·  ~5 min",
    ["In pairs (2 min): besides the phone itself, where might 'deleted' chat evidence still exist?",
     "List every place a WhatsApp/Messenger message could be recovered from.",
     "Take 3–4 answers aloud (3 min); mark which need lawful authorisation to access.",
     "Close: connect to privacy — the same copies that help investigators can leak YOUR data."],
    "Seeds: local app SQLite database, device backup, cloud backup (Google/iCloud), the other party's phone, the platform's servers, and SMS/notification logs. Accessing cloud/platform data lawfully needs proper authorisation.",
    "ACTIVITY [~5 min].")
add_quiz("S43 — Quick Check  ·  ~5 min",
    [("Q1.  Which extraction type generally yields the MOST data?","q"),
     ("a) manual   b) logical   c) file-system   d) ✅ physical (full image)","a"),
     ("     Why: a full bit-for-bit image captures the most, including deleted data — but it's the hardest to obtain.","o"),
     ("Q2.  A seized phone is placed in a Faraday bag primarily to:","q"),
     ("a) charge it   b) ✅ block all signals so it can't be remotely wiped or synced   c) unlock it   d) hash it","a"),
     ("     Why: isolating the phone from networks preserves the evidence against remote wipe and cloud sync.","o"),
     ("Discussion: where, besides the phone itself, might 'deleted' chat evidence still exist?","o")],
    "QUIZ [~5 min]. Land the extraction-level trade-off (more data = harder) and that isolation is the first, urgent step on any seized phone.")
add_summary("S43 · Summary  ·  [~2 min]",
    ["Phones are today's primary crime scene and a discipline of their own (always-on, encrypted, data-rich).",
     "Extraction ranges from manual → logical → file-system → physical, with app SQLite databases & cloud as key sources.",
     "The same integrity rules still apply: isolate (Faraday bag), document, hash, and keep chain of custody."],
    "Understanding what your phone stores — and how recoverable it is — directly shapes how you protect your own privacy and how you dispose of old devices.",
    "S44 — the legal side: admissibility, the ETA 2063, and where Nepal stands on cyber forensics.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S44
add_divider("Session 44 · Lecture hour 7 (of 7) — CLOSES UNIT 8","Legal Aspects · Cyber Forensics in Nepal",
    "Investigators recover damning evidence — but the judge rules it inadmissible because of how it was handled. The criminal walks free. In Nepal, who is even allowed to do this work, and under which law?",
    "OPENING HOOK [~5 min]. Land that law decides whether good forensics matters. Agenda: legal admissibility -> Nepal's legal framework (ETA 2063) -> the state of cyber forensics in Nepal.")

concept_understand("S44 · Concept 1 · [THEORY]","Legal Admissibility of Digital Evidence",
    "Admissibility is the set of conditions under which a court will accept digital evidence: relevance, authenticity, integrity (chain of custody + hashing), proper authorisation (a search warrant/lawful seizure), and expert testimony. Mishandling — even of genuine evidence — makes it inadmissible.",
    ["Relevant: it must actually bear on a fact in the case.",
     "Authentic & integral: proven unaltered via custody log and hashes.",
     "Lawfully obtained: a valid warrant or lawful seizure — not an illegal search.",
     "Explained by a competent expert the court can question."],
    None,"Truth isn't enough — evidence must be relevant, authentic, intact AND lawfully obtained to be admitted.",
    "~8 min. Misconception-first: 'if it's true the court must accept it.' No — illegally obtained or mishandled evidence is excluded regardless of truth.")
add_table_slide("S44 · Concept 1 · scaffolding","The admissibility checklist — every box must be ticked",
    ["Condition","What it requires","If it fails"],
    [["Relevance","Bears on a fact in the case","Excluded as irrelevant"],
     ["Authenticity","Proven to be what it claims to be","Weight collapses; may be rejected"],
     ["Integrity","Chain of custody + matching hashes","Challenged as possibly tampered"],
     ["Lawful authorisation","Search warrant / lawful seizure","Excluded — 'fruit of unlawful search'"],
     ["Expert testimony","A competent expert explains it","Court can't rely on it"],
     ["Handling","Correct process throughout","Mishandling sinks even true evidence"]],
    per_page=6,widths=[1.9,2.9,2.6],fs=11,
    note="Every condition must hold at once. A single failure — an unlawful seizure, a custody gap, a hash mismatch — can make genuine, damning evidence inadmissible. Truth alone is never sufficient.")
concept_apply("S44 · Concept 1 · [THEORY]","Legal Admissibility of Digital Evidence",
    "A Cyber Bureau case where the seizure lacked proper authorisation, or the custody chain has an unexplained gap, can see genuine evidence excluded — and the accused walks free. The evidence being true does not save it; the court asks how it was obtained and whether it stayed intact.",
    "\"If the evidence is true, the court must accept it.\" Even genuine evidence is rejected if illegally obtained or improperly handled — a broken chain of custody or a warrantless seizure can exclude it entirely. Lawful process is as essential as the truth of the data.",
    "Admissibility is the set of conditions for a court to accept digital evidence: relevance, authenticity, integrity (chain of custody + hashing), proper authorisation (warrant/lawful seizure), and expert testimony. Mishandling makes even genuine evidence inadmissible — an unlawful seizure or a custody gap can exclude damning data entirely, so truth alone is never sufficient.",
    "admissibility · relevance/authenticity/integrity · lawful authorisation · warrant · expert testimony · truth isn't enough")

concept_understand("S44 · Concept 2 · [THEORY]","The Legal Framework in Nepal",
    "Nepal's electronic evidence is governed mainly by the Electronic Transaction Act (ETA) 2063 (2008), which recognises electronic records/evidence and defines cyber offences, alongside Evidence Act provisions and the courts' growing acceptance of electronic records. A dedicated, modern cybercrime/data-protection law is still debated.",
    ["ETA 2063 (2008) recognises electronic records as evidence and defines cyber offences.",
     "Evidence Act provisions and case practice support electronic records in court.",
     "Cybercrime complaints are prosecuted via the Cyber Bureau under the ETA.",
     "There is ongoing debate about a dedicated modern cybercrime/data-protection law (links to Unit 9)."],
    None,"In Nepal, electronic records are recognised as evidence mainly under the ETA 2063 (2008).",
    "~8 min. Mini case: a complainant brings only WhatsApp screenshots — what's needed before it's court-ready? Forward-link the ETA to Unit 9.")
add_table_slide("S44 · Concept 2 · scaffolding","Nepal's legal handles on digital evidence",
    ["Instrument / body","Role","Note"],
    [["ETA 2063 (2008)","Recognises e-records; defines cyber offences","The main legal basis for e-evidence"],
     ["Evidence Act provisions","Support acceptance of electronic records","Used alongside the ETA"],
     ["Nepal Police Cyber Bureau","Investigates & prosecutes cybercrime","Central body (est. 2018)"],
     ["Courts","Accept electronic records as evidence","Practice still maturing"],
     ["Warrant / lawful seizure","Authorises collection","Required for admissibility"],
     ["Proposed modern law","Dedicated cybercrime/data-protection","Still debated (Unit 9)"]],
    per_page=6,widths=[2.0,2.7,2.7],fs=11,
    note="The ETA 2063 is the backbone but predates today's mobile/cloud reality — hence the ongoing push for a dedicated, modern cybercrime and data-protection law, explored in Unit 9.")
concept_apply("S44 · Concept 2 · [THEORY]","The Legal Framework in Nepal",
    "A complainant brings only WhatsApp screenshots to the Cyber Bureau. Before it's court-ready under the ETA 2063, more is needed: forensic extraction of the original messages with metadata, hashing, a chain-of-custody record, and lawful authorisation — turning weak screenshots into authenticated, admissible evidence.",
    "\"The ETA 2063 automatically makes any electronic file valid evidence in court.\" The ETA recognises electronic records, but the evidence still has to be authentic, intact, and lawfully obtained. Screenshots alone don't clear that bar; forensic extraction and custody do.",
    "Nepal's electronic evidence is governed mainly by the Electronic Transaction Act (ETA) 2063 (2008), which recognises electronic records and defines cyber offences, together with Evidence Act provisions and courts' growing acceptance of e-records. The ETA recognises e-records, but evidence must still be authenticated, intact and lawfully obtained; a dedicated modern law is debated (Unit 9).",
    "ETA 2063 (2008) · recognises e-records · defines cyber offences · Evidence Act · Cyber Bureau · modern law debated")

concept_understand("S44 · Concept 3 · [THEORY]","Cyber Forensics in Nepal — State & Challenges",
    "Nepal's cyber forensics centres on the Nepal Police Cyber Bureau, facing a rising caseload (online fraud, social-media abuse, financial scams) against real constraints: limited trained personnel, tool/lab capacity, backlog, dependence on foreign platforms for data, and an evolving legal framework.",
    ["The Cyber Bureau is the central body; district capacity is thin.",
     "Caseload is rising fast — fraud, harassment, scams, fake profiles.",
     "Constraints: few trained experts, limited labs/tools, growing backlog.",
     "Much evidence sits on foreign platforms (Facebook, Google) — access is slow and dependent."],
    "s44_ecosystem.png","Complaint → Cyber Bureau → forensic lab → court under ETA 2063; capacity must scale with the caseload.",
    "~7 min. Present the Nepal ecosystem diagram. The fire-brigade analogy: sound principles, but capacity must grow with the digital population.")
add_table_slide("S44 · Concept 3 · scaffolding","Cyber forensics in Nepal — strengths and gaps",
    ["Area","Current state","Challenge / gap"],
    [["Central body","Cyber Bureau investigates cybercrime","Overloaded; district reach is limited"],
     ["Caseload","Rising fast (fraud, abuse, scams)","Backlog grows faster than capacity"],
     ["Personnel","A trained core team exists","Too few trained forensic experts"],
     ["Lab / tools","Central lab at the Bureau","Limited lab capacity beyond it"],
     ["Foreign data","Evidence on Facebook/Google etc.","Slow, dependent cross-border access"],
     ["Legal framework","ETA 2063 in force","Ageing; modern law still debated"]],
    per_page=6,widths=[1.7,2.7,2.9],fs=11,
    note="The principles are sound; the constraint is capacity. Like a small fire brigade facing a fast-growing city, Nepal's cyber forensics must scale personnel, labs and law with the rising digital caseload.")
concept_apply("S44 · Concept 3 · [THEORY]","Cyber Forensics in Nepal — State & Challenges",
    "The Nepal Police Cyber Bureau handles a fast-rising caseload of online fraud, social-media abuse and financial scams with limited trained staff, constrained lab capacity, a growing backlog, and slow dependence on foreign platforms for data — all under an ageing ETA 2063. The framework works; capacity is the bottleneck.",
    "\"Nepal can't do real cyber forensics.\" It can and does — the Cyber Bureau applies sound principles daily. The real issue is capacity (people, labs, law, foreign-data access) that must scale with the rising caseload, not a lack of valid methodology.",
    "Nepal's cyber forensics centres on the Nepal Police Cyber Bureau, handling a rising caseload (online fraud, social-media abuse, financial scams) against constraints: limited trained personnel, tool/lab capacity, backlog, dependence on foreign platforms for data, and an evolving legal framework. The principles are sound — like a small fire brigade facing a growing city, capacity must scale with the digital population.",
    "Cyber Bureau · rising caseload · limited personnel/labs · backlog · foreign-platform dependence · capacity must scale")

add_activity("S44 — 'Screenshots to court-ready'  ·  ~5 min",
    ["In pairs (2 min): a complainant brings only WhatsApp screenshots to the Cyber Bureau.",
     "List the steps needed to turn them into court-ready, admissible evidence under the ETA 2063.",
     "Take 3–4 answers aloud (3 min); check each step against the admissibility checklist.",
     "Close: debate briefly — should Nepal create a dedicated cybercrime/data-evidence law beyond the ETA?"],
    "Steps: forensic extraction of the original messages + metadata, hashing, a chain-of-custody record, lawful authorisation/warrant, and expert testimony. Screenshots alone fail authenticity/integrity; the extraction and custody supply them.",
    "ACTIVITY [~5 min].")
add_quiz("S44 — Quick Check  ·  ~5 min",
    [("Q1.  Genuine evidence can still be rejected by a court if:","q"),
     ("a) it's too detailed   b) ✅ it was illegally obtained or improperly handled (broken chain of custody)   c) it's digital   d) it's on a phone","a"),
     ("     Why: admissibility needs lawful process + integrity — truth alone is never enough.","o"),
     ("Q2.  In Nepal, electronic records are primarily recognised as evidence under the:","q"),
     ("a) Muluki Ain   b) ✅ Electronic Transaction Act (ETA), 2063   c) Companies Act   d) no law","a"),
     ("     Why: the ETA 2063 (2008) recognises electronic records and defines cyber offences.","o"),
     ("Discussion: should Nepal create a dedicated cybercrime and digital-evidence law beyond the ETA? Argue both sides.","o")],
    "QUIZ [~5 min]. Land that admissibility needs legality + authenticity + integrity, and that the ETA 2063 is Nepal's main (but ageing) legal basis.")
add_summary("S44 · Summary  ·  [~2 min]",
    ["Admissibility needs legality + authenticity + integrity, not just truth — mishandled evidence is excluded.",
     "Nepal relies mainly on the ETA 2063 (2008) and the Nepal Police Cyber Bureau for electronic evidence.",
     "The principles are sound, but capacity (people, labs, law) must grow with the rising cybercrime caseload."],
    "As a BIM graduate you may one day file or face a cyber complaint — knowing what makes evidence admissible, and the Cyber Bureau's role, is directly practical for protecting yourself and others.",
    "Next unit (Unit 9) — Cyber Law in Nepal: the ETA, Electronic Transaction Rules, and IT/security policy in depth.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 8 · Cheat Sheet","One-page revision reference",
    [("Intro & principles (S38)","Digital forensics = science + law → legally admissible evidence. Grew from computer (1 PC) to digital (phones/cloud/IoT). Principles: don't alter original · work on copies · document · custody · repeatability."),
     ("The six stages (S39)","Identify → Preserve → Collect → Examine → Analyse → Report (NIST SP 800-86). Preservation protects everything downstream. Report for a non-technical judge. Integrity runs through all stages."),
     ("Evidence · lab (S40)","Good evidence = admissible, authentic, complete, reliable, believable (NOT 'encrypted'). Screenshot = weak. Tools by category (Autopsy/EnCase/FTK/Cellebrite) — method over brand. Lab: access control, air-gap, ISO 17025."),
     ("Collect & protect (S41)","Chain of custody = who/when/why/how, sealed & logged; a gap = challengeable. Order of volatility: RAM first, disk later. Write blocker = read-only; hashing (SHA-256) proves the copy is identical."),
     ("Recover data (S42)","Delete removes the pointer, not the data — recoverable until overwritten. Image bit-for-bit (incl. slack/unallocated), hash, analyse the copy. File carving rebuilds files by header/footer signatures."),
     ("Mobile & law (S43–S44)","Phone = the crime scene. Extraction: manual→logical→file-system→physical (SQLite + cloud). Isolate (Faraday), hash, custody. Admissibility = legal + authentic + intact. Nepal: ETA 2063 + Cyber Bureau.")])

add_glossary("Unit 8 · Glossary","Key terms — quick reference",
    [("Digital forensics","scientific identify/preserve/analyse/present of digital evidence, legally admissible."),
     ("Computer → digital forensics","the shift from a single PC to phones, cloud, networks and IoT."),
     ("Core principles","don't alter the original · work on copies · document · custody · repeatability."),
     ("Forensic process","identify → preserve → collect → examine → analyse → report."),
     ("NIST SP 800-86","standard model: collection, examination, analysis, reporting."),
     ("Digital evidence","data (stored/transmitted) that supports or refutes a fact in a case."),
     ("Properties of good evidence","admissible, authentic, complete, reliable, believable."),
     ("Metadata","hidden data about a file (author, timestamps, GPS)."),
     ("CDR","Call Detail Record from a telco (NTC/Ncell)."),
     ("Forensic lab","controlled, secure, (ideally) accredited environment for analysis (ISO/IEC 17025)."),
     ("Chain of custody","documented, unbroken record of who handled evidence, when, why and how."),
     ("Order of volatility","collect the most fragile data (RAM) before the durable (disk, backups)."),
     ("Faraday bag","signal-blocking bag that stops remote wipe/sync."),
     ("Write blocker","hardware/software that reads a drive but blocks any write."),
     ("Hashing (MD5/SHA-256)","a digital fingerprint proving data is unchanged."),
     ("Disk image","a bit-for-bit copy of a drive, incl. slack & unallocated space."),
     ("Slack / unallocated space","areas where 'deleted' data survives until overwritten."),
     ("File carving","rebuilding files from raw data via header/footer signatures, no index."),
     ("Mobile forensics","extracting/analysing evidence from phones, tablets, SIMs and apps."),
     ("Extraction levels","manual → logical → file-system → physical (more data = harder)."),
     ("Admissibility","conditions for a court to accept evidence: relevant, authentic, intact, lawful."),
     ("ETA 2063 (2008)","Nepal's Electronic Transaction Act — recognises e-records; defines cyber offences."),
     ("Cyber Bureau","Nepal Police central cybercrime body (est. 2018, Bhotahity)."),
     ("Live acquisition","capturing volatile data (RAM/keys) while a device is running/unlocked.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 8 · Revision","Consolidated end-of-unit quiz",
    "Ten MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit8_material.md.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  The defining goal of digital forensics is   →  ✅ producing legally admissible evidence","a"),
     ("2.  Computer→digital forensics grew because   →  ✅ evidence now lives on phones, cloud & networks","a"),
     ("3.  The correct order of the process is   →  ✅ identify→preserve→collect→examine→analyse→report","a"),
     ("4.  A property NOT required of good evidence is   →  ✅ that it be encrypted","a"),
     ("5.  The purpose of a write blocker is   →  ✅ read a drive while preventing any change to it","a"),
     ("6.  Matching hashes of original & copy prove   →  ✅ the copy is an exact, unaltered duplicate","a"),
     ("7.  When a file is 'deleted', usually   →  ✅ the pointer is removed but data remains until overwritten","a"),
     ("8.  File carving recovers files by   →  ✅ recognising file signatures in raw data, without the index","a"),
     ("9.  The extraction type yielding the most data is   →  ✅ physical (full image)","a"),
     ("10.  In Nepal, e-records are recognised as evidence under the   →  ✅ Electronic Transaction Act (ETA) 2063","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("11. Define chain of custody and why it matters.   12. List & explain the six forensic stages.   13. Why is a bare screenshot weak evidence?","o"),
     ("14. Explain how hashing proves integrity.   15. Name Nepal's central cyber-forensics body and two challenges it faces.","o"),
     ("Section C — Applied case","q"),
     ("16. Given a Nepal phone-seizure scenario, list the correct steps to preserve integrity and chain of custody.","o"),
     ("17. Explain why a piece of genuine but mishandled evidence would be ruled inadmissible.","o"),
     ("Section D — Discussion","q"),
     ("18. Should Nepal invest in a dedicated digital-forensics law and lab capacity beyond the current ETA and Cyber Bureau? Argue both sides.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit8_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 8  ·  IT 246",
          "S38–S44 complete: intro & principles · the six stages · digital evidence & the lab · collecting/seizing/protecting · recovering data · mobile forensics · legal aspects & Nepal",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe · chain of custody & integrity emphasised · Next: Unit 9 — Cyber Law in Nepal (ETA 2063).")

_add_page_numbers()
save("IT246_Unit8.pptx")
