# Architectural Patterns

This file catalogs every architectural pattern identified in Keras 3 during the
recovery process, with a description of where it appears, why it was chosen, and
which quality attributes it supports.

Reference: Bass, Clements, Kazman — *Software Architecture in Practice*, Ch.13

---

## Pattern 1: Layered Architecture

**Where it appears:**
The static module structure follows a strict layered order:
`keras.models → keras.layers → keras.ops → Backend`

**Description:**
Each layer depends only on the layer directly below it. No layer bypasses an
intermediate layer to reach a lower one. Dependencies never point upward.

**Why it was chosen:**
- Reduces coupling between abstraction levels
- Allows each layer to evolve independently
- Makes the impact of a change predictable and local

**Quality attributes supported:** Modifiability, Maintainability, Understandability

**Evidence:** `exp01_module_scan.py`, `exp02_forward_trace.py`

---

## Pattern 2: Pipe-and-Filter (Training Pipeline)

**Where it appears:**
The runtime training sequence:
`Forward pass → Loss computation → Gradient computation → Weight update`

**Description:**
Each phase is a discrete processing stage. The output of one stage (e.g., the
prediction tensor from the forward pass) becomes the input to the next stage
(loss computation). Stages are ordered and each has a single well-defined function.

**Why it was chosen:**
- Makes the training process traceable and analyzable
- Each stage can be replaced or extended independently
- Supports custom training loops (users can override any stage)

**Quality attributes supported:** Testability, Modifiability, Understandability

**Evidence:** `exp03_training_step.py`, `exp04_gradient_flow.py`

---

## Pattern 3: Feedback Control Loop

**Where it appears:**
The training loop as a whole: each iteration uses the loss signal from the current
batch to update model weights, which then affects the output of the next forward pass.

**Description:**
An iterative control system where output is fed back as input to drive the system
toward a desired state (minimum loss). The loop runs once per batch and accumulates
learning across epochs.

**Why it was chosen:**
- Captures the learning dynamic accurately
- Models the adaptive nature of gradient-based optimisation
- Makes convergence behavior analyzable

**Quality attributes supported:** Performance, Analyzability

**Evidence:** `exp03_training_step.py`

---

## Pattern 4: Bridge (Backend Abstraction)

**Where it appears:**
`keras.ops` acts as the bridge between the high-level abstraction (Keras API) and
the low-level implementations (TensorFlow, JAX, PyTorch backends).

**Description:**
The Bridge pattern decouples an abstraction from its implementation so the two can
vary independently. Here: the abstraction is the `keras.ops` API (stable); the
implementations are the backend runtimes (variable).

**Why it was chosen:**
- Enables multi-backend support without changing any layer or model code
- A new backend can be added by implementing the `keras.ops` interface
- The abstraction side (model and layer code) is completely insulated from backend changes

**Quality attributes supported:** Portability, Replaceability, Modifiability

**Tactic applied:** Use an intermediary (Bass et al., Ch.7)

**Evidence:** `exp05_backend_switching.py`, `exp06_backend_delegation.py`

---

## Pattern 5: Strategy (Interchangeable Algorithms)

**Where it appears in three places:**

1. **Optimizers** — SGD, Adam, RMSprop, Adagrad are interchangeable implementations
   of the same `Optimizer` interface (`apply_gradients`)
2. **Loss functions** — MSE, CrossEntropy, Huber are interchangeable implementations
   of the same `Loss` interface (`call(y_pred, y_true)`)
3. **Backends** — TensorFlow, JAX, PyTorch are interchangeable implementations
   of the backend interface (via `keras.ops`)

**Description:**
A family of algorithms is encapsulated behind a common interface. The client
(Model) works with the interface and is unaffected by which concrete algorithm
is chosen.

**Why it was chosen:**
- Supports experimentation (swap optimizers, loss functions, backends freely)
- Algorithm changes do not propagate to the model
- New strategies can be added without modifying existing code

**Quality attributes supported:** Modifiability, Testability, Extensibility

**Evidence:** `exp04_gradient_flow.py` (optimizer swap), `exp05_backend_switching.py` (backend swap)

---

## Pattern 6: Composite (Model over Layers)

**Where it appears:**
`keras.models.Model` composes multiple `keras.layers.Layer` instances into a
directed execution graph. Models can also contain sub-models (nested composition).

**Description:**
A Composite allows individual components (Layers) and compositions of components
(Models) to be treated uniformly. A sub-model is just another layer from the
perspective of its parent model.

**Why it was chosen:**
- Supports hierarchical model construction (e.g., encoder + decoder inside a larger model)
- Simplifies the interface: everything is a `Layer` from the model's perspective
- Enables recursive model nesting without special-casing

**Quality attributes supported:** Reusability, Modifiability

**Evidence:** `exp02_forward_trace.py`

---

## Pattern Summary Table

| Pattern | Where in Keras | Primary quality attribute |
|---|---|---|
| Layered Architecture | `models → layers → ops → backend` | Modifiability |
| Pipe-and-Filter | Training pipeline stages | Testability |
| Feedback Control Loop | Training loop per batch | Performance |
| Bridge | `keras.ops` ↔ backend | Portability |
| Strategy | Optimizers, losses, backends | Modifiability |
| Composite | Model composes Layers | Reusability |
