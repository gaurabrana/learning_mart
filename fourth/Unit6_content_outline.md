# Unit 6 — Transaction Processing, Concurrency Control & Recovery Techniques · Content Outline

**8 LHs → 8 sessions (S37–S44) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. A running **eSewa / bank money-transfer** example threads through the whole unit.
Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

> **Running example used unit-wide:** "Rita sends Rs. 500 from her eSewa wallet to Hari." This single transaction (debit Rita Rs. 500, credit Hari Rs. 500) is reused to motivate transactions (S37), ACID (S38), schedules/serializability (S39), locking (S40), timestamps (S41), and recovery (S42–S44).

---

## Unit 6 learning outcomes (what students can do after S37–S44)
1. Define a transaction, trace its states, and explain the role of the system log.
2. State and apply the ACID properties to judge whether a transaction is correct.
3. Build and analyse schedules; test for conflict serializability using a precedence graph.
4. Apply Two-Phase Locking and Timestamp Ordering to control concurrent transactions, and recognise deadlock.
5. Distinguish deferred-update, immediate-update, and shadow-paging recovery, and design a backup strategy against catastrophic failure.

---

## S37 — Introduction to Transaction Processing · Transaction & System Concepts

**Hook:** "Rita taps 'Send Rs. 500' on eSewa. The app debits her, then the wifi dies before Hari is credited. Where did the Rs. 500 go?" → a transaction must be all-or-nothing.

**Concepts & how each will be filled:**

1. **What is a transaction?**
   - Definition: a logical unit of work — one or more DB operations treated as a single indivisible action.
   - Theory bullets: begins with BEGIN, ends with COMMIT (success) or ABORT/ROLLBACK (undo); read_item(X), write_item(X).
   - Global example: ATM withdrawal = read balance → check → debit → dispense.
   - Local example: eSewa transfer = read Rita's balance → debit 500 → credit Hari 500 → commit.
   - Misconception: *"A transaction = a single SQL statement."* Correction: it can be many statements grouped into one unit.

2. **Single-user vs multi-user systems**
   - Definition: multi-user = many transactions interleave; concurrency is why this unit exists.
   - Local example: thousands of Dashain shoppers on Daraz checking out at once.
   - Mini case: "Two people pay the same NEA electricity bill at the same second" → motivates concurrency control (preview).

3. **Why transactions can go wrong (types of failures)**
   - Computer crash, transaction/system error, local errors (insufficient balance), concurrency enforcement, disk failure, physical catastrophe.
   - Local example: load-shedding kills a bank server mid-batch; Ntc data-center power trip.

4. **Transaction states & state diagram**
   - States: Active → Partially Committed → Committed; or Active → Failed → Aborted (terminated).
   - Diagram-heavy slide: the standard transaction state-transition diagram.
   - Misconception: *"Partially committed = done/safe."* Correction: not durable until fully committed and flushed.

5. **The system log (journal)**
   - Definition: sequential record of every write so the system can REDO/UNDO after failure.
   - Theory: entries — [start,T], [write,T,X,old,new], [commit,T], [abort,T]; stored on stable storage.
   - Fun element: analogy — the log is like a *khata* (ledger book) where you note every entry before acting, so you can retrace steps.
   - Local example: log entry for Rita's debit recorded before the wallet table is updated.

**Check for understanding:**
- MCQ1: A transaction that has executed all operations but not yet been made permanent is in which state? → Partially committed ✅
- MCQ2: Which log record lets the system *undo* a change? (a) [commit] (b) old value in [write,T,X,old,new] ✅ (c) [start] (d) [checkpoint]
- Discussion: "Describe one phone action that is really a multi-step transaction, and what should happen if it fails halfway."

**Real-life application:** every eSewa/Khalti payment and every bank fund transfer is wrapped in a transaction + logged — this is the safety net behind 'your money is safe.'

