from app.models.post import Post
from app.schemas.post import PostSchema
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert

class PostRepository:
    def __init__ (self, session:AsyncSession):
        self.session = session

    async def save_many(self, posts: list[PostSchema]) -> None:
        post_dicts = [post.model_dump() for post in posts]
        stmt = insert(Post).values(post_dicts).on_conflict_do_nothing(index_elements=['id'])

        await self.session.execute(stmt)
        await self.session.commit()

    async def get_posts_paginated(self, offset: int = 0, limit: int = 5) - > list[PostSchema]:
        stmt = select(Post).offset(offset).limit(limit)
        await self.session.execute(st)