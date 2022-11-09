from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    id: Optional[int]
    title: str
    content: str
    done: bool



    