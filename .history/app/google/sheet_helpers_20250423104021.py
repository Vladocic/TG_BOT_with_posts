from app.models.post import Post
from app.google.sheets_service import get_sheet


async def append_row_to_sheet(post:Post):
    sheet = get_sheet()
    sheet.ap
    pass

async def append_rows_to_sheet(posts:list):
      pass

async def delete_row_from_sheet(post_id:int):
      pass

async def clear_sheet():
     pass