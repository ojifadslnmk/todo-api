from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.schemas.response import APIResponse
from app.services import todo_service

router = APIRouter(prefix="/api/todos", tags=["Todos"])


@router.get("/", response_model=APIResponse[List[TodoResponse]])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = todo_service.get_todos(db, skip=skip, limit=limit)
    return {
        "success": True,
        "data": todos,
        "message": "Todos retrieved successfully"
    }


@router.get("/{todo_id}", response_model=APIResponse[TodoResponse])
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {
        "success": True,
        "data": todo,
        "message": "Todo retrieved successfully"
    }


@router.post("/", response_model=APIResponse[TodoResponse], status_code=201)
def create_todo(todo_in: TodoCreate, db: Session = Depends(get_db)):
    todo = todo_service.create_todo(db, todo_in)
    return {
        "success": True,
        "data": todo,
        "message": "Todo created successfully"
    }


@router.put("/{todo_id}", response_model=APIResponse[TodoResponse])
def update_todo(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated_todo = todo_service.update_todo(db, todo, todo_in)

    return {
        "success": True,
        "data": updated_todo,
        "message": "Todo updated successfully"
    }


@router.delete("/{todo_id}", response_model=APIResponse[None])
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_service.delete_todo(db, todo)

    return {
        "success": True,
        "data": None,
        "message": "Todo deleted successfully"
    }


@router.patch("/{todo_id}/toggle", response_model=APIResponse[TodoResponse])
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.completed = not todo.completed
    db.commit()
    db.refresh(todo)

    return {
        "success": True,
        "data": todo,
        "message": "Todo completion status toggled successfully"
    }
