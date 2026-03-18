import os

os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import keras
import numpy as np


def main():
    model = keras.Sequential(
        [
            keras.layers.Input(shape=(3,)),
            keras.layers.Dense(4),
        ]
    )

    model.compile(optimizer="adam", loss="mse")

    x = np.random.rand(2, 3).astype("float32")
    y = np.random.rand(2, 4).astype("float32")

    loss = model.train_on_batch(x, y)

    print("Keras backend:", keras.backend.backend())
    print("Loss:", float(loss))


if __name__ == "__main__":
    main()