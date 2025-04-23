from app.models.post import Post
from app.schemas.post import PostSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

class PostRepository:
    def __init__ (self, session:AsyncSession):
        self.session = session

    async def save_many(posts: list[PostSchema]):
        for post in posts:
            Post(post.model_dump()

    #    Post(post.dict()) for post in posts
#save_many(posts: list[PostSchema])