# Week 04 Experiments

This folder contains runnable experiments used as evidence for Week 04 architecture recovery.

## Folder Objective

Week 04 experiments are focused on validating modifiability and backend abstraction behavior in Keras.

The main question is:
- Can the same high-level model/training code run while backend selection changes?

## Experiment Index

### 1) experiments1-backend switching

Purpose:
- Validate backend selection and runtime execution path in a minimal training step.

What it does:
- Sets `KERAS_BACKEND` with an environment variable (currently `tensorflow`; can switch to `jax`).
- Builds a small `Sequential` model.
- Compiles with `sgd` and `mse`.
- Runs `train_on_batch` on synthetic NumPy data.
- Prints the active backend from Keras.

Expected observation:
- Script runs successfully without changing model code.
- Printed line confirms active backend, for example:

```text
Backend: tensorflow
```

Architectural evidence:
- Supports `Model -> Layer -> ops -> Backend` delegation logic.
- Demonstrates backend abstraction and modifiability-oriented design.

## How to Run

Run commands from repository root.

1. Activate virtual environment:

```powershell
& .\.venv\Scripts\Activate.ps1
```

2. Run experiment:

```powershell
python "weeks/week04/experiments/experiments1-backend switching"
```

## Optional Backend Switch Test

Inside `experiments1-backend switching`, change:

```python
os.environ["KERAS_BACKEND"] = "tensorflow"
```

to:

```python
os.environ["KERAS_BACKEND"] = "jax"
```

Then run the same command again and compare the printed backend output.

## Notes

- This experiment file is an executable Python script without a `.py` extension.
- Keep this experiment minimal; its goal is architectural evidence, not model accuracy.
- Record output evidence in:
	- `weeks/week04/README.md`
	- `weeks/week04/interpretation/Responsibilities, Patterns, and Findings.md`

## Common Issues

- If backend import fails, verify that required packages are installed in the active environment.
- If JAX backend is unavailable, keep `tensorflow` as baseline and record limitation in interpretation notes.