**Summary:** (1) transaction = all-or-nothing unit of work; (2) it moves through defined states; (3) the log records writes so failures can be recovered. **Next:** the four guarantees every good transaction must keep — ACID.

**Visual cues:** transaction state-transition diagram (centerpiece); read/write timeline of the eSewa transfer; sample log-record table. Mark slides [THEORY]/[EXAMPLE].

---

## S38 — Desirable Properties of Transactions (ACID)

**Hook:** "What if Rita's Rs. 500 was debited but never credited to Hari — and the bank says 'system was busy'? Which promise was broken?" → introduce ACID as four promises.

**Concepts & how each will be filled:**

1. **Atomicity**
   - Definition: all operations happen, or none do — no half-done transactions.
   - Local example: eSewa transfer — both debit AND credit, or roll back both.
   - Misconception: *"If the app crashes, it just leaves things as-is."* Correction: incomplete transactions must be undone (rollback).

2. **Consistency**
   - Definition: a transaction takes the DB from one valid state to another (constraints preserved).
   - Theory: invariant — total money in the system is unchanged by a transfer.
   - Local example: before = Rita 2000 + Hari 1000 = 3000; after = Rita 1500 + Hari 1500 = 3000. Sum preserved.
   - Mini case: a bug that credits Hari twice breaks consistency (money created from nothing).

3. **Isolation**
   - Definition: concurrent transactions must not interfere; each behaves as if alone.
   - Local example: Rita sending to Hari while Hari simultaneously sends to a shop — neither should see the other's half-finished state.
   - Fun element: analogy — like separate queues at different bank counters; you don't grab cash from the next person's stack mid-count.
   - Misconception: *"Isolation means transactions run one-at-a-time."* Correction: they *interleave* but must *appear* isolated.

4. **Durability**
   - Definition: once committed, changes survive any later crash.
   - Local example: after eSewa shows "Transfer successful", a power cut must not erase it.
   - Theory: achieved via the log + flushing to stable storage.

5. **ACID as a checklist**
   - One slide mapping each letter to the eSewa failure it prevents.

**Check for understanding:**
- MCQ1: "Once committed, it survives a crash" is which property? → Durability ✅
- MCQ2: Two transactions interleaving but not corrupting each other is ensured by → Isolation ✅
- Discussion: "Give a real Nepali payment scenario where breaking *consistency* would let money appear or vanish."

**Real-life application:** ACID is the literal reason regulators (NRB) trust digital wallets; fintech interview questions almost always ask 'explain ACID.'

**Summary:** (1) Atomicity = all-or-nothing; (2) Consistency = valid→valid; (3) Isolation = no interference; (4) Durability = survives crashes. **Next:** when many transactions run together, which interleavings are actually safe? → schedules & serializability.

**Visual cues:** four-quadrant ACID slide; before/after balance table showing the preserved sum (3000 = 3000).

---

## S39 — Serializable Schedules (serial vs concurrent · conflict serializability · precedence graph)

**Hook:** "Rita and Hari both top-up from the *same* shared family eSewa wallet at the exact same second. Whose top-up 'wins' — and is the final balance right?" → schedules decide correctness.

**Concepts & how each will be filled:**

1. **Schedule (history)**
   - Definition: an ordering of the operations of several transactions.
   - Theory: serial vs non-serial (concurrent/interleaved) schedule.
   - Local example: two transactions T1 (Rita +500) and T2 (Hari +300) on the family wallet, shown interleaved.

2. **The lost update / problem schedules**
   - Definition: anomalies from bad interleaving — lost update, dirty read, incorrect summary.
   - Local example: lost update — both read balance 1000, both write back, one top-up vanishes.
   - Misconception: *"Concurrency always corrupts data."* Correction: only *some* interleavings are bad; many are safe.

3. **Serializable schedule**
   - Definition: a concurrent schedule whose effect equals *some* serial order of the same transactions.
   - Theory: serializability = the gold standard of correctness for concurrency.
   - Fun element: analogy — a deck of interleaved tasks that, when you squint, is equivalent to doing them one full deck at a time.

