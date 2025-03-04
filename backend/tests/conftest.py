import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from app.main import app
from dotenv import load_dotenv

load_dotenv()

client = TestClient(app)

@pytest.fixture
def client_instance():
    return client

@pytest.fixture
def mock_openai():
    with patch("app.services.openai.ChatCompletion.acreate", new_callable=AsyncMock) as mock_api:
        dummy_response = {
            "choices": [
                {"message": {"content": '{"pizzas": [{"quantity": 2, "size": "medium", "crust": "hand tossed"}], "additional_info": "Extra info processed."}' }}
            ]
        }
        mock_api.return_value = dummy_response
        yield mock_api