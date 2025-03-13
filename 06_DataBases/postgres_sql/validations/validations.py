from pydantic import BaseModel, Field
from typing_extensions import Annotated

# create class to validate request body
class CreateTodo(BaseModel):
    title: str
    description: str
    completed: bool = False
    user_id: int

class CreateUser(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50)]
    email: Annotated[str, Field(pattern=r'^\S+@\S+$')]
    password: Annotated[str, Field(min_length=6)]

class UserLogin(BaseModel):
    email: str
    password: str