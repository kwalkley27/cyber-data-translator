from typing import Type
import translator_registry
from schemas.base_schema_translator import BaseSchemaTranslator
from inference.base_translator_agent import BaseTranslatorAgent

_schema_classes = translator_registry.discover_schemas()
_agent_classes = translator_registry.discover_agents()

def get_schema(name: str) -> Type[BaseSchemaTranslator]:
    """Get a schema translator class by name.

    Args:
        name: The name of the schema (e.g., 'OCSF')

    Returns:
        The schema translator class

    Raises:
        ValueError: If the schema is not supported or registered
    """
    if name in _schema_classes:
        return _schema_classes[name]
    else:
        raise ValueError(f'Schema with name {name} is not currently supported or has not been successfully registered.')

def get_agent(name: str) -> Type[BaseTranslatorAgent]:
    """Get an AI agent class by name.

    Args:
        name: The name of the agent (e.g., 'gemini')

    Returns:
        The agent class

    Raises:
        ValueError: If the agent is not supported or registered
    """
    if name in _agent_classes:
        return _agent_classes[name]
    else:
        raise ValueError(f'Agent with name {name} is not currently supported or has not been successfully registered.')
    