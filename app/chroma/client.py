import chromadb # type: ignore
from chromadb.utils import embedding_functions # type: ignore

def Chroma_Client(persistent_path:str, collection_name:str):
    client = chromadb.PersistentClient(path=persistent_path)
    client = client.get_or_create_collection(name=collection_name)
    return client
