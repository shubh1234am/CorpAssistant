from .embeddings import create_embedding
from .chroma_db import collection


def search_documents(query):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=3
    )

    return results