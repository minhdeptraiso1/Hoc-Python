"""
===============================================================================
                   PYTORCH ADVANCED: CNN + RNN
Gồm:
✔ CNN – Convolutional Neural Network (MNIST)
✔ RNN – Recurrent Neural Network (Text Classification demo)
===============================================================================
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# ============================= CNN =============================

print("\n===== CNN TRAINING ON MNIST =====")

# Dataset
transform = transforms.ToTensor()
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST(".", train=True, download=True, transform=transform),
    batch_size=64, shuffle=True
)

# CNN Model
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 32, 3),   # 28→26
            nn.ReLU(),
            nn.MaxPool2d(2),      # 26→13
            nn.Conv2d(32, 64, 3), # 13→11
            nn.ReLU(),
            nn.MaxPool2d(2),      # 11→5
            nn.Flatten(),
            nn.Linear(64 * 5 * 5, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        return self.model(x)

cnn = CNN()
optimizer = optim.Adam(cnn.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Train 1 batch (demo)
for img, lbl in train_loader:
    pred = cnn(img)
    loss = criterion(pred, lbl)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    break

print("CNN trained on 1 batch!")


# ============================= RNN =============================

print("\n===== SIMPLE RNN EXAMPLE =====")

class SimpleRNN(nn.Module):
    def __init__(self, input_size=10, hidden_size=20, output_size=2):
        super().__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        output, hidden = self.rnn(x)
        return self.fc(hidden[-1])

rnn = SimpleRNN()
sample = torch.randn(1, 5, 10)  # batch=1, seq=5, features=10
print("RNN output:", rnn(sample))
