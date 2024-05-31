from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Travel Recommendations API"}

def test_get_recommendations():
    response = client.get("/recommendations/?country=Canada&season=winter")
    assert response.status_code == 200
    data = response.json()
    assert data["country"] == "Canada"
    assert data["season"] == "winter"
    assert len(data["recommendations"]) == 3
