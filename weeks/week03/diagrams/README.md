# Week 03 Diagrams

This folder contains the visual artifacts used to recover the Component-and-Connector (C&C) architecture of Keras during Week 03.

## Folder Purpose

The diagrams provide complementary views of the same training system:

- Behavior view: how runtime interactions happen step by step.
- Structure view: what runtime components exist and how they are connected.

Together, they support architectural interpretation, responsibility mapping, and pattern identification.

## Contents

### 1) `1.C&C View — Sequence Diagram.md`

Primary focus:
- Runtime behavior of a training step.
- Interaction flow across `Model`, `Layer`, `Loss`, `Optimizer`, and `Backend`.

What it shows:
- Control flow and data flow during training.
- Ordered phases: forward pass, loss computation, backward pass, and parameter update.
- Delegation of numerical execution to backend operations.

Use this file when you need to answer:
- "What happens first, next, and last during training?"
- "Where are gradients computed and applied?"

### 2) `2.C&C View — Component Diagram.md`

Primary focus:
- Runtime component structure.
- Dependency relationships among major training components.

What it shows:
- The `Model` as orchestration hub.
- `keras.ops` as abstraction between high-level components and backend engines.
- Shared backend dependency for layers, loss, and optimizer logic.

Use this file when you need to answer:
- "Which components exist in the runtime architecture?"
- "How are responsibilities and dependencies distributed?"

## Recommended Reading Order

1. Read the sequence diagram first to understand runtime behavior.
2. Read the component diagram next to understand structural relationships.
3. Cross-check both views in interpretation notes to derive architectural findings.

## Relationship to Week 03 Deliverables

These diagrams are evidence artifacts for:
- C&C recovery
- architectural pattern identification
- responsibility analysis
- backend delegation reasoning

They are intended to be referenced by:
- `weeks/week03/docs/Reading Note3.md`
- `weeks/week03/interpretation/Responsibilities, Patterns, and Findings.md`
