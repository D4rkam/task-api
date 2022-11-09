from fastapi import APIRouter, status, Response
from starlette.status import HTTP_204_NO_CONTENT 
from schemas.taskSchemas import TaskSchema
from models.taskModels import tasks
from typing import List
from config.db import connec

router = APIRouter()

@router.get(
    path = "/api/tasks",
    response_model = List[TaskSchema],
    status_code = status.HTTP_200_OK)

async def get_tasks():
    return connec.execute(tasks.select()).fetchall() #Trae todo

@router.get(
    path = "/api/task/{id}",
    response_model = TaskSchema,
    status_code = status.HTTP_200_OK)

async def get_task(id: int):
    return connec.execute(tasks.select().where(tasks.c.id == id)).first()

@router.post(
    path = "/api/task",
    response_model = TaskSchema,
    status_code = status.HTTP_200_OK)

async def create_task(data_task: TaskSchema):
    new_task = {"title": data_task.title, "content": data_task.content, "done": data_task.done}
    result = connec.execute(tasks.insert().values(new_task))
    return connec.execute(tasks.select().where(tasks.c.id == result.lastrowid)).first()

@router.delete(
    path = "/api/task/{id}",
    status_code = status.HTTP_204_NO_CONTENT)

async def delete_task(id: int):
    connec.execute(tasks.delete().where(tasks.c.id == id))
    return Response(status_code = HTTP_204_NO_CONTENT)

@router.put(
    path = "/api/task/{id}",
    response_model= TaskSchema,
    status_code = status.HTTP_200_OK)

async def update_task(id: int, data_taks: TaskSchema):
    connec.execute(tasks.update().values(title=data_taks.title, content=data_taks.content, done=data_taks.done).where(tasks.c.id == id))
    return connec.execute(tasks.select().where(tasks.c.id == id)).first()



    