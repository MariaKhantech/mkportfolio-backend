import json

# app.py
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/chat")
def read_root():
    return {"Hello": "World"}

@app.get("/chat/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/chat/id/{item_id}")
def read_item(item_id: int):
    return {"chat ID": item_id}

handler = Mangum(app)

