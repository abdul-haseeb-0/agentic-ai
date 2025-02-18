from fastapi import FastAPI
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import datetime
import os


load_dotenv() # load env
app = FastAPI() 

# get data from user to created tode using body param
class get_todo(BaseModel):
    title : str

def get_mongodb_uri(): # making connection with mongodb
    try:
        client = MongoClient(os.getenv("MongoDB_URI"))
        return client
    except Exception as e:
        return {
            "status" : "Error",
            "message" : str(e)
            }
client = get_mongodb_uri()

# making connection with DB
db = client["mongodb_no_sql_learning"] 

# check server status
@app.get("/")
def read_root():
    return {
        "status" : "Server is Running."
    }

# show all data in todos collection.
@app.get("/todos")
def read_todos():
    try:
        todos = db.todos.find()
        list_todos = []
        for todo in todos:
            list_todos.append({
                "id" : str(todo["_id"]),
                "title" : todo["title"],
                "created at" : todo["created_at"]
            })
        return {
            "status" : "successful",
            "data" : list_todos
        }
    except Exception as e:
        return{
            "status" : "error",
            "message" : str(e)
        }

# find todos by id via path param
@app.get("/todos/{id}")
def read_todos_via_id( id: str ):
    try:
        todo = db.todos.find_one({"_id" : ObjectId(id)})
        if todo is None:
            return {
                "message" : "todo not found"
            }
        return {
            "data" : {
                "id" : str(todo["_id"]),
                "title" : todo["title"],
                "created at" : todo["created_at"]
            }
        }
    except Exception as e:
        return {
            "status" :"error",
            "message" : str(e)
            }

# find todo by title using query parameter
@app.get("/todos/title") 
def read_todo_via_title( title: str):
    try:
        todo = db.todos.find_one({"_id" : title})
        if todo is None:
            return {
                "message" : "todo not found"
            }
        return {
            "data" : {
                "id" : str(todo["_id"]),
                "title" : todo["title"],
                "created at" : todo["created_at"]
            }
        }
    except Exception as e:
        return {
            "status" :"error",
            "message" : str(e)
            }
    
# creating todo
@app.post("/todos/create")
def create_todo(todo: get_todo):
    try:
        todos = db.todos.insert_one({
        "title" : todo.title,
        "created at" : str(datetime.now())
        })
        return {
            "status" : "Successful",
            "data" : {"id": str(todos.inserted_id)},
            "message" : "Todo created"
        }
    except Exception as e:
        return {
            "status" :"error",
            "message" : str(e)
            }

# delete todo
@app.delete("/todos/delete/{id}")
def delete_todo(id: str):
    try:
        todos = db.todos.delete_one({"_id": ObjectId(id)})
        if todos.deleted_count == 0:
            return {
                "status": "error",
                "message": "Todo not found"
                }
        return {
            "status": "success",
            "message": "Todo deleted successfully"
            }
    except Exception as e:
        return {
            "status" :"error",
            "message" : str(e)
            }

# update
@app.put("/todos/update/{id}")
def update_todo(id: str, todo: get_todo):
    try:
        todos = db.todos.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "title": todo.title
                }
            }
        )
        if todos.modified_count == 0:
            return {
                "status": "failed",
                "message": "Todo not found",
                }
        return {
            "status": "successful",
            "message": "Todo updated successfully",
            }
    except Exception as e:
        return {
            "status" :"error",
            "message" : str(e)
            }