4. **Conflicting operations & conflict serializability**
   - Definition: two ops conflict if same data item, different transactions, at least one is a write (W-W, R-W, W-R).
   - Theory: swap non-conflicting ops to test equivalence to a serial schedule.
   - Local example: T1's write on the wallet vs T2's read on the same wallet = conflict.

5. **Precedence (serialization) graph**
   - Definition: node per transaction, edge Ti→Tj when Ti's op precedes a conflicting op of Tj.
   - Rule: schedule is conflict-serializable iff the graph has **no cycle**.
   - Worked example: a 2–3 transaction graph; show one acyclic (serializable) and one with a cycle (not).
   - Misconception: *"A cycle means deadlock."* Correction: here a cycle means *not serializable* — deadlock is a different idea (S40).

**Check for understanding:**
- MCQ1: A schedule is conflict-serializable if its precedence graph → has no cycle ✅
- MCQ2: Which pair conflicts? (a) read–read (b) write–write on same item ✅ (c) ops on different items (d) ops in same transaction
- Discussion: "Sketch two top-ups on one shared wallet that cause a *lost update*, then reorder them to fix it."

**Real-life application:** the DB engine behind Daraz checkout / eSewa silently rejects or reorders unsafe interleavings so your balance is never 'lost' during peak Dashain traffic.

**Summary:** (1) schedules order interleaved ops; (2) the safe ones are serializable; (3) test conflict serializability via an acyclic precedence graph. **Next:** *how* the DBMS actually enforces serializable order — locking.

**Visual cues:** interleaved-timeline of two transactions showing a lost update; side-by-side precedence graphs (acyclic vs cyclic).

---

## S40 — Two-Phase Locking (2PL) Concurrency Control · locks · growing/shrinking phases · deadlock

**Hook:** "To stop two people grabbing the same wallet balance, the DBMS hands out 'keys' (locks). But what if Rita holds Hari's key and Hari holds Rita's?" → locking and deadlock.

**Concepts & how each will be filled:**

1. **Locks**
   - Definition: a lock reserves a data item for a transaction.
   - Types: shared (read, S) vs exclusive (write, X); lock compatibility matrix.
   - Local example: T1 takes an X-lock on the wallet row to debit it; T2 must wait.
   - Misconception: *"A shared lock blocks other readers."* Correction: multiple S-locks can coexist; only X conflicts.

2. **Two-Phase Locking protocol**
   - Definition: every transaction acquires all locks before releasing any.
   - Two phases: **growing** (only acquire) → **shrinking** (only release). One peak, no going back.
   - Theory: 2PL *guarantees* conflict-serializability.
   - Fun element: analogy — collect all your shopping items first (growing), then start returning them (shrinking); never grab again after you start putting back.

3. **Variants of 2PL**
   - Basic, conservative (lock all upfront — avoids deadlock), strict (hold X-locks till commit — avoids cascading rollback), rigorous.
   - Local example: strict 2PL on the eSewa wallet so a half-committed debit is never read by another transaction.

4. **Deadlock**
   - Definition: two+ transactions each waiting for a lock the other holds → frozen forever.
   - Local example: T1 locks Rita's row & wants Hari's; T2 locks Hari's row & wants Rita's.
   - Handling: deadlock detection (wait-for graph + cycle), prevention (wait-die / wound-wait), timeouts.
   - Misconception: *"Deadlock = the server crashed."* Correction: it's a logical stalemate; DBMS resolves it by aborting a victim.
   - Diagram: wait-for graph with a cycle.

5. **Starvation (brief)**
   - Definition: a transaction repeatedly chosen as victim / never gets its lock; fix with priorities/aging.

**Check for understanding:**
- MCQ1: In 2PL, once a transaction releases its first lock it is in the → shrinking phase ✅
- MCQ2: Deadlock is detected by finding a cycle in the → wait-for graph ✅
- Discussion: "Describe a two-person eSewa scenario that deadlocks, and which transaction you'd abort to break it."

