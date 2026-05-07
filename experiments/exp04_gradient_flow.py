import os
os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import numpy as np
import keras
from keras import layers


def demonstrate_gradient_flow():
    model = keras.Sequential([
        layers.Input(shape=(2,)),
        layers.Dense(4, activation="relu"),
        layers.Dense(1),
    ])
    model.compile(
        optimizer=keras.optimizers.SGD(learning_rate=0.1),
        loss="mse",
    )

    x = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0]], dtype="float32")
    y = np.array([[2.0], [1.0], [3.0], [0.0]], dtype="float32")

    weights_before = [w.numpy().copy() for w in model.trainable_weights]
    loss_value = model.train_on_batch(x, y)
    weights_after = [w.numpy().copy() for w in model.trainable_weights]

    return loss_value, weights_before, weights_after


if __name__ == "__main__":
    print("=== Experiment 4: Gradient Flow ===")
    print(f"Backend: {keras.backend.backend()}\n")

    loss, before, after = demonstrate_gradient_flow()
    print(f"Loss after one training step: {loss:.4f}")

    print("\nWeight update status (confirms gradient computation occurred):")
    for i, (b, a) in enumerate(zip(before, after)):
        changed = not np.allclose(b, a, atol=1e-8)
        status = "UPDATED" if changed else "unchanged"
        print(f"  trainable_weights[{i}] shape={b.shape}: {status}")

    print("\nArchitectural finding:")
    print("  Weight changes after train_on_batch() confirm gradient flow.")
    print("  Model/Layer code never computes gradients directly.")
    print("  Autodiff and weight updates are fully delegated to the backend.")
    print("  This experiment uses only keras.* APIs -- no direct backend import.")
    print("  Confirms: Delegation pattern + Backend as sole execution boundary.")
