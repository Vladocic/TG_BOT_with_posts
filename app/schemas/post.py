from pydantic import BaseModel

class PostSchema(BaseModel):
    id: int
    user_id: int
    title: str
    body: str
