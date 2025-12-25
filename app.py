# app.py
import os
from transformers import pipeline

from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFacePipeline  # Updated import

# -----------------------------
# 1️⃣ Load DistilGPT-2 via pipeline (CPU-friendly)
# -----------------------------
print("Loading DistilGPT-2 model (CPU-friendly)...")
generator = pipeline(
    "text-generation",
    model="distilgpt2",
    device=-1,           # CPU
    max_new_tokens=150,  # Generate up to 150 new tokens
)

# Wrap for LangChain
llm = HuggingFacePipeline(pipeline=generator)

# -----------------------------
# 2️⃣ Load documents
# -----------------------------
data_path = "data/sample.txt"
if not os.path.exists(data_path):
    os.makedirs("data", exist_ok=True)
    with open(data_path, "w", encoding="utf-8") as f:
        f.write("DistilGPT-2 is a small, open-source language model.\n")
        f.write("Chroma is a vector database used for semantic search.\n")

loader = TextLoader(data_path, encoding="utf-8")
documents = loader.load()

# -----------------------------
# 3️⃣ Split text into chunks
# -----------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# -----------------------------
# 4️⃣ Create embeddings + Chroma DB
# -----------------------------
print("Creating embeddings and Chroma DB...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# -----------------------------
# 5️⃣ Create Retrieval QA chain
# -----------------------------
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever()
)

# -----------------------------
# 6️⃣ Ask questions
# -----------------------------
print("\n✅ DistilGPT-2 + Chroma Q&A is ready!")

while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break
    # Use invoke() instead of deprecated run()
    answer = qa.invoke({"query": query})["result"]
    print("\nAnswer:", answer)
