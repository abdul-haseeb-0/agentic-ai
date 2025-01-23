from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Student Registeration Information
class stuRegInfo(BaseModel):
    name : str
    email : str
    age: int
    course : list[str]

# email Update
class emailUpdate(BaseModel):
    update_email : str


# Get Student ID, Grade, Session
@app.get("/students/{student_id}")
def Stu_info(student_id : int,grade : Optional[bool] = None ,session : Optional[str] = None ):
    try:
        if not (1000<student_id<9999):
            raise ValueError("Invalid ID")
        return{
            "Status" : "OK",
            "Data" : {
                "Student ID" : student_id,
                "Grade" : grade,
                "Session" : session
            }
        }
    except Exception as e:
        return{
            "Status" : "error",
            "Message" : str(e),
            "Data" : None
        }
# Use http://127.0.0.1:8000/students/5000?grade=True&session=Spring2024 on postman app.



# student registeratuion
@app.post("/students/register")
def stu_reg( studRegInfo : stuRegInfo):
    try:
        if not(1<len(studRegInfo.name)<50):
            raise ValueError("Name must be between 1 to 50 characters")
        if not all(char.isalpha() or char.isspace() for char in studRegInfo.name):
            raise ValueError("Name must contain only alphabets and spaces")
        if not(18<=studRegInfo.age<=30):
            raise ValueError("Age must be between 18 and 30")
        if not "@" in studRegInfo.email:
            raise ValueError("Invalid Email")
        if not(1<=len(studRegInfo.course)<=5):
            raise ValueError("Courses list must be between 1 and 5 courses")
        if len(set(studRegInfo.course)) != len(studRegInfo.course):
            raise ValueError("No Duplictate cources allowed")
        return{
            "Status" : "OK",
            "Registeration Data" : studRegInfo
        }
    except Exception as e:
        return{
            "Status" : "error",
            "Message" : str(e),
            "Data" : None
        }
# Use http://127.0.0.1:8000/students/register on postman app.
# Json : 
#     {
#     "name": "Alice Smith",
#     "email": "alice.smith@example.com",
#     "age": 25,
#     "course": [
#         "Python",
#         "Pyhon"
#     ]
# }

# Update Email
@app.put("/students/{student_id}/email")
def update_email(student_id : int , email : emailUpdate  ):
    try:
        if not(1000 < student_id < 9999):
            raise ValueError("Invalid ID")
        if not "@" in email.update_email:
            raise ValueError("Invalid Email") 
        return{
            "Status" : "OK",
            "Updated Email" : email
        }
    except Exception as e:
                return{
            "Status" : "error",
            "Message" : str(e),
            "Data" : None
        }
# Use http://127.0.0.1:8000/students/5555/email on postman.
# Json : { "update_email": "new.email@example.com" }