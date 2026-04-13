# Week 04 Diagrams

This folder contains the architecture diagram artifacts for Week 04 of the Keras architecture recovery project.

## Folder Purpose

Week 04 emphasizes complete architecture representation across multiple views:
- Module view: static dependency structure
- C&C view: runtime interaction flow
- Allocation view: execution mapping to runtime and hardware

Together, these files support architecture documentation quality and modifiability analysis.

## Contents

### 1) [1.Module View.md](1.Module%20View.md)

Primary focus:
- Static dependency direction in Keras
- Layered responsibility boundaries

What it shows:
- `Model -> Layer -> Ops -> Backend`
- Separation of concerns and information hiding

### 2) [2.C&C View Runtime Diagram.md](2.C&C%20View%20Runtime%20Diagram.md)

Primary focus:
- Runtime training behavior in sequence form

What it shows:
- Forward-path and return-path interactions
- Delegation from high-level API to backend execution
- Iterative training loop with parameter updates

### 3) [3. Allocation View (Execution Mapping)](3.%20Allocation%20View%20(Execution%20Mapping))

Primary focus:
- Mapping software elements to runtime engines and hardware

What it shows:
- Python orchestration vs backend execution
- CPU/GPU execution boundary
- Why backend choice affects performance and portability

## Recommended Reading Order

1. Read the module view first to understand static structure.
2. Read the C&C runtime view second to understand dynamic behavior.
3. Read the allocation view third to understand where execution occurs.
4. Cross-check all three views in [weeks/week04/docs/Reading Note4.md](../docs/Reading%20Note4.md).

## Week 04 Deliverable Connection

These diagrams are evidence artifacts for:
- Multi-view architecture documentation
- Modifiability reasoning
- Responsibility and dependency analysis
- Execution mapping and deployment-oriented interpretation
