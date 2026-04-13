# Week 04 - Keras Architecture Recovery

## Week Objective

Week 04 focuses on documenting Keras architecture using complete multi-view representation and quality-attribute reasoning.

Main goals:
- Consolidate Module, C&C, and Allocation views
- Improve architecture documentation quality (view completeness and rationale)
- Analyze modifiability tactics in Keras multi-backend design

## Week Scope

This week emphasizes three architecture viewpoints:

1. Module structure (static dependencies)
2. Runtime behavior (C&C sequence interactions)
3. Allocation mapping (software to runtime/hardware)

## Folder Overview

- `docs/`: week reading and synthesis notes
- `diagrams/`: diagram artifacts and interpretation
- `experiments/`: reproducible checks and small validation scripts
- `interpretation/`: consolidated architecture findings

## Key Artifacts

### Reading Notes

- `docs/Reading Note4.md`

### Diagrams

- `diagrams/1.Module View.md`
  - Static layered dependencies (`Model -> Layer -> Ops -> Backend`)
- `diagrams/2.C&C View Runtime Diagram.md`
  - Runtime training flow and interaction loop
- `diagrams/3. Allocation View (Execution Mapping).md`
  - Software-to-runtime/hardware mapping (Python, backend, CPU/GPU)
- `diagrams/README.md`
  - Diagram index and usage guidance

### Experiments

- `experiments/experiments1-backend switching`
  - Backend-switching evidence artifact
- `experiments/README.md`
  - Experiment index and run notes (to be expanded)

### Interpretation

- `interpretation/Responsibilities, Patterns, and Findings.md`
  - Week 04 synthesized architecture analysis (in progress)

## How to Reproduce Week 04 Evidence

Run from repository root:

```powershell
& .\.venv\Scripts\Activate.ps1
python "weeks/week04/experiments/experiments1-backend switching"
```

## Week 04 Findings Snapshot

- Keras architecture must be documented with multiple complementary views.
- `keras.ops` is a key abstraction boundary for backend independence.
- Modifiability is supported through separation of concerns and indirection.
- Allocation mapping explains portability and performance differences.

## Current Status

In progress.

Completed in this week so far:
- Reading note restructured and finalized
- Three core diagrams documented with interpretation
- Diagram index (`diagrams/README.md`) completed

Next expected steps:
- Expand experiments and fill `experiments/README.md`
- Complete interpretation synthesis in `interpretation/Responsibilities, Patterns, and Findings.md`
- Normalize Week 04 file naming for full consistency
