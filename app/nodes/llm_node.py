from app.core.llm_factory import GenModel
from app.core.state import AgentState
from app.core.template_manager import Templates
from app.core.parser import Parser
from langchain_core.prompts import PromptTemplate

class LLM_Output:
    def __init__(self):
        pass

    def get_llm(self,state:AgentState):
        print("--- LLM Call ---")

        question = state["message"][0]

        print("Question........",question)

        prompt= PromptTemplate(
            template=Templates().get_llm_template(),
            input_variable=["question"],
            partial_variables={"format_instructions": Parser().get_parser().get_format_instructions()}
        )
        
        chain= prompt | GenModel().get_model() | Parser().get_parser()
        
        response = chain.invoke({"question":question})
        print('LLM response ',response)
        
        print("Parsed response:", response)

        return {"message":[response]}
    