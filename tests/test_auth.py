import pytest
from django.contrib.auth.models import User
from django.test import Client


def test_signup_page_loads():
    client = Client()
    response = client.get("/signup/")
    assert response.status_code == 200
    assert "Crear cuenta" in response.content.decode()


@pytest.mark.django_db
def test_signup_creates_user_and_redirects():
    client = Client()
    response = client.post(
        "/signup/",
        {
            "username": "alice",
            "display_name": "Alice Smith",
            "password1": "Str0ngP@ss!",
            "password2": "Str0ngP@ss!",
        },
    )
    assert response.status_code == 302
    assert response.url == "/"
    user = User.objects.get(username="alice")
    assert user.first_name == "Alice Smith"
    assert user.is_authenticated


@pytest.mark.django_db
def test_signup_duplicate_username_shows_error():
    User.objects.create_user("alice", password="Str0ngP@ss!")
    client = Client()
    response = client.post(
        "/signup/",
        {
            "username": "alice",
            "display_name": "Another Alice",
            "password1": "Str0ngP@ss!",
            "password2": "Str0ngP@ss!",
        },
    )
    assert response.status_code == 200
    assert User.objects.filter(username="alice").count() == 1


def test_login_page_loads():
    client = Client()
    response = client.get("/login/")
    assert response.status_code == 200
    assert "Iniciar sesión" in response.content.decode()


@pytest.mark.django_db
def test_successful_login_redirects():
    User.objects.create_user("bob", password="Str0ngP@ss!")
    client = Client()
    response = client.post(
        "/login/",
        {"username": "bob", "password": "Str0ngP@ss!"},
    )
    assert response.status_code == 302
    assert response.url == "/"


@pytest.mark.django_db
def test_wrong_credentials_shows_generic_error():
    User.objects.create_user("bob", password="Str0ngP@ss!")
    client = Client()
    response = client.post(
        "/login/",
        {"username": "bob", "password": "wrong"},
    )
    assert response.status_code == 200
    content = response.content.decode()
    assert "Please enter a correct username and password" in content


@pytest.mark.django_db
def test_logout_works():
    User.objects.create_user("bob", password="Str0ngP@ss!")
    client = Client()
    client.login(username="bob", password="Str0ngP@ss!")
    response = client.post("/logout/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_authenticated_user_sees_display_name_in_nav():
    User.objects.create_user("carol", first_name="Carol", password="Str0ngP@ss!")
    client = Client()
    client.login(username="carol", password="Str0ngP@ss!")
    response = client.get("/")
    content = response.content.decode()
    assert "carol" in content
    assert "Cerrar sesión" in content
