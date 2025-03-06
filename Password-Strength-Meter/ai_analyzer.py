from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

class AIPasswordAdvisor:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.7,google_api_key=GOOGLE_API_KEY)
        self.prompt_template = PromptTemplate(
            input_variables=["password", "strength_score"],
            template="""
            Analyze the following password and provide feedback based on its strength score:
            Password: {password}
            Strength Score: {strength_score}
            
            Provide personalized suggestions to improve the password if necessary.
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def get_feedback(self, password, strength_score):
        feedback = self.chain.run(password=password, strength_score=strength_score)
        return feedback