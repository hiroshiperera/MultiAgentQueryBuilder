from pydantic import BaseModel, Field


class TopicSelectionParser(BaseModel):
        topic:str=Field(description="selects topic")
        reasoning:str=Field(description="Reasoning Behind the selected topic")