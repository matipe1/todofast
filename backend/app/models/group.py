from pydantic import BaseModel

class Group(BaseModel):
    group_id: int
    title: str | None = f"Group {group_id}"