#!/usr/bin/env python3
"""IT220 (fourth) Unit 6 deck — Transaction Processing, Concurrency Control &
Recovery Techniques (S37–S44), built to COURSE_MATERIAL_STANDARD.md INCLUDING the
§7A depth rule: every confusable set is a comparison table, every 'X vs not-X'
concept a concrete-example table, claims get scaffolding tables — each table on its
OWN slide, paginated, never squeezed. Self-contained & PDF-safe two-slide concept
pairs; worked schedule/serializability/recovery problems via add_solved_problem.
Imports deckkit.py. Diagrams in images/ (build_unit6_images.py).
Run: python3 build_unit6_pptx.py -> IT220_Unit6.pptx
"""
from deckkit import *

# ============================================================
#                        BUILD
# ============================================================
add_title("Unit 6 — Transaction Processing, Concurrency Control & Recovery",
          "IT 220: Database Management System  ·  BIM 4th Semester  ·  Sessions S37–S44",
          "Self-contained slides with depth: every concept grounded in comparison & concrete-example TABLES "
          "(Nepal / IT localised — eSewa, bank transfers, ticket booking). A running example (Rita sends "
          "Rs. 500 to Hari) threads the whole unit. Exports to PDF with no information lost.")

add_outcomes("Unit 6 — Learning Outcomes","transactions · concurrency · recovery  ·  s37–s44",
    "By the end of this unit, you will be able to:",
    ["Define a transaction, trace its states, and explain the role of the system log (S37)",
     "State and apply the ACID properties to judge whether a transaction is correct (S38)",
     "Build and analyse schedules; test conflict serializability with a precedence graph (S39)",
     "Apply Two-Phase Locking and Timestamp Ordering, and recognise deadlock vs starvation (S40–S41)",
     "Distinguish deferred / immediate / shadow-paging recovery and design a backup strategy (S42–S44)"],
    "This is Unit 6 of IT 220. It builds on Unit 5's SQL (COMMIT/ROLLBACK are TCL) and answers the question "
    "behind 'your money is safe': how a DBMS keeps data correct despite concurrency and crashes.")

add_roadmap("Unit 6 — Roadmap","Where each session fits (S37–S44)",
    ["S37  Transaction & system concepts · states · the log",
     "S38  ACID — the four guarantees",
     "S39  Schedules · serializability · precedence graph",
     "S40  Two-Phase Locking · deadlock",
     "S41  Timestamp Ordering concurrency control",
     "S42  Recovery: deferred update (NO-UNDO/REDO)",
     "S43  Immediate update · shadow paging",
     "S44  Backup & catastrophic recovery — closes unit"],
    ["Units 1–5   DONE: concepts, ER, relational algebra, normalization, SQL",
     "Unit 7   Advanced topics — tuning, security,",
     "             distributed DBs, warehousing, big data, NoSQL"])

# NOTE on the aliases below: add_comparison_table / add_examples_table are semantic
# aliases of add_table_slide (deckkit §14). Used where they read clearest.

# ============================================================ S37
add_divider("Session 37 · Lecture hour 1 (of 8)","Introduction to Transaction Processing",
    "Rita taps 'Send Rs. 500' on eSewa. The app debits her wallet, then the wifi dies before Hari is credited. "
    "Where did the Rs. 500 go — and how does the system make sure money is never created or destroyed by a half-done action?",
    "OPENING HOOK [~5 min]. Draw out 'all-or-nothing'. Agenda: what a transaction is → single vs multi-user → why "
    "things fail → transaction states → the system log.")

concept_understand("S37 · Concept 1 · [THEORY]","What Is a Transaction",
    "A transaction is a logical unit of work — one or more database operations treated as a single, indivisible action "
    "that must either complete entirely or have no effect at all. It begins with BEGIN and ends with COMMIT (success) "
    "or ABORT/ROLLBACK (undo).",
    ["Its basic operations are read_item(X) and write_item(X) on data items.",
     "BEGIN → operations → COMMIT makes changes permanent; ABORT/ROLLBACK undoes them all.",
     "'Indivisible' means the outside world sees it as one step, never half-done.",
     "An ATM withdrawal is a transaction: read balance → check → debit → dispense — all or nothing."],
    None,"A transaction = one all-or-nothing unit of work, not one SQL line.",
    "~7 min. Say the eSewa transfer aloud as read Rita → debit 500 → credit Hari → commit. One unit, many steps.")
concept_apply("S37 · Concept 1 · [THEORY]","What Is a Transaction",
    "eSewa transfer: read Rita's balance → debit Rs. 500 → credit Hari Rs. 500 → commit. All four steps are one "
    "transaction. If the phone dies after the debit but before the credit, the whole unit is rolled back so Rita's "
    "Rs. 500 is restored — the money is never left in limbo between the two wallets.",
    "\"A transaction = a single SQL statement.\" No — a transaction can group many statements (several reads and "
    "writes) into one indivisible unit. The debit and the credit are two statements inside ONE transaction.",
    "A transaction is a logical unit of work comprising one or more database operations (read_item/write_item) that "
    "are executed as a single, indivisible action — it begins with BEGIN and ends with COMMIT (making changes "
    "permanent) or ABORT/ROLLBACK (undoing them). It must be all-or-nothing: either every operation takes effect or none does.",
    "transaction · logical unit of work · BEGIN/COMMIT/ROLLBACK · read_item/write_item · all-or-nothing")
add_table_slide("S37 · Concept 1 · examples","Everyday actions that are really multi-step transactions",
    ["Action (Nepal / IT)","The steps inside the ONE transaction","What must happen if it fails halfway"],
    [["eSewa: Rita sends Rs. 500 to Hari","read Rita → debit 500 → credit Hari → commit","roll back the debit — restore Rita's balance"],
     ["ATM cash withdrawal","read balance → check → debit → dispense cash","if cash not dispensed, re-credit the account"],
     ["IRCTC / bus ticket booking","reserve seat → charge card → issue ticket","if charge fails, release the held seat"],
     ["NEA electricity bill payment","read due amount → debit wallet → mark bill paid","if 'mark paid' fails, refund the debit"],
     ["Bank fund transfer (A→B)","debit A → credit B → log both","undo the debit if the credit never happens"],
     ["Daraz checkout","reserve stock → charge → create order","release the stock if payment is declined"]],
    per_page=6,widths=[1.9,2.9,2.6],fs=11,
    note="Each is ONE transaction made of several operations. 'All-or-nothing' is why none of them can leave you charged "
         "with nothing to show, or credited with nothing paid.")

concept_understand("S37 · Concept 2 · [THEORY]","Single-User vs Multi-User & Why It Matters",
    "A single-user system runs one transaction at a time; a multi-user system lets many transactions interleave and run "
    "concurrently. Concurrency — many transactions touching the same data at once — is the entire reason this unit exists.",
    ["Multi-user DBMSs interleave operations of different transactions to keep the CPU and disk busy.",
     "Interleaving is efficient, but uncontrolled interleaving can corrupt shared data.",
     "This motivates concurrency control (S39–S41): rules that make interleaving safe.",
     "Thousands of Dashain shoppers checking out on Daraz at once is the everyday multi-user case."],
    None,"One-at-a-time is easy; many-at-once is why concurrency control exists.",
    "~6 min. Preview: two people paying the same NEA bill in the same second — a concurrency problem we'll fix in S39.")
concept_apply("S37 · Concept 2 · [THEORY]","Single-User vs Multi-User & Why It Matters",
    "During Dashain, thousands of Daraz shoppers check out at the same second and many eSewa transfers run at once. The "
    "DBMS interleaves their operations rather than forcing a queue of one-at-a-time — but that interleaving must be "
    "controlled, or two people paying the same NEA bill could both 'succeed' and corrupt the record.",
    "\"Concurrency always corrupts data.\" No — only SOME interleavings are unsafe; the DBMS's job (S39–S41) is to allow "
    "the safe ones and block the unsafe ones, so concurrency is both fast AND correct.",
    "A single-user system executes one transaction at a time, while a multi-user system allows many transactions to "
    "interleave and execute concurrently for efficiency. Because concurrent access to shared data can corrupt it if "
    "uncontrolled, multi-user systems require concurrency control — the motivation for schedules, locking, and "
    "timestamp ordering studied later in this unit.",
    "single-user · multi-user · concurrency · interleaving · concurrency control (motivation)")

concept_understand("S37 · Concept 3 · [THEORY]","Why Transactions Go Wrong — Types of Failure",
    "Transactions can fail in several ways, and recovery (S42–S44) must handle each. The standard categories are computer "
    "crash, transaction/system error, local logical error, concurrency-enforcement abort, disk failure, and physical catastrophe.",
    ["System crash: power/hardware/software failure wipes main memory (the buffer) mid-transaction.",
     "Transaction/local error: bad input, insufficient balance, division by zero → the transaction aborts itself.",
     "Concurrency enforcement: the DBMS aborts a transaction to break a deadlock or preserve serializability.",
     "Disk failure / physical catastrophe: the media or whole data-center is destroyed (S44's problem)."],
    None,"Failures range from a mid-txn crash to a whole data-center gone.",
    "~6 min. Local example: load-shedding kills a bank server mid-batch; a Ntc data-center power trip. Different failures, different fixes.")
concept_apply("S37 · Concept 3 · [THEORY]","Why Transactions Go Wrong — Types of Failure",
    "Load-shedding cuts power to a Nepali bank server mid-batch (system crash — buffer lost); Rita tries to send Rs. 500 "
    "with only Rs. 300 (local error — transaction aborts itself); the DBMS aborts one of two frozen transfers to break a "
    "deadlock (concurrency enforcement); a fire destroys the disk array (catastrophe — needs S44's backup).",
    "\"A failure always means the hardware broke.\" Many failures are logical (insufficient balance, a deadlock the DBMS "
    "chose to break) — the transaction aborts cleanly and the data stays consistent. Not every abort is a disaster.",
    "Transactions fail through: system crashes (memory/buffer lost), transaction or system errors, local logical errors "
    "(e.g. insufficient balance), concurrency-control enforcement (the DBMS aborts a transaction to preserve correctness "
    "or break a deadlock), disk failures, and physical catastrophes. Recovery techniques (S42–S44) are designed to "
    "restore a consistent state after each kind.",
    "system crash · transaction/local error · concurrency enforcement · disk failure · physical catastrophe")
add_table_slide("S37 · Concept 3 · examples","Each failure type → a Nepali example → how recovery responds",
    ["Failure type","Example (Nepal / IT)","How the system recovers"],
    [["System crash (memory lost)","Load-shedding kills a bank server mid-batch","Reboot → scan log → REDO committed, UNDO the rest"],
     ["Transaction / local error","Rita sends Rs. 500 with only Rs. 300","Transaction aborts itself; no change made"],
     ["System error","Division by zero in a report job","Abort the transaction; log the error"],
     ["Concurrency enforcement","DBMS aborts one txn to break a deadlock","Abort victim, restart it later"],
     ["Disk / media failure","A hard-disk array fails at a data-center","Restore from backup + archived log (S44)"],
     ["Physical catastrophe","Earthquake / fire destroys the data-center","Off-site backup is the only recovery (S44)"]],
    per_page=6,widths=[2.0,2.8,2.7],fs=11,
    note="The first four are non-catastrophic (disk intact → log-based recovery, S42–S43). The last two are catastrophic "
         "(disk gone → only a separate backup saves you, S44).")

concept_understand("S37 · Concept 4 · [THEORY]","Transaction States & the State Diagram",
    "A transaction moves through defined states: Active (executing operations) → Partially Committed (last operation done, "
    "not yet made permanent) → Committed (changes durable). If anything goes wrong it enters Failed → Aborted (terminated, "
    "rolled back).",
    ["Active: the transaction is reading and writing data items.",
     "Partially committed: all operations executed, but changes not yet flushed to stable storage.",
     "Committed: the commit succeeded and changes are durable — the point of no return.",
     "Failed → Aborted: an error occurs; the transaction is rolled back and terminated."],
    "s37_states.png","Active → Partially committed → Committed; any failure → Failed → Aborted.",
    "~8 min. Walk the eSewa transfer around the diagram — commit is the point of no return; before that a failure just rolls back.")
concept_apply("S37 · Concept 4 · [THEORY]","Transaction States & the State Diagram",
    "Rita's transfer is Active while it reads and debits; Partially Committed the instant the credit to Hari is computed "
    "but not yet flushed to disk; Committed once eSewa shows 'Transfer successful' and the log is safely stored. Had the "
    "wifi died during the debit, it would go Failed → Aborted, and Rita's balance would be restored.",
    "\"Partially committed means it's done and safe.\" No — a partially committed transaction is NOT durable yet; a crash "
    "before the commit record is flushed can still lose it. Only the Committed state is safe.",
    "A transaction's states are: Active (executing read/write operations), Partially Committed (all operations done but "
    "changes not yet made permanent), Committed (changes durably stored), Failed (an error occurred), and Aborted "
    "(rolled back and terminated). The success path is Active → Partially Committed → Committed; any failure diverts to "
    "Failed → Aborted, undoing all changes.",
    "active · partially committed · committed · failed · aborted · rollback · commit point")

concept_understand("S37 · Concept 5 · [THEORY]","The System Log (Journal)",
    "The system log is a sequential record, on stable storage, of every write a transaction makes — kept so the system "
    "can REDO or UNDO changes after a failure. It is the safety net behind durability and recovery.",
    ["Entry types: [start,T], [write,T,X,old_value,new_value], [commit,T], [abort,T], [checkpoint].",
     "The old value in a write record enables UNDO; the new value enables REDO.",
     "The log lives on stable storage so it survives a crash of main memory.",
     "Write-Ahead Logging (S42): the log record is written BEFORE the data page — guaranteeing recoverability."],
    "s37_log.png","The log is a khata: note every entry before acting, so you can retrace.",
    "~7 min. Analogy: the log is like a shopkeeper's khata (ledger) — every entry recorded before acting, so nothing is lost.")
concept_apply("S37 · Concept 5 · [THEORY]","The System Log (Journal)",
    "For Rita's transfer, the log records [start,T], then [write,T,RitaBal,2000,1500] and [write,T,HariBal,1000,1500] — "
    "each with the OLD and NEW value — then [commit,T]. If the server crashes, the DBMS replays this log: the old values "
    "let it UNDO an unfinished transfer, the new values let it REDO a committed one.",
    "\"The log is just an error message for developers.\" No — the log is the load-bearing record of every write, stored "
    "on stable storage; recovery is literally impossible without it. It is data, not a debug print.",
    "The system log (journal) is a sequential record on stable storage of every write operation, with entries such as "
    "[start,T], [write,T,X,old,new], [commit,T], and [abort,T]. The old values enable UNDO and the new values enable "
    "REDO after a failure. It is the foundation of durability and recovery, written under the Write-Ahead Logging rule.",
    "system log/journal · [start]/[write]/[commit]/[abort] · old value = UNDO · new value = REDO · stable storage")
add_table_slide("S37 · Concept 5 · scaffolding","Reading the log: each record type and its recovery job",
    ["Log record","What it stores","Its job in recovery"],
    [["[start, T]","Transaction T has begun","Marks where T's work starts in the log"],
     ["[write, T, X, old, new]","T changed item X from old → new","old value → UNDO;  new value → REDO"],
     ["[read, T, X]","T read item X (some systems)","Not needed for undo/redo; used for analysis"],
     ["[commit, T]","T committed successfully","Tells recovery to REDO T (it is durable)"],
     ["[abort, T]","T was rolled back","Tells recovery to UNDO / ignore T"],
     ["[checkpoint]","Buffers flushed at this point","Limits how far back recovery must scan (S42)"]],
    per_page=6,widths=[2.1,2.7,2.7],fs=11,
    note="Recovery is just disciplined reading of this log: REDO transactions with both [start] and [commit]; UNDO those "
         "with [start] but no [commit]. Every technique in S42–S44 is built on these records.")

