# IT 246 — Lab Setup / Installation Guide (Instructor Prep)
### IT Ethics & Cybersecurity · BIM 6th Semester · Build the isolated cybersecurity lab

> **What this is.** The **preparation** guide you (the instructor / lab assistant) follow **before Day
> 1**, and the concrete reference behind **Lab 1** (install) and **Lab 6** (add the target + network) in
> the [Lab Manual](IT246_Lab_Manual.md). Do this once per lab room (or hand it to students who use
> their own laptops). By the end you have a working **attacker VM + target VM on an isolated network**,
> ready to teach.

> **Which document is which** — teach from the **[Lab Manual](IT246_Lab_Manual.md)** (step-by-step,
> students follow); grade with the **[Lab Work & Viva](IT246_Lab_Work_and_Viva.md)** (objectives +
> model answers); give students the **[Lab Questions](IT246_Lab_Questions.md)** and
> **[Report Format](IT246_Lab_Report_Format.md)**; use **this Setup Guide** to prepare the machines.

---

## What you are building (the picture)

```
   Your computer (the "host" — Windows / macOS / Linux)
   └── VirtualBox
        ├── Kali Linux VM     ← the "attacker" (all the security tools)   IP 192.168.56.x
        └── Metasploitable 2  ← the "target/victim" (safe to attack)      IP 192.168.56.y
             (both joined ONLY to a Host-Only network: they can talk to
              each other, but have NO internet — this is what keeps it legal & safe)
```

Everything students do runs **inside** these VMs. Nothing can reach the real internet or the college
network. That isolation is the whole safety model of the course.

---

## Part 0 — Requirements (check these first)

**Per host machine (a lab PC or a student laptop):**
- **64-bit CPU with hardware virtualization** (Intel **VT-x** or AMD **AMD-V**) — must be **enabled in
  BIOS/UEFI** (see Part 2, step 2). Almost every PC from the last decade has it.
- **RAM: 8 GB minimum** (Kali uses ~2 GB, Metasploitable ~0.5 GB, host keeps the rest). 4 GB will be
  painfully slow — use lab machines instead.
- **Free disk: ~40–60 GB** (Kali image ~15–20 GB expanded, Metasploitable ~2 GB, plus snapshots).
- OS: Windows 10/11, macOS, or Linux.

