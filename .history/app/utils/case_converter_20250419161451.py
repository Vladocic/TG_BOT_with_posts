import re

def camel_to_snake_case(data: list) -> list:



    for item in data:
        for key,value in item.items():


    pass



re.sub(r'(?<!^)(?=[A-Z])','_', c).lower()