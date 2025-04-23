from app.google.sheets_service import get_sheet
from app.models.post import Post


def _append_row_sync(post: Post, sheet):
    sheet.append_row([
        str(post.id),
        str(post.user_id),
        post.title,
        post.body
    ])


def _append_rows_sync(posts:list[dict], sheet):
      rows = [ 
            [str(post["id"]), str(post["user_id"]),post["title"],post["body"]]
            for post in posts
      ]
      sheet.append_rows(rows)


def _delete_row_sync(post_id: int, sheet):
    records = sheet.get_all_records()

    for idx, row in enumerate(records, start=2):  # Начинаем с 2, т.к. 1 — это заголовок
        if str(row.get("ID")) == str(post_id):
            sheet.delete_rows(idx)
            break


def _delete_all_table(sheet):
    num_rows = len(sheet.get_all_values())
    if num_rows > 1:
        sheet.batch_clear([f"A2:D{num_rows}"])

