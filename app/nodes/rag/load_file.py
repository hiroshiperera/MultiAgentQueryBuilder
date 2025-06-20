from langchain_community.document_loaders import PyPDFLoader
from app.nodes.rag.chunking import Chunking


class LoadDocument:
    def __init__(self,path):
        loader=PyPDFLoader(path)
        self.pages = loader.load()


    def get_split_docs(self):
        split_docs=Chunking().text_splitter.split_documents(self.pages)
        return split_docs
