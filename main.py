from fastapi import FastAPI
from model import User
import os
import face_recog

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
    flag = face_recog.face_rec(name)
    return {name: flag}

@app.get("/api/cmp")
def comp():
    if face_recog.compare_faces():
        return {"Faces":"Same"}
    return {"Faces": "Different"}

@app.get("/api/users")
def root1():
    return {"Hi": "Rishabh"}

