from behave import Step
from faker import Faker

fake = Faker()


@Step("the user tap the new project button")  # type: ignore
def step_tap_the_add_task_button(context):
    context.project_page = context.page_factory.get_page("project")
    # context.new_project_page.load()
    context.project_page.tap_add_project_button()


@Step("the user create a project")  # type: ignore
def step_create_a_task(context):
    context.project_name = fake.country()
    context.project_page.create_a_project(context.project_name)


@Step("the user validates the project data")  # type: ignore
def step_validate_the_task(context):
    from selenium.webdriver.common.by import By

    txt_project_name = (By.XPATH, f"//H1[text()='{context.project_name}']")
    assert context.project_page.driver.find_element(*txt_project_name).is_displayed()
    # Teardown
    context.project_page.delete_project()
