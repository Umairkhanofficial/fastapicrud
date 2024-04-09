from fastapi.testclient import TestClient
from studentcrud.query import app
def test_regex():
    Client = TestClient(app=app)
    Response = Client.get("/regex?q=fixed")
    assert Response.status_code == 200
    assert Response.json() == "fixed"