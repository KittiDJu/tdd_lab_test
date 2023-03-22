from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/{name}")
def read_root(name: str):
    return {"hello": name}
handler = Mangum(app)
