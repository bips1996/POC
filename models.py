from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "Employee"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index = True)
    email = Column(String, unique=True, index=True)
    position = Column(String,index=True)

class BUnits(Base):
    __tablename__ = "BUnits"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    director = Column(Integer, ForeignKey("Employee.id")) 


# {   
#    "id" :  1,
#     "title" :"IA",
#     "description" :"Deals with development" ,
#     "Director" : 1
# }

# {
#     "id" :1,
#     "name" : "Biplaba",
#     "email" : "a@b.in",
#     "position" : "intern"
# }