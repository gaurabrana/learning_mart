# Unit 6 — Personal Cybersecurity · Content Outline

**5 LHs → 5 sessions (S28–S32) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia (eSewa/Khalti/mobile banking safety, local Wi-Fi habits, scams targeting Nepali users, IoT in Nepali homes). Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 6 learning outcomes (what students can do after S28–S32)
1. Assess the security posture of their own home computer (updates, antivirus, backups, firewall) and fix the weak spots.
2. Harden their mobile phones and any IoT/smart-home devices against common threats (over-broad permissions, default passwords, insecure networks).
3. Apply physical-security habits that protect devices and data from theft, shoulder-surfing, and careless disposal.
4. Configure a safer work-from-home setup (segregated network, VPN, work/personal separation, safe video calls).
5. Secure their online accounts with strong unique passwords, a password manager, and MFA/2FA, and respond to a breach.

---

## S28 — Evaluating Your Cybersecurity Posture: Home Computer

**Hook:** "Your laptop has 47 pending updates, no backup, and an antivirus that expired in 2022 — but it 'feels fine.' If it died or got locked by ransomware tonight, what would you lose, and could you get it back?" → most personal security is just basic hygiene nobody does.

**Concepts & how each will be filled:**

1. **Security posture (what it means to "audit yourself")**
   - Definition: posture = the overall state of how well your device and habits resist/recover from threats.
   - Theory: think in layers — patch → protect → back up → contain. Risk = likelihood × impact; a single laptop holds your photos, college files, banking sessions.
   - Global example: WannaCry ransomware (2017) spread mostly to *unpatched* Windows machines worldwide.
   - Local example: a Pulchowk/BIM student's laptop hit by ransomware days before thesis submission — no backup, files gone.
   - Misconception: *"Hackers only target big companies, not me."* Correction: most attacks are automated and untargeted — they hit whoever is unpatched.

2. **Updates & patching**
   - Definition: patches fix known security holes attackers already know about.
   - Theory: turn on automatic OS + browser + app updates; "end-of-life" software (e.g., Windows 7) never gets fixes again.
   - Local example: pirated/cracked Windows common in Nepal often *can't* update safely and ships with bundled malware.
   - Misconception: *"Updates are just annoying new features."* Correction: most are security fixes, not cosmetics.

3. **Antivirus / anti-malware**
   - Definition: software that detects and blocks malicious files/behavior.
   - Theory: Windows Defender (built-in, free, fine for most users); real-time scanning vs on-demand; signatures vs behavior.
   - Mini case: "A free 'PC cleaner' downloaded from a pop-up *is itself* the malware — what gave it away?" (unsolicited pop-up, urgency, 'pay to fix 5 viruses').
   - Misconception: *"I need to buy 3 antiviruses to be safe."* Correction: one good, updated AV is enough; multiples conflict.

4. **Backups (the 3-2-1 rule)**
   - Definition: keeping recoverable copies of important data.
   - Theory: 3 copies, 2 media types, 1 offsite/cloud; ransomware/theft/disk failure all defeated by a clean backup.
   - Local example: load-shedding/power surges and cheap drives fail often in Nepal — and a stolen laptop in a tempo takes everything with it.
   - Fun analogy: a backup is a spare house key with a trusted neighbor — useless until the day you're locked out, then it's everything.

5. **Firewall basics**
   - Definition: a filter that controls which network traffic is allowed in/out.
   - Theory: host firewall (on the OS) vs router firewall; "deny by default" for incoming; don't blindly click "Allow" on every prompt.
   - Misconception: *"A firewall makes me unhackable."* Correction: it's one wall, not the whole castle.

**Check for understanding:**
- MCQ1: The best defense against ransomware locking your files is…? → recent offline/cloud backups ✅
- MCQ2: Running two real-time antivirus programs at once usually…? → causes conflicts/slowdowns (no extra safety) ✅
- Discussion: "Right now, where is the *only* copy of your most important file — and what happens if that device dies?"

