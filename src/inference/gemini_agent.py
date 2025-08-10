from inference.base_translator_agent import BaseTranslatorAgent
import google.generativeai as genai
import os

class GeminiAgent(BaseTranslatorAgent):

    def setup(self, system_instructions:str):

        REQUIRED_ENV_VAR = 'GEMINI_API_KEY'

        if not REQUIRED_ENV_VAR in os.environ():
            raise KeyError(f'The environment variable {REQUIRED_ENV_VAR} is not set.')

        return genai.GenerativeModel("gemini-2.5-pro", system_instruction=system_instructions)

    def generate(self, prompt:str) -> str:
        return self.model.generate_content(prompt).text.strip()
    
    def __init__(self):
        super().__init__()
        self.system_instructions = '''You are a helpful agent meant to help translate sample data into a normalized cyber schema. Only use the context provided about the schema to come up with the proper mappings'''
        self.model = self.setup(self.system_instructions)

    @classmethod
    def name(cls):
        return 'gemini'