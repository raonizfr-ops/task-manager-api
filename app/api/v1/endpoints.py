from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from ... import crud, schemas
from ...database import get_db

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

# Rota para criar uma nova tarefa
@router.post("/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova tarefa.
    """
    return crud.create_task(db=db, task=task)

# Rota para ler todas as tarefas (com filtro opcional por status)
@router.get("/", response_model=List[schemas.Task])
def read_tasks(
    skip: int = 0, 
    limit: int = 100, 
    status: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    """
    Lista todas as tarefas, com opção de filtrar por status (pending, in_progress, completed).
    """
    tasks = crud.get_tasks(db, skip=skip, limit=limit, status=status)
    return tasks

# Rota para ler uma tarefa específica
@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma tarefa específica pelo ID.
    """
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Rota para atualizar uma tarefa
@router.put("/{task_id}", response_model=schemas.Task)
def update_existing_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """
    Atualiza uma tarefa existente.
    """
    db_task = crud.update_task(db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Rota para deletar uma tarefa (soft delete)
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    """
    Deleta (soft delete) uma tarefa.
    """
    db_task = crud.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return

