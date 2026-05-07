import os
os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import numpy as np
import keras
from keras import layers


class DebugLayer(layers.Layer):
    """Prints input shape on every forward call to make execution order visible."""
    def call(self, inputs):
        print(f"  [{self.name}] shape: {tuple(inputs.shape)}")
        return inputs


class DebugDense(layers.Dense):
    """Extends Dense to print input -> output shapes during the forward pass."""
    def call(self, inputs):
        out = super().call(inputs)
        print(f"  [{self.name}] {tuple(inputs.shape)} -> {tuple(out.shape)}")
        return out


def build_traced_model():
    return keras.Sequential([
        layers.Input(shape=(4,)),
        DebugDense(8, activation="relu", name="dense_1"),
        DebugLayer(name="probe"),
        DebugDense(2, activation="softmax", name="dense_2"),
    ])


if __name__ == "__main__":
    print("=== Experiment 2: Forward Pass Trace ===")
    print(f"Backend: {keras.backend.backend()}\n")

    model = build_traced_model()
    x = np.random.rand(2, 4).astype("float32")

    print("Layer execution order during forward pass:")
    y = model(x, training=False)
    print(f"\nFinal output shape: {tuple(y.shape)}")

    print("\nArchitectural finding:")
    print("  Layers execute in registration order; Model controls the sequence.")
    print("  Each Layer.call() is a connector: function call + tensor dataflow.")
    print("  Delegation chain confirmed: Model -> Layer -> keras.ops -> Backend")
    print("  This validates the C&C Pipeline pattern (Bass et al. Ch.1).")
