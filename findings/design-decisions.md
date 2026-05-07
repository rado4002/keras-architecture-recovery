# Design Decisions — Seven-Category Mapping

This file maps the key architectural design decisions recovered from Keras 3 to the
seven categories defined in Bass, Clements, Kazman — *Software Architecture in Practice*, Ch.4.

Each category is a question. The decision is the answer Keras gives.

---

## Category 1: Allocation of Responsibilities

**Question:** What responsibilities are assigned to which elements?

**Keras decision:** Responsibilities are allocated along the primary dependency chain,
one concern per level:

| Element | Sole responsibility |
|---|---|
| `keras.models` | Orchestrate topology and training lifecycle |
| `keras.layers` | Define reusable, atomic transformation logic |
| `keras.ops` | Route operations to the active backend (dispatch only) |
| Backend | Execute all tensor mathematics and autodiff |

**Rationale:** Assigning one clear responsibility per level prevents coupling between
abstraction concerns. A change to how training is orchestrated (Model level) does not
affect how matrix multiplication is computed (Backend level).

**Quality attribute impact:** Modifiability — changes are local to one level.

---

## Category 2: Coordination Model

**Question:** How do elements coordinate — how do they communicate and synchronise?

**Keras decision:** Coordination is entirely through synchronous procedure calls and
tensor dataflow. There is no shared global mutable state between components outside
the model's weight tensors.

The training sequence is:
```
Model.fit() -> Layer.call() -> ops.matmul() -> Backend kernel -> return tensor
```

Each call passes data forward; results are returned synchronously. The backend is
the only component that writes to hardware memory.

**Rationale:** Synchronous call-and-return makes execution order predictable and
makes the system debuggable (you can trace any call with a standard Python debugger
or a `DebugLayer`).

**Quality attribute impact:** Testability, Understandability.

---

## Category 3: Data Model

**Question:** What are the major data abstractions and how do they flow through the system?

**Keras decision:** The fundamental data abstraction is the **tensor** — a multi-dimensional
array managed by the active backend. Tensors are the only data type that crosses
subsystem boundaries.

| Data type | Created by | Consumed by |
|---|---|---|
| Input tensor | User / `DataLoader` | `keras.layers` via `Model.call()` |
| Activation tensor | `keras.layers` (via `keras.ops`) | Next layer in the chain |
| Loss scalar | `keras.losses` | `keras.ops` (gradient computation) |
| Gradient tensor | Backend autodiff | `keras.optimizers` |
| Updated weight tensor | `keras.optimizers` (via `keras.ops`) | Model weight variables |

**Rationale:** A single unified data abstraction (tensor) that all components share
eliminates the need for data format conversion between components. The backend owns
the actual tensor representation; the Python API owns the references.

**Quality attribute impact:** Interoperability, Performance.

---

## Category 4: Management of Resources

**Question:** What shared resources exist? How are they managed? What are the limits?

**Keras decision:**

| Resource | Manager | Access policy |
|---|---|---|
| Model weights (tensors) | Backend (owns memory) | Written only by `Optimizer` via `keras.ops`; read by `Layer.call()` |
| Active backend | `KERAS_BACKEND` env var | Bound once at process start; immutable during a session |
| Hardware devices (CPU/GPU) | Backend runtime | Managed transparently; exposed to user only for explicit placement |
| Computation graph (JAX/TF) | Backend | Built and executed within the backend; invisible to Python tier |

**Rationale:** Centralising memory ownership in the backend allows backend-specific
optimisations (in-place ops, memory pools, graph caching) without exposing them to
the Python tier.

**Quality attribute impact:** Performance, Scalability.

---

## Category 5: Mapping Among Architectural Elements

**Question:** How do design-time constructs map to runtime constructs?

**Keras decision:**

| Design-time element | Runtime construct |
|---|---|
| `layers.Dense` class definition | A Python object instantiated per layer in the model |
| `model.compile()` call | Configures the training loop — binds optimizer, loss, and metrics to the model |
| `keras.ops.matmul` function | A backend kernel invocation at runtime |
| `KERAS_BACKEND=tensorflow` | Determines which backend module is loaded at Python import time |
| `model.fit(x, y)` | Triggers the iterative training loop — one Python call maps to N batch iterations |

**Rationale:** The mapping is designed so that the Python abstraction is thin and
predictable. `model.fit()` maps to a loop, not a single operation, which is made
explicit by the `BatchLogger` callback mechanism.

**Quality attribute impact:** Understandability, Testability.

---

## Category 6: Binding Time Decisions

**Question:** When are choices bound — at design time, compile time, load time, or runtime?

**Keras decision:**

| Decision | Binding time | Flexibility | Mechanism |
|---|---|---|---|
| Which backend to use | Runtime (process start) | Any backend can be chosen per run | `KERAS_BACKEND` environment variable |
| Which optimizer to use | Runtime (after `model.compile()`) | Can be changed between training runs | `model.compile(optimizer=...)` |
| Which device to use (CPU/GPU) | Runtime (backend startup) | Transparent; overridable via backend API | Backend device placement |
| Layer types in a model | Design time (model definition) | Fixed once the model is built | Constructor arguments |
| Keras API version | Design time (import) | Fixed to installed version | `import keras` |

**Key decision — backend binding at runtime:** Deferring backend binding to process
start (not code-compile time) is the central architectural decision that enables
multi-backend support. If the backend were bound at import time or hardcoded, the
portability scenario (QA Scenario 2) would be impossible.

**Quality attribute impact:** Portability, Modifiability.

---

## Category 7: Choice of Technology

**Question:** What technologies are used, and what constraints do those choices impose?

**Keras decision:**

| Technology | Used for | Constraint imposed |
|---|---|---|
| Python 3.11+ | All orchestration and API code | Dynamic typing; runtime flexibility; no compile-time dependency resolution |
| `keras.ops` unified API | All tensor operations | New backend must implement the full `keras.ops` interface |
| TensorFlow / JAX / PyTorch | Tensor execution backends | Each backend has its own tensor type; tensors are not portable across backends |
| Environment variable (`KERAS_BACKEND`) | Backend selection | Backend cannot be changed after Python process starts |
| NumPy-compatible array protocol | Data input | Input data must be convertible to the backend's tensor type |

**Rationale:** Python was chosen for the orchestration tier because its dynamic
nature supports the extension-by-subclassing design (custom layers, custom callbacks).
The backend-agnostic `keras.ops` API was introduced specifically to remove the prior
hard dependency on TensorFlow, which was the single largest modifiability constraint
in earlier Keras versions.

**Quality attribute impact:** Portability (multi-backend), Modifiability (ops abstraction),
Performance (backend-specific optimisation).
