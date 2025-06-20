from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage 
# LangChain, when you're dealing with multi-turn conversations or agents, messages are not plain strings. 
# AIMessage,HumanMessage,SystemMessage,ToolMessage. All of these inherit from BaseMessage
import operator

class AgentState(TypedDict):
    '''
    What is this method? It is I'm defining a dictionary called AgentState that always has a key called message.
    This value is a list of messages. When I have two such states to merge, the tool should just add the list of 
    messages
    '''
    message: Annotated[Sequence[BaseMessage], operator.add]