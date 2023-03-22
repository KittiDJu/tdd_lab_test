from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_name():
    global responseget = client.get("/callname/{name}")
    assert responseget.status_code == 200
    assert responseget.json() == {"hello": "{name}"}
