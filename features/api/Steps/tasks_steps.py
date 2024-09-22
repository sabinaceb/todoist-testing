from behave import Step
from todoist_requests.todoist_requests import *


# TASKS
@Step("the user request to get all Tasks")
def step_request_get_all_tasks(context):
    context.response = get_active_tasks()


@Step("the user should receive a {status_code} status code")
def step_receive_status_code(context, status_code):
    assert context.response.status_code == int(status_code)


@Step(
    'the user create a new task "{content}", "{due_string}", "{priority}", "{due_lang}"'
)
def step_create_new_task(context, content, due_string, priority, due_lang):
    context.response = create_new_task(content, due_string, priority, due_lang)


@Step("the user request to get an active task")
def step_get_active_task(context):
    context.response = get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = get_active_task(context.task_id)


@Step("the user request to get a non-existing active task")
def step_get_active_nonexisting_task(context):
    context.response = get_active_task(0)


@Step('the user update an active task "{content}"')
def step_update_task(context, content):
    context.response = get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = update_a_task(context.task_id, content)
    assert content == context.response.json()["content"]


@Step('the user update a non-existing active task "{content}"')
def step_update_nonexisting_task(context, content):
    context.response = update_a_task(0, content)


@Step("the user close an active task")
def step_close_task(context):
    context.response = get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = close_a_task(context.task_id)


@Step("the user close a non-existing active task")
def step_close_nonexisting_task(context):
    context.response = close_a_task(0)


@Step("the user reopen a specific task")
def step_reopen_task(context):
    context.response = get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = close_a_task(context.task_id)
    context.reopen = reopen_a_task(context.task_id)


@Step("the user reopen a non-existing task")
def step_reopen_nonexisting_task(context):
    context.response = reopen_a_task(0)


@Step("the user delete an active task")
def step_delete_task(context):
    context.response = get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = delete_a_task(context.task_id)


@Step("the user delete a non-existing active task")
def step_delete_non_existing_task(context):
    context.response = delete_a_task(0)


# PROJECTS
@Step("the user request to get all Projects")
def step_request_get_all_projects(context):
    context.response = get_all_projects()


@Step('the user create a new project "{name}"')
def step_create_new_project(context, name):
    context.response = create_new_project(name)


@Step('the user create a new project with invalid data "{name}", "{color}"')
def step_create_new_project_with_invalid_data(context, name, color):
    context.response = create_new_project_invalid_data(name, color)


@Step("the user request to get a project")
def step_get_project(context):
    context.response = get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = get_a_project(context.project_id)


@Step("the user request to get a non-existing project")
def step_get_nonexisting_project(context):
    context.response = get_a_project(0)


@Step('the user update a project "{name}"')
def step_update_project(context, name):
    context.response = get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = update_a_project(context.project_id, name)


@Step('the user update a non-existing project "{name}"')
def step_update_nonexisting_project(context, name):
    context.response = update_a_project(0, name)


@Step("the user delete a project")
def step_delete_project(context):
    context.response = get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = delete_a_project(context.project_id)


@Step("the user delete a non-existing project")
def step_delete_nonexisting_project(context):
    context.response = delete_a_project(0)


@Step("the user request to get the collaborators of a project")
def step_project_collaborators(context):
    context.response = get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = get_all_collaborators(context.project_id)


@Step("the user request to get the collaborators of a non-existing project")
def step_project_nonexisting_collaborators(context):
    context.response = get_all_collaborators(0)
