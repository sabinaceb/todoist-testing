import requests
import uuid
from requests import Response

from .base_client import BaseClient


class ProjectClient(BaseClient):
    def __init__(self, api_token: str) -> None:
        super().__init__(api_token)

    def get_all_projects(self) -> Response:
        response: Response = requests.get(
            f"{self.base_url}/rest/v2/projects", headers=self.headers
        )
        response.raise_for_status()
        return response

    def create_new_project(self, name: str) -> Response:
        headers = {**self.headers, "X-Request-Id": str(uuid.uuid4())}
        data = {"name": name}
        response: Response = requests.post(
            f"{self.base_url}/rest/v2/projects", data=data, headers=headers
        )
        # response.raise_for_status()
        return response

    def create_new_project_invalid_data(self, name: str, color: str) -> Response:
        headers = {**self.headers, "X-Request-Id": str(uuid.uuid4())}
        data = {"name": name, "color": color}
        response: Response = requests.post(
            f"{self.base_url}/rest/v2/projects", data=data, headers=headers
        )
        # response.raise_for_status()
        return response

    def get_a_project(self, project_id: str) -> Response:
        response: Response = requests.get(
            f"{self.base_url}/rest/v2/projects/{project_id}", headers=self.headers
        )
        # response.raise_for_status()
        return response

    def update_a_project(self, project_id: str, name: str) -> Response:
        headers = {**self.headers, "X-Request-Id": str(uuid.uuid4())}
        data = {"name": name}
        response: Response = requests.post(
            f"{self.base_url}/rest/v2/projects/{project_id}", data=data, headers=headers
        )
        # response.raise_for_status()
        return response

    def delete_a_project(self, project_id: str) -> Response:
        response: Response = requests.delete(
            f"{self.base_url}/rest/v2/projects/{project_id}", headers=self.headers
        )
        # response.raise_for_status()
        return response

    def get_all_collaborators(self, project_id: str) -> Response:
        response: Response = requests.get(
            f"{self.base_url}/rest/v2/projects/{project_id}/collaborators",
            headers=self.headers,
        )
        # response.raise_for_status()
        return response
