# Architecture Recovery Methodology

This document describes the process used to recover the architecture of Keras 3.
It explains the three-view approach, the evidence techniques applied, how claims
are validated, and the quality criteria used to assess completeness.

Reference: Bass, Clements, Kazman — *Software Architecture in Practice*, Ch.1, Ch.4

---

## 1. What Architecture Recovery Means Here

Architecture recovery is the process of extracting explicit architectural knowledge
from an existing system whose architecture was never formally documented, or whose
documentation has diverged from the implementation.

For Keras 3, the source code and documentation exist but no single document presents
the architecture in the structured, multi-view format described by Bass et al.
This project produces that document by combining reading, observation, and
experimentation.

**Goal:** Recover the three fundamental architectural structures of Keras and explain
how they jointly support the system's key quality attributes.

---

## 2. The Three-View Framework

No single architectural view captures all concerns. Bass et al. define three
categories of structure, each answering a different question:

| View | Question answered | Primary use |
|---|---|---|
| Module View | Who depends on whom at design time? | Reasoning about modifiability and change impact |
| Component-and-Connector View | Who interacts with whom at runtime, and in what order? | Reasoning about performance and runtime correctness |
| Allocation View | Where does each element actually execute? | Reasoning about portability and deployment |

Each view is necessary. Together they give a complete picture:
- The Module View explains *why* Keras can switch backends (no direct dependency).
- The C&C View shows *how* training actually runs (pipeline + feedback loop).
- The Allocation View shows *where* computation happens (Python vs backend vs hardware).

---

## 3. Recovery Techniques

Three complementary techniques were used, each suited to a different question type.

### 3.1 Static Analysis

**What it answers:** What modules exist? What are their dependencies?

**Techniques used:**
- `pkgutil.iter_modules(keras.__path__)` — enumerates all top-level Keras packages
- `inspect.getmodule(cls)` — traces which source module a class originates from
- Manual reading of `vendor/keras/` source — confirms dependency direction

**Limitations:** Static analysis reveals declared structure, not runtime behaviour.
A module dependency does not tell you when or how often the dependency is exercised
at runtime.

### 3.2 Dynamic Tracing

**What it answers:** In what order do components execute? What data flows between them?

**Techniques used:**
- `DebugLayer` and `DebugDense` subclasses — override `call()` to print shape information
  during the forward pass, making execution order directly observable
- `BatchLogger` callback — hooks into `on_train_batch_end` to make per-batch training
  progress visible
- `model.train_on_batch()` with weight snapshots — captures weight state before and after
  one training step to confirm gradient flow occurred

**Limitations:** Dynamic tracing only observes the paths exercised by the specific
inputs and configurations used. Edge cases and error paths are not observed.

### 3.3 Behavioural Validation

**What it answers:** Do abstraction boundaries hold functionally, not just structurally?

**Techniques used:**
- Backend switching via `KERAS_BACKEND` — runs identical model code with different
  backends to confirm that the `keras.ops` abstraction boundary holds in practice
- Direct `keras.ops.*` calls — calls `ops.matmul`, `ops.relu` directly to observe
  that they route to the backend without any backend import in the calling code

**Limitations:** Behavioural validation confirms that the architecture works as
claimed for the tested scenarios, but does not constitute a proof for all cases.

---

## 4. The Recovery Workflow

Each architectural claim follows this pipeline:

```
Hypothesis                  "keras.ops is the abstraction boundary"
    |
Static observation          Inspect module imports: no layer imports TF directly
    |
Dynamic confirmation        exp02_forward_trace.py: delegation chain observed at runtime
    |
Behavioural validation      exp05_backend_switching.py: same code runs on TF and JAX
    |
Documented claim            views/module-view.md + findings/design-decisions.md
```

A claim is considered recovered when all three steps are complete: the static
structure supports it, dynamic behaviour confirms it, and a behavioural experiment
validates it in a runnable script.

---

## 5. Quality Criteria for Recovered Architecture

A recovered view is considered complete when it meets all of the following criteria,
drawn from the Bass et al. completeness checklist (Ch.1):

| Criterion | Description |
|---|---|
| **Elements present** | Every component or module in the view is named and described |
| **Relations present** | Every dependency or interaction between elements is shown |
| **Behaviour present** | The view includes dynamic behaviour, not just static boxes |
| **Rationale present** | Each structural decision is explained in terms of quality attributes |
| **Evidence present** | At least one experiment supports each major claim |

A box-and-arrow diagram without behaviour and rationale is an incomplete view.
All three views in `views/` meet this standard.

---

## 6. Scope and Limitations

**In scope:**
- Core training pipeline: `Model`, `Layer`, `Optimizer`, `Loss`, `keras.ops`, `Backend`
- Three standard backends: TensorFlow, JAX, PyTorch (TF used as primary for experiments)
- Three architectural view types: Module, C&C, Allocation

**Out of scope:**
- Distributed training and multi-device allocation
- Keras saving, export, and deployment pipeline
- Pre-trained models (`keras.applications`) and preprocessing (`keras.preprocessing`)
- Backend-internal architecture (the internals of TensorFlow, JAX, or PyTorch)

These scoping decisions keep the recovery focused on the architectural claims that
are most relevant to the quality attributes under study: modifiability, portability,
and maintainability.
