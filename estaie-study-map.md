# estaie FDE (Integrations): Study Map

Journey file. It obeys `AGENTS.md` (teaching method, casebook research, honesty rules).
This file says WHAT to teach and what evidence exists. Last updated: 2026-09-30.

## 0. How the agent uses this file

1. If `MISSION.md` is missing, copy section 1 into it (confirm with the user first).
2. Teach the branches in section 6 in priority order. One branch per session, at most 2 new concepts.
3. Before each lesson, run the casebook protocol in `AGENTS.md` section 5. The seeds in section 7 are starting points. They do not replace research.
4. Follow the evidence rules in section 4. Never claim beyond them.
5. Update the progress table (section 11) only when a learning record exists. In chat mode, print the table.

## 1. Mission

**Why.** Pass the estaie Forward Deployed Engineer (Integrations) screening and be able to defend technical
follow-ups truthfully, using my own git repositories as evidence. Longer term, become a senior production and integration engineer.

**Success looks like**
- Explain webhook verification, idempotency, retries, and sync/reconciliation in 90 seconds each, in English.
- Tell two or three project stories (what I built, how it fails, what I would change) that survive "why?" and "what if it crashes here?" follow-ups.
- Say honestly what I have not done (NestJS, Next.js, queues) and what I understand about it.

**Constraints**
- HR screening call is not booked yet. The recruiter said shortlisting is closing soon.
- Preparation time is short, so depth follows section 5.

**Out of scope**
- Model training, ML math, Kafka/OpenSearch/Kubernetes depth, Go, tool tutorials with no real problem behind them.

## 2. Interview status

- Applied through LinkedIn. Job: https://www.linkedin.com/jobs/view/4467364804/
- Invited to a 10-15 minute AI screening by Osama Shawky (Founder/CEO): qualifications only, not personality
  or culture fit; same role-specific criteria for every candidate; he reviews answers personally;
  practice allowed; complete within 5 days; shortlisting closing soon.
- The user hit a technical conflict joining. Osama replied that the user is moving forward and should schedule a screening meeting with HR through a calendar link.
- CONFIRMED stage: HR screening, not yet held. "Qualifications only" was stated for the AI interview, not confirmed for the HR call.
- UNKNOWN: whether the AI interview is still required; HR call length and format; any technical, coding, system-design, or final round; location or remote terms; contract type; compensation.

## 3. Role model

estaie is an AI-native extended-stay platform (15-365 days) connecting hotels, holiday homes, channel managers,
payment providers, and other travel systems. The role owns solution design, development, integration,
deployment, and production.

- Responsibilities: integrations with channel managers, PMSs, booking platforms, payment providers; production apps in Next.js, React, TypeScript, NestJS, Node.js, PostgreSQL, Redis; API integrations (authentication, webhooks, data transformation, retries, rate limiting, idempotency, error handling); partner-facing troubleshooting; sync, transformation, reconciliation; queue and event-driven workflows; internal tools; AI/LLM automation; deploy, monitor, debug; architecture, tests, reviews.
- Requirements: 5+ years; TypeScript, React/Next.js, Node/NestJS; REST, webhooks, auth, data transformation; PostgreSQL plus Redis/queues; transactions, concurrency, idempotency, retries, fault tolerance; Docker and cloud; debugging; partner-facing work; independent ownership.
- Nice to have: Kafka/Redpanda, OpenSearch, BullMQ, Turborepo; hospitality, travel, fintech, e-commerce; payments, reservations, inventory distribution; LLMs, agents, vector search; GCP, Cloud Run, Kubernetes.
- POSSIBLE only (hints from a different estaie integrations posting, not this JD): Pub/Sub, Redis distributed locks, Go, 100+ partner integrations. Teach these as concepts at low depth; never assume they are asked.

## 4. Evidence rules

No resume file was found in the project files. Years of experience, employers, and dates are UNKNOWN.
Do not state them.
Project evidence below comes from the project docs read on 2026-09-30. "Verify in code" means confirm it in
the source before saying it aloud.

