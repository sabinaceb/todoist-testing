from behave import Step


@Step("the user request to get all Tasks")  # type: ignore
def step_request_get_all_tasks(context):
    context.response = context.task_client.get_active_tasks()


@Step("the user should receive a {status_code} status code")  # type: ignore
def step_receive_status_code(context, status_code):
    assert context.response.status_code == int(status_code)


@Step(
    'the user create a new task "{content}", "{due_string}", "{priority}", "{due_lang}"'
)  # type: ignore
def step_create_new_task(context, content, due_string, priority, due_lang):
    context.response = context.task_client.create_task(
        content, due_string, priority, due_lang
    )


@Step("the user request to get an active task")  # type: ignore
def step_get_active_task(context):
    context.response = context.task_client.get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = context.task_client.get_active_task(context.task_id)


@Step("the user request to get a non-existing active task")  # type: ignore
def step_get_active_nonexisting_task(context):
    context.response = context.task_client.get_active_task(0)


@Step('the user update an active task "{content}"')  # type: ignore
def step_update_task(context, content):
    context.response = context.task_client.get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = context.task_client.update_a_task(context.task_id, content)
    assert content == context.response.json()["content"]


@Step('the user update a non-existing active task "{content}"')  # type: ignore
def step_update_nonexisting_task(context, content):
    context.response = context.task_client.update_a_task(0, content)


@Step("the user close an active task")  # type: ignore
def step_close_task(context):
    context.response = context.task_client.get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = context.task_client.close_a_task(context.task_id)


@Step("the user close a non-existing active task")  # type: ignore
def step_close_nonexisting_task(context):
    context.response = context.task_client.close_a_task(0)


@Step("the user reopen a specific task")  # type: ignore
def step_reopen_task(context):
    # context.response = context.task_client.get_active_tasks()
    # context.task_id = context.response.json()[0]["id"]
    # context.response = context.task_client.close_a_task(context.task_id)
    context.reopen = context.task_client.reopen_a_task(context.task_id)


@Step("the user reopen a non-existing task")  # type: ignore
def step_reopen_nonexisting_task(context):
    context.response = context.task_client.reopen_a_task(0)


@Step("the user delete an active task")  # type: ignore
def step_delete_task(context):
    context.response = context.task_client.get_active_tasks()
    context.task_id = context.response.json()[0]["id"]
    context.response = context.task_client.delete_a_task(context.task_id)


@Step("the user delete a non-existing active task")  # type: ignore
def step_delete_non_existing_task(context):
    context.response = context.task_client.delete_a_task(0)