**Real-life application:** a 10-minute self-audit (turn on auto-updates, confirm Defender is on, set up one cloud/drive backup, check firewall is on) that every student does on their own laptop this week.

**Summary:** (1) posture = patch + protect + back up + contain; (2) updates close known holes; (3) one AV, 3-2-1 backups, firewall on. **Next:** the device in your pocket and the gadgets in your home.

**Visual cues:** "posture layers" stack diagram (Patch → Protect → Backup → Contain); 3-2-1 backup illustration; before/after "security checklist" screenshot mock.

---

## S29 — Mobile Devices & Internet of Things (IoT) Devices

**Hook:** "A free torch app asks for your contacts, microphone, location, and SMS — *why does a flashlight need to read your texts?*" And: "Your neighbour's CCTV camera still uses the password 'admin/admin' — anyone on the internet can watch their living room." → mobile + IoT are where most of us are weakest.

**Concepts & how each will be filled:**

1. **Mobile app permissions**
   - Definition: the access (camera, mic, location, SMS, contacts, storage) an app requests.
   - Theory: least privilege — grant only what the app's function needs; "while using the app" vs "always"; review/revoke in Settings.
   - Local example: fake/cloned "loan" and "eSewa/Khalti" apps on Nepali phones that demand SMS access to steal OTPs and contacts (then harass for repayment).
   - Misconception: *"If it's on the Play Store, it's safe."* Correction: malicious/cloned apps slip through; check developer, reviews, install count.

2. **Securing the phone itself**
   - Theory: screen lock + biometrics, auto-lock timeout, OS updates, install from official stores only, "Find My Device"/remote wipe, avoid sideloading APKs.
   - Local example: cheap Android phones in Nepal that stop getting updates after a year — and the habit of installing APKs shared on Facebook groups/Messenger.
   - Mini case: "A 'Dashain offer — win an iPhone!' link asks you to install an APK. What happens next?" (malware / banking-trojan that reads your OTP SMS).
   - Misconception: *"iPhones can't get hacked."* Correction: less common ≠ immune; phishing and account theft hit any platform.

3. **Mobile banking / wallet safety (Nepal focus)**
   - Theory: app-specific PIN, never share OTP/MPIN, beware SIM-swap, log out on shared devices, watch URLs (esewa.com.np vs lookalikes).
   - Local example: scam call "I'm from eSewa/your bank, tell me the OTP to reverse a wrong transfer" — eSewa/Khalti/banks *never* ask for OTP/MPIN.
   - Misconception: *"Telling the OTP is fine if they already know my name/number."* Correction: an OTP is the last key — sharing it = handing over your money.

4. **Internet of Things (IoT) risks**
   - Definition: everyday devices with internet connectivity (CCTV/IP cameras, smart bulbs, smart TVs, routers, smartwatches).
   - Theory: default passwords, no/rare updates, always-on, often unmonitored = easy bots; Mirai botnet enslaved millions of IoT devices via default passwords.
   - Local example: home/shop IP CCTV cameras in Kathmandu left on default logins and exposed online; ISP-provided routers (WorldLink/Vianet) kept on the default admin password printed on the sticker.
   - Mini case: "A baby monitor / CCTV streams to the open internet because nobody changed the password — what could a stranger do?"
   - Fun analogy: an IoT device with a default password is a house where the builder's master key still works on the front door.

**Check for understanding:**
- MCQ1: A flashlight app requesting SMS + contacts access is a sign of…? → over-broad/suspicious permissions ✅
- MCQ2: A caller claiming to be from your bank asks for the OTP to "fix" a transfer. You should…? → refuse and hang up; banks never ask for OTP ✅
- Discussion: "Open your phone's permission settings now — name one app with access it doesn't actually need."

**Real-life application:** audit one phone (revoke 2 unnecessary permissions, enable auto-lock + remote wipe) and one home device (change the router/CCTV default password) this week.

