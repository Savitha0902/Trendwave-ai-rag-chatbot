# 🤖 RAG Chatbot using Flask, LangChain & ChromaDB

## 📌 Project Overview

This project is a **Retrieval-Augmented Generation (RAG) Chatbot** that answers user questions based on the content of a PDF document. Instead of relying only on the language model's knowledge, the chatbot retrieves relevant information from a vector database and uses it to generate accurate, context-aware responses.

The application is built using **Python**, **Flask**, **LangChain**, **ChromaDB**, and **Hugging Face Embeddings**, with a simple web interface created using **HTML**, **CSS**, and **JavaScript**.

---

## 🚀 Features

- 📄 Question answering from PDF documents
- 🔍 Retrieval-Augmented Generation (RAG)
- 🧠 Vector embeddings using Hugging Face
- 📦 ChromaDB for vector storage and similarity search
- 🌐 Flask-based web application
- 💬 Interactive chatbot interface
- ⚡ Fast and context-aware responses

---

## 🛠️ Technologies Used

- Python
- Flask
- LangChain
- ChromaDB
- Hugging Face Embeddings
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```text
rag-chatbot/
│
├── chatbot.py
├── create_db.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── chatbot.html
│
├── static/
│   ├── chat.css
│   ├── chatbot.css
│   └── ai.js
│
├── documents/
│   └── TrendWave_Catalog.pdf
│
└── screenshots/
```

---

## ⚙️ How It Works

1. The PDF document is processed.
2. Text is divided into smaller chunks.
3. Hugging Face Embeddings convert the chunks into vectors.
4. ChromaDB stores the vector embeddings.
5. When a user asks a question:
   - The query is converted into an embedding.
   - ChromaDB retrieves the most relevant document chunks.
   - The retrieved context is sent to the language model.
   - The chatbot generates an answer based on the retrieved information.
