from inference.base_translator_agent import BaseTranslatorAgent
import google.generativeai as genai
import os
from typing import Any

class GeminiAgent(BaseTranslatorAgent):
    """AI agent that uses Google's Gemini API for data translation."""

    def setup(self, system_instructions: str) -> Any:
        """Initialize the Gemini generative model.

        Args:
            system_instructions: System prompt to guide the model's behavior

        Returns:
            Configured GenerativeModel instance

        Raises:
            KeyError: If GEMINI_API_KEY environment variable is not set
        """
        REQUIRED_ENV_VAR = 'GEMINI_API_KEY'

        if REQUIRED_ENV_VAR not in os.environ:
            raise KeyError(f'The environment variable {REQUIRED_ENV_VAR} is not set.')

        return genai.GenerativeModel("gemini-2.5-pro", system_instruction=system_instructions)

    def generate(self, prompt: str) -> str:
        """Generate a response from the AI model.

        Args:
            prompt: The prompt to send to the model

        Returns:
            The model's response text, stripped of leading/trailing whitespace
        """
        return self.model.generate_content(prompt).text.strip()

    def __init__(self) -> None:
        """Initialize the Gemini agent with default system instructions."""
        super().__init__()
        self.system_instructions = '''You are a helpful agent meant to help translate sample data into a normalized cyber schema. Only use the context provided about the schema to come up with the proper mappings'''
        self.model = self.setup(self.system_instructions)

    @classmethod
    def name(cls) -> str:
        """Return the agent's identifier name.

        Returns:
            The string 'gemini'
        """
        return 'gemini'