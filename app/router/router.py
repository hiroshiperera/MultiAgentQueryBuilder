from app.core.state import AgentState

class Routing:
    def __init__(self):
        pass


    def get_supervisor_result(self, state:AgentState):
        print('-- SUPERVISOR ROUTER --')

        last_message=state["message"][-1]
        print("Last Message",last_message)

        if 'rag call' in last_message.lower():
            return "RAG Call"
        
        if 'web call' in last_message.lower():
            return "WEB Call"
        
        else:
            return "LLM Call"


    def get_validator_result(self, state:AgentState):
        print('-- VALIDATOR ROUTER --')

        last_message=state["message"][-1]
        print("Last Message after validation..",last_message)

        if 'YES' in last_message:
            return "YES"
        
        else:
            return "NO"