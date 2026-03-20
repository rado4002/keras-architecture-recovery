
---

# Keras Architecture Recovery – Week 1 Notebook

**Project**: Recovering the Software Architecture of Keras 3 (keras-team/keras)  
**Date**: March 2026  
**Textbook reference**: *Software Architecture in Practice*, 3rd Edition (Bass, Clements, Kazman)  
**Focus**: Introduction to architecture views (Ch. 1), importance of architecture (Ch. 2), initial module decomposition

## 1. Why Keras? – Project Motivation (from Solo Project Overview)

Keras 3 is a high-level, multi-backend deep learning framework ("Deep Learning for humans").  
Key 2026 strengths:

- Unified API across **JAX**, **TensorFlow**, **PyTorch**, **OpenVINO**
- Backend switch via environment variable → extreme portability
- 100% Python → excellent for architecture study
- Clean, well-documented, very active repository (~63.9k stars)

**Architectural teaser**: Classic **abstraction layer** + **strategy pattern** (backend selection) + **composite pattern** (models over layers) → illustrates modifiability, portability, and layered structures (textbook Ch. 1 & 7).

## 2. Core Questions & Answers – Week 1 Discoveries

### Q1 — Why is multi-backend an architectural advantage?

Multi-backend is a major architectural win because it:

- **Decouples** model design from the computation engine  
- **Increases portability** across hardware/software ecosystems  
- **Improves maintainability** and long-term flexibility  
- **Allows future backend replacement** without rewriting user models

**Architecture keyword**: **Abstraction Layer**  
Keras = interface/abstraction  
Backends = pluggable implementation engines  
→ Classic **strategy pattern** / **bridge pattern** tactic (textbook Ch. 13)

### Q2 — Difference between Layer and Model abstraction

**Layer**  
- Small computational transformation unit  
- Examples: `Dense`, `Conv2D`, `LSTM`, `Activation`  
- Receives tensor → transforms tensor → has weights/parameters  

**Architectural role**: Fine-grained, reusable **component** (textbook Ch. 1: component in C&C view)

**Model**  
- Container / organizer of multiple layers  
- Defines forward graph, connects layers, manages training (loss, optimizer, fit loop)  

**Architectural role**: Composite **subsystem** / high-level **controller**  
→ **Composite pattern** + **orchestration** (textbook Ch. 1 & 13)

**Mental model**:

```
Layer   = function block  
Model   = workflow pipeline
```

### Q3 — Example of Module View in Keras (static structure)

Module View (Ch. 1) shows code organization & responsibilities.

Main top-level packages (observed via `pkgutil` style scans & repo knowledge in 2026):

- `keras.layers`       → reusable building blocks (Dense, Conv, etc.)  
- `keras.models`       → model classes (Sequential, Functional, subclassing)  
- `keras.optimizers`   → optimization algorithms (Adam, SGD, …)  
- `keras.losses`       → error measures (MSE, Crossentropy, …)  
- `keras.metrics`      → performance trackers (Accuracy, AUC, …)  
- `keras.backend`      → backend abstraction & ops dispatch  
- `keras.ops`          → unified operator API  
- `keras.utils`        → helpers (data, files, visualization)  
- `keras.datasets`     → toy datasets for quick testing  
- `keras.applications` → pre-trained reference models (ResNet, EfficientNet, …)

**One-line conclusion**: Clear **separation of concerns** — layered modular architecture (textbook Ch. 1).

### Q4 — Example of Runtime View in training (C&C perspective)

Typical training execution flow (Component-and-Connector view):

```
dataset batch
   ↓
model.forward pass (layers called sequentially/graph-wise)
   ↓
loss computation
   ↓
gradient computation (backpropagation)
   ↓
optimizer weight update
   ↓          ↻ (repeat)
```

→ **Pipeline + feedback control loop** architecture (textbook Ch. 1 & 13 patterns)

## 3. Recovered Module View Decomposition – Subsystem Responsibilities

(Recovered from static scans + tiny experiments)

