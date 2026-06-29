import chromadb


client = chromadb.PersistentClient(
    path="chroma_storage"
)

collection = client.get_or_create_collection(
    name="company_documents"
)


def store_chunks(chunks_data):

    for index, item in enumerate(chunks_data):

        collection.add(
            ids=[str(index)],
            documents=[item["chunk"]],
            embeddings=[item["embedding"].tolist()]
        )