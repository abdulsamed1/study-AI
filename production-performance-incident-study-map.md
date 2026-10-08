# Production Performance & Traffic-Spike Engineering — Study Map

> **Purpose:** Build the ability to diagnose, explain, mitigate, and permanently improve production systems when latency rises, throughput collapses, resources saturate, dependencies slow down, or traffic changes abruptly.

> **Scope:** This is a focused journey for **performance incidents, overload, capacity limits, bottleneck analysis, resilience under pressure, and production debugging**.

> **Core principle:** Do not memorize a fixed recipe such as `Load Balancer → Scale → Redis → Queue`. Diagnose the mechanism first. The intervention depends on the actual constraint, workload, correctness requirements, and failure mode.

---

## How to use this map (sessions, tools, evidence)

*Revised 2026-10-09. Teaching rules live in `AGENTS.md`; procedures in `TEACHING-PROTOCOLS.md`. This file says WHAT to learn.*

- **One session = one branch.** Pick one branch (for example `PERF-L2-C`), introduce at most two new concepts, teach through a real incident, give exactly one practice task, and write one learning record when the capability is demonstrated.
- **Teach before you quiz.** A level's "Learn" section is taught as a lesson first. The Practice task and exit criteria come after.
- **Branch IDs** for Progress Records: `PERF-L0` ... `PERF-L9`, plus the branch letter where one exists (`PERF-L2-C`).
- **Evidence rule.** Tick a Mastery box only when a learning record, a lab result, or a project file proves it. Write the record number next to the box (for example `(LR-0007)`). Reading a chapter is not evidence.
- **Modes.** Workspace (Claude Code / OpenCode): write lessons, records, casebook entries. ChatGPT Project: end with a Progress Record you save. NotebookLM: sources only; name the source to add when a case is missing.

| Level | Casebook concepts to research (`casebook/<slug>.md`) | Lab |
|---|---|---|
| L0 | `symptom-vs-mechanism` | none (written practice) |
| L1 | `observability-evidence` | none |
| L2 | `cpu-vs-queueing`, `pool-exhaustion` | 1, 3 |
| L3 | `n-plus-one`, `database-bottleneck` | 2 |
| L4 | `slow-dependency`, `retry-storm` | 4 |
| L5 | `load-shedding-vs-rate-limiting`, `queue-backlog` | 5 |
| L6 | `bottleneck-migration`, `cache-as-dependency` | 6, 7 |
| L7 | `profiling-and-load-testing` | all |
| L8 | full scenarios A-G | none (reasoning) |
| L9 | `llm-system-performance` | 8, 9 |

---

## Mission

### Why

Become able to answer production scenarios such as:

- "Traffic increased 20× and the API started timing out. What do you do?"
- "CPU is 95%, but adding servers did not solve the incident. Why?"
- "Application instances scaled from 5 to 50, but database CPU became saturated. What changed?"
- "Latency increased while CPU and memory stayed normal. Where do you investigate?"
- "A downstream payment provider became slow and took the whole request path with it. How do you contain the failure?"
- "A short-lived burst overloaded the service, but the work did not need to finish synchronously. What should change?"

### Success looks like

I can take a production symptom and move through:

`Symptom → Evidence → Hypothesis → Isolation → Targeted intervention → Validation → Root cause → Prevention`

without jumping directly to a technology choice.

I can also explain why a tempting intervention is **wrong for the diagnosed mechanism**.

### Constraints

- Learn the **decision-making skill**, not a catalog of architecture components.
- Use real production cases and controlled experiments.
- Prefer profiling, measurements, traces, query plans, load tests, and incident evidence over intuition.
- Treat scalability and performance as related but distinct problems.
- Treat a high CPU/memory/error metric as a **signal to investigate**, not automatically as the root cause.
- Do not claim production experience with a tool merely because it was studied.

### Out of scope

Do not turn this journey into a complete course on:

- microservices architecture;
- distributed consensus;
- leader election;
- sharding internals;
- Kubernetes internals;
- Kafka internals;
- service-mesh internals;
- cloud-provider certification material;
- generic design-pattern memorization;
- framework tutorials without a performance/production scenario.

---

# Mental Model

There are two different questions that are often mixed together.

### Performance

**How efficiently does the current system perform work?**

Examples:

- too much CPU work per request;
- excessive allocations or blocking;
- unnecessary database round trips;
- inefficient queries;
- contention;
- slow network calls;
- long queues caused by limited resources.

### Scalability / Capacity

**How much load can the system handle while continuing to meet its required behavior?**

Foundations of Scalable Systems frames scalability around increasing capacity in some operational dimension and identifies two broad ways to increase capacity: **replication** and **optimization**. It also explicitly warns that replicating resources that are not the real bottleneck adds cost without giving a scalability benefit.

**Study implication:** optimization can increase capacity; replication can increase capacity; neither should be selected before the constraint is understood.

> Source: *Foundations of Scalable Systems*, Ian Gorton, Ch. 1, especially the sections on scalability, replication, optimization, performance, and the relationship between bottlenecks and added capacity.

---

# The Learning Architecture

The levels below are a **learning progression**, not an incident-response algorithm.

```text
L0  Diagnostic mindset
 ↓
L1  Measure and localize
 ↓
L2  Resource and execution bottlenecks
 ↓
L3  Database/query-path bottlenecks
 ↓
L4  Dependency and failure propagation
 ↓
L5  Overload control and work shaping
 ↓
L6  Capacity and scaling decisions
 ↓
L7  Controlled validation and performance experiments
 ↓
L8  Full production scenarios + interview reasoning
 ↓
L9  Frontier-AI bridge: performance and reliability of LLM-backed systems
```

