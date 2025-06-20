from langchain.output_parsers import PydanticOutputParser
from app.core.pydantic_validation import TopicSelectionParser

class Parser:
    def __init__(self):
        self.parser=PydanticOutputParser(pydantic_object=TopicSelectionParser)


    def get_parser(self):
        return self.parser