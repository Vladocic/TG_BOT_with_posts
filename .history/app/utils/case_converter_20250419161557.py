import re

def camel_to_snake_case(data: list) -> list:

    snake_list=[]

    for item in data:
        for key,value in item.items():
            key = re.sub(r'(?<!^)(?=[A-Z])','_', key).lower() 
            snake_list.append({key:value})


    return snake_list



re.sub(r'(?<!^)(?=[A-Z])','_', key).lower()