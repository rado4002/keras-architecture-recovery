# Week 02 Experiments

This folder contains runnable experiments used to recover Keras architecture in Week 02.

## Folder Objective

The experiments provide evidence for:
- Static dependency discovery
- Forward-pass runtime tracing
- Backward-pass and gradient update flow
- Allocation and device visibility

## Experiment Index

### 1) Experiment 1_Dependency Discovery.py

Purpose:
- Identify where core Keras APIs come from at module level.

What it checks:
- Module path of `layers.Dense`
- Module path of `models.Model`
- Module path of `keras.ops`

Expected observation:
- Printed module origins that help map dependency direction (`layers`, `models`, `ops`, backend).

### 2) Experiment 2_Forward Pass Trace.py

Purpose:
- Trace data flow through a simple model during forward execution.

What it does:
- Defines a custom `DebugLayer`.
- Builds `Dense -> DebugLayer -> Dense` model.
- Prints intermediate shape inside `DebugLayer`.
- Prints final output shape.

Expected observation:
- Runtime trace showing layer execution order and tensor shape flow.

### 3) Experiment 3_Manual Training Step.py

Purpose:
- Recover a minimal backward pass and optimizer update flow.

What it does:
- Creates a one-layer model.
- Uses `tf.GradientTape` to compute loss and gradients.
- Prints gradients.
- Applies updates with `SGD`.

Expected observation:
- Non-empty gradients for trainable variables.
- Successful optimizer application (`apply_gradients`).

### 4) Experiment 4_Device Detection.py

Purpose:
- Identify available physical devices for execution mapping.

What it does:
- Prints `tf.config.list_physical_devices()`.

Expected observation:
- Device list (typically CPU, optionally GPU if configured).

## How to Run

Run from repository root.

1. Activate environment:

```powershell
& .\.venv\Scripts\Activate.ps1
```

2. Run all experiments in order:

```powershell
python "weeks/week02/experiments/Experiment 1_Dependency Discovery.py"
python "weeks/week02/experiments/Experiment 2_Forward Pass Trace.py"
python "weeks/week02/experiments/Experiment 3_Manual Training Step.py"
python "weeks/week02/experiments/Experiment 4_Device Detection.py"
```

## Suggested Evidence Capture

For each run, record in Week 02 interpretation notes:
- Key printed output
- What architectural property it confirms
- Any mismatch from expected behavior

## Relationship to Week 02 Outputs

These experiments support:
- `weeks/week02/README.md` (weekly summary)
- Week 02 diagrams and interpretation artifacts
- C&C and allocation analysis for Keras architecture recovery
