import requests
from requests import Response
import uuid
from .base_client import BaseClient


class TaskClient(BaseClient):
    def __init__(self, api_token: str) -> None:
        super().__init__(api_token)

    def get_active_tasks(self) -> Response:
        response: Response = requests.get(
            f"{self.base_url}/rest/v2/tasks", headers=self.headers
        )
        response.raise_for_status()
        return response

    def create_task(
        self, content: str, due_string: str, priority: str, due_lang: str = "en"
    ) -> Response:
        headers = {**self.headers, "X-Request-Id": str(uuid.uuid4())}
        data = {
            "content": content,
            "due_string": due_string,
            "due_lang": due_lang,
            "priority": priority,
        }
        response: Response = requests.post(
            f"{self.base_url}/rest/v2/tasks", data=data, headers=headers
        )
        # response.raise_for_status()
        return response

    def get_active_task(self, task_id: str) -> Response:
        response: Response = requests.get(
            f"{self.base_url}/rest/v2/tasks/{task_id}", headers=self.headers
        )
        # response.raise_for_status()
        return response

    def update_a_task(self, task_id: str, content: str) -> Response:
        headers = {**self.headers, "X-Request-Id": str(uuid.uuid4())}
        data = {"content": content}
        response: Response = requests.post(
            f"{self.base_url}/rest/v2/tasks/{task_id}", data=data, headers=headers
        )
        # response.raise_for_status()
        return response

    def close_a_task(self, task_id: str) -> Response:
        response: Response = requests.post(
            f"{self.base_url}/rest/v2/tasks/{task_id}/close", headers=self.headers
        )
        # response.raise_for_status()
        return response

    def reopen_a_task(self, task_id: str) -> Response:
        response: Response = requests.post(
            f"{self.base_url}/rest/v2/tasks/{task_id}/reopen", headers=self.headers
        )
        # response.raise_for_status()
        return response

    def delete_a_task(self, task_id: str) -> Response:
        response: Response = requests.delete(
            f"{self.base_url}/rest/v2/tasks/{task_id}", headers=self.headers
        )
        # response.raise_for_status()
        return response
