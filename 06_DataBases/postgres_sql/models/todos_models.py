from sqlalchemy import Column, Integer, String, Boolean, DateTime  # import column types
from sqlalchemy.ext.declarative import declarative_base # import base class for models
import datetime # import datetime module

Base = declarative_base() # create base class for models

class Todo(Base): # create model class
    __tablename__ = 'todos' # table name

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True, nullable = False)
    description = Column(String, nullable = False)
    completed = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.datetime.now())