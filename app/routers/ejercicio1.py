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
    complete : bool = False  # por defecto es False

class Task(BaseModel):
    id : str
    title : str
    description : Optional[str] = None # opcional, puede o no enviarse al backend
    priority : int = Field(..., ge=1, le=5)  # obligatorio, valor entre 1 y 5
    complete : bool = False  # por defecto es False

@router.post("/tasks")
async def create_task(payload : Task):
    task_id = str(uuid4())

    task = Task(
        id = task_id,
        title = payload.title,
        description = payload.description,
        priority = payload.priority,
        complete = False
    )