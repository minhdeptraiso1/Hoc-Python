"""
===============================================================================
                             NLP NÂNG CAO
Gồm:
✔ RNN
✔ LSTM
✔ Transformer (PyTorch)
Giúp em hiểu các mô hình xử lý ngôn ngữ tự nhiên:

✔ RNN – xử lý chuỗi (sequence)
✔ LSTM – ghi nhớ dài hạn, nền tảng của ChatGPT đời đầu
✔ Transformer – kiến trúc đứng sau ChatGPT, BERT, GPT-4, Gemini…
===============================================================================
"""

import torch
import torch.nn as nn


# ========================== RNN ==========================

print("\n===== SIMPLE RNN =====")

rnn = nn.RNN(input_size=10, hidden_size=20, batch_first=True)
x = torch.randn(1, 5, 10)
output, hidden = rnn(x)
print("RNN output:", output.shape)


# ========================== LSTM ==========================

print("\n===== LSTM =====")

lstm = nn.LSTM(input_size=10, hidden_size=20, batch_first=True)
output, (h, c) = lstm(x)
print("LSTM hidden state:", h.shape)


# ========================== Transformer ==========================

print("\n===== TRANSFORMER ENCODER =====")

encoder_layer = nn.TransformerEncoderLayer(d_model=32, nhead=4)
transformer = nn.TransformerEncoder(encoder_layer, num_layers=2)

inp = torch.randn(5, 1, 32)  # seq=5, batch=1, features=32
out = transformer(inp)

print("Transformer output:", out.shape)
