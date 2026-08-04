#!/usr/bin/env python3
"""IT246 (sixth) Unit 5 deck — Fundamentals of Cybersecurity (S22–S27), built to
COURSE_MATERIAL_STANDARD.md INCLUDING the §7A depth rule: every confusable set is a
comparison table, every 'X vs not-X' concept a concrete-example table, claims get
scaffolding tables — each table on its OWN slide, paginated, never squeezed.
DEFENSIVE / educational framing throughout — every attack is described only to RECOGNIZE
and DEFEND against it; there are NO exploit or attack-execution recipes anywhere in this deck.
Self-contained & PDF-safe. Imports deckkit.py. Diagrams in images/.
Run: python3 build_unit5_pptx.py -> IT246_Unit5.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 5 — Fundamentals of Cybersecurity",
          "IT 246: IT Ethics & Cybersecurity  ·  BIM 6th Semester  ·  Sessions S22–S27",
          "DEFENSIVE / awareness unit — every attack is described only to recognise and defend against it (no attack recipes). "
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES (Nepal / IT localised). Exports to PDF with no information lost.")

add_outcomes("Unit 5 — Learning Outcomes","fundamentals of cybersecurity  ·  s22–s27",
    "By the end of this unit, you will be able to:",
    ["Define cyberspace and cybersecurity, and explain the CIA triad as the core objective (S22)",
     "Explain how technology, economic-model shifts, and outsourcing reshape the threat landscape (S23)",
     "Express risk as threat × vulnerability × impact and use it to prioritise defences (S24)",
     "Recognise common attacks — malware, phishing, DoS, poisoned web services — and their defences (S25)",
     "Explain ARP/DNS poisoning and man-in-the-middle conceptually, and name the countermeasures (S26)",
     "Classify cyberattackers by motive and 'hat' (white/grey/black, script kiddies, hacktivists, state, insiders) (S27)"],
    "This is Unit 5 of IT 246 — the shift from ETHICS (Units 1–4) to DEFENCE. It gives you the vocabulary (CIA, risk, threat vs vulnerability) and the attack/defence pairs you will use for the rest of the course. Everything here is framed to defend, never to attack.")

add_roadmap("Unit 5 — Roadmap","Where each session fits (S22–S27)",
    ["S22  Cyberspace, cybersecurity & the CIA triad",
     "S23  Threat-landscape drivers (tech · economics · outsourcing)",
     "S24  Risk = threat × vulnerability × impact",
     "S25  Common attacks + poisoned web services (defence)",
     "S26  Network poisoning: ARP · DNS · MITM (defence)",
     "S27  Cyberattackers & their coloured hats — closes unit"],
    ["Units 6–8   Personal security, cryptography & digital forensics",
     "Unit 9   Cyber law in Nepal (ETA 2063, Privacy Act)"])

# ============================================================ S22
add_divider("Session 22 · Lecture hour 1 (of 6)","Introduction to Cyberspace & Cybersecurity · the CIA Triad",
    "Your eSewa balance, your exam results on a college portal, the NEA billing system, the army's email — all live in the same 'place' that doesn't physically exist. Who is responsible for keeping it safe, and safe from what exactly?",
    "OPENING HOOK [~5 min]. Draw out that 'the internet' is only part of it, and that 'secure' needs a precise meaning. Agenda: cyberspace → cybersecurity (people+process+tech) → the CIA triad.")

concept_understand("S22 · Concept 1 · [THEORY]","What Is Cyberspace",
    "Cyberspace is the interconnected digital environment of networks, systems, data, and the people and devices using them. It is not just 'the internet' — it includes private and bank networks, the cloud, OT/ICS (industrial control), and mobile. Think of it as a domain, like land, sea, air, and space.",
    ["It spans public internet AND private networks, cloud, and offline-connected devices.",
     "OT/ICS — the software running a power grid or water plant — is part of cyberspace too.",
     "Militaries treat it as the 'fifth domain' of conflict (after land, sea, air, space).",
     "Nepal's cyberspace is growing fast: National ID, eSewa/Khalti, Nagarik App, e-governance portals."],
    "s22_domains.png","Cyberspace = the whole connected digital domain, not just the websites you visit.",
    "~7 min. Kill the 'cyberspace = my browser tabs' reflex early. Point at NEA billing / OT and the Nagarik App as parts of the same domain that need protecting.")
add_table_slide("S22 · Concept 1 · concrete examples","Is this part of cyberspace? — beyond 'the websites I visit'",
    ["Real thing (Nepal / IT)","Part of cyberspace?","Why (verdict)"],
    [["The websites you browse","Yes","The visible surface — but only a slice of the whole"],
     ["A bank's back-end customer database","Yes","Private systems are cyberspace even if you never see them"],
     ["NEA grid / billing control software (OT/ICS)","Yes","Operational technology is a critical, often-forgotten part"],
     ["The Nagarik App on your phone","Yes","Mobile apps + their cloud back-ends are all in the domain"],
     ["A smart CCTV / IoT sensor in an office","Yes","Connected devices are entry points into cyberspace"],
     ["A paper land-record ledger in a cupboard","No","Not digital / not connected — outside cyberspace (until digitised)"]],
    per_page=6,widths=[2.6,1.7,3.0],fs=11,
    note="'Cyberspace = the websites I visit' is the misconception. It includes back-end systems, infrastructure (OT/ICS), cloud, and offline-connected devices — a whole domain like land/sea/air.")
concept_apply("S22 · Concept 1 · [THEORY]","What Is Cyberspace",
    "Nepal's cyberspace has exploded in a decade: the National ID system, eSewa/Khalti wallets, the Nagarik App, online banking, and e-governance portals all live in it — alongside the NEA billing/grid software you never see. NATO and militaries even treat cyberspace as the 'fifth domain' of conflict after land, sea, air, and space.",
    "\"Cyberspace = the websites I visit.\" It is far larger: back-end databases, cloud, industrial control systems (OT/ICS), and offline-connected devices are all part of it. Protecting cyberspace means protecting the plumbing you never see, not just the pages on your screen.",
    "Cyberspace is the interconnected digital environment of networks, systems, data, and the people and devices using them — a domain like land, sea, air, and space. It spans the public internet, private and bank networks, the cloud, OT/ICS, and mobile, so it includes back-end systems and infrastructure, not merely the websites a user visits.",
    "cyberspace · fifth domain · networks + systems + data + people · OT/ICS · more than the internet")

concept_understand("S22 · Concept 2 · [THEORY]","What Is Cybersecurity",
    "Cybersecurity is the practice of protecting systems, networks, and data from unauthorised access, harm, or disruption. It is a defensive discipline built on three pillars — people, process, and technology — not just antivirus software. The weakest of the three decides how secure you really are.",
    ["People: trained staff who don't click the phishing link or share the OTP.",
     "Process: policies, patching schedules, incident response, backups, access rules.",
     "Technology: firewalls, antivirus/EDR, encryption, MFA — tools, not the whole answer.",
     "In Nepal, NPCERT (the national CERT) coordinates response; banks run security teams under NRB cyber-resilience guidance."],
    None,"Cybersecurity = people + process + technology; the weakest pillar sets your real security.",
    "~7 min. The mini case: a college server reachable from the internet with a default admin password — is the threat the password, the exposure, or both? (Both — a process failure and an exposure.)")
add_table_slide("S22 · Concept 2 · scaffolding","People + process + technology — and what fails without each",
    ["Pillar","What it is","If this pillar is weak (Nepal / IT)"],
    [["People","Trained, aware staff and users","A clerk shares an OTP → account drained despite good tech"],
     ["Process","Policies, patching, backups, response","No patch schedule → a known flaw stays open for months"],
     ["Technology","Firewalls, antivirus/EDR, MFA, encryption","No MFA → one stolen password = full access"],
     ["People + process","Trained staff following a set drill","No incident plan → a breach turns into a public disaster"],
     ["Process + tech","Backups that are actually tested","Untested backup fails on restore → ransomware wins"],
     ["All three","A defensive discipline, not a product","'We bought antivirus, so we're secure' → false confidence"]],
    per_page=6,widths=[1.7,2.6,3.0],fs=11,
    note="Security is only as strong as the weakest pillar. Antivirus alone (technology) cannot save you from an untrained clerk (people) or a missing patch policy (process).")
concept_apply("S22 · Concept 2 · [THEORY]","What Is Cybersecurity",
    "In Nepal, NPCERT coordinates incident response, and banks run security teams under NRB cyber-resilience guidance. Worked mini-case: a college server sits on the internet with a default admin password. The threat (someone scanning for it) and the vulnerability (the default password + the exposure) are BOTH real — security means fixing the process and the exposure, not blaming one thing.",
    "\"Cybersecurity just means installing antivirus.\" Antivirus is one piece of the technology pillar. Real security is people + process + technology together — a trained user, a patching policy, and a firewall — and it is a continuous discipline, not a product you buy once.",
    "Cybersecurity is the practice of protecting systems, networks, and data from unauthorised access, harm, or disruption. It rests on three pillars — people (awareness/training), process (policies, patching, backups, response), and technology (firewalls, antivirus/EDR, MFA, encryption) — and is a defensive discipline, not just antivirus. Its strength is set by the weakest pillar.",
    "cybersecurity · people + process + technology · defensive discipline · NPCERT · weakest-pillar rule")

concept_understand("S22 · Concept 3 · [THEORY]","The CIA Triad — Confidentiality, Integrity, Availability",
    "The CIA triad is the three goals every security control serves: Confidentiality (secrecy / access control), Integrity (data stays unchanged and trustworthy), and Availability (the system is usable when needed). Every attack breaks at least one leg; there are real trade-offs between them.",
    ["Confidentiality = only authorised people can read the data (encryption, access control).",
     "Integrity = data has not been secretly altered (hashing, checksums, audit logs).",
     "Availability = the service is up when users need it (backups, redundancy, capacity).",
     "Trade-off: locking a system down hard (C) can hurt Availability — security is a balance."],
    "s22_ciatriad.png","CIA is a three-legged stool — saw off any leg and it falls over.",
    "~9 min. Map each Nepal incident to a leg: DDoS on e-banking = A; leaked database = C; altered exam result / land record = I. Keep returning to the stool analogy.")
add_comparison_table("S22 · Concept 3 · comparison","Confidentiality vs Integrity vs Availability",
    ["Dimension","Confidentiality (C)","Integrity (I)","Availability (A)"],
    [["Goal","Keep data secret","Keep data correct & trusted","Keep the service usable"],
     ["Broken when…","Data is leaked/read","Data is secretly altered","Service is knocked offline"],
     ["Typical control","Encryption, access control","Hashing, audit logs, checks","Backups, redundancy, capacity"],
     ["Nepal example (broken)","eSewa/KYC database leaks","Land-record data is altered","e-banking down in a DDoS"],
     ["Attack that hits it","Data theft / spyware","Tampering / defacement","DoS / ransomware lockout"]],
    per_page=5,widths=[1.7,2.1,2.1,2.1],fs=10.5,
    note="Every control ultimately serves one or more of C, I, A. A system that never leaks (C) but is always down (A) or tamper-prone (I) is still insecure — you need all three.")
concept_apply("S22 · Concept 3 · [THEORY]","The CIA Triad",
    "Map real Nepal incidents to the triad: a DDoS knocking a Nepali bank's e-banking offline breaks Availability; a leaked KYC/customer database breaks Confidentiality; a tampered exam result on a college portal or altered land-records data breaks Integrity. Ransomware is nasty because it can break Availability (files locked) and Confidentiality (data stolen) at once.",
    "\"Security just means keeping secrets (Confidentiality).\" An always-down or easily-tampered system is insecure even if nothing ever leaks. Integrity and Availability matter just as much — a bank whose data is trustworthy and secret but offline every festival has still failed its customers.",
    "The CIA triad — Confidentiality, Integrity, Availability — is the set of three goals every security control serves. C keeps data secret (encryption, access control), I keeps it unchanged and trustworthy (hashing, audit logs), A keeps the system usable (backups, redundancy). Every attack breaks at least one leg, and they trade off, so security means balancing all three — like a three-legged stool.",
    "CIA triad · confidentiality · integrity · availability · three-legged stool · every control serves C/I/A")
add_examples_table("S22 · Concept 3 · concrete examples","Which CIA goal does each incident violate?",
    ["Incident (Nepal / global)","CIA goal violated","Why (verdict)"],
    [["Ransomware locks a hospital's files","Availability","Legitimate users can't reach data when needed"],
     ["A leaked eSewa/KYC customer database","Confidentiality","Secret data is now readable by outsiders"],
     ["An exam result changed on a college portal","Integrity","Data is no longer trustworthy / unaltered"],
     ["DDoS takes a bank's e-banking offline","Availability","Service is unusable during the attack"],
     ["Land-record values quietly altered","Integrity","Records look official but are wrong"],
     ["Spyware silently copies your messages","Confidentiality","Private data is read without permission"],
     ["Ransomware that also steals data first","Confidentiality + Availability","Two legs broken at once — data stolen AND locked"]],
    per_page=7,widths=[2.9,2.0,2.6],fs=11,
    note="Naming the violated leg is the vocabulary every security job, audit, and NRB bank inspection uses. Some attacks (ransomware with exfiltration) break more than one leg.")

add_activity("S22 — 'Rank C, I, A for your result portal'  ·  ~5 min",
    ["In pairs (2 min): for your college result portal, rank Confidentiality, Integrity, and Availability by importance.",
     "Justify the ranking: what is the worst thing that could happen to each?",
     "Take 3–4 answers aloud (3 min); notice teams disagree — that is the point.",
     "Close: for a result portal, Integrity usually tops the list (a changed grade is catastrophic); for e-banking, all three are critical."],
    "Draw out that the ranking depends on the system: a result portal fears tampering (I) most; a hospital fears downtime (A); a KYC store fears leaks (C). There is no single 'right' order — it depends on the asset.",
    "ACTIVITY [~5 min].")
add_quiz("S22 — Quick Check  ·  ~5 min",
    [("Q1.  A ransomware attack that locks files mainly violates:","q"),
     ("a) Confidentiality   b) Integrity   c) ✅ Availability   d) none","a"),
     ("     Why: locked files mean legitimate users can't reach the data when they need it — that is Availability.","o"),
     ("Q2.  Ensuring data has not been secretly altered is:","q"),
     ("a) Confidentiality   b) ✅ Integrity   c) Availability   d) authentication","a"),
     ("     Why: Integrity is about data staying unchanged and trustworthy — no silent tampering.","o"),
     ("Discussion: for your college result portal, rank C, I, and A by importance — and justify.","o")],
    "QUIZ [~5 min]. Draw out that 'secure' means all three legs, not just secrecy — and that the ranking depends on the system.")
add_summary("S22 · Summary  ·  [~2 min]",
    ["Cyberspace = the whole connected digital domain (networks, systems, data, people) — not just the websites you visit.",
     "Cybersecurity = people + process + technology; a defensive discipline, not just antivirus (weakest pillar wins).",
     "The CIA triad — Confidentiality, Integrity, Availability — is the goal every control serves; every attack breaks a leg."],
    "CIA is the vocabulary you'll use for the rest of this course and in every real security job: every audit, penetration test, and NRB bank inspection is ultimately checking C, I, and A. Learn to name the leg an incident breaks and you can reason about any attack.",
    "S23 — the forces (technology, economics, outsourcing) that keep reshaping this landscape.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S23
add_divider("Session 23 · Lecture hour 2 (of 6)","Key Development Areas: Technology · Economics · Outsourcing",
    "Ten years ago a Nepali shop kept cash in a drawer. Today it takes QR payments, stores customer numbers in the cloud, and runs on a phone. Did the shop get a security team too? Why does the attack surface keep exploding?",
    "OPENING HOOK [~5 min]. Draw out that each convenience added an entry point but rarely a defender. Agenda: technology growth → economic-model shifts → outsourcing & supply chain.")

concept_understand("S23 · Concept 1 · [THEORY]","Technological Changes Expand the Attack Surface",
    "The attack surface is the sum of all the points where an attacker could try to get in. Each new technology — cloud, mobile, IoT, AI, remote work — adds new devices, data, and entry points, so it grows the attack surface. New features usually arrive before their security does.",
    ["More devices/data/entry points = a bigger attack surface to defend.",
     "Cloud moves data off-site; mobile puts sensitive apps on easily-lost phones; IoT adds cheap, weak devices.",
     "Remote work extends the network into homes and cafés you don't control.",
     "The lag: a shiny new feature ships, its security hardening comes (if at all) later."],
    "s23_attacksurface.png","Every new technology adds entry points — the attack surface only grows.",
    "~8 min. Contrast 2010 (a till + one PC) with 2026 (QR pay, cloud DB, app, CCTV, staff phones). Each convenience is also a door.")
add_examples_table("S23 · Concept 1 · concrete examples","New technology → the new attack surface it adds (Nepal)",
    ["New technology adopted","New entry point it adds","Defence to add with it"],
    [["QR payments (fonepay) at a shop","Fake QR / payment-redirect risk","Verify payee name; staff training; reconcile daily"],
     ["Customer data moved to the cloud","Data now reachable over the internet","Access control, encryption, MFA on the console"],
     ["Smart CCTV / IoT in the office","Cheap devices with weak defaults","Change defaults, segregate on their own network, patch"],
     ["Staff use personal phones for work","Lost/compromised phone = data leak","Screen lock, remote wipe, keep work data separate"],
     ["Remote / work-from-home setup","Home Wi-Fi and PCs you don't control","VPN, endpoint protection, secure config policy"],
     ["An AI chatbot handling queries","New data flows + prompt-abuse risk","Limit data it sees; monitor; validate its outputs"]],
    per_page=6,widths=[2.5,2.6,3.0],fs=11,
    note="Each row PAIRS the new tech with the defence it demands. New features arrive before their security — so the habit is: adopt a technology, add its defence in the same breath.")
concept_apply("S23 · Concept 1 · [THEORY]","Technological Changes Expand the Attack Surface",
    "Nepal's decade of QR payments (fonepay), the Nagarik App, smart CCTV, and cheap IoT in homes and offices has multiplied entry points. Globally, billions of IoT devices shipped with weak default passwords became botnet fuel (e.g. the Mirai botnet). Each convenience added a door — and doors need locks that were often bolted on afterwards, if at all.",
    "\"New technology is automatically more secure.\" Usually the opposite: new features arrive first and their security hardening comes later (or never for cheap IoT). Adopting a technology without adding its defence quietly grows your attack surface — convenience is not the same as safety.",
    "Technological change expands the attack surface — the sum of all points an attacker could target. Cloud, mobile, IoT, AI, and remote work each add devices, data, and entry points, and their security typically lags the feature. So every adopted technology must be paired with a defence; more capability without more protection simply means more ways in.",
    "attack surface · cloud/mobile/IoT/AI/remote · features before security · IoT botnets · adopt tech + its defence")

concept_understand("S23 · Concept 2 · [THEORY]","Economic Model Shifts — Cybercrime as a Business",
    "Cybercrime and IT itself have become businesses, and that changes who attacks and why. SaaS/cloud shifts where data lives; 'Cybercrime-as-a-Service' and Ransomware-as-a-Service (RaaS) let low-skill criminals RENT ready-made attack tools; and data itself becomes a traded commodity, bought and sold in bulk.",
    ["Cloud/SaaS moves data to third-party platforms you don't own — new dependency, new target.",
     "RaaS / phishing kits are rented like software subscriptions, lowering the skill needed to attack.",
     "Stolen data (cards, credentials, KYC) is a commodity, sold in bulk on criminal markets.",
     "Some ransomware gangs even run 'customer support' to help victims pay — crime as an industry."],
    None,"Crime went pro: a low-skill attacker in 2026 can RENT tools an expert once needed.",
    "~8 min. The mini case: why does a low-skill criminal in 2026 pose more risk than one in 2010? Answer — rented, ready-made tools. Localise: pre-packaged phishing kits aimed at Nepali users.")
add_comparison_table("S23 · Concept 2 · comparison","The attacker economy — 2010 vs 2026",
    ["Dimension","~2010 attacker","2026 attacker"],
    [["Skill needed","High — had to build tools","Low — rents ready-made kits (RaaS)"],
     ["Where data lives","On-premise servers","Cloud / SaaS platforms (new target)"],
     ["Business model","Lone hobbyist / vandal","Organised gangs with 'customer support'"],
     ["What's for sale","Little","Stolen cards, credentials, KYC in bulk"],
     ["Nepal impact","Rare, opportunistic","Pre-packaged phishing kits target local users"]],
    per_page=5,widths=[1.7,2.4,2.9],fs=10.5,
    note="The shift matters for defence: attacks are now cheap, scalable, and require little skill — so 'we're too small/unskilled a target for real hackers' is false. The tools are rented, not built.")
concept_apply("S23 · Concept 2 · [THEORY]","Economic Model Shifts",
    "In Nepal, stolen card / eSewa / bank credentials are sold in bulk on criminal markets, and pre-packaged phishing kits are aimed specifically at Nepali users (fake bank-KYC, fake wallet rewards). Globally, ransomware gangs operate like companies — complete with 'customer support' desks to walk victims through paying. Crime has become a scalable service industry.",
    "\"Only a genius hacker could attack us, and we're too small to bother with.\" Ransomware-as-a-Service and rented phishing kits mean a low-skill criminal can now run a powerful attack cheaply and at scale — small, local targets are attacked precisely because they are easy and numerous.",
    "Economic-model shifts have turned cybercrime and IT into businesses: SaaS/cloud changes where data lives; Cybercrime-/Ransomware-as-a-Service lets low-skill attackers rent powerful tools; and stolen data becomes a traded commodity sold in bulk. This lowers the skill and cost of attacking, so the volume and reach of attacks — including on small Nepali targets — rises sharply.",
    "economic shift · Cybercrime-/Ransomware-as-a-Service · data as commodity · rented tools · low skill, high reach")

concept_understand("S23 · Concept 3 · [THEORY]","Outsourcing & the Supply Chain",
    "Relying on third-party vendors and contractors introduces THEIR risk into YOUR system — this is supply-chain risk. Third-party access, shared credentials, and managed services extend your trust boundary outside your own walls, so a vendor's weakness can become your breach.",
    ["A vendor with access to your system is a door into it — their security is now your security.",
     "The chain is deep: you trust your vendor, and your vendor's sub-vendors too.",
     "A single compromised software update from a trusted vendor can hit all its customers at once.",
     "You outsource the WORK, but you keep the ACCOUNTABILITY for protecting your data."],
    "s23_supplychain.png","You outsource the work, not the accountability — a vendor breach is your breach.",
    "~7 min. Localise: Nepali banks/government outsourcing software development or hosting to outside vendors. If the vendor is breached, the bank's customers are the ones harmed.")
add_examples_table("S23 · Concept 3 · concrete examples","Outsourcing scenario → the risk it inherits (Nepal)",
    ["Outsourcing scenario","Risk inherited","Defence / control"],
    [["Bank outsources app development to a vendor","Vendor's insecure code ships into the bank","Security requirements in contract; code review; testing"],
     ["Government hosts a portal with a third party","Host's breach exposes citizen data","Data-protection clauses; audits; encryption"],
     ["Vendor gets remote access to maintain a system","A stolen vendor credential = access to you","Least privilege, MFA, time-limited access, logging"],
     ["Shared admin password given to a contractor","No accountability if it leaks","Unique named accounts; revoke on exit"],
     ["Managed service (SaaS) holds your data","Depend on their uptime & security","Review their certifications; a backup you control"],
     ["Vendor uses its own sub-vendor (deep chain)","Risk you can't even see","Require vendors to vet their sub-vendors"]],
    per_page=6,widths=[2.6,2.5,3.0],fs=11,
    note="The duty of care travels with the data (echoing Unit 4's outsourcing ethics). You outsource the work, not the accountability — a vendor's carelessness is your customers' breach.")
concept_apply("S23 · Concept 3 · [THEORY]","Outsourcing & the Supply Chain",
    "Nepali banks and government offices routinely outsource software development or hosting to outside vendors. If that vendor is breached — or ships insecure code, or has a stolen maintenance credential — the bank's customers are harmed and the bank's name is on the incident. Globally, supply-chain attacks (a poisoned update from a trusted vendor reaching thousands at once) show how deep the chain goes.",
    "\"If we outsource IT, we outsource the risk too.\" You outsource the WORK, not the accountability. Regulators, customers, and the public still hold YOU responsible for protecting the data — so vendor security must be contracted, audited, and monitored, not assumed.",
    "Outsourcing to third-party vendors introduces their risk into your system — supply-chain risk. Third-party access, shared credentials, and managed services extend the trust boundary beyond your walls, and the chain runs to your vendors' sub-vendors. A vendor breach becomes your breach; you outsource the work but keep accountability, so vendor security must be required and verified.",
    "supply-chain risk · third-party access · trust boundary extended · work outsourced, accountability kept · vet vendors")

add_activity("S23 — 'One new tech, one new risk'  ·  ~5 min",
    ["In pairs (2 min): name one new technology your family or workplace adopted recently.",
     "List the new risk that came with it, and one defence they could add.",
     "Take 3–4 answers aloud (3 min); sort them into technology / economics / outsourcing drivers.",
     "Close: notice almost nobody added a defender when they added the technology — that's the whole point."],
    "Seeds: QR payments (fake-QR risk), a smart TV/CCTV (weak default), online banking (phishing), a shop moving records to the cloud (access control). Reward pairs that name a concrete, matching defence.",
    "ACTIVITY [~5 min].")
add_quiz("S23 — Quick Check  ·  ~5 min",
    [("Q1.  The 'attack surface' grows mainly because:","q"),
     ("a) hackers get smarter   b) ✅ more devices, data, and entry points are added   c) laws change   d) prices fall","a"),
     ("     Why: every new device, data store, and connection is another point an attacker could target.","o"),
     ("Q2.  'Ransomware-as-a-Service' matters because it:","q"),
     ("a) is legal   b) protects victims   c) ✅ lets low-skill attackers rent powerful tools   d) needs no internet","a"),
     ("     Why: renting ready-made attack tools lowers the skill and cost of attacking, so attacks multiply.","o"),
     ("Discussion: name one new technology your family adopted recently — what new risk came with it?","o")],
    "QUIZ [~5 min]. Draw out that convenience adds doors, crime is now a cheap rented service, and outsourcing keeps the accountability with you.")
add_summary("S23 · Summary  ·  [~2 min]",
    ["New technology (cloud, mobile, IoT, AI, remote work) grows the attack surface — features arrive before their security.",
     "Cybercrime and IT became business models: RaaS/phishing kits let low-skill attackers rent power; data is a traded commodity.",
     "Outsourcing extends your trust boundary — a vendor's breach is your breach; you outsource the work, not the accountability."],
    "When you propose a new system at work — a cloud service, a vendor, an app — you'll be expected to ask 'what new risk does this add, and who now has access to our data?' This session is that habit: adopt a capability and its defence together.",
    "S24 — turning all this into measurable RISK, so you can decide what to fix first.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S24
add_divider("Session 24 · Lecture hour 3 (of 6)","Risks Cybersecurity Mitigates · Risk = Threat × Vulnerability × Impact",
    "Two laptops. One holds wedding photos with no internet; one holds a bank's customer database online. The same 'virus' lands on both — which one keeps you up at night, and can you now say WHY, precisely?",
    "OPENING HOOK [~5 min]. Draw out that the SAME threat carries very different risk depending on vulnerability and impact. Agenda: threat vs vulnerability vs asset → the risk formula → what security actually mitigates.")

concept_understand("S24 · Concept 1 · [THEORY]","Threats, Vulnerabilities & Assets",
    "Three words people confuse. A threat is something that COULD cause harm; a vulnerability is a weakness it can exploit; an asset is what you're protecting. The chain: a threat actor + a threat exploits a vulnerability to harm an asset. With no vulnerability, the threat has nothing to land on.",
    ["Threat = the potential danger (a worm, a phisher, a flood).",
     "Vulnerability = the weakness that lets it in (unpatched software, a weak password).",
     "Asset = what has value and is being protected (data, money, a service, reputation).",
     "Remove the vulnerability (e.g. patch) and the same threat can no longer cause harm."],
    "s24_tva.png","Threat = the flood; vulnerability = living in a basement; asset = your belongings.",
    "~8 min. Hammer the distinction with the flood analogy. A threat with no matching vulnerability ≈ harmless; patching is removing the vulnerability so the threat can't land.")
add_comparison_table("S24 · Concept 1 · comparison","Threat vs Vulnerability vs Asset",
    ["Term","What it is","Everyday analogy","Nepal / IT example"],
    [["Threat","Something that could cause harm","A flood","A worm; a phishing campaign"],
     ["Vulnerability","A weakness it can exploit","Living in a basement","An unpatched government web server"],
     ["Asset","What you're protecting","Your belongings","Citizen data; eSewa balances"],
     ["Threat actor","Who is behind the threat","The storm / a burglar","A criminal gang; an insider"],
     ["Exploit","Threat actually using the weakness","Water entering the basement","The worm compromising the server"]],
    per_page=5,widths=[1.5,2.3,2.1,2.6],fs=10.5,
    note="'Threat and vulnerability are the same thing' is the classic confusion. A flood (threat) only harms you if you live in a basement (vulnerability) — no weakness, no harm.")
concept_apply("S24 · Concept 1 · [THEORY]","Threats, Vulnerabilities & Assets",
    "A Nepali government site running outdated software (a vulnerability) is repeatedly defaced (a threat realised), harming citizens' trust (the asset). Globally, an unpatched server (vulnerability) plus a worm (threat) produced mass compromise (e.g. WannaCry). The lesson: the threat existed in both cases, but the harm only landed where a vulnerability let it.",
    "\"Threat and vulnerability are the same thing.\" They're different: a flood is a threat; living in a basement is the vulnerability; your belongings are the asset. You usually can't remove the threat (floods happen), but you CAN remove the vulnerability (patch, move upstairs) — that's what defence does.",
    "A threat is something that could cause harm; a vulnerability is a weakness it can exploit; an asset is what you protect. The chain is: a threat actor + threat exploits a vulnerability to harm an asset — and with no vulnerability, the threat cannot land. Because you rarely control the threat, defence concentrates on removing vulnerabilities and limiting impact to the asset.",
    "threat · vulnerability · asset · threat actor · exploit · no vulnerability ⇒ no harm · patch the weakness")

concept_understand("S24 · Concept 2 · [THEORY]","Risk = Threat × Vulnerability × Impact",
    "Risk is the likelihood × consequence of a threat exploiting a vulnerability — captured as risk = threat × vulnerability × impact. A high threat with no vulnerability is low risk; a tiny vulnerability with catastrophic impact is high risk. This is exactly how professionals prioritise where to spend limited defence budget.",
    ["Multiply, don't add: if any factor is near zero, the risk is low.",
     "High threat + zero vulnerability ≈ low risk (nothing to exploit).",
     "Small vulnerability + catastrophic impact ≈ high risk (worth fixing first).",
     "Rank risks by likelihood × impact and defend the top-right of the matrix first."],
    "s24_riskmatrix.png","Risk multiplies threat, vulnerability, and impact — one near-zero factor lowers it all.",
    "~9 min. Work the campus ranking case out loud. Then map to the matrix: high-impact financial systems get the most defence budget for a reason.")
add_examples_table("S24 · Concept 2 · concrete examples","Scoring risk — same threat, different risk (Nepal)",
    ["Scenario","Threat × Vulnerability × Impact","Risk level (verdict)"],
    [["Offline laptop of wedding photos, malware","High × Low (no net) × Low","Low — little to exploit, little lost"],
     ["Online bank customer DB, same malware","High × Medium × Critical","High — huge impact if it lands"],
     ["Defaced public webpage (no data lost)","High × Medium × Low","Medium — embarrassing, limited harm"],
     ["Leaked student grades on a portal","Medium × Medium × High","High — privacy + trust damage"],
     ["Wiped payroll database, no backup","Low × Medium × Critical","High — low odds, catastrophic loss"],
     ["Old test server, no real data","Medium × High × Low","Low — weak, but nothing valuable on it"]],
    per_page=6,widths=[2.6,2.6,2.9],fs=11,
    note="This is why financial systems get the most defence budget: not because they're attacked most, but because their IMPACT is critical. Rank by likelihood × impact and fix the top of the list first.")
concept_apply("S24 · Concept 2 · [THEORY]","Risk = Threat × Vulnerability × Impact",
    "Framing an incident like the NIC ASIA SWIFT fraud as high-impact (large funds moved) explains why banks and financial systems get the most defence budget — the impact factor is enormous even when likelihood is low. A worked campus example: rank (a) a defaced webpage, (b) leaked student grades, (c) a wiped payroll database — by impact, the wiped payroll and leaked grades outrank the defacement.",
    "\"The threat we hear about most is the one to fix first.\" Not necessarily — risk multiplies threat, vulnerability, AND impact. A loud but low-impact threat can rank below a quiet one with catastrophic impact. Fear ranks by headlines; professionals rank by likelihood × impact.",
    "Risk = threat × vulnerability × impact — the likelihood × consequence of a threat exploiting a vulnerability. Because the factors multiply, a high threat with no vulnerability is low risk, while a small vulnerability with catastrophic impact is high risk. Ranking risks this way (a risk matrix) lets professionals prioritise limited defence budget on the highest-impact exposures first.",
    "risk = T × V × I · likelihood × consequence · multiply not add · risk matrix · prioritise by impact")

concept_understand("S24 · Concept 3 · [THEORY]","What Cybersecurity Actually Mitigates",
    "The goal of cybersecurity is to reduce risk to an ACCEPTABLE level, not to reach zero. You attack the formula from three sides: reduce threat exposure, fix vulnerabilities (patching), and limit impact (backups, segmentation). Some risk always remains — this leftover is called residual risk.",
    ["Reduce threat exposure: don't expose services to the internet needlessly; filter, monitor.",
     "Reduce vulnerability: patch, strong passwords + MFA, secure configuration.",
     "Reduce impact: backups, network segmentation, encryption so a breach hurts less.",
     "Zero risk is impossible; you manage risk DOWN to a level the organisation accepts (residual risk)."],
    None,"You can't reach zero risk — you manage it down to acceptable, like a zebra crossing.",
    "~8 min. The analogy: you can't make crossing the road risk-free, but a zebra crossing + looking both ways makes the risk acceptable. Same for systems — reduce, don't fantasise about zero.")
add_examples_table("S24 · Concept 3 · payoff table","Each control → which risk factor it reduces",
    ["Control / practice","Reduces which factor?","Effect (verdict)"],
    [["Patching software promptly","Vulnerability","Removes the weakness the threat needs"],
     ["MFA on accounts","Vulnerability","A stolen password alone is no longer enough"],
     ["Tested backups","Impact","Ransomware/wipe hurts far less — you restore"],
     ["Network segmentation","Impact","A breach is contained to one segment"],
     ["Not exposing a service to the internet","Threat exposure","Fewer attackers can even reach it"],
     ["Staff phishing training","Vulnerability (human)","Fewer people click the lure in the first place"],
     ["Encryption of stored data","Impact","A stolen database is unreadable to the thief"]],
    per_page=7,widths=[2.7,2.2,2.6],fs=11,
    note="Defence works the formula from three sides: cut threat exposure, fix vulnerabilities, and limit impact. You can't zero any factor entirely — the leftover is residual risk you consciously accept.")
concept_apply("S24 · Concept 3 · [THEORY]","What Cybersecurity Actually Mitigates",
    "A Nepali bank can't make its e-banking risk-free, but it patches (cuts vulnerability), keeps offline backups (cuts impact), and doesn't expose admin panels to the internet (cuts threat exposure) — bringing risk down to a level it and NRB can accept. What's left after all controls is residual risk, acknowledged rather than pretended away.",
    "\"Good security means zero risk.\" Zero risk is impossible — you manage it down to an acceptable level. Chasing zero wastes budget and creates false confidence; the professional goal is proportionate, residual-risk-aware defence, like a zebra crossing makes road-crossing acceptable, not risk-free.",
    "Cybersecurity's goal is to reduce risk to an acceptable level, not zero. It works the risk formula from three sides — reducing threat exposure, fixing vulnerabilities (patching, MFA, secure config), and limiting impact (backups, segmentation, encryption). Some residual risk always remains and is consciously accepted; pretending zero risk is achievable is itself a security failure.",
    "reduce risk to acceptable · residual risk · cut exposure/vulnerability/impact · zero risk impossible · zebra-crossing")

add_activity("S24 — 'Threat, vulnerability, impact for your device'  ·  ~5 min",
    ["In pairs (2 min): pick one device you own (phone, laptop).",
     "Name one threat to it, one vulnerability it has, and the impact if it's compromised.",
     "Take 3–4 answers aloud (3 min); for each, suggest one control and which factor it reduces.",
     "Close: notice you can rarely remove the threat — but you can nearly always reduce the vulnerability or impact."],
    "Seeds: phone — threat: theft/phishing; vulnerability: no screen lock, reused password; impact: eSewa + photos lost. Control: lock + MFA (vulnerability), backup (impact). Reward correct factor labelling.",
    "ACTIVITY [~5 min].")
add_quiz("S24 — Quick Check  ·  ~5 min",
    [("Q1.  A weakness that an attack can exploit is a:","q"),
     ("a) threat   b) ✅ vulnerability   c) asset   d) risk","a"),
     ("     Why: a vulnerability is the weakness; the threat is the thing that could exploit it.","o"),
     ("Q2.  In risk = threat × vulnerability × impact, patching a flaw mainly reduces the:","q"),
     ("a) threat   b) impact   c) ✅ vulnerability factor   d) asset value","a"),
     ("     Why: patching removes the weakness, so the same threat has less to exploit.","o"),
     ("Discussion: pick one device you own — name one threat, one vulnerability, and the impact if compromised.","o")],
    "QUIZ [~5 min]. Draw out that risk multiplies three factors, and that defence usually targets vulnerability and impact (not the threat itself).")
add_summary("S24 · Summary  ·  [~2 min]",
    ["Threat ≠ vulnerability ≠ asset: a threat could harm; a vulnerability is the weakness it exploits; the asset is what you protect.",
     "Risk = threat × vulnerability × impact — factors multiply, so a near-zero factor means low risk; rank by likelihood × impact.",
     "Security reduces risk to ACCEPTABLE, never zero — cut exposure, fix vulnerabilities, limit impact; residual risk remains."],
    "Security budgets and even exam-grade priorities are set by risk, not fear — this formula is exactly how professionals decide what to fix first. Being able to say 'this is low likelihood but critical impact, so it's a high risk' is the language of every risk register and audit.",
    "S25 — the actual attacks that exploit these vulnerabilities, and how to recognise and defend against them.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S25
add_divider("Session 25 · Lecture hour 4 (of 6)","Common Cyberattacks & Poisoned Web Services (defensive view)",
    "An SMS says 'Your eSewa/IME is blocked — verify here' with a link. A pop-up says 'Your PC has 5 viruses, call this number.' Both want one thing from you. Can you name the trick AND the defence?",
    "OPENING HOOK [~5 min]. Frame the whole session as RECOGNISE-and-DEFEND — no attack recipes. Agenda: malware → phishing → DoS → poisoned web services. Every attack is paired with its defence.")

concept_understand("S25 · Concept 1 · [THEORY]","Malware — Recognition & Defence",
    "Malware is malicious software — viruses, worms, trojans, ransomware, spyware. Each behaves differently (spreads, hides, locks, or spies), but the defences overlap: keep software updated, run antivirus/EDR, use least privilege, and keep tested backups. We study behaviour and warning signs to defend, not to build it.",
    ["Virus attaches to files; worm spreads by itself; trojan hides in something you trust.",
     "Ransomware locks/encrypts your files for money; spyware silently watches and steals.",
     "Warning signs: sudden slowness, pop-ups, files renamed/locked, unknown processes.",
     "Defences: updates + antivirus/EDR + least privilege + backups + careful clicks."],
    None,"Different malware, overlapping defence: update, protect, least-privilege, back up.",
    "~8 min. Localise: pirated software is a common infection route in Nepal, and ransomware has hit Nepali businesses and government offices. Keep it about recognition + defence.")
add_comparison_table("S25 · Concept 1 · comparison","Malware types — behaviour, warning sign & defence",
    ["Type","How it behaves","Warning sign","Key defence"],
    [["Virus","Attaches to a file; runs when opened","Files corrupted; odd errors","Antivirus; don't open unknown files"],
     ["Worm","Self-spreads across the network","Network slow; devices infected fast","Patch promptly; segment the network"],
     ["Trojan","Hides inside trusted-looking software","Unexpected behaviour after install","Install only from trusted sources"],
     ["Ransomware","Encrypts files, demands payment","Files locked; ransom note","Tested offline backups; patch; least privilege"],
     ["Spyware","Silently watches, steals data","Battery/data drain; strange activity","Anti-malware; app-permission hygiene"],
     ["Adware / PUP","Floods pop-ups, bundles junk","Constant ads; new toolbars","Careful installs; avoid pirated software"]],
    per_page=6,widths=[1.4,2.4,2.1,2.6],fs=10.5,
    note="Studied for RECOGNITION and DEFENCE only. Notice the defences overlap: updates, antivirus/EDR, least privilege, backups, and careful clicks beat most of them.")
concept_apply("S25 · Concept 1 · [THEORY]","Malware — Recognition & Defence",
    "Globally, WannaCry ransomware spread worldwide through a single unpatched Windows flaw — a worm + ransomware combined. In Nepal, ransomware and malware have hit businesses and government offices, and pirated/cracked software is a common infection route (the 'free' download carries a trojan). The fix is unglamorous: patch, run EDR, least privilege, and keep tested backups.",
    "\"Antivirus alone keeps me safe.\" Antivirus is one layer. Updates (WannaCry was a missing patch), tested backups (your ransomware recovery), least privilege, and careful clicks matter just as much — and pirated software often IS the malware. Defence is layered, not a single product.",
    "Malware is malicious software — viruses (attach to files), worms (self-spread), trojans (hide in trusted software), ransomware (encrypt for money), and spyware (silently steal). Recognising each behaviour and its warning signs supports defence, which is layered and overlapping: prompt updates, antivirus/EDR, least privilege, tested backups, and cautious clicking beat most malware.",
    "malware · virus/worm/trojan/ransomware/spyware · WannaCry (unpatched) · layered defence · patch + backup + EDR")

concept_understand("S25 · Concept 2 · [THEORY]","Phishing & Social-Lure Attacks — Recognition & Defence",
    "Phishing tricks a PERSON into giving credentials, money, or clicks via fake messages. It targets people, not machines, so no firewall fully stops it. The signs: manufactured urgency, mismatched or look-alike links, requests for OTP/PIN. The defences: verify out-of-band, never share an OTP, use MFA, and report.",
    ["Red flags: urgency ('act now / account blocked'), mismatched links, look-alike domains, OTP/PIN requests.",
     "Spear-phishing is targeted and researched — it can fool experts, not just careless people.",
     "Defences: pause and verify through a known channel; never share OTP/PIN; enable MFA.",
     "Report suspected phishing (to the bank, IT team, or NPCERT) so others are warned."],
    None,"Phishing hacks the human, not the computer — urgency is the tell; verify out-of-band.",
    "~9 min. Work the 'principal asks for gift cards' mini case: list 3 red flags. Localise: fake eSewa/Khalti reward, fake bank-KYC SMS, fake Nepal Police/IRD fine, look-alike bank URLs.")
add_examples_table("S25 · Concept 2 · concrete examples","Nepali phishing lures — the red flag & the defence",
    ["Lure (Nepal)","Red flag to spot","What you should do"],
    [["'Your eSewa/IME is blocked — verify here'","Urgency + a link asking to log in","Don't click; open the app yourself; report"],
     ["'You won a Khalti reward — claim now'","Too-good offer + urgency","Ignore; verify in the official app only"],
     ["Fake bank-KYC SMS asking for OTP/PIN","Any request for OTP/PIN","Never share OTP/PIN — banks never ask"],
     ["'Nepal Police/IRD fine — pay via this link'","Threat + unofficial payment link","Verify through official channels, not the link"],
     ["Look-alike bank URL (subtly misspelled)","Domain slightly wrong (e.g. rn for m)","Type the address yourself; check carefully"],
     ["Email 'from the principal' wanting gift cards","Urgent, unusual request, odd sender","Verify by phone/in person out-of-band"]],
    per_page=6,widths=[2.7,2.4,2.6],fs=11,
    note="Phishing targets the human, so the defence is behavioural: pause on urgency, verify out-of-band, never share OTP/PIN, enable MFA, and report. Well-crafted spear-phishing fools experts too.")
concept_apply("S25 · Concept 2 · [THEORY]","Phishing & Social-Lure Attacks",
    "Nepali users are hit with fake 'eSewa/Khalti reward' messages, fake bank-KYC SMS demanding an OTP, fake Nepal Police/IRD fine notices, and look-alike bank domains. Worked mini-case: an email 'from your principal' urgently asks you to buy gift cards — three red flags are the urgency, the unusual request, and the mismatched sender address. The defence is to verify through a known, separate channel before acting.",
    "\"Only careless people fall for phishing.\" Well-crafted, targeted spear-phishing (researched, personalised, well-timed) fools experts and executives too. The defence isn't 'be smart', it's a habit: pause on urgency, verify out-of-band, never share an OTP, and enable MFA so a stolen password alone fails.",
    "Phishing tricks a person into giving credentials, money, or clicks through fake messages, targeting people rather than machines. Its signs are manufactured urgency, mismatched or look-alike links, and requests for OTP/PIN; spear-phishing is targeted enough to fool experts. Defences are behavioural: verify out-of-band, never share OTP/PIN, use MFA, and report — because no firewall fully stops a human being tricked.",
    "phishing · social engineering · urgency + look-alike links + OTP requests · spear-phishing · verify out-of-band + MFA")

concept_understand("S25 · Concept 3 · [THEORY]","Denial-of-Service (DoS / DDoS) — Conceptual",
    "A Denial-of-Service attack overwhelms a service with traffic so legitimate users can't reach it — it attacks Availability. A DDoS is 'distributed': the flood comes from many machines (often a botnet) at once. We cover this conceptually; there are no traffic-generation instructions here.",
    ["Many requests flood a server until it can't serve real users — the target is uptime, not secrecy.",
     "DDoS uses many sources (a botnet) so it's hard to simply block one address.",
     "Defences (conceptual): rate-limiting, CDNs / traffic-scrubbing services, spare capacity.",
     "Coordinate with your ISP and NPCERT during a sustained attack — you can't fight it alone."],
    "s25_dos.png","DoS floods a service to break Availability — defended by capacity, filtering & coordination.",
    "~8 min. Localise: Nepali bank / government portals knocked offline during hacktivist campaigns. Strictly conceptual — the point is recognising the CIA goal hit (Availability) and the defences.")
add_examples_table("S25 · Concept 3 · concrete examples","Attack family → CIA goal it hits → defence",
    ["Attack family","CIA goal it mainly hits","Core defence (paired)"],
    [["Malware / ransomware","Availability (+ Confidentiality)","Patch, EDR, least privilege, tested backups"],
     ["Phishing","Confidentiality (stolen creds)","Verify out-of-band, MFA, training, report"],
     ["DoS / DDoS","Availability","Rate-limiting, CDN/scrubbing, capacity, ISP/NPCERT"],
     ["Poisoned / defaced website","Integrity (+ Availability)","Patching, input validation, WAF, monitoring"],
     ["Data theft / spyware","Confidentiality","Encryption, access control, anti-malware"],
     ["Tampering with records","Integrity","Hashing, audit logs, backups, access control"]],
    per_page=6,widths=[2.3,2.4,3.0],fs=11,
    note="This is the map for the whole unit: name the CIA goal an attack hits, then reach for the paired defence. Every attack here is studied to defend against it.")
concept_apply("S25 · Concept 3 · [THEORY]","Denial-of-Service (DoS / DDoS)",
    "Nepali bank and government portals have been knocked offline during hacktivist campaigns — a textbook attack on Availability, where nothing is stolen or altered but nobody can use the service. Because a DDoS comes from many sources at once, the defences are capacity and filtering (rate-limiting, a CDN or scrubbing service) plus coordinating with the ISP and NPCERT — no single organisation absorbs a large flood alone.",
    "\"A DoS attack steals my data.\" Usually it steals nothing — it attacks Availability by making the service unreachable. That's still serious (a bank offline during a festival is a real harm), but the defence is about capacity and filtering, not about protecting secrets.",
    "A Denial-of-Service attack overwhelms a service with traffic so legitimate users can't reach it, attacking Availability; a DDoS distributes the flood across many machines (a botnet) at once. Studied conceptually, its defences are rate-limiting, CDNs/traffic-scrubbing, spare capacity, and ISP/NPCERT coordination — because a large distributed flood cannot be blocked from one point.",
    "DoS / DDoS · attacks Availability · distributed botnet flood · rate-limiting/CDN/scrubbing/capacity · ISP + NPCERT")

concept_understand("S25 · Concept 4 · [THEORY]","Poisoned Web-Service & Web-Based Attacks — Recognition & Defence",
    "A poisoned web-service attack turns a trusted website or service into a delivery vehicle — drive-by downloads, malvertising, defacement, or injected malicious content. The unsettling point: a familiar, HTTPS site can be compromised. Defences split between users (updates, script/ad hygiene) and site owners (input validation, patching, a WAF).",
    ["The site you trust can be turned against you if it's compromised or serving bad ads.",
     "Signs: unexpected downloads/pop-ups, altered content (defacement), browser warnings.",
     "User defences: keep browser/OS updated, ad/script hygiene, don't ignore warnings.",
     "Site-owner defences (conceptual): input validation, patching, a Web Application Firewall (WAF)."],
    None,"A poisoned trusted site is a tampered sample in a shop you trusted — the padlock ≠ safe.",
    "~7 min. Localise: defacement of Nepali government websites; cloned/fake banking login pages on poisoned or look-alike sites. Bust 'HTTPS = safe': the padlock means encrypted, not trustworthy.")
add_examples_table("S25 · Concept 4 · concrete examples","Web-based attack sign → what it is → defence",
    ["Sign / situation (Nepal)","What it likely is","Defence (paired)"],
    [["Govt website shows an attacker's message","Defacement (Integrity hit)","Patching, input validation, WAF, monitoring"],
     ["A trusted site suddenly pushes a download","Drive-by / compromised site","Keep browser/OS updated; don't run it"],
     ["Ads on a normal site trigger scary pop-ups","Malvertising","Ad/script hygiene; ad-blocker; ignore the pop-up"],
     ["A cloned bank login on a look-alike URL","Fake login (credential theft)","Check the domain + certificate; type the address"],
     ["Padlock shown but the site feels wrong","HTTPS ≠ trustworthy","Padlock = encrypted only; verify identity too"],
     ["Form input causes odd server behaviour","Possible injection","Site owner: validate/sanitise input; patch"]],
    per_page=6,widths=[2.7,2.3,2.7],fs=11,
    note="The padlock means the connection is ENCRYPTED, not that the site is TRUSTWORTHY — a poisoned or cloned site can have HTTPS. Trusted sites can be compromised; keep software patched and heed warnings.")
concept_apply("S25 · Concept 4 · [THEORY]","Poisoned Web-Service & Web-Based Attacks",
    "Nepali government websites have been defaced (an Integrity attack — the page is altered), and cloned banking login pages are hosted on poisoned or look-alike sites to harvest credentials. Users defend by keeping browsers/OS patched, practising ad/script hygiene, and heeding warnings; site owners defend (conceptually) with input validation, patching, and a WAF.",
    "\"A familiar or HTTPS site is always safe.\" Trusted sites can be compromised, and the padlock only means the connection is encrypted — not that the site is genuine or clean. A cloned phishing site can show a padlock too. Verify the domain and certificate; don't treat HTTPS as a safety guarantee.",
    "Poisoned web-service attacks turn trusted websites/services into delivery vehicles — drive-by downloads, malvertising, defacement, or injected content — so even a familiar HTTPS site can be compromised. User defences are updates, ad/script hygiene, and heeding warnings; site-owner defences (conceptual) are input validation, patching, and a WAF. The padlock means encrypted, not trustworthy.",
    "poisoned web service · drive-by/malvertising/defacement · HTTPS ≠ safe (encrypted ≠ trusted) · patch + WAF + validation")

add_activity("S25 — 'Share a real scam message'  ·  ~5 min",
    ["In pairs (2 min): share a real scam SMS/email you or your family received.",
     "Identify the lure (what it wanted) and the red flags that give it away.",
     "Take 3–4 examples aloud (3 min); for each, state what the person should have done.",
     "Close: almost every example uses urgency + a link or an OTP request — the same two tells."],
    "Expect fake eSewa/Khalti rewards, bank-KYC OTP requests, fake fines, look-alike URLs. Reward pairs who name the red flag AND the correct action (verify out-of-band, never share OTP, report). Keep it defensive.",
    "ACTIVITY [~5 min].")
add_quiz("S25 — Quick Check  ·  ~5 min",
    [("Q1.  A message creating urgency to make you click a fake link is:","q"),
     ("a) malware   b) ✅ phishing   c) DoS   d) a firewall","a"),
     ("     Why: phishing manipulates a person with urgency and a fake link to hand over credentials or money.","o"),
     ("Q2.  A DoS attack primarily targets which CIA goal?","q"),
     ("a) Confidentiality   b) Integrity   c) ✅ Availability   d) authentication","a"),
     ("     Why: DoS floods a service so real users can't reach it — that is an Availability attack.","o"),
     ("Discussion: share a real scam SMS/email — what was the lure, and what should the person have done?","o")],
    "QUIZ [~5 min]. Reinforce: name the attack, name the CIA goal it hits, name the defence. Keep everything recognition-and-defence.")
add_summary("S25 · Summary  ·  [~2 min]",
    ["Malware (virus/worm/trojan/ransomware/spyware) is beaten by layered defence: updates + antivirus/EDR + least privilege + backups.",
     "Phishing targets PEOPLE with urgency and fake links — verify out-of-band, never share OTP, use MFA, and report.",
     "DoS attacks Availability (capacity/filtering/ISP+NPCERT); poisoned/HTTPS sites can be compromised — the padlock ≠ safe."],
    "These four attack families cause the majority of real incidents in Nepal — recognising them is your single highest-value skill in this unit. If you can name the trick and the defence for a scam SMS, you can protect yourself, your family, and your future employer.",
    "S26 — attacks that poison the NETWORK beneath all this: ARP, DNS, and man-in-the-middle.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S26
add_divider("Session 26 · Lecture hour 5 (of 6)","Network Infrastructure Poisoning · MITM (defensive view)",
    "You type esewa.com.np and hit your real login... or do you? What if the 'signpost' that points your browser to the right address was quietly swapped — on public café Wi-Fi?",
    "OPENING HOOK [~5 min]. Frame as conceptual recognition + countermeasures only — no execution steps. Agenda: MITM → ARP poisoning → DNS poisoning → why infrastructure attacks are dangerous.")

concept_understand("S26 · Concept 1 · [THEORY]","Man-in-the-Middle (MITM) — the Idea",
    "In a man-in-the-middle attack, an attacker secretly sits between two parties and can READ or ALTER what passes. Because it can both eavesdrop and tamper, MITM breaks Confidentiality AND Integrity. The classic setting is an untrusted/public Wi-Fi network. The universal defence is encryption: HTTPS/TLS and a VPN.",
    ["The attacker relays traffic so both sides think they're talking directly — but everything passes through.",
     "It breaks Confidentiality (reads) and Integrity (can alter) at once.",
     "Common on untrusted/public Wi-Fi where anyone nearby may be positioned in the middle.",
     "Defences: HTTPS/TLS everywhere, a VPN on untrusted networks, and take certificate warnings seriously."],
    "s26_mitm.png","MITM = a secret relay between you and the server — encryption makes the relay useless.",
    "~8 min. Localise: open Wi-Fi at Kathmandu cafés/airports/campuses as a MITM risk for anyone checking e-banking. The fix is encryption, which makes intercepted traffic unreadable and un-alterable.")
add_comparison_table("S26 · Concept 1 · comparison","Network-poisoning attacks — what each targets & its defence",
    ["Attack","What it targets","How you might notice","Key defence"],
    [["MITM","Traffic between two parties","Certificate warnings; odd behaviour","HTTPS/TLS + VPN on untrusted Wi-Fi"],
     ["ARP poisoning","The LOCAL network (LAN)","Hard to see; needs monitoring","Segmentation, DAI, encryption"],
     ["DNS poisoning","Name→address lookup","Right name but cert warnings","DNSSEC, trusted resolver, HTTPS checks"],
     ["Rogue Wi-Fi hotspot","Users on public Wi-Fi","Unexpected/duplicate network name","VPN; avoid sensitive logins on it"]],
    per_page=4,widths=[1.6,2.2,2.4,2.5],fs=10.5,
    note="Conceptual recognition + countermeasures only. The through-line: encryption (HTTPS/VPN) and heeding warnings protect the USER even when the network beneath is compromised.")
concept_apply("S26 · Concept 1 · [THEORY]","Man-in-the-Middle (MITM)",
    "Open Wi-Fi at Kathmandu cafés, the airport, and campuses is a real MITM risk for anyone checking e-banking: an attacker on the same network may be positioned to read or alter unencrypted traffic. Globally, rogue Wi-Fi hotspots in airports and cafés have intercepted unencrypted traffic. The defence that works even there is encryption — HTTPS/TLS plus a VPN — which makes any relayed traffic unreadable and un-alterable.",
    "\"Public Wi-Fi is fine if it has a password posted on the wall.\" A shared, known password protects little against someone already on the same network. The real protection is end-to-end encryption (HTTPS/VPN) and heeding certificate warnings — not whether the Wi-Fi itself asked for a password.",
    "A man-in-the-middle attack secretly places an attacker between two parties so they can read or alter the traffic, breaking Confidentiality and Integrity at once; it's most common on untrusted/public Wi-Fi. The universal defence is encryption — HTTPS/TLS everywhere and a VPN on untrusted networks — plus taking certificate warnings seriously, since encrypted traffic can't be usefully read or changed.",
    "man-in-the-middle · reads + alters traffic · breaks C and I · public Wi-Fi · HTTPS/TLS + VPN + heed cert warnings")

concept_understand("S26 · Concept 2 · [THEORY]","ARP Poisoning — What It Is",
    "ARP poisoning tricks devices on a LOCAL network into sending their traffic to the attacker by faking hardware-address mappings. The root problem: the local network trusts ARP answers blindly. This enables MITM on a LAN. We describe it conceptually — there are no spoofing commands here — and focus on the defences.",
    ["Devices on a LAN ask 'who has this address?' and trust the reply — even a forged one.",
     "A forged reply can make traffic flow through the attacker (MITM on the LAN).",
     "Defences: network segmentation, dynamic ARP inspection (DAI), encrypted traffic, monitoring.",
     "Crucially: even on a poisoned LAN, HTTPS/VPN keeps the diverted traffic unreadable."],
    "s26_arp.png","ARP poisoning abuses a LAN's blind trust — but encryption still shields your data.",
    "~7 min. Mini case: on a shared office LAN, why does HTTPS/VPN still protect you even if the LAN is poisoned? Because the attacker sees only encrypted, useless traffic. Keep it conceptual.")
add_examples_table("S26 · Concept 2 · concrete examples","ARP-poisoning situations → the safe response",
    ["Situation (defensive framing)","Why it's a risk","Safe response / defence"],
    [["Shared office LAN, sensitive logins","LAN trusts ARP replies blindly","Use HTTPS/VPN; segment the network"],
     ["Guest devices on the same LAN as servers","A guest could divert traffic","Separate VLAN for guests"],
     ["Traffic silently rerouted on the LAN","MITM enabled locally","Dynamic ARP inspection (DAI) on switches"],
     ["No monitoring of the local network","Poisoning goes unnoticed","Monitor/alert on ARP anomalies"],
     ["Plaintext (HTTP) service on the LAN","Readable if diverted","Enforce HTTPS/TLS internally too"],
     ["Café/campus Wi-Fi with many strangers","Anyone may be on your segment","VPN; avoid banking on it"]],
    per_page=6,widths=[2.7,2.3,2.7],fs=11,
    note="Framed for defence only — no spoofing steps. The universal user safety net is encryption: a poisoned LAN still can't read or alter HTTPS/VPN traffic.")
concept_apply("S26 · Concept 2 · [THEORY]","ARP Poisoning",
    "On a shared office or campus LAN, the network trusts address answers blindly, so traffic can in principle be diverted through an attacker — a local MITM. The practical point for users: even if the LAN is poisoned, HTTPS and a VPN keep the diverted traffic encrypted, and so unreadable and un-alterable. For owners, segmentation, dynamic ARP inspection, and monitoring reduce the risk at the infrastructure level.",
    "\"If the office network is compromised, there's nothing I can do.\" Encryption still protects you: on a poisoned LAN the attacker sees only scrambled HTTPS/VPN traffic. User-side encryption and owner-side controls (segmentation, DAI, monitoring) each reduce the risk from different angles.",
    "ARP poisoning tricks devices on a local network into sending traffic to an attacker by faking hardware-address mappings, exploiting the LAN's blind trust in ARP replies to enable MITM. Described conceptually (no spoofing steps), its defences are segmentation, dynamic ARP inspection, monitoring, and — critically for users — encryption (HTTPS/VPN), which keeps diverted traffic unreadable even on a poisoned LAN.",
    "ARP poisoning · LAN trusts ARP blindly · local MITM · segmentation + DAI + monitoring · encryption still protects")

concept_understand("S26 · Concept 3 · [THEORY]","DNS Poisoning / Spoofing — What It Is",
    "DNS poisoning corrupts the 'phonebook' that turns a domain name into an address, so a correct-looking name leads to a FAKE server. Forged or cached DNS answers send users to look-alike sites. The tell for a user is a certificate/security warning: the name can look right while the destination is wrong. Defences: DNSSEC, trusted resolvers, and HTTPS + certificate checks.",
    ["DNS maps names (esewa.com.np) to addresses; poisoning makes it hand back a wrong one.",
     "You see the right NAME in the address bar, but you're sent to a fake server.",
     "A certificate warning is the clue — the fake server can't present a valid certificate for the real name.",
     "Defences: DNSSEC, trusted/secure resolvers, HTTPS everywhere, and heeding security warnings."],
    "s26_dns.png","DNS poisoning = tampering the phonebook so the right NAME rings the wrong number.",
    "~8 min. Localise: redirecting users typing a Nepali bank's domain to a cloned phishing login (framed as the threat + how to detect it). The certificate warning is the defence that catches it.")
add_examples_table("S26 · Concept 3 · concrete examples","DNS-poisoning signs → what's happening → defence",
    ["Sign the user sees","What's happening","Defence / safe response"],
    [["Right name, but a certificate warning","Sent to a fake server","Stop; don't proceed; heed the warning"],
     ["Bank login looks slightly 'off'","Possible cloned site via poisoned DNS","Close it; type the address; use the app"],
     ["Redirected somewhere unexpected","Forged/cached DNS answer","Use a trusted resolver; check HTTPS cert"],
     ["No padlock / invalid certificate","Fake server can't prove the name","Never enter credentials"],
     ["Different result on mobile data vs Wi-Fi","One resolver may be poisoned","Compare; report to IT/NPCERT"],
     ["Org-wide users hitting a fake site","Cache poisoning at the resolver","DNSSEC + secure resolver at the org level"]],
    per_page=6,widths=[2.6,2.4,2.7],fs=11,
    note="Poisoned DNS shows the RIGHT name while pointing at a FAKE server — so the address bar alone isn't proof. The certificate warning is the tell; DNSSEC and trusted resolvers stop it at the infrastructure level.")
concept_apply("S26 · Concept 3 · [THEORY]","DNS Poisoning / Spoofing",
    "The threat: a user typing a Nepali bank's domain is quietly redirected to a cloned phishing login that harvests credentials — the address bar shows the right name, but the server is fake. Detecting it: the fake server can't present a valid certificate for the real domain, so a security warning appears. Defences: DNSSEC + trusted resolvers (infrastructure) plus HTTPS + certificate checks (user).",
    "\"If the address bar shows the right name, the site must be real.\" Poisoned DNS can show the right NAME while pointing at a fake server. The reliable tell is the certificate: a fake server can't present a valid one for the real domain, so a certificate warning means STOP — don't type your password.",
    "DNS poisoning/spoofing corrupts the name→address 'phonebook' so a correct-looking domain leads to a fake server, via forged or cached DNS answers. Because the name can look right while the destination is wrong, the user's tell is a certificate/security warning. Defences are DNSSEC and trusted resolvers at the infrastructure level, and HTTPS plus certificate checks (and heeding warnings) for users.",
    "DNS poisoning · name→address phonebook tampered · right name, fake server · certificate warning is the tell · DNSSEC")

concept_understand("S26 · Concept 4 · [THEORY]","Why Infrastructure Attacks Are Dangerous",
    "Attacks on the network's plumbing (ARP, DNS, MITM) are dangerous because they are SILENT and hit many users at once, below the application layer — the app looks normal while the traffic beneath is compromised. The good news: a small set of universal user defences works across all of them.",
    ["They operate beneath the app, so the app can look completely normal.",
     "They're silent and can hit many users on a network simultaneously.",
     "Universal user defences: encryption (HTTPS/VPN), heed security warnings, avoid sensitive logins on untrusted networks.",
     "Infrastructure owners add DNSSEC, DAI, segmentation, and monitoring on top."],
    None,"Infra attacks hide below the app — but encryption + heeding warnings defends against them all.",
    "~5 min. Tie the session together: three different attacks, one repeated defence — encryption and heeding warnings. That's the takeaway students must leave with.")
add_examples_table("S26 · Concept 4 · scaffolding","One universal defence set → covers all infrastructure attacks",
    ["Universal user defence","Why it works","Covers"],
    [["Use HTTPS/TLS everywhere","Encrypted traffic can't be read or altered","MITM, ARP, DNS (partially)"],
     ["Use a VPN on untrusted Wi-Fi","Wraps all traffic in encryption","MITM, ARP, rogue hotspot"],
     ["Heed certificate/security warnings","The tell that you're on a fake/relayed path","DNS poisoning, MITM"],
     ["Avoid sensitive logins on public Wi-Fi","Removes the exposure entirely","MITM, rogue hotspot"],
     ["Keep the device/browser updated","Closes flaws these attacks lean on","All"],
     ["Owners: DNSSEC, DAI, segmentation, monitoring","Fix it at the infrastructure level","DNS, ARP, MITM"]],
    per_page=6,widths=[2.8,2.7,2.0],fs=11,
    note="The unifying lesson of S26: three different plumbing attacks, ONE repeated user defence — encryption plus heeding warnings — with infrastructure owners hardening DNS/ARP/segmentation underneath.")
concept_apply("S26 · Concept 4 · [THEORY]","Why Infrastructure Attacks Are Dangerous",
    "Because ARP, DNS, and MITM operate below the application, a Nepali user's banking app or browser can look perfectly normal while the traffic beneath is being read, altered, or redirected — and one poisoned café or campus network can affect everyone on it at once. That's why the same defence keeps recurring: encryption (HTTPS/VPN), heeding certificate warnings, and not doing e-banking on untrusted Wi-Fi.",
    "\"If the app looks normal, the connection must be safe.\" Infrastructure attacks are invisible at the app layer — the page looks fine while the plumbing is compromised. Safety comes from encryption and heeding warnings, not from the app 'looking okay'.",
    "Infrastructure attacks (ARP, DNS, MITM) are dangerous because they act silently below the application layer and can hit many users at once — the app looks normal while the underlying traffic is compromised. The countermeasure is a small universal set: encryption (HTTPS/VPN), heeding security warnings, and avoiding sensitive logins on untrusted networks, with owners adding DNSSEC, DAI, and monitoring.",
    "infrastructure attacks · silent, below the app, many users · universal defence = encryption + heed warnings + avoid untrusted Wi-Fi")

add_activity("S26 — 'Café Wi-Fi and your e-banking'  ·  ~5 min",
    ["In pairs (2 min): you must check e-banking and only café Wi-Fi is available. What do you do, and why?",
     "List the risks (MITM, poisoned DNS) and the defences you'd use.",
     "Take 3–4 answers aloud (3 min); rank them from safest to riskiest.",
     "Close: safest is mobile data or wait; if you must, use a VPN + HTTPS and never ignore a certificate warning."],
    "Strong answers: prefer mobile data / the official app over café Wi-Fi; if unavoidable, use a VPN, ensure HTTPS, and treat any certificate warning as STOP. Reward reasoning about WHY encryption defeats MITM/DNS poisoning.",
    "ACTIVITY [~5 min].")
add_quiz("S26 — Quick Check  ·  ~5 min",
    [("Q1.  An attacker secretly relaying/altering traffic between two parties is performing a:","q"),
     ("a) DoS   b) ✅ man-in-the-middle attack   c) phishing   d) defacement","a"),
     ("     Why: MITM sits between two parties and can read or alter what passes — breaking Confidentiality and Integrity.","o"),
     ("Q2.  The best everyday user defence against MITM on public Wi-Fi is:","q"),
     ("a) a longer password   b) ✅ use HTTPS/VPN encryption   c) turn off the screen lock   d) delete cookies","a"),
     ("     Why: encryption makes relayed traffic unreadable and un-alterable, defeating the middle attacker.","o"),
     ("Discussion: you must check e-banking and only café Wi-Fi is available — what do you do, and why?","o")],
    "QUIZ [~5 min]. Land the through-line: three plumbing attacks, one repeated defence — encryption plus heeding certificate warnings.")
add_summary("S26 · Summary  ·  [~2 min]",
    ["MITM = an attacker secretly relaying/altering traffic (breaks Confidentiality AND Integrity), common on public Wi-Fi.",
     "ARP poisoning targets the LOCAL network; DNS poisoning targets name lookups (right name, fake server — the cert warning is the tell).",
     "Universal defence: encryption (HTTPS/VPN) + heed security warnings + avoid sensitive logins on untrusted networks."],
    "As a future IT manager you'll set café-Wi-Fi policy, VPN rules, and HTTPS enforcement — these concepts let you justify those rules to a non-technical boss ('encryption is why a poisoned network still can't read our traffic'). It's the reasoning, not just the rule.",
    "S27 — WHO is behind all these attacks, and why: cyberattackers and their coloured hats.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S27
add_divider("Session 27 · Lecture hour 6 (of 6) — CLOSES UNIT 5","Cyberattackers and Their Coloured Hats",
    "The same skill that breaks into a bank can also be PAID by that bank to break in first and report it. So is a 'hacker' a criminal, a hero, or just a job title?",
    "OPENING HOOK [~5 min]. Draw out that MOTIVE and AUTHORISATION — not skill — define the hat. Agenda: coloured hats → attacker types by motive → why classifying attackers shapes defence.")

concept_understand("S27 · Concept 1 · [THEORY]","The Coloured Hats",
    "Hackers are classified by INTENT and AUTHORISATION, not by skill. A white hat is authorised and ethical (a penetration tester). A black hat is malicious and illegal. A grey hat is unauthorised but not (always) malicious — still illegal, because they act without permission even if they mean to help.",
    ["White hat: hired/authorised to test and improve security — legal, ethical (e.g. bug bounties).",
     "Black hat: attacks for malicious or criminal ends — illegal.",
     "Grey hat: pokes without permission and may report the flaw — well-meaning but still illegal.",
     "The hat is about authorisation + intent; the same technical skill sits behind all three."],
    "s27_hats.png","The hat is authorisation + intent, not skill — same knowledge, different purpose.",
    "~7 min. Localise: Nepali ethical-hacker/bug-bounty researchers who responsibly report flaws in bank/government sites (white) vs those who defaced them (black). Bust 'all hackers are criminals'.")
add_comparison_table("S27 · Concept 1 · comparison","White vs Grey vs Black hat",
    ["Dimension","White hat","Grey hat","Black hat"],
    [["Authorised?","Yes — invited","No","No"],
     ["Intent","Improve security","Mixed / curious","Malicious / criminal"],
     ["Legal?","Legal","Illegal (no permission)","Illegal"],
     ["Typical activity","Pen-test, bug bounty","Unrequested probing, then report","Fraud, ransomware, theft"],
     ["Nepal example","Reports a bank flaw responsibly","Finds a gov flaw uninvited","Defaces / steals data"]],
    per_page=5,widths=[1.5,2.2,2.2,2.2],fs=10.5,
    note="It's about authorisation + intent, not skill. A grey hat may mean well but is still acting illegally by probing without permission — good intentions don't make it authorised.")
concept_apply("S27 · Concept 1 · [THEORY]","The Coloured Hats",
    "In Nepal, ethical-hacker and bug-bounty researchers who responsibly report flaws in bank or government sites are white hats — invited or acting within a disclosure programme. Those who defaced the same sites are black hats. Globally, bug-bounty researchers (white) and ransomware operators (black) may possess identical skills; the hat is defined by whether they had permission and what they intended.",
    "\"All hackers are criminals.\" The hat is about authorisation and intent, not skill — many hackers are paid defenders (penetration testers, bug-bounty researchers) who make systems safer. Skill is neutral; how and why you use it decides the colour of the hat.",
    "Hackers are classified by intent and authorisation, not skill: a white hat is authorised and ethical (pen-testers, bug bounties), a black hat is malicious and illegal, and a grey hat is unauthorised but not necessarily malicious — still illegal because they act without permission. The same technical knowledge underlies all three, so the hat depends on authorisation plus intent, not ability.",
    "coloured hats · white/grey/black · authorisation + intent, not skill · pen-tester vs criminal · grey = illegal but not malicious")

concept_understand("S27 · Concept 2 · [THEORY]","Attacker Types by Motive",
    "Different attackers want different things, and motive predicts their behaviour. Script kiddies (low skill, seek thrills) use others' tools; hacktivists are politically/socially motivated; cybercriminals/organised crime want money; state/nation-state actors ('APT') pursue espionage and sabotage with deep resources; insiders misuse legitimate access, maliciously or by negligence.",
    ["Script kiddies: low skill, borrowed tools, chasing notoriety or thrills.",
     "Hacktivists: defacements, leaks, DDoS to make a political/social point.",
     "Cybercriminals / organised crime: fraud, ransomware, data theft — for money.",
     "State actors (APT): espionage, sabotage, strategic advantage — well-resourced and persistent.",
     "Insiders: employees/contractors misusing access — malicious OR simply negligent."],
    None,"Motive predicts the attacker: thrill, politics, money, espionage, or misused access.",
    "~9 min. Mini case: a site defaced with a political message and no money stolen — which type? (Hacktivist.) Localise each type with a Nepal example. Note insiders can be negligent, not just malicious.")
add_comparison_table("S27 · Concept 2 · comparison","Attacker types — motive, typical target & key defence",
    ["Attacker type","Motive","Typical target","Key defence"],
    [["Script kiddie","Thrills, notoriety","Easy, exposed systems","Patch, basic hygiene, MFA"],
     ["Hacktivist","Political / social message","Public gov / high-profile sites","DDoS defence, patching, monitoring"],
     ["Cybercriminal / org. crime","Money","Banks, wallets, personal data","Fraud controls, backups, MFA, monitoring"],
     ["State / nation-state (APT)","Espionage, sabotage","Government, critical infrastructure","Defence-in-depth, threat intel, segmentation"],
     ["Insider (malicious)","Revenge, profit","Own employer's data/systems","Least privilege, logging, separation of duties"],
     ["Insider (negligent)","(none — carelessness)","Accidental exposure","Training, DLP, access reviews"]],
    per_page=6,widths=[2.0,1.9,2.2,2.4],fs=10.5,
    note="Motive predicts target, method, and persistence — so it shapes which defences you prioritise. Note insiders split into malicious AND negligent; both need trust + monitoring controls, not just firewalls.")
concept_apply("S27 · Concept 2 · [THEORY]","Attacker Types by Motive",
    "In Nepal, hacktivist defacements of government sites have flared during regional tensions (a political message, not theft); financially-motivated fraud is framed by incidents like the NIC ASIA SWIFT case (money is the goal); and insiders misuse legitimate access. Worked mini-case: a site defaced with a political message and no money stolen points to a hacktivist, whose goal is attention, not profit.",
    "\"The biggest threat is always an outside genius hacker.\" In reality, insiders and simple phishing cause a large share of real damage, and much crime uses rented, unsophisticated tools. Ranking attackers by Hollywood image, not by motive and likelihood, misdirects your defences.",
    "Attackers are classified by motive, which predicts their behaviour: script kiddies (thrills, borrowed tools), hacktivists (political/social — defacements, leaks, DDoS), cybercriminals/organised crime (money — fraud, ransomware), state/nation-state actors (espionage/sabotage, well-resourced APTs), and insiders (misusing access, maliciously or negligently). Naming the motive tells you the likely target and method.",
    "script kiddie · hacktivist · cybercriminal · state actor (APT) · insider (malicious/negligent) · motive predicts behaviour")

concept_understand("S27 · Concept 3 · [THEORY]","Why Classifying Attackers Matters for Defence",
    "Motive predicts target, method, and persistence — so knowing WHO you face shapes your defence priorities. A bank fears organised crime and insiders most; a ministry fears state actors and hacktivists. And insiders need trust + monitoring controls (least privilege, logging), not just firewalls, because they're already inside.",
    ["Match the defence to the likely attacker: a bank hardens against fraud + insiders first.",
     "A ministry prioritises against state actors (APT) and hacktivists.",
     "Firewalls stop outsiders; insiders need least privilege, logging, and separation of duties.",
     "Spend the budget where the real, likely threat is — not on the scariest headline."],
    None,"Know your likely attacker and you know where to spend defence — motive shapes priorities.",
    "~5 min. The analogy: hats are like jersey colours — same game, but you defend differently against each team. Land that insiders + phishing, not a lone genius, cause much of the real damage.")
add_examples_table("S27 · Concept 3 · scaffolding","Organisation → top attacker to fear → defence priority (Nepal)",
    ["Organisation","Top attacker(s) to fear","Defence priority"],
    [["Commercial bank","Organised crime + insiders","Fraud controls, least privilege, monitoring, MFA"],
     ["Government ministry","State actors + hacktivists","Defence-in-depth, DDoS defence, threat intel"],
     ["College / campus","Script kiddies + phishing","Patching, MFA, awareness training"],
     ["Fintech / wallet (eSewa-like)","Cybercriminals + insiders","Fraud detection, segregation of duties, backups"],
     ["Hospital","Ransomware crews","Tested backups, segmentation, patching"],
     ["Telecom / ISP","State actors + DDoS crews","Infrastructure hardening, scrubbing, monitoring"]],
    per_page=6,widths=[2.3,2.4,3.0],fs=11,
    note="Motive predicts target and method, so it sets defence priorities. Insiders need trust + monitoring controls (least privilege, logging), not just a firewall — they're already inside.")
concept_apply("S27 · Concept 3 · [THEORY]","Why Classifying Attackers Matters for Defence",
    "A Nepali bank spends most on fraud controls, least privilege, and monitoring because organised crime and insiders are its realistic top threats; a ministry invests in defence-in-depth and DDoS resilience because it faces state actors and hacktivists. Matching defence to the likely attacker — rather than to the scariest movie villain — is how limited security budgets get spent where they actually reduce risk.",
    "\"Just buy a firewall and you're safe from everyone.\" A firewall stops outside network attacks but does little against an insider who already has access or a user tricked by phishing. Different motives need different controls — insiders need least privilege, logging, and separation of duties, not just a perimeter.",
    "Classifying attackers matters because motive predicts target, method, and persistence, so it shapes defence priorities: a bank hardens against organised crime and insiders, a ministry against state actors and hacktivists. Insiders in particular need trust and monitoring controls (least privilege, logging, separation of duties), not just firewalls — letting an organisation spend its limited budget where the real threat lies.",
    "motive predicts defence · bank vs ministry priorities · insiders need trust + monitoring · spend on likely, not scary")

add_activity("S27 — 'Biggest real risk to a Nepali bank?'  ·  ~5 min",
    ["In pairs (2 min): which attacker type is the biggest REAL risk to a Nepali bank — and why?",
     "Rank organised crime, insiders, hacktivists, and state actors for a bank specifically.",
     "Take 3–4 answers aloud (3 min); tie each to the defence it demands.",
     "Close: for a bank, organised crime + insiders usually top the list — and insiders need monitoring, not just a firewall."],
    "Reward reasoning that links MOTIVE to TARGET to DEFENCE. Draw out that insiders and phishing, not a lone genius, cause much real damage — so trust + monitoring controls matter as much as perimeter firewalls.",
    "ACTIVITY [~5 min].")
add_quiz("S27 — Quick Check  ·  ~5 min",
    [("Q1.  A hacker authorised to test a system to improve its security is a:","q"),
     ("a) black hat   b) grey hat   c) ✅ white hat   d) script kiddie","a"),
     ("     Why: white hats act with authorisation and good intent — the hat is about authorisation + intent, not skill.","o"),
     ("Q2.  An employee misusing legitimate access is an:","q"),
     ("a) outsider   b) ✅ insider threat   c) hacktivist   d) script kiddie","a"),
     ("     Why: insiders already have access, so they need least privilege, logging, and monitoring — not just a firewall.","o"),
     ("Discussion: which attacker type is the biggest real risk to a Nepali bank — and why?","o")],
    "QUIZ [~5 min]. Land the two big corrections: the hat is intent+authorisation not skill, and insiders/phishing cause much of the real damage.")
add_summary("S27 · Summary  ·  [~2 min]",
    ["Hats = intent + authorisation, not skill: white (authorised/ethical), black (malicious/illegal), grey (unauthorised but not always malicious — still illegal).",
     "Attackers range from script kiddies to hacktivists, cybercriminals, state actors (APT), and insiders (malicious or negligent).",
     "Motive predicts target and method, so it shapes defence — a bank fears crime + insiders; insiders need trust + monitoring, not just firewalls."],
    "Knowing WHO attacks and WHY lets you (and your future employer) spend defence budget where the real threats are, instead of on fear. This closes Unit 5: you now have the CIA vocabulary, the risk formula, the attack/defence pairs, and the attacker map.",
    "Next unit — from these fundamentals to PERSONAL cybersecurity: your own devices, accounts, and passwords.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 5 · Cheat Sheet","One-page revision reference",
    [("Foundations (S22)","Cyberspace = whole connected digital domain (not just websites). Cybersecurity = people + process + technology. CIA triad: Confidentiality (secrecy) · Integrity (unaltered) · Availability (usable) — every control serves C/I/A."),
     ("Threat landscape (S23)","New tech (cloud/mobile/IoT/AI/remote) grows the attack surface. Crime is a business: Ransomware-/Cybercrime-as-a-Service rents tools to low-skill attackers. Outsourcing = supply-chain risk; you outsource work, not accountability."),
     ("Risk (S24)","Threat = could harm · Vulnerability = weakness · Asset = what you protect. Risk = threat × vulnerability × impact (multiply). No vulnerability ⇒ threat can't land. Goal = reduce to ACCEPTABLE, not zero (residual risk)."),
     ("Common attacks (S25)","Malware (virus/worm/trojan/ransomware/spyware) → update+EDR+least priv+backups. Phishing → verify out-of-band, never share OTP, MFA. DoS → attacks Availability; rate-limit/CDN/ISP+NPCERT. Poisoned/HTTPS site → padlock ≠ safe."),
     ("Network poisoning (S26)","MITM = secret relay (breaks C+I), common on public Wi-Fi. ARP = poisons the LAN; DNS = right name, fake server (cert warning is the tell). Universal defence: HTTPS/VPN + heed warnings + avoid untrusted Wi-Fi logins."),
     ("Attackers (S27)","Hats = intent + authorisation, not skill: white/grey/black. Types: script kiddie · hacktivist · cybercriminal · state (APT) · insider. Motive predicts target → shapes defence. Insiders need monitoring, not just firewalls.")])

add_glossary("Unit 5 · Glossary","Key terms — quick reference",
    [("Cyberspace","the interconnected digital environment of networks, systems, data, and people/devices."),
     ("Cybersecurity","protecting systems, networks & data from unauthorised access, harm, or disruption."),
     ("People/process/technology","the three pillars of security; the weakest sets your real security."),
     ("CIA triad","Confidentiality, Integrity, Availability — the three goals every control serves."),
     ("Confidentiality","data kept secret / access-controlled."),
     ("Integrity","data stays unchanged and trustworthy."),
     ("Availability","the system is usable when needed."),
     ("Attack surface","the sum of all points where an attacker could try to get in."),
     ("Ransomware-as-a-Service","rented ready-made ransomware tools for low-skill attackers."),
     ("Supply-chain risk","a vendor's weakness becoming your breach; work is outsourced, accountability isn't."),
     ("Threat","something that could cause harm."),
     ("Vulnerability","a weakness a threat can exploit."),
     ("Asset","what you're protecting (data, money, service, reputation)."),
     ("Risk","threat × vulnerability × impact — likelihood × consequence."),
     ("Residual risk","the risk left after controls; you reduce risk to acceptable, not zero."),
     ("Malware","malicious software: virus, worm, trojan, ransomware, spyware."),
     ("Phishing","tricking a person into giving credentials/money/clicks via fake messages."),
     ("Spear-phishing","targeted, researched phishing that can fool experts."),
     ("DoS / DDoS","flooding a service so real users can't reach it — attacks Availability."),
     ("Poisoned web service","a trusted site turned into a delivery vehicle (drive-by, malvertising, defacement)."),
     ("MITM","attacker secretly relays/alters traffic between two parties (breaks C and I)."),
     ("ARP poisoning","faking hardware-address mappings to divert LAN traffic (local MITM)."),
     ("DNS poisoning","corrupting name→address lookup so a right-looking name leads to a fake server."),
     ("DNSSEC","authentication for DNS answers that helps prevent DNS poisoning."),
     ("White/grey/black hat","hacker classes by authorisation + intent (not skill)."),
     ("APT","advanced persistent threat — a well-resourced state/organised actor."),
     ("Insider threat","an employee/contractor misusing access — malicious or negligent."),
     ("NPCERT","Nepal's national Computer Emergency Response Team.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 5 · Revision","Consolidated end-of-unit quiz",
    "Ten MCQs across the whole unit (answers shown), then short-answer, applied-case, and discussion questions to work from the concept slides and Unit5_material.md. All content stays defensive / conceptual — no attack-execution steps.",
    "Use as a 15–20 min in-class quiz or take-home review.")
add_quiz("Section A — Multiple choice (answers shown)",
    [("1.  Cyberspace is best described as   →  ✅ the whole connected digital domain (not just websites)","a"),
     ("2.  The three CIA goals are   →  ✅ Confidentiality, Integrity, Availability","a"),
     ("3.  Ransomware locking files mainly violates   →  ✅ Availability","a"),
     ("4.  Secretly altering data violates   →  ✅ Integrity","a"),
     ("5.  The attack surface grows mainly because   →  ✅ more devices, data, and entry points are added","a"),
     ("6.  Ransomware-as-a-Service matters because it   →  ✅ lets low-skill attackers rent powerful tools","a"),
     ("7.  Risk is expressed as   →  ✅ threat × vulnerability × impact","a"),
     ("8.  A weakness an attack can exploit is a   →  ✅ vulnerability (a threat is what exploits it)","a"),
     ("9.  A message using urgency + a fake link is   →  ✅ phishing; the best MITM defence is   →  ✅ HTTPS/VPN","a"),
     ("10.  A hacker authorised to test a system is a   →  ✅ white hat; an employee misusing access is an   →  ✅ insider","a")],
    "Consolidated quiz Section A.",compact=True)
add_quiz("Sections B–D — short answer, applied case & discussion",
    [("Section B — Short answer","q"),
     ("11. Define cybersecurity (people+process+tech).   12. Explain each letter of the CIA triad with a Nepal example.","o"),
     ("13. Why does outsourcing keep accountability with you?   14. State and explain risk = threat × vulnerability × impact.   15. List 3 defences against phishing.","o"),
     ("Section C — Applied case","q"),
     ("16. For a Nepali bank or campus: identify the asset, threat, vulnerability, and impact, then propose two controls.","o"),
     ("17. A cloned/poisoned login page is reached via the right-looking address — name the likely technique and the user-side defence.","o"),
     ("Section D — Discussion","q"),
     ("18. For a Nepali ministry, rank hacktivists, organised crime, state actors, and insiders by real-world risk — justify your top two.","o")],
    "Consolidated quiz Sections B–D. Model answers on the concept slides and in Unit5_material.md. All defensive/conceptual.",compact=True)

# ---- close ----
add_title("End of Unit 5  ·  IT 246",
          "S22–S27 complete: cyberspace & the CIA triad · threat-landscape drivers · risk = T × V × I · common attacks & poisoned web services · ARP/DNS/MITM poisoning · cyberattackers & their hats",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · defensive/awareness framing (no attack recipes) · "
          "self-contained, PDF-safe · Next: Units 6–8 — personal security, cryptography & digital forensics.")

_add_page_numbers()
save("IT246_Unit5.pptx")
