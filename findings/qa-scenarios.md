# Quality Attribute Scenarios

Formal quality attribute scenarios for Keras 3, using the six-part template from
Bass, Clements, Kazman — *Software Architecture in Practice*, Ch.4.

Each scenario specifies: Source → Stimulus → Environment → Artifact → Response → Response Measure.
The response measure makes the scenario testable and unambiguous.

---

## Scenario 1: Modifiability — Adding a New Compute Backend

| Element | Value |
|---|---|
| **Source of stimulus** | Keras core maintainer |
| **Stimulus** | Wants to add WebGPU as a new execution backend for browser-based inference |
| **Environment** | Keras 3 production codebase, stable release, normal development |
| **Artifact** | `keras/backend/` module and `keras.ops` dispatch layer |
| **Response** | New backend is integrated; existing layer, model, and training code is unchanged; backend is selectable via `KERAS_BACKEND=webgpu` |
| **Response measure** | Fewer than 5 files outside `keras/backend/` require modification; all existing tests pass without change; the new backend is active by setting one environment variable |

**Architectural tactic enabling this:** Use an intermediary (`keras.ops`), Restrict dependencies (no layer imports a backend directly)

**Where the architecture satisfies it:** The `keras.ops` abstraction boundary (see `views/module-view.md`) means the only integration point for a new backend is within `keras/backend/`. The rest of the codebase is untouched by design.

**Evidence:** `experiments/exp05_backend_switching.py` — same model code runs unchanged when `KERAS_BACKEND` is switched, confirming the boundary holds.

---

## Scenario 2: Portability — Migrating a Model to a Different Runtime

| Element | Value |
|---|---|
| **Source of stimulus** | ML platform engineer |
| **Stimulus** | Needs to move a trained production model from TensorFlow to JAX for deployment on a new accelerator |
| **Environment** | Trained model already in production; JAX is available in the target environment |
| **Artifact** | Model definition code and training scripts |
| **Response** | The model runs on the JAX backend producing structurally identical outputs; no source code changes required in model or training files |
| **Response measure** | Zero lines of model or training code modified; only `KERAS_BACKEND` environment variable changed; model outputs agree within floating-point tolerance |

**Architectural tactic enabling this:** Encapsulate (backend details hidden behind `keras.ops`), Defer binding (backend bound at process start, not at code-compile time)

**Where the architecture satisfies it:** The Allocation View (see `views/allocation-view.md`) shows that backend selection is a runtime allocation decision, not a design-time code dependency.

**Evidence:** `experiments/exp05_backend_switching.py` — demonstrates that switching `KERAS_BACKEND` requires no code changes.

---

## Scenario 3: Testability — Validating an Architectural Claim Experimentally

| Element | Value |
|---|---|
| **Source of stimulus** | Architecture recovery analyst (student) |
| **Stimulus** | Wants to verify the claim that gradient computation is fully delegated to the backend and never occurs in model or layer Python code |
| **Environment** | Development environment, Keras 3 installed with TensorFlow backend |
| **Artifact** | A minimal model with inspectable trainable weights |
| **Response** | An experiment is written that runs one training step and confirms that: (a) weights change, proving gradient flow occurred; (b) no gradient computation code appears in model or layer Python source; (c) only `keras.*` APIs are needed — no direct backend import |
| **Response measure** | Experiment runs in under 5 seconds; all weights in the model are updated (confirmed by `numpy.allclose` comparison before and after); experiment source contains zero lines importing a backend library directly |

**Architectural tactic enabling this:** Separate concerns (model orchestrates; backend computes), Encapsulate (gradient computation hidden behind `train_on_batch`)

**Where the architecture satisfies it:** The C&C View (see `views/cnc-view.md`) shows that the gradient computation path flows through `keras.ops` → `Backend`, bypassing the Python model tier entirely.

**Evidence:** `experiments/exp04_gradient_flow.py` — uses only `keras.*` APIs; confirms weight updates; no backend import in source.

---

## Notes on Scenario Construction

These scenarios follow the format defined in Bass et al., Ch.4, Section 4.1.
Key properties of a valid quality attribute scenario:

1. **Quantified response measure** — "fewer than 5 files", "zero lines modified", "under 5 seconds"
2. **Named artifact** — specifies what part of the system is affected
3. **Realistic stimulus** — grounded in actual development activities, not abstract
4. **Architectural traceability** — each scenario references the view and tactic that enables the response