**Real-life application:** every relational DB (MySQL/PostgreSQL behind Nepali fintech apps) uses locking; 'deadlock found' is a real error developers debug in production.

**Visual cues:** S/X lock-compatibility matrix; growing-vs-shrinking lock-count graph (one peak); wait-for graph showing a deadlock cycle.

**Summary:** (1) S/X locks reserve items; (2) 2PL (grow then shrink) guarantees serializability; (3) locking can deadlock — detect or prevent it. **Next:** a lock-free way to order transactions — timestamps.

---

## S41 — Timestamp Ordering Concurrency Control Technique

**Hook:** "Instead of fighting over keys, what if every eSewa transaction got a numbered ticket — and the DBMS just enforced 'serve in ticket order'?" → timestamp ordering, no locks.

**Concepts & how each will be filled:**

1. **Timestamps**
   - Definition: a unique, monotonically increasing ID (TS) given when a transaction starts; older TS = higher priority.
   - Theory: source — system clock or a logical counter.
   - Local example: each eSewa transfer stamped with arrival time; the earlier one is the 'senior' transaction.

2. **Read/Write timestamps on data items**
   - Definition: each item X keeps read_TS(X) (newest reader) and write_TS(X) (newest writer).
   - Diagram: a data item annotated with its two timestamps.

3. **Basic Timestamp Ordering protocol**
   - Rule: a read/write that would violate timestamp order is rejected → the transaction is **aborted and restarted** with a new (larger) timestamp.
   - Theory: produces a serializable schedule equivalent to timestamp order; guarantees no deadlock (no waiting).
   - Local example: a 'late' transaction trying to write a wallet already written by a 'newer' transaction is rolled back.
   - Misconception: *"Timestamp ordering can deadlock like 2PL."* Correction: no — it never waits, so no deadlock (but it can cause repeated restarts/starvation).

4. **Thomas's Write Rule**
   - Definition: an obsolete (outdated) write can be safely *ignored* instead of aborting → allows more concurrency.
   - Brief worked example showing a write that is simply skipped.

5. **2PL vs Timestamp Ordering**
   - Comparison table: locking/waiting (2PL, deadlock possible) vs no-locking/restarts (TO, starvation possible).
   - Mini case: which fits a high-conflict eSewa peak vs a low-conflict reporting job.

**Check for understanding:**
- MCQ1: In basic timestamp ordering, a transaction that violates the timestamp order is → aborted and restarted ✅
- MCQ2: Compared to 2PL, basic timestamp ordering → cannot deadlock ✅
- Discussion: "Timestamp ordering never deadlocks but can starve a transaction. Why is that trade-off sometimes acceptable for a wallet system?"

**Real-life application:** timestamp/multiversion ordering underpins high-concurrency systems and many distributed databases (relevant to large-scale e-commerce and telecom billing in South Asia).

**Visual cues:** data item with read_TS/write_TS labels; flowchart of accept/reject/abort decision; 2PL-vs-TO comparison table.

**Summary:** (1) timestamps give a fixed serial order; (2) operations out of order are aborted/restarted; (3) no deadlock, but possible starvation; Thomas's rule boosts concurrency. **Next:** what happens *after* something fails — recovery begins.

---

## S42 — Recovery Concepts · NO-UNDO/REDO Recovery Based on Deferred Update

**Hook:** "The eSewa server crashes one second after Rita's transfer commits — and a second before it crashes during Hari's. After reboot, which one must be redone and which thrown away?" → recovery.

**Concepts & how each will be filled:**

1. **Recovery concepts & the log's role**
   - Definition: restoring the DB to the last consistent state after a failure, using the log.
   - Theory: undo (remove effects of uncommitted T) vs redo (reapply effects of committed T).
   - Local example: post-crash, the DBMS scans the eSewa log to decide undo/redo per transaction.

