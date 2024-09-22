from behave import Step
from faker import Faker

fake = Faker()


# New Tasks Steps
@Step("the user tap the add task button")
def step_tap_the_add_task_button(context):
    context.new_task_page = context.page_factory.get_page("dashboard")
    # context.new_task_page.load()
    context.new_task_page.tap_add_task_button()


@Step('the user create a task "{name}" "{description}"')
def step_create_a_task(context, name, description):
    context.new_task_page.create_a_task(name, description)


@Step('the user validates the task data "{name}" "{description}"')
def step_validate_the_task(context, name, description):
    context.new_task_page.validate_task(name, description)


@Step('the user creates "{number}" tasks')
def step_create_number_of_tasks(context, number):
    for _ in range(int(number)):
        task_name = fake.name()
        task_decription = fake.city()

        context.new_task_page.create_a_task(task_name, task_decription)
        context.new_task_page.validate_task(task_name, task_decription)
        context.new_task_page.delete_task(task_name)
