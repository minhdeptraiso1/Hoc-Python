"""
===============================================================================
                TRANSFORMER DECODER — XÂY MỘT CHATGPT MINI
===============================================================================
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math


# ====================== POSITONIAL ENCODING ======================

class PositionalEncoding(nn.Module):
    def __init__(self, dim, max_len=5000):
        super().__init__()
        pe = torch.zeros(max_len, dim)
        position = torch.arange(0, max_len).unsqueeze(1)

        div = torch.exp(torch.arange(0, dim, 2) * (-math.log(10000.0) / dim))

        pe[:, 0::2] = torch.sin(position * div)
        pe[:, 1::2] = torch.cos(position * div)

        self.pe = pe.unsqueeze(0)

    def forward(self, x):
        return x + self.pe[:, :x.size(1)]


# ====================== DECODER BLOCK ======================

class DecoderBlock(nn.Module):
    def __init__(self, dim, heads):
        super().__init__()
        self.attn = nn.MultiheadAttention(dim, heads, batch_first=True)
        self.ff = nn.Sequential(
            nn.Linear(dim, dim * 4),
            nn.ReLU(),
            nn.Linear(dim * 4, dim)
        )
        self.norm1 = nn.LayerNorm(dim)
        self.norm2 = nn.LayerNorm(dim)

    def forward(self, x, mask):
        attn_out, _ = self.attn(x, x, x, attn_mask=mask)
        x = self.norm1(x + attn_out)
        ff_out = self.ff(x)
        return self.norm2(x + ff_out)


# ====================== FULL DECODER MODEL ======================

class TransformerDecoder(nn.Module):
    def __init__(self, vocab, dim=128, layers=4, heads=4):
        super().__init__()
        self.token_embedding = nn.Embedding(vocab, dim)
        self.position = PositionalEncoding(dim)
        self.layers = nn.ModuleList([DecoderBlock(dim, heads) for _ in range(layers)])
        self.fc = nn.Linear(dim, vocab)

    def forward(self, x):
        tok = self.token_embedding(x)
        x = self.position(tok)

        seq_len = x.size(1)
        mask = torch.triu(torch.ones(seq_len, seq_len) * float("-inf"), diagonal=1)

        for layer in self.layers:
            x = layer(x, mask)

        return self.fc(x)


# ====================== GENERATION ======================

def generate(model, tokenizer, prompt, max_len=50):
    model.eval()
    ids = tokenizer(prompt)

    x = torch.tensor([ids])

    for _ in range(max_len):
        logits = model(x)
        next_id = torch.argmax(logits[0, -1]).unsqueeze(0)
        x = torch.cat([x, next_id.unsqueeze(0)], dim=1)

        if next_id.item() == tokenizer.eos:
            break

    return tokenizer.decode(x[0].tolist())


# ====================== DEMO ======================

class SimpleTokenizer:
    def __init__(self):
        self.vocab = {c: i + 1 for i, c in enumerate("abcdefghijklmnopqrstuvwxyz ")}
        self.vocab_size = len(self.vocab) + 2
        self.eos = self.vocab_size - 1

    def __call__(self, text):
        ids = [self.vocab.get(c, 0) for c in text.lower()]
        ids.append(self.eos)
        return ids

    def decode(self, ids):
        inv = {v: k for k, v in self.vocab.items()}
        return "".join(inv.get(i, "") for i in ids if i != self.eos)


tokenizer = SimpleTokenizer()
model = TransformerDecoder(tokenizer.vocab_size)

print("\nChatGPT mini generation:")
print(generate(model, tokenizer, "hello wor"))
