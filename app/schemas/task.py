from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Schema Base para criação e atualização (o que o usuário envia)
class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: str = Field("pending", pattern="^(pending|in_progress|completed)$")

# Schema para criação (herda de TaskBase)
class TaskCreate(TaskBase):
    pass

# Schema para atualização (herda de TaskBase, todos os campos opcionais)
class TaskUpdate(TaskBase):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[str] = Field(None, pattern="^(pending|in_progress|completed)$")

# Schema para leitura (o que a API retorna)
class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    class Config:
        from_attributes = True # Permite que o Pydantic leia dados de um objeto SQLAlchemy

