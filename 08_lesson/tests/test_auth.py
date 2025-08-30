import requests
import pytest
from config import Config

def test_auth_check():
    """Тест для проверки авторизации"""
    headers = {
        "Authorization": f"Bearer {Config.API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        f"{Config.BASE_URL}/projects",
        headers=headers,
        timeout=30
    )
    
    print(f"Auth check - Status: {response.status_code}")
    
    assert response.status_code == 200