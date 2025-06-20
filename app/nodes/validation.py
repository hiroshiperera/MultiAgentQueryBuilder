from app.core.llm_factory import GenModel
from app.core.template_manager import Templates
from app.core.state import AgentState

class Validating:
    def __init__(self):
        pass

class Validating:
    def __init__(self):
        pass

    def validation_output(self, state: AgentState):
        print("Validating query...",state["message"][0])
        print("Validating response...",state["message"][-1])
        # You must construct the actual validation input using the template
        validation_prompt = Templates().get_validation_template().format(
            user_query=state["message"][0],
            response=state["message"][-1]
        )

        self.validation_result = GenModel().get_model().invoke(validation_prompt).content

        print("Validation Result:", self.validation_result)

        if "YES" in self.validation_result.upper():
            return {'message':["YES"]} # Ensure messages are kept
        else:
            return {
                "message": [state["message"][-1]]
            } 
        