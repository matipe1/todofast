from fastapi import FastAPI
from routers.tasks import task_router
from routers.groups import group_router

app = FastAPI()
app.include_router(task_router)
app.include_router(group_router)


@app.get("/")
async def root():
    return {"status": "Todo API is Running..."}

