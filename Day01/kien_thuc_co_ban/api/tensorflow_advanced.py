"""
===============================================================================
                       TENSORFLOW – FUNCTIONAL API
Gồm:
✔ Functional API (thay cho Sequential)
✔ Mô hình CNN Functional
✔ Multiple Inputs / Outputs demo
===============================================================================
"""

import tensorflow as tf
from tensorflow.keras import layers, Model

print("\n===== FUNCTIONAL API – CNN =====")

inputs = layers.Input(shape=(28, 28, 1))

x = layers.Conv2D(32, 3, activation="relu")(inputs)
x = layers.MaxPool2D()(x)
x = layers.Conv2D(64, 3, activation="relu")(x)
x = layers.MaxPool2D()(x)
x = layers.Flatten()(x)

dense = layers.Dense(128, activation="relu")(x)
outputs = layers.Dense(10, activation="softmax")(dense)

model = Model(inputs, outputs)
model.summary()

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Load MNIST
(train_x, train_y), _ = tf.keras.datasets.mnist.load_data()
train_x = train_x.reshape(-1, 28, 28, 1) / 255.0

model.fit(train_x[:5000], train_y[:5000], epochs=1)  # train demo


# ================= MULTI-INPUT / MULTI-OUTPUT =================

print("\n===== MULTI INPUT / OUTPUT MODEL =====")

input1 = layers.Input(shape=(10,))
input2 = layers.Input(shape=(5,))

x1 = layers.Dense(16, activation="relu")(input1)
x2 = layers.Dense(8, activation="relu")(input2)

concat = layers.concatenate([x1, x2])
output1 = layers.Dense(1)(concat)
output2 = layers.Dense(3, activation="softmax")(concat)

multi_model = Model(inputs=[input1, input2], outputs=[output1, output2])
multi_model.summary()