2. **Caching, in-place update, and the WAL principle**
   - Definition: writes hit the buffer/cache first, then disk; Write-Ahead Logging = log record on stable storage *before* the data page.
   - Misconception: *"Data is written to disk the instant you commit."* Correction: it may sit in the buffer; the *log* is what guarantees durability.

3. **Checkpoints**
   - Definition: periodic point where buffers are flushed and a [checkpoint] mark is logged → limits how far back recovery must scan.
   - Fun element: analogy — a save point in a video game; you never replay the whole game, just from the last save.

4. **Deferred Update (NO-UNDO/REDO)**
   - Definition: defer all actual DB writes until *after* commit; until then changes live only in the log/buffer.
   - Why NO-UNDO: uncommitted transactions never touched the DB, so nothing to undo.
   - Why REDO: committed-but-not-yet-flushed transactions are reapplied from the log.
   - Local example: Rita's debit is only written to the wallet table after [commit,T]; if she crashes before commit, the DB was never changed → no undo needed.
   - Mini case: post-crash recovery list — REDO every transaction with both [start] and [commit] in the log; ignore the rest.

5. **Limitation of deferred update**
   - Brief: long transactions hold lots of changes in buffer; not ideal for huge updates → motivates S43.

**Check for understanding:**
- MCQ1: In deferred update (NO-UNDO/REDO), uncommitted transactions need → no undo ✅
- MCQ2: Writing the log record before the data page is the rule called → Write-Ahead Logging ✅
- Discussion: "After a crash, you find [start,T] but no [commit,T] for Rita's transfer under deferred update. What do you do, and why is it safe?"

**Real-life application:** deferred-update style recovery is why a wallet app can confidently show 'Transfer successful' even though the disk write happens slightly later.

**Visual cues:** undo-vs-redo decision tree; log timeline with a crash arrow and a checkpoint mark; buffer→disk flow diagram.

**Summary:** (1) recovery = restore last consistent state via the log; (2) WAL + checkpoints make it efficient; (3) deferred update needs REDO only (no UNDO). **Next:** the alternative — write immediately and be ready to undo.

---

## S43 — Recovery Technique Based on Immediate Update · Shadow Paging

**Hook:** "What if eSewa wrote each debit to disk *instantly* — faster, but now a crash can leave a half-done transfer on disk. How do we take it back?" → immediate update needs UNDO.

**Concepts & how each will be filled:**

1. **Immediate Update**
   - Definition: DB is updated *while* the transaction is still active (before commit), with WAL enforced.
   - Theory: requires both UNDO (for uncommitted writes already on disk) and REDO (for committed writes not yet flushed) → UNDO/REDO.
   - Local example: Rita's debit hits the wallet table immediately; if she aborts, UNDO restores the old balance from the log.

2. **UNDO/REDO vs UNDO-only (variants)**
   - UNDO/REDO (no forced flush at commit) vs UNDO-only (force all writes to disk at commit → no redo needed).
   - Comparison with S42's deferred update (NO-UNDO/REDO) in one table.
   - Misconception: *"Immediate update is just deferred update done faster."* Correction: it changes the recovery requirement — now you *must* be able to undo.

3. **Recovery procedure for immediate update**
   - Rule: REDO committed transactions; UNDO uncommitted ones (using old values from log, in reverse order).
   - Worked mini-walkthrough on the eSewa log after a crash.

4. **Shadow Paging**
   - Definition: keep a *shadow* (old) page table unchanged; updates go to *new* copies of pages; commit = switch the page-table pointer atomically.
   - Theory: no log needed for undo in pure form; abort = just discard new pages and keep the shadow.
   - Fun element: analogy — editing a *photocopy* of a document; if you're happy you make the copy official, otherwise you tear it up and keep the original.
   - Local example: a batch update to a customer table done on shadow pages; pointer flip makes it live atomically.

