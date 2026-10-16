from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_high_priority_lead():
    response = client.post("/leads/process", json={"name":"Jane Doe","email":"jane@example.com","company":"Example Co","phone":"+15550102030","employees":35,"interested_in":"ai-agent"})
    assert response.status_code == 200
    result = response.json()
    assert result["score"] == 100
    assert result["priority"] == "high"
    assert "priority:high" in result["crm_payload"]["tags"]


def test_invalid_email():
    response = client.post("/leads/process", json={"name":"Jane Doe","email":"not-an-email","company":"Example Co","employees":3,"interested_in":"crm"})
    assert response.status_code == 422


def test_low_priority_lead():
    response = client.post("/leads/process", json={"name":"Jane Doe","email":"jane@example.com","company":"Example Co","employees":1,"interested_in":"other"})
    assert response.status_code == 200
    assert response.json()["priority"] == "low"
