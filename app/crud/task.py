from sqlalchemy.orm import Session
from .. import models, schemas

# Cria uma nova tarefa
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Obtém uma tarefa pelo ID
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id, models.Task.is_deleted == False).first()

# Obtém todas as tarefas (com opção de filtro por status)
def get_tasks(db: Session, skip: int = 0, limit: int = 100, status: str = None):
    query = db.query(models.Task).filter(models.Task.is_deleted == False)
    if status:
        query = query.filter(models.Task.status == status)
    return query.offset(skip).limit(limit).all()

# Atualiza uma tarefa
def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task:
        # Atualiza apenas os campos que foram fornecidos no body da requisição
        update_data = task.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_task, key, value)
        
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

# "Deleta" uma tarefa (soft delete)
def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.is_deleted = True # Soft delete
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

