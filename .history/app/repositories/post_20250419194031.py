from app.models.post import Post
from app.schemas.post import PostSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert
class PostRepository:
    def __init__ (self, session:AsyncSession):
        self.session = session

    async def save_many(posts: list[PostSchema]):
        post_dicts = [post.model_dump() for post in posts]
        stmt = input(Post).values(post_dicts).onconf

#save_many(posts: list[PostSchema])