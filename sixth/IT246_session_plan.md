# IT 246: IT Ethics and Cybersecurity — Session Plan

**Program:** BIM, 6th Semester · **Lecture Hours:** 48
**Session length:** 50 min · **Cadence:** 3 lecture sessions/week **+ 1 practical session/week** → **16 teaching weeks**
*(The weekly practical is a separate 4th session; it does not consume the 48 lecture hours.)*
**Local-example context:** Nepal / South Asia

> Planning document only — no slide content yet. Once we approve this structure, we generate
> full session material one unit at a time (markdown first, then convert to PPT/PDF).

---

## Course objectives (from syllabus)
After completing this course, students will be able to:
- Understand concepts of ethics, and ethics for IT workers and IT organizations.
- Know intellectual property and related concepts and issues.
- Gain knowledge of threats, cybersecurity, and digital forensics.
- Know the provision of cyber law in the context of Nepal.

---

## Lecture-hour budget (sanity check)

| Unit | Title | LHs | Sessions |
|------|-------|-----|----------|
| 1 | An Overview of Ethics | 5 | 5 |
| 2 | Ethics for IT Workers and IT Users | 5 | 5 |
| 3 | Intellectual Property | 6 | 6 |
| 4 | Ethical Decisions in Software Development & Ethics of IT Organizations | 5 | 5 |
| 5 | Fundamentals of Cybersecurity | 6 | 6 |
| 6 | Personal Cybersecurity | 5 | 5 |
| 7 | Social Engineering and Cyber Terrorism | 5 | 5 |
| 8 | Digital Forensics | 7 | 7 |
| 9 | Cyber Law in Context of Nepal | 4 | 4 |
| — | **Total** | **48** | **48** |

48 sessions ÷ 3/week = **16 weeks**.

---

## Week-by-week plan

### Week 1 — Unit 1: An Overview of Ethics (5 LHs)
- **S1** Ethics defined (morals vs ethics vs law); Ethics in the Business World
- **S2** Corporate Social Responsibility (CSR); fostering CSR & good business ethics
- **S3** Improving business ethics (codes, training, audits)

### Week 2 — Unit 1 → Unit 2
- **S4** Ethical considerations in decision making (decision frameworks)
- **S5** Ethics in Information Technology *(closes Unit 1)*
- **S6** *(Unit 2)* Managing the IT worker relationship (employer/client/supplier/society)

### Week 3 — Unit 2: Ethics for IT Workers & Users (5 LHs)
- **S7** Encouraging professionalism of IT workers (codes of ethics, certification, licensing)
- **S8** Encouraging ethical use of IT resources among users
- **S9** Key privacy and anonymity issues

### Week 4 — Unit 2 → Unit 3
- **S10** Social networking ethical issues *(closes Unit 2)*
- **S11** *(Unit 3)* Intellectual property overview; Copyright
- **S12** Patent

### Week 5 — Unit 3: Intellectual Property (6 LHs)
- **S13** Trade secrets
- **S14** Plagiarism; reverse engineering
- **S15** Open-source code; competitive intelligence

### Week 6 — Unit 3 → Unit 4
- **S16** Trademark infringement; cybersquatting *(closes Unit 3)*
- **S17** *(Unit 4)* Software quality and its importance
- **S18** Strategies for developing quality software

### Week 7 — Unit 4: Ethics in SW Development & IT Organizations (5 LHs)
- **S19** Use of contingent workers; outsourcing
- **S20** Whistle-blowing
- **S21** Green computing *(closes Unit 4)* — **midterm checkpoint (Units 1–4)**

### Week 8 — Unit 5: Fundamentals of Cybersecurity (6 LHs)
- **S22** Intro to cyberspace & cybersecurity; cybersecurity perspectives
- **S23** Key development areas: technological changes, economic model shifts, outsourcing
- **S24** Risks cybersecurity mitigates

### Week 9 — Unit 5 (cont.)
- **S25** Common cyberattacks; poisoned web-service attacks
- **S26** Network infrastructure poisoning; technical attack techniques
- **S27** Cyberattackers and their "colored hats" *(closes Unit 5)*

