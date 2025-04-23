from pydantic import BaseModel

class PostSchema(BaseModel):
    user_id: int
    title: str
    body: str
