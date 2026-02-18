from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo_in: TodoCreate):
    todo = Todo(**todo_in.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(db: Session, todo: Todo, todo_in: TodoUpdate):
    update_data = todo_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: Todo):
    db.delete(todo)
    db.commit()

def get_todo_stats(db: Session):
    total = db.query(func.count(Todo.id)).scalar()
    completed = db.query(func.count(Todo.id)).filter(Todo.completed == True).scalar()
    pending = total - completed if total is not None and completed is not None else 0

    return {
        "total": total or 0,
        "completed": completed or 0,
        "pending": pending or 0
    }
