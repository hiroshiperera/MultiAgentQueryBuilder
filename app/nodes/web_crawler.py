#from langchain_community.tools import DuckDuckGoSearchRun
#from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from app.core.state import AgentState


class WebSearch:
    def __init__(self):
        pass


    def get_search_web(self,state:AgentState):
        print('---------------------WEB-------1-------------')
        self.question = state['message'][0]
        print('---------------------WEB-------2-------------',self.question)
        search = TavilySearch()
        response = search.invoke(self.question)

        # Get only the list of result contents
        web_contents = [item["content"] for item in response.get("results", []) if "content" in item]

        # Join into one string for LLM or reranker
        joined_content = "\n\n".join(web_contents)
        #search = DuckDuckGoSearchRun()
        #print('---------------------WEB-------3-------------')
        #response=search.run(self.question.reasoning)
        print('---------------------WEB-------3-------------')
        print(joined_content)
        return {'message':[joined_content]}
