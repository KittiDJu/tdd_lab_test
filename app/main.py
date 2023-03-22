from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/callname/{name}")
def get_name(name: str):
    return {"hello": name}
handler = Mangum(app)

@app.post("/callname")
def post_name(name: str):
    return {"hello": name}
handler = Mangum(app)
