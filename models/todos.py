from pydantic import BaseModel

class Todo(BaseModel):
    Work: str
    need: str
    completed: bool

