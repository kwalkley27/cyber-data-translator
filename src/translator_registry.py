import pkgutil
import importlib
from schemas.base_schema_translator import BaseSchemaTranslator
from inference.base_translator_agent import BaseTranslatorAgent

def discover_schemas():
    '''Dynamically loads BaseSchemaTranslator subclasses into a dictionary, mapped by the classes name function'''
    package = 'schemas'

    schema_classes = {}

    for _, module_name, _ in pkgutil.iter_modules([package]):
        module = importlib.import_module(f'{package}.{module_name}')
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, BaseSchemaTranslator) and obj is not BaseSchemaTranslator:
                schema_classes[obj.name()] = obj
    
    return schema_classes

def discover_agents():
    '''Dynamically loads BaseTranslatorAgent subclasses into a dictionary, mapped by the classes name function'''
    package = 'inference'

    agent_classes = {}

    for _, module_name, _ in pkgutil.iter_modules([package]):
        module = importlib.import_module(f'{package}.{module_name}')
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, BaseTranslatorAgent) and obj is not BaseTranslatorAgent:
                agent_classes[obj.name()] = obj
    
    return agent_classes