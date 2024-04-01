from fastapi.testclient import TestClient
from studentcrud.main import app

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == [{"studentID":1,
     "Name":"Umair",
     "Age":26,
     "Class": "Api"}]
    
def test_single_student():
    client = TestClient(app=app)
    response = client.get("/singlestudent/1")
    assert response.status_code == 200
    assert response.json() == {"studentID":1,
     "Name":"Umair",
     "Age":26,
     "Class": "Api"}
    
def test_temp():
    client = TestClient(app=app)
    response = client.get("/temp")
    assert response.status_code ==200
    assert response.json() == "temp"