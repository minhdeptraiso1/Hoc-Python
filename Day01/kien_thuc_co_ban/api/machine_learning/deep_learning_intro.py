"""
===============================================================================
                   DEEP LEARNING CƠ BẢN — PyTorch + TensorFlow
Gồm:
✔ MLP (Neural Network) với PyTorch
✔ MLP với TensorFlow / Keras
✔ Train đơn giản trên MNIST (subset)
===============================================================================
"""

# ========================= PYTORCH ============================

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

print("\n===== PYTORCH MODEL =====")

# Dataset
transform = transforms.ToTensor()
train_set = datasets.MNIST(root=".", train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

# Model
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        return self.layer(x)

model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train 1 epoch
for images, labels in train_loader:
    out = model(images)
    loss = criterion(out, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    break  # train demo 1 batch

print("PyTorch model trained 1 batch successfully!")


# ========================= TENSORFLOW ==========================

print("\n===== TENSORFLOW / KERAS MODEL =====")

import tensorflow as tf
from tensorflow.keras import layers

# Load MNIST
(train_x, train_y), _ = tf.keras.datasets.mnist.load_data()
train_x = train_x / 255.0

# Build model
tf_model = tf.keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])

tf_model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
tf_model.fit(train_x[:1000], train_y[:1000], epochs=1)  # train nhanh demo

print("TensorFlow model trained 1 epoch successfully!")