**Opran** (Cloudflare Workers proxy, billing, credential pool)
- Docs show: billing webhooks for Polar and CREEM verified with HMAC-SHA256 (`crypto.subtle.verify`); missing
  signature rejected with 403; duplicate events answered 200; a `webhook_dedup` table; D1 plus KV updates;
  refresh-token lifecycle with `INVALID_PERM` recovery; a bounded keep-alive scheduler (ADR-017: batches of
  at most 10, KV cursor, backoff from 4h to 48h); a July 2026 pool-exhaustion incident.
- Verify in code: the dedup key and the order (record first or mutate first); the status code for an INVALID
  signature (the architecture diagram says 500, the runbook says 403); what happens if D1 succeeds and KV
  fails; where the checkout rate limit lives and how it works.
- Caution: the docs mention capturing upstream tokens with an instrumentation toolchain. If an interviewer
  asks about authorization or terms of service, answer honestly. Lead with the billing and scheduler design.

**Eagles** (Twenty-based CRM: Meta Lead Ads and WhatsApp ingestion, round-robin assignment, SLA)
- Docs show: `meta-lead-ingestion` among the deployed ingestion sites; unique indexes on
  `(sourceId, externalSourceId)` and `(channel, externalMessageId)`; E.164 phone normalization; round-robin by
  open load (changed 2026-08-08; the older daily-count rule in the PRD is superseded); a `lead.created` trigger
  plus cron escalation; a 30-minute acknowledgement SLA; a double-assignment race (43 duplicate rows) fixed on
  2026-08-14 by keeping a single assignment path; Docker Compose on a VPS, Cloudflare Tunnel, pgBackRest.
- ESC-006 (`data-models.md`): booking overlap prevention is an application-level check only, with no database
  `EXCLUDE` constraint and no enforced `version` check. This is a known gap. Never say Eagles "prevents double
  booking". Say what the gap is and what the fix would be.
- Also in the docs: availability derived from bookings (FR-33 to FR-35); a compensating rollback of package hours.
- Verify in code: the Meta signature check (the PRD addendum lists it as a plan item); which path now assigns
  leads; what Twenty provides versus what I wrote.

**AegisFlow** (Cloudflare Workers consular-appointment automation)
- Docs show: a Durable Object job lock (90-second lease with heartbeat, sealed on confirmation); AES-256-GCM
  with a distinct IV per field; retry policies in `booking-flow.ts`; Workers AI Whisper with a fallback tier.
- Caution: it automates booking on a government portal and solves CAPTCHAs. Use it only as secondary evidence
  for lock and encryption design, and answer honestly if asked what it does.

**skills-bank** (Rust CLI)
- Docs show: hybrid keyword plus LLM classification, batching, concurrency limits, retries with backoff,
  provider failover, tolerant JSON parsing, deduplication. Supporting evidence for AI/LLM integration only.

**No evidence in the files** (do not claim): NestJS, Next.js, Redis/BullMQ, Kafka, GCP/Cloud Run, PMS or
channel-manager integrations, hospitality domain work, partner-facing troubleshooting, production traffic
figures, team leadership.

## 5. Depth model and targets

Depth: 0 recognise; 1 mental model; 2 practical; 3 engineering (implement, debug, test, failure cases);
4 system design (concurrency, consistency, security, trade-offs); 5 internals and edge cases.
Stage-aware target for the HR screening: Depth 2 spoken fluency across all P0 topics, plus 2-3 project stories
defended at Depth 3-4. Go deeper only when the user asks or a technical round is confirmed.
Priority: P0 immediate, P1 important, P2 secondary, P3 nice to have. [T] is the target depth.

## 6. Study map (dependency order; one branch per session)

