from app.google.sheet_helpers import append_row_to_sheet, append_rows_to_sheet, clear_sheet, delete_row_from_sheet
from app.models.post import Post
from app.schemas.post import PostSchema
from sqlalchemy import select, func, text, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError

class PostRepository:
    """
    Репозиторий для управления записями Post в базе данных и синхронизации с Google Sheets.
    """

    def __init__ (self, session:AsyncSession):
        """
        Инициализация репозитория с сессией SQLAlchemy.
        :param session: Асинхронная сессия SQLAlchemy.
        """
        self.session = session

    async def save_many(self, posts: list[PostSchema]) -> None:
        """
        Сохраняет список постов в базу данных и Google Sheets (bulk-режим).
        :param posts: Список схем постов.
        """
        post_dicts = [post.model_dump() for post in posts]
        stmt = insert(Post).values(post_dicts).on_conflict_do_nothing(index_elements=['id'])

        await self.session.execute(stmt)
        await self.update_id_seq()
        await self.session.commit()
        await append_rows_to_sheet(post_dicts)


    async def update_id_seq(self):
        """
        Обновляет счётчик последовательности ID в таблице posts.
        """
        await self.session.execute(
            text("SELECT setval('posts_id_seq', COALESCE((SELECT MAX(id) FROM posts), 1))")
        )


    async def get_posts_paginated(self, offset: int = 0, limit: int = 5) -> list[Post]:
        """
        Получает посты с пагинацией.
        :param offset: Смещение (по умолчанию 0).
        :param limit: Количество постов (по умолчанию 5).
        :return: Список объектов Post.
        """
        stmt = select(Post).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    
    async def del_post_by_id(self, id:int) -> bool:
                """
        Удаляет пост по ID из базы и из Google Sheets.

        :param id: ID поста.
        :return: True, если пост был удалён.
        """
        stmt = delete(Post).where(Post.id == id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        await delete_row_from_sheet(id)
        return result.rowcount > 0


    async def del_all_posts(self) -> bool:
        stmt = delete(Post)
        result = await self.session.execute(stmt)
        await self.session.commit()
        await clear_sheet()
        return result.rowcount > 0
    

    async def save_one(self, post: Post) -> int | None:
        try:
            await self.update_id_seq()
            self.session.add(post)
            await self.session.commit()
            await append_row_to_sheet(post)
            return post.id
        except SQLAlchemyError as e:
            await self.session.rollback()  # Откат, если была ошибка
            print(f"❌ Ошибка при сохранении поста: {e}")
            return None
    

    async def get_all_posts_id(self) -> list[int]:
        stmt = select(Post.id)
        result = await self.session.execute(stmt)
        ids = result.scalars().all()
        return ids
    

    async def get_post_by_id(self, id:int) -> list[Post]:
        stmt = select(Post).filter(Post.id == id)
        result = await self.session.execute(stmt)
        return result.scalars().all()
        