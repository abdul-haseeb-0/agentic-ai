# Install FastAPI => poetry add "fastapi[standard]"
# Install Uvicorn => poetry add uvicorn

from fastapi import FastAPI   # fastapi will not give error
app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World!"}

# To run code write in terminal => poetry run uvicorn Practice:app --reload 