At any real incident, you may jump between branches as evidence changes. The point of the map is to make each branch available when the evidence requires it.

---

# L0 — Diagnostic Mindset: Stop Treating Symptoms as Solutions

## Target

Build the first mental habit: **a production symptom is not yet a diagnosis**.

## Learn

### 1. Symptom vs. mechanism vs. root cause

A symptom is what the system exposes:

- high latency;
- high CPU;
- high memory;
- rising error rate;
- exhausted connections;
- growing queue depth;
- timeouts;
- throughput collapse.

The mechanism describes what is physically happening:

- a query is slow;
- requests are blocked on a pool;
- a downstream call is waiting;
- a hot key concentrates load;
- work is repeated unnecessarily;
- the service has exceeded a local resource limit.

The root cause is the underlying condition that explains why the mechanism appeared.

### 2. Performance vs. capacity

Learn to separate:

- **inefficiency:** the system does too much work for the same result;
- **capacity:** the system has reached a real resource or architectural limit under the required workload.

### 3. Workload matters

"20× traffic" is incomplete information.

The relevant load characteristics can include:

- request rate;
- concurrency;
- request mix;
- read/write ratio;
- data size;
- hot-key distribution;
- expensive versus cheap endpoints;
- synchronous versus asynchronous work;
- dependency behavior under load.

The books explicitly describe load in terms of resources consumed and note that performance and capacity depend on the workload and architecture.

## Practice

Given:

> Traffic increases 10×. CPU reaches 95%. Latency increases 4×. Database CPU is 45%.

Before proposing a fix, write **five measurements or traces** you would inspect to distinguish between:

- legitimate compute saturation;
- inefficient application work;
- blocking or queueing;
- downstream latency;
- another bottleneck.

## Exit criteria

I can explain why "CPU is 95% → add servers" is an incomplete diagnosis.

I can state what evidence would make scaling appropriate and what evidence would point to optimization instead.

## Source path

- *Foundations of Scalable Systems*, Ch. 1 — scalability, replication, optimization, performance, bottlenecks.
- *Understanding Distributed Systems*, 2nd ed., Roberto Vitillo, Ch. 1.3 — performance, throughput, response time, capacity.

---

# L1 — Measure and Localize: Build the Evidence Path

## Target

Turn an incident into a measurable search problem.

## Learn

### 1. Request-level signals

Know how to reason about:

- throughput / requests per second;
- response-time distributions;
- latency percentiles such as P95 and P99;
- error rate;
- timeouts;
- concurrency;
- queue depth where applicable.

Vitillo emphasizes throughput and response time as primary performance measures and explains why percentiles provide a better view of user experience than an average alone.

### 2. Resource and dependency signals

At minimum, be able to correlate application behavior with:

- CPU;
- memory;
- resource-pool utilization;
- database response time;
- database connection usage;
- dependency availability and latency;
- queue depth;
- cache hit/miss behavior when caching is involved.

### 3. Metrics → logs → traces

Learn the distinction:

- **Metrics** help detect and trend system behavior.
- **Logs** provide detailed event context.
- **Traces** connect latency and behavior across request boundaries.

Vitillo describes monitoring as focused on detecting failures and system health, while observability adds the ability to understand and debug system behavior by providing granular context.

### 4. Hypothesis-driven investigation

Do not inspect every signal equally.

Form a hypothesis:

> "The latency increase is caused by database wait time."

Then choose telemetry that can confirm or reject it:

- request trace;
- database timing;
- query duration;
- connection-pool wait;
- database CPU/locks;
- deployment timeline.

## Practice

Scenario:

> P99 latency doubled. CPU is 55%. Memory is stable. Error rate is unchanged. One endpoint is affected, and the endpoint spends most of its time waiting on another service.

Construct the evidence chain you would collect before changing architecture.

## Exit criteria

I can move from a dashboard symptom to a bounded hypothesis and name the telemetry that would falsify it.

## Source path

- *Understanding Distributed Systems*, Ch. 31 — Monitoring; Ch. 32 — Observability.
- *Designing Distributed Systems*, 2nd ed., Brendan Burns, Ch. 14 — Monitoring and Observability Patterns: metrics, request monitoring, alerting, tracing.
- *Foundations of Scalable Systems*, Ch. 5 material on application-service metrics, queues, thread pools, database connection pools, and data-driven performance experiments.

---

# L2 — Resource and Execution Bottlenecks

## Target

Learn to identify **where request processing is actually consuming capacity**.

## Branch A — CPU-bound work

Learn to distinguish:

- genuine compute saturation;
- expensive algorithmic work;
- excessive repeated work;
- unnecessary serialization/deserialization;
- high allocation pressure;
- CPU spent because another subsystem is causing pathological work.

The goal is not to memorize Big-O formulas. The goal is to connect workload growth to actual work performed and then verify the hypothesis with profiling or measurement.

## Branch B — Memory and garbage collection

Investigate:

- memory growth over time;
- allocation volume;
- cache growth without a bound;
- object retention;
- garbage-collection pressure where the runtime exposes it;
- whether memory pressure is causing secondary latency effects.

A memory graph that rises is evidence to investigate, not proof that more RAM is the correct remedy.

## Branch C — Threads, pools, blocking, and queues

This is critical for burst scenarios.

Understand the request-processing path:

```text
Incoming request
      ↓
accept / socket queue
      ↓
request worker / thread pool
      ↓
blocking operation or dependency
      ↓
resource pool
      ↓
response
```

The important lesson from *Foundations of Scalable Systems* is that response time can include both actual processing time and time spent waiting for scarce resources such as threads or database connections. Under heavy load, queues can grow, consume resources, and worsen latency further.

