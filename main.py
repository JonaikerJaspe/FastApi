#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body



app = FastAPI()

# Models

class Person (BaseModel):
    firstName: str
    lastName:str
    age:int
    hairColor:Optional[str] = None
    isMarried: Optional[bool] = None


@app.get("/")
def home():
    return {"Hello":"world"}



@app.post("/person/new")
def createPerson( person:Person = Body(...)):
    return person
