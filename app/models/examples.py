from copy import deepcopy
from typing import Dict

successful_response: Dict = {
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {}
            }
        }
    }
}

example_dict = {
    "name": "Foo",
    "description": "A very nice Item",
    "price": 35.4,
    "tax": 3.2,
}

example_str = "Example!"

successful_response_example_dict = deepcopy(successful_response)
successful_response_example_dict[200]["content"]["application/json"]["example"] = example_dict

successful_response_example_any = deepcopy(successful_response)
successful_response_example_any[200]["content"]["application/json"] = {
    "examples": {
        "example1": {
            "summary": "Example string",
            "value": example_str
        },
        "example2": {
            "summary": "Example dictionary",
            "value": example_dict
        }
    }
}
