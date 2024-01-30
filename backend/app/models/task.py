from pydantic import BaseModel

class Task(BaseModel):
    task_id: int
    title: str | None = f"Task {task_id}"
    done: bool | None = False

    # description: str | None = ""
    # status: str | None = "Open" -> Open - In progress - Complete
    # priority: int | None = None -> 1 - 2 - 3 
    # tags: list[str]

    # created_at: DateTime
    # due_date: Date or datetime -> When task should be completed by

    # assignee: Foreign key -> relate what user is assigned to the task
    # todo_id: Foreign key -> relate task to what todo list it belongs to