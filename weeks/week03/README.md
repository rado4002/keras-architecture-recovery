# Week 03 - Keras Architecture Recovery

## Week Objective

Week 03 focuses on recovering the Component-and-Connector (C&C) architecture of Keras through small controlled experiments and architectural interpretation.

Main goals:
- Trace runtime behavior of training.
- Identify component responsibilities and interaction patterns.
- Explain backend delegation and execution mapping.

## Week Scope

This week emphasizes three viewpoints:

1. Runtime behavior (sequence of interactions during training)
2. Runtime structure (components and dependencies)
3. Architectural interpretation (responsibilities, patterns, findings)

## Folder Overview

- `docs/`: reading and theory notes for Week 03
- `diagrams/`: C&C diagrams with explanations
- `experiments/`: runnable scripts used as architectural evidence
- `interpretation/`: synthesized architectural analysis


## Key Artifacts

### Reading Notes

- `docs/Reading Note3.md`

### Diagrams

- `diagrams/1.C&C View — Sequence Diagram.md`
	- Runtime training flow: forward, loss, backward, update
- `diagrams/2.C&C View — Component Diagram.md`
	- Runtime components and dependency structure
- `diagrams/README.md`
	- Diagram index and usage guidance

### Experiments

- `experiments/experiments1-Minimal Training Step Trace`
	- Minimal fit trace with batch-level loss logging
- `experiments/Experiment2-Backend_Delegation`
	- Small `keras.ops` matmul to show backend delegation
- `experiments/README.md`
	- Experiment index, goals, expected outputs, and run commands

### Interpretation

- `interpretation/Responsibilities, Patterns, and Findings.md`
	- Consolidated architectural analysis for Week 03

## How to Reproduce Week 03 Evidence

Run from repository root:

```powershell
& .\.venv\Scripts\Activate.ps1
python "weeks/week03/experiments/experiments1-Minimal Training Step Trace"
python "weeks/week03/experiments/Experiment2-Backend_Delegation"
```

## Week 03 Findings Snapshot

- Training behaves as a structured runtime pipeline.
- The model orchestrates; backend executes computation.
- `keras.ops` provides backend abstraction.
- Component boundaries support modularity and backend portability.

## Current Status

In progress.

Completed in this week so far:
- C&C sequence and component diagrams documented
- Initial runtime experiments executed
- Responsibilities and architectural patterns interpreted

Next expected steps:
- Expand experiments to include more complex model flow
- Add QA checks and validation notes
- Finalize slide-ready synthesis
