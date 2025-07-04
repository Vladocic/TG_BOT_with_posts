from app.google.sheet_sync_actions import _append_row_sync, _append_rows_sync, _delete_all_table, _delete_row_sync
from app.models.post import Post
from app.google.sheets_service import get_sheet
from typing import Callable, Any
import asyncio


async def run_sync_in_executor(action:Callable, *args):
      loop = asyncio.get_running_loop()
      sheet = get_sheet()
      await loop.run_in_executor(None, action, *args, sheet)

     
async def append_row_to_sheet(post: Post):
    await run_sync_in_executor(action=_append_row_sync, (post)


async def append_rows_to_sheet(posts:list[dict]):
      await run_sync_in_executor(action=_append_rows_sync,post=posts)



async def delete_row_from_sheet(post_id:int):
      await run_sync_in_executor(action=_delete_row_sync, post=post_id)


async def clear_sheet():
     await run_sync_in_executor(action=_delete_all_table, post=None)
     


