# Experiments

Each experiment produces empirical evidence for one architectural claim about Keras.
Run individually or all at once via `python main.py` from the repository root.

## Setup

```powershell
& .\.venv\Scripts\Activate.ps1
```

## Experiment Index

| File | Architectural claim validated |
|---|---|
| `exp01_module_scan.py` | Keras is decomposed into focused subsystems with clear responsibilities |
| `exp02_forward_trace.py` | Forward pass follows the delegation chain: Model → Layer → ops → Backend |
| `exp03_training_step.py` | Training is a stateful iterative feedback loop (Pipeline + Feedback Control Loop) |
| `exp04_gradient_flow.py` | Gradient computation is fully delegated to the backend; model code is backend-agnostic |
| `exp05_backend_switching.py` | Identical model code runs unchanged across backends; backend is a runtime configuration |
| `exp06_backend_delegation.py` | `keras.ops` routes all tensor operations to the active backend transparently |

## Running a Single Experiment

```powershell
python experiments/exp01_module_scan.py
```

## Switching the Backend

Set the `KERAS_BACKEND` environment variable before running:

```powershell
$env:KERAS_BACKEND = "jax"
python experiments/exp05_backend_switching.py
```

Valid values: `tensorflow`, `jax`, `torch` (requires corresponding package installed).

## Design Notes

- All experiments use only `keras.*` imports. No experiment imports a backend library directly (e.g., no `import tensorflow`), because the architectural claim being tested is that Keras is backend-agnostic. Using a backend import directly would contradict the claim.
- Each experiment prints an **Architectural finding** section at the end summarising what the output means architecturally.
- These experiments are the empirical foundation for the views in `views/` and the analysis in `findings/`.
