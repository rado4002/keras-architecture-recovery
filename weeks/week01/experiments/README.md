# Week 01 Experiments

This folder contains the initial hands-on experiments used for Week 01 architecture reconnaissance.

## Folder Objective

These experiments were created to build first evidence for:
- Basic Keras training workflow
- Module-level structure discovery
- Minimal training-step behavior
- Forward-pass execution tracing

## Experiment Index

### 1) experimentation.py

Purpose:
- Run a complete minimal training pipeline with Keras.

What it does:
- Sets backend to TensorFlow (if not already set).
- Builds a small sequential classifier.
- Compiles and trains with `model.fit()`.
- Runs a small prediction call.

Expected output:
- Printed backend and Keras path
- Epoch logs with loss and accuracy
- Prediction probabilities for two samples

### 2) experimentation1.py

Purpose:
- Discover top-level Keras modules for static architecture mapping.

What it does:
- Uses `pkgutil.iter_modules(keras.__path__)`.
- Prints top-level modules available in the installed Keras package.

Expected output:
- List of module names (for example `layers`, `models`, `ops`, etc.)

### 3) experimentation2.py

Purpose:
- Observe one manual training step with `train_on_batch()`.

What it does:
- Builds a minimal model.
- Compiles with Adam and MSE.
- Executes `train_on_batch` on small synthetic data.
- Prints backend and resulting batch loss.

Expected output:
- Printed backend name
- A numeric loss value

### 4) experimentation3.py

Purpose:
- Trace forward-pass execution through custom instrumented layers.

What it does:
- Defines `DebugDense`, a subclass of `keras.layers.Dense`.
- Prints a message whenever a layer `call()` executes.
- Runs a forward pass and prints output shape.

Expected output:
- Layer execution trace lines
- Final output tensor shape

## How to Run

Run commands from repository root.

1. Activate environment:

```powershell
& .\.venv\Scripts\Activate.ps1
```

2. Run all Week 01 experiments:

```powershell
python "weeks/week01/experiments/experimentation.py"
python "weeks/week01/experiments/experimentation1.py"
python "weeks/week01/experiments/experimentation2.py"
python "weeks/week01/experiments/experimentation3.py"
```

## Suggested Evidence Capture

For each script, record:
- Main output signals
- What architectural behavior it confirms
- Any open questions for later weeks

## Relationship to Week 01 Deliverables

These experiments support:
- `weeks/week01/README.md`
- Week 01 architectural reconnaissance notes and diagrams
- Early C&C and module-view recovery work
