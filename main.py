from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Setting up the Jinja2 templates
templates = Jinja2Templates(directory="templates")

class Task(BaseModel):
    id: str
    content: str

_id = -1
tasks: List[Task] = []

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/create/task")
async def create_task(content: str = Form(...)):
    global _id
    _id += 1
    task = Task(id=_id, content=content)
    tasks.append(task)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/task/{id}")
async def delete_task(id: int):
    if id >= 0 and id < len(tasks):
        tasks.pop(id)
    return RedirectResponse(url="/", status_code=303)

@app.get("/api/tasks")
async def get_tasks() -> List[Task]:
    return tasks