| Subsystem                        | Key Components                        | Architectural Responsibility                              | Supported Quality Attributes (Ch. 2)          |
|----------------------------------|---------------------------------------|------------------------------------------------------------|-----------------------------------------------|
| Core Computation                 | layers, activations, initializers, regularizers, constraints | Mathematical processing engine; atomic transformations     | Modifiability, Reusability                    |
| Model Composition                | models, wrappers                      | Structural composition & orchestration control             | Modifiability, Integrability                  |
| Training Control                 | optimizers, losses, metrics, callbacks| Adaptive learning feedback control system                  | Performance, Testability                      |
| Backend & Execution Abstraction  | backend, ops, _tf_keras               | Platform/hardware decoupling (multi-backend bridge)        | Portability, Replaceability                   |
| Performance & Numerical Policy   | mixed_precision, dtype_policies, distribution | Resource efficiency & scalability governance               | Performance, Scalability                      |
| Data & Preprocessing             | datasets, preprocessing, random       | Input preparation pipeline                                 | Usability, Reproducibility                    |
| Model Lifecycle & Persistence    | saving, export, legacy                | System evolution & deployment continuity                   | Maintainability, Evolability                  |
| System Infrastructure Utilities  | utils, config, visualization, applications | Support & ecosystem infrastructure                         | Usability, Analyzability                      |

**Overall architectural style observed**: Layered + Modular + Pipeline with strong **information hiding** behind the backend abstraction layer (textbook Ch. 1 & 7).

## 4. Week 1 Deep Review – Key Insights

**Purpose of Keras**  
Before high-level frameworks: manual graphs, gradients, GPU kernels → high complexity.  
Keras solution: **human-centered high-level abstraction** → developer focuses on model structure, framework handles engine.

**Multi-backend power**  
→ **Decoupling interface from implementation** (like DB abstraction layers or OS drivers)  
→ Textbook: strong modifiability & portability tactic (Ch. 7)

**Three views applied** (Ch. 1)

- **Module View** — static decomposition, layered modular style  
- **Runtime / C&C View** — pipeline + feedback loop (training)  
- **Allocation View** — Python API → backend runtime → hardware (CPU/GPU)

**Patterns already visible** (Ch. 13)  
- Layered architecture  
- Composite pattern (Model over Layers)  
- Strategy pattern (optimizers, backends)  
- Adapter / Bridge (backend abstraction)  
- Feedback control loop (training)

**Mental model to keep**:

```
External Data
    ↓
Model Controller
    ↓
Layer Pipeline
    ↓
Backend Engine
    ↓
Hardware Execution

Training loop: Loss Feedback → Optimizer → Updated Model
```

## 5. Experiments Summary (tiny & reproducible)

- Static module scan → `pkgutil.iter_modules` → discovered subsystem boundaries  
- Micro training (`train_on_batch`) → observed stateful adaptive loop  
- Forward pass trace → extensibility via custom layers → **Open-Closed Principle**

## 6. GitHub / Documentation Action Items (Week 1)

1. **Issue**: `week1: initial module view decomposition and responsibilities`  
   Labels: architecture, documentation  
   Files: docs/architecture/week1-module-view.md

2. **PR**: `docs: add Week 1 notebook + initial module decomposition table`  
   Branch: `arch/week1`  
   ```bash
   git checkout -b arch/week1
   git add docs/week1.md
   git commit -m "docs: Week 1 notebook + module view summary"
   git push origin arch/week1
   ```

3. **Issue**: `arch: create mermaid templates for module, C&C, allocation views`  
   Labels: architecture, good first issue

## 7. Blockers & Next-week Focus

**Blockers**  
- None major — assuming Python 3.11+ and `pip install -e ".[all]"` working  
- If backend issues → default to `KERAS_BACKEND=jax` or `tensorflow`

**Week 2 / 10 Plan**  
- Deepen **C&C view**: trace `compile()` → `fit()` → backend delegation  
- First **mermaid diagrams**: Module graph + simple training sequence  
- Small experiment: custom layer + gradient tape peek  
- Start quality attribute scenario: modifiability (adding a backend)  
- Readings: textbook Ch. 1 finish + Ch. 7 (Modifiability)

