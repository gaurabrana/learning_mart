# IT 246 — Unit 6: Personal Cybersecurity
### Full Lecturer-Ready Session Material (S28–S32)

**Program:** BIM, 6th Semester · **Unit weight:** 5 lecture hours
**Sessions:** S28–S32 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT246_Unit6.pptx` (92 slides), regenerated via `build_unit6_pptx.py` (imports `deckkit.py`); diagrams via `build_unit6_images.py`.

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each
> session has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just
> bullets), **worked examples**, a **timed in-class activity**, and lecturer cue cards in
> `> 🎙️` blocks. `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags:
> `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.**

---

## Unit 6 — Learning Outcomes
By the end of this unit, students will be able to:
1. Audit the security posture of their own home computer (updates, antivirus, backups, firewall) and fix the weak spots.
2. Harden their mobile phones and home IoT/smart devices against permissions abuse, default passwords, and insecure networks.
3. Apply physical-security habits that protect devices and data from theft, shoulder-surfing, and careless disposal.
4. Configure a safer work-from-home setup — secured router, VPN, work/personal separation, safe video calls.
5. Secure their online accounts with strong unique passwords, a password manager, and MFA/2FA, and respond to a breach.

---
---

# S28 — Evaluating Your Cybersecurity Posture: Home Computer
**Lecture hour 1 of 5 (Unit 6) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"It feels fine" is not a security plan**

> **Deliver (≈2 min):** Paint the picture. "Your laptop has **47 pending updates**, **no backup**, and
> an **antivirus that expired in 2022** — but it **'feels fine.'**"
>
> **Run the question (≈3 min):** "If it got **locked by ransomware tonight**, **what would you lose**,
> and **could you get it back?**" Take a few answers. Land the theme: **most personal security is just
> basic hygiene that nobody actually does.** Today: **what a security posture is → updates → antivirus
> → backups (3-2-1) → firewall.**

> 🎙️ Speaker note: Don't reassure them yet — the point is to expose how many run with no backup and
> stale protection. Write the four-layer agenda (patch · protect · back up · contain) on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Security Posture: auditing yourself `[THEORY]` `[~8 min]`

[SLIDE] **Posture = patch + protect + back up + contain**

> **Deliver:** Define it. **Your security posture is the overall state of how well your device and
> habits resist AND recover from threats.** Teach it as **four layers**: **patch → protect → back up →
> contain.** Then the risk frame: **risk = likelihood × impact.** Low-effort automated attacks are
> **very likely**, and the **impact on a single laptop is your whole digital life** — photos, college
> files, banking sessions. A good posture **assumes something will fail** and makes sure you can
> **recover.**

- 🌍 **Global example:** **WannaCry (2017)** spread mostly to **unpatched Windows machines** worldwide —
  not chosen targets, just unpatched ones.
- 🇳🇵 **Local example:** a **Pulchowk/BIM student's laptop hit by ransomware days before thesis
  submission** — **no backup, files gone.** Not targeted; just reachable and unprotected.

> ❌ **Common misconception:** *"Hackers only target big companies, not me."*
> ✅ **Correction:** "**Most attacks are automated and untargeted** — they scan the internet and hit
> **whoever is unpatched and un-backed-up**, student or bank alike. You don't have to be interesting to
> be a victim; you only have to be **reachable and unprotected.**"

> 🖼️ Visual: a **four-layer posture stack** (Patch → Protect → Back up → Contain).

> 🎙️ Speaker note: Land the mindset shift — security is a **posture you audit**, not a **product you
> buy.** The four layers are the spine of the whole session.

**📊 Depth table — The four posture layers — what each one does**

| Layer | What it does | If you skip it (Nepal / IT) |
|---|---|---|
| Patch | Closes known holes attackers already exploit | An unpatched laptop caught by an automated worm (WannaCry-style) |
| Protect | Antivirus + firewall block malware & bad traffic | A 'PC cleaner' pop-up installs the very malware it claims to remove |
| Back up | Recoverable copies survive ransomware/theft | Thesis files gone when a stolen laptop had the only copy |
| Contain | Limits damage when one layer fails | One phished password unlocks everything because nothing was segmented |

*ℹ️ No single layer is enough. Posture is the WHOLE stack — and the cheapest win is usually the layer you've been ignoring.*


#### Concept 2 — Updates & Patching `[THEORY]` `[~6 min]`

[SLIDE] **A patch closes a door attackers already have the key to**

> **Deliver:** Define it. **A patch fixes a known security hole that attackers already know about.**
> Once a patch is **public**, the hole it fixes is **public too** — so unpatched machines become
> **easy, known targets.** The habit: **turn on automatic updates** for **OS + browser + apps.** Then
> the trap: **end-of-life software** (e.g. **Windows 7**) **never gets fixed again** — every hole found
> after that stays open forever. And most updates are **security fixes, not new features**, so 'later'
> means 'exposed until later'.

- 🇳🇵 **Local example:** **pirated/cracked Windows** is common in Nepal and often **can't update
  safely** — and frequently **ships with bundled malware** from the crack itself.

> ❌ **Common misconception:** *"Updates are just annoying new features I can skip."*
> ✅ **Correction:** "**Most updates are security fixes** for holes attackers already know about — 'skip'
> means 'stay exposed'. And **end-of-life software is not merely old; it's permanently unpatchable**, so
> it only gets more dangerous."

> 🎙️ Speaker note: The pirated-Windows point lands hard here — a cracked OS that can't patch is a
> **permanently open door**, often compromised from day one.

**📊 Depth table — Patch or not? — real Nepali habits and their verdict**

| Habit / situation | Verdict | Why (consequence) |
|---|---|---|
| Auto-updates ON for Windows + Chrome | Safe | Holes close automatically before attackers arrive |
| 'Remind me later' clicked for weeks | Weak | Every known hole stays open the whole time |
| Pirated/cracked Windows that can't update | Dangerous | No safe patches + often ships bundled malware |
| Still running Windows 7 / an old Android | Dangerous | End-of-life: new holes are never fixed again |
| Ignoring app updates ('just new features') | Weak | Most updates are security fixes, not cosmetics |
| Updating the OS but never the router firmware | Weak | The router is a computer too — it has holes as well |

*ℹ️ Pirated/cracked software is common in Nepal and is the worst case: it usually cannot patch safely AND arrives with malware pre-installed.*


#### Concept 3 — Antivirus / Anti-Malware `[THEORY]` `[~6 min]`

[SLIDE] **One good, updated AV beats three fighting each other**

> **Deliver:** Define it. **Antivirus (anti-malware) is software that detects and blocks malicious
> files and behaviour.** For most home users, **Windows Defender is built in, free, and fine.** Explain
> the mechanics: **real-time scanning** (as files arrive) plus **on-demand scans**; and **signature
> detection** (known malware) plus **behaviour detection** (new threats acting suspiciously). Then the
> two rules students get wrong: **one good, updated AV is enough**, and **running two real-time AVs at
> once causes conflicts and slowdowns**, not extra safety.

- 🇳🇵 **Mini case (work it, ≈2 min):** a **free 'PC cleaner' from a pop-up IS the malware.** Ask "what
  gave it away?" Draw out the tells: **unsolicited pop-up**, **manufactured urgency**, and **'pay to fix
  5 viruses.'**

> ❌ **Common misconception:** *"I need to buy 3 antiviruses to be really safe."*
> ✅ **Correction:** "**One good, updated AV is enough**; multiple real-time scanners **conflict, slow
> the machine, and can miss threats while fighting each other.** More antivirus is **more problems**, not
> more security."

> 🎙️ Speaker note: The scareware pop-up is the teachable moment — real protection is **quiet and already
> installed**; the thing that **found you and rushed you for money** is the threat.

**📊 Depth table — Real antivirus / malware situations — spot the trap**

| Situation | Verdict | Why (the tell) |
|---|---|---|
| Windows Defender on, kept updated | Safe | One good real-time AV is enough for most users |
| Pop-up: 'Your PC has 5 viruses — pay to fix!' | Scam / malware | Unsolicited + urgency + pay-now = the malware itself |
| A free 'PC cleaner' from a random pop-up | Dangerous | Installs the threat it claims to remove |
| Installing 3 antiviruses 'to be extra safe' | Weak | They conflict and slow the PC — no extra safety |
| Cracked 'premium' AV from a torrent | Dangerous | Cracks commonly carry trojans |
| Ignoring AV alerts to keep working | Weak | Dismisses the one warning you actually got |

*ℹ️ The strongest tell of fake-AV/scareware: it found you (a pop-up), rushes you, and asks for money. Real protection is quiet and already installed.*


#### Concept 4 — Backups: the 3-2-1 Rule `[THEORY]` `[~8 min]`

[SLIDE] **3 copies · 2 media · 1 offsite**

> **Deliver:** Define it. **A backup is a recoverable copy of your important data.** Teach the rule to
> memorise: **3 copies, on 2 different media types, with 1 kept offsite (or in the cloud)** — plus a
> **tested restore.** Walk what each part defeats: **ransomware, theft, and disk failure** are all
> beaten by **one clean, recent backup you can restore from.** Warn: **a backup you have never
> test-restored is a hope, not a backup.**

- 🇳🇵 **Local example:** **load-shedding surges and cheap drives fail often in Nepal**, and a **stolen
  laptop in a tempo** takes everything with it. The **offsite/cloud copy** is what survives all three.
- 🍿 **Fun analogy (deliver it):** "A backup is a **spare house key with a trusted neighbour** — useless
  until the day you're **locked out**, and then it's **everything.**"

> ❌ **Common misconception:** *"Deleting files or having them on my laptop is basically a backup."*
> ✅ **Correction:** "**One copy on one device is ZERO backups** — theft, ransomware, or a dead disk
> wipes it out at once. A real backup is **separate, on different media, and offsite**, so no single
> event can reach all copies."

> 🖼️ Visual: the **3-2-1 illustration** — 3 copies · 2 media types · 1 offsite/cloud.

> 🎙️ Speaker note: Anchor on the thesis-day case. A **3-2-1 setup** (laptop + external drive + cloud)
> would have made ransomware a **shrug, not a catastrophe.**

**📊 Depth table — What each part of 3-2-1 defeats**

| 3-2-1 element | What it protects against | Nepal example |
|---|---|---|
| 3 copies | Any single copy being lost or corrupted | A file deleted or a drive that silently corrupts it |
| 2 media types | One type of hardware failing | A cheap external drive that dies after a year |
| 1 offsite / cloud | Theft, fire, or a whole-room disaster | Laptop snatched in a tempo — cloud copy survives |
| A tested restore | A backup that turns out to be broken | Discovering on thesis day that the backup was empty |

*ℹ️ Each part defeats a different disaster. Ransomware, theft, disk failure, and a load-shedding surge are ALL beaten by one recent, tested, offsite copy.*


#### Concept 5 — Firewall Basics `[THEORY]` `[~6 min]`

[SLIDE] **One wall of the castle, not the whole castle**

> **Deliver:** Define it. **A firewall is a filter that controls which network traffic is allowed in and
> out.** Two kinds: a **host firewall** on your OS (protects the one device) and a **router firewall** at
> your home gateway (protects the whole home). The safe default is **'deny incoming by default'** —
> unrequested connections blocked unless you allow them — and **don't blindly click 'Allow'** on every
> prompt; allow only apps you **actually trust and expect.**

- 🇳🇵 **Local example:** your home has **two firewalls** — the one in **Windows/Mac** and the one in your
  **WorldLink/Vianet router.** But if the router still uses the **sticker admin password**, that gateway
  firewall is **wide open** regardless.

> ❌ **Common misconception:** *"A firewall makes me unhackable."*
> ✅ **Correction:** "It's **one wall, not the whole castle.** A firewall blocks unrequested connections,
> but it **can't stop malware you download, a phishing site you log into, or a scam call that talks you
> out of your OTP.** It complements the other layers; it doesn't replace them."

> 🎙️ Speaker note: Bust the 'firewall = unhackable' myth. It **filters connections**; it does nothing
> against an **invited** threat (a download, a phished login).

**📊 Depth table — Firewall decisions — allow or deny?**

| Prompt / situation | Right move | Why |
|---|---|---|
| Windows Defender Firewall is ON by default | Keep it on | Blocks unrequested incoming connections |
| Unknown app asks to accept incoming connections | Deny | If you didn't expect it, don't allow it |
| Your known game/app needs a port to play online | Allow (that app) | Trusted, expected — allow narrowly |
| A pop-up says 'disable firewall to speed up PC' | Ignore | No legitimate fix requires turning off the firewall |
| Router admin panel on default password | Change it | An open gateway firewall is no firewall |
| Assuming the firewall stops all malware | Wrong belief | It filters traffic; it can't stop a phished login |

*ℹ️ A firewall controls connections; it does NOT stop malware you download or a password you hand over. It is one layer of the posture, not the whole thing.*


#### 🛠 ACTIVITY — "Where is your only copy?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **The one file you'd be devastated to lose**

> **Run it:** In pairs (2 min), each student names the **ONE file** they'd be devastated to lose
> (thesis, project, photos) and says **exactly where its only copy lives right now** and **what happens
> if that device dies tonight.** Take **3–4 answers aloud** (3 min) and place each on the **3-2-1 rule**
> — how many copies, how many media, any offsite? Close: **each student agrees one concrete backup to
> set up this week.**

> 🎙️ Speaker note: Most will admit the only copy is on **one laptop or phone.** Push them to convert
> "it's on my laptop" into a real **3-2-1 plan** — a **cloud copy is the single biggest upgrade.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The best defence against ransomware locking your files is:
a) a faster antivirus  b) ✅ **recent offline/cloud backups (3-2-1)**  c) a longer password  d) a new laptop

**MCQ 2.** Running two real-time antivirus programs at once usually:
a) doubles safety  b) ✅ **causes conflicts/slowdowns with no extra safety**  c) is required  d) speeds the PC up

**Discussion prompt:** *Right now, where is the only copy of your most important file — and what if that device dies?*

> 🎙️ Speaker note: Draw out the **four-layer posture** and the **3-2-1 rule.** Both MCQ traps ('more AV
> = safer', 'pay to unlock') are the exact misconceptions students hold.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** this is **your own laptop, your own thesis, your own banking session.** A
**10-minute self-audit** this week — **auto-updates on, Defender confirmed, one cloud backup, firewall
on** — is the **cheapest insurance you will ever buy**, and it is the single most likely thing between
you and a lost semester.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Security posture = patch + protect + back up + contain**; most attacks are **automated** and hit **whoever is unpatched.**
2. Turn on **automatic updates**, drop **end-of-life/pirated** software; run **one good, updated antivirus** (Defender is fine).
3. Keep **3-2-1 backups** (3 copies · 2 media · 1 offsite) and leave your **firewall on** with **deny-by-default.**

**Next session (S29):** the device in your pocket and the gadgets in your home — **mobile & IoT security.**

---
---

# S29 — Mobile Devices & Internet of Things (IoT)
**Lecture hour 2 of 5 (Unit 6) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Why does a flashlight need to read your texts?"**

> **Deliver (≈2 min):** Two hooks. "A **free torch app** asks for your **contacts, microphone, location,
> and SMS** — **why does a flashlight need to read your texts?**" And: "Your **neighbour's CCTV** still
> uses **'admin/admin'** — **anyone on the internet can watch their living room.**"
>
> **Run it (≈3 min):** Land the theme — **mobile and IoT are where most of us are weakest.** Agenda:
> **app permissions → securing the phone → mobile banking/wallet safety → IoT risks.**

> 🎙️ Speaker note: These two hooks (over-broad permissions and default-password IoT) frame the whole
> session. Keep both on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Mobile App Permissions `[THEORY]` `[~8 min]`

[SLIDE] **Least privilege — a torch needs no SMS**

> **Deliver:** Define it. **A permission is the access — camera, mic, location, SMS, contacts, storage —
> an app requests.** The principle is **least privilege: grant only what the app's actual function
> needs.** Teach the mechanics: prefer **'while using the app'** over **'always'**; **review and revoke**
> in **Settings → Apps → Permissions**; **match the permission to the function** — a map needs location,
> a chat app needs the mic, a flashlight needs **neither.**

- 🇳🇵 **Local example:** **fake/cloned 'loan' and 'eSewa/Khalti' apps** on Nepali phones demand **SMS
  access** — precisely to **read your OTP SMS and harvest contacts**, then **harass you (and your
  contacts) for 'repayment.'** The permission request **is** the attack.

> ❌ **Common misconception:** *"If it's on the Play Store, it must be safe."*
> ✅ **Correction:** "**Malicious and cloned apps slip through store review regularly.** Check the
> **developer name, review quality, and install count** — and above all, **judge the permissions**: an
> app asking for far more than its function needs is the warning, store or not."

> 🎙️ Speaker note: Anchor on the fake-loan/OTP-stealer apps — they demand SMS + contacts to **intercept
> OTPs** and **harass for repayment.** That's the whole business model.

**📊 Depth table — Does this app really need it? — permission red flags**

| App asks for… | Reasonable? | Why (Nepal / IT) |
|---|---|---|
| Torch app → SMS + contacts + location | No | A flashlight needs none of these — data grab |
| Map app → location while using | Yes | Core to its function; 'while using' limits it |
| Fake 'loan' app → SMS + contacts | No | Reads your OTPs and harasses contacts for repayment |
| Camera app → camera + mic | Yes | Needed to record video with sound |
| Cloned 'eSewa' app → SMS + accessibility | No | Steals OTPs and can control the screen |
| Game → contacts + call logs | No | Unrelated to gameplay — revoke it |

*ℹ️ The test is function-fit: does the app's real job require this access? Fake loan and cloned-wallet apps demand SMS specifically to intercept your OTPs.*


#### Concept 2 — Securing the Phone Itself `[THEORY]` `[~7 min]`

[SLIDE] **It's a bank and an OTP inbox — lock it, update it, wipe it**

> **Deliver:** Frame it. **Your phone is a computer holding your money, identity, and OTPs — secure it
> like one.** The essentials: **screen lock + biometrics**, a **short auto-lock timeout**, **OS + app
> updates**, **install only from official stores**, and enable **'Find My Device' / remote wipe.**
> **Avoid sideloading APKs** shared on Facebook groups/Messenger.

- 🇳🇵 **Local example:** **cheap Android phones in Nepal that stop getting updates after a year** — and
  the habit of **installing APKs shared on Facebook/Messenger.**
- 🇳🇵 **Mini case (work it):** a **'Dashain offer — win an iPhone!'** link asks you to install an
  **APK.** What happens next? Draw it out — a **banking trojan** that **reads your OTP SMS** and drains
  the wallet.

> ❌ **Common misconception:** *"iPhones can't get hacked, so I don't need to worry."*
> ✅ **Correction:** "**Less-common is not immune** — phishing, account theft, and malicious profiles hit
> **any platform.** Security is about your **habits** (locks, updates, official stores, remote wipe), not
> a **brand badge.**"

> 🎙️ Speaker note: The APK-from-Messenger route is the most common local malware path. Cheap phones that
> stop updating after a year make it worse — the holes never close.

**📊 Depth table — Phone-hardening habits — strong vs weak**

| Habit | Verdict | Why (consequence) |
|---|---|---|
| Biometric lock + 30-sec auto-lock | Strong | A lost phone stays locked to a thief |
| No lock 'because it's faster' | Weak | Anyone who grabs it owns your accounts + OTPs |
| Installing a 'Dashain offer' APK from Messenger | Dangerous | Banking trojans arrive exactly this way |
| Apps only from the official store | Strong | Far lower chance of malware |
| Cheap phone that stopped updating a year ago | Weak | Unpatched holes never get fixed |
| 'Find My Device' + remote wipe enabled | Strong | Locate or erase a lost/stolen phone remotely |

*ℹ️ A phone is a bank, an ID, and an OTP inbox in your pocket. Sideloaded APKs and no screen lock are the two habits that most often end in account takeover.*


#### Concept 3 — Mobile Banking & Wallet Safety `[THEORY]` `[EXAMPLE]` `[~8 min]`

[SLIDE] **eSewa/Khalti/banks NEVER ask for your OTP**

> **Deliver:** Mobile-money is a top target in Nepal, so **guard the keys.** The habits: an
> **app-specific PIN**, **NEVER share your OTP or MPIN**, **beware SIM-swap**, **log out on shared
> devices**, and **watch URLs** (esewa.com.np vs lookalikes). The core rule students must memorise:
> **eSewa, Khalti, and banks NEVER ask for your OTP or MPIN.** Explain **SIM-swap**: an attacker **ports
> your number to their SIM** to receive your OTPs.

- 🇳🇵 **Local example:** the scam call — **"I'm from eSewa/your bank, tell me the OTP to reverse a wrong
  transfer."** Sharing the OTP **doesn't reverse anything**; it **authorises THEIR transfer** out of
  your wallet.

> ❌ **Common misconception:** *"Telling the OTP is fine if they already know my name/number."*
> ✅ **Correction:** "An **OTP is the LAST key** — sharing it **hands over your money** regardless of what
> else the caller knows. Scammers buy or guess names and numbers **precisely to sound legit**; the one
> thing they still need is the **OTP you must never give.**"

> 🖼️ Visual: an **anatomy-of-an-OTP-scam** flow — fake authority → panic story → 'read me the OTP' →
> money gone — with the **red flags** (unsolicited · urgency · asks for OTP) labelled.

> 🎙️ Speaker note: Read the scam script aloud. The three red flags — **unsolicited, urgency, asks for
> OTP** — appear in almost every case; teach them as a reflex.

**📊 Depth table — OTP / wallet scams — spot the red flag and respond**

| Scenario (Nepal) | Red flag | Correct response |
|---|---|---|
| Call: 'I'm from eSewa, read the OTP to reverse a wrong transfer' | Asks for OTP + urgency | Refuse and hang up — they never ask for OTP |
| SMS link: 'Verify your Khalti account now or it's blocked' | Threat + unknown link | Don't click; open the app directly |
| Caller already knows your name and number | Feels 'legit' | Knowing your name is not proof — still refuse the OTP |
| Site 'esewa-rewards.com' asks you to log in | Lookalike domain | Only trust esewa.com.np / the official app |
| Your number suddenly loses signal, then OTPs stop | Possible SIM-swap | Contact your telco/bank immediately |
| Login saved on a cyber-café PC | Shared device | Log out; never save credentials there |

*ℹ️ One rule covers most of these: a real bank/wallet NEVER asks for your OTP or MPIN. Unsolicited + urgency + asks-for-OTP = scam, every time.*


#### Concept 4 — Internet of Things (IoT) Risks `[THEORY]` `[EXAMPLE]` `[~8 min]`

[SLIDE] **A default password = the builder's master key still works**

> **Deliver:** Define it. **IoT devices are everyday things with internet connectivity** — **IP/CCTV
> cameras, smart bulbs, smart TVs, routers, smartwatches.** Teach why they're weak: they ship with
> **default passwords**, get **few or no updates**, are **always-on**, and are usually **unmonitored** —
> which makes them **easy bots.** Give the landmark case: the **Mirai botnet enslaved millions of IoT
> devices using default passwords alone.**

- 🇳🇵 **Local example:** **home/shop IP/CCTV cameras in Kathmandu** left on **default logins** and
  **exposed online**; **ISP routers (WorldLink/Vianet)** kept on the **sticker admin password.**
- 🇳🇵 **Mini case (work it):** a **baby monitor / CCTV streams to the open internet** because nobody
  changed the password — **what could a stranger do?** (watch the feed; enslave the device into a
  botnet).
- 🍿 **Fun analogy (deliver it):** "An IoT device on its **default password** is a **house where the
  builder's master key still opens the front door.**"

> ❌ **Common misconception:** *"An IoT gadget is too small/dumb to be a security problem."*
> ✅ **Correction:** "Its **size doesn't matter** — it's **always-on, reachable, and enslavable.** Mirai
> proved it at the **scale of millions.**"

> 🖼️ Visual: an **IoT home map** (router, CCTV, TV, bulb, phone) flagged with **default-password
> warnings.**

> 🎙️ Speaker note: The single highest-value action is **changing the default password on every IoT
> device.** Segregating IoT onto a **guest network** (S31) is the follow-up.

**📊 Depth table — Why IoT devices are easy targets — and the fix**

| IoT weakness | Why it's dangerous | The fix |
|---|---|---|
| Default password (admin/admin) | Anyone online can just log in | Change it on first setup |
| Rare or no firmware updates | Known holes stay open for years | Update firmware; retire unsupported devices |
| Always-on, unmonitored | Misuse goes unnoticed for months | Put IoT on a separate guest network |
| Exposed directly to the internet | Scanners find it in minutes | Don't port-forward cameras; use the vendor app |
| Weak/no encryption | Traffic and feeds can be intercepted | Prefer devices with proper security |

*ℹ️ Mirai enslaved millions of devices using default passwords alone. The single highest-value action is changing the default password on every IoT device you own.*


#### 🛠 ACTIVITY — "Open your permission settings now" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Name one app with access it doesn't need**

> **Run it:** Right now (2 min), students open **Settings → Apps → Permissions** on their own phone and
> find **one app with access it doesn't actually need**, plus **one home device (router/CCTV)** — is it
> still on a **default password?** Share **3–4 examples aloud** (3 min); name the **permission to revoke**
> and the **password to change.** Close: **revoke 2 permissions and change 1 default password this
> week.**

> 🎙️ Speaker note: Students almost always find a **game or torch** with contacts/location access and a
> **router on the sticker password.** Reward **do-it-now** changes over intentions.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A flashlight app requesting SMS + contacts access is a sign of:
a) a good feature  b) ✅ **over-broad / suspicious permissions**  c) faster performance  d) nothing

**MCQ 2.** A caller claiming to be from your bank asks for the OTP to "fix" a transfer. You should:
a) share it to help  b) ✅ **refuse and hang up — banks never ask for OTP**  c) share half of it  d) call back and share

**Discussion prompt:** *Open your phone's permission settings now — name one app with access it doesn't actually need.*

> 🎙️ Speaker note: The two MCQs target the two highest-impact habits — **least-privilege permissions**
> and **never sharing an OTP.** Reinforce the **IoT default-password** point in discussion.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** the device in your pocket holds your **money, your OTPs, and your identity**,
and the gadgets in your home are **doors onto your network.** A **ten-minute permission-and-password
sweep** this week — revoke over-broad permissions, enable remote wipe, change one IoT default password —
closes the gaps **most Nepali users leave wide open.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Grant **least-privilege permissions** — a flashlight needs neither your SMS nor contacts; **an app store is not proof of safety.**
2. **Lock, update, and official-stores-only** your phone; **enable remote wipe**; never **sideload APKs** from social media.
3. **Never share your OTP/MPIN** (banks never ask), and **change the default password on every IoT device** — Mirai proves why.

**Next session (S30):** the physical world — **theft, prying eyes, and what you throw away.**

---
---

# S30 — Enhancing Physical Security
**Lecture hour 3 of 5 (Unit 6) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **The cheapest hack is often physical**

> **Deliver (≈2 min):** "Your password can be **20 characters long** — and **useless** if someone
> **watches you type it on the bus**, or **buys your old phone with your photos still on it.**"
>
> **Run it (≈3 min):** Land the theme — **the cheapest hack is often physical, not digital.** Agenda:
> **theft & loss → shoulder-surfing → secure disposal → screen locks & access control.**

> 🎙️ Speaker note: The point is that **digital defences fail if the physical layer is ignored** — a
> perfect password doesn't help if the device is unlocked or watched.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Device Theft & Loss `[THEORY]` `[~7 min]`

[SLIDE] **A lost unlocked device is a data breach, not lost hardware**

> **Deliver:** Frame it. **Losing a phone or laptop physically means losing everything logged in on
> it.** The defences: **full-disk encryption** (**BitLocker / FileVault**; on by default on modern
> Android & iOS), a **strong screen lock**, **remote-find/remote-wipe** enabled, and **not leaving
> devices unattended.** Encryption makes stored data **unreadable without your key** — theft yields a
> **brick, not your files.**

- 🇳🇵 **Local example:** **phone/laptop snatching** in crowded **micros, tempos, and cafés around
  Thamel/New Road.** Walk the **attack chain**: a **stolen phone still logged into eSewa/Facebook/Gmail**
  → the thief **resets passwords, reads OTP SMS, empties the wallet** → **account takeover**, not just
  lost hardware.

> ❌ **Common misconception:** *"They'll just sell the hardware — my data is safe."*
> ✅ **Correction:** "An **unlocked or unencrypted device exposes your accounts, OTP SMS, and saved
> passwords instantly.** The **resale value of the phone is trivial** next to the **eSewa balance and
> identity** sitting unlocked inside it."

> 🖼️ Visual: a **stolen-unlocked-phone attack chain** (theft → still-logged-in apps → OTP SMS visible →
> account takeover).

> 🎙️ Speaker note: Repeat the line — the **hardware is cheap; the logged-in accounts are not.**
> Encryption + lock + remote wipe turn a **theft into an inconvenience.**

**📊 Depth table — Stolen device — encrypted/locked vs not**

| Situation | Outcome | Why |
|---|---|---|
| Encrypted + locked phone snatched in a tempo | Thief gets a brick | Data unreadable; remote-wipe finishes it |
| Unlocked phone still in eSewa + Gmail | Account takeover | Thief resets passwords and drains the wallet |
| Laptop with no disk encryption stolen | Full data breach | Files readable by pulling the drive |
| Remote-wipe enabled on a lost phone | Data erased remotely | You cut off access once it's gone |
| Device left unattended on a café table | Opportunistic theft | Most loss is convenience, not a targeted heist |
| OTP SMS visible on the lock screen | Extra exposure | Thief reads reset codes without unlocking |

*ℹ️ The hardware is cheap to replace; the logged-in accounts are not. Encryption + lock + remote wipe turn a theft into an inconvenience instead of a breach.*


#### Concept 2 — Shoulder-Surfing & Visual Exposure `[THEORY]` `[~6 min]`

[SLIDE] **The lowest-effort attack is just watching you type**

> **Deliver:** Define it. **Shoulder-surfing is someone watching your screen or keystrokes to steal a
> PIN or information.** Defend by **shielding the keypad**, using a **privacy screen protector**,
> **sitting with your back to a wall**, and being **wary of ATM/POS camera overlays and strangers
> 'helping'** at the machine. It needs **no malware and no skill — just line of sight.**

- 🇳🇵 **Local example:** **shoulder-surfing PINs at ATMs** and **while entering an eSewa/MPIN in a shared
  room or cyber café.**
- 🇳🇵 **Mini case (work it):** a **stranger at the ATM offers to 'help' the queue move faster and stands
  close** — what's the risk? (watches your PIN; may swap or grab your card).

> ❌ **Common misconception:** *"No one bothers to watch what I type."*
> ✅ **Correction:** "Shoulder-surfing is the **lowest-effort attack there is** — no malware, just eyes or
> a hidden camera. It's common **exactly because people assume no one is looking**; shielding the keypad
> **costs nothing** and defeats it."

> 🎙️ Speaker note: The **helpful stranger** and the **ATM camera overlay** are the two vivid cases. Push
> the reflex: **cover the keypad, every time.**

**📊 Depth table — Shoulder-surfing situations — risk and defence**

| Situation (Nepal) | Risk | Defence |
|---|---|---|
| Typing an ATM PIN in a busy queue | Someone/ a camera sees it | Cover the keypad with your hand |
| Stranger 'helps' you at the ATM, stands close | Watches PIN / swaps card | Decline help; keep your distance |
| Entering MPIN on a bus / micro | Seatmate reads it | Angle the screen; shield entry |
| Working on a laptop in a café | Screen visible behind you | Sit back-to-wall; privacy filter |
| Camera overlay/skimmer on an ATM slot | PIN + card captured | Check the slot; use trusted ATMs |
| Entering a password in a shared room | Roommate sees keystrokes | Shield; use a password manager autofill |

*ℹ️ These attacks need no malware and no skill — just line of sight. Shielding the keypad and a privacy filter defeat almost all of them.*


#### Concept 3 — Secure Disposal & Resale `[THEORY]` `[~7 min]`

[SLIDE] **Delete ≠ erased — encrypt-then-wipe before you sell**

> **Deliver:** Define it. **Secure disposal means making data unrecoverable before you sell, donate, or
> discard a device.** Teach the key correction: a **factory reset alone is not always enough.** The
> process: **sign out of all accounts first**, **remove the SIM/SD card**, **encrypt-then-wipe**, and
> **physically destroy dead drives.** With encryption on, a wipe leaves **only unreadable ciphertext.**

- 🇳🇵 **Local example:** the **second-hand phone/laptop market** (**Hattisar, online resale groups**)
  where **buyers recover the seller's photos and logins** from a careless wipe.

> ❌ **Common misconception:** *"Deleting files / formatting the disk erases them."*
> ✅ **Correction:** "**Deleted data is usually recoverable until it's overwritten** — delete and
> quick-format only remove the **pointer, not the content.** Reliable erasure means **encryption-then-wipe**,
> or **physically destroying** a drive that can't be wiped."

> 🖼️ Visual: a **delete vs format vs factory-reset vs encrypt-then-wipe** recoverability bar.

> 🎙️ Speaker note: Land the resale angle — signing out + encrypt-then-wipe is the difference between
> **selling a phone and selling your identity with it.**

**📊 Depth table — Delete vs format vs factory reset vs encrypt-then-wipe**

| Method | How recoverable? | Safe to sell after? |
|---|---|---|
| Delete / recycle bin | Fully recoverable | No — data is still there |
| Quick format | Mostly recoverable | No — easily undeleted |
| Factory reset (unencrypted) | Often recoverable | Risky — traces may remain |
| Encrypt, then wipe | Unrecoverable | Yes — only ciphertext left |
| Physically destroy the drive | Unrecoverable | Yes — for dead/failed drives |

*ℹ️ Deleting or formatting only removes the 'index'; the data stays until overwritten. Encryption-then-wipe (or destruction) is the reliable erase before resale.*


#### Concept 4 — Screen Locks & Access Control `[THEORY]` `[~6 min]`

[SLIDE] **A short auto-lock + hidden OTP previews**

> **Deliver:** Define it. **Access control is what stands between a person holding your device and your
> data.** The habits: a **PIN/password/biometric**, a **short auto-lock timeout**, **lock on walk-away**
> (**Win+L**), and **disable lock-screen notification previews** that leak **OTPs and messages.** A **PIN
> or biometric is far stronger than a pattern** — patterns are **guessable and smudge-readable.**

- 🇳🇵 **Local example:** a **laptop left unlocked at a café** for two minutes, or a **phone showing your
  bank OTP on its lock screen** — both hand over access with **no hacking at all.**

> ❌ **Common misconception:** *"A pattern lock is plenty."*
> ✅ **Correction:** "Common patterns (**L, Z, box**) are easy to guess and **readable from the smudge
> trail** on the screen; a **PIN or biometric is markedly stronger.** And **any lock is undone if OTPs
> are previewed** on the lock screen — **hide previews too.**"

> 🍿 **Fun analogy (deliver it):** "Leaving a device unlocked is **leaving your house with the door open
> AND a sign saying which room the cash is in.**"

> 🎙️ Speaker note: The **notification-preview leak** is the underrated one — OTPs visible on a locked
> screen **defeat the lock.** Short timeout + hidden previews close both gaps.

**📊 Depth table — Access-control habits — strong vs weak**

| Habit | Verdict | Why |
|---|---|---|
| 6-digit PIN / biometric + 30-sec auto-lock | Strong | Fast for you, hard for a thief |
| Simple pattern lock (L or Z shape) | Weak | Guessable + readable from screen smudges |
| No auto-lock, screen stays on | Weak | A set-down device is wide open |
| Lock on walk-away (Win+L) | Strong | No unattended open session |
| OTP/message previews shown on lock screen | Weak | Codes readable without unlocking |
| Previews hidden until unlocked | Strong | OTPs and messages stay private |

*ℹ️ A lock you never trigger (no auto-lock) protects nothing, and previews that show OTPs defeat the lock entirely. Short timeout + hidden previews close both gaps.*


#### 🛠 ACTIVITY — "Where do you type a PIN in public?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Who could be watching — and what would a snatch expose?**

> **Run it:** In pairs (2 min): name **where you most often type a PIN/MPIN/password in public** — and
> **who could be watching.** Then trace **what a thief would get from your phone RIGHT NOW** if it were
> snatched unlocked. Take **3–4 answers aloud** (3 min); **separate 'lost hardware' from 'lost
> accounts.'** Close: **each student names one fix** — encryption, auto-lock, hidden previews, or
> shielding the keypad.

> 🎙️ Speaker note: Draw out that the **accounts (eSewa, Gmail, Facebook) are the real loss**, not the
> device. Reward students who connect a **specific public habit** to a **specific fix.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Before selling your old phone you should FIRST:
a) just factory reset  b) ✅ **sign out of all accounts, then encrypt/reset & remove SIM/SD**  c) delete some files  d) nothing

**MCQ 2.** "A factory reset alone guarantees no one recovers my data" is:
a) true  b) ✅ **false — encrypt-then-wipe (or destroy the drive) is safer**  c) true for phones only  d) true if it's fast

**Discussion prompt:** *Where do you most often type a PIN/password in public, and who could be watching?*

> 🎙️ Speaker note: Both MCQs attack the **'delete = erased'** and **'reset = safe'** misconceptions. Tie
> back to the **theft chain** — physical loss becomes a **data breach** without encryption + lock.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** you carry your **bank, your ID, and your OTPs** in your pocket through
**crowded micros and cafés** every day. **Encryption, a short auto-lock, hidden previews, and a careful
wipe before resale** are the physical-layer habits that keep a **snatch or a sale from becoming a
breach.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. A **lost unencrypted/unlocked device is a data breach**, not just lost hardware — **encrypt, lock, and enable remote wipe.**
2. **Shoulder-surfing needs only line of sight** — **shield the keypad**, use a **privacy screen**, sit **back-to-wall.**
3. **Wipe properly before disposal** (encrypt-then-wipe, remove SIM/SD, sign out); **lock screens** and **hide OTP previews.**

**Next session (S31):** taking all this into the home office — **cybersecurity when working from home.**

---
---

# S31 — Cybersecurity When Working from Home
**Lecture hour 4 of 5 (Unit 6) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **Home is the office now — without the office's security**

> **Deliver (≈2 min):** Paint the scene. "You join an **office Zoom from your bedroom** on the **same
> Wi-Fi as your smart TV, your roommate's torrents, and a CCTV with a default password** — and you've
> **saved the company database to your Desktop 'just for now.'**"
>
> **Run it (≈3 min):** "**Where could this go wrong?**" Land the theme — **home is now the office, but
> without the office's security.** Agenda: **securing the home network → VPNs → separating work &
> personal → video-call safety.**

> 🎙️ Speaker note: Almost every student works or studies from home. Keep the bedroom-office scene on the
> board and return to each risk as you cover it.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Securing the Home Network `[THEORY]` `[~7 min]`

[SLIDE] **The router is the front gate — lock it, then split it**

> **Deliver:** Frame it. **Your router is the front gate of your digital home — secure it first.** The
> steps: **change the default admin password**, use **WPA2/WPA3 with a strong Wi-Fi passphrase**,
> **update the router firmware**, **disable WPS**, and set up a **guest network** for visitors and IoT.
> The router is a **computer with holes** that need patching too, and a **guest/IoT network keeps a
> hacked camera or a visitor's laptop off your work devices.**

- 🇳🇵 **Local example:** **WorldLink/Vianet/Subisu routers left on the sticker password**, and
  **shared-Wi-Fi buildings** where **everyone sees everyone's traffic.**

> ❌ **Common misconception:** *"My Wi-Fi has a password, so it's secure."*
> ✅ **Correction:** "A **weak passphrase, a default router admin login, or outdated firmware** still
> leave you exposed even with 'a password' set. Wi-Fi security is the **whole gate** — passphrase, admin
> login, firmware, and **segmentation** — not just one lock."

> 🖼️ Visual: a **home-network diagram** splitting a **MAIN network** from a **GUEST/IoT network.**

> 🎙️ Speaker note: The **guest-network split** is the pro move — connect it back to S29's IoT
> default-password lesson.

**📊 Depth table — Home-network setup — strong vs weak**

| Setting (Nepal) | Verdict | Why (consequence) |
|---|---|---|
| Router admin still on the sticker password | Weak | Anyone nearby/online can reconfigure it |
| WPA3 (or WPA2) + a long passphrase | Strong | Neighbours can't join or snoop your traffic |
| Open/'password123' Wi-Fi shared with the building | Weak | Everyone sees everyone's traffic |
| Firmware updated on the router | Strong | Known router holes get patched |
| WPS left enabled for convenience | Weak | WPS PIN can be brute-forced |
| Guest/IoT network separate from work devices | Strong | A hacked camera can't reach your laptop |

*ℹ️ 'My Wi-Fi has a password' is not enough — a weak passphrase, default admin login, or old firmware still leaves the gate open. Lock all three, then segment.*


#### Concept 2 — VPNs `[THEORY]` `[~6 min]`

[SLIDE] **Encrypts the tunnel — but protects transport only**

> **Deliver:** Define it. **A VPN (Virtual Private Network) encrypts your traffic through a secure
> tunnel.** Use a **company VPN** to reach **work resources**, and a **trusted VPN on public/untrusted
> Wi-Fi** to **stop local snooping.** Then the warning: **'free VPN' apps may sell your data** — the
> product being sold is **you.**

- 🇳🇵 **Local example:** working from a **café/co-working space in Kathmandu on open Wi-Fi** — anyone on
  that network can potentially **snoop your traffic**, and a VPN scrambles it so they see **only
  gibberish.**

> ❌ **Common misconception:** *"A VPN makes me anonymous and 100% safe."*
> ✅ **Correction:** "It **protects the transport** — it **won't save you from phishing, malware, a weak
> password, or a site you log into willingly.** And a **free VPN can be worse than none** if it sells
> your data. Use a **trusted** VPN, but keep **every other layer** too."

> 🎙️ Speaker note: The one-liner: **a VPN secures the pipe, not the person.** Essential on untrusted
> Wi-Fi; useless against a decision to hand over a password.

**📊 Depth table — VPN — when it helps and what it can't do**

| Situation | Does a VPN help? | Why |
|---|---|---|
| Working on open café Wi-Fi in Kathmandu | Yes | Encrypts traffic against local snooping |
| Reaching internal company systems from home | Yes (company VPN) | Secure tunnel into work resources |
| You click a phishing link and log in | No | VPN protects transport, not your decisions |
| You download and run malware | No | VPN doesn't scan or block files |
| Using a 'free' VPN of unknown origin | Risky | It may log and sell your traffic |
| Reusing a weak password over a VPN | No | The password is still weak — VPN can't fix that |

*ℹ️ A VPN secures the pipe, not the person. It's essential on untrusted Wi-Fi, but it won't save you from phishing, malware, or a weak/reused password.*


#### Concept 3 — Separating Work and Personal `[THEORY]` `[~6 min]`

[SLIDE] **'Just for now' on personal Gmail is a leak the company can't see**

> **Deliver:** Frame it. **Keep work and personal data and logins apart.** Use the **work-issued
> device/account** for work, **don't store company data on personal cloud/email/USB**, and **lock the
> machine when you step away — even at home.** Mixing work logins with personal accounts **spreads a
> breach from one into the other**, and company data on **personal Gmail/Drive is outside the company's
> control and protection.**

- 🇳🇵 **Mini case (work it):** you **email a work file to your personal Gmail** to finish it at night —
  **what risks did you just create?** (data leakage, **no company control**, **breach exposure** with no
  visibility).

> ❌ **Common misconception:** *"At home there's no one around, so I can relax security."*
> ✅ **Correction:** "**Flatmates, family, guests, insecure IoT, and remote attackers are all still in
> scope** — 'home' is **not** 'safe.' Lock the machine when you step away and keep **work on work
> systems**, exactly as you would in an office."

> 🎙️ Speaker note: Doing the work on the **issued device/account** keeps it inside the **protections
> built for it** — policy, backups, monitoring. 'Just for now' copies are exactly how home-work data
> leaks.

**📊 Depth table — Work/personal separation — risk vs safe practice**

| Action | Verdict | Why (consequence) |
|---|---|---|
| Emailing a company file to personal Gmail | Risky | Data leaves company control; breach exposure |
| Doing work on the work-issued device/account | Safe | Policy, backups, and monitoring apply |
| Saving the client database to your Desktop 'for now' | Risky | Uncontrolled copy on an unmanaged machine |
| Using a personal USB for work files | Risky | Easy to lose; may carry malware |
| Locking the laptop when you leave the room | Safe | Flatmates/family can't wander into work data |
| Same password for work and personal accounts | Risky | One breach cascades across both |

*ℹ️ At home there IS someone around — flatmates, family, guests, IoT, and remote attackers. 'Just for now' copies on personal accounts are exactly how home-work data leaks.*


#### Concept 4 — Video-Call & Collaboration Safety `[THEORY]` `[~6 min]`

[SLIDE] **An open link with no password is a public poster**

> **Deliver:** Frame it. **Video calls and shared links leak more than people think.** The habits:
> **require meeting passwords and waiting rooms** (Zoom/Meet/Teams), **don't post invite links
> publicly**, **mind what's visible/audible in your background**, and **beware screen-share leaks and
> fake meeting-invite phishing.** A **whole-screen share** shows your **notifications and open tabs**; a
> **sensitive document behind you** is broadcast to everyone.

- 🇳🇵 **Local example:** **'Zoom-bombing' of online classes** and **Tihar/Dashain virtual meetings** in
  Nepal during lockdown, when **links were shared openly** with **no password.**
- 🍿 **Fun analogy (deliver it):** "An **open meeting link with no password** is a **public event poster
  — anyone who finds it walks in.**"

> ❌ **Common misconception:** *"It's just a quick call — I don't need a password or to check my
> background/share."*
> ✅ **Correction:** "An **open link with no password is a public poster** anyone can walk into, and a
> **whole-screen share or a cluttered background leaks information silently.** Passwords, waiting rooms,
> and **sharing only one window** cost seconds."

> 🎙️ Speaker note: Two habits prevent most incidents — **password + waiting room on every meeting**, and
> **sharing only the one window** you intend (not the whole screen).

**📊 Depth table — Video-call safety — risk vs safe practice**

| Situation | Verdict | Why |
|---|---|---|
| Meeting link posted publicly on Facebook | Risky | Anyone can join — 'Zoom-bombing' |
| Meeting password + waiting room enabled | Safe | Only admitted, invited people get in |
| Screen-sharing with other tabs/notifications open | Risky | Leaks messages, emails, other data |
| Sensitive documents visible in your background | Risky | On-camera info leak |
| Clicking a 'meeting invite' from an unknown sender | Risky | Fake-invite phishing / malware |
| Blurred/neutral background + shared window only | Safe | Nothing extra leaks on camera or screen |

*ℹ️ Two habits prevent most incidents: password + waiting room on every meeting, and sharing only the one window you intend (not the whole screen).*


#### 🛠 ACTIVITY — "Weakest link on your Wi-Fi" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Which device would an attacker target?**

> **Run it:** In pairs (2 min): **list three devices on your home Wi-Fi right now** (phone, laptop, TV,
> CCTV, roommate's PC…) and decide **which is the weakest link** an attacker would target, and **why.**
> Take **3–4 answers aloud** (3 min); note **how many homes still have the router on its sticker
> password.** Close: **each student names one fix** — change router admin, make a guest network, or set
> meeting passwords.

> 🎙️ Speaker note: The weakest link is usually a **default-password IoT device** or the **router
> itself.** Reward connecting the weak device to the **guest-network fix** and the **S29 IoT lesson.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** On open café Wi-Fi, the best protection for work traffic is:
a) hoping no one looks  b) ✅ **a trusted / company VPN**  c) a longer password  d) airplane mode

**MCQ 2.** Emailing a company file to your personal Gmail to finish later is:
a) fine and efficient  b) ✅ **a data-leakage risk — avoid it**  c) required for backup  d) safe if you delete it after

**Discussion prompt:** *List three devices on your home Wi-Fi right now — which is the weakest link an attacker would target?*

> 🎙️ Speaker note: MCQ1 rewards the **VPN-on-untrusted-Wi-Fi** habit; MCQ2 the **work/personal
> separation** rule. Draw the **router-as-gate** and **guest-network** points out in discussion.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** **home is the office now, without the office's IT team.** The habits here — a
**locked, segmented router**, a **VPN on café Wi-Fi**, **work kept on work systems**, and
**password-protected calls** — are exactly what a **remote Nepali developer or BPO worker** needs to
**work safely and keep a client's trust** (echoing the outsourcing duties from Unit 4).

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Lock down the router** (the gate): change admin password, use **WPA2/WPA3**, update firmware, add a **guest/IoT network.**
2. Use a **trusted/company VPN** on untrusted networks — but it protects **transport only**, not against phishing or weak passwords.
3. Keep **work and personal separate**, and protect meetings with **passwords + waiting rooms** while minding your **background.**

**Next session (S32):** the keys to everything — **securing your accounts and passwords** (closes Unit 6).

---
---

# S32 — Securing Your Accounts & Passwords
**Lecture hour 5 of 5 (Unit 6) · 50 minutes — CLOSES UNIT 6**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **One password, and the whole row of dominoes falls**

> **Deliver (≈2 min):** "You **reuse one password** across **Facebook, Gmail, eSewa, and your college
> portal.** One of those sites gets **breached** — now attackers **try that same password everywhere**
> (it's called **credential stuffing**)."
>
> **Run it (≈3 min):** "**How many of your accounts just fell with one domino?**" Land the theme —
> **accounts are the real target; passwords are the lock.** Agenda: **strong passwords → password
> managers → MFA/2FA → breach awareness & response.**

> 🎙️ Speaker note: This session ties the whole unit together — the accounts hold the money and identity
> everything else protects. Keep the **domino** image on the board.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Strong Passwords `[THEORY]` `[~7 min]`

[SLIDE] **Length beats complexity**

> **Deliver:** Define it. **A strong password is long, unique, and hard to guess.** Teach the core rule:
> **length beats complexity** — a **passphrase** like **'hariyo!gai-khana-25'** beats **'P@ss123'.** Make
> **every account unique**, and **never** use **names, DOB, 'password', or '123456'.** A **memorable
> passphrase of a few unrelated words** is both **strong and usable.**

- 🇳🇵 **Local example:** **weak Nepali-common passwords** — **phone number, 'nepal123', favourite
  team/idol, DOB** — and the habit of **reusing one across all accounts.**

> ❌ **Common misconception:** *"Adding @ and a number makes a password strong."*
> ✅ **Correction:** "**Short-but-symbolic ('P@ss123') is still weak** — **length and uniqueness matter
> most.** A **long passphrase** of a few words beats a short cryptic one, and **no amount of symbols
> saves a password that's reused everywhere.**"

> 🖼️ Visual: a **password-strength ladder** (short/complex → long passphrase).

> 🎙️ Speaker note: Land both moves — **length beats complexity**, and **uniqueness beats everything.**
> Even a strong password becomes weak the moment it's reused.

**📊 Depth table — Weak vs strong passwords — why length wins**

| Password | Weak or strong? | Why |
|---|---|---|
| nepal123 / your phone number | Weak | Guessable, common, in every wordlist |
| P@ss123 (short + symbols) | Weak | Short — cracked in seconds despite symbols |
| Ram@2003 (name + DOB) | Weak | Personal info is easy to find/guess |
| Kathmandu@2026 | Medium | Better, but still short and guessable |
| hariyo!gai-khana-25 (passphrase) | Strong | Long + unique — huge search space |
| Same password reused everywhere | Weak | One breach topples every account |

*ℹ️ Length beats complexity, and uniqueness beats everything: a long passphrase is strong, but reusing even a strong password across sites makes it weak again.*


#### Concept 2 — Password Managers `[THEORY]` `[~7 min]`

[SLIDE] **How 'unique everywhere' becomes realistic**

> **Deliver:** Define it. **A password manager generates and stores a unique password for every site
> behind one master password.** You remember **one strong master password** (protected with **MFA**),
> and the manager **does the rest** — which is what makes **'unique everywhere' realistic.** Options:
> **Bitwarden, the built-in browser manager, or Google's** — pick one and use it **consistently.**

- 🇳🇵 **Mini case (work it):** "You have **60 accounts** — can a human realistically use **60 unique
  strong passwords** without a manager?" (No — **that's why people reuse.**)

> ❌ **Common misconception:** *"A password manager is a single point of failure / unsafe."*
> ✅ **Correction:** "A **well-secured manager** — a **strong master password plus MFA** — is **far safer
> than reusing one password** across every site and scribbling others on sticky notes. The **real
> comparison is manager vs reuse**, and the manager **wins decisively.**"

> 🎙️ Speaker note: Reframe the fear — it's not **'manager vs perfect memory'**, it's **'manager vs reuse
> and sticky notes.'** The manager is the safe, realistic option.

**📊 Depth table — Password manager — myth vs reality**

| Claim / situation | Verdict | Why |
|---|---|---|
| 'I can remember 60 unique strong passwords' | Unrealistic | No one can — which is why people reuse |
| Manager + strong master password + MFA | Strong | One secured vault beats reuse everywhere |
| Writing passwords on sticky notes / a notes app | Weak | Easily seen, lost, or synced insecurely |
| 'A manager is one single point of failure' | Overstated | A well-secured vault is far safer than reuse |
| Reusing one password to 'keep it simple' | Weak | One breach = credential stuffing everywhere |
| Letting the manager autofill on the real site | Strong | Also resists lookalike-phishing domains |

*ℹ️ The realistic choice isn't 'manager vs perfect memory' — it's 'manager vs reuse and sticky notes'. A strong master password + MFA makes the vault the safe option.*


#### Concept 3 — MFA / 2FA `[THEORY]` `[~8 min]`

[SLIDE] **A second key — and email comes first**

> **Deliver:** Define it. **MFA (multi-factor authentication) adds a second proof beyond your password —
> something you have or are.** Teach the **strength ladder**: **SMS OTP < authenticator app (TOTP) <
> hardware key.** Turn it on for **email, banking, and social first** — and note that **SMS-OTP is
> weakened by SIM-swap.** The crucial point: **enable MFA on email FIRST**, because **your email can
> reset every other account.**

- 🇳🇵 **Local example:** turning on **2FA for eSewa/Khalti, bank apps, Gmail, and Facebook** — and **why
  your email 2FA matters most** (it **resets everything else**).

> ❌ **Common misconception:** *"MFA is too much hassle for what it's worth."*
> ✅ **Correction:** "**MFA blocks the vast majority of account takeovers even when your password is
> stolen** — a **few seconds per login** against **losing your wallet and identity.** It's the single
> highest-value habit **after not reusing passwords.**"

> 🖼️ Visual: an **MFA factor pyramid** (SMS → authenticator app → hardware key).

> 🎙️ Speaker note: Prefer an **authenticator app over SMS** where offered — SMS OTP can be intercepted
> via **SIM-swap**, while a **TOTP app** generates codes **on your device with no SIM to hijack.**

**📊 Depth table — MFA factors — weakest to strongest**

| Factor | Strength | Trade-off |
|---|---|---|
| Password only | Weakest | One stolen secret = full access |
| SMS OTP | Better | Vulnerable to SIM-swap; still far better than none |
| Authenticator app (TOTP) | Strong | Codes on your device, no SIM-swap risk |
| Hardware security key | Strongest | Resists phishing; small cost/effort |
| MFA on email specifically | Highest priority | Email resets all other accounts — protect it first |

*ℹ️ Move up the ladder where you can (app over SMS), but any MFA beats none. Enable it on email first — it's the master key that resets everything else.*


#### Concept 4 — Breach Awareness & Response `[THEORY]` `[~7 min]`

[SLIDE] **One leaked reused password topples every account**

> **Deliver:** Define it. **Breach awareness is knowing when your credentials leak and acting fast.**
> Check **haveibeenpwned.com**; on a breach → **change that password everywhere it was reused**, **enable
> MFA**, and **watch for follow-on phishing** that uses your **real leaked details to seem legit.** This
> is why **reuse is so dangerous** — one leaked password is **tried everywhere (credential stuffing).**

- 🇳🇵 **Local example:** **leaked Nepali service/forum databases** circulating, followed by **targeted
  scam calls/SMS using your real details** to seem legit.
- 🍿 **Fun analogy (deliver it):** "Reusing one password is **using the same key for your house, car,
  office, and locker** — lose it once, **lose everything**; a **password manager gives every lock its own
  key.**"

> ❌ **Common misconception:** *"Reusing one password is fine if it's a strong one."*
> ✅ **Correction:** "Once **any one site leaks it**, attackers **replay it across all your accounts** —
> **credential stuffing** — so a **strong-but-reused password topples like a domino.** **Uniqueness** (via
> a manager) is what **contains a single leak to a single account.**"

> 🖼️ Visual: a **credential-stuffing domino** graphic (one leaked password topples Facebook, Gmail,
> eSewa, college portal).

> 🎙️ Speaker note: A breach is a **when, not an if.** Teach the response as a reflex: **change +
> de-reuse + MFA**, and **treat any 'official' follow-up that knows your details as likely phishing.**

**📊 Depth table — Breach response — right vs wrong moves**

| Situation | Right move | Why |
|---|---|---|
| Your email shows up on haveibeenpwned | Change that password + enable MFA | Assume the leaked password is now public |
| You reused that password on 5 sites | Change it on all 5 | Credential stuffing tries it everywhere |
| A scam SMS quotes your real name + last order | Treat as phishing; don't click | Leaked data makes scams look legit |
| Ignoring a breach notice 'it's probably nothing' | Wrong | The password is already circulating |
| Adding MFA after a breach | Right | Blocks takeover even with the leaked password |
| Using the same 'new' password again everywhere | Wrong | Re-creates the reuse vulnerability |

*ℹ️ A breach is a when, not an if. Fast response — change + de-reuse + MFA — plus scepticism toward follow-on phishing is what limits the damage.*


#### 🛠 ACTIVITY — "How many accounts share a password?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Which one breaking would hurt the most?**

> **Run it:** In pairs (2 min): honestly, **how many of your accounts share a password right now?**
> Identify **which account breaking would hurt the most** (usually your **primary email**) and **why.**
> Take **3–4 answers aloud** (3 min); connect **reuse** to the **credential-stuffing domino.** Close:
> **each student names their plan** — set up a manager, make email unique, and turn on **email MFA** this
> week.

> 🎙️ Speaker note: Most students **share one password widely** and **haven't protected email first.**
> Reward the realisation that **email is the master key** and that a **manager + MFA is the fix**, not
> more willpower.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The single most important account to protect with a strong password + MFA is usually:
a) a game account  b) ✅ **your primary email (it can reset all the others)**  c) a shopping app  d) a news site

**MCQ 2.** Reusing one password and having one site breached enables:
a) faster login  b) ✅ **credential stuffing across your other accounts**  c) stronger security  d) nothing

**Discussion prompt:** *How many of your accounts share a password right now — and which one breaking would hurt the most?*

> 🎙️ Speaker note: MCQ1 lands the **email-is-the-master-key** point; MCQ2 the **credential-stuffing**
> danger of reuse. Close the unit by tying **passwords → manager → MFA → breach response** together.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** your **accounts — email, eSewa, bank, Facebook — are the real prize**, and
**passwords are the lock.** Setting up a **manager**, making your **email password unique**, and turning
on **authenticator-app MFA** this week is the **highest-return hour of security work you can do.**

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. Use **long, unique passphrases per site** — **length beats complexity**, and **reuse is the real weakness.**
2. A **password manager** makes 'unique everywhere' realistic; **MFA (authenticator app > SMS)** stops most takeovers — **protect email first.**
3. **Assume breaches happen**: check **haveibeenpwned**, **change + de-reuse** the password, **enable MFA**, and **expect follow-on phishing.**

**End of Unit 6 — Next unit:** **Social Engineering & Cyber Terrorism** — how attackers target the **human**, not the machine.

---
---

# 📋 UNIT 6 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. Answer key at the end.*

### Section A — Multiple Choice (1 mark each)
1. "Security posture" means:
   a) how fast your PC is  b) ✅ how well your device+habits resist AND recover from threats  c) your antivirus brand  d) your Wi-Fi speed
2. The 3-2-1 backup rule is:
   a) 3 passwords  b) ✅ 3 copies · 2 media types · 1 offsite/cloud  c) 2 backups a day  d) 1 backup a year
3. The purpose of patching is:
   a) to add features  b) ✅ to close known security holes attackers exploit  c) to slow the PC  d) nothing useful
4. Running two real-time antivirus programs at once:
   a) doubles safety  b) ✅ causes conflicts/slowdowns with no extra safety  c) is required  d) speeds the PC up
5. A flashlight app requesting SMS + contacts access is:
   a) a good feature  b) ✅ over-broad / suspicious permissions  c) normal  d) faster performance
6. A caller claiming to be your bank asks for your OTP. You should:
   a) share it  b) ✅ refuse and hang up — banks never ask for OTP  c) share half  d) call back and share
7. The main IoT risk is:
   a) they use too much power  b) ✅ default passwords + no updates (enslaved by Mirai)  c) they're too fast  d) none
8. Before selling your old phone you should FIRST:
   a) just factory reset  b) ✅ sign out of all accounts, then encrypt-then-wipe & remove SIM/SD  c) delete a few files  d) nothing
9. On open café Wi-Fi, the best protection for work traffic is:
   a) hope no one looks  b) ✅ a trusted / company VPN  c) a longer password  d) airplane mode
10. Reusing one password and having one site breached enables:
    a) faster login  b) ✅ credential stuffing across your other accounts  c) stronger security  d) nothing
11. The account to protect with MFA first is:
    a) a game account  b) ✅ your primary email (it can reset all the others)  c) a shopping app  d) a news site

### Section B — Short Answer (2 marks each)
12. Explain the **3-2-1 backup rule** and what each part defeats.
13. List **three** things to check when auditing a phone.
14. Explain **why a factory reset is not always enough** before disposal.
15. Name the **MFA factor types from weakest to strongest.**
16. What is **credential stuffing**, and how do unique passwords stop it?

### Section C — Applied Case (3 marks each)
17. Given a **messy home setup** — default router password, no backups, reused passwords, IoT on default logins — write a **prioritised hardening plan.**
18. You receive a **"from eSewa" call asking for an OTP** and an **SMS link.** Identify the **red flags** and the **correct response.**

### Section D — Discussion (open-ended)
19. "**Are password managers safer or riskier than memorising passwords?**" Argue **both sides**, then take a **position.**

---

### ✅ Answer Key (Section A)
1-b · 2-b · 3-b · 4-b · 5-b · 6-b · 7-b · 8-b · 9-b · 10-b · 11-b

> **Sections B–D: grade on key terms.** Q12 must give 3 copies / 2 media / 1 offsite and note it defeats
> ransomware, theft, and disk failure (bonus: a tested restore). Q13 — any three of: screen lock +
> biometrics, auto-lock, OS updates, official-stores-only, remote wipe, revoke over-broad permissions.
> Q14 must note that deleted/reset data is often recoverable until overwritten, and that encrypt-then-wipe
> (or physical destruction) plus signing out and removing SIM/SD is safe. Q15 must give password-only <
> SMS OTP < authenticator app (TOTP) < hardware key (and email-first as the priority). Q16 must define
> replaying a leaked password across accounts and explain that unique passwords contain a leak to one
> account. Q17 — reward a PRIORITISED plan: change router admin + WPA2/3 + firmware + guest network; set
> up 3-2-1 backups; unique passwords via a manager + MFA (email first); change every IoT default password.
> Q18 — red flags: unsolicited call, urgency, asks for OTP, unknown/lookalike link; response: refuse,
> never share OTP/MPIN, don't click, open the app directly, report. Q19 — reward both-sides reasoning
> (single point of failure vs reuse-and-sticky-notes) and a clear position that a well-secured manager
> (strong master + MFA) beats reuse.

---

## ✅ Unit 6 complete (full lecturer-ready depth)
The deck is built: **IT246_Unit6.pptx** (92 slides) — diagram-rich, self-contained, and PDF-safe,
carrying all **21 §7A depth tables** (comparison, concrete-example, and scaffolding) and **10
diagrams** (posture layers, 3-2-1 backup, IoT home map, OTP-scam anatomy, theft attack-chain,
delete-vs-wipe recoverability, home-network split, password-strength ladder, MFA factor pyramid,
credential-stuffing domino). This Markdown source now carries those **same 21 depth tables inline**
under each concept, so the source of truth and the deck stay in sync.
