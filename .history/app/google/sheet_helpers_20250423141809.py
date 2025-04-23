from app.google.sheet_sync import _append_row_sync, _appnd_rows_sync, _delete_row_sync
from app.models.post import Post
from app.google.sheets_service import get_sheet
from typing import Callable, Any
import asyncio


async def run_loop(action:Callable, post:Any):
      loop = asyncio.get_running_loop()
      sheet = get_sheet()
      await loop.run_in_executor(None, action, post, sheet)

     
async def append_row_to_sheet(post: Post):
    await run_loop(action=_append_row_sync,post=post)


async def append_rows_to_sheet(posts:list[dict]):
      await run_loop(action=_appnd_rows_sync,post=posts)



async def delete_row_from_sheet(post_id:int):
      await run_loop(action=_delete_row_sync, post=post_id)


async def clear_sheet():
     await run_loop(action=_delete_all_table)
     


_delete_all_table
