import pytest
import requests
from pages.projects_page import ProjectsPage

class TestProjects:
    """Тесты для методов работы с проектами"""
    
    def test_create_project_positive(self, auth_headers, test_project_data):
        """Позитивный тест создания проекта"""
        projects_page = ProjectsPage()
        
        response = projects_page.create_project(test_project_data, auth_headers)
        
        assert response.status_code == 201
        assert "id" in response.json()
        
        # Дополнительная проверка: можем ли получить проект
        project_id = response.json()["id"]
        get_response = projects_page.get_project(project_id, auth_headers)
        assert get_response.status_code == 200
    
    def test_create_project_negative_missing_title(self, auth_headers):
        """Негативный тест создания проекта без title"""
        projects_page = ProjectsPage()
        
        invalid_data = {}  # Пустые данные
        response = projects_page.create_project(invalid_data, auth_headers)
        
        assert response.status_code == 400
    
    def test_get_project_positive(self, auth_headers, created_project):
        """Позитивный тест получения проекта"""
        projects_page = ProjectsPage()
        
        response = projects_page.get_project(created_project, auth_headers)
        
        assert response.status_code == 200
        assert response.json()["id"] == created_project
    
    def test_get_project_negative_not_found(self, auth_headers):
        """Негативный тест получения несуществующего проекта"""
        projects_page = ProjectsPage()
        
        response = projects_page.get_project("non_existent_id_123", auth_headers)
        
        assert response.status_code == 404
    
    def test_update_project_positive(self, auth_headers, created_project):
        """Позитивный тест обновления проекта"""
        projects_page = ProjectsPage()
        
        update_data = {"title": "Updated Test Project"}
        
        response = projects_page.update_project(created_project, update_data, auth_headers)
        
        assert response.status_code == 200
        
        # Проверяем что изменения применились
        get_response = projects_page.get_project(created_project, auth_headers)
        assert get_response.json()["title"] == "Updated Test Project"
    
    def test_update_project_negative_invalid_data(self, auth_headers, created_project):
        """Негативный тест обновления с невалидными данными"""
        projects_page = ProjectsPage()
        
        invalid_data = {"title": ""}  # Пустой title
        
        response = projects_page.update_project(created_project, invalid_data, auth_headers)
        
        assert response.status_code == 400