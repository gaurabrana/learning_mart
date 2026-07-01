# Unit 7 — Social Engineering and Cyber Terrorism · Content Outline

**5 LHs → 5 sessions (S33–S37) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.
**Framing: DEFENSIVE / awareness only — students learn to *recognize* and *prevent* attacks, never to perform them. No operational how-to.**

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 7 learning outcomes (what students can do after S33–S37)
1. Define social engineering and explain why humans are the "weakest link" in security.
2. Recognize the psychological principles (trust, authority, reciprocity, urgency, fear) that attackers exploit — for defense.
3. Identify the major social-engineering attack types (phishing, vishing, smishing, pretexting, baiting, tailgating) and apply countermeasures.
4. Define cyber terrorism, distinguish it from cybercrime/hacktivism, and classify its types.
5. Explain cyber terrorism's effects on critical infrastructure and describe how it is countered at personal, organizational, and national levels.

---

## S33 — Introduction to Social Engineering · Need for & Reasons behind Attacks

**Hook:** "You can buy a Rs. 50,000 firewall, but if a polite caller says *'Namaste, I'm calling from your bank's head office'* and you read out your OTP — the firewall never even gets a vote. Why do humans break before machines do?" → people are the easiest system to hack.

**Concepts & how each will be filled:**

1. **What is social engineering**
   - Definition: manipulating people into giving up confidential information or access, instead of breaking technology directly.
   - Theory: it targets *human psychology* (trust, helpfulness, fear), not code; attacker "hacks the person, not the PC."
   - Global example: attackers impersonating IT helpdesk to reset employee passwords (the classic helpdesk-call scenario, described for awareness).
   - Local example: a fake "NTC/Ncell" SMS saying your SIM will be blocked unless you "verify" details on a link.
   - Misconception: *"Social engineering is a technical hacking skill."* Correction: it's mostly persuasion + deception; the tech is secondary.

2. **Need for social engineering (why attackers use it)**
   - Definition: it's the path of least resistance — cheaper and faster than defeating strong technical controls.
   - Theory: strong encryption/firewalls make direct attacks costly, so attackers pivot to the human; high success rate, low cost, hard to trace.
   - Local example: instead of cracking a bank's systems, scammers simply phone customers pretending to be "bank security" — far easier than breaching the bank.

3. **Reasons humans are the weakest link**
   - Helpfulness, obedience to authority, fear of consequences, curiosity, trust in familiar brands, low awareness.
   - Mini case: an office peon receives a call: *"Sir from the IT department here — your email will be deleted today, just confirm your password."* Why does it work on a busy, polite employee?
   - Fun analogy: the strongest castle wall is useless if the gatekeeper opens the gate to anyone wearing the right uniform.

**Check for understanding:**
- MCQ1: Social engineering primarily attacks…? → human psychology/people ✅ (not firewalls / not encryption / not hardware)
- MCQ2: Attackers prefer social engineering mainly because it is…? → low-cost and high-success vs. beating strong tech controls ✅
- Discussion: "Recall one suspicious call or SMS you (or your family) received in Nepali — what trick was it using?"

**Real-life application:** the most common way money is stolen from ordinary Nepalis online is not "hacking" — it's a convincing phone call or message; recognizing this is your first defense.

**Summary:** (1) social engineering = hacking people, not machines; (2) it's the cheapest attack path; (3) humans are exploitable through trust/fear/helpfulness. **Next:** the exact psychological levers attackers pull.

**Visual cues:** "human vs firewall" split image (sturdy wall, open gate); cost-vs-success quadrant placing social engineering in "cheap + effective."

---

## S34 — Understanding the Implications · Building Trust · Exploiting the Relationship

**Hook:** "Why does a scammer spend 10 minutes being *friendly* before asking for anything? Because the ask only works after the trust. Today we reverse-engineer the manipulation — so you see it coming." → the psychology of the con (for defense).

**Concepts & how each will be filled:**

