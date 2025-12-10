"""
===============================================================================
               REINFORCEMENT LEARNING – Q-Learning & DQN (Deep Q Network)
Giúp em hiểu trí tuệ tăng cường (Reinforcement Learning – RL)

RL là nền tảng của robot, game AI, tự động điều khiển, ChatGPT RLHF,…
===============================================================================
"""

import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim


# ============================================================================
# 1) Q-LEARNING (tabular RL)
# ============================================================================

print("\n===== Q-LEARNING =====")

# environment: GridWorld 1D: state 0 → 4, goal at 4
n_states = 5
n_actions = 2  # 0: left, 1: right
Q = np.zeros((n_states, n_actions))

alpha = 0.1   # learning rate
gamma = 0.99  # discount
epsilon = 0.1

def step(state, action):
    if action == 1:
        nxt = min(state + 1, 4)
    else:
        nxt = max(state - 1, 0)
    reward = 1 if nxt == 4 else 0
    return nxt, reward

for episode in range(200):
    s = 0
    for t in range(20):
        a = np.argmax(Q[s]) if random.random() > epsilon else random.randint(0, 1)
        nxt, r = step(s, a)
        Q[s, a] += alpha * (r + gamma * np.max(Q[nxt]) - Q[s, a])
        s = nxt
        if s == 4:
            break

print("Q-table:\n", Q)


# ============================================================================
# 2) DEEP Q NETWORK (DQN)
# ============================================================================

print("\n===== DQN (Deep Q Network) =====")

class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 32),
            nn.ReLU(),
            nn.Linear(32, 2)
        )

    def forward(self, x):
        return self.net(x)

dqn = DQN()
optimizer = optim.Adam(dqn.parameters(), lr=0.001)
criterion = nn.MSELoss()

# Train demo for a few steps
state = torch.tensor([[0.0]])

for _ in range(10):
    q_values = dqn(state)
    target = q_values.clone()
    target[0][1] = 1.0  # pretend: action "right" is good
    loss = criterion(q_values, target)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("DQN training demo complete!")
