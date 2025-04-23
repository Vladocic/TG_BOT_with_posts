from typing import Any


def show_text(posts:list[Any]) -> str:
    """
    Форматирует список постов в строку для отображения в Telegram.
    :param posts: Список объектов, содержащих поля `id`, `title`, `body`.
    :return: Отформатированная строка с постами в HTML-формате.
    """
    text = '\n\n'.join(
        f'<b>Post #{post.id}\nTitle</b>: {post.title}\n<b>Text</b>: {post.body}'for post in posts
        )
    return text