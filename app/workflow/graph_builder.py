from app.core.state import AgentState
from langgraph.graph import StateGraph, END, START
from app.orchestrator.supervisor import Supervisor
from app.nodes.llm_node import LLM_Output
from app.nodes.rag_node import Rag
from app.nodes.web_crawler import WebSearch
from app.router.router import Routing
from app.nodes.validation import Validating



class GraphBuilding:
    def __init__(self):
        self.workflow=StateGraph(AgentState)

        self.workflow.add_node("Supervisor",Supervisor().supervisor_work)
        self.workflow.add_node("LLM",LLM_Output().get_llm)
        self.workflow.add_node("RAG",Rag().rag_function)
        self.workflow.add_node("WEB",WebSearch().get_search_web)
        self.workflow.add_node("VALIDATE",Validating().validation_output)

        self.workflow.set_entry_point('Supervisor')

        self.workflow.add_edge("LLM","VALIDATE")
        self.workflow.add_edge("RAG","VALIDATE")
        self.workflow.add_edge("WEB","VALIDATE")

        self.workflow.add_conditional_edges(
            "Supervisor",
            Routing().get_supervisor_result,
            {
                'RAG Call':'RAG',
                'WEB Call':'WEB',
                'LLM Call':'LLM',

            }
        )

        self.workflow.add_conditional_edges(
            "VALIDATE",
            Routing().get_validator_result,
            {
                'YES':END,
                'NO':'Supervisor'
            }
        )

        


    def get_workflow(self):
        self.app=self.workflow.compile()
        return self.app
