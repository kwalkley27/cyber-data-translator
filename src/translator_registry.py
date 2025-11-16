import pkgutil
import importlib
from typing import Dict, Type
from schemas.base_schema_translator import BaseSchemaTranslator
from inference.base_translator_agent import BaseTranslatorAgent

def discover_schemas() -> Dict[str, Type[BaseSchemaTranslator]]:
    """Dynamically loads BaseSchemaTranslator subclasses into a dictionary.

    Returns:
        Dictionary mapping schema names to their translator classes
    """
    import schemas
    schema_classes: Dict[str, Type[BaseSchemaTranslator]] = {}

    for _, module_name, _ in pkgutil.iter_modules(schemas.__path__, schemas.__name__ + '.'):
        module = importlib.import_module(module_name)
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, BaseSchemaTranslator) and obj is not BaseSchemaTranslator:
                schema_classes[obj.name()] = obj

    return schema_classes

def discover_agents() -> Dict[str, Type[BaseTranslatorAgent]]:
    """Dynamically loads BaseTranslatorAgent subclasses into a dictionary.

    Returns:
        Dictionary mapping agent names to their agent classes
    """
    import inference
    agent_classes: Dict[str, Type[BaseTranslatorAgent]] = {}

    for _, module_name, _ in pkgutil.iter_modules(inference.__path__, inference.__name__ + '.'):
        module = importlib.import_module(module_name)
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, BaseTranslatorAgent) and obj is not BaseTranslatorAgent:
                agent_classes[obj.name()] = obj

    return agent_classes