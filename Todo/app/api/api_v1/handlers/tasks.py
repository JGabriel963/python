from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail, TaskCreate
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from services.task_service import TaskService
from models.task_model import Task

task_router = APIRouter()

@task_router.get("/", summary="Lista de Tarefas", response_model=list[TaskDetail])
async def list_tasks(user: User = Depends(get_current_user)):
    return await TaskService.list_tasks(user)

@task_router.post("/create", summary="Adicionar Tarefa", response_model=Task)
async def create_task(*, user: User = Depends(get_current_user), data: TaskCreate):
    return await TaskService.create_task(user, data)