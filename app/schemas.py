from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    status: TaskStatus = TaskStatus.pending

class TaskUpdate(BaseModel):
    title: Optional[str]
    status: Optional[TaskStatus]

class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True