add_activity("S37 — 'Spot the transaction'  ·  ~5 min",
    ["In pairs (2 min): name one phone action that is really a multi-step transaction (not a single tap).",
     "List its steps, and say what should happen if it fails halfway through.",
     "Take 3–4 answers aloud (3 min); mark which step is the 'point of no return'.",
     "Close: every good example is all-or-nothing — a half-done version would corrupt data or money."],
    "Seeds: eSewa/Khalti transfer, bus/movie ticket booking, mobile top-up, Daraz checkout. Push students to name the "
    "rollback (undo the debit, release the seat) and to locate the commit point.",
    "ACTIVITY [~5 min].")
add_quiz("S37 — Quick Check  ·  ~5 min",
    [("Q1.  A transaction that has executed all its operations but is not yet made permanent is in which state?","q"),
     ("a) active   b) ✅ partially committed   c) committed   d) aborted","a"),
     ("     Why: all ops are done but changes aren't durable yet — a crash here can still lose it.","o"),
     ("Q2.  Which log record lets the system UNDO a change?","q"),
     ("a) [commit]   b) ✅ the old value in [write,T,X,old,new]   c) [start]   d) [checkpoint]","a"),
     ("     Why: the old value is what the change is rolled back to; the new value is for REDO.","o"),
     ("Discussion: describe one phone action that is really a multi-step transaction, and what should happen if it fails halfway.","o")],
    "QUIZ [~5 min]. Draw out the partially-committed-is-not-safe point and the log's undo/redo role.")
