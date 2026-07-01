# Unit 5 — Fundamentals of Cybersecurity · Content Outline

**6 LHs → 6 sessions (S22–S27) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.
**Framing note:** this is a *defensive / educational* unit — every attack is described to **recognize and defend** against it, never as step-by-step "how to attack." No exploit recipes.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 5 learning outcomes (what students can do after S22–S27)
1. Define cyberspace and cybersecurity, and explain the CIA triad as the core security objective.
2. Explain how technological change, economic-model shifts, and outsourcing reshape the threat landscape.
3. Express risk in terms of threat × vulnerability × impact and use it to prioritize defenses.
4. Recognize common cyberattacks (malware, phishing, DoS, web-based attacks) and the defenses against them.
5. Explain network-infrastructure poisoning (ARP/DNS) and man-in-the-middle conceptually, and name the countermeasures.
6. Classify cyberattackers by motive and "hat" (white/black/grey, script kiddies, hacktivists, state actors, insiders).

---

## S22 — Introduction to Cyberspace & Cybersecurity · Cybersecurity Perspectives (CIA triad)

**Hook:** "Your eSewa balance, your exam results on a college portal, the NEA billing system, the army's email — all live in the same 'place' that doesn't physically exist. Who is responsible for keeping it safe, and safe *from what exactly*?" → cyberspace + what 'secure' even means.

**Concepts & how each will be filled:**

1. **Cyberspace**
   - Definition: the interconnected digital environment of networks, systems, data, and the people/devices using them.
   - Theory: not just "the internet" — includes private networks, cloud, OT/ICS, mobile; a domain like land/sea/air.
   - Global example: cyberspace treated as the "fifth domain" of conflict by NATO/militaries.
   - Local example: Nepal's growing cyberspace — National ID, eSewa/Khalti, Nagarik App, online banking, e-governance portals.
   - Misconception: *"Cyberspace = the websites I visit."* Correction: it includes back-end systems, infrastructure, and offline-connected devices too.

2. **Cybersecurity**
   - Definition: the practice of protecting systems, networks, and data from unauthorized access, harm, or disruption.
   - Theory: people + process + technology, not just antivirus; defensive discipline.
   - Local example: Nepal CERT / NPCERT and the IT Emergency Response role; banks' security teams under NRB cyber-resilience guidance.
   - Mini case: "A college server is reachable from the internet with a default admin password — is the threat the password, the exposure, or both?"

3. **Cybersecurity perspectives — the CIA triad**
   - Definition: Confidentiality, Integrity, Availability — the three goals every control serves.
   - Theory: C = secrecy/access control; I = data unchanged/trustworthy; A = system usable when needed. Trade-offs between them.
   - Global example: ransomware breaks Availability; a leaked database breaks Confidentiality; a tampered exam result breaks Integrity.
   - Local example: a DDoS knocking a Nepali bank's e-banking offline = Availability; altered land-records data = Integrity.
   - Misconception: *"Security just means keeping secrets (Confidentiality)."* Correction: an always-down, tamper-prone system is insecure even if nothing leaks.
   - Fun element: analogy — CIA triad is a three-legged stool; saw off any leg and you fall.

**Check for understanding:**
- MCQ1: A ransomware attack that locks files mainly violates…? → Availability ✅
- MCQ2: Ensuring data has not been secretly altered is…? → Integrity ✅
- Discussion: "For your college result portal, rank C, I, and A by importance — and justify."

**Real-life application:** every security job, audit, and bank inspection is ultimately checking C, I, and A — it's the vocabulary you'll use for the rest of the course.

**Summary:** (1) cyberspace = the whole connected digital domain; (2) cybersecurity = people+process+tech; (3) CIA triad is the goal. **Next:** what *forces* keep changing this landscape.

**Visual cues:** CIA triad triangle with one Nepal example per corner; "fifth domain" map graphic.

---

## S23 — Key Development Areas: Technological Changes · Economic Model Shifts · Outsourcing

**Hook:** "Ten years ago a Nepali shop kept cash in a drawer. Today it takes QR payments, stores customer numbers in the cloud, and runs on a phone. Did the shop get a security team too?" → why the attack surface keeps exploding.

**Concepts & how each will be filled:**