### Week 10 — Unit 6: Personal Cybersecurity (5 LHs)
- **S28** Evaluating your posture: home computer
- **S29** Mobile devices; IoT devices
- **S30** Enhancing physical security

### Week 11 — Unit 6 → Unit 7
- **S31** Cybersecurity when working from home
- **S32** Securing your accounts; passwords *(closes Unit 6)*
- **S33** *(Unit 7)* Intro to social engineering; need & reasons for SE attacks

### Week 12 — Unit 7: Social Engineering & Cyber Terrorism (5 LHs)
- **S34** Understanding implications; building trust; exploiting the relationship
- **S35** Performing SE attacks; countermeasures & prevention
- **S36** Cyber terrorism; types of cyber terrorism

### Week 13 — Unit 7 → Unit 8
- **S37** Effects of cyber terrorism on infrastructure; countering cyber terrorism *(closes Unit 7)*
- **S38** *(Unit 8)* Introduction; computer forensics → digital forensics
- **S39** Stages of digital forensics

### Week 14 — Unit 8: Digital Forensics (7 LHs)
- **S40** Role of digital evidence; methods and lab
- **S41** Collecting, seizing & protecting evidence
- **S42** Recovering data

### Week 15 — Unit 8 close → Unit 9
- **S43** Mobile forensics
- **S44** Legal aspects of digital forensics; cyber forensics in Nepal *(closes Unit 8)*
- **S45** *(Unit 9)* Cyber law in Nepal; legal perspective of cybercrime

### Week 16 — Unit 9 + wrap-up (4 LHs)
- **S46** Electronic Transaction Act (ETA)
- **S47** Electronic Transaction Rules (ETR); IT Policy
- **S48** Information security & policies; **course review + project/lab presentations** *(closes Unit 9)*

---

## Laboratory track — weekly practical (16 sessions, one per week)

> **This is a separate 4th session each week**, on top of the three 50-min lecture sessions — it
> does **not** consume the 48 lecture hours.
>
> **Defensive & educational only.** Every technical lab runs in an **isolated lab environment**
> (host-only VMs, no internet, no real targets), and every offensive demo is paired with its
> countermeasure. The goal is to recognize attacks and build protections — never to attack real
> systems.
>
> **The lab is a self-contained *technical* track — the real cybersecurity lab starts in Week 1.**
> Ethics/IP (Units 1–4) is taught and assessed as **lecture classwork, not lab practicals** — it has
> no hands-on lab component, so we don't fake one. Instead the lab uses Weeks 1–7 to build the
> foundations the security tools actually need (Linux → networking → the isolated lab), then runs the
> cybersecurity/forensics tools in Weeks 8–16. The lab track therefore runs on its own schedule,
> independent of which ethics unit the lectures are on. All cases use a Nepal/South-Asia context.

