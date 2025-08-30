import requests
import json
from config import Config

class ProjectsPage:
    def __init__(self):
        self.base_url = f"{Config.BASE_URL}/projects"
    
    def create_project(self, data, headers):
        """POST /api-v2/projects - создание проекта"""
        print(f"Creating project with data: {json.dumps(data, ensure_ascii=False)}")
        
        response = requests.post(
            self.base_url,
            json=data,
            headers=headers,
            timeout=30
        )
        
        print(f"Create response: {response.status_code} - {response.text}")
        return response
    
    def get_project(self, project_id, headers):
        """GET /api-v2/projects/{id} - получение проекта"""
        response = requests.get(
            f"{self.base_url}/{project_id}",
            headers=headers,
            timeout=30
        )
        print(f"Get response: {response.status_code} - {response.text}")
        return response
    
    def update_project(self, project_id, data, headers):
        """PUT /api-v2/projects/{id} - обновление проекта"""
        print(f"Updating project {project_id} with data: {json.dumps(data, ensure_ascii=False)}")
        
        response = requests.put(
            f"{self.base_url}/{project_id}",
            json=data,
            headers=headers,
            timeout=30
        )
        
        print(f"Update response: {response.status_code} - {response.text}")
        return response
    
    def delete_project(self, project_id, headers):
        """DELETE проекта (для cleanup)"""
        response = requests.delete(
            f"{self.base_url}/{project_id}",
            headers=headers,
            timeout=30
        )
        print(f"Delete response: {response.status_code} - {response.text}")
        return response