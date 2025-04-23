from app.models.post import Post
from app.schemas.post import PostSchema
from sqlalchemy import select, func, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError

class PostRepository:
    def __init__ (self, session:AsyncSession):
        self.session = session

    async def save_many(self, posts: list[PostSchema]) -> None:
        post_dicts = [post.model_dump() for post in posts]
        stmt = insert(Post).values(post_dicts).on_conflict_do_nothing(index_elements=['id'])

        await self.session.execute(stmt)
        await self.session.execute(
            text("SELECT setval('posts_id_seq', (SELECT MAX(id) FROM posts))")
        )
        await self.session.commit()

    async def update_id_seq(self):
        await self.session.execute(
            text("SELECT setval('posts_id_seq', (SELECT MAX(id) FROM posts))")
        )

    async def get_posts_paginated(self, offset: int = 0, limit: int = 5) -> list[Post]:
        stmt = select(Post).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    
    async def save_one(self, post: Post) -> int | None:
        try:
            self.session.add(post)
            await self.session.commit()
            return post.id
        except SQLAlchemyError as e:
            await self.session.rollback()  # Откат, если была ошибка
            print(f"❌ Ошибка при сохранении поста: {e}")
            return None
    
    # async def get_count_all_posts(self) -> int:
    #     stmt = select(func.count(Post.id))
    #     result = await self.session.execute(stmt)
    #     return result.scalar()
    
    async def get_all_posts_id(self) -> list[int]:
        stmt = select(Post.id)
        result = await self.session.execute(stmt)
        ids = result.scalars().all()
        return ids
    

    async def get_post_by_id(self, id:int) -> list[Post]:
        stmt = select(Post).filter(Post.id == id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
        