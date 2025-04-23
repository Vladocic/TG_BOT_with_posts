import re


def convert_dict_keys(d: dict) -> dict:
    """
    Преобразует ключи словаря из camelCase в snake_case.
    :param d: Словарь с ключами в camelCase.
    :return: Новый словарь с ключами в snake_case.
    """
    return {
        re.sub(r'(?<!^)(?=[A-Z])','_', key).lower():value for  key,value in d.items()
    }


def camel_to_snake_case(data: list[dict]) -> list[dict]:
        """
    Применяет преобразование ключей к каждому словарю в списке.

    :param data: Список словарей с ключами в camelCase.
    :return: Список словарей с ключами в snake_case.
    """
    return [convert_dict_keys(items) for items in data ]