## Branch D — Concurrency and contention

Understand enough concurrency to diagnose:

- lock contention;
- blocked work;
- race conditions;
- serialized critical sections;
- contention increasing as concurrency rises.

Do not turn this branch into a general concurrency course. Learn only what is required to explain the observed production behavior.

## Practice

Scenario:

> Application latency rises sharply under load. CPU is only 60%. Thread count is high. Database CPU is 30%. Requests spend a large fraction of their time waiting for an application resource pool.

Explain why increasing the number of application instances might change the symptom without addressing the underlying bottleneck.

## Exit criteria

I can distinguish:

`CPU saturation` vs `queue/pool waiting` vs `blocking/contended work` vs `inefficient execution`.

I know what profiling or runtime telemetry I need before changing instance size.

## Source path

- *Foundations of Scalable Systems*, Ch. 5 — application service execution, thread pools, request queues, database connection pools, utilization, latency.
- *Foundations of Scalable Systems*, Part I — concurrency fundamentals only to the depth required to reason about contention and performance.

---

# L3 — Database and Query-Path Bottlenecks

## Target

Become strong at the most common class of performance failures in request/response systems: the application is waiting on the data path.

## Learn

### 1. Count database work before optimizing hardware

Be able to ask:

- How many queries does one request generate?
- How much data is read?
- How many round trips occur?
- How long does each query take?
- Are queries repeated unnecessarily?
- Is the database waiting on CPU, I/O, locks, connections, or something else?

### 2. N+1 query pattern

Use this concrete mechanism from the supplied article material:

```text
Get N orders
   ↓
Loop through orders
   ↓
Query customer for each order
   ↓
N additional round trips
```

The important skill is not memorizing the label "N+1". It is recognizing **repeated remote work inside a loop** and checking whether a set-based operation, join, batching, or another access pattern is appropriate.

### 3. Indexing and query plans

Learn to investigate:

- whether a query can use an appropriate index;
- whether the database is scanning far more data than necessary;
- whether the query shape matches available indexes;
- whether the query plan explains the observed latency;
- whether an index improves the actual workload rather than merely existing.

Do not replace query-plan evidence with a simplistic statement such as "indexes make everything O(log N)". The study target is **real query behavior**.

### 4. Connection pools

A database connection is a bounded resource.

Understand:

```text
Application concurrency
        ↓
Connection pool
   ┌────┴────┐
available  waiting
              ↓
           timeout
```

A database can become the bottleneck even after the application tier is scaled out.

### 5. Locks and contention

Learn enough PostgreSQL/relational behavior to investigate:

- blocked queries;
- lock contention;
- long-running transactions;
- concurrency-sensitive code paths;
- connection exhaustion caused by waiting work.

### 6. Read replicas and caching — only after the read path is understood

Caching is an optimization, not a substitute for diagnosis.

Before using it, establish:

- the data is read-heavy enough;
- the same data is requested repeatedly;
- stale data is acceptable to the required degree;
- invalidation/expiration is manageable;
- a cache failure will not turn into an origin overload event.

Vitillo explicitly notes that caching introduces consistency and operational issues, and that a cache failure can expose the origin to a sudden surge of traffic. The origin therefore still needs protection.

## Practice

Scenario:

> API instances scale from 5 → 50. P95 latency improves briefly. Then database CPU reaches 100%, database connections are exhausted, and API latency becomes worse than before.

Diagnose the mechanism and list the **first database-side measurements** you would need before considering more API instances.

## Exit criteria

I can analyze a slow endpoint from:

`request → query count → query latency → query plan → connection wait → locks/contention → data-access redesign`

before suggesting database scaling.

## Source path

- Supplied article material — N+1 query and performance-engineering examples.
- *Foundations of Scalable Systems*, Ch. 1–2 — optimization, database bottlenecks, caching, and service/database interaction.
- *Understanding Distributed Systems*, Ch. 19 — Data Storage; Ch. 20 — Caching.

---

# L4 — Downstream Dependencies and Failure Propagation

## Target

Understand what happens when the system is healthy but one dependency becomes slow, unavailable, or partially degraded.

## Learn

### 1. Slow is a failure mode

A dependency does not have to return errors to damage the caller.

```text
Client
  ↓
API
  ↓
Slow dependency
  ↓
Requests remain open
  ↓
Concurrency accumulates
  ↓
Pools / threads / sockets become scarce
  ↓
Caller degrades
```

Vitillo describes slow network calls as difficult-to-detect failures because waiting consumes resources and can degrade the system.

### 2. Timeouts

Learn:

- why every potentially non-returning network operation needs bounded waiting;
- how timeout policy relates to downstream latency distribution;
- why timeout values must be observable;
- how timeout behavior prevents failure from propagating indefinitely.

### 3. Retries

Retries are not free capacity.

Learn:

- transient vs persistent failure;
- bounded retries;
- exponential backoff;
- jitter;
- retry storms;
- retry amplification across dependency chains;
- idempotency and correctness before retrying non-idempotent operations.

Vitillo explicitly shows that retries can worsen overload when performed immediately and that multiple retrying layers can amplify downstream load.

### 4. Circuit breaking / isolation

Study circuit breakers only to the depth required to answer:

> "How do I stop a failing dependency from taking down its callers?"

The important idea is **failure containment**, not memorizing a library API.

## Practice

Scenario:

> Your API calls a payment provider. The provider changes from 150 ms P95 to 5 seconds. The provider returns successful responses for most requests. The API has no application error spike yet, but its worker pool is filling and requests begin timing out.

Explain the mechanism and choose the first containment controls.

## Exit criteria

I can explain why:

`"dependency has no errors"` does **not** imply `"dependency is healthy"`.

