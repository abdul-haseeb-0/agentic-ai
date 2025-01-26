from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import re

app = FastAPI()

# Student Registeration Information Class
class stuRegInfo(BaseModel):
    name : str
    email : str
    age: int
    course : list[str]

# email Update
class emailUpdate(BaseModel):
    email : str

# Get Student ID, Grade, Session
@app.get("/students/{student_id}")
def Stu_info( student_id: int, include_grades: Optional[bool]=None, semester: Optional[str]=None ):
    try:
        if not (1000 < student_id < 9999):
            raise HTTPException(
                status_code=422,
                detail="Invalid ID, Student ID must be between 1000 and 9999."
            )
        if include_grades:
            if include_grades is not True or False:
                raise HTTPException(
                    status_code=422,
                    detail = "You can give only True and False value."                
                    )
        if semester:
            if not re.match(r"^(Fall|Spring|Summer)\d{4}$", semester):
                raise HTTPException(
                    status_code=422,
                    detail="Invalid semester format. Valid format: Fall2025, Spring2024, or Summer2023."
                )
        return {
            "Status": "OK",
            "Data": {
                "Student ID": student_id,
                "Include Grade": include_grades,
                "semester": semester
            }
        }
    except Exception as e:
        return{
            "Status" : "error",
            "Message" : str(e),
            "Data" : None
        }
# URL: http://127.0.0.1:8000/students/5000?grade=True&session=Spring2024



# student registeratuion
@app.post("/students/register")
def stu_reg( studRegInfo : stuRegInfo):
    try:
        # Name Validation
        if not(1<len(studRegInfo.name)<50) and not all(char.isalpha() or char.isspace() for char in studRegInfo.name):
                raise HTTPException(
                    status_code=422,
                    detail = "Name must be between 1 to 50 characters and must contain only alphabets and spaces"        
                    )
        # Age Validation
        if not(18<=studRegInfo.age<=30):
            raise HTTPException(
                    status_code=422,
                    detail = "Age must be between 18 and 30"
                    )
        # Email Validation
        if not "@gmail.com" in studRegInfo.email:
            raise HTTPException(
                    status_code=422,
                    detail = "Invalid Email format"
                    )
        # Course Validation
        if not(1<=len(studRegInfo.course)<=5):
            raise HTTPException(
                    status_code=422,
                    detail = "Courses list must be between 1 and 5 courses"
                    )
        if len(set(studRegInfo.course)) != len(studRegInfo.course):
            raise HTTPException(
                    status_code=422,
                    detail = "No Duplictate cources allowed"
                    )
        for course in studRegInfo.course:
            if not(5<=len(course)<=50):
                raise HTTPException(
                    status_code=422,
                    detail = "Each course name should be between 5-30 characters."
                    )
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
# URL : http://127.0.0.1:8000/students/register 
# Json : 
#     {
#     "name": "Alice Smith",
#     "email": "alice.smith@example.com",
#     "age": 25,
#     "course": [
#         "Physics",
#         "Chemistry"
#     ]
# }

# Update Email
@app.put("/students/{student_id}/email")
def update_email(student_id : int , email : emailUpdate  ):
    try:
        if not(1000 < student_id < 9999):
            raise HTTPException(
                status_code = 422,
                detail = "Invalid ID, Student ID must be between 1000 and 9999."
            )
        if not "@gmail.com" in email.email:
            raise HTTPException(
                    status_code=422,
                    detail = "Invalid Email format"
                    )
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