| Week | Practical (L#) | Tools |
|------|----------------|-------|
| 1 | **L1 — First Linux VM:** install VirtualBox; boot & log in to Kali; open a terminal; take a snapshot | VirtualBox, Kali |
| 2 | **L2 — Linux command line:** navigate the filesystem; create/read/move/delete files; get help (`ls`,`cd`,`cat`,`nano`,`man`) | Kali terminal |
| 3 | **L3 — Users, permissions & packages:** `sudo`, users, file permissions (`chmod`/`chown`), install tools (`apt`), processes | Kali terminal |
| 4 | **L4 — Networking fundamentals I:** IP & MAC addresses, ports, client/server; `ip a`, `ping` between machines | Kali terminal |
| 5 | **L5 — Networking fundamentals II:** TCP/IP, DNS, HTTP; ports↔services; `traceroute`, `curl`, `netstat` | Kali terminal |
| 6 | **L6 — Complete the isolated lab:** add a vulnerable target VM (DVWA/Metasploitable); host-only network; verify VMs ping each other but not the internet; Golden Rules; CIA triad & vuln/threat/attack | VirtualBox, Kali, DVWA |
| 7 | **L7 — Security concepts & first reconnaissance:** attack surface; a ping sweep to find the target; read what's exposed — bridge into scanning | Kali, `ping`/`arp` |
| 8 | **L8 — Reconnaissance & scanning:** host discovery, port/service/version scan on the isolated target; countermeasures (close ports) | Nmap |
| 9 | **L9 — Traffic sniffing:** capture lab traffic; spot plaintext vs encrypted; why HTTPS/encryption matters | Wireshark |
| 10 | **L10 — Web vulnerabilities:** SQL Injection & XSS on DVWA, then fix them (parameterized queries, output encoding) | DVWA / OWASP Juice Shop |
| 11 | **L11 — Passwords & accounts:** password-strength & cracking demo on self-made hashes; MFA + password manager | hashcat/John, password manager |
| 12 | **L12 — Firewall & WFH defense:** configure and test host-firewall rules; secure-accounts & work-from-home checklist | ufw / Windows Firewall |
| 13 | **L13 — Phishing awareness:** SET phishing-page demo in isolation; recognize & prevent; anti-phishing checklist | Social-Engineering Toolkit |
| 14 | **L14 — Forensics I — imaging & recovery:** create a disk image, recover deleted files, document chain of custody — **lab practical** | FTK Imager / Autopsy, foremost |
| 15 | **L15 — Forensics II + incident response:** artifact analysis; mobile-forensics overview; IR tabletop (detect→contain→eradicate→recover) | Autopsy, IR playbook |
| 16 | **L16 — Cyber-law mapping + presentations:** map a real Nepali cybercrime case to the Electronic Transaction Act; investigation capstone & lab demos | ETA text, case pack |

---

## Assessment touchpoints (suggested)

- **Unit quizzes:** end of Units 1, 3, 5, 7 (short MCQ/short-answer checks)
- **Midterm:** Week 7 — covers Units 1–4 (ethics & IP block)
- **Case-study assignment:** an ethics/cyber-incident case analysis (Nepal context) — Weeks 9–12
- **Lab practical:** Week 14 — scanning/vulnerability-ID/incident-response
- **Final:** covers all units; balanced ethics + cybersecurity + cyber law
- **Project/presentation:** Week 16 — a cyber-law or digital-forensics case study, demoed in S48

---

## Learning outcomes by unit (for per-session prompts later)

- **U1** — Explain what ethics is, distinguish it from law/morals, and apply ethical reasoning to business/IT decisions.
- **U2** — Describe professional responsibilities of IT workers and the privacy/anonymity issues facing IT users.
- **U3** — Differentiate copyright, patent, trade secret, and trademark, and identify IP issues (plagiarism, cybersquatting, etc.).
- **U4** — Reason about software-quality ethics, outsourcing/contingent work, whistle-blowing, and green computing.
- **U5** — Explain core cybersecurity concepts, common attacks, and attacker types ("colored hats").
- **U6** — Assess and harden personal cybersecurity posture across devices, accounts, and work-from-home setups.
- **U7** — Explain social-engineering attack stages & countermeasures, and the nature/effects of cyber terrorism.
- **U8** — Describe the digital-forensics process, evidence handling, and its legal aspects (incl. Nepal).
- **U9** — Explain Nepal's cyber-law framework: the Electronic Transaction Act, Rules, and IT Policy.

---

## Suggested readings (from syllabus)

- Reynolds — *Ethics in Information Technology*, 6th ed. (primary — Units 1–4)
- Tavani — *Ethics and Technology*, 5th ed.
- Quinn — *Ethics for the Information Age*, 8th ed.
- Steinberg, Beaver, Coombs & Winkler — *Cybersecurity All-in-One for Dummies*, 1st ed. (Units 5–6)
- Holt, Bossler & Seigfried-Spellar — *Cybercrime and Digital Forensics: An Introduction*, 3rd ed. (Units 7–8)
- Government of Nepal — *Electronic Transaction Act (ETA)*, *Electronic Transaction Rules (ETR)*, *IT Policy* (Unit 9)

---

## Next step

Approve this structure, then I'll generate full session material **one unit at a time** in
markdown (opening hook → content with Nepal/global examples + mini case studies →
check-for-understanding → real-life application → summary), using the per-session template.
We convert approved units to PPT/PDF afterward.
