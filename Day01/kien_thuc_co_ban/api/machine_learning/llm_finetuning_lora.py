"""
===============================================================================
                     LLM FINE-TUNING WITH LoRA + QLoRA
Fine-tuning LLM lớn bằng LoRA + QLoRA

Train mô hình với VRAM thấp (6–12GB)

Dùng cho việc huấn luyện chatbot theo dữ liệu doanh nghiệp
===============================================================================
"""

from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model
import torch

print("\n===== LOAD BASE MODEL =====")

model_name = "tiiuae/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,   # QLoRA
    device_map='auto'
)

# ======================== LoRA CONFIG ========================

config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["query_key_value"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, config)

# ======================== TRAINING DATA =======================

dataset = [
    {"instruction": "Xin chào", "output": "Chào bạn, tôi có thể giúp gì?"},
    {"instruction": "Nhà hàng Hoa Ban ở đâu?", "output": "97 Trần Phú, Đà Nẵng."}
]

def tokenize(example):
    text = f"### Instruction: {example['instruction']}\n### Response: {example['output']}"
    return tokenizer(text, truncation=True)

train_data = [tokenize(x) for x in dataset]

# ======================== TRAINER =============================

training_args = TrainingArguments(
    output_dir="lora_finetuned",
    per_device_train_batch_size=1,
    learning_rate=2e-4,
    num_train_epochs=2
)

trainer = Trainer(
    model=model,
    train_dataset=train_data,
    args=training_args
)

trainer.train()

print("Fine-tuning với LoRA + QLoRA hoàn thành!")
