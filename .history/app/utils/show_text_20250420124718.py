


def show_text


  text = '\n\n'.join(
                    f'<b>Post #{post.id}\nTitle</b>: {post.title}\n<b>Text</b>: {post.body}'
                    for post in posts
                )