I can reason about timeout, retry, and circuit-breaker trade-offs without treating them as a fixed trio that must always be installed.

## Source path

- *Understanding Distributed Systems*, Ch. 24 — Common Failure Causes.
- *Understanding Distributed Systems*, Ch. 27 — Downstream Resiliency: 27.1 Timeout; 27.2 Retry; retry backoff, jitter, and amplification; 27.3 Circuit breaker.

---

# L5 — Overload Control: Rate Limiting, Load Shedding, Load Leveling

## Target

Learn to control incoming work when demand exceeds what the system can safely process.

## Learn

### 1. Load shedding

Load shedding is a response to **local overload**.

Vitillo's model:

```text
Current local work
       ↓
Is the service over its safe capacity?
       ↓
Reject excess work early
       ↓
Protect work already in progress
```

It can be selective when requests have different priorities.

### 2. Rate limiting

Rate limiting is different from local load shedding.

It controls a quota based on a key such as:

- user;
- API key;
- tenant;
- IP address;
- another application-specific identity.

The study target is the **policy distinction**:

- load shedding → local protection from overload;
- rate limiting → traffic control according to a quota/global policy.

### 3. Load leveling with queues

When the client does not need immediate completion, asynchronous work can decouple arrival rate from processing capacity.

```text
Producer
   ↓
Queue
   ↓
Workers
   ↓
Database / external service
```

The queue absorbs short-lived bursts by allowing consumers to work at their own pace.

But learn the failure mode too:

- backlog growth;
- consumer lag;
- poison messages / repeated failures;
- downstream saturation;
- indefinite backlog if arrival rate remains above service rate.

### 4. Graceful degradation

Learn to protect the business-critical path by changing non-critical behavior under pressure.

Examples from the supplied material include:

- delaying background email/SMS work;
- reducing expensive reports;
- disabling non-critical recommendations.

The decision must be tied to business priority, not applied mechanically.

## Practice

Scenario:

> A flash sale creates a short burst of writes. Users only need confirmation that the event was accepted; persistence can complete asynchronously. The downstream database cannot safely process the burst synchronously.

Compare:

`load shedding` vs `rate limiting` vs `queue/load leveling`.

State which one addresses the user-visible requirement and what new failure mode the choice introduces.

## Exit criteria

I can distinguish the three controls and choose among them based on **work semantics and overload behavior**, not tool familiarity.

## Source path

- *Understanding Distributed Systems*, Ch. 28 — Upstream Resiliency: 28.1 Load Shedding; 28.2 Load Leveling; 28.3 Rate Limiting; 28.4 Constant Work.
- *Foundations of Scalable Systems*, Ch. 2 — increasing responsiveness with asynchronous queueing.
- *Designing Distributed Systems*, Ch. 11 — Work Queue Systems; Ch. 12 — Event-Driven Batch Processing.

---

# L6 — Capacity and Scaling Decisions

## Target

Learn when scaling is actually the correct intervention and how to scale without moving the bottleneck somewhere else.

## Learn

### 1. Scale up vs. scale out

Understand the trade-off:

- **Scale up:** increase resources available to the existing processing unit.
- **Scale out:** add processing replicas.

Scaling is appropriate when the workload is genuinely exceeding the capacity of the affected resource.

### 2. Bottleneck migration

A classic production sequence:

```text
Application capacity is exhausted
           ↓
Add application replicas
           ↓
Application bottleneck improves
           ↓
Database receives more concurrent work
           ↓
Database becomes the bottleneck
```

This is not automatically a reason to avoid scaling. It is a reason to understand **the full resource chain** before and after the intervention.

### 3. Statelessness as a scaling enabler

When scaling application instances horizontally, the system needs to allow requests to move between instances without depending on instance-local session state.

This is a supporting concept, not a reason to redesign the whole application into microservices.

### 4. Load balancing

Learn only the operational decision surface:

- how traffic reaches multiple replicas;
- health checks;
- removing unhealthy instances;
- uneven/hot workloads;
- the cost and limitations of the load-balancing layer.

Vitillo notes that delayed load information can create surprising balancing behavior and that load balancing itself contributes to system performance and availability.

### 5. Autoscaling

Learn the relationship:

```text
Observed load / resource pressure
             ↓
Capacity policy
             ↓
Add/remove replicas
```

Do not learn autoscaling as "latency high → add pods." Learn which metric is causally connected to useful capacity.

### 6. The database follows the application

Every scaling decision must ask:

> "What shared resource receives the additional work?"

That includes:

- databases;
- caches;
- message brokers;
- external APIs;
- connection pools;
- storage;
- downstream services.

## Practice

Scenario:

> The service handles 1,000 RPS at P99 200 ms. At 1,500 RPS, P99 rises to 2 seconds. CPU is 92%. Database CPU is 40%. Query latency is stable. Profiling shows request-local CPU work is the dominant cost.

Choose between:

`optimize`, `scale up`, `scale out`.

Defend the decision from the evidence and state what you would measure after the change.

## Exit criteria

I can justify scaling from evidence and can predict at least one downstream bottleneck that the intervention could expose.

## Source path

- *Foundations of Scalable Systems*, Ch. 1–2 — replication, optimization, scale-up/scale-out, service/database bottlenecks, caching, queueing.
- *Understanding Distributed Systems*, Ch. 1.3 — capacity and scaling; Ch. 18 — Network Load Balancing.
- *Designing Distributed Systems*, Ch. 6 — Replicated Load-Balanced Services.

---

# L7 — Controlled Validation: Profiling, Load Testing, Capacity Curves

## Target

Move from "I think this is the bottleneck" to **measured engineering evidence**.

## Learn

