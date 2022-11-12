from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskSchema(BaseModel):
    id: Optional[int]
    title: str
    content: str
    type: str
    created: datetime = datetime.now().strftime("%d/%m/%Y")


    