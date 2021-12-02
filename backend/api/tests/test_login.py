from ..core import settings

# SUCCESFUL TOKEN GENERATION, WITH NO ERRORS
def test_token(test_app):
    user_credentials={
        "grant_type": "password",
        "username": "tim@apple.com", 
        "password": "SecretPwd1."
    }

    response = test_app.post(
        "/users/token",
        data=user_credentials
    )
    assert response.status_code == 200
    assert response.json().get('token_type') == "bearer"
    assert response.json().get('access_token') is not None

# UNAUTHORIZED REQUEST DUE TO INVALID CREDENTIALS
def test_token_invalid_credentials(test_app):
    user_credentials={
        "grant_type": "password",
        "username": "tim@apple.com", 
        "password": "WRONG"
    }

    response = test_app.post(
        "/users/token",
        data=user_credentials
    )
    assert response.status_code == 401
    assert response.json().get('detail') == "Incorrect username or password"

# BAD REQUEST DUE TO UNPROCESSABLE ENTITY
def test_token_invalid_body(test_app):
    user_credentials={
        "grant_type": "password",
        "username": "tim@apple.com"
    }

    response = test_app.post(
        "/users/token",
        data=user_credentials
    )
    assert response.status_code == 422
    assert response.json().get('detail')[0].get('msg') == "field required"
