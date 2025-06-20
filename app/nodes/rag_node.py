from langchain.prompts import PromptTemplate
from app.core.template_manager import Templates
from app.nodes.rag.retriever import Retriever
from app.core.llm_factory import GenModel
from app.core.state import AgentState
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class Rag:
    def __init__(self):
        pass

    def format_docs(self,docs):
        return "\n\n".join(doc.page_content for doc in docs)


    def rag_function(self, state:AgentState):
        print("-- RAG ---")

        question=state["message"][0]

        prompt=PromptTemplate(
            template=Templates().get_rag_template(),

        input_variables=['context','question']
        )

        rag_chain=(
            {'context':Retriever().get_retriever() 
             
             | self.format_docs,
             
             'question':RunnablePassthrough()
             
             }

             | prompt

             | GenModel().get_model()

             | StrOutputParser()

        )

        result = rag_chain.invoke(question)
        print("--------Rag Result---------",result)

        return {'message':[result]}
    
