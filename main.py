from fastapi import FastAPI
from enum import Enum
import pandas as pd
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Color(int, Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

df = pd.read_csv('output.csv', sep='^')

@app.get("/random/quote")
async def random_quote():
    i = random.randint(0, len(df)-1)
    out = df.iloc[i].to_dict()
    out = {key: val if not pd.isna(val) else '' for key, val in out.items()}
    return out

@app.get("/specific_quote/{i}")
async def specific_quote(i: int):
    out = df.iloc[i].to_dict()
    out = {key: val if not pd.isna(val) else '' for key, val in out.items()}
    return out