import os
from typing import Any

from todoist_client.task_client import TaskClient
from todoist_client.projects_client import ProjectClient


def before_all(context: Any) -> None:
    context.api_token = os.getenv("TODOIST_API_TOKEN")
    context.task_client = TaskClient(api_token=context.api_token)
    context.project_client = ProjectClient(api_token=context.api_token)
