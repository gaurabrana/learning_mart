# IT 246 — Lab Questions (answer from your own lab work)
### IT Ethics & Cybersecurity · BIM 6th Semester · Hands-on cybersecurity lab (isolated VMs)

These are the definitive lab questions for IT 246. You answer them by **documenting the technical lab
work you did across the 16 labs, in a printed lab report (A4)**. For every question, write:

1. **The question** (as given here),
2. **What you did** — the command/configuration or the analysis,
3. **A screenshot** of the result on *your* screen (from your isolated lab), and
4. **A 1–2 line explanation in your own words — and for every attack, its countermeasure.**

> **About ethics/IP (Units 1–4):** these are taught and assessed in **lectures/classwork**, not the
> lab — so there are no "ethics practical" questions here. Where ethics and **cyber law** connect to
> the technical work (the legality of scanning, and the Q16 capstone), you answer them from that work.
>
> **Legal/ethical reminder (state it in your report):** all technical work was done **only inside an
> isolated lab (host-only VMs) against provided targets**. Doing any of it on real systems is illegal
> under Nepal's Electronic Transaction Act 2063. Step-by-step help is in
> **[IT246_Lab_Manual.md](IT246_Lab_Manual.md)**; lay out the report with
> **[IT246_Lab_Report_Format.md](IT246_Lab_Report_Format.md)**.

---

## Part A — Foundations: Linux, Networking & the Isolated Lab (Labs 1–7)

**Q1. First Linux VM.** Show your Kali VM running with a terminal open and `whoami`/`uname -a` output
(screenshot). Explain what a **virtual machine** is and why you use one for this course.

**Q2. Linux command line.** Show a terminal where you create a folder, make a file with `nano`, and
`cat` it back (screenshot). Explain what `pwd`, `ls`, and `cd` do.

**Q3. Users, permissions & packages.** Show `ls -l` before/after a `chmod`, and an `apt install`
(screenshots). Explain how Linux **file permissions (rwx)** relate to **access control** and the CIA
triad, and what `sudo` does.

**Q4. Networking I.** Show `ip a` (your VM's IP) and a successful `ping` (screenshot). Explain the
difference between an **IP address** and a **port**, and the **client/server** model.

**Q5. Networking II.** Show your own web server (`python3 -m http.server`) being fetched with `curl`,
with the server logging the request (screenshot). Explain what **TCP**, **DNS**, and **HTTP** are.

**Q6. Complete the isolated lab.** Show the VirtualBox **Host-only** network setting and prove
isolation: Kali **pings the target successfully** but the **internet ping fails** (screenshots).
Explain why host-only networking makes the labs safe and legal, and define the **CIA triad** and
**vulnerability vs threat vs attack**.

**Q7. First reconnaissance.** Show `arp-scan` (or a ping sweep) finding your target on the network
(screenshot). Explain what **reconnaissance** and **attack surface** mean.

---

## Part B — Cybersecurity Tools: Attack & Defence (Labs 8–13)

**Q8. Scanning (Nmap).** Show your Nmap scan of the target listing open ports/services (screenshot).
Explain how scanning maps the attack surface and give **three countermeasures** to reduce it.

**Q9. Sniffing (Wireshark).** Show a captured **HTTP** packet (readable) and an encrypted **TLS**
packet (unreadable) (screenshots). Explain why HTTP is dangerous and how **HTTPS/TLS** fixes it.

**Q10. Web vulnerabilities.** Show **SQL Injection** (`1' OR '1'='1` returning all users) and **XSS**
(`<script>` popup) working on DVWA at Low, and **failing** at High (screenshots). Name the exact fix
for each (**prepared statements**; **output escaping**).

**Q11. Passwords.** Show a cracking tool breaking a **weak** hash but not a **strong** one, on hashes
**you created yourself** (screenshot). List the defences: length + randomness + **MFA** + salted
hashing.

**Q12. Firewall.** Show `ufw status` with your rules and an Nmap scan showing **fewer open ports** after
enabling the firewall (screenshots). Explain "default deny" and give your **work-from-home** checklist.

**Q13. Phishing awareness.** Show the cloned login page confined to your **lab network only**
(screenshot) and present your **anti-phishing checklist**. Explain why phishing is "social engineering"
and the main defences (verify URL, don't click links, MFA).

---

## Part C — Forensics, Incident Response & Cyber Law (Labs 14–16)

**Q14. Disk imaging & recovery.** Show **matching SHA-256 hashes** for your original and copy, and a
**recovered deleted file** (screenshots). Explain why you work on a copy and how the hash proves
integrity. Include your **chain-of-custody** table.

**Q15. Forensics & incident response.** Show **Autopsy** artefacts from your image (screenshot) and
present your **incident-response plan** for the ransomware scenario using the six phases (preparation →
identification → containment → eradication → recovery → lessons learned).

**Q16. Cyber-law capstone.** Map a real/realistic Nepali cybercrime case to a provision of the
**Electronic Transaction Act 2063**: what the offender did, which provision it breaks, what evidence
would be collected (imaging + chain of custody), and how it could have been prevented (link to your
Lab 8–13 defences). Explain why we need **both ethics and law**.

---

### How this is used
- **Printed lab report (submitted):** answer all 16 questions — each with what you did, a screenshot,
  an explanation, **and the countermeasure for every attack**. Follow the **Lab Report Format** guide
  and get it signed off before printing.
- **Viva (external + internal):** the examiner reads your report and asks you to **explain your own
  work and its defence** — e.g. "how does a prepared statement stop the injection in Q10?" A student
  who did the labs can explain it; a copied report cannot.

*(Instructor's version with model answers and marking: [IT246_Lab_Work_and_Viva.md](IT246_Lab_Work_and_Viva.md).)*
