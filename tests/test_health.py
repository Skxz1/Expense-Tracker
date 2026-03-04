# Import a testing client for FastAPI
# This lets us simulate HTTP requests without starting a real server
from fastapi.testclient import TestClient

# Import the FastAPI app we created
from expense_tracker.web.app import app


def test_health() -> None:

    # Create a test client that can call our API
    client = TestClient(app)

    # Simulate visiting /health
    response = client.get("/health")

    # Check that the response status code is 200 (success)
    assert response.status_code == 200

    # Check that the JSON response is correct
    assert response.json() == {"status": "ok"}
