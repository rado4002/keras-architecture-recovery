import os

os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import numpy as np
import keras
from keras import layers


def main():
	print("Keras backend:", keras.backend.backend())
	print("Keras path:", keras.__file__)

	x = np.random.random((1000, 20)).astype("float32")
	y = np.random.randint(0, 3, size=(1000,)).astype("int32")

	model = keras.Sequential(
		[
			layers.Input(shape=(20,)),
			layers.Dense(64, activation="relu"),
			layers.Dense(3, activation="softmax"),
		]
	)

	model.compile(
		optimizer="adam",
		loss="sparse_categorical_crossentropy",
		metrics=["accuracy"],
	)

	model.fit(x, y, epochs=3, batch_size=32, verbose=2)

	preds = model.predict(x[:2], verbose=0)
	print("Predictions for 2 samples:\n", preds)


if __name__ == "__main__":
	main()    
