# IT 246 — IT Ethics & Cybersecurity · Lab Manual (Student Workbook)
### BIM 6th Semester · 16 weekly practicals · **for complete beginners**

> **Read this first.** This is a **hands-on cybersecurity lab**. It assumes you have **never** used a
> command line, never installed a virtual machine, and have never touched a security tool. Every step
> tells you exactly what to click, type, and expect. Do the labs **in order** — each one builds on the
> last.
>
> **This lab is purely technical, and it starts in Week 1.** The *ethics and intellectual-property*
> parts of the course (Units 1–4) are learned and assessed in **lectures and classwork** — they have
> no hands-on lab, so there is no "ethics practical." The lab instead spends Weeks 1–7 building the
> foundations the security tools actually need (**Linux → networking → your isolated lab**), then runs
> the real tools in Weeks 8–16. *(You still answer ethics/law questions in the report where they
> connect to the technical work — e.g. the legality of scanning, and the cyber-law capstone.)*

---

## ⚠️ THE GOLDEN RULES — read them now, and again before every lab from Lab 6

Security tools are powerful. Using them on systems you don't own is a **crime** under Nepal's
**Electronic Transaction Act (ETA) 2063** and similar laws everywhere. In this course:

1. **Isolated lab only.** Every scanning/attacking tool runs **inside your own virtual machines**, on
   a **host-only network with no internet**, against **targets we provide** (DVWA, Metasploitable).
2. **Never touch real systems.** Never scan, sniff, phish, or crack anything on your college network,
   your friends, a real website, or the public internet. "Just testing" is not a defence.
3. **Every attack is paired with its defence.** The point of seeing an attack is to learn how to
   **stop it**. Each attack lab ends with the countermeasure.
4. **Get written permission for anything real.** Real security testing always requires the owner's
   written authorization. In this course, your only authorized targets are the lab VMs.

> If you're ever unsure whether something is allowed — **ask your instructor first.** These rules are
> also your exam answers on the legal/ethical parts.

---

## The tools you will use (installed step-by-step across the labs)

| Tool | What it is | Labs |
|------|-----------|------|
| **VirtualBox** | Free software that runs a whole computer *inside* a window (a "virtual machine") | 1, 6 |
| **Kali Linux** | A Linux system pre-loaded with security tools (your "attacker" VM) | 1–16 |
| **DVWA / Metasploitable** | Deliberately **vulnerable** practice targets (your "victim" VM) — safe to attack | 6–16 |
| **The Linux terminal** | The text command line — how you drive almost every tool | 2–16 |
| **Nmap** | Scans a network to find hosts and open ports | 7–8 |
| **Wireshark** | Captures and reads network traffic | 9 |
| **hashcat / John the Ripper** | Demonstrates password cracking (on hashes you make yourself) | 11 |
| **ufw / firewall** | Configures which network traffic is allowed | 12 |
| **SET (Social-Engineering Toolkit)** | Demonstrates how phishing pages are made — to recognize them | 13 |
| **Autopsy / foremost** | Digital-forensics tools to image disks and recover files | 14–15 |

---

## The lab document set (which file is which)

| File | For | Use it to |
|------|-----|-----------|
| **IT246_Lab_Setup_Guide.md** | instructor | prepare the room (VirtualBox + VMs + network) before Day 1 |
| **IT246_Lab_Manual.md** (this file) | everyone | the step-by-step for each lab — teach/learn from it |
| **IT246_Lab_Questions.md** | students | the questions to answer in the report |
| **IT246_Lab_Report_Format.md** | students | how to format & print the report |
| **IT246_Lab_Work_and_Viva.md** | instructor | objectives, expected output & viva model answers (grading) |

## How to use this manual with your lab report

For **every** lab, save evidence for your report (see
[IT246_Lab_Report_Format.md](IT246_Lab_Report_Format.md)):
1. **What you did** (the command or the configuration).
2. A **screenshot** of the result on *your* screen (from your isolated lab — a host-only IP like
   `192.168.56.x` is good proof).
3. A **short explanation** in your own words — including, for every attack, **the countermeasure**.

---
---

# PART 1 — Foundations: Linux, Networking & Your Isolated Lab (Labs 1–7)
*You cannot use security tools without knowing Linux and networking first. These seven weeks build
exactly that — real skills, from zero.*

