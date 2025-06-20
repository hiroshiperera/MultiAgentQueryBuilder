
class Templates:
    def __init__(self):
        self.supervisor_temp= """
            You are routing a user query to one of three systems:
            - 'RAG' → for queries that ask about internal company reports, documents, finance of Prime Land Recidencies(PLR), PLR policies, guidelines, or PDFs we have indexed.
            - 'WEB' → for questions that need current or real-time information like weather, prices, news, current affairs of the world. All the uptodate information needs to be answered by this
            - 'LLM' → for general knowledge, how-to questions, or basic facts.

            Return a JSON object with these fields:
            {{ 
            "topic": "<one of RAG Call, WEB Call, LLM Call>", 
            "reasoning": "<brief explanation for your choice>" 
            }}

            user query : {question}
            {format_instructions}
            """
        
        
        self.llm_temp='''
                answer the following question with your knowledge of the real world. 
                If you dont know the anwer just tell, [I dont know]. Here is the user question. 


                    Return a JSON object with these fields:
                    {{ 
                    "topic": "answer", 
                    "reasoning": "<brief explanation for your choice>" 
                    }}

                    user query : {question}
                    {format_instructions}
            '''
        
        self.rag_temp= """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
                            If you don't know the answer, just say [I dont know]. 
                            Use three sentences maximum and keep the answer concise.\n 
                            Question: {question} \n 
                            Context: {context} \n Answer:"""
        
                       
                        
        
        self.validation_temp = """
                        Evaluate the following response for completeness and relevance to the user query. If the Response is with lots of information,
                        but if the Response have the answer, extract the answer. If the extracted answer has the value, then return 'YES' with the direct answer. 
                        Else reply directly 'NO'

                        User Query: {user_query}
                        Response: {response}        
                        """


    def get_supervisor_template(self):
        return self.supervisor_temp
    

    def get_rag_template(self):
        return self.rag_temp
    
    def get_validation_template(self):
        return self.validation_temp
    
    
    def get_llm_template(self):
        return self.llm_temp