**Summary:** (1) grant least-privilege permissions; (2) update + lock + official-stores-only your phone; (3) never share OTP/MPIN; (4) change default passwords on every IoT device. **Next:** the physical world — theft, prying eyes, and what you throw away.

**Visual cues:** "what does this app really need?" permission table; IoT home map (router, CCTV, TV, bulb) flagged with default-password warnings; "anatomy of an OTP scam" comic strip.

---

## S30 — Enhancing Physical Security

**Hook:** "Your password can be 20 characters long — and useless if someone watches you type it on the bus, or buys your old phone with your photos still on it." → the cheapest hack is often physical, not digital.

**Concepts & how each will be filled:**

1. **Device theft & loss**
   - Definition: physical loss of a phone/laptop = loss of everything logged in on it.
   - Theory: full-disk encryption (BitLocker/FileVault/Android-iOS default), strong screen lock, remote-find/remote-wipe enabled, don't leave devices unattended.
   - Local example: phone/laptop snatching in crowded micros, tempos, and at cafés in Thamel/New Road; a stolen phone still logged into eSewa/Facebook/Gmail.
   - Misconception: *"They'll just sell the hardware, my data is safe."* Correction: an unlocked or unencrypted device exposes accounts, OTP SMS, and saved passwords.

2. **Shoulder-surfing & visual exposure**
   - Definition: someone watching your screen/keystrokes to steal PINs or info.
   - Theory: shield the keypad, privacy screen protectors, sit with your back to a wall, beware ATM/POS camera overlays and people "helping" at the machine.
   - Local example: shoulder-surfing PINs at ATMs and while entering eSewa/MPIN in a shared room or cyber café.
   - Mini case: "A stranger at the ATM offers to 'help' the queue move faster and stands close — what's the risk?"

3. **Secure disposal & resale**
   - Definition: making data unrecoverable before you sell/donate/discard a device.
   - Theory: factory reset is *not* always enough — sign out of accounts first, remove SIM/SD card, encrypt-then-wipe, physically destroy dead drives.
   - Local example: second-hand phone/laptop market (Hattisar, online resale) where buyers recover the seller's photos and logins from a careless wipe.
   - Misconception: *"Deleting files / formatting erases them."* Correction: deleted data is often recoverable until overwritten or the drive was encrypted.

4. **Screen locks & access control**
   - Theory: PIN/password/biometric, short auto-lock timeout, lock screen on walk-away (Win+L), disable lock-screen notification previews that leak OTPs/messages.
   - Misconception: *"A pattern lock is plenty."* Correction: common patterns are guessable and smudge-readable; a PIN/biometric is stronger.
   - Fun analogy: leaving a device unlocked is leaving your house with the door open *and* a sign saying which room the cash is in.

**Check for understanding:**
- MCQ1: Before selling your old phone you should FIRST…? → sign out of all accounts, then encrypt/factory-reset & remove SIM/SD ✅
- MCQ2: A "factory reset alone guarantees no one recovers my data" is…? → false (encrypt-then-wipe is safer) ✅
- Discussion: "Where do you most often type a PIN/password in public, and who could be watching?"

**Real-life application:** enable encryption + remote wipe + a 30-second auto-lock on your own device, and turn off OTP/message previews on the lock screen, today.

**Summary:** (1) a lost unencrypted device = a data breach; (2) shield your screen and PINs; (3) wipe properly before disposal; (4) lock screens + hide notification previews. **Next:** taking all this into the home-office / remote-work setting.

**Visual cues:** "stolen unlocked phone" attack-chain diagram (theft → still-logged-in apps → account takeover); ATM shoulder-surfing illustration; "delete vs wipe vs encrypt" comparison bar.

---

## S31 — Cybersecurity When Working from Home

**Hook:** "You join an office Zoom from your bedroom on the same Wi-Fi as your smart TV, your roommate's torrents, and a CCTV with a default password — and you've saved the company database to your Desktop 'just for now.' Where could this go wrong?" → home is now the office, but without the office's security.

**Concepts & how each will be filled:**

