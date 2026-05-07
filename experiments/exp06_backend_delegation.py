import os
os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import keras
from keras import ops


def demonstrate_ops_delegation():
    """Calls keras.ops directly to show it routes to the active backend."""
    x = ops.ones((3, 3))
    y = ops.ones((3, 3))
    product = ops.matmul(x, y)
    activated = ops.relu(ops.subtract(product, ops.ones((3, 3))))
    return x, product, activated


if __name__ == "__main__":
    print("=== Experiment 6: Backend Delegation via keras.ops ===")
    backend = keras.backend.backend()
    print(f"Active backend: {backend}\n")

    x, product, activated = demonstrate_ops_delegation()

    print(f"ops.ones((3,3)) type:            {type(x).__name__}")
    print(f"ops.matmul result shape:         {tuple(product.shape)}")
    print(f"ops.relu(product - 1) shape:     {tuple(activated.shape)}")

    print("\nArchitectural finding:")
    print("  ops.ones, ops.matmul, ops.relu are all routed to the active backend.")
    print(f"  Returned tensor type is backend-specific: {type(x).__name__}")
    print("  But the caller uses only keras.ops -- no backend import required.")
    print("  This is the keras.ops abstraction boundary in action:")
    print("  Layer / Model -> keras.ops -> Backend (TF / JAX / PyTorch)")
    print("  Tactics: Encapsulate + Use an intermediary (Bass et al., Ch.7).")
