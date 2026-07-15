# IT 246 — Laboratory Work Record & Viva Question Set (Instructor Copy)
### IT Ethics & Cybersecurity · BIM 6th Semester · Hands-on cybersecurity lab (isolated VMs)

This is the **instructor/examiner** companion to the student docs. It lists every lab work, its tasks
and expected output, what the student must record, and the **viva questions with model answers**. It
maps 1:1 to the 16 weekly practicals in [IT246_session_plan.md](../IT246_session_plan.md) and to the
step-by-step [IT246_Lab_Manual.md](IT246_Lab_Manual.md).

- **The lab is a purely technical track.** Ethics/IP (Units 1–4) is taught and assessed as **lecture
  classwork, not lab practicals** — it has no hands-on component, so no "ethics lab" is faked. The lab
  uses Weeks 1–7 to build the foundations the tools need (**Linux → networking → the isolated lab**),
  then runs the tools in Weeks 8–16. Ethics/law is examined in the report only where it connects to the
  technical work (legality of scanning; the Lab 16 cyber-law capstone).
- **Environment:** VirtualBox with **Kali (attacker)** + a **vulnerable target** on a **host-only,
  no-internet** network. Beginner-safe; nothing can reach real systems.
- **Audience:** treat every student as a **complete beginner** who has never used a terminal. Assess
  understanding and, above all, **responsible/defensive practice** — not attacking skill.

---

## ⚠️ Safety & legality framing (enforce in every technical session)

> All offensive tools are used **only** inside the isolated lab against provided targets. Using them on
> real systems violates Nepal's **Electronic Transaction Act 2063**. Every attack demo **must** be
> paired with its countermeasure. A student who runs a tool but cannot state the defence has **not**
> passed that lab. Make students verify the **host-only** network (Lab 6) at the start of each tool lab.

---

## How the lab record is kept and assessed

