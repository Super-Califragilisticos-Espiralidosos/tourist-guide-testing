from ..core import settings

# TEST SUCCESSFUL SIGN UP PROCESS
def test_signup_success(test_app):
    test_user = {
        "username": "Test User",
        "email": "test@email.com",
        "password": "TestPassword."
    }

    response = test_app.post("/users/signup", json=test_user)
    assert response.status_code == 201
    assert response.json().get('message') == "User added successfully"
    assert test_app.mongodb[settings.MONGODB_COLLECTION_USERS].find_one_and_delete({"email": test_user['email']}) is not None

# TEST MODEL VALIDATOR FOR WEAK PASSWORD
def test_signup_weak_password(test_app):
    test_user = {
        "username": "Test User",
        "email": "test@email.com",
        "password": "weak"
    }

    response = test_app.post("/users/signup", json=test_user)
    assert response.status_code == 422
    assert response.json().get('detail')[0].get('msg') == "Password must be 8 characters or longer"
    assert test_app.mongodb[settings.MONGODB_COLLECTION_USERS].find_one_and_delete({"email": test_user['email']}) is not None

# TEST MODEL VALIDATOR FOR EMPTY FIELD
def test_signup_empty_username(test_app):
    test_user = {
        "username": "",
        "email": "test@email.com",
        "password": "weak"
    }

    response = test_app.post("/users/signup", json=test_user)
    assert response.status_code == 422
    assert response.json().get('detail')[0].get('msg') == "Empty strings are not allowed"
    assert test_app.mongodb[settings.MONGODB_COLLECTION_USERS].find_one_and_delete({"email": test_user['email']}) is not None