1. **Securing the home network**
   - Definition: the router is the front gate of your digital home.
   - Theory: change default admin password, use WPA2/WPA3 + a strong Wi-Fi passphrase, update router firmware, disable WPS, set up a guest network for visitors/IoT.
   - Local example: WorldLink/Vianet/Subisu routers left on the sticker password; neighbours sharing one Wi-Fi where everyone sees everyone's traffic.
   - Misconception: *"My Wi-Fi has a password, so it's secure."* Correction: weak passphrase + default router login + outdated firmware still leave you exposed.

2. **VPNs**
   - Definition: a VPN encrypts your traffic through a secure tunnel.
   - Theory: company VPN for work resources; on public/untrusted Wi-Fi a VPN stops local snooping; "free VPN" apps may *sell* your data.
   - Local example: working from a café/co-working space in Kathmandu on open Wi-Fi — and the difference a VPN makes there.
   - Misconception: *"A VPN makes me anonymous and 100% safe."* Correction: it protects the transport; it won't save you from phishing, malware, or a weak password.

3. **Separating work and personal**
   - Theory: don't mix work logins/data with personal accounts; use the work-issued device/account for work; avoid storing company data on personal cloud; lock the machine when AFK at home too.
   - Mini case: "You email a work file to your personal Gmail to finish it at night — what risks did you just create?" (data leakage, no company control, breach exposure).
   - Misconception: *"At home there's no one around, so I can relax security."* Correction: family/flatmates/IoT and remote attackers are all still in scope.

4. **Video-call & collaboration safety**
   - Theory: require meeting passwords + waiting rooms (Zoom/Meet/Teams), don't post invite links publicly, mind what's visible/audible in background, beware screen-share leaks and fake meeting-invite phishing.
   - Local example: "Zoom-bombing" of online classes/Tihar-Dashain virtual meetings in Nepal during lockdown when links were shared openly.
   - Fun analogy: an open meeting link with no password is a public event poster — anyone who finds it walks in.

**Check for understanding:**
- MCQ1: On open café Wi-Fi, the best protection for work traffic is…? → a (trusted/company) VPN ✅
- MCQ2: Emailing a company file to your personal Gmail to finish later is…? → a data-leakage risk, avoid it ✅
- Discussion: "List three devices on your home Wi-Fi right now — which is the weakest link an attacker would target?"

**Real-life application:** harden one home router (change admin + Wi-Fi password, enable WPA2/3, make a guest network for IoT/visitors) and set meeting passwords on your next online class/call.

**Summary:** (1) lock down the router (the gate); (2) VPN on untrusted networks; (3) keep work and personal separate; (4) password-protect meetings & mind your background. **Next:** the keys to everything — your accounts and passwords.

**Visual cues:** home-network diagram with main vs guest network split; "café Wi-Fi with vs without VPN" before/after; meeting-security checklist card.

---

## S32 — Securing Your Accounts & Passwords (closes Unit 6)

**Hook:** "You reuse one password across Facebook, Gmail, eSewa, and your college portal. One of those sites gets breached — now attackers try that same password *everywhere* (it's called credential stuffing). How many of your accounts just fell with one domino?" → accounts are the real target; passwords are the lock.

**Concepts & how each will be filled:**

1. **Strong passwords**
   - Definition: long, unique, hard-to-guess credentials.
   - Theory: length beats complexity — a passphrase ("hariyo!gai-khana-25") beats "P@ss123"; unique per site; never names/DOB/"password"/"123456".
   - Local example: weak Nepali-common passwords (phone number, "nepal123", favourite team/idol, DOB) and reusing one across all accounts.
   - Misconception: *"Adding @ and a number makes it strong."* Correction: short-but-symbolic is still weak; length + uniqueness matter most.