**Each lab-work entry in the student's report must contain:**
1. **Lab number & title**, date, student name/roll.
2. **Objective** (1–2 lines, student's own words).
3. **What they did** — command or configuration (just what's new).
4. **A screenshot of the result** on their machine (from the isolated lab).
5. **The countermeasure/defence** for any attack, and **answers to that lab's viva questions.**

**Assessment (printed lab report + viva — adjust to your college's scheme):**
| Part | Weight | What it checks |
|---|---|---|
| Printed lab report (all 16 questions: work + screenshot + defence + explanation) | 50% | Every lab documented, each attack paired with its countermeasure |
| Viva voce (external + internal) on the report | 40% | Student can **explain their own work and its defence** — anti-copying check |
| Regularity / attendance / sign-offs | 10% | Work done across the semester |

> **Zero-tolerance rule (state it up front):** any evidence a student ran a tool against a **real /
> non-lab** system fails the lab **and** is a disciplinary/legal matter. The lab is defensive and
> isolated by design.

---

## List of Lab Works (16) → weekly sessions

| Lab | Title | Week | Links to |
|-----|-------|------|----------|
| 1 | First Linux VM (VirtualBox + Kali) | 1 | foundation for U5–U8 |
| 2 | Linux command line | 2 | foundation |
| 3 | Users, permissions & packages | 3 | access control (CIA) |
| 4 | Networking fundamentals I (IP, ports) | 4 | foundation |
| 5 | Networking fundamentals II (TCP/DNS/HTTP) | 5 | foundation |
| 6 | Complete the isolated lab (host-only; CIA; vuln/threat/attack) | 6 | U5 |
| 7 | Security concepts & first reconnaissance | 7 | U5 |
| 8 | Reconnaissance & scanning (Nmap) | 8 | U5 |
| 9 | Traffic sniffing (Wireshark) | 9 | U5 |
| 10 | Web vulnerabilities: SQLi & XSS + fixes (DVWA) | 10 | U5 |
| 11 | Passwords: hashing & cracking demo | 11 | U6 |
| 12 | Firewall config & WFH defence | 12 | U6 |
| 13 | Phishing awareness (SET, lab-only) | 13 | U7 |
| 14 | Forensics I: imaging & recovery (**practical**) | 14 | U8 |
| 15 | Forensics II & incident response | 15 | U8 |
| 16 | Cyber-law capstone + presentation | 16 | U9 |

---

# Part 1 — Foundations: Linux, Networking & the Isolated Lab

## Lab Work 1 — First Linux VM
**Objective:** Get a safe Linux environment running.
**Tasks:** Install VirtualBox; import & boot Kali; log in; open a terminal; `whoami`/`uname -a`;
snapshot "clean".
**Expected output:** Kali running, terminal open.
**Record:** desktop + terminal screenshot.
**Viva (model answers):**
- *What is a virtual machine?* → A whole computer running in software inside your host OS.
- *Why use a VM here?* → To experiment with security tools safely, isolated from your real machine.
- *What does a snapshot do?* → Saves the VM's state so you can roll back after a lab.

## Lab Work 2 — Linux command line
**Objective:** Be comfortable in the terminal.
**Tasks:** navigate (`pwd`/`ls`/`cd`); create/read/copy/move/delete files; `man`.
**Expected output:** confident file/folder handling.
**Record:** terminal screenshot (mkdir/nano/cat).
**Viva:**
- *What do `pwd`, `ls`, `cd` do?* → Show current directory, list contents, change directory.
- *Why is the command line important in security?* → Almost all tools are CLI-driven and scriptable.
- *How do you get help on a command?* → `man <cmd>` or `<cmd> --help`.

## Lab Work 3 — Users, permissions & packages
**Objective:** Understand access control; install tools.
**Tasks:** `id`/`sudo`; read and change permissions (`chmod`/`chown`); `apt install`; view processes.
**Expected output:** a permission change; a tool installed.
**Record:** `ls -l` before/after + `apt install` screenshot.
**Viva:**
- *What do the rwx permission bits mean?* → Read/write/execute for owner, group, others.
- *How do permissions relate to security?* → They are access control — the **C** (confidentiality) in
  the CIA triad.
- *What does `sudo` do?* → Runs a command with administrator (root) privileges.

## Lab Work 4 — Networking fundamentals I
**Objective:** IP addresses, ports, client/server.
**Tasks:** `ip a`; identify private IP & MAC; explain ports; `ping` localhost/own IP.
**Expected output:** VM's IP; successful pings.
**Record:** `ip a` + ping screenshot.
**Viva:**
- *IP address vs port?* → IP identifies the machine; port identifies the service on it.
- *Give three well-known ports.* → 80 HTTP, 443 HTTPS, 22 SSH (also 3306 MySQL).
- *What is the client/server model?* → A client requests; a server responds.

## Lab Work 5 — Networking fundamentals II
**Objective:** TCP/IP, DNS, HTTP; see a client/server exchange.
**Tasks:** `ss -tuln`; run `python3 -m http.server`; fetch with `curl -v`.
**Expected output:** a listening server + a successful fetch with logs.
**Record:** two-terminal (server + client) screenshot.
**Viva:**
- *What is DNS?* → It resolves names (google.com) to IP addresses.
- *TCP vs UDP?* → TCP is reliable/ordered (handshake); UDP is fast, best-effort.
- *What is HTTP?* → The request/response protocol of the web.

## Lab Work 6 — Complete the isolated lab
**Objective:** Build attacker+target on a safe network; learn core vocabulary.
**Tasks:** import target; set **both** to Host-only; ping between VMs (works) and to internet (fails);
snapshot; define CIA & vuln/threat/attack.
**Expected output:** isolation proven (internal ping OK, internet ping FAIL).
**Record:** network setting + both ping results.
**Viva:**
- *Why host-only networking?* → Isolates the VMs so tools can't reach real systems — legal & safe.
- *Name the CIA triad.* → Confidentiality, Integrity, Availability.
- *Vulnerability vs threat vs attack?* → Weakness / something that could exploit it / the exploitation
  actually happening.

## Lab Work 7 — Security concepts & first reconnaissance
**Objective:** First recon; attack-surface idea.
**Tasks:** confirm network; `arp-scan`/ping sweep to find target; `nc` to a port; define attack
surface.
**Expected output:** target discovered.
**Record:** scan screenshot.
**Viva:**
- *What is reconnaissance?* → Mapping what a target exposes before attacking.
- *What is an attack surface?* → All the points (ports/services/pages/logins) an attacker could use.
- *How do defenders reduce it?* → Disable unused services, firewall, patch.

---

# Part 2 — Cybersecurity Tools: Attack & Defence

## Lab Work 8 — Scanning (Nmap)
**Objective:** Reconnaissance + defence.
**Tasks:** host discovery; port scan; version scan of the target; state countermeasures.
**Expected output:** open-port list.
**Record:** Nmap output.
**Viva:**
- *What does Nmap reveal?* → Live hosts, open ports, services, and versions.
- *Three defences?* → Close unused ports/services, firewall, patch software.
- *Why does a version scan help an attacker?* → It reveals known-vulnerable software versions.

## Lab Work 9 — Sniffing (Wireshark)
**Objective:** Why encryption matters.
**Tasks:** capture HTTP (readable) vs TLS (unreadable); state the fix.
**Expected output:** contrasting captures.
**Record:** HTTP + TLS packet screenshots.
**Viva:**
- *What can a sniffer see on HTTP?* → Everything in plain text, including credentials.
- *How does HTTPS/TLS help?* → It encrypts traffic so the sniffer sees only ciphertext.
- *When is sniffing legal?* → Only on networks/traffic you own or are authorized to monitor.

## Lab Work 10 — Web vulnerabilities (SQLi & XSS)
**Objective:** See the attacks and the exact fixes.
**Tasks:** SQLi and XSS on DVWA Low; show both fail at High; name the fix for each.
**Expected output:** attack works at Low, blocked at High.
**Record:** SQLi, XSS, and fixed screenshots.
**Viva:**
- *What is SQL injection and its fix?* → Injecting SQL via input; fixed by **prepared/parameterized
  statements** that treat input as data.
- *What is XSS and its fix?* → Injecting script that runs in the browser; fixed by **escaping/encoding
  output** (+ CSP).
- *Common root cause of both?* → Trusting/using unvalidated user input directly.

## Lab Work 11 — Passwords
**Objective:** Weak vs strong passwords; defences.
**Tasks:** crack a weak self-made hash, fail on a strong one; list defences.
**Expected output:** weak cracked, strong not.
**Record:** cracking result.
**Viva:**
- *Why do weak passwords fall instantly?* → They're in wordlists (rockyou); tools try millions/sec.
- *Best defences?* → Length + randomness, a password manager, and **MFA**.
- *How should servers store passwords?* → Salted slow hashes (bcrypt/argon2), never plain or MD5.

## Lab Work 12 — Firewall & WFH
**Objective:** Control traffic; harden home setup.
**Tasks:** ufw default-deny + rules; verify fewer ports via Nmap; WFH checklist.
**Expected output:** firewall reduces open ports.
**Record:** ufw status + before/after scan.
**Viva:**
- *What does a firewall do?* → Allows/blocks traffic by rules.
- *Why "default deny"?* → Block everything, then allow only what's needed — smallest attack surface.
- *Two WFH security measures?* → Updated OS + firewall; VPN + strong Wi-Fi (WPA3); separate devices.

## Lab Work 13 — Phishing awareness
**Objective:** Recognize & prevent phishing.
**Tasks:** observe a lab-only cloned page; build an anti-phishing checklist.
**Expected output:** checklist + lab-only demo.
**Record:** lab-only page + checklist.
**Viva:**
- *Why is phishing "social engineering"?* → It manipulates people, not software.
- *Three red flags?* → Wrong/misspelled URL, urgency, unexpected link asking for credentials.
- *Best technical defence if a password is phished?* → MFA (the stolen password alone won't work).
- *(Ethics/law check)* *Why can't you send your cloned page to anyone?* → It's unauthorized —
  illegal under ETA 2063 and unethical; the lab is only to learn recognition.

---

# Part 3 — Forensics, IR & Cyber Law

## Lab Work 14 — Forensics I: imaging & recovery (**practical week**)
**Objective:** Handle evidence correctly.
**Tasks:** image a source; verify with matching hashes; recover a deleted file; chain of custody.
**Expected output:** matching hashes + recovered file.
**Record:** hash match + recovered file + custody table.
**Viva:**
- *Why work on a copy, not the original?* → To preserve the original evidence unaltered.
- *What does a matching hash prove?* → The copy is bit-for-bit identical and untampered.
- *What is chain of custody?* → A documented record of who handled the evidence, when — for
  admissibility.

## Lab Work 15 — Forensics II & incident response
**Objective:** Analyse artefacts; respond to an incident.
**Tasks:** Autopsy analysis; mobile-forensics note; IR tabletop (6 phases).
**Expected output:** artefacts found + IR plan.
**Record:** Autopsy screenshot + IR plan.
**Viva:**
- *Name the incident-response phases.* → Preparation, identification, containment, eradication,
  recovery, lessons learned.
- *First action on a ransomware infection?* → Contain — isolate the machine from the network.
- *How does mobile forensics differ?* → Data in apps/cloud, special tools, isolate device to prevent
  remote wipe.

## Lab Work 16 — Cyber-law capstone + presentation
**Objective:** Connect practice to Nepal's law.
**Tasks:** map a case to an ETA 2063 provision; note evidence + prevention; present portfolio.
**Expected output:** case-to-law mapping + presentation.
**Record:** the mapping + portfolio.
**Viva:**
- *What does the Electronic Transaction Act 2063 criminalize?* → Unauthorized access, data theft,
  damaging systems, cyber-fraud (with penalties).
- *Why need both ethics and law?* → Ethics guides behaviour beforehand; law imposes consequences
  afterward.
- *Trace one case: offence → law → evidence → prevention.* → (Student explains their own mapping.)

---

## External Viva & Practical Exam — guidance

**How the external viva typically runs (adapt to your college):**
1. **Report check** — the examiner reads the printed A4 report and confirms all 16 questions have
   work + screenshot + **countermeasure** + explanation, signed off by the internal instructor.
2. **Viva Q&A** — the examiner asks the student to **explain their own work and its defence**, plus the
   per-lab and cross-cutting questions below. This exposes a copied report.

**Evidence checklist the report should contain:**
- ☐ A working **Kali VM** and confidence in the **Linux terminal** (Labs 1–3)
- ☐ **Networking** understanding: IP/ports, a client/server exchange (Labs 4–5)
- ☐ An **isolated (host-only) lab** with Kali + a target VM, **isolation proven** (Lab 6)
- ☐ Reconnaissance + Nmap scan (+ defences); Wireshark HTTP-vs-TLS
- ☐ SQLi & XSS demonstrated **and fixed**; password cracking (self-made hashes) + MFA/defences
- ☐ Firewall reducing open ports; anti-phishing checklist (lab-only demo)
- ☐ Forensic imaging with matching hashes + recovery; an incident-response plan
- ☐ A cybercrime case mapped to the ETA 2063

**Cross-cutting viva questions (whole course):**
- *For any attack in your report, state the defence.* (the core competency)
- *Why is everything you did legal?* → Isolated lab, provided targets, no real systems (ETA 2063).
- *Explain the difference between a vulnerability, a threat, and an attack.*
- *Walk through how you'd both cause and prevent a SQL injection.*
- *How does a host-only network keep the lab safe?*

**Suggested viva marking (out of the viva weight):** explanation of their **own** work (30%),
**countermeasures/defensive understanding** (30%), Linux/networking foundations (20%), forensics/law
understanding (20%).

---

> **Companion documents:** the student-facing [Lab Questions](IT246_Lab_Questions.md), the beginner
> step-by-step [Lab Manual](IT246_Lab_Manual.md), and the [Lab Report Format](IT246_Lab_Report_Format.md).
> Lab numbers here map to the 16 weekly practicals in the session plan.