---

## Lab 1 (Week 1) — Your first Linux virtual machine

**Goal:** Install **VirtualBox**, boot the **Kali Linux** VM, log in, open a terminal, and take a
snapshot. By the end you have a safe Linux computer running inside your own.

### Before you start
- A computer with **8 GB RAM** (4 GB will be very slow), **~40 GB free disk**, hardware
  virtualization enabled, and the admin password.
- Your instructor will provide the **Kali VM image** (and usually a ready-made `.ova` you just import,
  to avoid a huge download).

> **Instructor:** the full room-preparation steps — download links, versions, the target VM, the
> host-only network, and how to package images for the class — are in the
> **[Lab Setup Guide](IT246_Lab_Setup_Guide.md)**. Do that once before this session.

### Steps

**1. Install VirtualBox.** Go to **`https://www.virtualbox.org`** → **Downloads** → pick your operating
system → install with the default options (click Next/Allow through any popups).

**2. Import the Kali VM.** In VirtualBox: **File → Import Appliance** → choose the Kali file your
instructor gave you → **Import** and wait.

**3. Start Kali.** Select the Kali VM in the list → click **Start** (green arrow). A window opens and
Linux boots.

**4. Log in.** The default login is usually `kali` / `kali` (confirm with the image notes).

**5. Open a terminal.** Click the black terminal icon (top bar), or press `Ctrl+Alt+T`. A text window
opens with a prompt like `┌──(kali㉿kali)-[~]` `└─$`.

**6. Prove it works.** Type each and press Enter:
```bash
whoami        # who am I? -> kali
uname -a      # what system is this? -> Linux ...
```

**7. Take a snapshot (your undo button).** In the VirtualBox menu for this VM: **Machine → Take
Snapshot** → name it **clean**. If you ever break the VM, you restore this.

### What you should see
Kali booted, a terminal open, and `whoami` printing `kali`. Screenshot the desktop + terminal.

### If it goes wrong
- **"VT-x/AMD-V not available":** enable **virtualization** in your computer's BIOS/UEFI (ask your
  instructor). On Windows you may also need to turn off Hyper-V.
- **Very slow:** give the VM less RAM (VM → Settings → System), close other apps, or use a lab machine.

### What you learned
A **virtual machine** is a full computer running in software — so you can experiment safely without
risking your real machine. The **terminal** is where the rest of this course happens.

---

## Lab 2 (Week 2) — The Linux command line

**Goal:** Get comfortable moving around Linux and handling files from the terminal — the single most
important skill for everything that follows.

### Steps — type each, read the result

```bash
pwd                 # print working directory: where am I now?
ls                  # list files here
ls -l               # list with details (permissions, size, date)
ls -la              # also show hidden files (start with .)
cd /home/kali       # change directory
cd ..               # go up one level
cd ~                # go to your home folder
```

Now create and edit things:

```bash
mkdir lab2                 # make a folder
cd lab2
touch notes.txt            # create an empty file
nano notes.txt             # open a simple editor -> type a line -> Ctrl+O, Enter, Ctrl+X to save/exit
cat notes.txt              # print the file's contents
cp notes.txt copy.txt      # copy
mv copy.txt renamed.txt    # rename/move
rm renamed.txt             # delete
ls                         # see what's left
```

Getting help (remember this):

```bash
man ls              # the manual for any command (press q to quit)
ls --help           # quick help
clear               # clear the screen
```

### What you should see
You can navigate folders and create/read/copy/delete files without a mouse. Screenshot a terminal
showing `mkdir` + `nano` + `cat` of your file.

### If it goes wrong
- **"No such file or directory":** you're not in the folder you think — run `pwd` and `ls` to check.
- **Stuck inside `man`:** press **q** to quit.

### What you learned
The command line is faster and scriptable, and it's how you'll run every security tool. `pwd`/`ls`/`cd`
move you around; `nano`/`cat`/`cp`/`mv`/`rm` handle files; `man` explains anything.

---

## Lab 3 (Week 3) — Users, permissions & installing tools

**Goal:** Understand Linux **users and file permissions** (this *is* access control — the heart of
security) and learn to **install tools** with the package manager.

