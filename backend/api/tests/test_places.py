from ..core import settings

example_place_id = "61a6be1c9d65bdcea4a32833"

user_credentials={
        "grant_type": "password",
        "username": "tim@apple.com", 
        "password": "SecretPwd1."
    }

# TEST PLACES LIST SUCCESSFULLY
def test_places_list_success(test_app):
    response1 = test_app.post(
        "/users/token",
        data=user_credentials
    )

    token = response1.json().get('access_token')

    response2 = test_app.get(
        "/places/list",
        headers={'Authorization': f"Bearer {token}"}
    )

    assert response2.status_code == 200
    assert response2.json().get('message') == "List retrieved successfully"
    assert response2.json().get('data') is not None

# TRY ROUTE WITHOUT AUTHENTICATION
def test_places_list_no_auth(test_app):
    response = test_app.get(
        "/places/list"
    )

    assert response.status_code == 401
    assert response.json().get('detail') == "Not authenticated"

# TRY TO AUTHENTICATE WITH WRONG TOKEN
def test_places_list_failed_auth(test_app):
    token = "I am an invalid token"

    response = test_app.get(
        "/places/list",
        headers={'Authorization': f"Bearer {token}"}
    )

    assert response.status_code == 401
    assert response.json().get('detail') == "Could not validate credentials"

# GET PLACE ID AND TEST SUCCESS
def test_place_by_id_success(test_app):
    response1 = test_app.post(
        "/users/token",
        data=user_credentials
    )

    token = response1.json().get('access_token')

    response2 = test_app.get(
        f"/places/{example_place_id}",
        headers={'Authorization': f"Bearer {token}"}
    )

    assert response2.status_code == 200
    assert response2.json().get('message') == "Place retrieved successfully"
    assert response2.json().get('data') is not None

# TRY ROUTE WITHOUT AUTHENTICATION
def test_places_by_id_no_auth(test_app):
    response = test_app.get(
        f"/places/{example_place_id}"
    )

    assert response.status_code == 401
    assert response.json().get('detail') == "Not authenticated"

# TRY TO AUTHENTICATE WITH WRONG TOKEN
def test_places_by_id_failed_auth(test_app):
    token = "I am an invalid token"

    response = test_app.get(
        f"/places/{example_place_id}",
        headers={'Authorization': f"Bearer {token}"}
    )

    assert response.status_code == 401
    assert response.json().get('detail') == "Could not validate credentials"

# TRY TO GET NON EXISTENT PLACE WHILE AUTHORIZED
def test_places_by_id_not_exists(test_app):
    response1 = test_app.post(
        "/users/token",
        data=user_credentials
    )

    token = response1.json().get('access_token')
    invalid_place_id = "1234567890"

    response = test_app.get(
        f"/places/{invalid_place_id}",
        headers={'Authorization': f"Bearer {token}"}
    )

    assert response.status_code == 404
    assert response.json().get('detail') == f"Place with ID {invalid_place_id} not found"