add_summary("S37 · Summary  ·  [~2 min]",
    ["A transaction is an all-or-nothing logical unit of work (BEGIN → ops → COMMIT / ROLLBACK), not a single SQL line.",
     "It moves through defined states (Active → Partially Committed → Committed; or Failed → Aborted); commit is the point of no return.",
     "The system log records every write (old + new values) on stable storage so failures can be UNDONE or REDONE."],
    "Every eSewa/Khalti payment and every bank fund transfer is wrapped in a logged transaction — this is the safety net "
    "behind the promise 'your money is safe'. Understanding it is expected of any fintech or backend developer in Nepal.",
    "S38 — the four guarantees every correct transaction must keep: ACID.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S38
add_divider("Session 38 · Lecture hour 2 (of 8)","Desirable Properties of Transactions — ACID",
    "Rita's Rs. 500 was debited but never credited to Hari — and the bank just says 'the system was busy'. Which promise "
    "did the system break? Every correct transaction must keep four promises: A, C, I, D.",
    "OPENING HOOK [~5 min]. Introduce ACID as four promises, each preventing a specific eSewa failure. Agenda: A → C → I → D → ACID as a checklist.")

concept_understand("S38 · Concept 1 · [THEORY]","Atomicity",
    "Atomicity guarantees that all operations of a transaction happen, or none do — there are no half-done transactions. "
    "If a transaction cannot complete, every change it made is rolled back.",
    ["The transaction is treated as a single indivisible ('atomic') step by the outside world.",
     "On failure, the recovery manager uses the log's old values to UNDO partial changes.",
     "It is the direct enforcement of the 'all-or-nothing' idea from S37.",
     "Atomicity is what makes a debit-without-credit impossible to leave behind."],
    "s38_acid.png","Atomicity = all-or-nothing; a half-done transaction is undone.",
    "~7 min. eSewa: both the debit AND the credit, or roll back both. Never one without the other.")
concept_apply("S38 · Concept 1 · [THEORY]","Atomicity",
    "eSewa transfer: the system must perform BOTH the debit from Rita AND the credit to Hari, or neither. If the credit "
    "fails, atomicity forces a rollback of the debit, so Rita's Rs. 500 reappears in her wallet — the money is never "
    "silently lost between the two accounts.",
    "\"If the app crashes, it just leaves things as they are.\" No — an incomplete transaction must be UNDONE (rolled "
    "back), not frozen half-done. 'Leaving it as-is' after a debit-but-no-credit is exactly the corruption atomicity prevents.",
    "Atomicity is the ACID property guaranteeing that all of a transaction's operations execute completely or not at all "
    "— there are no partial transactions. If a transaction fails, the recovery manager rolls back every change it made "
    "(using the log's old values). In the eSewa transfer, atomicity ensures both the debit and credit happen, or neither does.",
    "atomicity · all-or-nothing · rollback · no partial transactions · recovery manager")

concept_understand("S38 · Concept 2 · [THEORY]","Consistency",
    "Consistency guarantees that a transaction takes the database from one valid state to another valid state, preserving "
    "all integrity constraints and invariants. A correctly written transaction, run alone, never violates a rule.",
    ["An invariant is a rule that must always hold — e.g. total money in the system is unchanged by a transfer.",
     "Before and after any transfer, the sum of all balances must be equal.",
     "It is a shared responsibility: the DBMS enforces constraints, the developer writes correct logic.",
     "A bug that credits twice (creating money) breaks consistency even if atomicity held."],
    None,"Consistency = valid state → valid state; the invariant is never broken.",
    "~7 min. Show the sum: before = Rita 2000 + Hari 1000 = 3000; after = 1500 + 1500 = 3000. The invariant holds.")
concept_apply("S38 · Concept 2 · [THEORY]","Consistency",
    "Before the transfer: Rita Rs. 2000 + Hari Rs. 1000 = Rs. 3000. After: Rita Rs. 1500 + Hari Rs. 1500 = Rs. 3000. The "
    "invariant 'total money is conserved' is preserved — that is consistency. A bug that credited Hari twice (Rs. 2000 "
    "total after) would create money from nothing and break consistency.",
    "\"Consistency is the same thing as atomicity.\" No — atomicity is about all-or-nothing execution; consistency is "
    "about not violating the rules/invariants. A fully-executed (atomic) transaction can still leave the DB inconsistent "
    "if its logic is wrong (e.g. double-credit).",
    "Consistency is the ACID property guaranteeing that a transaction moves the database from one valid state to another, "
    "preserving all integrity constraints and invariants (such as 'total money is conserved' in a transfer). The DBMS "
    "enforces declared constraints and the developer supplies correct logic; a transaction that broke an invariant "
    "(e.g. double-crediting) would violate consistency.",
    "consistency · valid state → valid state · integrity constraints · invariant · conservation of money")
add_examples_table("S38 · Concept 2 · examples","Consistency: preserving the invariant (money is conserved)",
    ["Scenario","Before","After — correct","What a bug would do (violates consistency)"],
    [["Rita → Hari Rs. 500","Rita 2000, Hari 1000 (=3000)","Rita 1500, Hari 1500 (=3000)","credit Hari twice → 3500 (money created)"],
     ["eSewa cashback Rs. 50","Wallet 200 (+bank)","Wallet 250, promo-fund −50","cashback with no matching debit → money created"],
     ["Bank A → B Rs. 10,000","A 50k, B 20k (=70k)","A 40k, B 30k (=70k)","debit A but skip credit B → 60k (money lost)"],
     ["Ticket refund Rs. 800","Seat sold, wallet 100","Seat freed, wallet 900","refund without freeing seat → seat double-sold"],
     ["NEA bill Rs. 1200","Wallet 2000, bill due","Wallet 800, bill paid","mark paid without debit → revenue lost"],
     ["Daraz order Rs. 3000","Stock 5, wallet 5000","Stock 4, wallet 2000","charge without reducing stock → oversell"]],
    per_page=6,widths=[1.7,1.7,1.9,2.7],fs=10.5,
    note="Consistency = the invariant (money conserved, stock matched, seat count correct) holds before AND after. The "
         "last column is money/goods appearing or vanishing — exactly what consistency forbids.")

concept_understand("S38 · Concept 3 · [THEORY]","Isolation",
    "Isolation guarantees that concurrently executing transactions do not interfere with each other — each transaction "
    "behaves as if it were running alone, even though the DBMS interleaves them for efficiency.",
    ["Transactions interleave (for speed) but must APPEAR to run one after another.",
     "No transaction should see another's uncommitted, half-finished changes.",
     "Isolation is enforced by concurrency control (locking S40, timestamps S41).",
     "Weaker isolation levels trade some safety for more concurrency (a real DBMS setting)."],
    None,"Isolation = interleave freely, but each txn appears to run alone.",
    "~7 min. Analogy: separate queues at separate bank counters — you don't grab cash from the next person's stack mid-count.")
concept_apply("S38 · Concept 3 · [THEORY]","Isolation",
    "Rita sends money to Hari at the same moment Hari sends money to a shop. Isolation ensures neither transaction sees "
    "the other's half-finished state: Hari's outgoing payment doesn't read a balance that Rita's incoming transfer has "
    "only partly written. Each behaves as if it ran alone, so the final balances are correct.",
    "\"Isolation means transactions run strictly one-at-a-time.\" No — they INTERLEAVE for efficiency; isolation only "
    "requires that the RESULT is as if they ran in some serial order. Serial execution is one way to get isolation, not "
    "the definition of it.",
    "Isolation is the ACID property guaranteeing that concurrent transactions do not interfere: each behaves as though it "
    "executed alone, even though the DBMS interleaves their operations. No transaction sees another's uncommitted "
    "changes. It is enforced by concurrency-control techniques (two-phase locking, timestamp ordering), and the "
    "equivalent serial order is the correctness standard (serializability, S39).",
    "isolation · no interference · interleave but appear alone · uncommitted data hidden · concurrency control")

concept_understand("S38 · Concept 4 · [THEORY]","Durability",
    "Durability guarantees that once a transaction has committed, its changes survive any subsequent failure — including "
    "a power cut or crash. Committed means permanent.",
    ["Achieved via the log written to stable storage plus flushing at commit.",
     "Even if the data page is still only in the buffer, the committed log record lets recovery REDO it.",
     "This is why 'Transfer successful' can be trusted the instant it appears.",
     "Durability is the 'D' that recovery techniques (S42–S44) exist to guarantee."],
    None,"Durability = once committed, it survives any later crash.",
    "~6 min. After eSewa shows 'Transfer successful', a power cut must NOT erase it. The committed log record guarantees this.")
concept_apply("S38 · Concept 4 · [THEORY]","Durability",
    "The instant eSewa shows Rita 'Transfer successful', durability guarantees that a power cut one second later cannot "
    "erase the transfer. Even if the updated balance is still sitting in the buffer (not yet on disk), the committed log "
    "record on stable storage lets recovery REDO the change after reboot.",
    "\"Data is written to disk the instant you commit.\" Not necessarily — the data page may still be in the buffer. What "
    "guarantees durability is the LOG record flushed to stable storage at commit, not the data page itself (S42's WAL idea).",
    "Durability is the ACID property guaranteeing that once a transaction commits, its changes persist through any "
    "subsequent failure. It is achieved by writing the transaction's log records to stable storage at commit time, so "
    "even if the updated data pages are still in the buffer when a crash occurs, recovery can REDO the committed changes. "
    "'Committed' therefore means permanent.",
    "durability · committed = permanent · survives crashes · log on stable storage · REDO from log")
add_comparison_table("S38 · ACID · comparison","ACID as a checklist — each letter, its job, and the eSewa failure it prevents",
    ["Property","One-word job","What it guarantees","eSewa failure it prevents"],
    [["Atomicity","All-or-nothing","Every op happens or none do","Rita debited but Hari never credited"],
     ["Consistency","Valid → valid","Invariants/constraints preserved","A double-credit creating money from nothing"],
     ["Isolation","No interference","Concurrent txns appear to run alone","Two transfers reading each other's half state"],
     ["Durability","Survives crashes","Committed changes are permanent","'Transfer successful' erased by a power cut"],
     ["(together)","Correctness","A trustworthy transaction","The reason NRB trusts digital wallets"],
     ["(enforced by)","Log + CC","Log = A/C/D; concurrency control = I","—"]],
    per_page=6,widths=[1.4,1.5,2.6,2.9],fs=11,
    note="ACID is the literal reason regulators (Nepal Rastra Bank) trust digital wallets, and 'explain ACID' is a "
         "near-certain fintech interview question. Map each letter to the failure it stops.")

add_solved_problem("S38 · Solved problem · [EXAMPLE]","Trace Rita → Hari Rs. 500 through A, I, and D",
    "Rita (balance 2000) sends Rs. 500 to Hari (balance 1000). Show what Atomicity, Isolation, and Durability each "
    "guarantee, and what the log records at each step.",
    ["Atomicity — the debit (Rita 2000→1500) and credit (Hari 1000→1500) are ONE unit: both, or neither. If the credit "
     "fails, the debit is rolled back using the log's old value (2000).",
     "Isolation — if Hari is simultaneously paying a shop, his transaction must not read Rita's half-written balance; "
     "each appears to run alone, so no update is lost.",
     "Durability — once eSewa shows 'Transfer successful', the committed log record on stable storage means a power cut "
     "cannot undo it; recovery will REDO if needed.",
     "Log trace: [start,T] → [write,T,RitaBal,2000,1500] → [write,T,HariBal,1000,1500] → [commit,T]."],
    "A = both debit and credit or neither (rollback via old values). I = neither transfer sees the other's uncommitted "
    "state. D = the committed log record survives the crash. Consistency holds throughout: 3000 before = 3000 after.",
    "SOLVED PROBLEM [~8 min]. This is exam Q16 — students should be able to narrate the log trace and the three guarantees.")

add_activity("S38 — 'Name the broken promise'  ·  ~5 min",
    ["In pairs (2 min): for each mini-scenario, decide WHICH ACID property was broken.",
     "(a) money debited, never credited; (b) 'success' shown then erased by a crash; (c) a double-credit created money; (d) two transfers corrupted each other.",
     "Take answers aloud (3 min): (a) Atomicity, (b) Durability, (c) Consistency, (d) Isolation.",
     "Close: every real payment bug maps to exactly one ACID letter — that's why the acronym is worth memorising."],
    "(a) Atomicity — half-done. (b) Durability — committed change lost. (c) Consistency — invariant broken. (d) Isolation "
    "— interference. Reward students who can also name the mechanism (log, locks) that would have prevented it.",
    "ACTIVITY [~5 min].")
add_quiz("S38 — Quick Check  ·  ~5 min",
    [("Q1.  'Once committed, it survives a crash' is which property?","q"),
     ("a) atomicity   b) consistency   c) isolation   d) ✅ durability","a"),
     ("     Why: durability = committed changes are permanent, guaranteed by the log on stable storage.","o"),
     ("Q2.  Two transactions interleaving but not corrupting each other is ensured by:","q"),
     ("a) atomicity   b) ✅ isolation   c) durability   d) consistency","a"),
     ("     Why: isolation makes concurrent transactions appear to run alone.","o"),
     ("Discussion: give a real Nepali payment scenario where breaking CONSISTENCY would let money appear or vanish.","o")],
    "QUIZ [~5 min]. Draw out that atomicity ≠ consistency — a fully-run transaction can still be inconsistent if its logic is wrong.")
add_summary("S38 · Summary  ·  [~2 min]",
    ["Atomicity = all-or-nothing; Consistency = valid state → valid state (invariants preserved).",
     "Isolation = concurrent transactions don't interfere (appear to run alone); Durability = committed changes survive crashes.",
     "A/C/D are guaranteed mainly by the log; Isolation is guaranteed by concurrency control (S40–S41)."],
    "ACID is why NRB and customers trust eSewa, Khalti, and every bank app — and 'explain ACID' is one of the most common "
    "fintech/backend interview questions in Nepal and abroad. Know each letter with an example.",
    "S39 — when many transactions run together, which interleavings are actually safe? Schedules & serializability.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S39
add_divider("Session 39 · Lecture hour 3 (of 8)","Serializable Schedules",
    "Rita and Hari both top-up from the SAME shared family eSewa wallet at the exact same second. Whose top-up 'wins' — "
    "and is the final balance right? A schedule decides whether concurrent transactions stay correct.",
    "OPENING HOOK [~5 min]. Motivate correctness of interleaving. Agenda: schedules → the lost-update problem → serializable "
    "schedules → conflicting operations → the precedence graph.")

concept_understand("S39 · Concept 1 · [THEORY]","Schedules (Histories)",
    "A schedule (history) is an ordering of the operations of several transactions, preserving the order within each "
    "transaction. A serial schedule runs one transaction completely before the next; a non-serial (concurrent) schedule "
    "interleaves their operations.",
    ["A serial schedule is always correct but wastes time (no concurrency).",
     "A non-serial schedule interleaves operations to run faster — but may or may not be correct.",
     "Operations within a single transaction keep their relative order in any schedule.",
     "The goal: get the SPEED of a non-serial schedule with the CORRECTNESS of a serial one."],
    None,"A schedule orders interleaved ops; serial = one-at-a-time, non-serial = interleaved.",
    "~7 min. Show T1 (Rita +500) and T2 (Hari +300) on the family wallet, once serial, once interleaved.")
concept_apply("S39 · Concept 1 · [THEORY]","Schedules (Histories)",
    "On the family wallet, T1 (Rita +500) and T2 (Hari +300) can run serially (T1 fully, then T2) or interleaved "
    "(read/write operations mixed). The serial order is obviously correct — final balance = start + 800 — but slow at "
    "scale; the DBMS wants a fast interleaving that gives the SAME result.",
    "\"Any interleaving is just as good as running them one at a time.\" No — some interleavings corrupt data (the "
    "lost-update problem, next). Only interleavings equivalent to SOME serial order are safe.",
    "A schedule (history) is a total ordering of the operations of a set of transactions that preserves each "
    "transaction's internal operation order. A serial schedule executes transactions one at a time (correct but with no "
    "concurrency); a non-serial (concurrent) schedule interleaves their operations for efficiency but must be checked "
    "for correctness. The aim is concurrency that behaves like some serial order.",
    "schedule/history · serial vs non-serial · interleaving · preserves per-transaction order")

concept_understand("S39 · Concept 2 · [THEORY] [EXAMPLE]","The Lost-Update Problem",
    "The lost-update problem is a concurrency anomaly where two transactions read the same value, then both write back "
    "based on it, so one update overwrites (loses) the other. It is the classic reason uncontrolled interleaving is unsafe.",
    ["Both transactions read the old balance before either writes → they work from a stale value.",
     "The second write overwrites the first, so one top-up simply vanishes.",
     "Other anomalies: dirty read (reading uncommitted data) and incorrect summary.",
     "The fix is concurrency control (locking / timestamps) that forces a safe order."],
    "s39_lost_update.png","Lost update: both read old value → one write overwrites the other.",
    "~8 min. Work the numbers: both read 1000, T1 writes 1500, T2 writes 1300 → final 1300, and T1's +500 is lost.")
concept_apply("S39 · Concept 2 · [THEORY] [EXAMPLE]","The Lost-Update Problem",
    "Family wallet at Rs. 1000. Rita's top-up (+500) and Hari's top-up (+300) both READ 1000 first. Rita writes 1500; "
    "Hari then writes 1300 — overwriting Rita's update. Final balance = 1300, but it should be 1800. Rita's Rs. 500 "
    "top-up is silently LOST because both worked from the same stale read.",
    "\"Concurrency always corrupts data.\" No — only unsafe interleavings do. If Hari's transaction had read AFTER Rita's "
    "write (a serializable order), the result would be correct. The problem is the ordering, not concurrency itself.",
    "The lost-update problem occurs when two concurrent transactions read the same data item and then both write back a "
    "value based on the value they read, so the second write overwrites and loses the first update. In the family-wallet "
    "example both read 1000 and one top-up is lost. It (with dirty read and incorrect summary) shows why uncontrolled "
    "interleaving is unsafe and motivates concurrency control.",
    "lost update · dirty read · incorrect summary · stale read · overwrite · concurrency anomaly")
add_examples_table("S39 · Concept 2 · examples","Concurrency anomalies — what goes wrong and the fix",
    ["Anomaly","What happens (Nepal / IT)","Result","Fix"],
    [["Lost update","Two top-ups read Rs.1000, both write back","One top-up vanishes","lock/serialize the writes"],
     ["Dirty read","T2 reads Rita's balance mid-transfer, T1 aborts","T2 used data that never existed","don't read uncommitted data"],
     ["Incorrect summary","A report sums balances while transfers run","Total is off by an in-flight amount","isolate the reporting txn"],
     ["Unrepeatable read","A balance re-read in one txn gives two values","Inconsistent decision","hold the read lock"],
     ["Phantom","Count of 'today's txns' changes mid-report","New rows appear unexpectedly","range/predicate locking"],
     ["Double booking","Two users book the last bus seat at once","Seat sold twice","serialize on the seat row"]],
    per_page=6,widths=[1.7,2.9,1.9,1.8],fs=10.5,
    note="Every one of these is a specific bad interleaving. Concurrency control (S40 locking, S41 timestamps) exists to "
         "allow the safe interleavings and block exactly these.")

concept_understand("S39 · Concept 3 · [THEORY]","Serializable Schedules",
    "A schedule is serializable if its effect is equivalent to SOME serial execution of the same transactions. "
    "Serializability is the gold standard of correctness for concurrent execution: a serializable schedule is guaranteed correct.",
    ["'Equivalent to a serial order' means the final database state is the same as if run one-at-a-time.",
     "There may be several valid serial orders; matching any ONE of them is enough.",
     "Conflict serializability (next) is the practical, testable form used by real DBMSs.",
     "If a schedule is serializable, no anomaly like lost update can occur."],
    None,"Serializable = interleaved, but equals SOME one-at-a-time order.",
    "~7 min. Analogy: interleaved tasks that, when you squint, are equivalent to doing one full task then the next.")
concept_apply("S39 · Concept 3 · [THEORY]","Serializable Schedules",
    "The DBMS behind eSewa or Daraz checkout accepts a fast interleaving of thousands of transactions ONLY if it is "
    "serializable — equivalent to some order of running them one after another. That guarantee is why your balance is "
    "never 'lost' during peak Dashain traffic, even though everything is running concurrently.",
    "\"Serializable means the schedule IS serial.\" No — a serializable schedule is usually NON-serial (interleaved); it "
    "just has the same EFFECT as some serial order. Serial is a special case; serializable is the useful general property.",
    "A schedule is serializable if it is equivalent in effect to some serial execution of the same transactions — i.e. "
    "the final database state matches running them one at a time in some order. Serializability is the correctness "
    "standard for concurrency: a serializable schedule cannot produce anomalies like lost updates. The practical, "
    "testable form is conflict serializability.",
    "serializable schedule · equivalent to a serial order · correctness standard · conflict serializability")

concept_understand("S39 · Concept 4 · [THEORY]","Conflicting Operations & Conflict Serializability",
    "Two operations conflict if they belong to different transactions, act on the SAME data item, and at least one is a "
    "WRITE. A schedule is conflict-serializable if it can be turned into a serial schedule by swapping only "
    "non-conflicting adjacent operations.",
    ["The three conflict types on the same item: write-write, read-write, and write-read.",
     "Read-read on the same item does NOT conflict (both just read).",
     "Operations on DIFFERENT items never conflict; operations in the same transaction aren't 'conflicts'.",
     "Swapping non-conflicting operations doesn't change the result — that's the test for equivalence."],
    None,"Conflict = same item, different txns, at least one write (W-W, R-W, W-R).",
    "~8 min. T1's write on the wallet vs T2's read on the same wallet = conflict; two reads of the wallet = no conflict.")
concept_apply("S39 · Concept 4 · [THEORY]","Conflicting Operations & Conflict Serializability",
    "On the family wallet, T1's write(wallet) and T2's read(wallet) CONFLICT — swapping them changes what T2 sees, so "
    "their order matters. But T1's read(wallet) and T2's read(wallet) do NOT conflict — two reads can be freely reordered. "
    "Conflict serializability checks whether reordering only the non-conflicting ops can reach a serial schedule.",
    "\"Any two operations on the same item conflict.\" No — two READS of the same item do not conflict (neither changes "
    "it). A conflict needs at least one WRITE plus different transactions plus the same item.",
    "Two operations conflict if they are from different transactions, access the same data item, and at least one is a "
    "write (the conflict types are write-write, read-write, and write-read). A schedule is conflict-serializable if it "
    "can be transformed into a serial schedule by swapping only non-conflicting adjacent operations — a testable, "
    "sufficient condition for serializability used by real DBMSs.",
    "conflict · same item + different txn + ≥1 write · W-W/R-W/W-R · read-read never conflicts · conflict-serializable")
add_comparison_table("S39 · Concept 4 · comparison","Do these two operations conflict? (same data item)",
    ["T_i operation","T_j operation","Conflict?","Why"],
    [["read(X)","read(X)","No","neither changes X — order doesn't matter"],
     ["read(X)","write(X)","Yes (R-W)","T_j changes what T_i reads"],
     ["write(X)","read(X)","Yes (W-R)","T_j reads what T_i wrote"],
     ["write(X)","write(X)","Yes (W-W)","final value depends on order"],
     ["read/write(X)","read/write(Y)","No","different items — independent"],
     ["two ops of the SAME txn","—","N/A","conflicts are only ACROSS transactions"]],
    per_page=6,widths=[1.9,1.9,1.4,2.8],fs=11,
    note="Rule of thumb: a conflict needs different transactions + the same item + at least one write. Read-read and "
         "different-item pairs are always safe to reorder.")

concept_understand("S39 · Concept 5 · [THEORY] [EXAMPLE]","The Precedence (Serialization) Graph",
    "A precedence graph has one node per transaction and a directed edge Ti → Tj whenever an operation of Ti precedes and "
    "conflicts with an operation of Tj on the same item. The rule: a schedule is conflict-serializable if and only if its "
    "precedence graph has NO cycle.",
    ["Draw a node for each transaction, then add an edge for every conflicting pair in schedule order.",
     "No cycle → the graph gives a valid serial order (topological sort) → serializable.",
     "A cycle → there is no consistent serial order → NOT conflict-serializable.",
     "A cycle here means 'not serializable' — it is NOT the same as a deadlock (that is S40)."],
    "s39_precedence.png","Conflict-serializable ⟺ the precedence graph has NO cycle.",
    "~8 min. Draw one acyclic (serializable) and one cyclic (not) graph; stress cycle ≠ deadlock.")
concept_apply("S39 · Concept 5 · [THEORY] [EXAMPLE]","The Precedence (Serialization) Graph",
    "Build a precedence graph for the day's wallet transactions: if T1 writes the wallet before T2 reads it, draw "
    "T1 → T2. If the edges form a straight chain (T1→T2→T3), there's no cycle → the schedule is serializable and safe. "
    "If you also find T2 → T1, that cycle means no serial order exists → the schedule must be rejected or reordered.",
    "\"A cycle in the precedence graph means deadlock.\" No — here a cycle means the schedule is NOT conflict-serializable. "
    "Deadlock (a cycle in the WAIT-FOR graph, S40) is a different idea about transactions waiting on each other's locks.",
    "A precedence (serialization) graph has a node per transaction and a directed edge Ti → Tj whenever a conflicting "
    "operation of Ti precedes one of Tj on the same item. A schedule is conflict-serializable if and only if this graph "
    "is acyclic; the topological order of an acyclic graph gives an equivalent serial schedule. A cycle means the "
    "schedule is not serializable (distinct from deadlock, which is a cycle in the wait-for graph).",
    "precedence/serialization graph · node per txn · edge Ti→Tj on conflict · acyclic ⟺ serializable · cycle ≠ deadlock")

add_solved_problem("S39 · Solved problem · [EXAMPLE]","Test a schedule for conflict serializability",
    "Schedule S on item X (family wallet): T1:read(X); T2:read(X); T1:write(X); T2:write(X). Is S conflict-serializable? "
    "Build the precedence graph and decide.",
    ["List the conflicting pairs (same item X, different txns, ≥1 write). Reads-only pairs (both read X) do NOT conflict.",
     "T1:write(X) after T2:read(X) → T2 read X before T1 wrote it → edge T2 → T1.",
     "T2:write(X) after T1:write(X) → T1 wrote X before T2 → edge T1 → T2.",
     "The graph now has T1 → T2 AND T2 → T1 → a CYCLE.",
     "By the rule 'serializable ⟺ acyclic', a cycle means S is NOT conflict-serializable."],
    "S is NOT conflict-serializable — the precedence graph has a cycle (T1⇄T2). This is exactly the lost-update pattern: "
    "both read the old X, then overwrite each other. A DBMS would prevent it via locking (S40) or timestamps (S41).",
    "SOLVED PROBLEM [~8 min]. Reinforce: cycle = not serializable, NOT deadlock. Optionally redraw a safe version (T1 reads/writes, then T2).")

add_activity("S39 — 'Cause a lost update, then fix it'  ·  ~5 min",
    ["In pairs (3 min): on a shared wallet at Rs. 1000, write two top-ups (T1 +500, T2 +300) as an interleaving that "
     "causes a LOST UPDATE.",
     "Show the wrong final balance, then REORDER the operations so the final balance is correct (Rs. 1800).",
     "Draw the precedence graph for each version; note which has a cycle.",
     "Share (2 min): the bad version has a cycle / lost update; the good version is serial-equivalent."],
    "Bad interleaving: both read 1000, then both write → 1300 or 1500 (one lost). Fixed: T1 reads-writes fully, then T2 "
    "reads the new value → 1800. Reward students who connect the cycle in the graph to the lost update.",
    "ACTIVITY [~5 min].")
add_quiz("S39 — Quick Check  ·  ~5 min",
    [("Q1.  A schedule is conflict-serializable if its precedence graph:","q"),
     ("a) has a cycle   b) ✅ has no cycle   c) is empty   d) has one node","a"),
     ("     Why: an acyclic graph can be topologically ordered into an equivalent serial schedule.","o"),
     ("Q2.  Which pair of operations CONFLICTS?","q"),
     ("a) read–read on X   b) ✅ write–write on the same item X   c) ops on different items   d) two ops of one txn","a"),
     ("     Why: a conflict needs the same item, different txns, and at least one write.","o"),
     ("Discussion: sketch two top-ups on one shared wallet that cause a lost update, then reorder them to fix it.","o")],
    "QUIZ [~5 min]. Reinforce cycle-in-precedence-graph = not serializable, and read-read never conflicts.")
add_summary("S39 · Summary  ·  [~2 min]",
    ["A schedule orders interleaved operations; serial is always correct, non-serial is fast but must be checked.",
     "Bad interleavings cause anomalies (lost update, dirty read); the safe ones are serializable (equal to some serial order).",
     "Test conflict serializability with a precedence graph: serializable ⟺ the graph is acyclic (a cycle ≠ deadlock)."],
    "The database engine behind Daraz checkout and eSewa silently rejects or reorders unsafe interleavings so your balance "
    "is never lost during peak Dashain traffic — serializability is the theory that makes that guarantee possible.",
    "S40 — HOW the DBMS actually enforces a serializable order: locking and Two-Phase Locking.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S40
add_divider("Session 40 · Lecture hour 4 (of 8)","Two-Phase Locking (2PL) Concurrency Control",
    "To stop two people grabbing the same wallet balance, the DBMS hands out 'keys' (locks) so only one transaction holds "
    "an item at a time. But what if Rita holds Hari's key and Hari holds Rita's — and neither will let go?",
    "OPENING HOOK [~5 min]. Motivate locks and the deadlock risk. Agenda: locks (S/X) → the 2PL protocol → variants → deadlock → starvation.")

concept_understand("S40 · Concept 1 · [THEORY]","Locks — Shared and Exclusive",
    "A lock reserves a data item for a transaction so others can't interfere. A shared (S) lock is for reading — many "
    "transactions can hold it at once; an exclusive (X) lock is for writing — only one transaction can hold it, and no S-locks may coexist.",
    ["Shared (S) = read lock: multiple readers can share it simultaneously.",
     "Exclusive (X) = write lock: held by exactly one transaction, blocks all others.",
     "The lock compatibility matrix: S–S compatible; S–X, X–S, X–X all incompatible.",
     "A transaction must acquire the right lock before reading (S) or writing (X) an item."],
    None,"S-locks share among readers; an X-lock is exclusive to one writer.",
    "~7 min. T1 takes an X-lock on the wallet row to debit it; T2 wanting the same row must WAIT until T1 releases it.")
concept_apply("S40 · Concept 1 · [THEORY]","Locks — Shared and Exclusive",
    "To debit the family wallet, T1 takes an EXCLUSIVE (X) lock on that row; any other transaction wanting to read or "
    "write the same row must wait until T1 releases it. But if two transactions only want to READ the balance (e.g. two "
    "balance-checks), both can hold a SHARED (S) lock at the same time — reads don't interfere.",
    "\"A shared lock blocks other readers.\" No — MULTIPLE shared locks can coexist; that's the point of 'shared'. Only "
    "an EXCLUSIVE (write) lock conflicts with others, because a write must not overlap any other access.",
    "A lock reserves a data item for a transaction. A shared (S) lock permits reading and can be held by several "
    "transactions simultaneously; an exclusive (X) lock permits writing and can be held by only one transaction, with no "
    "other S or X lock allowed on the item. Compatibility: S–S is allowed; any pairing involving X is not. A transaction "
    "acquires the appropriate lock before accessing an item.",
    "lock · shared (S, read) · exclusive (X, write) · compatibility matrix · S–S compatible, X conflicts")
add_comparison_table("S40 · Concept 1 · comparison","Lock compatibility matrix — can the requested lock be granted?",
    ["Item currently held as…","Request: Shared (S)","Request: Exclusive (X)"],
    [["(no lock held)","✅ granted","✅ granted"],
     ["Shared (S) by others","✅ granted (readers share)","✗ must wait (write needs exclusivity)"],
     ["Exclusive (X) by another","✗ must wait","✗ must wait"],
     ["Example: two balance checks","both get S → run together","—"],
     ["Example: a debit (write)","—","one X only → others wait"],
     ["Rule","only S–S is compatible","any X pairing conflicts"]],
    per_page=6,widths=[2.4,2.0,2.4],fs=11,
    note="Read-read shares (S–S compatible), so many balance-checks run together; any write needs an exclusive X-lock, "
         "so it blocks and is blocked by everything else on that item.")

concept_understand("S40 · Concept 2 · [THEORY]","The Two-Phase Locking Protocol",
    "Two-Phase Locking (2PL) requires that every transaction acquire ALL the locks it needs before releasing ANY lock. "
    "This splits its life into a growing phase (only acquire) and a shrinking phase (only release), with a single peak. "
    "2PL guarantees conflict-serializability.",
    ["Growing phase: the transaction only ACQUIRES locks (lock count rises to a peak).",
     "Shrinking phase: after the first release, it may only RELEASE locks (never acquire again).",
     "The single 'lock point' (the peak) is what forces a serializable order.",
     "2PL is the most widely used concurrency-control method in real relational DBMSs."],
    "s40_phases.png","Grow (acquire) then shrink (release); one peak, never re-acquire.",
    "~8 min. Analogy: collect all your shopping first (growing), then start returning items (shrinking) — never grab again after returning starts.")
concept_apply("S40 · Concept 2 · [THEORY]","The Two-Phase Locking Protocol",
    "A transfer transaction under 2PL first ACQUIRES exclusive locks on both the sender's and receiver's wallet rows "
    "(growing phase), performs the debit and credit, and only THEN begins releasing locks (shrinking phase). Because it "
    "never grabs a new lock after releasing one, the DBMS can prove the overall schedule is serializable.",
    "\"2PL means locking in exactly two steps / two locks.\" No — 'two-phase' refers to the growing then shrinking PHASES "
    "of lock activity over the transaction's life, not the number of locks or steps. It can hold many locks.",
    "Two-Phase Locking (2PL) is a concurrency-control protocol in which every transaction acquires all its locks before "
    "releasing any, dividing its execution into a growing phase (locks only acquired) and a shrinking phase (locks only "
    "released), separated by a single lock point. This discipline guarantees conflict-serializability and is the most "
    "common locking scheme in real DBMSs.",
    "two-phase locking · growing phase · shrinking phase · lock point · guarantees serializability")

concept_understand("S40 · Concept 3 · [THEORY]","Variants of 2PL",
    "Several 2PL variants trade concurrency for stronger guarantees: basic 2PL, conservative (static) 2PL, strict 2PL, "
    "and rigorous 2PL. They differ in WHEN locks are acquired and released.",
    ["Basic 2PL: the plain grow-then-shrink rule (serializable, but deadlock possible).",
     "Conservative (static) 2PL: acquire ALL locks up front → deadlock-free, but lower concurrency.",
     "Strict 2PL: hold all EXCLUSIVE locks until commit/abort → avoids cascading rollback (most common).",
     "Rigorous 2PL: hold ALL locks (S and X) until commit → simplest to reason about."],
    None,"Variants differ in when locks are taken (conservative) or released (strict/rigorous).",
    "~7 min. Strict 2PL on the eSewa wallet: a half-committed debit is never read by another transaction.")
concept_apply("S40 · Concept 3 · [THEORY]","Variants of 2PL",
    "eSewa would use STRICT 2PL on wallet rows: a transfer holds its exclusive locks until it commits, so no other "
    "transaction can read a half-committed debit (preventing dirty reads and cascading rollback). A batch job that knows "
    "all the rows it needs up front might use CONSERVATIVE 2PL to avoid deadlock entirely.",
    "\"All 2PL variants behave the same.\" No — basic 2PL can deadlock and allow cascading rollback; conservative 2PL "
    "avoids deadlock; strict/rigorous 2PL prevent cascading rollback. The choice is a real trade-off between concurrency "
    "and safety.",
    "Variants of 2PL: basic 2PL (grow then shrink; serializable but deadlock-prone), conservative/static 2PL (all locks "
    "acquired up front → deadlock-free but low concurrency), strict 2PL (exclusive locks held until commit/abort → "
    "prevents cascading rollback; the most common in practice), and rigorous 2PL (all locks held until commit). They "
    "trade concurrency against stronger recovery/deadlock guarantees.",
    "basic 2PL · conservative (static) 2PL · strict 2PL · rigorous 2PL · cascading rollback · deadlock-free")

concept_understand("S40 · Concept 4 · [THEORY] [EXAMPLE]","Deadlock",
    "A deadlock occurs when two or more transactions are each waiting for a lock held by another, so none can ever "
    "proceed — a frozen stalemate. It is detected as a cycle in the wait-for graph, and resolved by aborting a 'victim'.",
    ["Cause: T1 holds A and wants B; T2 holds B and wants A → circular wait.",
     "Detection: build a wait-for graph (edge Ti→Tj if Ti waits for a lock Tj holds); a cycle = deadlock.",
     "Prevention schemes: wait-die and wound-wait use timestamps to decide who waits vs aborts.",
     "Resolution: abort one transaction (the victim), release its locks, and restart it later."],
    "s40_deadlock.png","Deadlock = a cycle in the wait-for graph; abort a victim to break it.",
    "~8 min. T1 locks Rita's row & wants Hari's; T2 locks Hari's row & wants Rita's — neither can move.")
concept_apply("S40 · Concept 4 · [THEORY] [EXAMPLE]","Deadlock",
    "Two eSewa transfers deadlock: T1 (Rita→Hari) locks Rita's row and waits for Hari's; T2 (Hari→Rita) locks Hari's row "
    "and waits for Rita's. Each holds what the other needs — a circular wait. The DBMS detects the cycle in the wait-for "
    "graph and aborts one transaction (say T2), releasing its locks so T1 finishes; T2 is restarted afterwards.",
    "\"Deadlock means the server crashed.\" No — a deadlock is a logical stalemate, not a crash. The DBMS detects it and "
    "resolves it by aborting and restarting a victim transaction; the server keeps running fine.",
    "A deadlock is a state where two or more transactions each hold a lock the other needs and wait indefinitely — a "
    "circular wait. It is detected by finding a cycle in the wait-for graph (edge Ti→Tj when Ti waits for a lock held by "
    "Tj) and resolved by aborting a victim transaction and restarting it. Prevention schemes (wait-die, wound-wait) use "
    "transaction timestamps to avoid the circular wait.",
    "deadlock · circular wait · wait-for graph · cycle = deadlock · victim abort · wait-die/wound-wait")
add_comparison_table("S40 · Concept 4 · comparison","Two cycles, two very different meanings",
    ["Graph","Node = ","Edge means","A cycle means…","Belongs to"],
    [["Precedence graph","a transaction","Ti's op conflicts before Tj's","schedule is NOT serializable","S39 (correctness)"],
     ["Wait-for graph","a transaction","Ti waits for a lock Tj holds","DEADLOCK (frozen stalemate)","S40 (locking)"],
     ["Fix for precedence cycle","—","—","reject / reorder the schedule","—"],
     ["Fix for wait-for cycle","—","—","abort a victim, restart it","—"]],
    per_page=4,widths=[1.9,1.5,2.3,2.2,1.6],fs=10.5,
    note="Do not confuse them: a cycle in the PRECEDENCE graph = not serializable (S39); a cycle in the WAIT-FOR graph "
         "= deadlock (S40). Same word 'cycle', completely different problem.")

concept_understand("S40 · Concept 5 · [THEORY]","Starvation",
    "Starvation happens when a particular transaction is repeatedly delayed or chosen as the deadlock victim, so it never "
    "gets the locks it needs and never completes. It is a fairness problem, distinct from deadlock.",
    ["Cause: the same transaction keeps losing — always waiting or always the aborted victim.",
     "Unlike deadlock, the system as a whole keeps making progress; one transaction is left behind.",
     "Fix: fair scheduling, priorities, or aging (raise a waiting transaction's priority over time).",
     "Aging guarantees an old, repeatedly-delayed transaction eventually wins."],
    None,"Starvation = one txn never gets its turn; fix with priorities / aging.",
    "~5 min. Contrast with deadlock: deadlock freezes several; starvation strands one while others proceed.")
concept_apply("S40 · Concept 5 · [THEORY]","Starvation",
    "During a Dashain rush, a low-priority reporting transaction keeps getting picked as the victim whenever it clashes "
    "with high-value transfers — it is aborted and restarted again and again, never finishing. Aging fixes this: each "
    "time it is delayed, its priority rises, until it eventually outranks new arrivals and completes.",
    "\"Starvation is the same as deadlock.\" No — in deadlock NObody proceeds (a mutual freeze); in starvation the system "
    "keeps working but ONE unlucky transaction never gets its turn. Deadlock is a stalemate; starvation is unfairness.",
    "Starvation is a situation where a transaction is repeatedly delayed or repeatedly selected as the victim to abort, "
    "so it never acquires the resources it needs to complete — even though the system as a whole makes progress. Unlike "
    "deadlock (a mutual freeze), starvation strands a single transaction, and it is addressed by fair scheduling, "
    "priorities, or aging (increasing a waiting transaction's priority over time).",
    "starvation · repeated victim/delay · fairness · priorities · aging · distinct from deadlock")

add_activity("S40 — 'Deadlock two transfers'  ·  ~5 min",
    ["In pairs (3 min): write two eSewa transfers on rows A (Rita) and B (Hari) that DEADLOCK.",
     "Show which lock each holds and which it is waiting for; draw the wait-for graph and mark the cycle.",
     "Decide which transaction you would abort as the victim, and why.",
     "Share (2 min): note that the fix is aborting + restarting one, not restarting the server."],
    "Deadlock: T1 X-locks A, wants B; T2 X-locks B, wants A → wait-for cycle. Reasonable victim policy: abort the "
    "younger/less-work transaction and restart it. Reward correct wait-for graphs and a clear victim rationale.",
    "ACTIVITY [~5 min].")
add_quiz("S40 — Quick Check  ·  ~5 min",
    [("Q1.  In 2PL, once a transaction releases its first lock it is in the:","q"),
     ("a) growing phase   b) ✅ shrinking phase   c) commit phase   d) abort phase","a"),
     ("     Why: after the first release it may only release, never acquire — the shrinking phase.","o"),
     ("Q2.  Deadlock is detected by finding a cycle in the:","q"),
     ("a) precedence graph   b) ✅ wait-for graph   c) B-tree   d) page table","a"),
     ("     Why: an edge Ti→Tj means Ti waits for a lock Tj holds; a cycle = mutual wait = deadlock.","o"),
     ("Discussion: describe a two-person eSewa scenario that deadlocks, and which transaction you'd abort to break it.","o")],
    "QUIZ [~5 min]. Reinforce phases (grow→shrink) and precedence-graph vs wait-for-graph cycles.")
add_summary("S40 · Summary  ·  [~2 min]",
    ["S (read, shareable) and X (write, exclusive) locks reserve data items; only S–S is compatible.",
     "Two-Phase Locking (grow then shrink, one lock point) guarantees conflict-serializability; strict 2PL also stops cascading rollback.",
     "Locking can deadlock (cycle in the wait-for graph → abort a victim) and can starve a transaction (fix with aging)."],
    "Every relational DB behind Nepali fintech apps (MySQL, PostgreSQL) uses locking; 'deadlock found; aborting one "
    "transaction' is a real production error developers must understand and design around.",
    "S41 — a lock-free alternative that orders transactions by a timestamp instead of fighting over keys.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S41
add_divider("Session 41 · Lecture hour 5 (of 8)","Timestamp Ordering Concurrency Control",
    "Instead of fighting over keys (locks), what if every eSewa transaction got a numbered ticket the moment it arrived — "
    "and the DBMS simply enforced 'serve in ticket order'? That is timestamp ordering: concurrency control with no locks.",
    "OPENING HOOK [~5 min]. Contrast with locking. Agenda: timestamps → read/write timestamps on items → the basic TO protocol "
    "→ Thomas's write rule → 2PL vs TO.")

concept_understand("S41 · Concept 1 · [THEORY]","Timestamps",
    "A timestamp TS(T) is a unique, monotonically increasing identifier assigned to a transaction when it starts. An "
    "older (smaller) timestamp means higher priority — the DBMS enforces an execution order equivalent to timestamp order.",
    ["Source: the system clock, or a simple logical counter that increments per transaction.",
     "Each transaction's timestamp is unique and never reused — it fixes a total order.",
     "The 'senior' (earlier) transaction is the one with the smaller timestamp.",
     "This fixed order is the serial order the schedule will be made equivalent to."],
    None,"Timestamp = a ticket number at start; smaller TS = older = higher priority.",
    "~7 min. Each eSewa transfer is stamped with its arrival time; the earlier one is the 'senior' transaction.")
concept_apply("S41 · Concept 1 · [THEORY]","Timestamps",
    "Every eSewa transfer is stamped with its arrival order — think of the token/ticket you take at a bank counter. If "
    "Rita's transfer arrives at TS=101 and Hari's at TS=102, Rita's is 'senior'. The DBMS will enforce a schedule "
    "equivalent to running them in timestamp order (101 before 102), no locks required.",
    "\"Timestamps are just the wall-clock time and can repeat.\" No — timestamps must be UNIQUE and strictly increasing; "
    "a logical counter is often used precisely so two transactions never share a timestamp, which would break the total order.",
    "A timestamp TS(T) is a unique, monotonically increasing identifier assigned to a transaction at its start, drawn "
    "from the system clock or a logical counter. It defines a total order on transactions in which a smaller timestamp "
    "means an older, higher-priority transaction. Timestamp-ordering concurrency control enforces a schedule equivalent "
    "to executing transactions in timestamp order.",
    "timestamp TS(T) · unique · monotonically increasing · older = higher priority · defines serial order")

concept_understand("S41 · Concept 2 · [THEORY]","Read and Write Timestamps on Data Items",
    "To enforce timestamp order, each data item X keeps two values: read_TS(X) — the largest timestamp of any transaction "
    "that has READ X — and write_TS(X) — the largest timestamp of any transaction that has WRITTEN X.",
    ["read_TS(X): the timestamp of the youngest transaction that successfully read X.",
     "write_TS(X): the timestamp of the youngest transaction that successfully wrote X.",
     "Every read/write request is checked against these two values before it is allowed.",
     "These two stamps let the DBMS spot an operation that arrives 'too late' (out of order)."],
    "s41_timestamps.png","Each item X carries read_TS(X) and write_TS(X) — the newest reader/writer.",
    "~6 min. Draw item X with its two timestamps; every op is validated against them.")
concept_apply("S41 · Concept 2 · [THEORY]","Read and Write Timestamps on Data Items",
    "The family-wallet item X remembers read_TS(X) (the newest transaction that read the balance) and write_TS(X) (the "
    "newest that wrote it). When a new transfer tries to read or write X, the DBMS compares its timestamp against these "
    "two — this is how it detects a 'late' transaction trying to act after a 'newer' one already has.",
    "\"A data item only needs one timestamp.\" No — it needs TWO (read_TS and write_TS), because reads and writes create "
    "different kinds of ordering conflicts; a single stamp couldn't distinguish a late read from a late write.",
    "In timestamp ordering, each data item X stores read_TS(X), the largest timestamp of any transaction that has read X, "
    "and write_TS(X), the largest timestamp of any transaction that has written X. Every read or write request is "
    "validated against these two values to ensure operations occur in timestamp order; the stamps are updated when an "
    "operation is allowed.",
    "read_TS(X) · write_TS(X) · largest reader/writer timestamp · validate each op · updated on success")

concept_understand("S41 · Concept 3 · [THEORY] [EXAMPLE]","The Basic Timestamp-Ordering Protocol",
    "Under basic timestamp ordering, a read or write is allowed only if it does not violate timestamp order; an operation "
    "that would violate it causes the transaction to be ABORTED and RESTARTED with a new, larger timestamp. This produces "
    "a serializable schedule and, because nothing ever waits, cannot deadlock.",
    ["Write rule: T's write(X) is rejected if a YOUNGER transaction has already read or written X.",
     "Read rule: T's read(X) is rejected if a YOUNGER transaction has already written X.",
     "A rejected transaction is rolled back and restarted with a fresh (larger) timestamp.",
     "No waiting means no circular wait → no deadlock (but repeated restarts can cause starvation)."],
    None,"Out-of-order op → abort & restart with a larger timestamp; never wait, never deadlock.",
    "~8 min. A 'late' transaction trying to write a wallet already written by a 'newer' one is rolled back and restarted.")
concept_apply("S41 · Concept 3 · [THEORY] [EXAMPLE]","The Basic Timestamp-Ordering Protocol",
    "A slow transfer with TS=101 tries to write the wallet, but a newer transfer (TS=102) has ALREADY written it "
    "(write_TS=102 > 101). Allowing the old write would overwrite newer data out of order, so the DBMS aborts the "
    "TS=101 transaction and restarts it with a fresh, larger timestamp — no lock, no waiting, no deadlock.",
    "\"Timestamp ordering can deadlock like 2PL.\" No — it NEVER makes a transaction wait; conflicts are resolved by "
    "aborting/restarting, so there is no circular wait and therefore no deadlock (though repeated restarts can starve a transaction).",
    "The basic timestamp-ordering protocol allows an operation only if it respects timestamp order: a write is rejected "
    "if a younger transaction has already read or written the item, and a read is rejected if a younger transaction has "
    "already written it. A violating transaction is aborted and restarted with a larger timestamp. This yields a "
    "serializable schedule and is deadlock-free (nothing waits), though it can cause starvation.",
    "basic TO protocol · read/write rules · reject out-of-order op · abort & restart · deadlock-free · starvation possible")

concept_understand("S41 · Concept 4 · [THEORY]","Thomas's Write Rule",
    "Thomas's write rule is an optimisation of basic timestamp ordering: an OBSOLETE write — one by a transaction older "
    "than the item's write_TS — can simply be IGNORED instead of aborting the transaction, because a newer write has "
    "already superseded it. This allows more concurrency.",
    ["If T's write(X) is outdated (a younger transaction already wrote X), the write is simply skipped.",
     "Skipping is safe because the value T would write is immediately overwritten anyway.",
     "It relaxes the basic rule, rejecting fewer transactions and allowing more concurrency.",
     "It applies only to write-write ordering; read rules are unchanged."],
    None,"Thomas's rule: ignore an obsolete write instead of aborting → more concurrency.",
    "~5 min. Show a write that is simply skipped because a newer write already replaced that value.")
concept_apply("S41 · Concept 4 · [THEORY]","Thomas's Write Rule",
    "A transaction with TS=101 tries to write the wallet's non-critical field, but TS=105 has already written it. Under "
    "the BASIC rule, TS=101 would be aborted; under THOMAS'S rule, the DBMS simply IGNORES the obsolete write (its value "
    "would be overwritten anyway) and lets TS=101 continue — fewer aborts, more concurrency.",
    "\"Thomas's rule loses data by skipping a write.\" No — it only skips a write that a NEWER write has already "
    "superseded, so the skipped value would have been immediately overwritten regardless. No committed data is lost.",
    "Thomas's write rule optimises timestamp ordering by ignoring an obsolete write — a write by a transaction whose "
    "timestamp is older than the item's write_TS — rather than aborting the transaction, since a younger write has "
    "already superseded that value. It applies only to write-write cases and increases concurrency by rejecting fewer "
    "operations, while still producing a serializable schedule.",
    "Thomas's write rule · obsolete write · ignore instead of abort · write-write only · more concurrency")
add_comparison_table("S41 · 2PL vs TO · comparison","Two-Phase Locking vs Timestamp Ordering — the two concurrency-control families",
    ["Dimension","Two-Phase Locking (2PL)","Timestamp Ordering (TO)"],
    [["Mechanism","Locks (S/X); acquire then release","Timestamps; serve in TS order"],
     ["Transactions that clash","WAIT for the lock to be freed","ABORT & restart with a larger TS"],
     ["Guarantees","Conflict-serializability","Serializable in timestamp order"],
     ["Failure mode","Deadlock (circular wait) possible","Starvation (repeated restarts) possible"],
     ["Deadlock?","Yes — detect/prevent it","No — nothing ever waits"],
     ["Best fit (Nepal / IT)","High-conflict eSewa peak (steadier)","Low-conflict reporting / distributed jobs"]],
    per_page=6,widths=[1.7,2.6,2.6],fs=11,
    note="The core trade-off: 2PL makes clashing transactions WAIT (so it can deadlock); TO makes them RESTART (so it "
         "can starve but never deadlocks). Pick by how much contention the workload has.")

add_solved_problem("S41 · Solved problem · [EXAMPLE]","Apply the basic timestamp-ordering rules",
    "Item X has read_TS(X)=0, write_TS(X)=0. Transactions arrive with TS: T1=100, T2=110. Trace: T2 write(X); "
    "T1 write(X). What does basic TO do with each operation?",
    ["T2 write(X): check younger reader/writer? read_TS(X)=0 and write_TS(X)=0 are both < 110 → ALLOWED. "
     "Update write_TS(X)=110.",
     "T1 write(X): T1's TS=100. Compare with write_TS(X)=110 (a YOUNGER transaction, T2, already wrote X).",
     "A write by an OLDER transaction over a value a younger one already wrote violates timestamp order.",
     "Basic rule → ABORT T1 and restart it with a new timestamp larger than 110.",
     "(Under Thomas's write rule instead, T1's obsolete write would simply be IGNORED — no abort.)"],
    "Basic TO aborts and restarts T1 (its write arrived after younger T2's write on X). No waiting occurred, so no "
    "deadlock is possible. Thomas's write rule would instead ignore T1's obsolete write, allowing more concurrency.",
    "SOLVED PROBLEM [~8 min]. Contrast the basic-rule abort with the Thomas's-rule skip on the same trace.")

add_activity("S41 — 'Lock vs ticket'  ·  ~5 min",
    ["In pairs (2 min): for a high-conflict eSewa peak and a low-conflict nightly report job, decide whether 2PL "
     "(locking) or timestamp ordering fits better.",
     "List the failure mode each would suffer (deadlock vs starvation/restarts).",
     "Take 3–4 answers aloud (3 min).",
     "Close: high conflict → many restarts under TO (locking may be steadier); low conflict → TO's no-wait shines."],
    "Reasonable answers: TO avoids deadlock but restarts a lot under high contention (wasteful at peak); 2PL is steadier "
    "under contention but risks deadlock. Reward reasoning about the trade-off, not a single 'right' answer.",
    "ACTIVITY [~5 min].")
add_quiz("S41 — Quick Check  ·  ~5 min",
    [("Q1.  In basic timestamp ordering, a transaction that violates the timestamp order is:","q"),
     ("a) queued   b) ignored always   c) ✅ aborted and restarted (with a larger timestamp)   d) committed early","a"),
     ("     Why: it never waits — conflicts are resolved by rolling back and restarting.","o"),
     ("Q2.  Compared to 2PL, basic timestamp ordering:","q"),
     ("a) deadlocks more   b) ✅ cannot deadlock   c) needs more locks   d) is always faster","a"),
     ("     Why: nothing waits, so there is no circular wait and no deadlock (though starvation is possible).","o"),
     ("Discussion: timestamp ordering never deadlocks but can starve a transaction — why is that trade-off sometimes acceptable for a wallet system?","o")],
    "QUIZ [~5 min]. Reinforce abort-and-restart (no waiting) and the no-deadlock-but-starvation trade-off.")
add_summary("S41 · Summary  ·  [~2 min]",
    ["A timestamp gives each transaction a fixed order at start (older = higher priority); items keep read_TS and write_TS.",
     "Basic timestamp ordering aborts and restarts any operation that violates timestamp order — it never waits.",
     "No waiting means no deadlock, but repeated restarts can cause starvation; Thomas's write rule ignores obsolete writes for more concurrency."],
    "Timestamp and multiversion ordering underpin high-concurrency and distributed databases (relevant to large-scale "
    "e-commerce and telecom billing across South Asia), where avoiding lock waits at massive scale is worth the restarts.",
    "S42 — what happens AFTER a failure: recovery begins with the deferred-update (NO-UNDO/REDO) technique.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S42
add_divider("Session 42 · Lecture hour 6 (of 8)","Recovery Concepts · Deferred Update (NO-UNDO/REDO)",
    "The eSewa server crashes one second AFTER Rita's transfer commits — and mid-way through a second transfer that had "
    "not yet committed. After reboot, which one must be redone and which one thrown away?",
    "OPENING HOOK [~5 min]. Motivate undo vs redo. Agenda: recovery concepts → caching, WAL → checkpoints → deferred update → its limitation.")

concept_understand("S42 · Concept 1 · [THEORY]","Recovery Concepts — UNDO and REDO",
    "Recovery is the process of restoring the database to the most recent consistent state after a failure, using the "
    "system log. Its two basic operations are UNDO (remove the effects of an uncommitted transaction) and REDO (reapply "
    "the effects of a committed one).",
    ["After a crash, the recovery manager scans the log to classify each transaction.",
     "UNDO: transactions with [start] but no [commit] → roll back using old values.",
     "REDO: transactions with both [start] and [commit] → reapply using new values.",
     "The exact mix of undo/redo depends on the update technique (deferred vs immediate)."],
    None,"Recovery = restore last consistent state; UNDO the uncommitted, REDO the committed.",
    "~7 min. Post-crash, the DBMS scans the eSewa log to decide undo or redo per transaction.")
concept_apply("S42 · Concept 1 · [THEORY]","Recovery Concepts — UNDO and REDO",
    "After the eSewa server reboots, the recovery manager scans the log: Rita's transfer has both [start] and [commit], "
    "so it is REDONE (reapplied from the new values) to be sure it's on disk; the second transfer has [start] but no "
    "[commit], so it is UNDONE (or simply discarded) — the customer never saw 'success' for it.",
    "\"Recovery just reloads the last backup.\" Not for a normal crash — the disk is intact, so recovery uses the LOG to "
    "undo/redo individual transactions to the last consistent state. Full backups are only for catastrophic media loss (S44).",
    "Recovery is the restoration of the database to its most recent consistent state after a failure, driven by the "
    "system log. It relies on two operations: UNDO, which removes the effects of transactions that did not commit (using "
    "the log's old values), and REDO, which reapplies the effects of committed transactions (using the new values). "
    "Which operations are needed depends on the update technique in use.",
    "recovery · last consistent state · UNDO (uncommitted, old values) · REDO (committed, new values) · log-driven")
add_examples_table("S42 · Concept 1 · scaffolding","The recovery-action table — what to do with each transaction after a crash",
    ["Transaction (log evidence)","Status","Recovery action","Values used"],
    [["[start,T] and [commit,T] present","Committed","REDO (make sure it's on disk)","new values"],
     ["[start,T] but NO [commit,T]","Uncommitted","UNDO (immediate) / ignore (deferred)","old values"],
     ["[start,T] then [abort,T]","Aborted","UNDO / already rolled back","old values"],
     ["Committed before last [checkpoint]","Durable","Skip — already flushed","none"],
     ["Rita's transfer: committed pre-crash","Committed","REDO the debit + credit","new balances"],
     ["Hari's transfer: crashed mid-way","Uncommitted","UNDO the partial debit","old balance"]],
    per_page=6,widths=[2.5,1.5,2.6,1.6],fs=10.5,
    note="Recovery is disciplined log-reading: REDO transactions with [start]+[commit]; UNDO (or ignore, under deferred "
         "update) those with [start] but no [commit]. The checkpoint marks what is already safely on disk.")

concept_understand("S42 · Concept 2 · [THEORY]","Caching, In-Place Update & Write-Ahead Logging",
    "For efficiency, the DBMS updates data in a memory buffer (cache) first and writes to disk later; in-place update "
    "overwrites the item in its disk location. Write-Ahead Logging (WAL) is the rule that the log record must reach "
    "stable storage BEFORE the corresponding data page is written.",
    ["Writes hit the buffer first; dirty pages are flushed to disk later, not instantly at commit.",
     "WAL guarantees the old value (for UNDO) and new value (for REDO) are safely logged before the data page changes.",
     "Without WAL, a crash could leave a changed data page with no log record to undo/redo it.",
     "WAL is what actually makes durability and recovery possible."],
    None,"WAL: write the log record to stable storage BEFORE the data page.",
    "~7 min. The key myth to kill: commit does NOT mean 'instantly on disk' — it means 'safely in the log'.")
concept_apply("S42 · Concept 2 · [THEORY]","Caching, In-Place Update & Write-Ahead Logging",
    "When eSewa commits Rita's transfer, the updated balance may still be sitting in the buffer, not yet on disk. What "
    "makes 'success' safe is that the log records ([write...][commit]) were flushed to stable storage FIRST (WAL). If the "
    "server crashes before the data page is written, recovery REDOes the change from the logged new value.",
    "\"Data is written to disk the instant you commit.\" No — the data page may linger in the buffer; only the LOG record "
    "is guaranteed on stable storage at commit. Durability comes from the log (WAL), not from an immediate data-page write.",
    "The DBMS caches data in a memory buffer and updates it there first (in-place update overwrites the item's disk copy "
    "when flushed). Write-Ahead Logging (WAL) requires a transaction's log record to reach stable storage before the "
    "corresponding data page, so every change can be undone (old value) or redone (new value) after a crash. WAL is the "
    "foundation of durability: commit means 'safely logged', not 'already on the data disk'.",
    "buffer/cache · in-place update · dirty page · Write-Ahead Logging (WAL) · log before data page · commit = logged")

concept_understand("S42 · Concept 3 · [THEORY]","Checkpoints",
    "A checkpoint is a periodic point at which the DBMS flushes all buffered updates to disk and writes a [checkpoint] "
    "record to the log. It limits how far back recovery must scan: transactions that committed before the checkpoint "
    "need not be redone.",
    ["At a checkpoint, dirty buffer pages are forced to disk and a [checkpoint] mark is logged.",
     "After a crash, recovery only needs to consider transactions active at or after the last checkpoint.",
     "This bounds recovery time — you never replay the ENTIRE log from the beginning.",
     "Checkpoints trade a brief pause now for much faster recovery later."],
    None,"Checkpoint = a save point; recovery starts from the last one, not the very start.",
    "~7 min. Analogy: a save point in a video game — you never replay the whole game, just from the last save.")
concept_apply("S42 · Concept 3 · [THEORY]","Checkpoints",
    "eSewa's DBMS takes a checkpoint every few minutes, flushing buffered balances to disk and logging a [checkpoint] "
    "mark. If it crashes at 3:07 and the last checkpoint was 3:05, recovery only replays the log from 3:05 — transfers "
    "that committed and were flushed before 3:05 are already safe on disk and skipped.",
    "\"Recovery always replays the whole log from the beginning.\" No — the last [checkpoint] bounds the work: anything "
    "committed and flushed before it is already durable, so recovery starts from the checkpoint, not from transaction one.",
    "A checkpoint is a periodic operation in which the DBMS flushes all buffered (dirty) pages to disk and records a "
    "[checkpoint] entry in the log. Because everything committed before the checkpoint is guaranteed on disk, recovery "
    "after a crash only needs to examine transactions active at or after the last checkpoint, bounding recovery time. It "
    "is like a save point that avoids replaying the entire log.",
    "checkpoint · flush dirty pages · [checkpoint] log record · bounds recovery scan · save point analogy")

concept_understand("S42 · Concept 4 · [THEORY] [EXAMPLE]","Deferred Update (NO-UNDO/REDO)",
    "In the deferred-update technique, all actual database writes are DEFERRED until AFTER the transaction commits; until "
    "then the changes live only in the log and buffer. Because uncommitted transactions never touched the database, "
    "recovery needs NO UNDO — only REDO for committed transactions not yet flushed.",
    ["Before commit, the DB on disk is untouched; changes are recorded in the log only.",
     "NO-UNDO: an uncommitted transaction changed nothing on disk → nothing to roll back.",
     "REDO: a committed transaction's changes may still be only in the log/buffer → reapply from the log.",
     "Recovery rule: REDO every transaction with both [start] and [commit]; ignore the rest."],
    "s42_deferred.png","Deferred update: write only after commit → REDO only, never UNDO.",
    "~9 min. Rita's debit only hits the wallet table AFTER [commit,T]; crash before commit = DB never changed → no undo.")
concept_apply("S42 · Concept 4 · [THEORY] [EXAMPLE]","Deferred Update (NO-UNDO/REDO)",
    "Under deferred update, Rita's debit is written to the wallet table only AFTER [commit,T] is logged. If the server "
    "crashes before she commits, the wallet table was never changed — nothing to undo. If it crashes just after commit "
    "but before the buffer is flushed, recovery REDOes her transfer from the logged new values.",
    "\"Deferred update still needs to undo unfinished transactions.\" No — because writes are deferred until after "
    "commit, an uncommitted transaction made NO changes to the database, so there is nothing to undo. Deferred update is "
    "NO-UNDO/REDO by design.",
    "The deferred-update (NO-UNDO/REDO) technique postpones all database writes until after a transaction commits, "
    "keeping changes in the log/buffer until then. Consequently, uncommitted transactions never modify the database (no "
    "UNDO is ever needed), while committed transactions whose changes may still be buffered are reapplied (REDO). "
    "Recovery simply REDOes every transaction having both [start] and [commit] and ignores the rest.",
    "deferred update · NO-UNDO/REDO · write after commit · nothing to undo · REDO committed · [start]+[commit] rule")

concept_understand("S42 · Concept 5 · [THEORY]","Limitation of Deferred Update",
    "Deferred update is simple and needs no UNDO, but it must hold ALL of a transaction's changes in the log/buffer until "
    "commit. For long or large transactions this consumes a lot of buffer/log space and delays visibility of changes — "
    "which motivates the immediate-update technique (S43).",
    ["A long transaction accumulates many buffered changes it cannot write until it commits.",
     "Large batch updates can exhaust buffer space under pure deferred update.",
     "Changes are invisible on disk until commit, delaying when they become durable there.",
     "Immediate update (S43) fixes this by writing early — at the cost of needing UNDO."],
    None,"Deferred update strains memory for long/large transactions → motivates immediate update.",
    "~5 min. Bridge to S43: writing everything only at commit doesn't scale for huge updates.")
concept_apply("S42 · Concept 5 · [THEORY]","Limitation of Deferred Update",
    "A bank's nightly interest-calculation batch updates millions of accounts in one transaction. Under pure deferred "
    "update, every one of those changes must sit in the log/buffer until the whole batch commits — a heavy memory and "
    "log burden. This is exactly the case where immediate update (write as you go) is preferable.",
    "\"Deferred update is always the best choice because it needs no undo.\" No — its no-undo simplicity costs buffer/log "
    "space and delays durability for long/large transactions; immediate update trades in an UNDO requirement to write "
    "early and scale better.",
    "The main limitation of deferred update is that it must retain all of a transaction's changes in the log/buffer until "
    "commit, which strains memory and log space for long-running or large (e.g. batch) transactions and delays when "
    "changes reach disk. This scalability cost motivates the immediate-update technique, which writes changes to the "
    "database as they occur at the price of requiring UNDO.",
    "limitation of deferred update · buffer/log pressure · long/large transactions · delayed durability · motivates immediate update")

add_solved_problem("S42 · Solved problem · [EXAMPLE]","Recover a deferred-update log after a crash",
    "After a crash under DEFERRED update, the log shows: [start,T1] [write,T1,X,-,50] [commit,T1] [start,T2] "
    "[write,T2,Y,-,80] — then CRASH (no [commit,T2]). What does recovery do?",
    ["Deferred update is NO-UNDO/REDO: writes happened only after commit, so uncommitted transactions changed nothing on disk.",
     "T1 has both [start,T1] and [commit,T1] → it committed → REDO T1: reapply write X=50 from the log's new value.",
     "T2 has [start,T2] but NO [commit,T2] → it never committed → its write was never applied to the DB.",
     "So T2 needs NO UNDO (nothing was written) — simply ignore/discard T2.",
     "Result: X=50 is restored/confirmed; Y is untouched, exactly as if T2 never ran."],
    "REDO T1 (committed) from the logged new value X=50; ignore T2 (no commit) — no undo needed because deferred update "
    "never wrote uncommitted changes to disk. This is why the technique is called NO-UNDO/REDO.",
    "SOLVED PROBLEM [~8 min]. This is the exam 'you find [start] but no [commit]' discussion made concrete.")

add_activity("S42 — 'Undo, redo, or ignore?'  ·  ~5 min",
    ["In pairs (3 min): under DEFERRED update, a crash leaves these in the log — classify each transaction.",
     "T_a: [start][write][commit];  T_b: [start][write] (no commit);  T_c: committed before the last [checkpoint].",
     "Decide REDO / ignore for each, and say why deferred update never needs UNDO.",
     "Share (2 min): T_a → REDO; T_b → ignore (nothing written); T_c → already on disk, skip."],
    "T_a REDO (committed, maybe still buffered); T_b ignore (deferred → no disk change, no undo); T_c skip (flushed at "
    "the checkpoint). Reward the reason 'nothing was written before commit' for the no-undo point.",
    "ACTIVITY [~5 min].")
add_quiz("S42 — Quick Check  ·  ~5 min",
    [("Q1.  In deferred update (NO-UNDO/REDO), uncommitted transactions need:","q"),
     ("a) undo only   b) both undo and redo   c) ✅ no undo   d) redo only","a"),
     ("     Why: writes are deferred until commit, so an uncommitted txn changed nothing on disk.","o"),
     ("Q2.  Writing the log record before the data page is the rule called:","q"),
     ("a) checkpointing   b) ✅ Write-Ahead Logging (WAL)   c) shadow paging   d) in-place update","a"),
     ("     Why: WAL guarantees the undo/redo information is safe before the data changes.","o"),
     ("Discussion: after a crash you find [start,T] but no [commit,T] for Rita's transfer under deferred update. What do you do, and why is it safe?","o")],
    "QUIZ [~5 min]. Draw out no-undo (nothing written pre-commit) and WAL as the durability guarantee.")
add_summary("S42 · Summary  ·  [~2 min]",
    ["Recovery restores the last consistent state from the log: UNDO the uncommitted, REDO the committed.",
     "Write-Ahead Logging (log before data page) plus checkpoints make recovery correct and fast.",
     "Deferred update writes only after commit → NO-UNDO/REDO, but strains memory for long/large transactions."],
    "Deferred-update-style recovery is why a wallet app can confidently show 'Transfer successful' even though the actual "
    "disk write may happen slightly later — the committed log record is the real guarantee.",
    "S43 — the alternative: write to the database immediately (and be ready to UNDO), plus shadow paging.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S43
add_divider("Session 43 · Lecture hour 7 (of 8)","Recovery Based on Immediate Update · Shadow Paging",
    "What if eSewa wrote each debit to disk INSTANTLY — faster, but now a crash can leave a half-done transfer already on "
    "disk. How do we take it back? And is there a way to update with no undo log at all?",
    "OPENING HOOK [~5 min]. Motivate UNDO and an alternative to logging. Agenda: immediate update → UNDO/REDO variants → recovery "
    "procedure → shadow paging → its pros/cons.")

concept_understand("S43 · Concept 1 · [THEORY]","Immediate Update",
    "In the immediate-update technique, the database is modified WHILE the transaction is still active — before it commits "
    "— with Write-Ahead Logging enforced. Because uncommitted changes may already be on disk, recovery requires BOTH "
    "UNDO (for uncommitted writes) and REDO (for committed writes not yet flushed).",
    ["Changes are written to the database as operations execute, not deferred to commit.",
     "WAL is mandatory: the old value must be logged before the data page changes, so UNDO is possible.",
     "UNDO handles uncommitted writes already on disk; REDO handles committed writes still in buffer.",
     "This is the UNDO/REDO model used by most real DBMS engines."],
    "s43_immediate.png","Immediate update writes early → recovery needs BOTH UNDO and REDO.",
    "~8 min. Rita's debit hits the wallet table immediately; if she aborts, UNDO restores the old balance from the log.")
concept_apply("S43 · Concept 1 · [THEORY]","Immediate Update",
    "Under immediate update, Rita's debit is written to the wallet table AS it happens. If she then aborts (or the server "
    "crashes before commit), that debit is already on disk, so recovery must UNDO it — restoring her old balance from the "
    "log's old value. Committed-but-unflushed transfers are REDONE. Hence UNDO/REDO.",
    "\"Immediate update is just deferred update done faster.\" No — it changes the RECOVERY requirement: because "
    "uncommitted changes can reach disk, you now MUST be able to UNDO them. Deferred update never needs undo; immediate "
    "update always might.",
    "The immediate-update technique writes a transaction's changes to the database while it is still active (before "
    "commit), under Write-Ahead Logging. Because uncommitted changes may already be on disk, recovery requires both UNDO "
    "(rolling back uncommitted writes using logged old values) and REDO (reapplying committed writes still in the "
    "buffer). It is the UNDO/REDO model implemented by most production DBMSs.",
    "immediate update · write before commit · WAL enforced · UNDO/REDO · old value enables undo")

concept_understand("S43 · Concept 2 · [THEORY]","UNDO/REDO vs UNDO-only Variants",
    "Immediate update has variants depending on flushing policy. UNDO/REDO (the general case) does not force all writes to "
    "disk at commit, so it may need REDO. UNDO-only forces all of a transaction's writes to disk at commit, so committed "
    "changes are already durable and no REDO is ever needed.",
    ["UNDO/REDO: don't force-flush at commit → may need both undo and redo (most flexible).",
     "UNDO-only (force at commit): flush all writes at commit → committed data is on disk → no redo needed.",
     "Contrast with deferred update's NO-UNDO/REDO (writes only after commit → no undo).",
     "The choice trades commit-time I/O against recovery-time work."],
    None,"UNDO-only forces writes at commit (no redo); UNDO/REDO defers the flush (may redo).",
    "~7 min. Put the three techniques side by side in the table so the undo/redo needs are unmistakable.")
concept_apply("S43 · Concept 2 · [THEORY]","UNDO/REDO vs UNDO-only Variants",
    "A payment system that force-flushes each committed transfer to disk (UNDO-only) never needs REDO — once 'success' is "
    "shown, the data is already on disk — but pays extra I/O at every commit. A system that lets committed changes linger "
    "in the buffer (UNDO/REDO) commits faster but must REDO after a crash. Both must UNDO uncommitted writes.",
    "\"All immediate-update recovery is the same.\" No — forcing writes at commit (UNDO-only) removes the REDO step but "
    "adds commit-time I/O; not forcing (UNDO/REDO) is faster at commit but needs REDO on recovery. It's a real trade-off.",
    "Immediate-update variants differ by commit-time flushing: the general UNDO/REDO variant does not force all writes to "
    "disk at commit, so recovery may need REDO as well as UNDO; the UNDO-only variant forces all of a transaction's "
    "writes to disk at commit, making committed changes durable so no REDO is needed. Both contrast with deferred "
    "update's NO-UNDO/REDO, and the choice trades commit-time I/O against recovery work.",
    "UNDO/REDO · UNDO-only (force-at-commit) · no-redo when forced · commit-time I/O trade-off · vs NO-UNDO/REDO")
add_comparison_table("S43 · Concept 2 · comparison","The three recovery techniques — UNDO/REDO needs at a glance",
    ["Technique","When DB is written","UNDO needed?","REDO needed?","Trade-off"],
    [["Deferred update","only AFTER commit","No (nothing written pre-commit)","Yes (committed, maybe buffered)","simple, but strains buffer for big txns"],
     ["Immediate update (UNDO/REDO)","during the txn; no force at commit","Yes (uncommitted may be on disk)","Yes (committed, maybe buffered)","fast commit; most recovery work"],
     ["Immediate update (UNDO-only)","during the txn; force at commit","Yes","No (forced to disk at commit)","no redo, but extra commit-time I/O"],
     ["Shadow paging","new pages; pointer flip at commit","No (discard new pages)","No (pointer flip is atomic)","no undo log, but fragmentation & poor concurrency"]],
    per_page=4,widths=[1.9,2.2,1.7,1.7,2.5],fs=10.5,
    note="Read the undo/redo columns as the exam answer: deferred = NO-UNDO/REDO; immediate = UNDO/REDO (or UNDO-only if "
         "force-flushed); shadow paging needs neither because commit is an atomic pointer switch.")

concept_understand("S43 · Concept 3 · [THEORY]","Recovery Procedure for Immediate Update",
    "To recover an immediate-update database after a crash, the recovery manager scans the log and: REDOes every "
    "committed transaction (forward, using new values) and UNDOes every uncommitted transaction (in REVERSE order, using "
    "old values).",
    ["Identify committed transactions ([start]+[commit]) and uncommitted ones ([start], no [commit]).",
     "REDO committed transactions forward from their logged new values.",
     "UNDO uncommitted transactions backward (reverse order) from their logged old values.",
     "Reverse order for UNDO ensures overlapping changes are rolled back correctly."],
    None,"Immediate-update recovery: REDO committed (forward), UNDO uncommitted (reverse).",
    "~7 min. Walk the eSewa log after a crash: redo the committed transfer, undo the half-done one from its old values.")
concept_apply("S43 · Concept 3 · [THEORY]","Recovery Procedure for Immediate Update",
    "After an eSewa crash under immediate update, the log shows one committed transfer and one that wrote a debit but "
    "never committed. Recovery REDOes the committed transfer (reapplying its new values) and UNDOes the uncommitted one "
    "in reverse, restoring the old balance from the logged old value — so the half-done debit disappears.",
    "\"You can undo transactions in any order.\" No — UNDO must go in REVERSE chronological order so that if two "
    "uncommitted writes touched the same item, the earliest old value is restored last and the item ends correct.",
    "Recovery under immediate update scans the log and REDOes all committed transactions (in forward order, using logged "
    "new values) while UNDOing all uncommitted transactions (in reverse order, using logged old values). Redoing ensures "
    "committed changes are durable even if only buffered; undoing in reverse ensures overlapping uncommitted changes are "
    "correctly rolled back to the last consistent state.",
    "immediate-update recovery · REDO committed forward · UNDO uncommitted reverse · old/new values · consistent state")

concept_understand("S43 · Concept 4 · [THEORY] [EXAMPLE]","Shadow Paging",
    "Shadow paging is a recovery technique that keeps an unchanged SHADOW (old) copy of the page table while updates go "
    "to NEW copies of pages. Committing means atomically switching the current page-table pointer to the new table; "
    "aborting means discarding the new pages and keeping the shadow — so no undo log is needed.",
    ["Two page tables: a shadow (points to old, unchanged pages) and a current (points to new pages).",
     "A write creates a NEW copy of the page; the shadow's pages are never overwritten.",
     "Commit = atomically switch the pointer from the shadow to the current page table.",
     "Abort = simply discard the new pages; the shadow already points to the consistent old state (no undo)."],
    "s43_shadow.png","Shadow paging: edit copies, then flip the page-table pointer atomically to commit.",
    "~8 min. Analogy: edit a PHOTOCOPY; if happy, make the copy official (pointer flip); if not, tear it up and keep the original.")
concept_apply("S43 · Concept 4 · [THEORY] [EXAMPLE]","Shadow Paging",
    "A batch update to a customer table is done on shadow pages: new copies of the changed pages are written while the "
    "originals stay put. If the batch succeeds, one atomic pointer flip makes all the new pages live at once; if it "
    "fails, the new pages are discarded and the original (shadow) table is untouched — recovery is instant with no undo log.",
    "\"Shadow paging is always better because it needs no log.\" No — it causes data fragmentation, complicates "
    "concurrency (hard to share pages being versioned), and needs garbage collection of old pages, so it scales poorly. "
    "Most real DBMSs still use log-based recovery.",
    "Shadow paging keeps a shadow (old) page table pointing to the original pages while updates are written to new page "
    "copies referenced by a current page table. Committing atomically switches the pointer to the current table; "
    "aborting discards the new pages and retains the shadow, so no undo log is required. Its drawbacks — fragmentation, "
    "poor concurrency support, and garbage collection — mean most production systems prefer log-based recovery.",
    "shadow paging · shadow vs current page table · new page copies · atomic pointer switch · no undo log · fragmentation")

concept_understand("S43 · Concept 5 · [THEORY]","Pros and Cons of Shadow Paging",
    "Shadow paging's advantage is simplicity — atomic commit by pointer flip and no undo log. Its disadvantages are data "
    "fragmentation, difficulty supporting high concurrency, and the overhead of garbage-collecting obsolete pages.",
    ["Pro: commit/abort are simple and atomic; no undo log to maintain.",
     "Con: updated pages scatter across the disk → fragmentation and lost locality.",
     "Con: hard to combine with high-concurrency access to shared pages.",
     "Con: old (shadow) pages must be garbage-collected, adding overhead."],
    None,"Shadow paging: simple atomic commit, but fragments data and scales poorly under concurrency.",
    "~5 min. Note where the idea lives on: copy-on-write file systems and storage snapshots.")
concept_apply("S43 · Concept 5 · [THEORY]","Pros and Cons of Shadow Paging",
    "Shadow-paging ideas survive in copy-on-write file systems and storage snapshots (e.g. taking a point-in-time "
    "snapshot before an upgrade). But for a high-concurrency wallet like eSewa, its fragmentation and weak concurrency "
    "support make log-based UNDO/REDO the better fit — which is exactly what MySQL/InnoDB and PostgreSQL implement.",
    "\"Shadow paging is obsolete and unused.\" No — while unsuitable as a busy DBMS's main recovery method, its "
    "copy-on-write, atomic-switch idea is alive in modern file systems and snapshot features. The concept matters even "
    "where the full technique doesn't scale.",
    "Shadow paging's pros are its simplicity: atomic commit via a pointer switch and no need for an undo log. Its cons "
    "are data fragmentation (updated pages scatter), poor support for high concurrency, and the overhead of garbage "
    "collecting obsolete shadow pages. These limitations lead most DBMSs to use log-based recovery, though the "
    "copy-on-write idea persists in modern file systems and snapshots.",
    "pros: simple, atomic commit, no undo log · cons: fragmentation, poor concurrency, garbage collection · copy-on-write legacy")

add_solved_problem("S43 · Solved problem · [EXAMPLE]","Recover an immediate-update log (UNDO + REDO)",
    "After a crash under IMMEDIATE update, the log shows: [start,T1] [write,T1,X,10,50] [commit,T1] [start,T2] "
    "[write,T2,Y,20,80] — then CRASH (no [commit,T2]). Both writes may already be on disk. What does recovery do?",
    ["Immediate update is UNDO/REDO: uncommitted changes can already be on disk, so undo is required.",
     "Classify: T1 has [start]+[commit] → committed; T2 has [start] but no [commit] → uncommitted.",
     "REDO T1 forward from its NEW value → ensure X=50 is on disk (it may only have been buffered).",
     "UNDO T2 using its OLD value → restore Y=20 (its write of 80 may already be on disk and must be rolled back).",
     "Process UNDO in reverse order of the log for correctness."],
    "REDO T1 (X→50, committed) and UNDO T2 (Y→20, uncommitted). This needs BOTH operations — the defining feature of "
    "immediate update (UNDO/REDO), unlike deferred update which never undoes.",
    "SOLVED PROBLEM [~8 min]. Contrast directly with the S42 deferred-update problem: there T2 needed no undo; here it does.")

add_activity("S43 — 'Edit the original vs edit a photocopy'  ·  ~5 min",
    ["In pairs (3 min): for a bank's nightly batch update, compare IMMEDIATE update (edit the original directly) with "
     "SHADOW paging (edit a photocopy, then flip the pointer).",
     "For each, state what happens on a mid-batch crash and what recovery costs.",
     "Decide which you'd trust more for this batch and why.",
     "Share (2 min): immediate = UNDO/REDO from the log; shadow = discard new pages, keep the original (instant, no undo log)."],
    "Immediate update: crash → UNDO uncommitted from the log, REDO committed. Shadow paging: crash before the pointer "
    "flip → the original is intact, discard new pages. Reward reasoning about concurrency and fragmentation, not just correctness.",
    "ACTIVITY [~5 min].")
add_quiz("S43 — Quick Check  ·  ~5 min",
    [("Q1.  Immediate-update recovery requires:","q"),
     ("a) undo only   b) redo only   c) ✅ both UNDO and REDO   d) neither","a"),
     ("     Why: uncommitted writes may be on disk (need UNDO) and committed writes may be buffered (need REDO).","o"),
     ("Q2.  In shadow paging, committing a transaction means:","q"),
     ("a) writing an undo log   b) ✅ switching the current page-table pointer to the new page table   c) flushing the buffer   d) taking a lock","a"),
     ("     Why: commit is an atomic pointer switch to the new pages; abort just discards them.","o"),
     ("Discussion: compare 'edit the original directly' (immediate update) vs 'edit a photocopy' (shadow paging) for a bank's nightly batch — which would you trust more and why?","o")],
    "QUIZ [~5 min]. Reinforce UNDO/REDO for immediate update and the atomic pointer flip for shadow paging.")
add_summary("S43 · Summary  ·  [~2 min]",
    ["Immediate update writes changes during the transaction (WAL enforced) → recovery needs BOTH UNDO and REDO.",
     "Recovery: REDO committed transactions forward; UNDO uncommitted ones in reverse, from the log's old values.",
     "Shadow paging swaps page tables atomically at commit (no undo log), but fragments data and scales poorly under concurrency."],
    "The UNDO/REDO model is what production engines (PostgreSQL, MySQL/InnoDB behind Nepali apps) actually implement; "
    "shadow-paging's copy-on-write idea lives on in file-system snapshots.",
    "S44 — when the WHOLE disk or data-center is destroyed: backup and catastrophic recovery (closes the unit).",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============================================================ S44
add_divider("Session 44 · Lecture hour 8 (of 8) — CLOSES UNIT 6","Backup & Recovery from Catastrophic Failures",
    "An earthquake floods a Kathmandu data-center and the whole disk array is destroyed — the transaction log is gone "
    "too. Log-based recovery (S42–S43) assumed the disk survived. Now what saves your eSewa balance?",
    "OPENING HOOK [~5 min]. Distinguish catastrophic from ordinary failure. Agenda: catastrophic vs non-catastrophic → backups → "
    "3-2-1 strategy → recovery procedure → RPO/RTO & HA → Unit 6 synthesis.")

concept_understand("S44 · Concept 1 · [THEORY]","Catastrophic vs Non-Catastrophic Failure",
    "A non-catastrophic failure is a crash where the disk survives — handled by log-based recovery (S42–S43). A "
    "catastrophic failure destroys the storage media or whole site (disk failure, fire, flood, earthquake, ransomware), "
    "so the on-disk data AND log may be gone — only a separate backup can recover it.",
    ["Non-catastrophic: power cut, software crash → memory lost but disk (and log) intact → undo/redo from the log.",
     "Catastrophic: the disk/site itself is destroyed → the log on that disk is gone too.",
     "Catastrophic failure is why backups must live on SEPARATE, ideally off-site, storage.",
     "The two need completely different recovery strategies."],
    None,"Non-catastrophic → recover from the log; catastrophic → recover from a separate backup.",
    "~7 min. 2015-earthquake / fire / flood scenario for a Nepali bank data-center; ransomware wiping the disks.")
concept_apply("S44 · Concept 1 · [THEORY]","Catastrophic vs Non-Catastrophic Failure",
    "A load-shedding power cut is non-catastrophic — the bank's disk survives, so recovery replays the log (S42–S43). But "
    "an earthquake, fire, flood, or ransomware attack that destroys the disk array is catastrophic: the log on that disk "
    "is gone too, so the ONLY way back is a separate backup kept elsewhere.",
    "\"The transaction log alone can recover anything.\" No — if the disk holding the log is physically destroyed, there "
    "is no log to replay. Catastrophic recovery depends on a SEPARATE backup, which is why log-based recovery is not enough.",
    "A non-catastrophic failure (e.g. power cut, software crash) leaves the disk and its log intact, so log-based UNDO/REDO "
    "recovery applies. A catastrophic failure destroys the storage media or the entire site (disk failure, fire, flood, "
    "earthquake, ransomware), taking the on-disk data and log with it; recovery then depends on a separate, ideally "
    "off-site, backup. The two failure classes require fundamentally different recovery strategies.",
    "non-catastrophic (disk intact, log recovery) · catastrophic (media/site destroyed) · separate backup required")

concept_understand("S44 · Concept 2 · [THEORY]","Database Backup",
    "A database backup is a periodic copy of the database (and log) written to separate, stable storage — tape, a "
    "separate disk, or the cloud. A full backup copies everything; incremental/differential backups copy only what "
    "changed since the last backup, saving time and space.",
    ["Full backup: a complete copy of the database — slow and large, but self-contained.",
     "Incremental backup: only changes since the LAST backup — fast and small, but needs the chain to restore.",
     "Differential backup: all changes since the last FULL backup — a middle ground.",
     "The archived log lets you roll forward from a backup to the moment of failure."],
    None,"Full = copy everything; incremental = only what changed since last backup.",
    "~7 min. Backup + archived log = restore the last backup, then REDO from the archived log to the failure point.")
concept_apply("S44 · Concept 2 · [THEORY]","Database Backup",
    "A Nepali bank takes a FULL backup every midnight and INCREMENTAL backups through the day, all copied off-site (a "
    "second city or a cloud region), plus it archives the transaction log. If the data-center is destroyed at 3 PM, it "
    "restores the midnight full backup, applies the day's incrementals, and REDOes the archived log up to 3 PM.",
    "\"One backup is enough / backups can live on the same disk.\" No — a backup on the SAME disk dies with it in a "
    "catastrophe. Backups must be on separate media and ideally off-site, and you need the archived log to roll forward "
    "to the failure point.",
    "A database backup is a periodic copy of the database (and its log) stored on separate, stable media (tape, a "
    "separate disk, or cloud). A full backup copies the entire database; incremental and differential backups copy only "
    "what changed (since the last backup, or since the last full backup, respectively) to save time and space. Combined "
    "with an archived log, a backup lets you restore and then REDO forward to the point of failure.",
    "database backup · full vs incremental vs differential · separate/off-site media · archived log · roll forward")

concept_understand("S44 · Concept 3 · [THEORY]","Backup Strategy & the 3-2-1 Rule",
    "A sound backup strategy follows the 3-2-1 rule: keep 3 copies of the data, on 2 different types of media, with at "
    "least 1 copy off-site. This survives the loss of any single device or even the whole site.",
    ["3 copies: the live data plus at least two backups — redundancy against corruption.",
     "2 media types: e.g. disk + cloud (or disk + tape) — no single technology failure wipes all copies.",
     "1 off-site: a copy in another city or a cloud region — survives a site-wide disaster.",
     "Test restores regularly — an untested backup is only a hope, not a guarantee."],
    None,"3-2-1: 3 copies, 2 media, 1 off-site — survives any single site's destruction.",
    "~7 min. Analogy: keep a copy of your important documents at a relative's house in another town in case yours burns down.")
concept_apply("S44 · Concept 3 · [THEORY]","Backup Strategy & the 3-2-1 Rule",
    "A Nepali fintech applies 3-2-1: the live database (copy 1), a nightly backup on a separate on-prem disk (copy 2, "
    "media A), and an encrypted copy in a cloud region in another city (copy 3, media B, off-site) — aligning with NRB "
    "IT-guideline expectations. A fire in the main office cannot destroy all three.",
    "\"Backups guarantee recovery on their own.\" No — an untested backup can be corrupt or incomplete; you must "
    "regularly TEST restores. And a backup kept only on-site or on one medium violates 3-2-1 and can be lost in the same disaster.",
    "A robust backup strategy follows the 3-2-1 rule: maintain 3 copies of the data, on 2 different media types, with at "
    "least 1 copy stored off-site. This protects against corruption of any one copy, failure of any one media "
    "technology, and destruction of the primary site. Backups should be tested by trial restores, since an unverified "
    "backup provides no real guarantee.",
    "3-2-1 rule · 3 copies · 2 media · 1 off-site · test restores · regulatory expectation (NRB)")
add_examples_table("S44 · Concept 3 · scaffolding","A worked 3-2-1 plan for a Nepali fintech",
    ["Copy","Where it lives","Media","Purpose"],
    [["Copy 1 (live)","Primary data-center, Kathmandu","Production disk/SSD","Serves live traffic"],
     ["Copy 2 (backup)","Same site, separate server","Separate disk / NAS","Fast restore from local failure"],
     ["Copy 3 (off-site)","Cloud region / second city","Cloud object storage","Survives a site-wide disaster"],
     ["Archived log","Off-site with copy 3","Cloud / tape","Roll forward to the failure point"],
     ["Full backup","Nightly (e.g. midnight)","All media","Self-contained restore baseline"],
     ["Incremental backup","Hourly through the day","All media","Small, fast, limits data loss (low RPO)"]],
    per_page=6,widths=[1.7,2.4,1.9,2.5],fs=11,
    note="3 copies (live + local + off-site), 2 media (disk + cloud/tape), 1 off-site — plus the archived log to roll "
         "forward. A fire or earthquake at the primary site cannot destroy every copy.")

concept_understand("S44 · Concept 4 · [THEORY] [EXAMPLE]","Recovery from Catastrophic Failure",
    "To recover from a catastrophic failure: restore the most recent FULL backup, apply any INCREMENTAL backups in order, "
    "then REDO committed transactions from the archived log up to the point of failure. This reconstructs the database as "
    "close to the failure moment as the backups and log allow.",
    ["Step 1: restore the latest full backup onto new/replacement hardware.",
     "Step 2: apply incremental/differential backups in chronological order.",
     "Step 3: REDO committed transactions from the archived log to the failure point.",
     "The gap between the last backup/log and the failure is the data you actually lose (the RPO)."],
    None,"Restore full backup → apply incrementals → REDO archived log to the failure point.",
    "~7 min. Data-center down at 3 PM; last full backup midnight + archived logs → reconstruct up to 3 PM.")
concept_apply("S44 · Concept 4 · [THEORY] [EXAMPLE]","Recovery from Catastrophic Failure",
    "A bank's data-center is destroyed at 3 PM. Recovery on replacement hardware: restore the midnight FULL backup, apply "
    "the day's INCREMENTAL backups, then REDO the archived transaction log up to 3 PM. The reconstructed database matches "
    "the state just before the disaster — as long as the off-site log was current.",
    "\"After a catastrophe you just restore the backup and you're done.\" No — the backup alone only gets you to the last "
    "backup time; you must also REDO the ARCHIVED LOG to roll forward to the failure point, or you lose every transaction "
    "since the last backup.",
    "Catastrophic recovery restores the most recent full backup, applies incremental/differential backups in order, and "
    "then REDOes committed transactions from the archived log up to the point of failure, reconstructing the database on "
    "replacement hardware. The amount of data unavoidably lost is the interval not covered by the backups and archived "
    "log — the recovery point objective (RPO).",
    "catastrophic recovery · restore full backup · apply incrementals · REDO archived log · roll forward to failure")

concept_understand("S44 · Concept 5 · [THEORY]","Disaster Recovery — RPO, RTO & High Availability",
    "Disaster-recovery planning is measured by two objectives: RPO (recovery point objective) — how much data you can "
    "afford to lose (how far back the last usable copy is) — and RTO (recovery time objective) — how fast you must be "
    "back up. High availability (replication/standby servers) protects UPTIME, which is different from backups protecting DATA.",
    ["RPO: the maximum acceptable data loss, set by how frequently you back up / archive the log.",
     "RTO: the maximum acceptable downtime, set by how fast you can restore and switch over.",
     "Replication/standby servers keep a live copy running so failover is near-instant (low RTO).",
     "Backups protect the DATA; high availability protects UPTIME — you usually need both."],
    "s44_backup.png","RPO = data you can lose; RTO = time to be back; HA ≠ backup.",
    "~6 min. Bust the myth: backups protect data, HA/replication protects uptime — different goals, both needed.")
concept_apply("S44 · Concept 5 · [THEORY]","Disaster Recovery — RPO, RTO & High Availability",
    "A wallet provider might set RPO = 5 minutes (hourly-plus log archiving, so at most a few minutes of transactions "
    "lost) and RTO = 30 minutes (a standby replica it can fail over to). The replica gives high availability (low "
    "downtime); the off-site backups give recoverability (low data loss) — two different guarantees.",
    "\"Backups give you high availability.\" No — backups protect your DATA (recoverability); high availability (live "
    "replication, standby servers) protects UPTIME. A daily backup does nothing for the hours a system is down; a replica "
    "does nothing if both copies are corrupted. You need both.",
    "Disaster-recovery planning is quantified by the recovery point objective (RPO) — the maximum tolerable data loss, "
    "determined by backup/log-archiving frequency — and the recovery time objective (RTO) — the maximum tolerable "
    "downtime, determined by how fast you can restore and fail over. High availability (replication, standby servers) "
    "protects uptime and is distinct from backups, which protect data; a complete strategy needs both.",
    "RPO (data loss tolerated) · RTO (downtime tolerated) · replication/standby · high availability ≠ backup")

add_solved_problem("S44 · Capstone · [EXAMPLE]","Unit 6 synthesis — one transfer, all concepts",
    "Trace 'Rita sends Rs. 500 to Hari' end-to-end through the WHOLE unit, then outline a disaster-recovery plan — the "
    "capstone that ties transactions, concurrency, and recovery together.",
    ["TRANSACTION (S37): read Rita → debit 500 → credit Hari → commit; states Active → Partially Committed → Committed; "
     "logged as [start][write][write][commit].",
     "ACID (S38): Atomicity (both or neither), Consistency (3000 total preserved), Isolation (no interference), Durability (survives crash).",
     "SCHEDULE (S39): if concurrent with other transfers, the schedule must be conflict-serializable (acyclic precedence graph).",
     "CONCURRENCY CONTROL (S40–S41): enforced by strict 2PL (X-lock both rows) OR timestamp ordering (serve in ticket order).",
     "RECOVERY (S42–S43): a crash → REDO if committed, UNDO if not (immediate update) / REDO-only (deferred update).",
     "CATASTROPHE (S44): if the data-center is destroyed, restore the off-site 3-2-1 backup + REDO the archived log to the failure point."],
    "One transfer touches every idea in Unit 6: it is a logged transaction (S37) obeying ACID (S38), run in a "
    "serializable schedule (S39) enforced by locking or timestamps (S40–S41), made durable by log-based recovery "
    "(S42–S43), and protected against disaster by a 3-2-1 backup with RPO/RTO targets (S44).",
    "CAPSTONE [~8 min]. This is exam Q16–Q18 combined — the single 'one transfer, all concepts' narrative students should be able to give.")

add_activity("S44 — 'Design a 3-2-1 backup plan'  ·  ~5 min",
    ["In pairs (3 min): design a one-paragraph backup + disaster-recovery plan for a small Nepali fintech startup using the 3-2-1 rule.",
     "Say WHERE each of the 3 copies lives, on WHICH 2 media, and which 1 is off-site.",
     "State a target RPO and RTO and justify them for a wallet.",
     "Share (2 min): check every plan survives losing the primary site entirely."],
    "Good plans: live DB + local backup + cloud/off-site copy; disk + cloud media; log archived off-site; RPO minutes "
    "(frequent log archiving), RTO short (a standby replica). Reward plans that survive the primary site being destroyed.",
    "ACTIVITY [~5 min].")
add_quiz("S44 — Quick Check  ·  ~5 min",
    [("Q1.  Recovery from a physically destroyed disk relies primarily on:","q"),
     ("a) the buffer cache   b) the precedence graph   c) ✅ an off-site / separate backup (plus archived log)   d) shared locks","a"),
     ("     Why: if the disk (and its log) is destroyed, only a separate backup can restore the data.","o"),
     ("Q2.  'How much data loss is acceptable' is measured by:","q"),
     ("a) RTO   b) ✅ RPO   c) throughput   d) latency","a"),
     ("     Why: RPO = recovery POINT objective = the maximum tolerable data loss; RTO is downtime.","o"),
     ("Discussion: design a one-paragraph backup plan for a small Nepali fintech startup using the 3-2-1 rule — where do the copies live?","o")],
    "QUIZ [~5 min]. Reinforce backup ≠ high availability and RPO (data) vs RTO (time).")
add_summary("S44 · Summary  ·  [~2 min]",
    ["A catastrophic failure destroys the disk/log → only a separate, off-site backup can save you (log recovery is not enough).",
     "Recover by restoring the last full backup, applying incrementals, and REDOing the archived log to the failure point.",
     "Plan with 3-2-1 (3 copies, 2 media, 1 off-site), RPO (data loss) and RTO (downtime), and replication for uptime (HA ≠ backup)."],
    "Every regulated financial institution in Nepal (banks and wallet providers under NRB) must have a documented "
    "disaster-recovery/backup plan — this is a compliance requirement and an employability essential for any DBA or backend role.",
    "End of Unit 6. Next unit: Advanced topics — performance tuning, security, distributed databases, warehousing, big data, and NoSQL.",
    "REAL-LIFE APPLICATION [~3 min] + SUMMARY [~2 min].")

# ============= END-OF-UNIT REVISION AIDS =============
add_cheatsheet("Unit 6 · Cheat Sheet","One-page revision reference",
    [("Transactions & log (S37)","Transaction = all-or-nothing unit (BEGIN→ops→COMMIT/ROLLBACK). States: Active→Partially "
      "Committed→Committed; or Failed→Aborted. Log: [start][write,X,old,new][commit]; old→UNDO, new→REDO."),
     ("ACID (S38)","Atomicity = all-or-nothing; Consistency = valid→valid (invariant); Isolation = no interference; "
      "Durability = survives crash. A/C/D via log; I via concurrency control."),
     ("Serializability (S39)","Schedule = ordering of ops. Serializable = equals some serial order. Conflict = same item, "
      "diff txn, ≥1 write. Serializable ⟺ acyclic precedence graph. Cycle ≠ deadlock."),
     ("2PL & deadlock (S40)","S (read, shareable) / X (write, exclusive) locks. 2PL: grow (acquire) then shrink (release), "
      "one peak → serializable. Deadlock = cycle in wait-for graph → abort a victim. Starvation → aging."),
     ("Timestamp ordering (S41)","TS at start (older=priority); item has read_TS, write_TS. Out-of-order op → abort & "
      "restart. No waiting → no deadlock (starvation possible). Thomas's rule = ignore obsolete write."),
     ("Recovery & backup (S42–S44)","Deferred = write after commit → NO-UNDO/REDO. Immediate = write early → UNDO/REDO. "
      "Shadow paging = atomic pointer flip, no undo log. Catastrophe → 3-2-1 backup + REDO archived log; RPO vs RTO.")])

add_glossary("Unit 6 · Glossary","Key terms — quick reference",
    [("Transaction","an all-or-nothing logical unit of database work (BEGIN → COMMIT/ROLLBACK)."),
     ("read_item / write_item","the basic read and write operations on a data item."),
     ("Transaction states","Active, Partially Committed, Committed, Failed, Aborted."),
     ("System log (journal)","sequential record of writes on stable storage for UNDO/REDO."),
     ("Atomicity","all operations happen or none do (rollback on failure)."),
     ("Consistency","a transaction takes the DB from one valid state to another."),
     ("Isolation","concurrent transactions don't interfere; each appears to run alone."),
     ("Durability","once committed, changes survive any later crash."),
     ("Schedule (history)","an ordering of the operations of several transactions."),
     ("Serial / non-serial","one-at-a-time vs interleaved schedule."),
     ("Serializable","equivalent in effect to some serial schedule."),
     ("Conflict","same item, different txns, at least one write (W-W/R-W/W-R)."),
     ("Precedence graph","node per txn, edge on conflict; acyclic ⟺ conflict-serializable."),
     ("Lost update","two txns read then both write, so one update is overwritten."),
     ("Lock (S / X)","shared read lock (shareable) / exclusive write lock (one holder)."),
     ("Two-Phase Locking","acquire all locks (growing) before releasing any (shrinking)."),
     ("Strict 2PL","hold exclusive locks until commit → no cascading rollback."),
     ("Deadlock","circular wait for locks; a cycle in the wait-for graph."),
     ("Starvation","a transaction repeatedly delayed/aborted; fixed with aging."),
     ("Timestamp (TS)","unique increasing ID at start; older = higher priority."),
     ("read_TS / write_TS","newest reader / writer timestamp stored on a data item."),
     ("Thomas's write rule","ignore an obsolete write instead of aborting the txn."),
     ("Write-Ahead Logging","write the log record before the data page (enables recovery)."),
     ("Checkpoint","flush buffers + log a mark; bounds how far recovery scans."),
     ("Deferred update","write only after commit → NO-UNDO/REDO."),
     ("Immediate update","write during the txn (WAL) → UNDO/REDO."),
     ("Shadow paging","new page copies + atomic pointer flip at commit; no undo log."),
     ("Catastrophic failure","media/site destroyed; needs a separate backup."),
     ("3-2-1 rule","3 copies, 2 media, 1 off-site."),
     ("RPO / RTO","tolerable data loss / tolerable downtime.")])

# ============= CONSOLIDATED END-OF-UNIT QUIZ =============
add_divider("Unit 6 · Revision","Consolidated end-of-unit quiz",
    "Ten MCQs across the whole unit (answers shown), then short-answer and long/applied questions to work from the "
    "concept slides and Unit6_material.md.",
    "Use as a 20-minute review quiz. The per-session 2-MCQ checks above are retained for in-class use.")
add_quiz("Part A — Multiple choice (answers shown)",
    [("1.  A logical unit of DB work that is all-or-nothing is a   →  ✅ transaction","a"),
     ("2.  A transaction that finished all operations but is not yet permanent is   →  ✅ partially committed","a"),
     ("3.  'Once committed, it survives a crash' is   →  ✅ durability","a"),
     ("4.  Concurrent transactions not interfering with each other is   →  ✅ isolation","a"),
     ("5.  A concurrent schedule is conflict-serializable iff its precedence graph   →  ✅ has no cycle","a"),
     ("6.  In Two-Phase Locking, releasing the first lock begins the   →  ✅ shrinking phase","a"),
     ("7.  Deadlock is detected by a cycle in the   →  ✅ wait-for graph","a"),
     ("8.  In basic timestamp ordering, an op violating timestamp order is   →  ✅ aborted and restarted","a"),
     ("9.  Deferred-update (NO-UNDO/REDO) recovery requires   →  ✅ redo only","a"),
     ("10.  Recovery from a physically destroyed disk depends primarily on   →  ✅ an off-site backup + archived log","a")],
    "Consolidated quiz Part A.",compact=True)
add_quiz("Parts B–C — short answer & long/applied",
    [("Part B — Short answer","q"),
     ("11. List the four ACID properties + the one-word job of each.   12. Draw & label the transaction state-transition diagram.","o"),
     ("13. Show one schedule on a wallet that causes a lost update.   14. State the precedence-graph rule for conflict serializability.","o"),
     ("15. Explain why immediate-update recovery needs UNDO but deferred-update does not.","o"),
     ("Part C — Long answer / applied","q"),
     ("16. Trace 'Rita sends Rs. 500 to Hari' through atomicity, isolation, and durability, and describe what the log records at each step.","o"),
     ("17. Compare 2PL and timestamp ordering: mechanism, what each guarantees, failure mode (deadlock vs starvation), and a scenario favouring each.","o"),
     ("18. Compare deferred / immediate / shadow-paging recovery (mechanism, undo/redo, pros/cons), then outline a 3-2-1 backup + DR plan for a Nepali fintech.","o")],
    "Consolidated quiz Parts B–C. Model answers are on the concept slides and in Unit6_material.md.",compact=True)

# ---- close ----
add_title("End of Unit 6  ·  IT 220",
          "S37–S44 complete: transactions & the log · ACID · serializable schedules & precedence graphs · "
          "2PL & deadlock · timestamp ordering · deferred / immediate / shadow-paging recovery · backup & catastrophic recovery",
          "Built to COURSE_MATERIAL_STANDARD.md incl. the §7A depth rule · comparison & concrete-example tables throughout · "
          "self-contained, PDF-safe · Next: Unit 7 — Advanced Topics (tuning, security, distributed DBs, warehousing, big data, NoSQL).")

_add_page_numbers()
save("IT220_Unit6.pptx")