2. **Password managers**
   - Definition: a tool that generates and stores unique passwords behind one master password.
   - Theory: Bitwarden/built-in browser/Google managers; you remember one strong master password + the manager does the rest; reduces reuse.
   - Mini case: "You have 60 accounts — can a human realistically use 60 unique strong passwords without a manager?" (no — that's why people reuse).
   - Misconception: *"A password manager is a single point of failure / unsafe."* Correction: a well-secured manager (strong master + MFA) is far safer than reuse and sticky notes.

3. **MFA / 2FA (multi-factor authentication)**
   - Definition: a second proof beyond the password (something you have/are).
   - Theory: SMS OTP < authenticator app (Google/Microsoft Authenticator, TOTP) < hardware key; enable on email + banking + social first; beware SIM-swap weakening SMS-OTP.
   - Local example: turning on 2FA for eSewa/Khalti, bank apps, Gmail, and Facebook; why your *email* 2FA matters most (it resets everything else).
   - Misconception: *"MFA is too much hassle."* Correction: it blocks the vast majority of account-takeover even when your password is stolen.

4. **Breach awareness & response**
   - Definition: knowing when your credentials leak and acting fast.
   - Theory: check haveibeenpwned.com; on breach → change that password + everywhere it was reused, enable MFA, watch for follow-on phishing.
   - Local example: leaked Nepali service/forum databases circulating, followed by targeted scam calls/SMS using your real details to seem legit.
   - Fun analogy: reusing one password is using the same key for your house, car, office, and locker — lose it once, lose everything; a password manager gives every lock its own key.

**Check for understanding:**
- MCQ1: The single most important account to protect with a strong password + MFA is usually…? → your primary email (it can reset all the others) ✅
- MCQ2: Reusing one password and having one site breached enables…? → credential stuffing across your other accounts ✅
- Discussion: "How many of your accounts share a password right now — and which one breaking would hurt the most?"

**Real-life application:** set up a password manager, generate a unique password for your email + one banking/wallet account, enable authenticator-app MFA on both, and run your email through haveibeenpwned — all this week.

**Summary:** (1) long, unique passphrases per site; (2) a password manager makes that realistic; (3) MFA (authenticator > SMS) stops most takeovers; (4) check for breaches and react fast. **End of Unit 6 — Next unit:** Social Engineering & Cyber Terrorism (how attackers target the *human*, not the machine).

**Visual cues:** "credential stuffing domino" graphic (one leaked password topples many accounts); password-strength ladder (short/complex → long passphrase); MFA factor pyramid (SMS → app → hardware key); haveibeenpwned screenshot mock.

---

## 📋 Unit 6 — End-of-Unit Quiz (added per your preference)

**Section A — MCQ (10):** what "security posture" means; the 3-2-1 backup rule; purpose of patching; whether two antiviruses help; over-broad app permissions; the OTP-never-share rule; IoT default-password risk; encrypt-then-wipe before disposal; VPN on public Wi-Fi; credential stuffing; which account matters most for MFA.
**Section B — Short answer (5):** explain the 3-2-1 backup rule; list 3 things to check when auditing a phone; why is a factory reset not always enough; name the MFA factor types from weakest to strongest; what is credential stuffing?
**Section C — Applied case (2):** (i) given a messy home setup (default router password, no backups, reused passwords, IoT on default logins), write a prioritized hardening plan; (ii) you receive a "from eSewa" call asking for an OTP and an SMS link — identify the red flags and the correct response.
**Section D — Discussion (1):** "Are password managers safer or riskier than memorizing passwords? Argue both sides, then take a position."
*(Full questions + answer key generated with the material.)*

---

## Open questions before I generate Unit 6 material
1. Keep the Nepal examples above (eSewa/Khalti OTP scams, WorldLink/Vianet default routers, Thamel/New Road snatching, second-hand phone market, Zoom-bombing of online classes)?
2. For tools — name specific products (Windows Defender, Bitwarden, Google/Microsoft Authenticator, haveibeenpwned), or keep it vendor-neutral?
3. Same as the other units: keep 2-MCQ + discussion per session **and** the end-of-unit quiz?
4. Should the hands-on "do this week" actions become a single graded Personal-Security-Audit lab deliverable tied to the unit's Lab Work?
