import pytest
from app import app
from datetime import datetime

@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if homepage loads successfully."""
    response = client.get("/")
    assert response.status_code == 200

def test_add_task(client):
    """Test adding a new reminder task."""
    response = client.post("/add", data={
        "task_name": "Test Task",
        "reminder_time": datetime.now().strftime("%Y-%m-%dT%H:%M")
    })
    assert response.status_code == 302  # Redirects after adding task

def test_get_reminders(client):
    """Test fetching reminders API."""
    response = client.get("/get_reminders")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_delete_task(client):
    """Test deleting a task (ID needs to exist in DB)."""
    fake_id = "650c6781f2d3e63b841d7a92"  # Change this to a real one from your DB
    response = client.post(f"/delete/{fake_id}")
    assert response.status_code == 200
