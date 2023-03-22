from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_name():
    response = client.get("/callname/{name}")
    assert response.status_code == 200
    assert response.json() == {"hello": "{name}"}
    
def test_post_name():
    response = client.post("/callname")
    assert response.status_code == 200
    assert response.json() == {"hello": "{name}"}
