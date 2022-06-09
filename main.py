from fastapi import FastAPI
from model import User
import os

app = FastAPI()

encoded_image:str

@app.post("/")
async def get_picture(user: User):
    encoded_image = user.base64_string
    return {"post":"successful"}

@app.get("/")
def foo():
    return {"Rishabh":"hi"}

@app.get("/{name}")
def root(name:str):
    directory = 'images/'
    for filename in os.listdir(directory):
        f = os.path.join(directory,filename)
        if os.path.isfile(f):
            basename = os.path.basename(f)
            (filename,ext) = os.path.splitext(basename)
            if filename == name:
                return {name:'Present'}
    return {name:'Absent'}

@app.get("/users")
def root1():
    return {"Hi": "Rishabh here"}

