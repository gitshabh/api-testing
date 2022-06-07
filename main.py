from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "from Rishabh"}

@app.get("/users")
def root1():
    return {"Hi": "from Rishabh"}