import os
import requests
import uuid

BASE_URL = "https://api.todoist.com"
API_TOKEN = os.getenv("TODOIST_API_TOKEN")


# TASKS
def get_active_tasks():
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f"{BASE_URL}/rest/v2/tasks", headers=header)
    response.raise_for_status()
    return response


def create_new_task(content, due_string, priority, due_lang="en"):
    headers = {
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {API_TOKEN}",
    }
    data = {
        "content": content,
        "due_string": due_string,
        "due_lang": due_lang,
        "priority": priority,
    }
    response = requests.post(f"{BASE_URL}/rest/v2/tasks", data=data, headers=headers)
    # response.raise_for_status()
    return response


def get_active_task(task_id):
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f"{BASE_URL}/rest/v2/tasks/{task_id}", headers=header)
    # response.raise_for_status()
    return response


def update_a_task(task_id, content):
    headers = {
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {API_TOKEN}",
    }
    data = {"content": content}
    response = requests.post(
        f"{BASE_URL}/rest/v2/tasks/{task_id}", data=data, headers=headers
    )
    # response.raise_for_status()
    return response


def close_a_task(task_id):
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(
        f"{BASE_URL}/rest/v2/tasks/{task_id}/close", headers=header
    )
    # response.raise_for_status()
    return response


def reopen_a_task(task_id):
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(
        f"{BASE_URL}/rest/v2/tasks/{task_id}/reopen", headers=header
    )
    # response.raise_for_status()
    return response


def delete_a_task(task_id):
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.delete(f"{BASE_URL}/rest/v2/tasks/{task_id}", headers=header)
    # response.raise_for_status()
    return response


# PROJECTS
def get_all_projects():
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f"{BASE_URL}/rest/v2/projects", headers=header)
    response.raise_for_status()
    return response


def create_new_project(name):
    headers = {
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {API_TOKEN}",
    }
    data = {"name": name}
    response = requests.post(f"{BASE_URL}/rest/v2/projects", data=data, headers=headers)
    # response.raise_for_status()
    return response


def create_new_project_invalid_data(name, color):
    headers = {
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {API_TOKEN}",
    }
    data = {"name": name, "color": color}
    response = requests.post(f"{BASE_URL}/rest/v2/projects", data=data, headers=headers)
    # response.raise_for_status()
    return response


def get_a_project(project_id):
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f"{BASE_URL}/rest/v2/projects/{project_id}", headers=header)
    # response.raise_for_status()
    return response


def update_a_project(project_id, name):
    headers = {
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {API_TOKEN}",
    }
    data = {"name": name}
    response = requests.post(
        f"{BASE_URL}/rest/v2/projects/{project_id}", data=data, headers=headers
    )
    # response.raise_for_status()
    return response


def delete_a_project(project_id):
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.delete(
        f"{BASE_URL}/rest/v2/projects/{project_id}", headers=header
    )
    # response.raise_for_status()
    return response


def get_all_collaborators(project_id):
    header = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(
        f"{BASE_URL}/rest/v2/projects/{project_id}/collaborators", headers=header
    )
    # response.raise_for_status()
    return response