1. **Technological changes expand the attack surface**
   - Definition: each new technology adds new things to defend.
   - Theory: cloud, mobile, IoT, AI, remote work — more devices/data/entry points = bigger attack surface.
   - Global example: billions of IoT devices shipped with weak defaults became botnet fuel.
   - Local example: explosion of QR payments (fonepay), Nagarik App, smart CCTV, and IoT in Nepali homes/offices.
   - Misconception: *"New tech is automatically more secure."* Correction: new features usually arrive before their security does.

2. **Economic model shifts**
   - Definition: cybercrime and IT itself have become businesses, changing who attacks and why.
   - Theory: subscription/cloud (SaaS) shifts where data lives; "Cybercrime-as-a-Service" / ransomware-as-a-service lowers the skill needed to attack; data itself becomes a traded commodity.
   - Global example: ransomware gangs operating like companies with "customer support."
   - Local example: stolen card/eSewa/bank credentials sold in bulk; pre-packaged phishing kits targeting Nepali users.
   - Mini case: "Why does a low-skill criminal in 2026 pose more risk than one in 2010?" (answer: rented tools).

3. **Outsourcing & the supply chain**
   - Definition: relying on third-party vendors/contractors introduces *their* risk into *your* system.
   - Theory: third-party access, shared credentials, managed services = trust extended outside your walls (supply-chain risk).
   - Local example: Nepali banks/government outsourcing software development or hosting to outside vendors; a vendor breach becomes your breach.
   - Misconception: *"If we outsource IT, we outsource the risk too."* Correction: you outsource the work, not the accountability.
   - Fun element: analogy — outsourcing is giving a spare house key to a contractor; convenient, but now their carelessness is your break-in.

**Check for understanding:**
- MCQ1: "Attack surface" grows mainly because…? → more devices, data, and entry points are added ✅
- MCQ2: "Ransomware-as-a-Service" matters because it…? → lets low-skill attackers rent powerful tools ✅
- Discussion: "Name one new technology your family adopted recently — what new risk came with it?"

**Real-life application:** when you propose a new system at work (cloud, a vendor, an app), you'll be expected to ask "what new risk does this add?" — this is that habit.

**Summary:** (1) new tech grows the attack surface; (2) crime/IT became business models; (3) outsourcing extends trust + accountability stays yours. **Next:** turning all this into measurable *risk*.

