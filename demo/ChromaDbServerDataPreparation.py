import chromadb
from chromadb.utils import embedding_functions


default_ef = embedding_functions.DefaultEmbeddingFunction()
chroma_client = chromadb.HttpClient(host='localhost', port=8000)

collection = chroma_client.create_collection(name="my_collection")
collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    metadatas=[
        {"source": "source1"},
        {"source": "source2"}
    ],
    ids=["id1", "id2"]
)
    