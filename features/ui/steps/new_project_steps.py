from behave import Step
from faker import Faker

fake = Faker()


# New Project Steps
@Step("the user tap the new project button")  # type: ignore
def step_tap_the_add_task_button(context):
    context.new_project_page = context.page_factory.get_page("inbox")
    # context.new_project_page.load()
    context.new_project_page.tap_add_project_button()


@Step("the user create a project")  # type: ignore
def step_create_a_task(context):
    context.project_name = fake.country()
    context.new_project_page.create_a_project(context.project_name)


@Step("the user validates the project data")  # type: ignore
def step_validate_the_task(context):
    context.new_project_page.validate_project(context.project_name)
    # Teardown
    context.new_project_page.delete_project()
