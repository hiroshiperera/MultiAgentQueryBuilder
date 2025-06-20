from app.nodes.rag.chromaDb import VectorStore


class Retriever:
    def __init__(self):
        self.retriever = VectorStore().vector_store.as_retriever(
                        search_type="mmr", search_kwargs={"k": 1, "fetch_k": 5}
                    )


    def get_retriever(self):
        return self.retriever