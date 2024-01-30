from fastapi import FastAPI
from routers import tasks

app = FastAPI()

app.include_router(tasks.router)


# Greetings
@app.get("/")
async def root():
    return {"message": "Hello World"}

