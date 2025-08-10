from abc import ABC, abstractmethod

class BaseTranslatorAgent(ABC):

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def generate(self, prompt:str) -> str:
        pass

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        pass