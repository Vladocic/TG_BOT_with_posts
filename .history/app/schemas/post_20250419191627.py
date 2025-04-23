from pydantic import BaseModel

class f(BaseModel):
    user_id: int
    title: str
    body: str
