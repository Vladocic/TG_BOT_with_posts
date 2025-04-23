from app.models.post import Post
from app.google.sheets_service import get_sheet
import asyncio


def _append_row_sync(post: Post):
    sheet = get_sheet()
    sheet.append_row([
        str(post.id),
        str(post.user_id),
        post.title,
        post.body
    ])


async def append_row_to_sheet(post: Post):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, _append_row_sync, post)



async def append_rows_to_sheet(posts:list[Post]):
      loop = asyncio.get_running_loop()
      await loop.ru
      pass

async def delete_row_from_sheet(post_id:int):
      pass

async def clear_sheet():
     pass