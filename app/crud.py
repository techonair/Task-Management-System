from sqlalchemy.orm import Session
from app import models, schemas
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate
from app.database import SessionLocal

def create_task(db: Session, task: schemas.TaskCreate):
    new_task = models.Task(**task.dict())
    db.add(new_task)
    try:
        db.commit()
        db.refresh(new_task)
        return new_task
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Task with title '{task.title}' already exists."
        )

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: UUID):
    # print(f"Task: {db.query(models.Task).filter(models.Task.id == task_id).first()}")
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# def get_task_by_id(db: Session, task_id: UUID):
#     return db.query(models.Task).filter(models.Task.id == task_id)

def update_task(db: Session, db_task: models.Task, updates: schemas.TaskUpdate):
    # print(f"Debug: {updates.dict(exclude_unset=True).items()}")
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: UUID):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
        return True
    return False