from langchain_chroma import Chroma
from app.nodes.rag import embed
from uuid import uuid4

class VectorStore:
    def __init__(self):
        
        self.vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embed.Embedding().embedding,
        persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
    )
        

    def add_documents(self,documents):

        '''add documents to the vector db'''

        uuids = [str(uuid4()) for _ in range(len(documents))]
        self.vector_store.add_documents(documents=documents, ids=uuids)