### Steps

**1. Who am I, and becoming admin:**
```bash
id                       # your user and groups
sudo whoami              # run a command as admin (root) -> prints "root"
```
`sudo` = "do this as the superuser (admin)." You'll type it before anything that changes the system.

**2. Read file permissions.** Run `ls -l`. Each line starts like `-rwxr-xr--`:
- First char: `-` file, `d` directory.
- Then three groups of **rwx** = **read / write / execute** for **owner**, **group**, **others**.

Make a file and change its permissions:
```bash
touch secret.txt
chmod 600 secret.txt     # owner can read/write; nobody else can
ls -l secret.txt         # confirm: -rw-------
chmod 644 secret.txt     # owner rw, others read-only
```

**3. Install a tool with `apt`** (the package manager):
```bash
sudo apt update              # refresh the list of available software
sudo apt install -y tree     # install a small tool called "tree"
tree /home/kali/lab2         # show a folder as a tree
```

**4. See running programs (processes):**
```bash
ps aux | head            # list processes
top                      # live view (press q to quit)
```

### What you should see
`sudo whoami` printing `root`, a file whose permissions you changed, and `tree` installed and working.
Screenshot the `ls -l` permission change and the `apt install`.

### What you learned
Linux **permissions** decide who can read/write/run each file — that's **access control**, a core
security idea (the **C** in the CIA triad you'll meet in Lab 6). `sudo` grants admin power; `apt`
installs the tools you need.

---

## Lab 4 (Week 4) — Networking fundamentals I: addresses & ports

**Goal:** Understand what an **IP address** and a **port** are, and how one computer talks to another —
the model behind every network attack and defence.

### Steps

**1. Find your machine's address:**
```bash
ip a                 # show network interfaces and IP addresses
```
Look for a line like `inet 192.168.56.10/24` — that's this VM's **IP address**. `192.168.x.x` is a
**private** address (used inside local networks). You'll also see a **MAC address** (`link/ether …`) —
the hardware ID of the network card.

**2. The idea of a port (write this in your report).** One computer runs many services. An **IP
address** finds the *computer*; a **port number** (0–65535) finds the *service* on it. Well-known
ports:
- **80** = HTTP (web) · **443** = HTTPS (secure web) · **22** = SSH (remote login) · **3306** = MySQL.

**3. Client and server (the core model).** A **client** asks; a **server** answers. Your browser
(client) connects to a web server on port 80/443. Test the loopback (your own machine):
```bash
ping -c 4 127.0.0.1      # 127.0.0.1 = "localhost" = this machine; 4 pings then stop
ping -c 4 <your-own-ip>  # replace with the IP from step 1
```
`ping` sends a tiny "are you there?" packet and times the reply.

### What you should see
Your VM's IP from `ip a`, and successful pings to localhost. Screenshot both.

### If it goes wrong
- **`ping` runs forever:** you forgot `-c 4`; press `Ctrl+C` to stop.

### What you learned
Every machine has an **IP address** (which computer) and offers services on **ports** (which service).
Communication is **client → server**. Attackers look for open ports; defenders close them (Lab 8 & 12).

---

## Lab 5 (Week 5) — Networking fundamentals II: services, DNS & HTTP

**Goal:** See a real **client and server** talk on your own VM, and understand **TCP/IP, DNS, and
HTTP** — the protocols the later labs attack and defend.

### Steps

**1. Key ideas (note them):**
- **TCP** = reliable, ordered connection (used by web, email); **UDP** = fast, no guarantee (used by
  video, DNS). A **TCP connection** starts with a 3-step "handshake" (SYN → SYN/ACK → ACK).
- **DNS** = the internet's phone book: turns a name (`google.com`) into an IP address.
- **HTTP** = the language of the web: a client sends a **request**, the server sends a **response**.

**2. See what's listening on your machine:**
```bash
ss -tuln         # list listening TCP/UDP ports (t=tcp u=udp l=listening n=numbers)
```

**3. Run your own web server and connect to it (client + server on one VM):**
```bash
# In terminal 1: start a simple web server on port 8000
python3 -m http.server 8000
```
Open a **second** terminal tab (`Ctrl+Shift+T`) and act as the client:
```bash
curl http://127.0.0.1:8000/      # fetch the page over HTTP -> you see HTML come back
```
Go back to terminal 1 — you'll see the server **logged your request**. Press `Ctrl+C` there to stop it.

**4. See an HTTP request/response detail:**
```bash
curl -v http://127.0.0.1:8000/   # -v shows the request headers and the response headers
```

### What you should see
`ss -tuln` listing your server on port 8000, and `curl` fetching the page while the server logs the
hit. Screenshot the two terminals (server + client).

### What you learned
Services **listen on ports**; a **client** connects and exchanges **HTTP** requests/responses over
**TCP**. You just watched a server and client talk — exactly what Wireshark will capture in Lab 9 and
what web attacks in Lab 10 abuse.

---

## Lab 6 (Week 6) — Complete your isolated lab (attacker + target)

**Goal:** Add a **vulnerable target VM**, connect it and Kali on a **host-only network with no
internet**, and prove the isolation. Then learn the core security vocabulary. This is the sandbox for
every remaining lab.

### Steps

**1. Import the target VM.** In VirtualBox: **File → Import Appliance** → choose the
**Metasploitable / DVWA** image your instructor provided → **Import**.

**2. Put BOTH VMs on a host-only network (critical for safety).** For **each** VM (Kali and the
target): select it → **Settings → Network → Adapter 1** → set **"Attached to" = Host-only Adapter**.
(Create one first if needed, via **File → Host Network Manager → Create**.)

**3. Start both VMs** and find their IPs. In each, run `ip a` — both should be on the same
`192.168.56.x` range. Note Kali's IP and the target's IP.

**4. Prove the isolation (this is the safety test):**
```bash
# From Kali:
ping -c 3 <target-ip>     # SHOULD succeed -> the two VMs can talk to each other
ping -c 3 8.8.8.8         # SHOULD FAIL -> no internet = fully isolated = safe & legal
```

**5. Snapshot both VMs** as **clean** (Machine → Take Snapshot), so you can undo any lab.

**6. Learn the vocabulary (write these in your report):**
- **CIA triad** — the three goals of security: **Confidentiality** (only authorized people read it),
  **Integrity** (data isn't tampered with), **Availability** (it's there when needed).
- **Vulnerability** = a weakness (e.g. an unpatched service). **Threat** = something that could exploit
  it (e.g. an attacker). **Attack** = the threat actually exploiting the vulnerability.

### What you should see
Kali pinging the target **successfully**, and the internet ping **failing** (proving isolation).
Screenshot the VirtualBox network setting and both ping results.

### If it goes wrong
- **VM can reach the internet (it must not):** the adapter is on NAT/Bridged — change it to
  **Host-only**.
- **Ping to target fails:** target VM isn't running, or the two are on different adapters — recheck
  both are Host-only and powered on.

### What you learned
A **host-only network** isolates your lab so nothing escapes to real systems — this is what makes the
rest of the course legal. You now have an **attacker (Kali)** and a **target**, and you know the **CIA
triad** and the vulnerability/threat/attack chain.

---

## Lab 7 (Week 7) — Security concepts & first reconnaissance

**Goal:** Do your first hands-on **reconnaissance** — find the target on the network and see what it
exposes — and understand **attack surface**. This bridges straight into Nmap next week.

### Steps

**1. Confirm your isolated network.** In Kali: `ip a` (note Kali's IP, e.g. `192.168.56.10`). The
target is on the same range.

**2. Find live hosts (a manual "ping sweep"):**
```bash
# arp-scan lists machines on your local network segment
sudo arp-scan --interface=eth0 --localnet
```
*(If `arp-scan` isn't installed: `sudo apt install -y arp-scan`. If your interface isn't `eth0`, use
the name from `ip a`.)* You should see the target's IP and MAC listed.

**3. Knock on a port with netcat.** If the target runs a web server on port 80:
```bash
nc -v <target-ip> 80        # connect to port 80; you may see it open / a banner
# type:  GET / HTTP/1.0     then press Enter twice to get a response
```

**4. Understand "attack surface" (write it).** The **attack surface** is everything about a system an
attacker could interact with — open ports, running services, web pages, logins. **Recon** is mapping
that surface. Defenders shrink it by turning off what isn't needed.

### What you should see
`arp-scan` listing your target, and a connection to an open port. Screenshot the scan.

### What you learned
**Reconnaissance** is always the attacker's first step — you can't attack what you haven't found. Next
week, **Nmap** automates this and reveals *every* open port and service at once.

---
---

# PART 2 — Cybersecurity Tools: Attack & Defence (Labs 8–13)
*Unit 5 (cybersecurity fundamentals) has started in lectures. You now use real tools — always inside
your isolated lab (built in Lab 6). Re-read the Golden Rules.*

---

## Lab 8 (Week 8) — Reconnaissance & scanning with Nmap

**Goal:** Use **Nmap** to discover the target and all its open ports/services, then apply the
countermeasure (Unit 5). *(Only against your own target VM.)*

### Steps

**1. Confirm your isolated network.** In Kali, run `ip a` and note Kali's IP. The target must be on the
same `192.168.56.x` host-only range (from Lab 6). **Both must be your VMs.**

**2. Find live hosts:**
```bash
nmap -sn 192.168.56.0/24
```
This lists which VMs are up. Note the target's IP.

**3. Scan the target's ports** (replace with your target's IP):
```bash
nmap 192.168.56.101
```
You'll see a list of **open ports** and **services** (e.g. 21/ftp, 80/http, 3306/mysql).

**4. Get more detail (versions):**
```bash
nmap -sV 192.168.56.101
```
This shows the **software versions** — how attackers find known-vulnerable versions.

**5. The countermeasure (write this up):** open ports are the "doors" into a machine. Defences:
- **Close/disable** services you don't need.
- Put a **firewall** in front (Lab 12).
- Keep software **updated** so version-based attacks fail.

### What you should see
Nmap output listing the target's open ports and services. Screenshot it.

### If it goes wrong
- **"Note: Host seems down":** the target VM isn't running, or it's on a different network — recheck the
  host-only adapter and that the target is powered on.

### What you learned
**Scanning** automates recon — it maps the whole attack surface fast. Defenders reduce that surface by
closing unused ports, firewalling, and patching.

---

## Lab 9 (Week 9) — Capturing traffic with Wireshark

**Goal:** See why **unencrypted** traffic is dangerous, using **Wireshark** on your lab network — then
understand the fix (Unit 5). *(Capture only your own lab traffic.)*

### Steps

**1. Open Wireshark** in Kali (Applications → Sniffing → Wireshark, or type `wireshark`).

**2. Start a capture** on the host-only interface (double-click it, e.g. `eth0`/`eth1`).

**3. Generate some traffic.** From Kali, visit the target's web page over plain HTTP, e.g.:
```bash
curl http://192.168.56.101/
```
or log in to DVWA in the browser.

**4. Filter and read it.** In Wireshark's filter bar type `http` and press Enter. Click a packet →
expand it. If a login was sent over **HTTP**, you can see the **username/password in plain text**.

**5. The countermeasure (write this up):**
- **HTTPS/TLS encrypts** traffic so a sniffer sees only scrambled data.
- Never send credentials over plain HTTP; use a VPN on untrusted networks.
- Filter `tls` in Wireshark to see that encrypted traffic is unreadable — the contrast is the lesson.

### What you should see
Captured HTTP packets, ideally showing readable form data; and encrypted TLS packets that are
unreadable. Screenshot both.

### What you learned
Anything sent **unencrypted** can be read by anyone on the network. **HTTPS/TLS** is the defence — this
is why the padlock matters.

---

## Lab 10 (Week 10) — Web vulnerabilities: SQL Injection & XSS (and the fix)

**Goal:** On the deliberately-vulnerable DVWA, see **SQL Injection** and **Cross-Site Scripting
(XSS)** work, then learn exactly how developers stop them (Unit 5). *(DVWA only.)*

> Set DVWA's security level to **Low** for the demo, then read how **High** blocks it.

### Steps

**1. SQL Injection (SQLi).**
- In DVWA → **SQL Injection**. In the input box, a normal id like `1` returns one user.
- Now enter: `1' OR '1'='1` — the page returns **all** users. You changed the query's logic.
- **Why it worked:** the app glued your text directly into its SQL.
- **The fix (write it):** use **prepared statements / parameterized queries** so input is treated as
  data, never as SQL. Switch DVWA to **High** and show the same input now fails.

**2. Cross-Site Scripting (XSS).**
- In DVWA → **XSS (Reflected)**. In the name box enter: `<script>alert('xss')</script>`.
- A pop-up appears — your script ran in the browser.
- **Why it worked:** the app printed your input into the page without escaping it.
- **The fix (write it):** **escape/encode output** (e.g. `htmlspecialchars`) so `<script>` shows as
  text, and set a Content-Security-Policy. Show DVWA **High** rendering it as harmless text.

### What you should see
The SQLi returning all records; the XSS pop-up; and both **failing** at High security. Screenshot each.

### What you learned
Both attacks come from **trusting user input**. **SQLi** is stopped by prepared statements; **XSS** is
stopped by escaping output. As a developer, never build queries or HTML by pasting raw user input.

---

## Lab 11 (Week 11) — Passwords: strength, hashing & cracking demo

**Goal:** Understand why weak passwords fall instantly, using a cracking tool **on hashes you create
yourself** — then adopt strong defences (Unit 6). *(Your own hashes only.)*

### Steps

**1. Make some hashes to crack (your own).** In Kali's terminal:
```bash
echo -n "password123" | md5sum
echo -n "Tr0ub4dour&3!xQ" | md5sum
```
Copy each hash into a text file `hashes.txt` (one per line).

**2. Crack with a wordlist.** Kali ships with the `rockyou` wordlist:
```bash
# unzip the wordlist once
sudo gunzip /usr/share/wordlists/rockyou.txt.gz 2>/dev/null
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
john --show --format=raw-md5 hashes.txt
```
- The **weak** password (`password123`) is cracked in seconds; the **strong** random one is not found.

**3. The countermeasures (write these up):**
- Use **long, random** passwords (a **password manager** generates/stores them).
- Turn on **Multi-Factor Authentication (MFA)** so a stolen password isn't enough.
- Sites should store passwords with a **slow salted hash** (bcrypt/argon2), never plain or MD5.

### What you should see
`john` cracking the weak password but not the strong one. Screenshot the result.

### What you learned
Weak/common passwords are in every wordlist and fall instantly. Defences: **length + randomness +
MFA**, and proper **salted hashing** on the server side.

---

## Lab 12 (Week 12) — Firewall configuration & work-from-home defence

**Goal:** Configure a **host firewall** to control traffic, and build a personal WFH security
checklist (Unit 6). *(On your own VM.)*

### Steps

**1. Check the firewall status** (using `ufw` — the Uncomplicated Firewall):
```bash
sudo ufw status
```

**2. Set safe default rules:**
```bash
sudo ufw default deny incoming      # block all incoming by default
sudo ufw default allow outgoing     # allow the machine to reach out
sudo ufw allow 22/tcp               # allow SSH (example of an explicit allow)
sudo ufw enable
sudo ufw status verbose
```

**3. Test the effect.** From Kali, re-run your Nmap scan (Lab 8) against the firewalled machine — ports
you didn't allow should now show **filtered/closed**. This proves the firewall reduced the attack
surface.

**4. Remove a rule (clean up):**
```bash
sudo ufw deny 22/tcp
```

**5. Write a WFH security checklist** (Unit 6): strong Wi-Fi password + WPA3, updated OS, firewall on,
VPN for work, separate work/personal devices, lock screen, encrypted disk, careful with home IoT.

### What you should see
`ufw status` showing your rules, and an Nmap scan showing fewer open ports after the firewall.
Screenshot both, plus your checklist.

### What you learned
A **firewall** decides which traffic is allowed — "default deny" is the safe posture. Personal
cybersecurity at home is a **layered checklist**, not a single setting.

---

## Lab 13 (Week 13) — Phishing awareness (Social-Engineering Toolkit)

**Goal:** See how a phishing page is cloned **inside the isolated lab**, so you can **recognize and
prevent** real phishing (Unit 7). *(Lab network only — never send anything to a real person.)*

> **Strict rule:** the cloned page stays on your host-only network and is shown only to your own VMs.
> Sending a phishing link to any real person is illegal. This lab is purely to learn the red flags.

### Steps

**1. Understand the attack first (write it):** phishing tricks a victim into entering credentials on a
fake copy of a real login page. Attackers rely on **urgency, trust, and look-alike URLs**.

**2. See a clone in the lab (demonstration).**
- In Kali: `sudo setoolkit` → choose **Social-Engineering Attacks → Website Attack Vectors →
  Credential Harvester → Site Cloner**.
- When asked for the URL to clone, use a **local practice page** or a generic login — keep everything
  on your host-only IP. From your *other* lab VM's browser, open Kali's IP and observe the cloned page.
- Note how convincing it looks and that the URL/IP is the giveaway. **Stop here — do not deploy it
  anywhere real.**

**3. The countermeasures (the real deliverable — write these up):**
- **Check the URL** carefully (misspellings, wrong domain, no HTTPS on a login).
- **Never click links** in unexpected emails/SMS; type the address yourself.
- Enable **MFA** so a stolen password alone fails.
- Report suspected phishing; organizations should run **awareness training** and email filtering.

**4. Build an anti-phishing checklist** (5–7 red flags a user can spot).

### What you should see
The cloned login page shown only inside your lab, and your anti-phishing checklist. Screenshot the
lab-only page and your checklist.

### What you learned
Phishing is **social engineering** — it attacks the human, not the software. The defence is
**awareness + verifying URLs + MFA**. Recognizing the red flags is the goal, not attacking anyone.

---
---

# PART 3 — Digital Forensics, Incident Response & Cyber Law (Labs 14–16)
*Units 8–9. Now you handle evidence, respond to incidents, and connect it all to Nepal's cyber law.*

---

## Lab 14 (Week 14) — Digital forensics I: disk imaging & data recovery · **lab practical week**

**Goal:** Learn evidence handling — create a **forensic image**, **recover deleted files**, and
document a **chain of custody** (Unit 8). *(On a small test drive/file you own.)*

### Steps

**1. Prepare a tiny test "evidence" source.** Create a small file, delete it, so you have something to
recover. For example, on a small USB or a disk image file:
```bash
# create a small disk image to practise on
dd if=/dev/zero of=evidence.img bs=1M count=20
mkfs.vfat evidence.img
# mount it, add a file, delete it (simulating a suspect's deleted file)
```
*(Your instructor will give exact steps for your setup — the idea is: a small volume with a deleted
file.)*

**2. Make a forensic copy (never work on the original).** Image it with `dd` and record a hash so you
can prove it wasn't altered:
```bash
dd if=evidence.img of=evidence_copy.img
sha256sum evidence.img evidence_copy.img   # the two hashes must match
```

**3. Recover deleted files.** Use a recovery tool on the **copy**:
```bash
foremost -i evidence_copy.img -o recovered/
```
Look inside `recovered/` for your deleted file.

**4. Chain of custody.** Fill a simple table for your report: *who* collected the evidence, *when*,
*what* it is, its **hash**, and every hand-off. Explain why the hash proves integrity.

### What you should see
Matching SHA-256 hashes (proving an exact copy) and a recovered file. Screenshot the hash match and
the recovered file.

### What you learned
Forensics rule #1: **work on a verified copy, never the original.** A **hash** proves the copy is
identical and untampered. The **chain of custody** keeps evidence admissible.

---

## Lab 15 (Week 15) — Digital forensics II & incident response

**Goal:** Examine an image for **artefacts**, understand **mobile forensics**, and run an
**incident-response** tabletop (Unit 8).

### Steps

**1. Analyse with Autopsy.** Open **Autopsy** (in Kali or as a provided tool). Create a new case, add
your `evidence_copy.img` as a data source, and let it process. Explore: deleted files, file
timestamps, and any recovered documents/images. Note 2 artefacts you found.

**2. Mobile forensics (concept + note).** Explain in your report how phone forensics differs: data is
in apps/cloud, needs special tools and legal care, and often the device must be isolated (airplane
mode / Faraday bag) to stop remote wiping.

**3. Incident-response tabletop.** Take a scenario: *A college computer is infected with ransomware.*
Write the response using the standard phases:
1. **Preparation** (backups, plan exist beforehand)
2. **Identification** (detect and confirm the incident)
3. **Containment** (isolate the machine from the network)
4. **Eradication** (remove the malware)
5. **Recovery** (restore from clean backups)
6. **Lessons learned** (what to fix so it can't recur)

### What you should see
Autopsy showing recovered artefacts, and your written IR plan for the scenario. Screenshot the Autopsy
findings.

### What you learned
Forensics reconstructs *what happened*; **incident response** is the disciplined **detect → contain →
eradicate → recover → learn** cycle that limits damage.

---

## Lab 16 (Week 16) — Cyber-law mapping & investigation capstone

**Goal:** Connect everything to **Nepal's cyber law** and present your lab portfolio (Unit 9).

### Steps

**1. Study the law.** Read a summary of Nepal's **Electronic Transaction Act (ETA) 2063** — focus on
what it makes illegal (unauthorized access, data theft, damaging computer systems, cyber-fraud) and
the penalties.

**2. Map a real case (the capstone).** Take a real (or realistic) Nepali cybercrime case — e.g.
unauthorized access to an account, an online fraud, or a data leak. Write:
- What the offender did.
- **Which ETA provision** it violates.
- What evidence a forensic investigator (Labs 14–15) would collect, and how (imaging + chain of
  custody).
- How the victim could have prevented it (link to your defences from Labs 8–13).

**3. Reflect on ethics + law together.** In a short paragraph, connect the course's ethics content
(Units 1–4, from lectures) to Unit 9's law: why we need **both** — law punishes after the fact; ethics
guides behaviour before.

**4. Present your portfolio.** Assemble all 16 labs and present your work (individual or group of ≤4):
the isolated lab, the recon/scanning, the attack-and-defence demos, the forensics work, and this legal
mapping.

### What you should see
A written case-to-law mapping and your complete lab portfolio ready to present.

### What you learned
Cybersecurity, forensics, and **cyber law** form one chain: security protects systems, forensics
investigates breaches, and the **ETA** provides the legal consequences — guided throughout by the
ethics you studied in lectures.

---
---

## Appendix A — Safety & troubleshooting (all technical labs)

| Problem | Cause | Fix |
|---------|-------|-----|
| VM won't start ("VT-x not available") | Virtualization disabled | Enable it in BIOS/UEFI (ask instructor); disable conflicting Hyper-V on Windows |
| VM can reach the internet (it must not) | Adapter set to NAT/Bridged | Change Network → **Host-only Adapter** (Lab 6) |
| `ping`/scan to target fails | Target off / wrong network | Power on target; confirm both on `192.168.56.x` host-only |
| A VM got broken during a lab | Expected — that's why we snapshot | Restore the **clean** snapshot (Lab 1 / Lab 6) |
| `ping` never stops | Missing `-c` count | Press `Ctrl+C`; use `ping -c 4 …` |
| Tool asks to attack a real URL/IP | Never allowed | Use only your lab VMs' IPs; if unsure, stop and ask |
| Wireshark shows nothing | Capturing wrong interface | Select the **host-only** interface (from `ip a`) |
| "command not found" | Tool not installed | `sudo apt update && sudo apt install -y <tool>` |

## Appendix B — Command cheat-sheet (what you learned)

`whoami` · `uname -a` · `pwd` · `ls -la` · `cd` · `mkdir` · `touch` · `nano` · `cat` · `cp` · `mv` ·
`rm` · `man` · `sudo` · `id` · `chmod` · `chown` · `apt update`/`apt install` · `ps`/`top` · `ip a` ·
`ping -c` · `ss -tuln` · `curl` · `python3 -m http.server` · `arp-scan` · `nc` · `nmap` · `wireshark` ·
`john` · `ufw` · `setoolkit` · `dd` · `sha256sum` · `foremost` · Autopsy.

## Appendix C — The one rule that keeps you legal
> **Only ever run these tools inside your own isolated lab, against the VMs we provide.** Everything
> else needs the owner's **written permission**. This is both the law (ETA 2063) and professional
> ethics — and it is the answer examiners want to hear.

> **Next:** answer the questions in [IT246_Lab_Questions.md](IT246_Lab_Questions.md), lay them out
> using [IT246_Lab_Report_Format.md](IT246_Lab_Report_Format.md), and get each lab signed off.
