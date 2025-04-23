import re

def camel_to_snake_case(data: list) -> list:

    snake_list=[]

    for item in data:
        new_dict = {}
        for key,value in item.items():
            key = re.sub(r'(?<!^)(?=[A-Z])','_', key).lower()
            new_dict[key] = value
        snake_list.append(new_dict)

    return snake_list

def convert_dict_keys(d: dict) -> dict:
    new_dict = {}
    for key,value in d.items():
        key = re.sub(r'(?<!^)(?=[A-Z])','_', key).lower()
        new_dict[key] = value
    return    



def camel_to_snake_case(data: list[dict]) -> list[dict]:



