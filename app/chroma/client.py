import chromadb  # type: ignore
from chromadb.utils import embedding_functions  # type: ignore
from chroma.utils import ef  # type: ignore

def agent(persistent_path: str, collection_name: str):
    try:
        client = chromadb.PersistentClient(path=persistent_path)
        memory = client.get_or_create_collection(name=collection_name)

        return client, memory
    except Exception as e:
        print(f"Error initializing ChromaDB: {e}")
        raise