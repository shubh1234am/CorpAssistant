from .chunker import chunk_text
from .embeddings import create_embedding


def process_document(text):

    chunks = chunk_text(text)

    results = []

    for chunk in chunks:

        embedding = create_embedding(chunk)

        results.append(
            {
                "chunk": chunk,
                "embedding": embedding,
            }
        )

    return results