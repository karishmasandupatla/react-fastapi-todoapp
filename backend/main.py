from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for all origins (for React to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class Task(BaseModel):
    title: str

# In-memory task list
tasks = []

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# Add a new task
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.dict())
    return {"message": "Task added"}

# Update a task by index
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = updated_task.dict()
    return {"message": "Task updated"}

# Delete a task by index
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.pop(task_id)
    return {"message": "Task deleted"}
