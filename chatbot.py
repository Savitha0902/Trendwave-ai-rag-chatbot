from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

app = Flask(__name__)
CORS(app)

API_KEY = "Your_API_KEY"
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding
)

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    docs = db.similarity_search(user_message, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the provided catalog information.

Catalog Information:
{context}

Question:
{user_message}

If the answer is not present in the catalog information, reply:
Sorry, I could not find that information in the product catalog.
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-120b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()

    reply = data["choices"][0]["message"]["content"]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)