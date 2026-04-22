from app import app

def test_health():
    response = app.test_client().get('/health')
    assert response.json["status"] == "ok"

def test_homes():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Jenkins" in response.data