# Recovering the Architecture of Keras

## Project Context

This repository contains a solo academic software architecture recovery project focused on analyzing and documenting the architecture of the open-source deep learning framework Keras.

The project is conducted as part of an introductory Software Architecture course.

## Why Keras

Keras is a suitable architecture-recovery target because it combines:
- Clean API-layer design (`Sequential`, Functional API, subclassing)
- Modular subsystem organization
- Runtime orchestration logic
- Backend and hardware abstraction

Modern Keras (Keras 3) supports multi-backend execution across TensorFlow, JAX, and PyTorch through a unified API surface.

## Project Objectives

The project aims to recover and explain Keras architecture from static and dynamic perspectives.

Primary goals:
- Recover the Module View (subsystems and dependencies)
- Recover the Component-and-Connector (C&C) View (runtime interactions)
- Recover the Allocation View (mapping to runtime/hardware)
- Identify architectural patterns used by Keras
- Build practical understanding of AI model execution pipelines

## Method

Architecture recovery is conducted iteratively each week:

1. Static analysis
  - Source/module exploration
  - Dependency observation
  - Subsystem identification
2. Dynamic analysis
  - Forward and training-step tracing
  - Runtime connector observation
  - Backend delegation evidence
3. Architectural synthesis
  - Diagrams
  - Responsibility mapping
  - Pattern interpretation
4. Documentation refinement
  - Weekly README updates
  - Interpretation improvements
  - QA and presentation artifacts

## Repository Structure

```text
keras-architecture-recovery/
├── docs/
│   ├── architecture-recovery-process.md
│   └── reusable-project-framework.md
├── weeks/
│   ├── week01/
│   ├── week02/
│   └── week03/
└── vendor/
   └── keras/
```

Each week contains:
- `README.md`
- `docs/`
- `diagrams/`
- `experiments/`
- `interpretation/`


## Weekly Progress

### Week 01 (Complete)

Focus:
- Initial architecture reconnaissance
- Core module discovery
- First runtime forward-flow observations

Main artifacts:
- `weeks/week01/README.md`
- `weeks/week01/experiments/README.md`

### Week 02 (Complete)

Focus:
- Dependency discovery (`layers -> ops -> backend`)
- Forward and backward training-step tracing
- Device/allocation mapping
- Architecture pattern interpretation

Main artifacts:
- `weeks/week02/README.md`
- `weeks/week02/experiments/README.md`

### Week 03 (In Progress)

Focus:
- C&C sequence and component views
- Backend delegation evidence
- Consolidated responsibility and pattern interpretation

Main artifacts:
- `weeks/week03/README.md`
- `weeks/week03/docs/Reading Note3.md`
- `weeks/week03/diagrams/README.md`
- `weeks/week03/experiments/README.md`
- `weeks/week03/interpretation/Responsibilities, Patterns, and Findings.md`

## Current State Snapshot

- Week 01 and Week 02 are complete.
- Week 03 core artifacts (docs, diagrams, experiments, interpretation) are produced and being refined.
- The project now contains per-folder README files for experiment and diagram navigation in active weeks.

## Learning Outcomes Targeted

By project completion, expected outcomes are:
- Stronger architecture-analysis skills on large frameworks
- Practical understanding of deep learning runtime execution
- Experience with architecture recovery workflows
- Portfolio-grade technical documentation and evidence artifacts