1. **Understanding the implications (what's really at stake)**
   - Definition: a single successful manipulation can cascade into data loss, financial theft, identity theft, and reputational damage.
   - Theory: one leaked OTP/password can unlock email → bank → social accounts (chain reaction); impact is rarely "just one account."
   - Local example: a victim who shared an OTP loses eSewa/Khalti wallet balance *and* the attacker then messages their contacts for more money.
   - Misconception: *"It's just one password, no big deal."* Correction: credentials are keys to a whole chain of accounts.

2. **Building trust (the levers — explained to recognize, not to use)**
   - Definition: attackers manufacture trust using familiar names, authority, and social proof.
   - Theory (Cialdini-style principles, awareness framing): authority ("I'm from the bank/police"), liking/rapport, social proof ("everyone has updated their KYC"), reciprocity ("I helped you, now help me").
   - Global example: spoofed sender names/logos that look like a real institution.
   - Local example: a caller using a real-sounding Nepali bank name, branch, and your actual name (scraped from a leaked list) to sound legitimate.

3. **Exploiting the relationship (urgency, fear, the close)**
   - Definition: once trust exists, attackers add pressure so the victim acts before thinking.
   - Theory: urgency ("account blocks in 10 minutes"), fear ("police case filed"), scarcity ("lottery claim expires today").
   - Mini case: a "Facebook lottery" message — *"You've won Rs. 25 lakh, pay Rs. 5,000 processing fee to release it."* Identify every trust + urgency lever used.
   - Fun analogy: a magician's patter — the friendly chatter is the misdirection; the "trick" is the request that follows.

**Check for understanding:**
- MCQ1: An attacker saying "I'm calling from the police, act now or face arrest" is combining…? → authority + fear/urgency ✅
- MCQ2: Why is leaking one OTP serious? → it can unlock a chain of linked accounts ✅
- Discussion: "In a scam call your aunt got, which trust-building tactic was used — authority, liking, or social proof?"

**Real-life application:** spotting the *emotion* a message is trying to trigger (fear, greed, urgency) is the single fastest way to catch a scam before reacting.

**Summary:** (1) impact chains far beyond one account; (2) attackers manufacture trust via authority/liking/social proof; (3) they exploit it with urgency and fear. **Next:** the named attack types and how to defend against each.

**Visual cues:** "trust ladder" graphic (rapport → authority → urgency → the ask); annotated screenshot of a fake lottery/KYC message with each lever labeled.

---

## S35 — Performing Social Engineering Attacks (types & recognition) · Countermeasures & Prevention

**Hook:** "Phishing, vishing, smishing, pretexting, baiting, tailgating — six names, one goal: make *you* the door. Today you learn to recognize all six in the wild, and how to shut the door." → a field guide to spotting attacks. *(Recognition only — no instructions to carry them out.)*

**Concepts & how each will be filled:**

1. **The major attack types (described for recognition)**
   - **Phishing (email):** fake emails/links posing as a bank, college, or service to steal logins. Recognition: mismatched URLs, generic greetings, urgent threats, attachments.
   - **Vishing (voice call):** fake bank/telecom/"police" calls. Recognition: pressure to share OTP/PIN, caller "verifying" sensitive data they should already have.
   - **Smishing (SMS):** fake texts with links (KYC update, parcel delivery, lottery). Local example: "Your eSewa/bank account is suspended, click here."
   - **Pretexting:** an invented backstory ("I'm the new auditor / your boss's assistant") to extract info.
   - **Baiting:** dangling something tempting — a "free" download, or a USB drive left in a parking lot/canteen.
   - **Tailgating/piggybacking:** following an authorized person through a secure door (physical social engineering).
   - Global example: package-delivery smishing waves; CEO-impersonation ("business email compromise") asking finance to wire money.
   - Local example: fake "Nepal lottery / Daraz prize" SMS; a "bank officer" vishing call asking for the OTP just sent to you.
   - Misconception: *"Phishing only happens over email."* Correction: it spans SMS (smishing), calls (vishing), QR codes, and social media.

2. **Social engineering countermeasures (organizational + technical)**
   - Definition: layered defenses combining people, process, and technology.
   - Theory: security-awareness training, simulated-phishing drills, verify-via-callback policy, least-privilege access, MFA, email filtering/anti-spoofing (SPF/DKIM/DMARC named at awareness level), visitor badges & escort policy against tailgating.
   - Local example: a Nepali bank running staff awareness sessions and a rule "we will *never* ask for your OTP/PIN."

3. **Preventing attacks (personal habits)**
   - Never share OTP/PIN/password; verify by calling the official number yourself; hover/check links; slow down when rushed; report suspicious messages.
   - Mini case: you get an SMS "parcel held at customs, pay Rs. 200 here." Walk through the safe response (don't click → verify with the courier directly).
   - Fun analogy: "STOP, THINK, then CLICK" — like looking both ways before crossing a road; the pause is the protection.

**Check for understanding:**
- MCQ1: A fraudulent *phone call* asking for your OTP is an example of…? → vishing ✅
- MCQ2: The single best rule against OTP fraud is…? → never share your OTP with anyone, even "the bank" ✅
- Discussion: "Which of the six types do you think is most common in Nepal right now, and why?"

**Real-life application:** banks and wallets (eSewa, Khalti, NIC ASIA, etc.) repeatedly warn customers they will never ask for an OTP — knowing the attack names lets you instantly classify and reject the scam.

**Summary:** (1) six recognizable attack types across channels; (2) countermeasures = training + process + tech; (3) personal rule: verify, never share OTP, slow down. **Next:** when manipulation scales up to attacks on a whole nation — cyber terrorism.

**Visual cues:** six-icon "attack types" cheat sheet (email/call/SMS/pretext/bait/door); a "spot the phish" annotated fake-SMS; "STOP–THINK–CLICK" poster.

---

## S36 — Cyber Terrorism · Types of Cyber Terrorism

**Hook:** "A teenager defacing a website for fun, an activist protesting online, and a group trying to shut down a country's power grid — all use computers, but only one is *cyber terrorism*. Where's the line?" → defining the term precisely.

**Concepts & how each will be filled:**

1. **What is cyber terrorism**
   - Definition: politically or ideologically motivated use of computers/networks to cause serious harm, fear, or disruption — especially to critical systems or the public.
   - Theory: the key ingredients are *intent* (political/ideological), *target* (often critical infrastructure or public fear), and *severity* (real-world harm or terror).
   - Global example: attacks aimed at power grids and industrial control systems intended to cause physical disruption.
   - Local example (awareness): defacement of Nepali government websites and attacks on public-service portals during regional tensions, used to spread fear/embarrassment.
   - Misconception: *"Any hacking is cyber terrorism."* Correction: most hacking is crime or vandalism; terrorism requires political/ideological intent + intent to terrorize or seriously harm.

2. **Distinguishing related terms**
   - Definition: cybercrime (profit), hacktivism (protest/message), cyber warfare (state-vs-state), cyber terrorism (terror/ideology) — overlapping but distinct.
   - Mini case: classify three events — a ransomware gang for money, a protest-driven website defacement, and an attempt to disable a national grid — into the right bucket.

3. **Types of cyber terrorism**
   - Definition: common categories used for awareness — (a) attacks on critical infrastructure (power, water, telecom, finance, aviation), (b) data destruction/manipulation of public records, (c) disruption/denial of essential services (large-scale DoS), (d) propaganda, recruitment & psychological operations / disinformation online, (e) financing via cyber means.
   - Local example: disinformation campaigns on social media during sensitive national events; threats to telecom/banking continuity in South Asia.
   - Fun analogy: cyber terrorism is "arson with a keyboard" — the goal isn't theft, it's fear and damage.

**Check for understanding:**
- MCQ1: What most distinguishes cyber terrorism from ordinary cybercrime? → political/ideological intent to cause fear or serious harm ✅ (not "uses a computer" / not "is illegal")
- MCQ2: Spreading propaganda and disinformation to recruit and instill fear is which type? → psychological operations / propaganda ✅
- Discussion: "Is a website defacement of a government portal cybercrime, hacktivism, or cyber terrorism? Defend your classification."

**Real-life application:** as future IT/business professionals, you'll need to correctly label incidents — mislabeling a vandalism case as "terrorism" (or vice versa) changes the legal and response path entirely.

**Summary:** (1) cyber terrorism = ideological intent + harm/fear, often vs. infrastructure; (2) it's distinct from crime/hacktivism/warfare; (3) types span infrastructure attacks, service denial, data destruction, and propaganda. **Next:** what it does to real infrastructure and how nations counter it.

**Visual cues:** 2x2 "intent vs. target" map placing crime/hacktivism/warfare/terrorism; icon row of cyber-terror types (grid/water/telecom/records/propaganda).

---

## S37 — Effects on Infrastructure · Countering Cyber Terrorism (closes Unit 7)

**Hook:** "Imagine Kathmandu's power, the banking network, and mobile service all going dark for two days — no ATMs, no eSewa, no calls. Cyber terrorism's real damage isn't on a screen; it's in the streets." → why critical infrastructure is the prize, and how we defend it.

**Concepts & how each will be filled:**

1. **Effects of cyber terrorism on infrastructure**
   - Definition: disruption of critical infrastructure (CI) — the systems a society can't function without.
   - Theory: cascading/domino effects — power outage → telecom down → banking/hospitals/water affected → public panic and economic loss.
   - Global example: prolonged outages from attacks on energy/utility control systems causing regional blackouts.
   - Local example: dependence on a few telecom operators and on digital wallets (eSewa/Khalti/connectIPS) means an attack on national payment or telecom infrastructure could freeze daily commerce; attacks on government data centers risk citizen records.
   - Misconception: *"Cyber attacks only cause online/digital damage."* Correction: attacks on industrial/control systems can cause physical, economic, and human harm.

2. **Countering cyber terrorism (layered defense)**
   - Definition: coordinated defense across personal, organizational, and national levels.
   - Theory:
     - **National:** CERT/national incident-response teams, critical-infrastructure protection policies, intelligence sharing, international cooperation, legal frameworks.
     - **Organizational:** network segmentation, monitoring/intrusion detection, incident-response & business-continuity/disaster-recovery plans, regular drills, backups.
     - **Personal/citizen:** awareness, reporting suspicious activity, not amplifying disinformation/panic.
   - Local example: Nepal's CERT (NPCERT) and government IT-security efforts; the role of cyber-law (Electronic Transaction Act — ties forward to Unit 9) in prosecution; coordination among NRB, telecoms, and agencies.

3. **Resilience & preparedness**
   - Definition: assuming attacks will happen and building the ability to keep operating and recover fast.
   - Mini case: a national bank suffers a service-disrupting attack — what continuity steps (backups, failover, public communication, coordination with CERT) limit the damage?
   - Fun analogy: like earthquake preparedness in Nepal — you can't stop every quake, but drills, building codes, and a recovery plan decide whether it's a scare or a catastrophe.

**Check for understanding:**
- MCQ1: The most dangerous feature of an infrastructure attack is…? → cascading effects across dependent systems ✅
- MCQ2: A national team that coordinates response to major cyber incidents is a…? → CERT (Computer Emergency Response Team) ✅
- Discussion: "Which piece of Nepal's critical infrastructure worries you most if attacked, and what one defense would you prioritize?"

**Real-life application:** organizations now expect employees to follow incident-response and business-continuity plans; understanding infrastructure resilience makes you valuable in any IT/management role and a responsible digital citizen.

**Summary:** (1) infrastructure attacks cause cascading, real-world harm; (2) countering needs national + organizational + personal layers; (3) resilience and preparedness beat hoping it won't happen. **Next unit:** Digital Forensics — how incidents are investigated after the fact.

**Visual cues:** "cascade/domino" diagram (power → telecom → banking → hospitals); three-layer defense pyramid (national / organizational / personal); Nepal CI map (telecom, payments, government data, energy).

---

## 📋 Unit 7 — End-of-Unit Quiz (added per your preference)

**Section A — MCQ (10):** definition of social engineering; why humans are the weakest link; why attackers prefer it (cost/success); trust-building principles (authority/liking/social proof); urgency & fear tactics; match attack type to channel (phishing/vishing/smishing/pretexting/baiting/tailgating); best rule against OTP fraud; what distinguishes cyber terrorism from cybercrime; a type of cyber terrorism; what a CERT does.
**Section B — Short answer (5):** define social engineering; list 4 reasons humans are exploited; name & explain 3 social-engineering attack types; list 4 countermeasures (personal + organizational); define cyber terrorism and give two of its types.
**Section C — Applied case (2):** (i) given a Nepali scam SMS/call transcript, identify the attack type, the psychological levers used, and the correct safe response; (ii) given a national-infrastructure attack scenario, describe the cascading effects and three countering measures across the national/organizational/personal layers.
**Section D — Discussion (1):** "Is a politically motivated defacement of a Nepali government website 'cyber terrorism'? Argue both sides using intent, target, and severity."
*(Full questions + answer key generated with the material. All attack content stays at recognition/defense level — no operational steps.)*

---

## Open questions before I generate Unit 7 material
1. Keep the Nepali examples above (NTC/Ncell SIM-block SMS, fake bank OTP calls, Facebook/Daraz lottery, eSewa/Khalti wallet theft, NPCERT, government-website defacement)?
2. For S34's psychology, keep it applied/awareness-only (current), or add a little more theory depth on the persuasion principles?
3. Confirm the defensive framing depth for S35 is right — recognition + countermeasures only, with zero step-by-step attack instructions?
4. Same as before: keep 2-MCQ + discussion per session **and** the end-of-unit quiz?
