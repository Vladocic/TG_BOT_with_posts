from app.models.post import Post
from app.schemas.post import PostSchema
from sqlalchemy.ext.asyncio import AsyncSession


#save_many(posts: list[PostSchema])