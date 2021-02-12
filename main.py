from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional
import models
from database import SessionLocal,engine
from sqlalchemy.orm import Session
from models import Employee , BUnits

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post("/Employee")
# def create_Employee(create_Employee : createEmployeeOne,)