import schema_registry

_schema_classes = schema_registry.discover_schemas()

def get_schema(name:str):
    if name in _schema_classes:
        return _schema_classes[name]
    else:
        raise ValueError(f'Schema with name {name} is not currently supported or has not been successfully registered.')
    