### 1. Baseline before intervention

Capture:

- throughput;
- latency distribution;
- error rate;
- resource utilization;
- database behavior;
- dependency behavior;
- queue depth / backlog when relevant.

### 2. Profiling

Use profiling to answer a narrow question:

> "Where is the process spending CPU/time/memory?"

The profile must be interpreted together with production behavior. A hot function is not automatically the root cause; it is evidence about where resources are being consumed.

### 3. Load testing

Learn to construct workload experiments that vary:

- request rate;
- concurrency;
- request mix;
- data volume;
- dependency latency;
- cache hit ratio where relevant.

### 4. Find the knee / capacity boundary

Think in curves, not single numbers:

```text
Load ↑
  │        response time
  │          /
  │         /
  │________/________
           ↑
     capacity boundary
```

Vitillo describes the point where a resource becomes exhausted and performance plateaus or worsens. Gorton likewise connects scalability to maintaining performance as load grows.

### 5. Validate the intervention

After a change, ask:

- Did the original bottleneck move?
- Did total work decrease?
- Did throughput increase?
- Did tail latency improve?
- Did error rate improve?
- Did a downstream resource become saturated?
- Did cost increase disproportionately?
- Did correctness change?

## Practice

Design one load test for the following claim:

> "Adding application instances will let the service absorb a 10× traffic burst."

Your test must be able to detect the case where the application tier scales successfully but the database becomes the new bottleneck.

## Exit criteria

I can design a controlled experiment that separates:

`better software efficiency` from `more compute capacity` from `a bottleneck moved downstream`.

## Source path

- *Foundations of Scalable Systems*, Ch. 1–2 — performance/scalability experiments and bottleneck-focused scaling.
- *Understanding Distributed Systems*, Ch. 29 — Testing; Ch. 31–32 — monitoring/observability.
- *Designing Distributed Systems*, Ch. 14 — Monitoring and Observability Patterns.

---

# L8 — Full Production Scenarios and Senior-Level Reasoning

## Target

Integrate the branches into realistic incidents without falling back to a memorized architecture recipe.

## Scenario set

### Scenario A — Traffic spike + high CPU

Possible mechanisms to discriminate:

- legitimate compute saturation;
- inefficient request processing;
- hot endpoint;
- excessive allocation/GC;
- lock/contention;
- a downstream failure causing local work to accumulate.

### Scenario B — Traffic spike + normal CPU + high latency

Possible directions:

- database latency;
- connection-pool wait;
- downstream network wait;
- queueing;
- locks;
- external service degradation.

### Scenario C — Scale-out makes the database fail

Investigate:

- query volume per request;
- total query rate;
- connection counts;
- hot queries;
- missing/ineffective indexes;
- locking;
- read amplification;
- cache behavior.

### Scenario D — Dependency becomes slow but still returns 200

Investigate:

- timeout configuration;
- worker/connection occupancy;
- retry behavior;
- retry amplification;
- circuit breaking/isolation;
- fallback or degraded behavior.

### Scenario E — Burst of asynchronous work

Investigate:

- whether the user needs synchronous completion;
- queue/load-leveling suitability;
- worker throughput;
- backlog growth;
- retry behavior;
- poison work;
- database write capacity.

### Scenario F — One tenant or API key dominates the workload

Investigate:

- rate-limiting policy;
- fairness;
- local versus global limits;
- business priority;
- whether rejected work should be retried;
- the cost of enforcing the quota itself.

### Scenario G — Cache disappears and the origin collapses

Investigate:

- cache hit ratio;
- origin capacity;
- cache warm-up behavior;
- request coalescing/thundering-herd risk;
- load shedding at the origin;
- whether the system can continue more slowly without the cache.

Vitillo explicitly treats caching as an optimization and discusses the possibility of cache failure causing a sudden origin surge.

---

# L9 — Frontier-AI Bridge: Performance and Reliability of LLM-Backed Systems

## Target

Apply the diagnostic skill of L0-L8 to systems whose slow, costly, rate-limited, nondeterministic dependency is a model call. This is the level that connects this journey to the Frontier Deployed Engineer mission in `AGENTS.md`.

## Why this level exists

L0-L8 are model-agnostic. A deployed agent adds a dependency with unusual properties: long and variable latency, a provider-side rate limit, a cost that grows with input and output size, and output that can be wrong even when the call succeeds. The same mechanisms apply (queueing, pool exhaustion, retry amplification, bottleneck migration), but a few new questions appear.

## Learn

### 1. The model call as a downstream dependency

- Tail latency of generation calls; time to first token versus total time when streaming is available.
- Provider rate limits and the error responses they return; timeouts sized to a latency budget, not to a guess.
- Cost as a capacity dimension: requests per second is not the only load measure; tokens per request and tokens per second matter.

### 2. Retries, side effects, and idempotency

- Retrying a pure model call is cheap in correctness terms but expensive in cost and load. Retrying a step that already triggered a tool with side effects (sending, writing, paying) is a correctness problem: apply the idempotency reasoning from L4.
- Capped exponential backoff with jitter, a retry budget, and honoring any retry guidance the provider returns. Retry storms are amplified when many workers back off in sync.

### 3. Concurrency and work shaping

- Your own pool or worker limit versus the provider's limit: which one binds first? Raising concurrency can lower throughput once the provider limit binds (compare Lab 3 and Lab 6).
- Work that does not need an immediate answer (batch classification, document processing) is a load-leveling candidate (L5). Interactive work needs bounded waiting and graceful degradation.

### 4. Context growth as unbounded state

- A conversation history or retrieved context that grows without a bound raises latency and cost per call and eventually fails. Treat it like the unbounded cache in L2-B: set a bound and a compaction or retrieval policy.

