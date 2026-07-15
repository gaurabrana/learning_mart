# IT 246 — Lab Report Format (printed A4)
### IT Ethics & Cybersecurity · How to prepare and print your lab report

Your lab report is the document you submit and are examined on. It must, on its own, prove that you did
the **isolated-lab** cybersecurity work — from the Linux/networking foundations to the attacks — and,
for every attack, that you know the **defence**. *(Ethics/IP is examined via lecture classwork, not
here; the only ethics/law content in this report is where it connects to the technical work — the
legality of scanning, and the Lab 16 cyber-law capstone.)* Follow this exact structure so every report
is consistent and easy for the examiner to mark.

Answer the 16 questions in **[IT246_Lab_Questions.md](IT246_Lab_Questions.md)**. Each answer =
**what you did + screenshot + explanation (+ countermeasure for any attack)**.

> **Legal statement (put it in your Introduction):** *"All technical work in this report was performed
> only inside an isolated lab (host-only virtual machines) against provided vulnerable targets, for
> defensive and educational purposes, in compliance with Nepal's Electronic Transaction Act 2063."*

---

## Order of pages

1. **Cover page**
2. **Certificate / sign-off page**
3. **Index (table of contents)**
4. **Introduction** (½ page — include the legal statement above)
5. **Answers to Q1–Q16** (the main body)
6. **Conclusion** (½ page)

---

### 1. Cover page
Centered, one page:
- College / campus name and logo
- **IT 246: IT Ethics and Cybersecurity — Lab Report**
- Student name, roll number, section/group
- Submitted to: (instructor name), Department of …
- Date

### 2. Certificate / sign-off page
A short certificate plus a sign-off table (the examiner looks for the instructor's signatures):

> *This is to certify that **[name]**, roll no. **[…]**, has completed the laboratory work of the
> course **IT 246: IT Ethics and Cybersecurity** during the academic year …, as recorded in this
> report.*
>
> Internal Examiner: ______________  External Examiner: ______________  Date: __________

| # | Lab work | Date completed | Instructor signature |
|---|----------|----------------|----------------------|
| 1 | First Linux VM (VirtualBox + Kali) | | |
| 2 | Linux command line | | |
| 3 | Users, permissions & packages | | |
| 4 | Networking fundamentals I (IP, ports) | | |
| 5 | Networking fundamentals II (TCP/DNS/HTTP) | | |
| 6 | Complete the isolated lab | | |
| 7 | Security concepts & first reconnaissance | | |
| 8 | Scanning (Nmap) | | |
| 9 | Sniffing (Wireshark) | | |
| 10 | Web vulnerabilities (SQLi & XSS) | | |
| 11 | Passwords | | |
| 12 | Firewall & WFH | | |
| 13 | Phishing awareness | | |
| 14 | Forensics I: imaging & recovery | | |
| 15 | Forensics II & incident response | | |
| 16 | Cyber-law capstone | | |

### 3. Index
A table: **Question no. · Title · Page no.** — so the examiner can jump to any answer.

### 4. Introduction (½ page)
- What the lab covered (Linux & networking foundations → an isolated cybersecurity/forensics lab).
- The **legal statement** (above) — this is required.
- The tools used: VirtualBox, Kali (Linux terminal), DVWA/Metasploitable, Nmap, Wireshark,
  John/hashcat, ufw, SET, Autopsy.

### 5. Answers (main body)
Repeat this block for **each** question, Q1 → Q16:

> **Q[n]. [paste the question text]**
>
> **What I did:** the analysis / command / configuration (paste commands in a monospace box).
>
> **Output:** *(a labelled screenshot — Fig n, from your isolated lab)*
>
> **Explanation & countermeasure:** 1–2 lines on what happened, **and the defence** for any attack.

### 6. Conclusion (½ page)
What you learned building from Linux/networking foundations through cybersecurity, forensics, and cyber
law; and why isolated, authorized, defensive practice matters.

---

## Formatting rules (keep it consistent)
- **Paper:** A4, portrait. Margins ~1 inch. Page numbers in the footer.
- **Body text:** a clean serif/sans font, size 11–12.
- **Commands / code:** a **monospace** font (Consolas / Courier New), in a bordered or shaded box.
  Paste only the relevant commands.
- **Screenshots:** cropped and legible, labelled *Fig 1, Fig 2, …*, and clearly from your **isolated
  lab** (host-only IPs like `192.168.56.x` are good proof). A blurry or full-desktop shot loses marks.
- **Every attack answer must include its countermeasure** — an attack shown without a defence is
  incomplete and loses marks.
- **Your own work:** what's in the report must match what you can explain in the viva.

## What makes a screenshot count as proof
- **Foundations (Q1–Q5):** Kali running with a terminal; file/permission commands; `ip a`; a
  client/server exchange (`http.server` + `curl`).
- **Isolated lab (Q6):** VirtualBox **Host-only** setting + isolation proven (target ping succeeds,
  internet ping fails).
- **Recon/scanning/sniffing (Q7–Q9):** `arp-scan`; Nmap output; Wireshark HTTP (readable) vs TLS
  (unreadable).
- **Web vulns (Q10):** the attack succeeding at Low **and** failing at High.
- **Passwords (Q11):** the weak hash cracked, the strong one not — on **your own** hashes.
- **Firewall (Q12):** `ufw status` + fewer open ports after enabling.
- **Forensics (Q14–Q15):** matching SHA-256 hashes; a recovered file; Autopsy artefacts.

## Before you print
1. Answer all 16 questions; check each has the work **and** a screenshot **and** an explanation — and
   a **countermeasure** wherever there was an attack.
2. Confirm the **legal statement** is in your Introduction.
3. Get the sign-off table signed by your instructor.
4. Print, arrange in page order, and bind (spiral or staple) as your college requires.

---

> **Companion documents:** [IT246_Lab_Questions.md](IT246_Lab_Questions.md) (what to answer),
> [IT246_Lab_Manual.md](IT246_Lab_Manual.md) (step-by-step how, with safety rules), and
> [IT246_Lab_Work_and_Viva.md](IT246_Lab_Work_and_Viva.md) (instructor/viva copy).
