


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

  