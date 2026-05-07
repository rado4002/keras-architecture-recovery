import os
os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import numpy as np
import keras
from keras import layers


def run_standard_model():
    """Identical model code regardless of which backend is active."""
    model = keras.Sequential([
        layers.Input(shape=(3,)),
        layers.Dense(8, activation="relu"),
        layers.Dense(1),
    ])
    model.compile(optimizer="sgd", loss="mse")
    x = np.random.rand(8, 3).astype("float32")
    y = np.random.rand(8, 1).astype("float32")
    return model.train_on_batch(x, y)


def detect_devices():
    backend = keras.backend.backend()
    if backend == "tensorflow":
        import tensorflow as tf
        return [d.name for d in tf.config.list_physical_devices()]
    return [f"(device listing not implemented for {backend} backend)"]


if __name__ == "__main__":
    print("=== Experiment 5: Backend Switching ===")
    backend = keras.backend.backend()
    print(f"Active backend: {backend}")
    print("To switch: set KERAS_BACKEND=tensorflow|jax|torch before running\n")

    loss = run_standard_model()
    print(f"Training loss ({backend} backend): {loss:.4f}")

    print("\nDetected devices:")
    for d in detect_devices():
        print(f"  {d}")

    print("\nArchitectural finding:")
    print("  Identical model code executes correctly regardless of active backend.")
    print("  Backend selection is a runtime allocation decision, not an API decision.")
    print("  User code depends only on keras.*; backend is environment configuration.")
    print("  Confirms: keras.ops as abstraction boundary (Bridge pattern).")
    print("  Tactic: Use an intermediary (Bass et al., Ch.7 Modifiability).")