### 5. Trade-offs that need evaluation, not intuition

- Cheaper or faster model, shorter context, fewer tool calls, a cache, or a non-AI fallback each change quality as well as latency and cost. No such change ships without re-running the evaluation set from the FDE delivery loop (`AGENTS.md` section 7).
- Graceful degradation order: smaller model, then deterministic path, then human review, chosen by business criticality.

### 6. Observability for LLM calls

Record per call: workflow step, model identifier, input and output size, latency, retry count, outcome, estimated cost, and a trace id that ties it to the request. Without these fields the L1 diagnostic path cannot run.

**Verification rule.** Provider limits, error codes, parameters, and pricing change. Before teaching any specific number or parameter, check the current official documentation and state the date. Never quote limits from memory.

## Practice

> A pipeline processes 5,000 documents per night with an agent. After the team raised worker concurrency 4×, throughput fell, a large share of calls returned rate-limit errors, and the nightly cost rose by about 60%.

Write: (1) the measurements you would pull first; (2) two competing mechanisms; (3) the smallest intervention for each; (4) how you would show, with the evaluation set, that quality did not drop; (5) what you would add so the next change is caught earlier.

## Exit criteria

I can explain why more concurrency can reduce throughput once a provider limit binds.
I can state which retries are safe in an agent workflow and which are not, and why.
I can name the per-call fields I need in a trace to diagnose latency, cost, and failure.
I do not change a model, context size, or retry policy without an evaluation check.

## Source path

- Current official provider documentation on rate limits, errors, streaming, and timeouts (verify and date it).
- *Understanding Distributed Systems*, Vitillo, Ch. 27 — Downstream Resiliency.
- *Foundations of Scalable Systems*, Gorton, Ch. 5 — pools, queues, utilization.
- Anthropic Engineering, "A postmortem of three recent issues" (Sept 2025): why quality evals on production systems matter (re-open before teaching).

---

# Senior Interview Framework

When asked:

> **"Traffic suddenly increases 20×. What would you do?"**

Do **not** recite:

`Load Balancer → Kubernetes → Redis → Queue → Rate Limit`

Use a reasoning structure:

### 1. Establish the failure surface

What changed?

- traffic;
- latency;
- throughput;
- errors;
- concurrency;
- saturation;
- dependency behavior.

### 2. Find the constraint

Which resource or dependency is limiting useful work?

### 3. Verify the mechanism

Use:

- metrics;
- logs;
- traces;
- profiles;
- database/query evidence;
- queue/pool evidence;
- deployment/change timeline.

### 4. Mitigate according to the mechanism

Examples:

- inefficient CPU path → optimize;
- DB query bottleneck → fix access path/query/index/locking issue;
- downstream slowness → bound waiting and contain retries/failure;
- burst of asynchronous work → queue/load-level where semantics permit;
- abusive/excess traffic → rate limit or shed according to policy;
- true compute capacity limit → scale;
- non-critical work → degrade gracefully.

### 5. Re-measure

Prove that:

- latency improved;
- throughput improved;
- errors reduced;
- the original bottleneck eased;
- no more dangerous bottleneck appeared elsewhere.

### 6. Prevent recurrence

After mitigation:

- identify root cause;
- add instrumentation;
- improve tests/load tests;
- add capacity limits or protection;
- improve the runbook;
- perform a postmortem when warranted.

This aligns with Vitillo's operational guidance that incident response first mitigates user impact, then investigates root cause and prevention.

### 7. Say what you have and have not done

State the mechanism you would check, then separate experience from knowledge. Sample answers (keep these in English):

- Experience: "In <project>, I saw <symptom>. I checked <evidence>, found <mechanism>, changed <one thing>, and measured <before/after>."
- Adjacent experience: "I have not run this in production. I have reproduced it in a lab with <setup>, and the measurement showed <result>."
- Unknown: "I do not know yet. The measurement that would tell us is <metric or trace>."

Never claim a deployment, a number, or ownership that `EVIDENCE.md` does not support.

---

# What Not to Memorize

This journey deliberately avoids turning these technologies into default answers:

| Technology / pattern | Do not memorize as | Learn instead |
|---|---|---|
| Load balancer | "Traffic spike solution" | A traffic-distribution and health-management mechanism |
| Horizontal scaling | "More users = more servers" | Capacity replication for a diagnosed bottleneck |
| Redis / cache | "Latency is high = add Redis" | Read-path optimization with consistency/failure trade-offs |
| Queue | "High traffic = Kafka/RabbitMQ/SQS" | Load leveling when work can be asynchronous |
| Rate limiting | "Protect everything with 429" | Quota-based traffic control with explicit policy |
| Load shedding | "Return 503 when busy" | Local overload protection and admission control |
| Retry | "Retry transient errors" | Bounded, backoff-aware, idempotency-aware recovery |
| Circuit breaker | "Always install it" | Downstream failure isolation |
| Kubernetes autoscaling | "Scale on CPU" | Capacity control tied to the actual workload/resource |
| Index | "Indexes always make queries fast" | Query-plan-driven data-access optimization |

---

# Production Evidence Checklist

Use this before proposing a fix in a real incident.

## Request behavior

- [ ] RPS / throughput
- [ ] P50 / P95 / P99 latency
- [ ] Error rate
- [ ] Timeout rate
- [ ] Concurrency
- [ ] Endpoint/request mix

## Application

- [ ] CPU
- [ ] Memory
- [ ] Allocation / GC behavior where relevant
- [ ] Thread / worker saturation
- [ ] Queue/wait time
- [ ] Internal pool saturation
- [ ] Profile of expensive paths

## Database

