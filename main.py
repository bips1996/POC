from fastapi import FastAPI ,Depends,BackgroundTasks,Request
from pydantic import BaseModel 
from typing import Optional
import models
from database import SessionLocal,engine
from sqlalchemy.orm import Session
from models import Employee , BUnits 

class createEmployee(BaseModel) :
    id : int
    name : str
    email : str
    position : str

class bUnit(BaseModel) :
    id = 0
    title = ""
    description =""
    director = 0

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# def fetch_emp_data(id:int):

@app.post("/Employees")
def create_Employee(emp : createEmployee, db : Session = Depends(get_db)): 
    employee = Employee()
    employee.id = emp.id
    employee.name = emp.name
    employee.email = emp.email
    employee.position = emp.position
    db.add(employee)
    db.commit()
    # Background_tasks.add_task(fetch_emp_data,employee.id)
    return{
        "code":"Success",
        "messege": "Created"
    }

@app.post("/BUnits")
def create_BUnits(create_bunit: bUnit, db:Session = Depends(get_db)) :
    bunit = BUnits()
    bunit.id = create_bunit.id 
    bunit.title = create_bunit.title
    bunit.description = create_bunit.description
    bunit.director = create_bunit.director
    db.add(bunit)
    db.commit()
    return{
        "code":"Success",
        "messege": "New Bunit added"
    }
    