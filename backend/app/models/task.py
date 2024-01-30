from pydantic import BaseModel

class Task(BaseModel):
    id: str
    title: str | None = ''
    description: str | None = ''
    completed: bool = False
    
    # status: str | None = "Open" -> Open - In progress - Complete
    # priority: int | None = None -> 1 - 2 - 3 
    # tags: list[str]

    # created_at: DateTime
    # due_date: Date or datetime -> When task should be completed by

    # assignee: Foreign key -> relate what user is assigned to the task
    # list_id: Foreign key -> relate task to what todo list it belongs to