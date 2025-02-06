import pytest
from app import app, db, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_task(client):
    response = client.post('/add', data=dict(
        task_name="Test Task",
        reminder_time="2025-12-12T10:30"
    ), follow_redirects=True)
    assert b"Test Task" in response.data

def test_delete_task(client):
    new_task = Task(task_name="Delete Me", reminder_time="2025-12-12T10:30")
    db.session.add(new_task)
    db.session.commit()
    task_id = new_task.id
    response = client.get(f'/delete/{task_id}', follow_redirects=True)
    assert b"Delete Me" not in response.data
