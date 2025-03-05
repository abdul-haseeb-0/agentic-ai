from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.database import engine, sessions # import database connection
from models.todos_models import Todo # import model class

app = FastAPI()

def get_db(): # create function to get database connection
    db = sessions()
    try:
        yield db
    finally:
        db.close()

class CreateTodo(BaseModel): # create class to validate request body
    title : str
    description : str
    completed : bool = False

@app.post("/todos/create")
def create_todo( todo: CreateTodo, db: Session = Depends(get_db)):
    try:
        new_todo = Todo(
            title=todo.title,
            description=todo.description,
            completed=todo.completed
        )
        db.add(new_todo) # add new todo to database
        db.commit() # commit changes
        db.refresh(new_todo) # refresh database
        return new_todo
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )