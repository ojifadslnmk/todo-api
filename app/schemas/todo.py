from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TodoBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
