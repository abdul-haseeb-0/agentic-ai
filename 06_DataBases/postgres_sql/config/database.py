from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("neon_db_uri")) # create engine
sessions = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create session

def get_db(): # create function to get database connection
    db = sessions()
    try:
        yield db
    finally:
        db.close()