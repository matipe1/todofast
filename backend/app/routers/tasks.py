from fastapi import APIRouter


task_router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

# DB example:
task_list = [
    {
        "task_id": 1,
        "title": "Do the bed",
        "done": True
    },
    {
        "task_id": 2,
        "title": "Do the dishes",
        "done": False
    },
    {
        "task_id": 3,
        "title": "Workout"
    },
]

# Read
@task_router.get('/')
async def all_tasks():
    return "Not Implemented"


# Create
@task_router.post('/')
async def post_task():
    return "Not Implemented"


# Update a task
@task_router.put('/{key}')
async def update_task(key: int):
    return "Not Implemented"

 
# Delete a task
@task_router.delete('/{key}')
async def delete_task(key):
    return "Not Implemented"