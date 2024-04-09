from fastapi import FastAPI,Path,Query,Body
import uvicorn 
from pydantic import BaseModel ,Field
from typing import Annotated ,Optional


app = FastAPI()
student_List = [
    {"studentID":4,
     "Name":"Umair",
     "Age":26,
     "Class": "Api"
     }
]

@app.get("/person")
def perso(person):
    return person
@app.get("/testing")
def test(q: Annotated[int,Query(ge=2)]):
    return q

#all students in list
@app.get("/students")
def students():
    print("students details")
    return student_List
#get single student
@app.get("/singlestudent/{studentid}")
def singleStudent(studentid:Annotated[int,Path(ge=2)]):
    for student in student_List:
        if student["studentID"] == studentid:
            return student
    return {"message": "Student not found"}

@app.post("/addstudent")
def addStudent(studentid:Annotated[int,Query(ge=2)],Name,Age,Class):
 
    global student_List
    student_List.append({"studentID":studentid,"Name":Name,"Age":Age,"Class":Class})
    return student_List
#update student
@app.put("/updatestudent")
def updateStudent(studentid:int,Name,Age,Class):
    studentIndex=None
    for i,student in list(enumerate(student_List)):
        if student["studentID"] == studentid:
            studentIndex=i
        
    if studentIndex is None:
        return "Not found"
        # del student_List[studentIndex]
    student_List[studentIndex]["Name"]=Name
    student_List[studentIndex]["Age"]=Age
    student_List[studentIndex]["Class"]=Class
    #return f"updated {student_List[studentIndex]["Name"]}"
        
    return f"Updated {student_List[studentIndex]['Name']}"

#delete student
@app.delete("/deletestudent/{studentid}")

def deleteStudent(studentid:int):
    delindex=None
    for index,student in enumerate(student_List):
        if student["studentID"] == studentid:
            delindex = index
            del student_List[delindex]
            return student_List
        else: return "No Record found"

@app.get("/temp")
def temp():
    print("hello")
    return "temp"
#pydantic body prams
class Item(BaseModel):
    id:int = Field(ge=2)
    title:str
    disc:str
class NewItem(BaseModel):
    date:str
    func:str
    
@app.get("/body/{name}")
def bodypram(id:int, item:Item,item2:NewItem,count:Annotated[int,Body()]):
    print(item.title)
    print(item2.func)
    return (item,item2)
#Query param validation
@app.get("/queryval")
def queryValidation(name:Annotated[str,Query(min_length=3,max_length=5,pattern="^[a-zA-Z]")]):
    
    return name,
 
def start():
    uvicorn.run("studentcrud.main:app",host="127.0.0.1",port=8080,reload=True),
