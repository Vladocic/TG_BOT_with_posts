from app.google.sheets_service import get_sheet
from app.models.post import Post


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
      rows = [ 
            [str(post["id"]), str(post["user_id"]),post["title"],post["body"]]
            for post in posts
      ]
      sheet.append_rows(rows)


def _delete_row_sync(post_id: int):
    sheet = get_sheet()
    records = sheet.get_all_records()

    for idx, row in enumerate(records, start=2):  # Начинаем с 2, т.к. 1 — это заголовок
        if str(row.get("id")) == str(post_id):
            sheet.delete_rows(idx)
            break