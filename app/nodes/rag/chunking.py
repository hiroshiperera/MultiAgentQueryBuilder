from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunking:
    def __init__(self):
        self.text_splitter=RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=50
        )