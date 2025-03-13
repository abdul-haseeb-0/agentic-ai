from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from validations.validations import CreateTodo
from utils.utilities import verify_token
from models.models import Todo, Users

todos_router = APIRouter()

# route to get all todos
@todos_router.get("/", dependencies=[Depends(verify_token)] )
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

# route to create todo by id connected with user
@todos_router.get("/create")
def create_todo( todo: CreateTodo, user = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        user = db.query(Users).filter(Users.id == todo.user_id).first() #   filter user from Users Table
        if not user:
            raise HTTPException( status_code = 404, detail= "User not found")
        if Users.email != todo.user_email:
            raise HTTPException( status_code = 404, detail= "Invalid email or password")
        if Users.password != todo.user_password:
            raise HTTPException( status_code = 404, detail= "Invalid email or password")   
        new_todo = Todo(
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            user_id = todo.user_id
        )
        db.add(new_todo) # add new todo to database
        db.commit() # commit changes
        db.refresh(new_todo) # refresh database
        return {
            "data" : new_todo,
            "status" : "success",
            "message" : " todo creates"}
    except Exception as e:
        return {
            "message": str(e),
            "status": "error",
            "data": None
        }

# route to update todo by id
@todos_router.put("/{todo_id}", dependencies=[Depends(varify_token)])
def update_todo(todo_id: int, todo_update: CreateTodo, user = Depends(varify_token), db: Session = Depends(get_db)):
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
@todos_router.delete("/{todo_id}", dependencies=[Depends(varify_token)])
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

