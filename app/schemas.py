from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str
    description: str | None
    priority: int = Field(default=1, ge=1, le=5)
    category: str | None

class TaskEdit(BaseModel):
    title: str
    description: str | None
    priority: int = Field(default=1, ge=1, le=5)
    category: str | None
    completed: bool