**Visual cues:** growing "attack surface" graphic (2010 vs 2026 device cloud); supply-chain trust diagram (you → vendor → vendor's vendor).

---

## S24 — Risks Cybersecurity Mitigates (threats, vulnerabilities, risk = threat × vulnerability × impact)

**Hook:** "Two laptops. One holds wedding photos with no internet; one holds a bank's customer database online. Same 'virus' lands on both — which keeps you up at night, and *why* can you now say it precisely?" → risk = more than the threat.

**Concepts & how each will be filled:**

1. **Threats, vulnerabilities, and assets**
   - Definition: threat = something that *could* cause harm; vulnerability = a weakness it can exploit; asset = what you're protecting.
   - Theory: threat actor + threat → exploits a vulnerability → harms an asset. No vulnerability ⇒ the threat can't land.
   - Global example: an unpatched server (vulnerability) + a worm (threat) = mass compromise.
   - Local example: a Nepali government site running outdated software (vulnerability) is repeatedly defaced (threat realized).
   - Misconception: *"Threat and vulnerability are the same thing."* Correction: a flood is a threat; living in a basement is the vulnerability.

2. **Risk = threat × vulnerability × impact**
   - Definition: risk is the *likelihood × consequence* of a threat exploiting a vulnerability.
   - Theory: high threat but no vulnerability ≈ low risk; tiny vulnerability with catastrophic impact ≈ high risk. Used to prioritize spending.
   - Local example: framing the NIC ASIA SWIFT fraud incident as high-impact (large funds moved) → why financial systems get the most defense budget.
   - Mini case: "Rank three risks for a campus: (a) a defaced public webpage, (b) leaked student grades, (c) a wiped payroll database — using impact."

3. **What cybersecurity actually mitigates**
   - Definition: the goal is to *reduce risk to an acceptable level*, not reach zero.
   - Theory: reduce threat exposure, fix vulnerabilities (patching), and limit impact (backups, segmentation); residual risk always remains.
   - Misconception: *"Good security means zero risk."* Correction: zero risk is impossible; you manage it down to acceptable.
   - Fun element: analogy — you can't make crossing the road risk-free, but a zebra crossing + looking both ways makes the risk acceptable.

**Check for understanding:**
- MCQ1: A weakness that an attack can exploit is a…? → vulnerability ✅
- MCQ2: In risk = threat × vulnerability × impact, patching a flaw mainly reduces the…? → vulnerability factor ✅
- Discussion: "Pick one device you own; name one threat, one vulnerability, and the impact if it's compromised."

**Real-life application:** security budgets and exam-grade priorities are set by risk, not fear — this formula is how professionals decide what to fix first.

**Summary:** (1) threat ≠ vulnerability ≠ impact; (2) risk multiplies all three; (3) we manage risk down, never to zero. **Next:** the actual attacks that exploit these vulnerabilities.

**Visual cues:** "risk = T × V × I" formula card with a worked Nepal example; risk-priority matrix (likelihood vs impact, 2×2).

---

## S25 — Common Cyberattacks · Poisoned Web Service Attacks (defensive view)

**Hook:** "An SMS says 'Your eSewa/IME is blocked — verify here' with a link. A pop-up says 'Your PC has 5 viruses, call this number.' Both want one thing from you. Can you name the trick *and* the defense?" → recognizing attacks to stop them.

**Concepts & how each will be filled:** *(all described for recognition + defense — no how-to-attack steps)*

1. **Malware (recognition & defense)**
   - Definition: malicious software — viruses, worms, trojans, ransomware, spyware.
   - Theory: how each *behaves* (spreads / hides / locks / spies) and the warning signs; defenses = updates, antivirus/EDR, least privilege, backups.
   - Global example: WannaCry ransomware spreading via an unpatched flaw worldwide.
   - Local example: ransomware/malware reports against Nepali businesses and government offices; pirated software as a common infection route in Nepal.
   - Misconception: *"Antivirus alone keeps me safe."* Correction: updates, backups, and careful clicks matter as much.

2. **Phishing & social-lure attacks (recognition & defense)**
   - Definition: tricking a person into giving credentials/money/clicks via fake messages.
   - Theory: signs — urgency, mismatched links, look-alike domains, requests for OTP/PIN; defenses = verify out-of-band, never share OTP, MFA, report.
   - Local example: fake "eSewa/Khalti reward," fake bank-KYC SMS, fake Nepal Police/IRD fine messages, look-alike domains (e.g., subtly misspelled bank URLs).
   - Mini case: "An email from 'your principal' urgently asks for gift cards — list 3 red flags." (defensive checklist).
   - Misconception: *"Only careless people fall for phishing."* Correction: well-crafted, targeted phishing (spear-phishing) fools experts too.

3. **Denial-of-Service (DoS/DDoS) — conceptual**
   - Definition: overwhelming a service so legitimate users can't reach it (attacks Availability).
   - Theory: many requests flood a server; defenses (conceptual) = rate-limiting, CDNs/scrubbing, capacity, ISP/CERT coordination. *No traffic-generation instructions.*
   - Local example: Nepali bank / government portals knocked offline during hacktivist campaigns.

4. **Poisoned web-service & web-based attacks (recognition & defense)**
   - Definition: trusted websites/services turned into delivery vehicles — drive-by downloads, malvertising, defacement, injection of malicious content.
   - Theory: signs a site is compromised; user defenses = updates, ad/script hygiene, HTTPS awareness; site-owner defenses (conceptual) = input validation, patching, WAF.
   - Local example: defacement of Nepali government websites; fake/cloned banking login pages hosted on poisoned or look-alike sites.
   - Misconception: *"A familiar/HTTPS site is always safe."* Correction: trusted sites can be compromised; the padlock means encrypted, not trustworthy.
   - Fun element: analogy — a poisoned web service is a tampered sample at a trusted store; you trusted the shop, not the tampering.

**Check for understanding:**
- MCQ1: A message creating urgency to make you click a fake link is…? → phishing ✅
- MCQ2: A DoS attack primarily targets which CIA goal? → Availability ✅
- Discussion: "Share a real scam SMS/email you (or family) received — what was the lure, and what should they have done?"

**Real-life application:** these four attack families cause the majority of real incidents in Nepal — recognizing them is your single highest-value skill in this unit.

**Summary:** (1) malware = malicious software, beaten by updates+backups+care; (2) phishing targets *people*; (3) DoS attacks Availability; (4) trusted sites can be poisoned. **Next:** attacks that poison the *network* beneath all this.

**Visual cues:** "spot-the-phish" annotated SMS/email; attack-family table (attack → CIA goal hit → defense); padlock-≠-safe callout.

---

## S26 — Network Infrastructure Poisoning · Technical Attack Techniques (ARP/DNS poisoning, MITM — defensive view)

**Hook:** "You type esewa.com.np and hit your real login... or do you? What if the 'signpost' that points your browser to the right address was quietly swapped — on public café Wi-Fi?" → attacks on the plumbing of the network.

**Concepts & how each will be filled:** *(conceptual recognition + countermeasures only — no execution steps)*

1. **Man-in-the-Middle (MITM) — the idea**
   - Definition: an attacker secretly sits between two parties, able to read or alter what passes.
   - Theory: why it breaks Confidentiality *and* Integrity; common setting = untrusted/public Wi-Fi. Defenses = HTTPS/TLS everywhere, VPN on untrusted networks, certificate warnings taken seriously.
   - Global example: rogue Wi-Fi hotspots in airports/cafés intercepting unencrypted traffic.
   - Local example: open Wi-Fi at Kathmandu cafés/airports/campuses as a MITM risk for users checking e-banking.
   - Misconception: *"Public Wi-Fi is fine if it has a password posted on the wall."* Correction: a shared/known password protects little against someone on the same network.

2. **ARP poisoning — what it is**
   - Definition: tricking devices on a *local* network into sending traffic to the attacker by faking hardware-address mappings.
   - Theory (conceptual): the local network trusts ARP answers blindly, enabling MITM on a LAN; defenses = network segmentation, dynamic ARP inspection, encrypted traffic, monitoring. *No spoofing commands.*
   - Mini case: "On a shared office LAN, why does encryption (HTTPS/VPN) still protect you even if the LAN is poisoned?"

3. **DNS poisoning / spoofing — what it is**
   - Definition: corrupting the "phonebook" that turns a domain name into an address, so a correct-looking name leads to a fake server.
   - Theory (conceptual): forged or cached DNS answers send users to look-alike sites; defenses = DNSSEC, trusted resolvers, HTTPS + certificate checks, watching for cert/security warnings.
   - Local example: redirecting users typing a Nepali bank's domain to a cloned phishing login (framed as the threat + how to detect it).
   - Misconception: *"If the address bar shows the right name, the site must be real."* Correction: poisoned DNS can show the right *name* while pointing at a fake server — certificate warnings are the tell.
   - Fun element: analogy — DNS poisoning is tampering with the phone directory so the right name lists the wrong number.

4. **Why infrastructure attacks are dangerous (defensive takeaway)**
   - Theory: they're *silent* and hit many users at once below the application layer; the universal user defenses = encryption (HTTPS/VPN), heed security warnings, avoid sensitive logins on untrusted networks.

**Check for understanding:**
- MCQ1: An attacker secretly relaying/altering traffic between two parties is performing a…? → man-in-the-middle attack ✅
- MCQ2: The best everyday user defense against MITM on public Wi-Fi is…? → use HTTPS/VPN encryption ✅
- Discussion: "You must check e-banking and only café Wi-Fi is available — what do you do, and why?"

**Real-life application:** as a future IT manager you'll choose café-Wi-Fi policy, VPNs, and HTTPS enforcement — these concepts justify those rules to non-technical bosses.

**Summary:** (1) MITM = attacker in the middle; (2) ARP poisoning targets the LAN, DNS poisoning targets name lookups; (3) encryption + heeding warnings is the universal defense. **Next:** *who* is behind all these attacks, and why.

**Visual cues:** MITM diagram (user — attacker — server); "DNS phonebook" tampering graphic; ARP-LAN trust illustration.

---

## S27 — Cyberattackers and Their Colored Hats (closes Unit 5)

**Hook:** "The same skill that breaks into a bank can also be paid by that bank to break in *first* and report it. So is a 'hacker' a criminal, a hero, or just a job title?" → motive defines the hat.

**Concepts & how each will be filled:**

1. **The colored hats**
   - Definition: hackers classified by intent and authorization, not skill.
   - Theory: **white hat** = authorized, ethical (pen-testers); **black hat** = malicious/illegal; **grey hat** = unauthorized but not (always) malicious — still illegal.
   - Global example: bug-bounty researchers (white) vs ransomware operators (black).
   - Local example: Nepali ethical-hacker/bug-bounty researchers who responsibly report flaws in Nepali bank/government sites vs attackers who defaced them.
   - Misconception: *"All hackers are criminals."* Correction: the hat is about authorization + intent; many are paid defenders.

2. **Attacker types by motive**
   - Definition & motive of each:
     - **Script kiddies** — low skill, use others' tools, seek thrills/notoriety.
     - **Hacktivists** — politically/socially motivated (defacements, leaks, DDoS).
     - **Cybercriminals / organized crime** — money (fraud, ransomware, data theft).
     - **State / nation-state actors** — espionage, sabotage, strategic advantage; well-resourced ("APT").
     - **Insiders** — employees/contractors misusing access (malicious or negligent).
   - Local example: hacktivist defacements of Nepali government sites during regional tensions; financially-motivated fraud framed around the NIC ASIA SWIFT-style incident; insider misuse of access at an organization.
   - Mini case: "A site is defaced with a political message and no money is stolen — which attacker type, and what's their goal?"

3. **Why classifying attackers matters for defense**
   - Theory: motive predicts target, method, and persistence → shapes your defense priorities (a bank fears organized crime + insiders most; a ministry fears state actors + hacktivists). Insiders need *trust + monitoring* controls, not just firewalls.
   - Misconception: *"The biggest threat is always an outside genius hacker."* Correction: insiders and simple phishing cause a large share of real damage.
   - Fun element: analogy — hats are like jersey colors; same game, but you defend differently against each team.

**Check for understanding:**
- MCQ1: A hacker authorized to test a system to improve its security is a…? → white hat ✅
- MCQ2: An employee misusing legitimate access is an…? → insider threat ✅
- Discussion: "Which attacker type do you think is the biggest real risk to a Nepali bank — and why?"

**Real-life application:** knowing *who* attacks and *why* lets you (and your future employer) spend defense budget where the real threats are, instead of on fear.

**Summary:** (1) hats = intent + authorization, not skill; (2) attackers range from script kiddies to state actors and insiders; (3) motive shapes defense. **Next unit:** turning all of this into *personal* cybersecurity — your own devices, accounts, and passwords.

**Visual cues:** "hats" spectrum (white → grey → black) with intent labels; attacker-type table (type → motive → typical target → key defense).

---

## 📋 Unit 5 — End-of-Unit Quiz (added per your preference)

**Section A — MCQ (10):** define cyberspace; the three CIA goals; which goal ransomware/DoS/tampering each violates; attack-surface drivers; ransomware-as-a-service; risk = T × V × I; threat vs vulnerability; phishing red flag; MITM defense; matching attacker hat to motive.
**Section B — Short answer (5):** define cybersecurity (people+process+tech); explain each letter of the CIA triad with a Nepal example; explain why outsourcing keeps accountability with you; state and explain the risk formula; list 3 defenses against phishing.
**Section C — Applied case (2):** (i) for a Nepali bank or campus scenario, identify the asset, threat, vulnerability, and impact, then propose two controls; (ii) given a described incident (e.g., a poisoned/cloned login page reached via the right-looking address), name the likely technique and the user-side defense.
**Section D — Discussion (1):** "For a Nepali government ministry, rank these attacker types by real-world risk — hacktivists, organized crime, state actors, insiders — and justify your top two."
*(Full questions + answer key generated with the material. All content stays defensive/conceptual — no attack execution steps.)*

---

## Open questions before I generate Unit 5 material
1. Keep the Nepal examples above (NIC ASIA SWIFT-style framing, NPCERT/Nepal CERT, government-site defacements, eSewa/Khalti/fonepay phishing, café Wi-Fi)?
2. For ARP/DNS poisoning (S26), keep it strictly conceptual + defenses (current draft), or add a little more technical depth while still avoiding any execution steps?
3. Same as Unit 1: keep 2-MCQ + discussion per session **and** the end-of-unit quiz?
