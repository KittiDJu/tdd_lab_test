from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/callname/{name}")
def get_name(name: str):
    global names = name
    return {"hello": names}
handler = Mangum(app)
