from fastapi import APIRouter


group_router = APIRouter(prefix="/api/groups", tags=["Groups"])

# DB example:
group_list = [
    {
        "group_id": 1,
        "title": "Daily"
    },
    {
        "group_id": 2,
        "title": "University"
    },
    {
        "group_id": 3
    },
]


# Read
@group_router.get('/')
async def all_groups():
    return "Not Implemented"


# Create
@group_router.post('/')
async def post_group():
    return "Not Implemented"


# Update a task
@group_router.put('/{key}')
async def update_group(key: int):
    return "Not Implemented"

 
# Delete a task
@group_router.delete('/{key}')
async def delete_group(key):
    return "Not Implemented"