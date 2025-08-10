import translator_registry

_schema_classes = translator_registry.discover_schemas()
_agent_classes = translator_registry.discover_agents()

def get_schema(name:str):
    if name in _schema_classes:
        return _schema_classes[name]
    else:
        raise ValueError(f'Schema with name {name} is not currently supported or has not been successfully registered.')
    
def get_agent(name:str):
    if name in _agent_classes:
        return _agent_classes[name]
    else:
        raise ValueError(f'Agent with name {name} is not currently supported or has not been successfully registered.')
    