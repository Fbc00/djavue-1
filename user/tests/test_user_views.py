import json
from unittest.mock import ANY

from django.contrib.sessions.middleware import SessionMiddleware

from user.views import user_login, user_logout, user_whoami


def test_user_login_with_valid_user(rf, user):
    request = rf.post(
        "/api/user/login/",
        data={
            "id": user.id,
            "username": user.username,
            "password": "password",
        },
    )

    middleware = SessionMiddleware(get_response=ANY)
    middleware.process_request(request)

    response = user_login(request)
    response_content = json.loads(response.content)

    assert response.status_code == 200
    assert user.id == response_content["id"]
    assert user.first_name == response_content["first_name"]
    assert user.last_name == response_content["last_name"]
    assert user.email == response_content["email"]


def test_user_login_with_invalid_user(rf, user):
    request = rf.post(
        "/api/user/login/",
        data={
            "id": ANY,
            "username": ANY,
            "password": ANY,
        },
    )

    middleware = SessionMiddleware(get_response=ANY)
    middleware.process_request(request)

    response = user_login(request)
    response_content = json.loads(response.content)

    assert response.status_code == 404
    assert response_content == {}


def test_user_logout_with_logged_user(rf, user):
    request = rf.get("/api/user/logout/")
    request.user = user

    middleware = SessionMiddleware(get_response=ANY)
    middleware.process_request(request)

    response = user_logout(request)
    response_content = json.loads(response.content)

    assert response.status_code == 200
    assert response_content == {}


def test_user_logout_with_anonymous_user(rf, anonymous_user):
    request = rf.get("/api/user/logout")
    request.user = anonymous_user

    middleware = SessionMiddleware(get_response=ANY)
    middleware.process_request(request)

    response = user_logout(request)
    response_content = json.loads(response.content)

    assert response.status_code == 404
    assert response_content == {}


def test_user_whoami_with_logged_user(rf, user):
    request = rf.get("/api/user/whoami/")
    request.user = user

    response = user_whoami(request)
    response_content = json.loads(response.content)

    assert response.status_code == 200
    assert response_content["authenticated"] is True
    assert user.id == response_content["user"]["id"]
    assert user.first_name == response_content["user"]["first_name"]
    assert user.last_name == response_content["user"]["last_name"]
    assert user.email == response_content["user"]["email"]


def test_user_whoami_with_anonymous_user(rf, anonymous_user):
    request = rf.get("/api/user/whoami/")
    request.user = anonymous_user

    response = user_whoami(request)
    response_content = json.loads(response.content)

    assert response.status_code == 404
    assert response_content["authenticated"] is False
