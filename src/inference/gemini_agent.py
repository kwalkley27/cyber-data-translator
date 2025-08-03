from inference.base_translator_agent import BaseTranslatorAgent

class GeminiAgent(BaseTranslatorAgent):

    def setup(self):
        pass

    def generate(self, prompt:str) -> str:
        return 'Test Gemini generation'
    
    @classmethod
    def name(cls):
        return 'gemini'