import re

def camel_to_snake_case(data: list) -> list:

    snake_list=[]

    for item in data:
        for key,value in item.items():

            snake_list.append({key:value})


    return



re.sub(r'(?<!^)(?=[A-Z])','_', c).lower()