Seeds [S#] refer to section 7. Flags: VERIFY = check in code first. NO-EVIDENCE = teach the concept and
prepare an honest phrasing.

```
LEVEL 0: Integration mental model                                   P0 [T=2]
|- L0.1 Delivery semantics: at-least-once, duplicates, reordering, ambiguous failure    [S1,S2]
|- L0.2 HTTP status codes as retry signals; timeouts. A bad signature must not cause retries.
|        VERIFY Opran invalid-signature status (500 vs 403)                              [S4]
|- L0.3 Push vs pull: webhooks, polling, scheduled sync; why reconciliation exists       [S4,S11]
|- L0.4 Hospitality map: PMS, channel manager, OTA, ARI (availability, rates, inventory)
|        P1 [T=1-2], NO-EVIDENCE                                                        [S11]
v
LEVEL 1: Contracts                                                  P0 [T=3]
|- L1.1 Webhook receiver: raw body, HMAC verification, constant-time compare, replay window
|        VERIFY Opran billing; Eagles Meta signature check (plan only)                   [S4,S13]
|- L1.2 Acknowledge fast, process asynchronously, which responses make senders retry      [S4,S12]
|- L1.3 Partner auth: API keys, OAuth2 refresh, token expiry, secret handling
|        Evidence: Opran refresh flow and INVALID_PERM recovery
|- L1.4 Mapping and validation: canonical model, schema validation, unknown and blank fields,
|        API versioning. Evidence: Eagles E.164 normalization                             [S5]
|- L1.5 Rate limits: 429 and Retry-After, token bucket, client-side throttling            [S2]
v
LEVEL 2: Reliability                                                P0 [T=4]
|- L2.1 Idempotency keys and deduplication (unique constraint, INSERT ... ON CONFLICT)    [S1,S3]
|        Evidence: Opran webhook_dedup; Eagles unique indexes
|- L2.2 The crash window: dedup record versus side effect; receipt and durable enqueue in
|        one transaction. VERIFY Opran ordering                                           [S3,S12]
|- L2.3 Retries: exponential backoff with jitter, transient vs permanent errors,
|        retry budgets, retry storms and herd effects                                     [S2,S5,S6]
|        Evidence: skills-bank retries; Opran 4h-48h backoff
|- L2.4 Timeouts, circuit breakers, cascading failure, dead-letter handling  [T=2-3]     [S2,S6]
|- L2.5 Dual writes, compensation, transactional outbox
|        Evidence: Eagles package-hours rollback; Opran D1+KV dual write (VERIFY)        [S9]
v
LEVEL 3: PostgreSQL correctness                                     P0 [T=3-4]
|- L3.1 Transactions, isolation levels, and the anomalies each allows
|- L3.2 Check-then-act races and fixes: unique or partial index, SELECT FOR UPDATE,
|        SKIP LOCKED, advisory lock, version column, Serializable plus retry
|        Evidence: Eagles double-assignment race (2026-08-14)
|- L3.3 Overlap prevention: EXCLUDE USING gist on a time range (btree_gist); derived vs
|        stored availability. Evidence: Eagles ESC-006 gap (state the gap and the fix)    [S10]
|- L3.4 Locks, leases, fencing tokens; Postgres vs Redis vs Durable Object  P1 [T=2-3]   [S7,S8]
|        Evidence: AegisFlow job lock (secondary)
v
LEVEL 4: Async and scheduled work                                   P1 [T=3]
|- L4.1 Queue semantics (BullMQ-style): attempts, backoff, delayed jobs, stalled jobs,
|        failed set, idempotent consumers. NO-EVIDENCE: build a tiny worker
|- L4.2 Ordering and per-key concurrency; scheduler versus queue; cursor checkpoints      [S6]
|        Evidence: Opran ADR-017; Eagles cron (SRE book ch. 24 on cron)
|- L4.3 Pub/Sub and Kafka concepts only                              P3 [T=1]
v
LEVEL 5: Sync, reconciliation, operations                           P0/P1 [T=3-4]
|- L5.1 Full vs delta sync, watermarks, replay. Evidence: Eagles backfill / daily-sync    [S11]
|- L5.2 Reconciliation loop: compare, classify drift, repair, report, source of truth  P0
|- L5.3 Observability for integrations: correlation IDs, structured logs, alerts, replay tools
|        Evidence: audit_logs, CRITICAL_SRE_ALERT
|- L5.4 Partner debugging playbook and partner communication            P0 for HR [T=2-3]
|        Timeline: received, verified, deduped, processed, persisted, acknowledged.
|        NO-EVIDENCE: prepare one honest story
|- L5.5 Integration security: secrets, HMAC, field-level AES-256-GCM, RBAC, PII   [T=2-3]
v
LEVEL 6: Stack and domain                                           P1/P2 [T=2]
|  Concept first; build a tool only when a real problem needs it (AGENTS.md section 8).
|- L6.1 NestJS concepts: modules, DI, guards, pipes, interceptors, DTO validation.
|        Real problem to use: structure one webhook module. NO-EVIDENCE
|- L6.2 Next.js/React concepts: server vs client components, route handlers for internal
|        tools. NO-EVIDENCE
|- L6.3 Docker and cloud deploy: Compose, Workers, stateless containers, Cloud Run concepts
|        Evidence: Eagles Docker Compose, Cloudflare Tunnel, pgBackRest
|- L6.4 LLM calls as a production dependency: structured output, schema validation, fallback,
|        cost and latency. Evidence: skills-bank; AegisFlow Whisper fallback
|- L6.5 Go, gRPC, Vertex AI                                          P3, sibling-posting hint only
```

## 7. Seed sources (Tier 1 unless noted; URLs seen in search results on 2026-09-30; re-open before citing)

- S1 Stripe, "Designing robust and predictable APIs with idempotency": https://stripe.com/blog/idempotency
  Idempotency keys, retrying ambiguous failures, backoff with jitter.
- S2 Amazon Builders' Library, "Timeouts, retries, and backoff with jitter":
  https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
  Why retries amplify overload; choosing timeouts; jitter.
- S3 Airbnb Engineering, "Avoiding Double Payments in a Distributed Payments System":
  https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb
  Seen in a reference list, not opened; fetch it before teaching.
- S4 GitHub Docs, "Best practices for using webhooks":
  https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks
  Secrets, responding within the time limit, queueing, event-type checks.
- S5 Google Cloud incident report, 12 June 2025 (Service Control):
  https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW
  Blank policy fields hit an unprotected code path; recovery herd effect on Spanner because the restarting
  tasks lacked randomized exponential backoff. Fits L1.4 and L2.3.
- S6 Google SRE book, ch. 22 "Addressing Cascading Failures": https://sre.google/sre-book/addressing-cascading-failures/
  Table of contents (ch. 24 Cron, ch. 26 Data Integrity): https://sre.google/sre-book/table-of-contents/
- S7 Martin Kleppmann, "How to do distributed locking":
  https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
  Read together with S8.
- S8 antirez, reply on Redlock: https://www.antirez.com/news/101
- S9 Transactional outbox: https://microservices.io/patterns/data/transactional-outbox.html
  Also Designing Data-Intensive Applications, ch. 11 on dual writes. Not opened this session.
- S10 Overlap constraints (Tier 2 and docs): Supabase, "Simplifying Time-Based Queries with Range Columns"
  https://supabase.com/blog/range-columns ; Django docs on PostgreSQL ExclusionConstraint (notes btree_gist)
  https://docs.djangoproject.com/en/dev/ref/contrib/postgres/constraints ;
  PostgreSQL manual (range types, CREATE TABLE EXCLUDE, Concurrency Control): https://www.postgresql.org/docs/current/
- S11 RateGain developer docs, PMS to channel manager ARI push (vendor docs, Tier 2):
  https://developer.rategain.com/our-products/channel-manager/rg-bridge-supply-push/interface-specifications-availability-and-rates-notification-service
- S12 Receipt-then-enqueue crash window (Tier 2, secondary blog, 2026-09-13):
  https://oneuptime.com/blog/post/2026-09-13-stripe-webhook-event-id-atomic-enqueue/view
  Read it, then confirm the claims against the provider's own docs.
- S13 Stripe webhook guide (official): docs.stripe.com/webhooks. Not opened this session; fetch it first.

Gaps to research: a primary-source incident for webhook duplicate delivery; a primary-source case on channel
manager overbooking or sync drift; a reconciliation case study from a payments company.

## 8. Project defense targets

Whiteboard sequences to be able to draw: (A) Opran webhook, (B) Eagles ingestion to assignment, before and
after the race fix, (C) the Opran keep-alive loop.

- **A. Opran billing webhook (P0).** POST, verify HMAC, parse, dedup, switch on event type, update D1, update
  KV, suspend or reactivate keys. Must answer from code: dedup key and write order; status codes per failure;
  D1 succeeds and KV fails; `scheduled_cancel` versus `canceled` versus `expired`.
- **B. Eagles ingestion and assignment (P0).** Normalize, dedupe by unique index, create lead, trigger
  assignment by open load, SLA timer, cron escalation. Must answer: why two paths raced under bursts, why
  removing one path fixed it, what a lock or unique constraint would have done instead.
- **C. Eagles ESC-006 gap (P0).** State that overlap prevention is a check-then-act in application code. Explain
  the race, then the fix (an `EXCLUDE` constraint on a time range, or `SELECT FOR UPDATE`, or a version check),
  and why it is not built yet.
- **D. Opran keep-alive incident (P1).** Bounded batches, KV cursor, backoff, the July 2026 pool exhaustion,
  the fix, and what detection was missing.
- **E. AegisFlow lock and encryption (secondary). F. skills-bank LLM pipeline (secondary).**

## 9. Question bank (source: JD, stage, project evidence)

Behavioral: (1) Walk me through an integration you built end to end. (2) A hard production bug across systems.
(3) Troubleshooting with a partner (NO-EVIDENCE: use a real story or describe the method).
Technical: (4) How do you receive a webhook securely? (5) Crash after the side effect but before recording the
event. (6) Two requests take the last room at once. (7) Unique index versus application check.
Integration: (8) A partner returns 429s; design the client. (9) Design a sync with a channel manager (POSSIBLE).
Debugging and reliability: (10) "Bookings are missing": walk the timeline. (11) At-least-once queues and
duplicate effects. Security and AI: (12) Partner credentials and failed refresh. (13) An LLM inside an
integration workflow. Project: (14) Whiteboard the Opran webhook; D1 succeeds, KV fails.

## 10. Gaps (highest risk first)

| Gap | Type | Target | Closes with |
|---|---|---|---|
| Idempotency ordering and atomicity | Conceptual + project | 4 | L2.1, L2.2 |
| Postgres concurrency toolbox | Conceptual | 3-4 | L3.1-L3.3 |
| Reconciliation design | Architecture | 3-4 | L5.1, L5.2 |
| Queues (BullMQ/Redis) | Implementation | 3 | L4.1 |
| Partner-facing communication | Communication | 2-3 | L5.4 |
| Multi-store consistency (D1 + KV) | Architecture | 3 | L2.5 |
| NestJS, Next.js | Implementation | 2 | L6.1, L6.2 |
| Hospitality vocabulary | Domain | 1-2 | L0.4 |
| Understanding AI-assisted code | Project-specific | n/a | Section 8 checks |

Honest phrasing pattern for NO-EVIDENCE topics: "I have not used X in production. The closest thing I have built
is Y. I understand the model as Z."

## 11. Progress (update only with a learning record)

```
[ ] L0.1  [ ] L0.2  [ ] L0.3  [ ] L0.4
[ ] L1.1  [ ] L1.2  [ ] L1.3  [ ] L1.4  [ ] L1.5
[ ] L2.1  [ ] L2.2  [ ] L2.3  [ ] L2.4  [ ] L2.5
[ ] L3.1  [ ] L3.2  [ ] L3.3  [ ] L3.4
[ ] L4.1  [ ] L4.2  [ ] L4.3
[ ] L5.1  [ ] L5.2  [ ] L5.3  [ ] L5.4  [ ] L5.5
[ ] L6.1  [ ] L6.2  [ ] L6.3  [ ] L6.4  [ ] L6.5
```

Suggested order for the HR screening: L0.1-L0.3, L1.1-L1.2, L2.1-L2.3, L3.2-L3.3, L5.2, L5.4, then the rest.

## 12. Open items

- Resume not found in the project files; ask the user to add it.
- Confirm with HR whether the AI interview is still required, and ask about location, contract, compensation.
- Fetch the sources marked "not opened" before teaching from them.