- [ ] Query count per request
- [ ] Query latency
- [ ] Query plan
- [ ] Connection-pool utilization
- [ ] Locks/blocking
- [ ] CPU / I/O
- [ ] Hot queries / hot keys
- [ ] Read/write distribution

## Dependencies

- [ ] Downstream latency
- [ ] Downstream error rate
- [ ] Timeout behavior
- [ ] Retry volume
- [ ] Retry amplification
- [ ] Dependency-specific quotas/limits

## Protection mechanisms

- [ ] Rate limits
- [ ] Load shedding
- [ ] Queue depth / backlog
- [ ] Worker throughput
- [ ] Graceful degradation
- [ ] Cache hit ratio and origin load

## After the fix

- [ ] Did the original bottleneck improve?
- [ ] Did throughput improve?
- [ ] Did tail latency improve?
- [ ] Did correctness remain intact?
- [ ] Did cost remain acceptable?
- [ ] Did the bottleneck move downstream?
- [ ] Can the failure be reproduced in a controlled test?

---

# Labs — Learn by Breaking and Measuring

The project should have a small repeatable lab environment where the same API can be subjected to different failure modes.

## Lab 1 — CPU inefficiency

Create an endpoint with intentionally expensive request-local work.

Measure:

- RPS;
- P95/P99;
- CPU;
- request cost.

Change the implementation, then compare the same workload.

**Goal:** experience optimization increasing capacity without adding replicas.

## Lab 2 — Database amplification

Create an endpoint that retrieves a collection and then performs repeated database lookups per item.

Measure:

- queries/request;
- total query rate;
- database latency;
- connection usage;
- API latency.

Replace the access pattern with a set-based approach and re-measure.

**Goal:** connect application-level structure to database pressure.

## Lab 3 — Pool exhaustion

Introduce a deliberately slow dependency or database operation.

Increase concurrency while keeping CPU moderate.

Measure:

- in-flight requests;
- pool wait time;
- queue depth;
- timeout rate.

**Goal:** see how waiting can dominate response time even without CPU saturation.

## Lab 4 — Downstream retry storm

Create a dependency that intermittently fails.

Compare:

- immediate retries;
- capped backoff;
- jitter;
- no retry for permanent errors.

**Goal:** observe retry amplification rather than learning it only as a definition.

## Lab 5 — Burst + queue

Create asynchronous work that does not need to finish during the request.

Compare:

- synchronous processing;
- queued processing.

Then push arrival rate above worker capacity temporarily and observe backlog behavior.

**Goal:** understand what a queue absorbs and what it does not solve.

## Lab 6 — Scale-out shifts the bottleneck

Run the same workload with:

`1 → 2 → 4 → 8 application replicas`

while keeping a shared database resource bounded.

Track the point at which the database becomes the limiting resource.

**Goal:** experience bottleneck migration directly.

## Lab 7 — Cache as an optimization, not a dependency

Introduce a cache in front of a slower origin.

Measure:

- hit ratio;
- origin request rate;
- latency;
- behavior when the cache is unavailable.

**Goal:** see both the benefit and the failure mode.

## Lab 8 — LLM call under rate limits (L9)

Put a stub model service in front of a worker pool. Make the stub slow with a long tail, and make it return rate-limit errors above a request-rate threshold. Run the pool at increasing concurrency.

Compare:

- fixed retries;
- capped exponential backoff with jitter and a retry budget;
- a queue with a worker count set below the stub's limit.

Measure throughput, error rate, wasted calls, and total cost units.

**Goal:** see that raising concurrency past the provider limit lowers useful throughput, and that retries can multiply load.

## Lab 9 — Context growth and an evaluation gate (L9)

Build a small agent loop whose history grows each step. Measure latency and token counts per step. Add a bound (truncate or summarize) and re-measure. Run a small evaluation set before and after.

**Goal:** treat context as bounded state, and prove that a performance change did not break quality.

---

# Study Order Inside Each Level

For each level, use the same learning rhythm:

### Step 1 — Read the source

Read only the cited sections first. Do not read an entire distributed-systems book simply because one incident requires one concept.

### Step 2 — Rebuild the mechanism

Draw the request/data flow and mark:

- where work is created;
- where state lives;
- where waiting occurs;
- what resource is bounded;
- what happens under concurrency;
- what happens when a dependency fails.

### Step 3 — Break it

Run one controlled scenario from the labs or a project-specific equivalent.

### Step 4 — Observe it

Use the telemetry needed to test the hypothesis.

### Step 5 — Repair it

Change one variable.

### Step 6 — Compare

Record before/after measurements.

### Step 7 — Explain it

Answer the production scenario in your own words, without naming a tool until the mechanism requires it.

### Step 8 — Record it

Write a learning record only if you demonstrated the capability (a corrected misconception, a lab result, a decision you defended). Add a glossary term only once you can use it correctly. Update the reference sheet. Add the case to `casebook/<concept>.md`. Then re-ask the same idea in a changed scenario after a gap of days, not on the same day.

---

# Mastery Criteria

The journey is complete when I can handle the following cases without falling into a generic architecture checklist.

**Evidence rule:** tick a box only when a learning record, lab result, or project file proves it, and write its reference next to the box.

## Performance diagnosis

- [ ] I can explain why high CPU is a symptom, not automatically the root cause.
- [ ] I can distinguish CPU saturation from queueing/waiting.
- [ ] I can find where latency is spent using metrics, logs, and traces.
- [ ] I can use profiling to verify expensive execution paths.

## Database diagnosis

- [ ] I can detect query amplification such as N+1.
- [ ] I can reason from query count and query latency to database pressure.
- [ ] I can inspect query plans before assuming an indexing solution.
- [ ] I understand connection-pool exhaustion and blocking.
- [ ] I can recognize that scaling application instances can overload a shared database.

