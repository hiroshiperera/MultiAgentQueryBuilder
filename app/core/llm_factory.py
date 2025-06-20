from langchain_google_genai import ChatGoogleGenerativeAI
import os
import dotenv

class GenModel:
    def __init__(self):
        self.google_api_key=os.environ['GOOGLE_GEN_API_KEY']
        self.model=ChatGoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=self.google_api_key)

    def get_model(self):
        return self.model