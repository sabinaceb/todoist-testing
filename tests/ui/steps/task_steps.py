from behave import Step
from faker import Faker

fake = Faker()


@Step("the user click the add task button")  # type: ignore
def step_click_the_add_task_button(context):
    context.task_page = context.page_factory.get_page("task")
    # context.new_task_page.load()
    context.task_page.click_add_task_button()


# TODO: Generar un escenario en el Task Feature para crear un nuevo task usando este metodo
@Step('the user create a task "{name}" "{description}"')  # type: ignore
def step_create_a_task(context, name, description):
    context.task_page.create_a_task(name, description)


# TODO: Validar el paso de arriba con este metodo
@Step('the user validates the task data "{name}" "{description}"')  # type: ignore
def step_validate_the_task(context, name, description):
    txt_new_task_name = context.task_page.new_task_name(name)
    txt_new_task_description = context.task_page.new_task_description(description)

    assert context.task_page.driver.find_element(*txt_new_task_name).is_displayed()
    assert context.task_page.driver.find_element(
        *txt_new_task_description
    ).is_displayed()


@Step('the user creates "{number}" tasks')  # type: ignore
def step_create_number_of_tasks(context, number):
    for _ in range(int(number)):
        task_name = fake.name()
        task_decription = fake.city()

        context.task_page.create_a_task(task_name, task_decription)
        txt_new_task_name = context.task_page.new_task_name(task_name)
        txt_new_task_description = context.task_page.new_task_description(
            task_decription
        )

        assert context.task_page.driver.find_element(*txt_new_task_name).is_displayed()
        assert context.task_page.driver.find_element(
            *txt_new_task_description
        ).is_displayed()
        context.task_page.delete_task(task_name)
