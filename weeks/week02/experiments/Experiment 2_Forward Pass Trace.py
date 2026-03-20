import keras
import numpy as np
from keras import layers


class DebugLayer(layers.Layer):
    def call(self, inputs):
        print("Inside DebugLayer:", inputs.shape)
        return inputs * 2


model = keras.Sequential([
    layers.Dense(4),
    DebugLayer(),
    layers.Dense(1)
])

x = np.random.rand(2, 3)
y = model(x)

print("Final output:", y.shape)