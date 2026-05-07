# Keras Architecture Recovery

A software architecture recovery study of Keras 3, applying the three-view framework
from Bass, Clements, Kazman — *Software Architecture in Practice*.

**Start here:** [ARCHITECTURE.md](ARCHITECTURE.md) — the complete recovered architecture.

---

## What This Project Does

Keras is a high-level deep learning API written in Python that runs on top of TensorFlow,
JAX, or PyTorch. It provides a unified interface for building and training neural networks
while delegating all tensor computation to a swappable backend.

This project recovers and documents the software architecture of Keras 3 using three
complementary views (Module, C&C, Allocation) and validates every claim with a runnable
experiment.

---

## Repository Structure

```
keras-architecture-recovery/
│
├── ARCHITECTURE.md        ← Read this first — complete recovered architecture
├── main.py                ← Runs all experiments to validate architectural claims
│
├── experiments/           ← Empirical evidence (6 Python scripts)
├── views/                 ← Canonical architectural views (3 Mermaid diagrams)
├── findings/              ← Synthesized analysis (components, patterns, QA, decisions)
├── docs/                  ← Project context, methodology, quality concerns
└── vendor/keras/          ← Keras 3 source (read-only reference)
```

---

## Quick Start

```powershell
& .\.venv\Scripts\Activate.ps1
python main.py
```

This runs all six experiments in sequence and prints the confirmed architectural model.

---

## Reading Path

| Step | File | Time |
|---|---|---|
| 1 | [ARCHITECTURE.md](ARCHITECTURE.md) | ~10 min — full architecture |
| 2 | [views/module-view.md](views/module-view.md) | ~5 min — static structure |
| 3 | [views/cnc-view.md](views/cnc-view.md) | ~5 min — runtime pipeline |
| 4 | [views/allocation-view.md](views/allocation-view.md) | ~3 min — execution mapping |
| 5 | [findings/qa-scenarios.md](findings/qa-scenarios.md) | ~5 min — formal QA scenarios |
| 6 | [findings/design-decisions.md](findings/design-decisions.md) | ~5 min — 7-category decisions |

---

## Recovered Architectural Model (Summary)

**Module View — dependency chain:**
```
keras.models  ->  keras.layers  ->  keras.ops  ->  Backend (TF / JAX / PyTorch)
```

**C&C View — training pipeline:**
```
fit()  ->  forward pass  ->  loss  ->  gradients  ->  weight update  ->  [repeat]
```

**Allocation View — execution tiers:**
```
Python (orchestration)  ->  keras.ops (boundary)  ->  Backend Runtime  ->  CPU / GPU
```

---

## Key Quality Attributes

| Attribute | How Keras achieves it |
|---|---|
| **Modifiability** | `keras.ops` abstraction boundary isolates backend from model code |
| **Portability** | Backend bound at runtime via `KERAS_BACKEND`; zero code changes to switch |
| **Maintainability** | Strict layered dependency direction; one responsibility per level |

---

## Project Context

| Topic | File |
|---|---|
| Project scope and subject selection | [docs/project-description.md](docs/project-description.md) |
| Business context and stakeholders | [docs/business-context.md](docs/business-context.md) |
| Key quality concerns | [docs/key-quality-concerns.md](docs/key-quality-concerns.md) |
| Recovery methodology | [docs/methodology.md](docs/methodology.md) |
| Early architecture design decisions | [findings/design-decisions.md](findings/design-decisions.md) |
| Quality attribute scenarios | [findings/qa-scenarios.md](findings/qa-scenarios.md) |
| Patterns and tactics | [findings/patterns.md](findings/patterns.md) |
