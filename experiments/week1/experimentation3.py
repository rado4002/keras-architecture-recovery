import keras
import numpy as np

class DebugDense(keras.layers.Dense):
    def call(self, inputs):
        print("➡️ Layer forward execution:", self.name)
        return super().call(inputs)

model = keras.Sequential([
    keras.layers.Input(shape=(5,)),
    DebugDense(8, activation="relu"),
    DebugDense(3, activation="softmax")
])

x = np.random.rand(2, 5).astype("float32")

print("\n=== Running Forward Pass ===")
y = model(x)

print("Output shape:", y.shape)