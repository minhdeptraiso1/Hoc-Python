"""
===============================================================================
                 AI CHATBOT NÂNG CAO (TRANSFORMER + RAG PIPELINE)

Tạo chatbot dùng Transformers (DialoGPT)

Tích hợp RAG (Retrieval-Augmented Generation)

Lưu dữ liệu vào FAISS vector database

Chatbot trả lời dựa trên kiến thức riêng của em
===============================================================================
"""

# ============================== 1) EMBEDDINGS ===============================

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

print("\n===== BUILD VECTOR STORE (FAISS) =====")

embedder = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Nhà hàng Hoa Ban phục vụ món chay.",
    "Thời gian mở cửa từ 7h đến 22h.",
    "Địa chỉ: 97 Trần Phú, Đà Nẵng."
]

embeddings = embedder.encode(documents, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


# ============================== 2) RETRIEVAL ===============================

def retrieve(query):
    q_emb = embedder.encode([query])[0]
    dist, idx = index.search(np.array([q_emb]), k=2)
    return [documents[i] for i in idx[0]]


# ============================== 3) TRANSFORMER LLM ==========================

from transformers import AutoModelForCausalLM, AutoTokenizer

print("\n===== LOAD TRANSFORMER MODEL =====")

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

def answer_with_rag(query):
    context = retrieve(query)
    prompt = "Context: " + " | ".join(context) + "\nUser: " + query + "\nBot:"

    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_length=100)
    return tokenizer.decode(output[0], skip_special_tokens=True)

print("\nChatbot trả lời:", answer_with_rag("Nhà hàng ở đâu?"))
