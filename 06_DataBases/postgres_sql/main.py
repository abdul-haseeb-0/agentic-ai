from fastapi import FastAPI
from dotenv import load_dotenv
from routes import todos_routes,users_routes
import os

load_dotenv()

app = FastAPI()

app.include_router(todos_routes.todos_router, prefix = "/todos", tags = ["Todos"])
app.include_router(users_routes.users_router, prefix = "/users", tags = ["Users"])