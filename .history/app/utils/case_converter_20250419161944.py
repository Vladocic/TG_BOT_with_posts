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



