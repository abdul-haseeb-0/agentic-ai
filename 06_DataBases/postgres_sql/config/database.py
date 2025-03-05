from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker # import sessionmaker function
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("neon_db")) # create engine
sessions = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create session