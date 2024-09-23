from behave import Step
from faker import Faker

fake = Faker()


@Step("the user tap the add task button")  # type: ignore
def step_tap_the_add_task_button(context):
    context.task_page = context.page_factory.get_page("task")
    # context.new_task_page.load()
    context.task_page.tap_add_task_button()


@Step('the user create a task "{name}" "{description}"')  # type: ignore
def step_create_a_task(context, name, description):
    context.task_page.create_a_task(name, description)


@Step('the user validates the task data "{name}" "{description}"')  # type: ignore
def step_validate_the_task(context, name, description):
    from selenium.webdriver.common.by import By

    txt_new_task_name = (
        By.XPATH,
        f"//DIV[@class='task_content' and contains(text(),'{name}')]",
    )
    txt_new_task_description = (
        By.XPATH,
        f"//DIV[@class='task_description']//P[contains(text(),'{description}')]",
    )
    assert context.task_page.driver.find_element(*txt_new_task_name).is_displayed()
    assert context.task_page.driver.find_element(
        *txt_new_task_description
    ).is_displayed()


@Step('the user creates "{number}" tasks')  # type: ignore
def step_create_number_of_tasks(context, number):
    from selenium.webdriver.common.by import By

    for _ in range(int(number)):
        task_name = fake.name()
        task_decription = fake.city()

        context.task_page.create_a_task(task_name, task_decription)
        txt_new_task_name = (
            By.XPATH,
            f"//DIV[@class='task_content' and contains(text(),'{task_name}')]",
        )
        txt_new_task_description = (
            By.XPATH,
            f"//DIV[@class='task_description']//P[contains(text(),'{task_decription}')]",
        )
        assert context.task_page.driver.find_element(*txt_new_task_name).is_displayed()
        assert context.task_page.driver.find_element(
            *txt_new_task_description
        ).is_displayed()
        context.task_page.delete_task(task_name)
