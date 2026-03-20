import tensorflow as tf
import keras


model = keras.Sequential([
    keras.layers.Dense(1)
])

optimizer = keras.optimizers.SGD(learning_rate=0.1)

x = tf.constant([[1.0], [2.0]])
y_true = tf.constant([[2.0], [4.0]])

with tf.GradientTape() as tape:
    y_pred = model(x)
    loss = tf.reduce_mean((y_pred - y_true) ** 2)

grads = tape.gradient(loss, model.trainable_variables)

print("Gradients:", grads)

optimizer.apply_gradients(zip(grads, model.trainable_variables))