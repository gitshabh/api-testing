from fastapi import FastAPI
from model import User


app = FastAPI()

encoded_image:str

@app.post("/")
async def get_picture(user: User):
    encoded_image = user.base64_string
    return {"post":"successful"}

@app.get("/")
def root():
    return {"Hello": "from Rishabh"}

@app.get("/users")
def root1():
    return {"Hi": "from Rishabh"}