from fastapi import FastAPI,Query
import uvicorn
from typing import Annotated

app = FastAPI()

@app.get("/querytest")
def query(q:Annotated[str,Query(min_length=3,max_length=10,)]):
    return q

@app.get("/regex")
def query(q:str|None = Query(None,min_length=3,max_length=10,regex="^fixed$")):
    return q

def start():
    uvicorn.run("studentcrud.query:app",host="127.0.0.1",port=8080, reload=True)