5. **Pros/cons of shadow paging**
   - Pros: simple, no undo log. Cons: data fragmentation, hard with concurrency, garbage collection of old pages.
   - Misconception: *"Shadow paging is always better because it needs no log."* Correction: it scales poorly under high concurrency — most real DBMSs use log-based recovery.

**Check for understanding:**
- MCQ1: Immediate update recovery requires → both UNDO and REDO ✅
- MCQ2: In shadow paging, committing a transaction means → switching the current page-table pointer to the new page table ✅
- Discussion: "Compare 'edit the original directly' (immediate update) vs 'edit a photocopy' (shadow paging) for a bank's nightly batch — which would you trust more and why?"

**Real-life application:** the UNDO/REDO model is what production engines (PostgreSQL, MySQL/InnoDB behind Nepali apps) actually implement; shadow-paging ideas live on in copy-on-write file systems and snapshots.

**Visual cues:** UNDO/REDO recovery flow on a log timeline; shadow-paging diagram (current vs shadow page table, pointer flip); recovery-techniques comparison table (deferred / immediate / shadow).

**Summary:** (1) immediate update writes early → needs UNDO and REDO; (2) shadow paging swaps page tables atomically, no undo log; (3) each has clear trade-offs. **Next:** when the *whole* disk or data-center is gone — backup and catastrophic recovery (closes the unit).

---

## S44 — Database Backup & Recovery from Catastrophic Failures (closes Unit 6)

**Hook:** "An earthquake floods a Kathmandu data center and the whole disk array is destroyed. The log is gone too. Now what saves your eSewa balance?" → backups and off-site recovery.

**Concepts & how each will be filled:**

1. **Catastrophic vs non-catastrophic failure**
   - Definition: non-catastrophic = crash but disk intact (log-based recovery, S42–S43); catastrophic = media/disk/site destroyed.
   - Local example: 2015 earthquake / fire / flood scenario for a Nepali bank data center; ransomware wiping disks.
   - Misconception: *"The transaction log alone can recover anything."* Correction: if the disk holding the log is destroyed, you need a separate backup.

2. **Database backup**
   - Definition: periodic full copy of the DB (and log) to separate/off-site stable storage (tape, separate disk, cloud).
   - Types: full vs incremental/differential backup.
   - Theory: backup + archived log lets you restore the last backup, then REDO from the archived log to the failure point.

3. **Backup strategy & best practices**
   - The 3-2-1 rule: 3 copies, 2 media, 1 off-site.
   - Local example: a Nepali bank keeping a daily backup off-site (e.g., a second city / cloud region) per NRB IT guidelines.
   - Fun element: analogy — keeping a copy of your important documents at a relative's house in another town in case yours burns down.

4. **Recovery from catastrophic failure (procedure)**
   - Restore the most recent full backup → apply incremental backups → REDO committed transactions from the archived/backup log.
   - Mini case: data center down at 3 PM; last full backup at midnight + archived logs → reconstruct up to 3 PM.

5. **Disaster recovery, RTO/RPO & high availability (closing synthesis)**
   - Definitions: RPO (how much data you can afford to lose) vs RTO (how fast you must be back); replication/standby servers.
   - Misconception: *"Backups = high availability."* Correction: backups protect *data*; HA/replication protects *uptime* — different goals.

6. **Unit 6 synthesis**
   - One slide tying it together on the eSewa transfer: transaction → ACID → serializable schedule → 2PL/timestamp concurrency → log-based recovery → backup against catastrophe.

**Check for understanding:**
- MCQ1: Recovery from a destroyed disk relies primarily on → an off-site/separate backup (plus archived log) ✅
- MCQ2: "How much data loss is acceptable" is measured by → RPO ✅
- Discussion: "Design a one-paragraph backup plan for a small Nepali fintech startup using the 3-2-1 rule — where do the copies live?"

**Real-life application:** every regulated financial institution in Nepal (banks, wallet providers under NRB) must have a documented disaster-recovery/backup plan — this is a compliance and employability essential.

