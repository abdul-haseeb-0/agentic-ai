from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from validations.validations import CreateTodo
from utils.utilities import verify_token
from models.models import Todo, Users

todos_router = APIRouter()

# route to get all todos
@todos_router.get("/", dependencies=[Depends(verify_token)])
def get_todos(db: Session = Depends(get_db)):
    try:
        todos = db.query(Todo).all()
        return {
            "data": todos,
            "message": "Todos fetched successfully",
            "status": "success"
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

# route to create todo
@todos_router.post("/create")
def create_todo(todo: CreateTodo, user = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        valid_user = db.query(Users).filter(Users.id == todo.user_id).first() # filter user from Users Table
        if not valid_user:
            raise HTTPException(status_code=404, detail="User not found")
        new_todo = Todo(
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            user_id=todo.user_id
        )
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return {
            "data": new_todo,
            "status": "success",
            "message": "Todo created"
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

# route to update todo by id
@todos_router.put("/{todo_id}", dependencies=[Depends(verify_token)])
def update_todo(todo_id: int, todo_update: CreateTodo, user = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")

        todo.title = todo_update.title
        todo.description = todo_update.description
        todo.completed = todo_update.completed
        db.commit()
        db.refresh(todo)
        return {
            "data": todo,
            "message": "Todo updated successfully",
            "status": "success"
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

# route to delete todo by id
@todos_router.delete("/{todo_id}", dependencies=[Depends(verify_token)])
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")

        db.delete(todo)
        db.commit()
        return {
            "message": "Todo deleted",
            "status": "success"
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

