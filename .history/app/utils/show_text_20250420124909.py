from app.schemas.post import PostSchema



def show_text(posts:list[PostSchema]) -> str:
  
  


  text = '\n\n'.join(
                    f'<b>Post #{post.id}\nTitle</b>: {post.title}\n<b>Text</b>: {post.body}'
                    for post in posts
                )