**Visual cues:** full-vs-incremental backup timeline; 3-2-1 backup diagram; RPO/RTO timeline on a failure axis; the Unit 6 synthesis 'one transfer, all concepts' slide.

**Summary:** (1) catastrophic failure destroys the disk/log → only backups save you; (2) restore backup + REDO archived log to the failure point; (3) plan with 3-2-1, RPO/RTO, and replication. **End of Unit 6.** Next unit: Advanced Topics (performance tuning, security, distributed databases, data warehousing, big data, NoSQL).

---

## END-OF-UNIT 6 QUIZ (consolidated · all sessions S37–S44)

> Suggested use: 20-minute review quiz. Correct answers marked ✅. (Per-session 2-MCQ checks above are retained for in-class use.)

### Part A — Multiple choice (10)
1. A logical unit of database work that is all-or-nothing is a → (a) schema (b) **transaction ✅** (c) cursor (d) view.
2. A transaction that finished all operations but is not yet permanent is → (a) **partially committed ✅** (b) aborted (c) failed (d) active-only.
3. "Once committed, it survives a crash" is → (a) atomicity (b) isolation (c) **durability ✅** (d) consistency.
4. Concurrent transactions not interfering with each other is → (a) **isolation ✅** (b) durability (c) consistency (d) atomicity.
5. A concurrent schedule is conflict-serializable iff its precedence graph → (a) has a cycle (b) **has no cycle ✅** (c) is empty (d) has one node.
6. In Two-Phase Locking, releasing the first lock begins the → (a) growing (b) **shrinking ✅** (c) commit (d) abort phase.
7. Deadlock is detected by a cycle in the → (a) precedence graph (b) **wait-for graph ✅** (c) B-tree (d) page table.
8. In basic timestamp ordering, an operation violating timestamp order is → (a) queued (b) ignored always (c) **aborted and restarted ✅** (d) committed early.
9. Deferred-update (NO-UNDO/REDO) recovery requires → (a) undo only (b) **redo only ✅** (c) both undo and redo (d) neither.
10. Recovery from a physically destroyed disk depends primarily on → (a) the buffer cache (b) **an off-site backup + archived log ✅** (c) the precedence graph (d) shared locks.

### Part B — Short answer (5)
11. List the four ACID properties and give the one-word job of each.
12. Draw the transaction state-transition diagram and label all states.
13. Given two transactions on one wallet, show one schedule that causes a *lost update*.
14. State the rule that makes a schedule conflict-serializable using a precedence graph.
15. Explain why immediate-update recovery needs UNDO but deferred-update does not.

### Part C — Long answer / applied (3)
16. Using the eSewa "Rita sends Rs. 500 to Hari" transfer, trace it through atomicity, isolation, and durability, and describe what the log records at each step.
17. Compare Two-Phase Locking and Timestamp Ordering: mechanism, what each guarantees, and the failure mode each suffers (deadlock vs starvation). Give a scenario favouring each.
18. Compare deferred update, immediate update, and shadow paging for recovery (mechanism, undo/redo needs, pros/cons), then outline a 3-2-1 backup + disaster-recovery plan for a Nepali fintech facing catastrophic failure.

---

## Open questions before I generate Unit 6 material
1. Keep the single **eSewa "Rita → Hari Rs. 500"** running example throughout, or split between eSewa and a traditional bank transfer?
2. For S39, is a **2-transaction precedence-graph** worked example enough, or do you want a 3-transaction one for extra rigor?
3. Quiz: is the **per-session 2-MCQ + 1-discussion AND a consolidated end-of-unit quiz** the right balance, or trim one?
4. Depth of S40 deadlock — cover **wait-die/wound-wait prevention** in detail, or keep it at detection + brief mention (current plan)?
5. Keep **RPO/RTO + high-availability** in S44, or is that beyond the BIM 4th-sem scope and should be cut to a single mention?
