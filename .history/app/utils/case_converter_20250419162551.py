import re


def convert_dict_keys(d: dict) -> dict:
    return {
        re.sub(r'(?<!^)(?=[A-Z])','_', key).lower():value for  key,value in d.items()
    }




def camel_to_snake_case(data: list[dict]) -> list[dict]:
    return [convert_dict_keys(items) for items in data ]




