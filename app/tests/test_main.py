from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

responseget = None

def test_get_name():
    global responseget
    responseget = client.get("/callname/{name}")
    assert responseget.status_code == 200
    assert responseget.json() == {"hello": "{name}"}
    
def test_post_name():
    response = client.post("/callname")
    assert response.status_code == 200
    assert response.json() == responseget.json()
