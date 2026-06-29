from .search import search_documents
from .llm import ask_llm


def ask_company(question):
    """
    Complete RAG Pipeline
    """

    results = search_documents(question)

    context = "\n\n".join(results["documents"][0])

    answer = ask_llm(
        context,
        question
    )

    return answer