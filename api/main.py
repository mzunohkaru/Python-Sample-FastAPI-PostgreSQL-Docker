from fastapi import FastAPI
from os import environ as env

from api.routers import task, done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)

@app.get("/")
def index():
    return {"Secret": f"{env['MY_VARIABLE']}"}