from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

names = ""

@app.get("/callname/{name}")
def get_name(name: str):
    global names
    names = name
    return {"hello": names}

handler = Mangum(app)

@app.post("/callname")
def post_name():
    return {"hello": names}

handler = Mangum(app)
