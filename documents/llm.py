import requests


def ask_llm(context, question):
    """
    Send context and question to Ollama.
    """

    prompt = f"""
You are CorpAssistant, an AI assistant for company employees.

Answer ONLY from the provided context.

If the answer is not found in the context, reply exactly:

"I couldn't find that information in the uploaded company documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:latest",
            "prompt": prompt,
            "stream": False,
        },
    )

    return response.json()["response"]