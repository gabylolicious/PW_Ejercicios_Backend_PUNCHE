from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="",
    tags=["Ejercicio 1 - Tasks"]
)

tasks_repertory : dict[str, "Task"] = {}

class Task(BaseModel):
    id : str
    title : str
    description : Optional[str] = None # opcional, puede o no enviarse al backend
    priority : int = Field(..., ge=1, le=5)  # obligatorio, valor entre 1 y 5
    completed : bool = False  # por defecto es False

class TaskCreate(BaseModel):
    title : str
    description : Optional[str] = None # opcional, puede o no enviarse al backend
    priority : int = Field(..., ge=1, le=5)  # obligatorio, valor entre 1 y 5

# Endpoint 1
@router.post("/tasks")
async def create_task(payload : TaskCreate):
    task_id = str(uuid4())

    task = Task(
        id = task_id,
        title = payload.title,
        description = payload.description,
        priority = payload.priority,
        completed = False
    )

    tasks_repertory[task_id] = task
    return {
        "msg" : "Task creado exitosamente",
        "data" : task
    }

# Endpoint 2
@router.get("/tasks/{task_id}")
async def get_task(task_id : str):
    task = tasks_repertory.get(task_id)
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task no encontrada"
        )
    
    return {
        "msg" : "Task creado exitosamente",
        "data" : task
    }