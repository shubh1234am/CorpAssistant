import os

from groq import Groq
from dotenv import load_dotenv

# Load .env file
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(context, question):
    """
    Send context and question to Groq.
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

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content