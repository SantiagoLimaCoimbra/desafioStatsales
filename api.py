#Código simples que fiz apenas para aprender a usar o FastAPI

import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Inputs(BaseModel):
    inp1: int
    inp2: str

@app.get("/exget")
def exampleget() -> str:
    return "operação get"


@app.post("/expost")
def examplepost(inputs: Inputs) -> str:
    return inputs.inp2


if _name_ == "_main_":
    uvicorn.run(app, port=8000)