import pytest, ssl
from ..main import app
from ..core import settings
from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient

@pytest.fixture(scope="module")
def test_app():
    app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URL, ssl_cert_reqs=ssl.CERT_NONE)
    app.mongodb = app.mongodb_client[settings.MONGODB_NAME]
    client = TestClient(app)
    client.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URL, ssl_cert_reqs=ssl.CERT_NONE)
    client.mongodb = app.mongodb_client[settings.MONGODB_NAME]
    yield client
