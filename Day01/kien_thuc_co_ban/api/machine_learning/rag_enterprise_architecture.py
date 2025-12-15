"""
===============================================================================
       RAG ENTERPRISE ARCHITECTURE — FULL PIPELINE (FAISS + TRANSFORMER)
===============================================================================
"""

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import faiss
import numpy as np


# ========================== 1. DOCUMENT INGESTION ==========================

print("\n===== STEP 1: LOAD DOCUMENTS =====")

documents = [
    "Hoa Ban Restaurant địa chỉ 97 Trần Phú Đà Nẵng.",
    "Nhà hàng mở cửa từ 7h đến 22h.",
    "Các món signature: lẩu nấm, cơm sen, salad rong biển.",
    "Voucher 10% áp dụng cho hóa đơn trên 300k."
]


# ========================== 2. EMBEDDING & VECTOR DB =======================

print("\n===== STEP 2: EMBEDDINGS + FAISS =====")

embedder = SentenceTransformer("all-MiniLM-L6-v2")
vectors = embedder.encode(documents)

dim = vectors.shape[1]
index = faiss.IndexFlatIP(dim)
index.add(vectors)


# ========================== 3. RETRIEVAL FUNCTION ==========================

def retrieve(query, k=3):
    q_vec = embedder.encode([query])
    scores, idxs = index.search(q_vec, k)
    return [documents[i] for i in idxs[0]]


# ========================== 4. GENERATION USING TRANSFORMER ================

print("\n===== STEP 4: TRANSFORMER GENERATION =====")

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

def rag_answer(query):
    # Retrieve
    context = retrieve(query)
    ctx_text = " | ".join(context)

    # Build prompt
    prompt = f"""
Dưới đây là dữ liệu nội bộ của doanh nghiệp:

{ctx_text}

Câu hỏi: {query}
Trả lời theo đúng dữ liệu trên, không được bịa.
"""

    inputs = tokenizer(prompt, return_tensors="pt")
    out = model.generate(**inputs, max_length=200)
    return tokenizer.decode(out[0], skip_special_tokens=True)


print("\nRAG Output:")
print(rag_answer("Nhà hàng ở đâu?"))
