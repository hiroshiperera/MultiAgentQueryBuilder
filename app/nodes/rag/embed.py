from langchain_huggingface import HuggingFaceEmbeddings

class Embedding:
    def __init__(self):
        self.embedding=HuggingFaceEmbeddings(model_name="BAAI/bge-small-en")


    def embed_query(self, query):
        return self.embedding.embed_query(query)
    
    def embed_doc(self, document):
        return self.embedding.embed_documents(document)