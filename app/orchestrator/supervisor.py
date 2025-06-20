from langchain_core.prompts import ChatMessagePromptTemplate,PromptTemplate
from app.core.state import AgentState
from app.core.llm_factory import GenModel
from app.core.template_manager import Templates
from app.core.parser import Parser
import logging

logger = logging.getLogger(__name__)

class Supervisor:
    def __init__(self):
        pass
        
    def supervisor_work(self, state:AgentState):
        print("---Supervisor message----",state["message"])
        question=state["message"][0]
        print("----- Inside the Supervisor Node ------")

        template=Templates().get_supervisor_template()
        
        prompt= PromptTemplate(
            template=template,
            input_variable = ["question"],
            partial_variables = {
                "format_instructions":Parser().get_parser().get_format_instructions()
            }
        )

        chain = prompt | GenModel().get_model() | Parser().get_parser()

        response = chain.invoke({"question":question})

        
        print('----supervisor output---',response)

        return {'message':[response.topic]}