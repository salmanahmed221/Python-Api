import json
from jsonschema import validate

schema1 = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 18}
    },
    "required": ["name", "age"]
}

data = {"name": "John Doe", "age": 20}

try:
    validate(instance=data, schema=schema1)
    print("Data is valid")
except jsonschema.exceptions.ValidationError as e:
    print("Data is invalid:", e)