from app.models.post import Post
from app.google.sheets_service import get_sheet
from typing import Callable, Any
import asyncio


def _append_row_sync(post: Post):
    sheet = get_sheet()
    sheet.append_row([
        str(post.id),
        str(post.user_id),
        post.title,
        post.body
    ])

def _appnd_rows_sync(posts:list[dict]):
      sheet = get_sheet()
      for post in posts:
            sheet.append_rows([
            str(post["id"]),
            str(post.[]),
            post.title,
            post.body
      ])
     pass


async def append_row_to_sheet(post: Post):
    await run_loop(action=_append_row_sync(post),post=post)



async def append_rows_to_sheet(posts:list[Post]):
      await run_loop()
      loop = asyncio.get_running_loop()
      await loop.run_in_executor()
      pass

async def delete_row_from_sheet(post_id:int):
      pass

async def clear_sheet():
     pass



async def run_loop(action:Callable, post:Any):
      loop = asyncio.get_running_loop()
      await loop.run_in_executor(None, action, post)

     