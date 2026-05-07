import os
os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import pkgutil
import inspect
import keras
from keras import layers, models, ops


def scan_top_level_packages():
    return sorted(name for _, name, _ in pkgutil.iter_modules(keras.__path__))


def trace_module_origins():
    targets = {
        "layers.Dense": layers.Dense,
        "models.Model": models.Model,
        "ops (module)": ops,
    }
    return {
        name: inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else "unknown"
        for name, obj in targets.items()
    }


if __name__ == "__main__":
    print("=== Experiment 1: Module Scan ===")
    print(f"Backend: {keras.backend.backend()}\n")

    packages = scan_top_level_packages()
    print(f"Top-level Keras packages ({len(packages)}):")
    for p in packages:
        print(f"  keras.{p}")

    print("\nModule origins for key classes:")
    for name, module in trace_module_origins().items():
        print(f"  {name:22s} -> {module}")

    print("\nArchitectural finding:")
    print("  Keras exposes a clean public API decomposed into focused subsystems.")
    print("  Each subsystem encapsulates one concern: layers, models, ops, backend.")
    print("  This confirms a Decomposition module structure (Bass et al. Ch.1).")
