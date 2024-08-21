import pytest
from fastapi.testclient import TestClient
from main import app  # Ensure 'main' is the name of your Python file

client = TestClient(app)

def test_process_case():
    response = client.post("/process_case/", json={"details": "Sample case details"})
    assert response.status_code == 200
    assert "output" in response.json()