## Dependency resilience

- [ ] I can explain why slow dependencies are dangerous even when they return 200 responses.
- [ ] I can choose timeout behavior based on an explicit latency/error budget.
- [ ] I can reason about retries, backoff, jitter, and amplification.
- [ ] I can explain the correctness implications of retrying non-idempotent operations.

## Overload control

- [ ] I can distinguish rate limiting from load shedding.
- [ ] I can recognize when load leveling is appropriate.
- [ ] I can reason about queue backlog and consumer capacity.
- [ ] I can choose graceful degradation based on business-criticality.

## Scaling decisions

- [ ] I can justify scale-up vs scale-out from measured evidence.
- [ ] I can identify the likely downstream bottleneck created by a scaling change.
- [ ] I can explain why statelessness matters for horizontal scaling.
- [ ] I can discuss health checks and load balancing at the operational level.

## Production judgment

- [ ] I mitigate user impact before trying to perfect the root-cause fix.
- [ ] I can state what I do not know and what measurement would resolve the uncertainty.
- [ ] I validate changes under controlled load.
- [ ] I can turn an incident into prevention work: instrumentation, tests, limits, runbooks, and postmortem actions.

## Interview judgment

- [ ] I do not begin a 20× traffic answer by naming Redis, Kubernetes, or a load balancer.
- [ ] I start by establishing the observed failure and the bottleneck evidence.
- [ ] I select interventions conditionally.
- [ ] I explicitly discuss trade-offs and downstream effects.
- [ ] I can say, truthfully: **"I would diagnose the bottleneck first; the solution depends on which resource or dependency is actually limiting the system."**

## AI-system bridge

- [ ] I can explain why raising concurrency can lower throughput once a provider rate limit binds.
- [ ] I can decide which agent steps are safe to retry and which need idempotency protection.
- [ ] I can list the per-call fields needed to trace latency, cost, and failures of model calls.
- [ ] I can bound context growth and show with an evaluation set that quality held.
- [ ] I can choose a degradation order (smaller model, deterministic path, human review) by business criticality.

---

# Primary Project Sources

## 1. Foundations of Scalable Systems — Ian Gorton

Use for the fundamental performance/scalability distinction and for the connection between optimization, replication, application capacity, database bottlenecks, caching, asynchronous queueing, and resource pools.

Relevant material retrieved from the project source:

- Ch. 1 — scalability; replication and optimization; performance; bottlenecks.
- Ch. 2 — service tiers; scale-out; database bottlenecks; caching; asynchronous queueing; hardware scalability.
- Ch. 5 — application service execution; thread pools; request queues; database connection pools; utilization and monitoring.

## 2. Understanding Distributed Systems, 2nd ed. — Roberto Vitillo

Use for the operational reasoning around performance, load, capacity, overload, downstream failure, caching, monitoring, and observability.

Relevant material:

- Ch. 1.3 — Scalability.
- Ch. 18 — Network Load Balancing.
- Ch. 19 — Data Storage.
- Ch. 20 — Caching.
- Ch. 23 — Messaging.
- Ch. 24 — Common Failure Causes.
- Ch. 26 — Fault Isolation.
- Ch. 27 — Downstream Resiliency.
- Ch. 28 — Upstream Resiliency.
- Ch. 29 — Testing.
- Ch. 31 — Monitoring.
- Ch. 32 — Observability.

## 3. Designing Distributed Systems, 2nd ed. — Brendan Burns

Use selectively for implementation-oriented patterns and labs, not as a reason to study distributed systems broadly.

Relevant material:

- Ch. 6 — Replicated Load-Balanced Services.
- Ch. 9 — Functions and Event-Driven Processing.
- Ch. 11 — Work Queue Systems.
- Ch. 12 — Event-Driven Batch Processing.
- Ch. 14 — Monitoring and Observability Patterns.
- Ch. 16 — Common Failure Patterns, especially the thundering-herd and obsolete-work patterns.

## 4. User-supplied production/performance articles

Use these as the anti-pattern and scenario source for:

- measure before changing architecture;
- performance engineering before blind hardware scaling;
- N+1 query amplification;
- database bottlenecks;
- memory/CPU as symptoms that require investigation;
- timeout/retry/circuit-breaker reasoning;
- asynchronous work;
- rate limiting;
- graceful degradation;
- scaling only after establishing that the current capacity is genuinely insufficient.

These materials are treated as **scenario input**, not as a substitute for source-backed implementation details from the project books.

## 5. Casebook seeds (research starting points, not verified facts)

Open the primary source, read it, and record the case with the format in `TEACHING-PROTOCOLS.md` P§2 before teaching from it.

- Google Cloud incident report, 2025-06-12 (Service Control): recovery without randomized exponential backoff. Link in P§7. Unchecked.
- Anthropic Engineering, "A postmortem of three recent issues" (Sept 2025): evaluation of production quality. Link in P§7. Unchecked.
- Possible further cases, named from memory and unchecked: Facebook's September 2010 outage; Slack's 2021-01-04 outage; Cloudflare's 2025-11-18 outage; AWS us-east-1 on 2025-10-20. Confirm each exists, read the postmortem, and discard any that do not fit a level.
- If fewer than five solid cases exist for a concept, say so and record the gap in `RESOURCES.md`.

---

# Final Rule

> **The goal is not to become the engineer who knows the largest number of scaling components. The goal is to become the engineer who can look at a failing production system, identify the constraint, prove the mechanism, choose the smallest appropriate intervention, and verify that the system actually became better.**

That is the skill this study map is designed to train.
