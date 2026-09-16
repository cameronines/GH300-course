from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.delete("/activities/Chess Club/unregister?email=michael@mergington.edu")

    assert response.status_code == 200
    assert response.json() == {"message": "Unregistered michael@mergington.edu from Chess Club"}
    assert "michael@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]

    client.post("/activities/Chess Club/signup?email=michael@mergington.edu")
