# 📘 Week 01 Log – Keras Architecture Reconnaissance  
**Final / Improved Version**  
**Date range:** March 12–14, 2026  
**Status:** Complete – foundational mapping + initial runtime observations

## Objectives

- Understand **Keras architectural philosophy** and core design principles
- Discover the **actual module structure** (beyond surface-level docs)
- Identify key **architectural subsystems** and their responsibilities
- Observe **runtime execution behavior** (forward pass + basic control flow)

## Readings

- Keras **Getting Started** guide (official documentation)
- Software Architecture **Chapter 1** — structures & architectural views

## Experiments Run

- Sequential model training pipeline (standard `fit()` style)
- Static module discovery using `pkgutil.walk_packages()` + introspection
- Micro-training experiment with `model.train_on_batch()` (minimal external loop control)
- Forward execution tracing via custom debug layer and/or callback hooks

## Architecture Findings

Keras exhibits a **clean, layered modular architecture** with strong separation of concerns and excellent extensibility:

- **Layered / composable design** — core computation built from reusable units (layers)
- **Pipeline-style dataflow** during the forward pass
- **Model** class acts as the central **orchestration controller** (wires layers, manages call graph)
- **Backend subsystem** provides a powerful **platform abstraction layer** (TensorFlow, JAX, PyTorch)
- **Training loop** structured as a **closed feedback control system**  
  (forward → loss computation → backward → parameter update)

Multi-backend support strongly reinforces a **platform-agnostic**, highly portable design.  
Presence of dedicated optimization and (optionally) distribution-related modules further highlights **scalability** and production-readiness.

### Module View – Core Architectural Subsystems

1. **Computation subsystem**  
   → Layers, activations, initializers, regularizers, constraints

2. **Orchestration subsystem**  
   → `Model` base class, `Sequential`, Functional API, subclassing API

3. **Training control subsystem**  
   → Optimizers, losses, metrics, callbacks, `fit()` / `train_on_batch()` / `evaluate()` logic

4. **Infrastructure abstraction subsystem**  
   → Backend (`keras.src.backend`), unified `ops` namespace, dispatch/routing mechanism

5. **Lifecycle management subsystem**  
   → Model saving/loading, serialization, exporting (Keras v3 format, SavedModel, ONNX, etc.)

### Component & Connector View – Observed Runtime Sequence (Forward Pass)

- Input tensor(s) enter the model
- **Model** routes data through an **ordered layer pipeline** (sequential) or graph execution (functional/subclassed)
- For each layer:
  - Executes any custom Python logic (if present)
  - **Delegates core tensor/math operations** to the active backend via `ops` / backend dispatch
- Output tensor is produced and returned
- In training mode: loss computed → backward pass triggered (gradient flow begins)

This results in a very clean **dataflow + delegation** pattern — elegant and backend-transparent at the Keras level.

## Blockers / Open Questions

- Limited visibility into **gradient backpropagation connectors**  
  (exact path: layers → ops → backend → framework autograd engine)
- Unclear **allocation / device mapping** — which ops run on CPU vs. GPU/TPU/XPU  
  (especially across different backends and in mixed-precision scenarios)
- Need better understanding of **backend dispatch decision points**  
  (when/how Keras chooses specific backend implementations)

## Next Week Focus

- Trace the full **gradient update runtime cycle** (backward pass + apply_gradients)
- Map and document the **detailed backend call chain**  
  (Keras → `ops` → backend framework → hardware execution)
- Build an **allocation architecture table**  
  (categorizing subsystems and common ops as backend-agnostic vs. backend-dependent)

---

**Week 01 Summary Tagline**  
*High-level philosophy → concrete module mapping → first glimpses of runtime behavior*