from ..core import settings

# GET CURRENT PROFILE WITH AUTHORIZATION
def test_profile_success(test_app):
    user_credentials={
        "grant_type": "password",
        "username": "tim@apple.com", 
        "password": "SecretPwd1."
    }

    response1 = test_app.post(
        "/users/token",
        data=user_credentials
    )

    token = response1.json().get('access_token')

    response2 = test_app.get(
        "/users/me",
        headers={'Authorization': f"Bearer {token}"}
    )

    assert response2.status_code == 200
    assert response2.json().get('message') == "Current user retrieved"
    assert response2.json().get('data') is not None

# TRY ROUTE WITHOUT AUTHENTICATION
def test_profile_success(test_app):
    response = test_app.get(
        "/users/me"
    )

    assert response.status_code == 401
    assert response.json().get('detail') == "Not authenticated"

# TRY TO AUTHENTICATE WITH WRONG TOKEN
def test_profile_success(test_app):
    token = "I am an invalid token"

    response = test_app.get(
        "/users/me",
        headers={'Authorization': f"Bearer {token}"}
    )

    assert response.status_code == 401
    assert response.json().get('detail') == "Could not validate credentials"
