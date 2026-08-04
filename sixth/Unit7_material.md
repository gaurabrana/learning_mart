# IT 246 — Unit 7: Social Engineering and Cyber Terrorism
### Full Lecturer-Ready Session Material (S33–S37)

**Program:** BIM, 6th Semester · **Unit weight:** 5 lecture hours
**Sessions:** S33–S37 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT246_Unit7.pptx` (76 slides), regenerated via `build_unit7_pptx.py` (imports `deckkit.py`).

> **Framing — read first.** This unit is taught **DEFENSIVELY / for awareness only.** Students learn
> to **recognise and prevent** attacks, never to perform them; there is **no operational how-to.**
> Cyber terrorism is kept **conceptual and responsible** — we classify and defend, we do not instruct.

> **How to read this file.** This is written to **carry a full 50 minutes on its own.** Each
> session has **minute markers** `[~X min]`, the actual **explanation to deliver** (prose, not just
> bullets), **worked examples**, a **timed in-class activity**, and lecturer cue cards in
> `> 🎙️` blocks. `[SLIDE]` marks slide-ready blocks; `🖼️` marks diagram cues. Pace tags:
> `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]`. Total per session: **5 + 35 + 5 + 3 + 2 = 50 min.**

---

## Unit 7 — Learning Outcomes
By the end of this unit, students will be able to:
1. Define social engineering and explain why humans are the "weakest link" in security.
2. Recognise the psychological principles (trust, authority, reciprocity, urgency, fear) that attackers exploit — for defence.
3. Identify the major social-engineering attack types (phishing, vishing, smishing, pretexting, baiting, tailgating) and apply countermeasures.
4. Define cyber terrorism, distinguish it from cybercrime/hacktivism/warfare, and classify its types.
5. Explain cyber terrorism's effects on critical infrastructure and describe how it is countered at personal, organizational, and national levels.

---
---

# S33 — Introduction to Social Engineering
**Lecture hour 1 of 5 (Unit 7) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"The firewall never gets a vote"**

> **Deliver (≈2 min):** Set the scene slowly. "You can buy a **Rs. 50,000 firewall**, but if a polite
> caller says **'Namaste, I'm calling from your bank's head office'** and **you read out your OTP** —
> the firewall **never even gets a vote.**"
>
> **Run a quick reaction (≈3 min):** "**Why do humans break before machines do?**" Take a few answers.
> Land the theme: **people are the easiest system to 'hack.'** Today: **what social engineering is →
> why attackers use it → why humans are the weakest link.** Remind them up front: **we learn to
> recognise these tricks, never to run them.**

> 🎙️ Speaker note: Keep the framing defensive from minute one. The surprise to land: the strongest
> technical defence is irrelevant the moment a human is persuaded to open the door.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Is Social Engineering `[THEORY]` `[~10 min]`

[SLIDE] **Hacking the person, not the PC**

> **Deliver:** Give the definition and write it on the board. **Social engineering = manipulating
> PEOPLE into giving up confidential information or access, instead of breaking technology directly.**
> The attacker **"hacks the person, not the PC"** — it targets **human psychology** (trust, helpfulness,
> fear), **not code.** Make the key moves explicit:
> - It **bypasses the technology entirely** — no firewall is defeated if a human opens the door.
> - The **"system" being attacked is a person's judgement** — **persuasion and deception**, not exploits.
> - It works over **any channel**: a call, an SMS, an email, or a face-to-face visit.
> - The **tech (a fake page, a spoofed number) is only a prop**; the con is the **human manipulation.**

- 🌍 **Global example (awareness):** attackers **impersonating the IT helpdesk** to get an employee to
  **reset a password** — no code is broken, the human is persuaded.
- 🇳🇵 **Local example:** a fake **"NTC / Ncell" SMS** saying your SIM will be **blocked** unless you
  **"verify" details on a link.** No telecom system is breached — a person is frightened into clicking.

> ❌ **Common misconception:** *"Social engineering is a technical hacking skill."*
> ✅ **Correction — say it out loud:** "It's **mostly persuasion + deception**; the **tech is
> secondary.** A scammer needs a **convincing story** far more than coding skill — which is why
> **anyone**, not just 'techies', can be targeted."

> 🖼️ Visual: a **human-vs-firewall split** — a sturdy brick wall (the machine, "never gets a vote")
> beside a person willingly opening the gate ("reads out the OTP"); the attacker's arrow routes to the
> person.

> 🎙️ Speaker note: Return to the slogan **"hacking the person, not the PC"** all session. Defence is
> **human-first** — awareness and habits, not just software.

**📊 Depth table — Hacking the machine vs hacking the person**

| Dimension | Technical attack (the machine) | Social engineering (the person) |
|---|---|---|
| Target | Code, servers, encryption | A human's trust and judgement |
| Method | Exploits, brute force, malware | Persuasion, deception, impersonation |
| What it defeats | A weak system | A busy, polite, or fearful person |
| Cost & skill | High — needs deep tech skill | Low — mostly a convincing story |
| Nepal example | Cracking a bank's core system | Phoning a customer as 'bank security' |
| Defence | Firewalls, patching, encryption | Awareness, verify-before-trust habits |

*ℹ️ The whole point: social engineering routes AROUND the technology by targeting the person operating it. Defence is therefore human-first — awareness and habits, not just software.*

**📊 Depth table — Real Nepali social-engineering incidents — the con, not the code**

| Real case (Nepal / IT) | What the attacker actually did | Why it's social engineering (verdict) |
|---|---|---|
| Fake 'NTC/Ncell' SIM-block SMS with a link | Scared the user into 'verifying' on a fake page | Persuasion + fear — no telecom system was breached |
| 'Bank head office' call asking for the OTP | Impersonated authority to extract the code | Targets the person's trust, not the bank's servers |
| 'IT helpdesk' asks a staffer to confirm a password | Used helpfulness + urgency to reset access | The human is the door; the network is untouched |
| Fake eSewa 'account suspended' message | Rushed the victim to click and log in | Deception over a channel — the wallet wasn't hacked |
| Caller uses your real name + branch (leaked list) | Manufactured legitimacy to lower your guard | Story-building, not code — sounds official |
| 'Daraz prize' claim asking for a 'fee' | Dangled a reward to get money/details | Greed lever — a con, not a technical exploit |

*ℹ️ In every row the technology is untouched — the attacker persuaded a person. That is the signature of social engineering, and the reason awareness (not just software) is the defence.*


#### Concept 2 — Why Attackers Use It (the need) `[THEORY]` `[~10 min]`

[SLIDE] **The path of least resistance**

> **Deliver:** Define it plainly. **Social engineering is the path of LEAST resistance — cheaper,
> faster, and more reliable than defeating strong technical controls.** Strong **encryption and
> firewalls make direct attacks costly**, so attackers **pivot to the human.** Walk the economics:
> - Hardened tech **raises the cost** of a direct attack → the **human becomes the cheap way in.**
> - **High success, low cost, hard to trace** back to the attacker.
> - **No expensive tools** needed — a **phone and a convincing story** can be enough.
> - It **scales**: one message blasted to thousands needs only a **few victims** to pay off.

- 🇳🇵 **Local example:** instead of cracking a **bank's systems** — expensive, slow, likely to fail —
  scammers simply **phone customers pretending to be "bank security."** It is far easier to **fool a
  thousand customers** than to **breach one well-defended bank.**

> ❌ **Misconception:** *"If the bank is secure, my money is safe."*
> ✅ **Correction:** "The bank's servers may be hardened, but **YOU are the softer target.** Attackers
> deliberately **skip the strong wall and knock on the human door** — so **your own awareness is part
> of the bank's security.**"

> 🖼️ Visual: a **cost-vs-success quadrant** placing **social engineering** in **'low cost + high
> success'**, with brute-force crypto and zero-days in the costly corners.

> 🎙️ Speaker note: Attackers are **economically rational.** They pick the **cheapest path with the
> highest payoff** — which, once machines are hardened, runs **straight through the person.**

**📊 Depth table — Why the human is the path of least resistance**

| Attack path | Cost / skill to the attacker | Success & traceability |
|---|---|---|
| Breaking strong encryption | Very high — often infeasible | Low success; heavy effort wasted |
| Finding a zero-day exploit | High — rare, expensive skill | Works, but costly and perishable |
| Phoning a customer as 'bank security' | Very low — a phone + a script | High success; hard to trace |
| Mass phishing SMS to thousands | Very low — one message, bulk send | A few victims still pays off |
| Tricking a busy employee for a password | Low — a plausible story | Bypasses every technical control |

*ℹ️ Attackers are economically rational: they pick the cheapest path with the highest payoff. When machines are hardened, that path runs straight through the person.*


#### Concept 3 — Why Humans Are the Weakest Link `[THEORY]` `[~10 min]`

[SLIDE] **Good human traits, turned into an attack surface**

> **Deliver:** Name the mechanism. **Humans are exploitable through predictable traits** —
> **helpfulness, obedience to authority, fear of consequences, curiosity, and trust in familiar
> brands** — combined with **low security awareness.** The crucial point: **attackers don't break
> these traits; they USE them.**
> - **Helpfulness:** we want to assist, so we comply with a reasonable-sounding request.
> - **Obedience to authority:** a "boss" or "official" voice **short-circuits our doubt.**
> - **Fear & urgency:** a threat ("account will be blocked") makes us **act before thinking.**
> - **Curiosity & trust in brands:** a familiar logo or a "you've won" message **lowers the guard.**

- 🇳🇵 **Mini case (work it, ≈2 min):** an office peon receives a call: **"Sir, from the IT department
  here — your email will be deleted today, just confirm your password."** Ask: "why does this **work on
  a busy, polite employee?**" Draw it out — **authority + urgency + helpfulness** all fire at once.

> ❌ **Misconception:** *"Only careless or foolish people fall for scams."*
> ✅ **Correction:** "**Smart, busy, polite people are exactly the target** — the attack exploits
> **normal good traits** under time pressure. Assuming **'it won't happen to me'** is itself the
> vulnerability."

> 🍿 **Fun analogy (deliver it):** "The **strongest castle wall is useless** if the **gatekeeper opens
> the gate** to anyone wearing the **right uniform.** Social engineering **is** the right uniform."

> 🎙️ Speaker note: Defence is **not** becoming rude or paranoid — it's a **small verify-before-you-act
> habit** for each trigger. Keep it practical.

**📊 Depth table — Human trait → how it's exploited → how you defend**

| Human trait | How the attacker exploits it (Nepal) | Defence habit |
|---|---|---|
| Helpfulness | 'Just confirm your password so I can fix your email' | No one legitimate needs your password — refuse |
| Obedience to authority | 'I'm calling from the bank / the police' | Verify the identity via the official number yourself |
| Fear of consequences | 'A police case is filed unless you pay now' | Real authorities don't demand instant payment by phone |
| Urgency / time pressure | 'Your account blocks in 10 minutes' | Slow down — urgency is a red flag, not a reason |
| Curiosity | 'Open this to see who viewed your profile' | Don't open unexpected links/attachments |
| Trust in familiar brands | Fake eSewa / Daraz logo and sender name | Check the real sender/URL; brands don't ask for OTP |

*ℹ️ Each row is a normal, good human trait turned into an attack surface. Defence is not becoming rude or paranoid — it is a small verify-before-you-act habit for each trigger.*

#### 🛠 ACTIVITY — "Name the trick" `[ACTIVITY]` `[~5 min]`

[SLIDE] **A suspicious call/SMS you or your family received**

> **Run it:** In pairs (2 min), each student **recalls one suspicious call or SMS** (in Nepali) that
> they or their family received. They **write the exact story it told and what it asked for**, then
> **name the human trait** it targeted (helpfulness / authority / fear / curiosity / brand trust). Take
> **3–4 answers aloud** (3 min); notice how often **authority + urgency appear together.** Seeds:
> NTC/Ncell SIM-block SMS, a "bank security" OTP call, Facebook/Daraz prize, eSewa "account suspended."

> 🎙️ Speaker note: **Recognising the lever is the fastest early-warning sign.** The goal is
> **recognition, not any how-to** — keep the discussion on spotting, not doing.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** Social engineering primarily attacks:
a) firewalls b) encryption c) ✅ **human psychology / people** d) hardware

**MCQ 2.** Attackers prefer social engineering mainly because it is:
a) more technical b) ✅ **low-cost and high-success vs. beating strong tech controls** c) always legal d) slower

**Discussion prompt:** *Recall one suspicious call/SMS you or your family received — what trick was it using?*

> 🎙️ Speaker note: Reward students who **name the specific lever** (authority/urgency/fear) rather than
> just "a scam." Keep the tone defensive.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** the **most common way money is stolen from ordinary Nepalis online is not
"hacking"** — it's a **convincing phone call or message.** Recognising this is your **first and
cheapest line of defence**, for you and your family. You don't need to be a security expert; you need
the reflex to **pause and verify** when someone pressures you.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Social engineering = hacking PEOPLE, not machines** — persuasion and deception over any channel.
2. It's the **cheapest, highest-success** attack path, so attackers **pivot to the human by choice.**
3. Humans are exploitable through **helpfulness, authority, fear, curiosity, and brand trust** — **verify before you act.**

**Next session (S34):** the exact **psychological levers** attackers pull, and how the con is built.

---
---

# S34 — Implications · Building Trust · Exploiting the Relationship
**Lecture hour 2 of 5 (Unit 7) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Why be friendly for 10 minutes first?"**

> **Deliver (≈2 min):** "**Why does a scammer spend 10 minutes being friendly before asking for
> anything?** Because **the ask only works after the trust.**"
>
> **Run the question (≈3 min):** "Today we **reverse-engineer the manipulation — so you see it
> coming.**" Land the agenda: **what's really at stake → how trust is manufactured → how urgency and
> fear close the trap.** Emphasise: this is the **psychology of the con, taught for defence.**

> 🎙️ Speaker note: The con has **two phases** — build trust, then squeeze. Keep returning to that
> shape; it's the recognition key for the whole session.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Understanding the Implications `[THEORY]` `[~10 min]`

[SLIDE] **One leaked OTP is never "just one account"**

> **Deliver:** Define the stakes. **A single successful manipulation rarely stays "one account."** One
> leaked **OTP or password** can cascade into **data loss, financial theft, identity theft, and
> reputational damage** — because **credentials are keys to a whole chain of linked accounts.**
> - **Credentials are keys, not doors:** one unlocks **email**, which resets others.
> - **Email → bank → wallet → social accounts** is a common **chain reaction.**
> - The attacker then **messages your contacts** for more money — spreading the damage.
> - Impact is **delayed and wide** — you often see it **only after** the chain has run.

- 🇳🇵 **Local example:** a victim who shares an OTP **loses their eSewa / Khalti wallet balance** *and*
  the attacker then **messages their contacts** for more money — so the harm spreads to **friends and
  family** through the victim's own name.

> ❌ **Misconception:** *"It's just one password, no big deal."*
> ✅ **Correction:** "**Credentials are keys to a whole chain of accounts.** One leaked code can unlock
> **email, then the bank, then social, then your contacts.** The impact is **almost never limited** to
> the single thing you first gave away."

> 🖼️ Visual: a **chain-reaction flow** — 1 OTP → EMAIL → BANK/eSewa → SOCIAL → CONTACTS scammed next.

> 🎙️ Speaker note: Use the cascade to **kill the "no big deal" reflex.** The one code is the **first
> link** that unlocks all the others.

**📊 Depth table — One leaked credential — what it unlocks (the chain)**

| Step in the chain | What the attacker reaches | Why it cascades |
|---|---|---|
| OTP / password shared | The first account (e.g. email) | The entry point to everything linked |
| Email taken over | Password resets for other services | Most accounts recover via email |
| Bank / eSewa / Khalti | Wallet balance & payment history | Direct financial theft |
| Social accounts | Identity & the contact list | Enables the next round of scams |
| Contacts messaged | Friends & family targeted next | Trust in YOUR name is now the weapon |

*ℹ️ The damage is a chain, not a point. This is why 'it's just one OTP' is dangerous thinking — that one code is the first link that unlocks all the others.*


#### Concept 2 — Building Trust — the levers `[THEORY]` `[~10 min]`

[SLIDE] **Trust is manufactured — spot the lever**

> **Deliver:** Frame it clearly. **Attackers manufacture trust using well-known influence principles**
> (Cialdini-style) — **authority, liking/rapport, social proof, and reciprocity.** Teach them **only to
> RECOGNISE them**: the **friendly, legitimate-sounding front is engineered, not genuine.**
> - **Authority:** "I'm from the bank / the police" — a title that **short-circuits doubt.**
> - **Liking / rapport:** friendly small talk to **make you comfortable** before the ask.
> - **Social proof:** "everyone has already updated their KYC" — the **herd nudge.**
> - **Reciprocity:** "I've helped you fix this, now just **confirm the code** for me."

- 🌍 **Global example:** **spoofed sender names / logos** that look like a real institution.
- 🇳🇵 **Local example:** a caller using a **real-sounding Nepali bank name, branch, and your actual
  name** (scraped from a **leaked list**) to sound legitimate. Every detail is **engineered**; none of
  it **proves** who they are.

> ❌ **Misconception:** *"If they know my name, my branch, and my bank, they must be genuine."*
> ✅ **Correction:** "That information is often **scraped from leaked lists** and is **exactly how
> attackers manufacture legitimacy.** Knowing your details **proves nothing** — verify by contacting
> the institution **through its official number yourself.**"

> 🖼️ Visual: a **levers grid** — authority, liking/rapport, social proof, reciprocity, urgency, fear —
> each with a one-line Nepali example.

> 🎙️ Speaker note: These are **legitimate psychology principles turned into a con.** The moment a
> student can **name the lever**, its power drops. Attackers often **stack several at once.**

**📊 Depth table — The influence levers — recognise, don't use**

| Lever | How it sounds (Nepal) | The red flag it should raise |
|---|---|---|
| Authority | 'I'm calling from the bank / police / IT' | A title alone is not proof — verify independently |
| Liking / rapport | Warm, friendly chat before any request | Unusual friendliness from a stranger who then asks |
| Social proof | 'Everyone has updated their KYC already' | 'Everyone's doing it' is pressure, not a reason |
| Reciprocity | 'I helped you — now just confirm this code' | A small favour used to extract a bigger one |
| Familiarity | Uses your real name, branch, or last digits | Scraped from a leaked list to fake legitimacy |
| Consistency | 'You already agreed, so just finish the step' | Manufactured momentum toward the real ask |

*ℹ️ These are legitimate psychology principles turned into a con. You are learning them to DETECT them — the moment you can name the lever, its power drops.*


#### Concept 3 — Exploiting the Relationship — the close `[THEORY]` `[~10 min]`

[SLIDE] **Trust is the setup; urgency is the close**

> **Deliver:** Complete the con. **Once trust exists, attackers add PRESSURE so the victim acts before
> thinking** — **urgency, fear, and scarcity.** This is **"the close":** the emotional squeeze that
> converts a friendly conversation into a **harmful action.**
> - **Urgency:** "your account blocks in 10 minutes" — **no time to verify.**
> - **Fear:** "a police case has been filed against you" — **panic overrides judgement.**
> - **Scarcity:** "this lottery claim expires today" — **act now or lose out.**
> - The **friendly build-up is misdirection**; the **pressured ask is the trick.**

- 🇳🇵 **Mini case (work it, ≈2 min):** a **"Facebook lottery" message** — **"You've won Rs. 25 lakh,
  pay Rs. 5,000 processing fee to release it."** Have students **identify every trust + urgency + greed
  lever** used. It's a **magician's patter:** friendly chatter, then the ask.

> ❌ **Misconception:** *"A real urgent message means I must act immediately."*
> ✅ **Correction:** "**Manufactured urgency is the attacker's main weapon** — it exists precisely to
> **stop you verifying.** The correct response to pressure is to **slow down**; a genuine institution
> **will not punish you** for taking time to confirm."

> 🍿 **Fun analogy (deliver it):** "It's a **magician's patter** — the **friendly chatter is the
> misdirection**; the **'trick' is the request that follows.**"

> 🖼️ Visual: the **social-engineering attack cycle** — Research → Build trust → Exploit → Exit.

> 🎙️ Speaker note: The **emotion (greed, fear, urgency) is the tell.** Naming the lever and **refusing
> to be rushed** defuses the close.

**📊 Depth table — Annotated scams — spot the levers and the close**

| Scam message (Nepal) | Levers used | The 'close' + safe response |
|---|---|---|
| 'You've won Rs. 25 lakh — pay Rs. 5,000 fee to release it' | Greed + authority + scarcity | Urgency to pay → never pay a fee to receive a 'prize' |
| 'Account blocks in 10 min — confirm your OTP now' | Authority + urgency | Time pressure → banks never ask for your OTP |
| 'Police case filed — settle immediately or be arrested' | Authority + fear | Threat of arrest → hang up, call the real police line |
| 'KYC expires today — verify on this link' | Social proof + urgency | Deadline → visit the bank/app directly, not the link |
| 'Parcel held at customs — pay Rs. 200 here' | Curiosity + urgency | Small ask → verify with the courier's official number |
| 'I'm your boss's assistant — approve this transfer fast' | Authority + rapport | Rushed approval → confirm with the boss on a known number |

*ℹ️ In every case the emotion (greed, fear, urgency) is the tell. Naming the lever and refusing to be rushed is the single fastest way to defuse the close.*

#### 🛠 ACTIVITY — "Which lever?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **In a real scam call — which trust tactic, and which close?**

> **Run it:** In pairs (2 min), take a **scam call your aunt/uncle actually got** (or one of the
> messages above). **Identify the trust-building tactic first** (authority, liking, or social proof),
> **then the "close"** — the urgency, fear, or scarcity that pushed for action. Take **3–4 answers
> aloud** (3 min) and confirm the pattern: **build trust, then squeeze.**

> 🎙️ Speaker note: The strongest answers **separate the trust phase from the close** and **name the
> emotion** each lever targets. Recognition only — no how-to.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** An attacker saying "I'm calling from the police, act now or face arrest" is combining:
a) liking + scarcity b) ✅ **authority + fear/urgency** c) reciprocity only d) social proof

**MCQ 2.** Why is leaking one OTP serious?
a) it isn't b) ✅ **it can unlock a chain of linked accounts** c) only if it's a bank OTP d) it expires

**Discussion prompt:** *In a scam call your family got, which trust tactic was used — authority, liking, or social proof?*

> 🎙️ Speaker note: Reward answers that **separate the trust-building lever from the urgency/fear
> close.** Emphasise: **naming the emotion is the defence.**

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** spotting the **EMOTION a message is trying to trigger** — fear, greed,
urgency — is the **single fastest way to catch a scam** before you react. You will rarely out-analyse a
polished con in the moment; but you can always ask **"what feeling is this trying to create in me?"** —
and that **pause** is your protection.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Impact chains** far beyond one account — one leaked OTP can unlock **email, bank, wallet, and your contacts.**
2. Attackers **manufacture trust** via **authority, liking/rapport, social proof, reciprocity** — the friendly front is **engineered.**
3. They **exploit it with urgency, fear, and scarcity** — the **"close"** that makes you act before verifying.

**Next session (S35):** the **named attack types**, how to recognise each, and how to defend.

---
---

# S35 — Attack Types (Recognition) · Countermeasures & Prevention
**Lecture hour 3 of 5 (Unit 7) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Six names, one goal: make YOU the door"**

> **Deliver (≈2 min):** "**Phishing, vishing, smishing, pretexting, baiting, tailgating** — six names,
> one goal: **make YOU the door.**"
>
> **Run the question (≈3 min):** "Today you learn to **recognise all six in the wild**, and **how to
> shut the door.**" State the boundary loudly: **recognition only — no instructions to carry them
> out.** Agenda: **the six attack types → countermeasures (organizational + technical) → personal
> prevention habits.**

> 🎙️ Speaker note: This is a **field guide to spotting attacks**, strictly defensive. Every
> description stays at the level of **what a victim sees**, never how to run it.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Major Attack Types (recognise them) `[THEORY]` `[~10 min]`

[SLIDE] **Same con, different channel**

> **Deliver:** Frame it. **The same con appears across channels under different names** — you learn to
> **RECOGNISE each, never to run it.**
> - **Digital channels:** **phishing** (email), **smishing** (SMS), **vishing** (a call) — same trick,
>   different pipe.
> - **Human / physical:** **pretexting** (a fake role/story), **baiting** (a "free" download or dropped
>   USB), **tailgating** (following an authorised person through a secured door).
> - **Recognition cues repeat:** **mismatched URLs, urgent threats, requests for OTP/PIN, generic
>   greetings.**

- 🌍 **Global example:** **package-delivery smishing waves**; **CEO-impersonation ("business email
  compromise")** asking finance to **wire money.**
- 🇳🇵 **Local example:** fake **"Nepal lottery / Daraz prize" SMS**; a **"bank officer" vishing call**
  asking for **the OTP just sent to you.**

> ❌ **Common misconception:** *"Phishing only happens over email."*
> ✅ **Correction:** "It **spans SMS (smishing), calls (vishing), QR codes, and social media.** Guarding
> only your inbox leaves **every other channel open** — the con simply **switches pipes** to whichever
> one you trust more."

> 🖼️ Visual: a **taxonomy tree** — Social engineering → Digital (phishing/smishing/vishing) and
> Human/Physical (pretexting/baiting/tailgating).

> 🎙️ Speaker note: Keep every description at **recognition level** — what the victim sees — with
> **zero operational detail.**

**📊 Depth table — The six attack types — channel, recognition cue, example**

| Type | Channel | How you recognise it (Nepal example) |
|---|---|---|
| Phishing | Email | Fake 'bank/college' email + link; mismatched URL, generic greeting |
| Vishing | Voice call | 'Bank officer' pressuring you to share the OTP/PIN just sent |
| Smishing | SMS | 'eSewa/bank suspended — click here'; 'Daraz prize'; 'parcel fee' |
| Pretexting | Any (a story) | 'I'm the new auditor / your boss's assistant' invented role |
| Baiting | Download / USB | A 'free' movie/app, or a USB left in the canteen/parking |
| Tailgating | Physical door | A stranger following staff through a secure door 'hands full' |

*ℹ️ Phishing is NOT only email — smishing, vishing, QR codes, and social media all carry the same con. Recognising the channel plus the tell (urgency, a link, an OTP request) is enough to refuse.*

**📊 Depth table — Red flag → defence (the §7A field guide)**

| Attack (technique) | Red flag to spot | Defence / safe response | If you fall for it (consequence) |
|---|---|---|---|
| Vishing — 'bank' OTP call | Anyone asking you to read out an OTP/PIN | Hang up; call the bank's official number yourself | Wallet/account drained within minutes |
| Smishing — 'account suspended' SMS | A link + urgency in a text you didn't expect | Don't click; open the app/site directly | Credentials phished on a fake login page |
| Phishing — fake bank/college email | Mismatched URL, generic 'Dear customer' | Hover the link; verify via official channel | Login stolen; inbox used to reset other accounts |
| Baiting — 'free' download / dropped USB | Something too tempting or conveniently 'found' | Don't plug in / don't download; report it | Malware installed on your device or network |
| Pretexting — 'new auditor' call | A stranger with a story wanting info/access | Verify the role with a known internal contact | Sensitive data handed to an outsider |
| Tailgating — door-following | Someone without a badge following you in | Don't hold the door; direct them to reception | An intruder gains physical access to the office |

*ℹ️ This is the core recognition table: spot the red flag, apply the defence, and note the consequence of NOT doing so. Every defence is a refusal or a verify — never an instruction to attack.*


#### Concept 2 — Countermeasures — organizational + technical `[THEORY]` `[~8 min]`

[SLIDE] **Defence-in-depth: people + process + technology**

> **Deliver:** State the principle. **Defence is layered — combining people, process, and technology.**
> **No single control stops social engineering**; they work together so a **slip at one layer is caught
> by another.**
> - **People:** **security-awareness training** and **simulated-phishing drills.**
> - **Process:** **verify-via-callback** policy, **least-privilege** access, **visitor badges & escort**
>   rules against tailgating.
> - **Technology:** **MFA**, **email filtering**, **anti-spoofing (SPF/DKIM/DMARC** — named at awareness
>   level).
> - **Policy anchor:** a bank publicly stating **"we will NEVER ask for your OTP/PIN."**

- 🇳🇵 **Local example:** a **Nepali bank** running **staff awareness sessions and simulated-phishing
  drills**, enforcing a **verify-via-callback** rule, turning on **MFA**, and repeating one public
  message: **"we will never ask for your OTP/PIN."**

> ❌ **Misconception:** *"We have MFA / a spam filter, so we're safe."*
> ✅ **Correction:** "**One control is never enough** — attackers adapt, and social engineering targets
> **people**, not just technology. Real defence **layers** people (training), process (callback, least
> privilege), and technology (MFA, filtering) so **no single failure is fatal.**"

> 🎙️ Speaker note: Keep **MFA/SPF/DKIM/DMARC at the awareness level** — students should know these
> **exist and what they achieve**, not configure them. The strongest cultural control is the **"we
> never ask for your OTP"** rule.

**📊 Depth table — Countermeasures by layer — and what each stops**

| Layer | Measure | What it stops |
|---|---|---|
| People | Awareness training + simulated-phishing drills | Staff recognise and report the lure |
| Process | Verify-via-callback before acting on a request | Impersonation calls fail the check |
| Process | Least-privilege access | A fooled account can reach less |
| Process | Visitor badges & escort policy | Tailgating into secure areas |
| Technology | Multi-factor authentication (MFA) | A stolen password alone can't log in |
| Technology | Email filtering + anti-spoofing (SPF/DKIM/DMARC) | Many phishing/spoofed emails never arrive |

*ℹ️ Defence-in-depth: each layer catches what the previous one missed. MFA, for example, means even a successfully phished password is not enough on its own.*


#### Concept 3 — Preventing Attacks — personal habits `[THEORY]` `[~7 min]`

[SLIDE] **STOP · THINK · then CLICK**

> **Deliver:** Give the habits students can use tonight. **Personal prevention is a small set of habits
> that defeats most attacks:**
> - **Never share an OTP/PIN/password** — with anyone, even "the bank."
> - **Verify independently:** call the **official number YOU look up**, not the one you were given.
> - **Check links and senders** before you act.
> - **Slow down** when a message pushes urgency — and **report** it so others are warned.

- 🇳🇵 **Mini case (work it, ≈2 min):** you get an SMS **"parcel held at customs, pay Rs. 200 here."**
  Walk the **safe response** — **don't click → verify with the courier directly.**

> ❌ **Misconception:** *"If a message looks official, it's safe to act on it."*
> ✅ **Correction:** "**Logos, names, and official tone are trivial to fake.** The safe habit **ignores
> how it looks** and instead **verifies through a channel you control** — the official number or app —
> before doing anything, especially anything **urgent.**"

> 🍿 **Fun analogy (deliver it):** "**'STOP, THINK, then CLICK'** — like **looking both ways before
> crossing a road.** Urgency is the attacker's weapon, so the **deliberate pause is the protection.**"

> 🖼️ Visual: a **STOP–THINK–CLICK** flow poster with the core rules underneath.

> 🎙️ Speaker note: Banks and wallets (**eSewa, Khalti, NIC ASIA**) repeatedly warn they **will never
> ask for an OTP** — so any such request is the **scam identifying itself.**

**📊 Depth table — Scam scenario → wrong reaction → safe response**

| Scenario (Nepal) | The wrong (unsafe) reaction | The safe response |
|---|---|---|
| 'Parcel held at customs — pay Rs. 200 here' | Click the link and pay to release it | Don't click; contact the courier's official number |
| 'Bank security' asks for the OTP just sent | Read out the code to 'confirm identity' | Refuse — banks never ask; hang up and call them |
| 'You won a prize — pay a small fee' | Pay the fee to claim the winnings | Ignore — real prizes never require an upfront fee |
| Email: 'reset your password here now' | Click the in-email link and log in | Go to the site directly and check your account |
| A found USB / 'free movie' download | Plug it in / download to see what it is | Don't; hand a found USB to IT, avoid the download |
| 'Your KYC expires today — verify now' | Rush to submit details on the link | Visit the branch or official app on your own |

*ℹ️ The pattern is always the same: refuse, then verify independently. 'STOP, THINK, then CLICK' — the deliberate pause defeats the urgency the attacker depends on.*

#### 🛠 ACTIVITY — "Spot the phish" `[ACTIVITY]` `[~5 min]`

[SLIDE] **The "parcel held at customs" SMS — find the red flags**

> **Run it:** In pairs (2 min), take the **"parcel held at customs, pay Rs. 200"** SMS. **List every
> red flag** (link, urgency, small fee, unexpected). Write the **safe response step by step** (don't
> click → verify with the courier directly). Take **3–4 answers aloud** (3 min): **which of the six
> types is it, and why?** (It's **smishing.**)

> 🎙️ Speaker note: Reward listing **concrete red flags** and a **verify-first** response. Discussion
> seed: **which of the six types is most common in Nepal now, and why?** Recognition + defence only.

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** A fraudulent *phone call* asking for your OTP is an example of:
a) phishing b) smishing c) ✅ **vishing** d) baiting

**MCQ 2.** The single best rule against OTP fraud is:
a) share it only with the bank b) ✅ **never share your OTP with anyone, even "the bank"** c) share it if urgent d) email it

**Discussion prompt:** *Which of the six attack types do you think is most common in Nepal right now, and why?*

> 🎙️ Speaker note: Reinforce the **"never share OTP"** rule and **channel-matching** (call = vishing,
> SMS = smishing, email = phishing). Recognition and defence only.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** banks and wallets (**eSewa, Khalti, NIC ASIA**, etc.) repeatedly warn
customers they **will never ask for an OTP** — **knowing the attack names** lets you **instantly
classify and reject** the scam instead of freezing. When you can say "that's vishing" the moment it
starts, you've already won.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Six recognisable attack types** across channels: **phishing, vishing, smishing, pretexting, baiting, tailgating.**
2. **Countermeasures are layered** — people (training), process (callback, least privilege), technology (MFA, filtering).
3. **Personal rule:** **verify independently, never share your OTP, slow down** — **STOP, THINK, then CLICK.**

**Next session (S36):** when manipulation **scales up to attacks on a whole nation** — **cyber terrorism.**

---
---

# S36 — Cyber Terrorism · Types of Cyber Terrorism
**Lecture hour 4 of 5 (Unit 7) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Where's the line?"**

> **Deliver (≈2 min):** "A **teenager defacing a website for fun**, an **activist protesting online**,
> and a **group trying to shut down a country's power grid** — all use computers, but **only one is
> cyber terrorism.**"
>
> **Run the question (≈3 min):** "**Where's the line?**" Take a few answers. Land the agenda:
> **defining the term precisely → distinguishing it from crime/hacktivism/warfare → its types.** Keep
> it **conceptual and responsible — no operational content.**

> 🎙️ Speaker note: The skill this session builds is **correct classification.** Resist any drift
> toward methods — we define, distinguish, and defend.

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What Is Cyber Terrorism `[THEORY]` `[~10 min]`

[SLIDE] **Intent + target + severity**

> **Deliver:** Define it. **Cyber terrorism = the politically or ideologically motivated use of
> computers / networks to cause serious harm, fear, or disruption** — especially to **critical systems
> or the public.** Three **ingredients** define it:
> - **Intent:** **political or ideological** motivation — **not profit.**
> - **Target:** often **critical infrastructure** or the **public's sense of safety.**
> - **Severity:** **real-world harm or genuine terror**, not mere nuisance.
> - **All three together** are what separate it from **ordinary hacking or vandalism.**

- 🌍 **Global example:** attacks aimed at **power grids and industrial control systems** intended to
  cause **physical disruption.**
- 🇳🇵 **Local example (awareness):** **defacement of Nepali government websites** and attacks on
  **public-service portals** during regional tensions, used to **spread fear / embarrassment.**

> ❌ **Misconception:** *"Any hacking is cyber terrorism."*
> ✅ **Correction:** "**Most hacking is crime (for profit) or vandalism.** Terrorism requires
> **political/ideological intent PLUS an intent to terrorise or seriously harm** — **mislabelling** a
> prank or a profit scam as 'terrorism' **distorts both the threat and the response.**"

> 🎙️ Speaker note: Keep this **conceptual and responsible** — the local examples are **awareness
> only**, with **no methods** discussed.

**📊 Depth table — The three ingredients of cyber terrorism**

| Ingredient | What it means | Why it matters |
|---|---|---|
| Intent | Political / ideological motive (not money) | Separates terrorism from profit-driven crime |
| Target | Critical systems or the public's safety | The aim is society-wide impact, not one victim |
| Severity | Serious harm, fear, or disruption | Nuisance/vandalism alone doesn't qualify |
| The public effect | Spreading terror or coercion | The 'terror' in cyber terrorism — fear is the goal |

*ℹ️ Only when intent + target + severity line up do you have cyber terrorism. Missing the ideological intent makes it crime; missing the severity makes it vandalism.*


#### Concept 2 — Distinguishing Related Terms `[THEORY]` `[~10 min]`

[SLIDE] **Sort by motive and actor**

> **Deliver:** Lay out the four. **Cybercrime, hacktivism, cyber warfare, and cyber terrorism overlap
> but are distinct** — separated mainly by **MOTIVE and ACTOR.** Labelling an incident correctly
> **changes the legal and response path entirely.**
> - **Cybercrime:** motive is **profit** (e.g. a **ransomware gang for money**).
> - **Hacktivism:** motive is **protest or a message** (e.g. a defacement to make a point).
> - **Cyber warfare:** **state-versus-state** action as part of conflict.
> - **Cyber terrorism:** **ideological motive** aiming to **terrorise or seriously harm.**

- 🇳🇵 **Mini case (work it, ≈2 min):** classify **three events** — a **ransomware gang for money**, a
  **protest-driven website defacement**, and an **attempt to disable a national grid** — into the
  **right bucket.** Same tools, very different labels.

> ❌ **Misconception:** *"If it's illegal and uses a computer, it's cyber terrorism."*
> ✅ **Correction:** "**Illegality and computers are common to all four.** The distinguishing factors
> are **motive** (profit vs protest vs state conflict vs ideology-and-terror) **and actor** — which is
> exactly why **careful classification matters.**"

> 🖼️ Visual: a **2×2 map** — **motive** (profit → ideological) against **severity/target** — placing
> **crime, hacktivism, warfare, and terrorism.**

> 🎙️ Speaker note: The exercise is **classification, not method.** Getting the label right decides
> **who responds** (police vs regulator vs national security) and **under which law.**

**📊 Depth table — Cybercrime vs hacktivism vs cyber warfare vs cyber terrorism**

| Term | Primary motive | Typical actor | Example (awareness) |
|---|---|---|---|
| Cybercrime | Profit / money | Criminals, fraud gangs | Ransomware gang; OTP/eSewa scams |
| Hacktivism | Protest / a message | Activists | Website defacement to make a point |
| Cyber warfare | State conflict | Nation-states | State-vs-state attacks in a conflict |
| Cyber terrorism | Ideology + terror/harm | Ideologically driven groups | Attempt to disable a national grid to cause fear |
| (shared trait) | All use computers | Overlapping tools | The tool is not what distinguishes them |

*ℹ️ They share tools, so the tool never decides the label — MOTIVE and ACTOR do. Getting the label right changes the legal route and who responds (police vs national security).*


#### Concept 3 — Types of Cyber Terrorism `[THEORY]` `[~10 min]`

[SLIDE] **"Arson with a keyboard"**

> **Deliver:** Give the categories, **for awareness.** Common **types of cyber terrorism:**
> - **(a) Attacks on critical infrastructure** — power, water, telecom, finance, aviation.
> - **(b) Data destruction / manipulation** of public records.
> - **(c) Disruption / denial of essential services** (large-scale DoS).
> - **(d) Propaganda, recruitment & psychological operations / disinformation** online.
> - **(e) Financing** via cyber means.

- 🇳🇵 **Local example (awareness):** **disinformation campaigns on social media** during sensitive
  national events; **threats to telecom / banking continuity** in South Asia.

> ❌ **Misconception:** *"Cyber terrorism only means blowing up power plants."*
> ✅ **Correction:** "Its types are **broader** — **data destruction, large-scale service denial**, and
> especially **propaganda and disinformation** that attack the **public's mind.** An information
> campaign that **spreads fear** can be as much a part of it as an infrastructure strike."

> 🍿 **Fun analogy (deliver it):** "Cyber terrorism is **'arson with a keyboard'** — the goal isn't
> **theft**, it's **fear and damage.**"

> 🖼️ Visual: an **icon row of cyber-terror types** — infrastructure / data destruction / service
> denial / propaganda / financing.

> 🎙️ Speaker note: These are **awareness categories, not a manual.** Each names **what** is targeted
> and **why**, so students can **recognise and correctly report** — never carry out.

**📊 Depth table — Types of cyber terrorism — example and intended effect**

| Type | Example (awareness level) | Intended effect |
|---|---|---|
| Critical-infrastructure attack | Targeting power/water/telecom/finance/aviation | Physical disruption and public fear |
| Data destruction / manipulation | Corrupting or wiping public records | Erode trust; damage governance |
| Service denial (large-scale) | Disrupting essential online services | Freeze daily life and commerce |
| Propaganda & psy-ops | Disinformation during sensitive national events | Spread fear, divide, and recruit |
| Recruitment / radicalisation | Online content to recruit and radicalise | Grow the movement, normalise harm |
| Financing via cyber means | Moving/raising funds online for operations | Fund and sustain the campaign |

*ℹ️ These are awareness categories, not a manual — each names WHAT is targeted and WHY, so you can recognise and correctly report it. The common thread is fear and damage, not profit.*

#### 🛠 ACTIVITY — "Crime, hacktivism, or terrorism?" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Classify a government-portal defacement**

> **Run it:** In pairs (2 min), take a **website defacement of a government portal.** **Classify it
> using the three ingredients:** intent, target, and severity. Decide — **cybercrime, hacktivism, or
> cyber terrorism** — and **defend your choice.** Take **3–4 answers aloud** (3 min); note how **motive
> and severity swing the label.**

> 🎙️ Speaker note: There's **no single 'right' label** — reward reasoning with **intent/target/
> severity.** A pure protest message leans **hacktivism**; an ideological attempt to terrorise leans
> **terrorism.** The skill is **correct classification.**

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** What most distinguishes cyber terrorism from ordinary cybercrime?
a) it uses a computer b) it is illegal c) ✅ **political/ideological intent to cause fear or serious harm** d) it is online

**MCQ 2.** Spreading propaganda and disinformation to recruit and instill fear is which type?
a) baiting b) ✅ **psychological operations / propaganda** c) phishing d) ransomware

**Discussion prompt:** *Is a website defacement of a government portal cybercrime, hacktivism, or cyber terrorism? Defend your classification.*

> 🎙️ Speaker note: Reward correct use of **intent/target/severity.** Keep the discussion **analytical
> and responsible** — no methods, only classification.

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** as future **IT / business professionals**, you'll need to **correctly label
incidents** — **mislabelling a vandalism case as "terrorism"** (or vice versa) **changes the legal and
response path entirely.** The right label decides whether the matter goes to the **police, a
regulator, or national security**, and under **which law** it's handled.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Cyber terrorism = ideological/political INTENT + serious harm or fear**, often aimed at **critical infrastructure.**
2. It's **distinct** from **cybercrime (profit), hacktivism (protest), and cyber warfare (state-vs-state)** — **motive & actor decide.**
3. Its **types** span **infrastructure attacks, data destruction, service denial, propaganda/psy-ops, and financing.**

**Next session (S37):** what it does to **real infrastructure**, and how **nations, organizations, and citizens** counter it.

---
---

# S37 — Effects on Infrastructure · Countering Cyber Terrorism
**Lecture hour 5 of 5 (Unit 7) · 50 minutes — CLOSES UNIT 7**

### 🎯 OPENING — Hook `[~5 min]`

[SLIDE] **"Two days in the dark"**

> **Deliver (≈2 min):** "Imagine **Kathmandu's power, the banking network, and mobile service all going
> dark for two days** — **no ATMs, no eSewa, no calls.**"
>
> **Run the question (≈3 min):** "Cyber terrorism's **real damage isn't on a screen; it's in the
> streets.**" Land the agenda: **cascading effects on infrastructure → layered countering (national /
> organizational / personal) → resilience & preparedness.**

> 🎙️ Speaker note: Keep it about **effects and resilience**, not methods. This session **closes the
> unit** and links forward to **Unit 8 (Digital Forensics)** and **Unit 9 (cyber law).**

---

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Effects on Critical Infrastructure `[THEORY]` `[~10 min]`

[SLIDE] **The cascade — power → telecom → banking → hospitals**

> **Deliver:** Define the target and the danger. **Critical infrastructure (CI) = the systems a society
> can't function without.** An attack **rarely stays contained:** **cascading (domino) effects** spread
> from one system to the next, causing **public panic and economic loss** well beyond the first target.
> - **Cascade:** a **power outage** takes **telecom** down, which hits **banking, hospitals, and
>   water.**
> - The damage is **physical and economic**, not merely "digital."
> - **Dependence concentrates risk:** a few **telecom operators and wallets** carry the whole economy.
> - Attacks on **government data centres** also put **citizens' records** at risk.

- 🌍 **Global example:** **prolonged outages** from attacks on **energy / utility control systems**
  causing **regional blackouts.**
- 🇳🇵 **Local example:** dependence on a **few telecom operators** and on **digital wallets (eSewa /
  Khalti / connectIPS)** means an attack on **national payment or telecom infrastructure** could
  **freeze daily commerce**; attacks on **government data centres** risk **citizen records.**

> ❌ **Misconception:** *"Cyber attacks only cause online / digital damage."*
> ✅ **Correction:** "Attacks on **industrial and control systems** can cause **physical, economic, and
> human harm** — blackouts, frozen commerce, risk to hospitals. The **'cyber' part is only the entry
> point**; the damage is very much in the **physical world.**"

> 🖼️ Visual: a **cascade / domino** diagram — **power → telecom → banking / eSewa → hospitals & water →
> public panic.**

> 🎙️ Speaker note: The lesson is the **CASCADE** — one failure topples dependent systems. That's why CI
> protection matters **far more** than the size of any single target suggests.

**📊 Depth table — Infrastructure attacked → cascade → real-world effect**

| If this is hit (Nepal) | The cascade it triggers | Real-world effect on people |
|---|---|---|
| National power / load-dispatch | Telecom & data centres lose power | Blackout; comms and services go dark |
| Telecom operators | Internet, calls, and OTP delivery fail | Wallets and banking become unusable |
| Payment infra (eSewa/Khalti/connectIPS) | Digital commerce halts | Shops, salaries, remittances freeze |
| Banking network | ATMs and transfers stop | People can't access their own money |
| Government data centre | Citizen records exposed/altered | Identity risk; loss of trust in e-gov |
| Aviation / hospital systems | Safety-critical operations disrupted | Direct risk to travel and to life |

*ℹ️ The lesson is the CASCADE: one failure topples dependent systems. This is why CI protection matters far more than the size of any single target suggests.*


#### Concept 2 — Countering It — a layered defence `[THEORY]` `[~10 min]`

[SLIDE] **National + organizational + personal — all must hold**

> **Deliver:** Lay out the three levels. **Countering cyber terrorism is coordinated across national,
> organizational, and personal levels.** **No single level is sufficient**; the **base, middle, and top
> must all hold.**
> - **National:** **CERT / national incident-response teams, critical-infrastructure protection policy,
>   intelligence sharing, legal frameworks, international cooperation.**
> - **Organizational:** **network segmentation, monitoring / intrusion detection, incident-response &
>   business-continuity / disaster-recovery plans, regular drills, backups.**
> - **Personal / citizen:** **awareness, reporting suspicious activity, and NOT amplifying
>   disinformation or panic.**

- 🇳🇵 **Local example:** **Nepal's CERT (NPCERT)** and government IT-security efforts; the role of
  **cyber law (the Electronic Transaction Act — ties forward to Unit 9)** in prosecution; and
  **coordination among NRB, telecoms, and agencies.**

> ❌ **Misconception:** *"Cyber terrorism is only the government's problem."*
> ✅ **Correction:** "Defence needs **all three layers** — national policy and CERTs, organizational
> plans and monitoring, **AND individual citizens** who **report suspicious activity and don't spread
> panic or disinformation.** Leaving it entirely to 'the government' removes **two of the three**
> defensive layers."

> 🖼️ Visual: a **three-layer defence pyramid** — national (base) / organizational (middle) / personal
> (tip).

> 🎙️ Speaker note: Nepal specifics — **NPCERT**, the **Electronic Transaction Act** (forward link to
> Unit 9), and **cross-agency coordination.** Citizens counter it partly by **not amplifying
> disinformation.**

**📊 Depth table — Countering cyber terrorism — by layer**

| Layer | Key measures | Nepal example |
|---|---|---|
| National | CERT, CI-protection policy, intelligence sharing, cyber law, intl cooperation | NPCERT; the Electronic Transaction Act (Unit 9) |
| National | Cross-agency coordination | NRB, telecoms, and government agencies together |
| Organizational | Segmentation, monitoring/IDS, backups | Banks isolating and monitoring core systems |
| Organizational | Incident-response + BCP/DR plans, drills | Tested continuity plans and regular rehearsals |
| Personal / citizen | Awareness; report suspicious activity | Reporting scams/phishing to the bank/CERT |
| Personal / citizen | Don't amplify disinformation/panic | Verifying before resharing during a crisis |

*ℹ️ Defence is a stack: the national base (CERT, law), the organizational middle (segmentation, IR/BCP), and the personal tip (awareness, don't amplify). A gap at any level weakens the whole.*


#### Concept 3 — Resilience & Preparedness `[THEORY]` `[~7 min]`

[SLIDE] **Assume it WILL happen — then recover fast**

> **Deliver:** Define the mindset. **Resilience means ASSUMING attacks will happen and building the
> ability to keep operating and recover fast.** **Preparedness — backups, failover, tested plans, and
> coordination — decides whether an incident is a scare or a catastrophe.**
> - **Assume breach:** plan for **"when", not "if".**
> - **Continuity:** **backups and failover** keep essential services running.
> - **Response:** a **tested incident-response plan and clear communication** limit damage.
> - **Coordination:** working with a **CERT and partners** speeds recovery.

- 🇳🇵 **Mini case (work it, ≈2 min):** a **national bank suffers a service-disrupting attack** — what
  **continuity steps** (backups, failover, public communication, coordination with CERT) **limit the
  damage?** Walk the incident-response cycle end to end.

> ❌ **Misconception:** *"Good defence means never getting attacked."*
> ✅ **Correction:** "**No defence is perfect**, so **hoping it won't happen is not a plan.** Resilience
> **assumes an incident will occur** and invests in **backups, failover, tested response, and
> coordination** — so **recovery is fast** and the **impact is contained.**"

> 🍿 **Fun analogy (deliver it):** "Like **earthquake preparedness in Nepal** — you **can't stop every
> quake**, but **drills, building codes, and a recovery plan** decide whether it's a **scare or a
> catastrophe.**"

> 🖼️ Visual: the **incident-response cycle** — Prepare → Detect → Contain → Eradicate → Recover →
> Review.

> 🎙️ Speaker note: Every step **assumes the attack will come** and is **rehearsed before it does.**
> **Clear public communication** limits panic — the attacker's real goal.

**📊 Depth table — A bank under a disruptive attack — resilience steps in order**

| Incident-response step | What the bank does | Why it limits the damage |
|---|---|---|
| Prepare (before) | Backups, tested BCP/DR, staff drills | Ready to act — no improvising mid-crisis |
| Detect | Monitoring/IDS flags the disruption | Faster detection means less spread |
| Contain | Isolate affected systems; fail over | Stops the cascade to other services |
| Eradicate | Remove the threat from the network | Prevents re-infection on recovery |
| Recover | Restore service from clean backups | Gets customers back online safely |
| Review & communicate | Learn, coordinate with NPCERT, inform the public | Prevents recurrence; limits panic |

*ℹ️ Preparedness is the difference between a scare and a catastrophe: every step assumes the attack will come and is rehearsed before it does. Clear public communication limits panic — the attacker's real goal.*

#### 🛠 ACTIVITY — "Defend one system" `[ACTIVITY]` `[~5 min]`

[SLIDE] **Which piece of Nepal's CI worries you most — and one defence?**

> **Run it:** In pairs (2 min): pick the **piece of Nepal's critical infrastructure that worries you
> most** if attacked. **Name the cascade you fear** (what fails next). Choose **ONE defence to
> prioritise** across the **national / organizational / personal** layers. Take **3–4 answers aloud**
> (3 min); **connect each defence to a layer of the pyramid.**

> 🎙️ Speaker note: Seeds — telecom, national payments (eSewa/connectIPS), power, government data.
> Reward answers that **name the cascade AND pick a concrete, layer-appropriate defence** (e.g. backups
> + BCP at the org layer, NPCERT coordination at the national layer).

---

### 🧠 CHECK FOR UNDERSTANDING `[QUIZ]` `[~5 min]`

**MCQ 1.** The most dangerous feature of an infrastructure attack is:
a) it's online b) ✅ **cascading effects across dependent systems** c) it's slow d) it's visible

**MCQ 2.** A national team that coordinates response to major cyber incidents is a:
a) ISP b) firewall c) ✅ **CERT (Computer Emergency Response Team)** d) VPN

**Discussion prompt:** *Which piece of Nepal's critical infrastructure worries you most if attacked, and what one defence would you prioritise?*

> 🎙️ Speaker note: Draw out the **cascade** concept and the **three defensive layers.** Connect the
> **CERT** answer forward to **Unit 9 (cyber law).**

---

### 💡 REAL-LIFE APPLICATION `[~3 min]`
**This matters because…** organizations now expect employees to **follow incident-response and
business-continuity plans**; understanding **infrastructure resilience** makes you **valuable in any
IT/management role** and a **responsible digital citizen.** Knowing the cascade, the layers, and the
recovery cycle is exactly what an employer wants when the worst day comes.

---

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
1. **Infrastructure attacks cause cascading, real-world harm** — power → telecom → banking → hospitals → panic.
2. **Countering needs three layers:** **national** (CERT/NPCERT, law), **organizational** (segmentation, IR/BCP), and **personal** (awareness).
3. **Resilience & preparedness** — **assume breach, back up, drill, recover** — **beat hoping it won't happen.**

**Next unit (Unit 8):** **Digital Forensics** — how incidents are **investigated after the fact.**

---
---

# 📋 UNIT 7 — END-OF-UNIT QUIZ
*Use as a 15–20 min in-class quiz or a take-home review. Answer key at the end. All attack content stays at recognition/defence level — no operational steps.*

### Section A — Multiple Choice (1 mark each)
1. Social engineering primarily attacks:
   a) firewalls  b) encryption  c) ✅ human psychology / people  d) hardware
2. Humans are the "weakest link" mainly because of:
   a) slow typing  b) ✅ helpfulness, authority, fear, curiosity, brand trust  c) bad passwords only  d) old hardware
3. Attackers prefer social engineering because it is:
   a) more technical  b) ✅ low-cost and high-success vs. beating strong tech  c) always legal  d) slower
4. "I'm calling from the police, act now or face arrest" combines:
   a) liking + scarcity  b) ✅ authority + fear/urgency  c) reciprocity only  d) social proof
5. A fraudulent phone call asking for your OTP is:
   a) phishing  b) smishing  c) ✅ vishing  d) baiting
6. The single best rule against OTP fraud is:
   a) share it only with the bank  b) ✅ never share your OTP with anyone, even "the bank"  c) share if urgent  d) email it
7. A fraudulent SMS with a malicious link (KYC/parcel/lottery) is:
   a) phishing  b) vishing  c) ✅ smishing  d) tailgating
8. What most distinguishes cyber terrorism from ordinary cybercrime?
   a) it uses a computer  b) it is illegal  c) ✅ political/ideological intent to cause fear or serious harm  d) it is online
9. Which is a type of cyber terrorism?
   a) refactoring  b) ✅ propaganda / psy-ops (or a critical-infrastructure attack)  c) backups  d) UAT
10. A national team that coordinates response to major cyber incidents is a:
    a) ISP  b) firewall  c) ✅ CERT (e.g. NPCERT)  d) VPN

### Section B — Short Answer (2 marks each)
11. **Define social engineering.**
12. **List four reasons humans are exploited** by social engineers.
13. **Name and explain three** social-engineering attack types.
14. **List four countermeasures** (personal + organizational).
15. **Define cyber terrorism** and give **two of its types.**

### Section C — Applied Case (3 marks each)
16. Given a **Nepali scam SMS/call transcript**, identify the **attack type**, the **psychological levers used**, and the **correct safe response.**
17. Given a **national-infrastructure attack scenario**, describe the **cascading effects** and **three countering measures** across the **national / organizational / personal** layers.

### Section D — Discussion (open-ended)
18. "**Is a politically motivated defacement of a Nepali government website 'cyber terrorism'?**" Argue **both sides** using **intent, target, and severity**, then state your own position.

---

### ✅ Answer Key (Section A)
1-c · 2-b · 3-b · 4-b · 5-c · 6-b · 7-c · 8-c · 9-b · 10-c

> **Sections B–D: grade on key terms.** Q11 must give "manipulating people into giving up information/
> access, not breaking technology." Q12 — any four of: helpfulness, obedience to authority, fear of
> consequences, urgency, curiosity, trust in familiar brands, low awareness. Q13 must name and explain
> three of phishing (email), vishing (call), smishing (SMS), pretexting (invented story), baiting
> (lure/USB), tailgating (door-following). Q14 — personal: never share OTP, verify independently, check
> links, slow down/report; organizational: awareness training, verify-via-callback, least privilege,
> MFA, email filtering/anti-spoofing, visitor/escort policy. Q15 must give "ideologically/politically
> motivated use of computers to cause serious harm/fear" plus two types (critical-infrastructure attack,
> data destruction, service denial, propaganda/psy-ops, financing). Q16 — reward correct attack-type
> label + named levers (authority/urgency/fear/greed) + a verify-first safe response. Q17 — reward the
> cascade (power→telecom→banking→hospitals) AND one measure per layer (national CERT/law, org
> segmentation/IR/BCP, personal awareness/report). Q18 — reward students who weigh intent, target, and
> severity on both sides rather than a one-word verdict.

---

## ✅ Unit 7 complete (full lecturer-ready depth)
The deck is built: **IT246_Unit7.pptx** (76 slides) — diagram-rich, self-contained, and PDF-safe,
carrying all **17 §7A depth tables** (comparison, concrete-example, and scaffolding) and **12
diagrams** (human-vs-firewall, cost/success quadrant, credential chain-reaction, influence levers, the
social-engineering attack cycle, the attack-type taxonomy, STOP-THINK-CLICK, the intent-vs-severity
map, cyber-terror types, the infrastructure cascade, the layered-defence pyramid, and the
incident-response cycle). This Markdown source carries those **same 17 depth tables inline** under each
concept, so the source of truth and the deck stay in sync. **Framing throughout: defensive / awareness
only — recognise and prevent, never perform; cyber terrorism kept conceptual and responsible.**
