from django.test import Client


def test_homepage_returns_200():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200
