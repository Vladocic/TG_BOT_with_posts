from pydantic import BaseModel

class PostSchema(BaseModel):
    id
    user_id: int
    title: str
    body: str
