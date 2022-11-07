from fastapi import APIRouter, status
from schemas.task_schemas import TaskSchema
from models.taskM import tasks
from typing import List
from config.db import connec

router = APIRouter()

@router.get(
    path = "/tasks",
    response_model = List[TaskSchema],
    status_code = status.HTTP_200_OK
    )
async def get_tasks(data_task: TaskSchema):
    connec.execute(data_task.select()).fetchall()

@router.get(
    path = "/task/{id}",
    response_model = TaskSchema,
    status_code = status.HTTP_200_OK)
async def get_task(id: int):
    pass

@router.post(
    path = "/task",
    status_code = status.HTTP_200_OK)

async def create_task(data_task: TaskSchema):
    new_task = {"title": data_task.title, "content": data_task.content, "done": data_task.done}
    result = connec.execute(tasks.insert().values(new_task))
    print(f"Aca empieza los results:\n{result}")
    return "Success!"

@router.delete(
    path = "/task/{id}",
    status_code = status.HTTP_204_NO_CONTENT)
async def delete_task(id: int):
    pass

@router.put(
    path = "/task/{id}",
    response_model= TaskSchema,
    status_code = status.HTTP_200_OK)
async def update_task(id: int):
    pass