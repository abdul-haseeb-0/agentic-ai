from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
import datetime 

Base = declarative_base() # create base class

# create model of users
class Users(Base):
    __tablename__ = 'users' # table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, CheckConstraint('email ~* "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"'), nullable=False, unique=True)
    password = Column(String, nullable=False)

# create model of todos
class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))