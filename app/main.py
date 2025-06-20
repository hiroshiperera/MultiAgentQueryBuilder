from app.nodes.rag.embed import Embedding
from app.nodes.rag import load_file
from app.nodes.rag.chromaDb import VectorStore
from app.nodes.rag.retriever import Retriever
from app.workflow.graph_builder import GraphBuilding

if __name__=="__main__":
    file_path= r"D:/DataScience/Assignments/Lang_Graph_Proj1/app/data/PLR.pdf"

    split_docs=load_file.LoadDocument(file_path).get_split_docs()

    # Embed documents
    #embed_documents=Embedding().embed_doc([doc.page_content for doc in split_docs]) # For embedding you should send always a list of strings

    VectorStore().add_documents(split_docs)

    #retrieved_results=Retriever().retriever.invoke("How is the growth of PLR"))

    # Call the graph builder

    app=GraphBuilding().get_workflow()

    state={'message':['what is the profit of PLR in 2025?']}

    result=app.invoke(state)

    print('Final Result...',result)