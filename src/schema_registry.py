import pkgutil
import importlib
from schemas.base_schema_translator import BaseSchemaTranslator


def discover_schemas():
    package = 'schemas'

    schema_classes = {}

    for _, module_name, _ in pkgutil.iter_modules([package]):
        module = importlib.import_module(f'{package}.{module_name}')
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, BaseSchemaTranslator) and obj is not BaseSchemaTranslator:
                schema_classes[obj.name()] = obj
    
    return schema_classes