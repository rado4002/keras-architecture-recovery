# Week 02 Diagrams

This folder contains architecture views for the Keras recovery study in Week 02.

```mermaid
graph TD
User["User Code"]

Model["Model (Orchestrator)"]
Layer["Layer (Logic)"]
Ops["Ops (Abstraction)"]
Backend["Backend Engine"]
Autograd["Autograd"]
Optimizer["Optimizer"]
Kernel["Kernels"]
Hardware["CPU / GPU"]

User --> Model
Model --> Layer
Layer --> Ops
Ops --> Backend

Backend --> Kernel
Kernel --> Hardware

Backend --> Autograd
Autograd --> Kernel

Optimizer --> Backend
Backend --> Model
```

## Files

- `1.Module View-Dependency Discovery.md`
- `2.C&C View-Forward Pass Trace.md`
- `3.Full Training Cycle-Gradient Flow.md`
- `4.Allocation View-Device Detection.md`