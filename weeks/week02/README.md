# 📘 Week 02 Log — Keras Architecture Recovery

**Scope:** Module and forward/backward flow recovery  
**Version:** Final / Improved  
**Date range:** March 15–20, 2026  
**Status:** Complete — module mapping, forward-pass tracing, gradient computation, device allocation, and architecture interpretation finalized.

## Objectives

1. Understand Keras module structures by identifying core modules (`layers`, `models`, `ops`) and their responsibilities.
2. Trace forward execution and observe data flow through sequential and custom layers.
3. Recover backward/gradient flow, including training step and optimizer application.
4. Determine allocation mapping across runtime environment, device detection, and module-to-backend mapping.
5. Analyze architectural patterns in modularity, backend delegation, and extensibility.

## Readings

- Bass, Clements, Kazman (2012), *Software Architecture in Practice* (3rd Edition), Chapters 1, 2, and 13.
- Keras official documentation: https://keras.io
- Solo Project Overview (2026): Keras 3 architecture, multi-backend design, Python abstractions.

## Experiments Run

1. **Dependency Discovery (Static Module Analysis)**
   - Inspected module origin of `layers.Dense`, `models.Model`, and `ops`.
   - Revealed primary dependencies (`layers → ops → backend`).

2. **Forward Pass Trace**
   - Used a custom `DebugLayer` to observe input/output shapes.
   - Traced flow: `Dense → DebugLayer → Dense`.
   - Validated data propagation and layer orchestration.

3. **Manual Training Step / Full Gradient Flow**
   - Used `GradientTape` to compute loss gradients.
   - Observed gradient propagation from output to weights.
   - Applied `SGD` updates via `apply_gradients`.

4. **Device Detection / Allocation Mapping**
   - Collected available devices from TensorFlow (CPU/GPU).
   - Produced allocation mapping from modules to runtime environment.

## Architecture Findings

- **Modular design:** `layers`, `models`, `ops`, and backend are clearly separated.
- **Separation of concerns:** Layers define computation, models orchestrate, ops delegate execution.
- **Patterns observed:**
  - Strategy pattern for backend selection (TensorFlow / JAX / PyTorch / OpenVINO).
  - Factory pattern for layer creation and registration.
  - Layered architecture (`Input → Layer → Model → Backend → Hardware`).
- **Portability and extensibility:** Same layer code runs across multiple backends.
- **Backend delegation:** Python-level logic is decoupled from hardware kernels.
- **Runtime consistency:** Forward pass, backward pass, and optimizer update follow expected DL training flow.

## Module View — Core Architectural Subsystems

- **Model:** Orchestrates layers; entry point for training/inference.
- **Layer:** Encapsulates per-layer computation and transformation.
- **Ops:** Abstract computation primitives; delegates to backend.
- **Backend:** Execution engine over TF/JAX/PyTorch and device runtime.
- **Autograd:** Gradient engine producing derivatives (`GradientTape` context).
- **Kernels:** Hardware-level numeric operations (CPU/GPU).
- **Optimizer:** Applies parameter updates through backend operations.

## Component & Connector View — Forward and Backward Pass

1. **Input stage:** Tensor `x` enters model.
2. **Forward flow:** Each `layer.call()` runs sequentially (`Dense → DebugLayer → Dense`), delegating ops to backend.
3. **Output/loss stage:** `y_pred` is computed, then loss is evaluated.
4. **Backward flow:** `GradientTape` computes gradients for trainable variables via backend kernels.
5. **Optimizer update:** `apply_gradients` updates model weights.
6. **Device allocation:** Backend dispatches computation to available device(s).

**Observation:** Delegation, abstraction, and separation are consistently applied, with a backend-agnostic C&C flow.

## Allocation Table (Week 2 — Final)

| Component | Type | Runs Where | Dependency |
| --- | --- | --- | --- |
| Model | Orchestrator | Python (CPU) | Layers |
| Layer | Logic wrapper | Python | Ops |
| Ops | Abstraction API | Python API | Backend |
| Backend | Execution engine | TensorFlow / JAX / PyTorch | Hardware |
| Autograd | Gradient engine | Backend | Hardware |
| Kernels | Numeric ops | CPU / GPU | None |
| Optimizer | Update logic | Python + backend ops | Backend |

## Blockers / Open Questions

1. Backend-specific optimizations (for example JAX JIT) were not fully traced.
2. Multi-device synchronization patterns remain unclear for distributed training.
3. Some non-standard `call()` signatures may expose hidden dependency behavior.

## Next Week Focus

1. Trace multi-layer and Functional API models (expand C&C view).
2. Recover full runtime training call chain (`model.fit`) across backends.
3. Document inter-layer dependency patterns and optimization strategies for Week 3.

## Week 02 Summary Tagline

Module → Forward/Backward → Allocation → Pattern discovery: Keras internals reveal modularity, backend-agnostic delegation, and runtime orchestration.