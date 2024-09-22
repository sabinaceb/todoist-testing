from behave import Step


@Step("the user request to get all Projects")  # type: ignore
def step_request_get_all_projects(context):
    context.response = context.project_client.get_all_projects()


@Step('the user create a new project "{name}"')  # type: ignore
def step_create_new_project(context, name):
    context.response = context.project_client.create_new_project(name)


@Step('the user create a new project with invalid data "{name}", "{color}"')  # type: ignore
def step_create_new_project_with_invalid_data(context, name, color):
    context.response = context.project_client.create_new_project_invalid_data(
        name, color
    )


@Step("the user request to get a project")  # type: ignore
def step_get_project(context):
    context.response = context.project_client.get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = context.project_client.get_a_project(context.project_id)


@Step("the user request to get a non-existing project")  # type: ignore
def step_get_nonexisting_project(context):
    context.response = context.project_client.get_a_project(0)


@Step('the user update a project "{name}"')  # type: ignore
def step_update_project(context, name):
    context.response = context.project_client.get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = context.project_client.update_a_project(context.project_id, name)


@Step('the user update a non-existing project "{name}"')  # type: ignore
def step_update_nonexisting_project(context, name):
    context.response = context.project_client.update_a_project(0, name)


@Step("the user delete a project")  # type: ignore
def step_delete_project(context):
    context.response = context.project_client.get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = context.project_client.delete_a_project(context.project_id)


@Step("the user delete a non-existing project")  # type: ignore
def step_delete_nonexisting_project(context):
    context.response = context.project_client.delete_a_project(0)


@Step("the user request to get the collaborators of a project")  # type: ignore
def step_project_collaborators(context):
    context.response = context.project_client.get_all_projects()
    context.project_id = context.response.json()[-1]["id"]
    context.response = context.project_client.get_all_collaborators(context.project_id)


@Step("the user request to get the collaborators of a non-existing project")  # type: ignore
def step_project_nonexisting_collaborators(context):
    context.response = context.project_client.get_all_collaborators(0)
