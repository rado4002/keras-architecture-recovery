# Week 03 Experiments

This folder contains runnable experiments used as evidence for Week 03 architecture recovery.

## Purpose

The experiments are designed to observe:
- Runtime training flow in Keras (`forward -> loss -> backward -> update`)
- Backend delegation through `keras.ops`

## Files in This Folder

### 1) experiments1-Minimal Training Step Trace

Goal:
- Trace a minimal training step with per-batch debug output.

What it does:
- Builds a small sequential model.
- Compiles with Adam and MSE.
- Trains for one epoch on synthetic data.
- Prints batch-level loss values using a custom callback.

Expected output signals:
- Batch logs such as `Batch 0 -> loss: ...`
- A short Keras fit progress summary.

### 2) Experiment2-Backend_Delegation

Goal:
- Verify that numerical operations can be routed through `keras.ops`.

What it does:
- Creates two small tensors with `keras.ops.ones`.
- Runs matrix multiplication with `ops.matmul`.
- Prints the resulting tensor.

Expected output signals:
- A 2x2 tensor result from matrix multiplication.

## How to Run

Run commands from the repository root.

1. Activate the local environment:

```powershell
& .\.venv\Scripts\Activate.ps1
```

2. Run experiment 1:

```powershell
python "weeks/week03/experiments/experiments1-Minimal Training Step Trace"
```

3. Run experiment 2:

```powershell
python "weeks/week03/experiments/Experiment2-Backend_Delegation"
```

## Notes

- These files are executable Python scripts without a `.py` extension.
- Keep experiments small and focused so each run isolates one architectural observation.
- Record findings in `weeks/week03/interpretation/Responsibilities, Patterns, and Findings.md`.
