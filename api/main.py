from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_response


class data(BaseModel):
    lyric: str

app = FastAPI()
app.previous = ""
def generate(input):
    app.previous = generate_response(input)
    return app.previous

@app.post("/predict", response_model=data)
def predict(input: data):
    resp = generate(input.lyric)
    return data(lyric=resp)

@app.get("/predict", response_model=data)
def predict():
    return data(lyric=generate(''))

@app.get("/", response_model=str)
def predict():
    return generate('')

@app.get('/continue', response_model=data)
def predict():
    rem = len(app.previous)
    return data(lyric=generate(app.previous)[rem:])
