import os
os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import numpy as np
import keras
from keras import layers, callbacks


class BatchLogger(callbacks.Callback):
    """Logs per-batch loss to make the training pipeline visible at runtime."""
    def on_train_batch_end(self, batch, logs=None):
        print(f"  batch {batch:>2d} -> loss: {logs.get('loss', 0.0):.4f}")


def build_and_train():
    model = keras.Sequential([
        layers.Input(shape=(4,)),
        layers.Dense(16, activation="relu"),
        layers.Dense(1),
    ])
    model.compile(optimizer="adam", loss="mse")

    x = np.random.rand(32, 4).astype("float32")
    y = np.random.rand(32, 1).astype("float32")
    model.fit(x, y, epochs=1, batch_size=8, callbacks=[BatchLogger()], verbose=0)
    return model


if __name__ == "__main__":
    print("=== Experiment 3: Training Step Trace ===")
    print(f"Backend: {keras.backend.backend()}\n")

    print("Pipeline: fit() -> forward -> loss -> backward -> update  [repeat]")
    print("Per-batch loss (shows iterative feedback loop):")
    build_and_train()

    print("\nArchitectural finding:")
    print("  Training is a stateful iterative feedback loop, not a single function call.")
    print("  model.fit() orchestrates all phases; the backend executes each one.")
    print("  Stages: forward pass -> loss computation -> gradient -> weight update.")
    print("  Confirms: Pipeline + Feedback Control Loop C&C pattern.")
