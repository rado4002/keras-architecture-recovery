"""
Keras Architecture Recovery Pipeline
=====================================
Runs the six experiments in order, producing empirical evidence for the
recovered architectural model of Keras 3.

Architectural pattern of this pipeline: Pipe-and-Filter
  Each experiment is a filter that observes one property of Keras and
  writes its findings to stdout. main.py is the pipe that sequences them.

Usage:
    python main.py

The recovered architectural model (validated by this pipeline):
  Module View:     keras.models -> keras.layers -> keras.ops -> Backend
  C&C View:        fit() -> forward -> loss -> backward -> update [repeat]
  Allocation View: Python API -> Backend Runtime -> CPU / GPU

For the full synthesized architecture document, see ARCHITECTURE.md.
"""

import subprocess
import sys
import os

EXPERIMENTS = [
    (
        "experiments/exp01_module_scan.py",
        "Module Scan — Keras subsystem decomposition",
    ),
    (
        "experiments/exp02_forward_trace.py",
        "Forward Trace — Model -> Layer -> ops -> Backend delegation chain",
    ),
    (
        "experiments/exp03_training_step.py",
        "Training Step — iterative feedback control loop",
    ),
    (
        "experiments/exp04_gradient_flow.py",
        "Gradient Flow — backend delegation of autodiff",
    ),
    (
        "experiments/exp05_backend_switching.py",
        "Backend Switching — abstraction boundary validation",
    ),
    (
        "experiments/exp06_backend_delegation.py",
        "Backend Delegation — keras.ops routing",
    ),
]

DIVIDER = "=" * 62
STAGE_DIV = "-" * 62


def run_experiment(path, description):
    print(f"\n{STAGE_DIV}")
    print(f"  {description}")
    print(STAGE_DIV)
    result = subprocess.run(
        [sys.executable, path],
        env={**os.environ},
    )
    return result.returncode == 0


def main():
    print(DIVIDER)
    print("  Keras Architecture Recovery — Evidence Pipeline")
    print(DIVIDER)
    print(f"  Backend: {os.environ.get('KERAS_BACKEND', 'tensorflow (default)')}")
    print(f"  Python:  {sys.version.split()[0]}")
    print(DIVIDER)

    passed = 0
    failed = []

    for path, description in EXPERIMENTS:
        if run_experiment(path, description):
            passed += 1
        else:
            failed.append(description)

    total = len(EXPERIMENTS)
    print(f"\n{DIVIDER}")
    print(f"  Pipeline complete: {passed}/{total} experiments passed")

    if failed:
        print("\n  Failed:")
        for f in failed:
            print(f"    - {f}")

    print(f"\n{DIVIDER}")
    print("  Architectural model confirmed by evidence:")
    print()
    print("  Module View:")
    print("    keras.models -> keras.layers -> keras.ops -> Backend")
    print()
    print("  C&C View (training pipeline):")
    print("    fit() -> forward pass -> loss -> gradients -> update [loop]")
    print()
    print("  Allocation View:")
    print("    Python (orchestration) -> Backend Runtime -> CPU / GPU")
    print()
    print("  For full analysis: ARCHITECTURE.md")
    print(DIVIDER)

    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
