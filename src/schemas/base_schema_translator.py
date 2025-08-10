from abc import ABC, abstractmethod

class BaseSchemaTranslator(ABC):

    @abstractmethod
    def translate(self, sample:str) -> str:
        pass

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        pass