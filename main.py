from fastapi import FastAPI ,Depends,BackgroundTasks,Request
from pydantic import BaseModel 
from typing import Optional,List
import models
from database import SessionLocal,engine
from sqlalchemy.orm import Session
from models import Employee , BUnits ,Complains

class createEmployee(BaseModel) :
    id : int
    name : str
    email : str
    position : str
    reporting_manager : Optional[int]
    works_on: Optional[int]
    class Config:
        orm_mode = True
    

# id = Column(Integer, primary_key=True, index=True)
#     name = Column(String,index = True)
#     email = Column(String, unique=True, index=True)
#     position = Column(String,index=True)
#     reporting_manager = Column(Integer ,ForeignKey("Employee.id"))
#     works_on = Column(Integer,ForeignKey("BUnits.id"))

class bUnit(BaseModel) :
    id = 0
    title = ""
    description =""

class complains(BaseModel):
    e_id = 0
    comp_messege = ""


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

# #APIS Employee
# 1. Create_Employees
# 2. Employee_by_id
# 3. Employee_by_name
# 4. All_employee

@app.post("/Create_Employees")
def create_Employee(emp : createEmployee, db : Session = Depends(get_db)): 
    _employee = Employee()
    _employee.id = emp.id
    _employee.name = emp.name
    _employee.email = emp.email
    _employee.position = emp.position
    _employee.works_on: emp.works_on
    _employee.reporting_manager : emp.reporting_manager
    db.add(_employee)
    db.commit()
    # Background_tasks.add_task(fetch_emp_data,employee.id)
    
    return{
        "code":"Success",
        "messege": "Employee created the name"+emp.name
    }
@app.get("/Employees_by_id" ) 
def employee_by_id(id : int) :
    db = SessionLocal()
    emp = db.query(Employee).filter(Employee.id == id).first()
    return emp

@app.get("/Employees_by_name")
def employees_by_name(name : str) :
    db = SessionLocal()
    return db.query(Employee).filter(Employee.name == name).first()

@app.get("/All_Employees", response_model = List[ createEmployee ])
def all_employee(skip: int = 0, limit: int = 100,db : Session =  Depends(get_db)):
    return db.query(Employee).offset(skip).limit(limit).all()

# #APIS BUnits
# 1. Create_BUnit
# 2. BUnit_by_id

@app.post("/Create_BUnits")
def create_BUnits(create_bunit: bUnit, db:Session = Depends(get_db)) :
    bunit = BUnits()
    bunit.id = create_bunit.id 
    bunit.title = create_bunit.title
    bunit.description = create_bunit.description
    db.add(bunit)
    db.commit()
    return{
        "code":"Success",
        "messege": "New Bunit added"
    }
@app.get("Buisness_units_by_id")
def bunits_by_id(id : int) :
    db = SessionLocal()
    emp = db.query(BUnits).filter(BUnits.id == id).first()
    return emp



# #APis Goals
# 1.Goals_by_id
# 2.Goals_by_eid

# #Apis Complains
# 1.Complains_by_id
# 2.Complains_by_eid
@app.post("/complains")
def create_complain(comp : complains, db:Session = Depends(get_db)) :
    _comp = Complains()
    _comp.e_id = comp.e_id
    _comp.comp_messege = comp.comp_messege
    db.add(_comp)
    db.commit()
    return{
        "code":"Success",
        "messege": "Complain created"
    }














