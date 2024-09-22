from behave import Step
from config import USERNAME, PASSWORD

# Login Steps


@Step("the user navigates to the login page")  # type: ignore
def step_navigate_to_login_page(context):
    context.login_page = context.page_factory.get_page("login")
    context.login_page.load()


@Step("the user logs in with valid credentials")  # type: ignore
def step_login_with_valid_credentials(context):
    context.login_page.login(USERNAME, PASSWORD)


@Step('the user logs in with invalid credentials "{invalid_user}" "{password}"')  # type: ignore
def step_login_with_invalid_credentials(context, invalid_user, password):
    context.login_page.login(invalid_user, password)


@Step("the user should be redirected to the dashboard")  # type: ignore
def step_verify_login_successful(context):
    context.login_page.validate_successful_login()


@Step("the user should see an error message")  # type: ignore
def step_verify_login_unsuccessful(context):
    context.login_page.validate_unsuccessful_login()
