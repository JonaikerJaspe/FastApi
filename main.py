#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query


app = FastAPI()

# Models

class Person (BaseModel):
    firstName: str
    lastName:str
    age:int
    hairColor:Optional[str] = None
    isMarried: Optional[bool] = None


# Request and Response

@app.get("/")
def home():
    return {"Hello":"world"}

# Validaciones : Query Parameters

@app.post("/person/new")
def createPerson( person:Person = Body(...)):
    return person


@app.get("/person/datail")
def show_person(
    name: Optional[str] = Query(None, min_length=1 , max_length=30),
    age: str = Query(...)
):
    return{name: age}