import json

# app.py
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}


handler = Mangum(app)