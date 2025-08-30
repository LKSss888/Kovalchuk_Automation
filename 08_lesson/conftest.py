import pytest
from config import Config

@pytest.fixture
def auth_headers():
    """Фикстура для авторизационных заголовков"""
    return {
        "Authorization": f"Bearer {Config.API_TOKEN}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def test_project_data():
    """Фикстура с тестовыми данными проекта"""
    return {
        "title": "Test Project"  # Только title!
    }

@pytest.fixture
def created_project(auth_headers, test_project_data):
    """Фикстура создает проект и возвращает его ID, удаляет после теста"""
    from pages.projects_page import ProjectsPage
    
    projects_page = ProjectsPage()
    response = projects_page.create_project(test_project_data, auth_headers)
    
    print(f"Create status: {response.status_code}")
    print(f"Create response: {response.text}")
    
    if response.status_code not in [200, 201]:
        pytest.fail(f"Failed to create project: {response.status_code} {response.text}")
    
    project_id = response.json()["id"]
    
    yield project_id
    
    # Cleanup - удаление проекта после теста
    projects_page.delete_project(project_id, auth_headers)