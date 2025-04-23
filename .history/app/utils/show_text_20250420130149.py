from app.models.post import Post
from



def show_text(posts:list[Any]) -> str:
    text = '\n\n'.join(
        f'<b>Post #{post.id}\nTitle</b>: {post.title}\n<b>Text</b>: {post.body}'for post in posts
        )
    return text