**Software you'll download (all free):**
| Item | Where | Size (approx) |
|------|-------|---------------|
| **VirtualBox 7.x** installer | `https://www.virtualbox.org` → Downloads | ~110 MB |
| **Kali Linux — prebuilt VirtualBox image** | `https://www.kali.org/get-kali/` → **Virtual Machines** → **VirtualBox 64-bit** | ~3–4 GB (.7z) |
| **Metasploitable 2** (the target) | `https://sourceforge.net/projects/metasploitable/` (Rapid7's intentionally-vulnerable VM) | ~800 MB (.zip) |

> **Why Metasploitable 2 as the target?** It's a single, self-contained victim VM that already exposes
> lots of open ports (great for **Nmap**, Lab 8), plaintext services (great for **Wireshark**, Lab 9),
> **and it ships with DVWA** (Damn Vulnerable Web App) for the **SQLi/XSS** lab (Lab 10) — reachable at
> `http://<target-ip>/dvwa` (login `admin` / `password`). One download covers Labs 8–12. It needs **no
> internet**, which suits our isolated network. *(Alternatives: a standalone DVWA VM, or OWASP Juice
> Shop, if you prefer a modern web target — but Metasploitable 2 is the simplest for beginners.)*

---

## Part 1 — Choose how to deploy (pick ONE)

**Option A — Pre-built images you distribute (recommended for a class).**
You build the two VMs **once** on your machine (Parts 2–7), then **export** them as `.ova` files
(Part 8) and copy them to student machines by USB / shared drive. Students just **import** — fast,
identical for everyone, and **no big downloads on lab day**. Best when the lab has limited or shared
internet.

**Option B — Each student installs on their own laptop.**
Give students this guide; each downloads VirtualBox + the two images and does Parts 2–7 themselves.
Good for BYOD classes with decent internet. Budget extra time in the first session.

> Recommended: **Option A**. Do Parts 2–7 yourself now; do Part 8 to package; on Lab 1 students only
> install VirtualBox and import your `.ova` files.

---

## Part 2 — Install VirtualBox (+ enable virtualization)

**1. Install VirtualBox.** Download the installer for your OS from `virtualbox.org` and run it,
accepting the defaults (click through the network-interface warning — it's normal). *(The
"Extension Pack" is optional and **not** needed for this course.)*

**2. Enable virtualization in BIOS/UEFI (do this if a VM later refuses to start).**
- Restart the computer and enter BIOS/UEFI (usually **F2**, **F10**, **Del**, or **Esc** at boot —
  varies by brand).
- Find **Intel VT-x / Virtualization Technology** (or **AMD-V / SVM Mode**) and set it **Enabled**.
- Save and exit.
- **Windows note:** if VirtualBox shows VT-x errors even after this, Microsoft **Hyper-V** is grabbing
  virtualization. Turn it off: *Control Panel → Programs → Turn Windows features on or off →* untick
  **Hyper-V**, **Windows Hypervisor Platform**, and **Virtual Machine Platform** → restart.

---

## Part 3 — Get and import the Kali (attacker) VM

**1. Download** the Kali **prebuilt VirtualBox image** from `kali.org/get-kali` → **Virtual Machines**
→ **VirtualBox**. You get a `.7z` archive.

**2. Extract it** (use **7-Zip** on Windows / **The Unarchiver** on macOS / `7z x file.7z` on Linux).
Inside is a folder with a `.vbox` and a `.vdi` file.

**3. Add it to VirtualBox.** Either double-click the `.vbox` file, **or** in VirtualBox choose
**Machine → Add…** and select the `.vbox`. Kali now appears in the VM list. *(This method — "Add" an
existing image — is different from "Import Appliance", which you'll use for `.ova`/Metasploitable.)*

**4. Give it resources** (select Kali → **Settings**):
- **System → Motherboard:** 2048–4096 MB RAM.
- **System → Processor:** 2 CPUs if the host has 4+.

**Default login:** `kali` / `kali`.

---

## Part 4 — Get and import the Metasploitable 2 (target) VM

**1. Download** Metasploitable 2 from the SourceForge link in Part 0. You get a `.zip`.

**2. Extract it** → you'll find `Metasploitable.vmdk` (a virtual disk) among the files.

**3. Create a VM around that disk.** In VirtualBox → **New**:
- Name: `Metasploitable2` · Type: **Linux** · Version: **Other Linux (64-bit)** (or Ubuntu 32/64).
- Memory: **512 MB** is enough.
- Hard disk: choose **"Use an existing virtual hard disk file"** → browse to `Metasploitable.vmdk` →
  Create.

**Default login:** `msfadmin` / `msfadmin`. *(You rarely need to log in — it runs services on boot.)*

> ⚠️ **Never** connect Metasploitable 2 to the internet or a real network — it is **deliberately
> insecure**. The host-only network in Part 5 is mandatory.

---

## Part 5 — Create the host-only network and attach both VMs

**1. Create a Host-Only network** (once per machine).
- VirtualBox 7: **File → Tools → Network Manager → Host-only Networks → Create**. You'll get one named
  like `vboxnet0` with the range **192.168.56.0/24** (leave the defaults; DHCP enabled is fine).
- *(Older VirtualBox: **File → Host Network Manager → Create**.)*

**2. Attach BOTH VMs to it.** For **each** VM (Kali, then Metasploitable2): select it → **Settings →
Network → Adapter 1**:
- **Enable Network Adapter:** ticked.
- **Attached to:** **Host-Only Adapter**.
- **Name:** the `vboxnet0` you just created.
- Click **OK**.

> This is the single most important safety step. With **Host-Only**, the two VMs see each other but
> **cannot** reach the internet or the college LAN. Do **not** use NAT or Bridged.

---

## Part 6 — First boot, find IPs, and verify isolation

**1. Start Metasploitable2**, wait for the `login:` prompt (it auto-starts its services). Log in
`msfadmin`/`msfadmin` and run `ifconfig` — note its IP (e.g. `192.168.56.101`).

**2. Start Kali**, log in `kali`/`kali`, open a terminal, run `ip a` — note Kali's IP (e.g.
`192.168.56.10`).

**3. Verify the two can talk (should succeed):**
```bash
ping -c 3 192.168.56.101      # Kali → target
```

**4. Verify there is NO internet (should FAIL — this proves isolation):**
```bash
ping -c 3 8.8.8.8             # should be "unreachable" / 100% loss
```

**5. Confirm the web target works** (for Lab 10): in Kali's browser open
`http://192.168.56.101/dvwa` → log in `admin` / `password` → set **DVWA Security = Low** for demos.

### If any check fails
- **VM won't start / VT-x error:** finish Part 2 step 2 (BIOS + Hyper-V).
- **Ping to target fails:** both VMs must be **Host-Only** on the **same** `vboxnet0`, both powered on.
- **Internet ping *succeeds* (bad):** an adapter is still NAT/Bridged — fix it in Settings → Network.

---

## Part 7 — Snapshot both VMs ("clean")

For **each** VM: select it → **Snapshots** (or **Machine → Take Snapshot**) → name it **clean**.
If a lab ever breaks a VM, **restore this snapshot** and it's back to normal in seconds. Tell students
to do this too (it's Lab 1 step 7 and Lab 6 step 5).

---

## Part 8 — (Option A only) Export appliances to distribute

Package your prepared VMs so students just import them:

1. **File → Export Appliance** → tick **both** VMs → **Next**.
2. Format **OVF 2.0**, output e.g. `IT246-lab.ova` → **Export**.
3. Copy the `.ova` (plus the VirtualBox installer) to USB drives / a shared folder.
4. On each student machine: install VirtualBox, then **File → Import Appliance** → select the `.ova` →
   **Import**. Re-check the **Host-Only** network (Part 5) on the imported VMs, then snapshot.

> An `.ova` bundles both VMs and their disks into one file — the fastest way to get 30 identical
> setups without 30 downloads.

---

## ✅ Pre-teaching checklist (run through this the day before Lab 1)

- ☐ VirtualBox installed; a test VM starts without VT-x errors
- ☐ Kali VM boots; login `kali`/`kali` works; terminal opens
- ☐ Metasploitable2 boots to a `login:` prompt
- ☐ A **Host-Only** network exists; **both** VMs attached to it
- ☐ Kali **pings the target** successfully
- ☐ Internet ping **fails** (isolation confirmed)
- ☐ `http://<target-ip>/dvwa` loads and `admin`/`password` logs in
- ☐ A **clean** snapshot saved on both VMs
- ☐ (Option A) `.ova` exported and copied to distribution media
- ☐ You have the [Lab Manual](IT246_Lab_Manual.md) open to Lab 1 to teach from

---

## Credentials & addresses quick-reference (pin this up)

| Thing | Value |
|-------|-------|
| Kali login | `kali` / `kali` |
| Metasploitable 2 login | `msfadmin` / `msfadmin` |
| DVWA (on the target) | `http://<target-ip>/dvwa` — `admin` / `password` |
| Host-Only network range | `192.168.56.0/24` (typical) |
| Find a VM's IP | Kali: `ip a` · Metasploitable: `ifconfig` |
| Undo a broken VM | Restore the **clean** snapshot |

## Rough time budget
- Instructor prep (Parts 2–8), first time: **~2–3 hours** (mostly downloads).
- Student Lab 1 with Option A (import `.ova` + verify): **~30–40 min**.
- Student Lab 1 with Option B (full download + install): **~1.5–2 hours** — split across the session or
  ask students to pre-download.

---

> **Next:** with the lab built, teach **Lab 1** from the [Lab Manual](IT246_Lab_Manual.md). Labs 1–5
> (Linux + networking) only need the Kali VM; Lab 6 brings in the target and the host-only network you
> set up here; Labs 8–16 use both.
