from fastapi import APIRouter, HTTPException, status
from models.task import Task

router = APIRouter(prefix='/tasks')


# Create
@router.post('/', )
async def add_task():
    return

# Read
@router.get('/', response_model=list[Task])
async def read_tasks():
    return
    # try:
    #     return a task in database
    # except:
    #     raise HTTPException(...)



# @router.get('/{task_id}', response_model=Task)
# async def read_task(task_id):
#     return
#     try:
#         return task in database
#     except:
#         raise HTTPException(...)


# Update a task
@router.patch('/')
async def update_task():
    return

# Delete a task
@router.delete('/{task_id}')
async def delete_task(task_id):
    return
    # try:
    #     delete
    #     return {"msg": "Task deleted successfully"}

    # except:
    #     raise HTTPException(...)
