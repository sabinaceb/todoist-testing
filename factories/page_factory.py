from pages.login_page import LoginPage
from pages.new_task_page import NewTask
from pages.new_project_page import ProjectPage
from selenium.webdriver.remote.webdriver import WebDriver


class PageFactory:
    def __init__(self, driver: WebDriver, base_url: str) -> None:
        self.driver: WebDriver = driver
        self.base_url: str = base_url

    def get_page(self, page_name: str) -> object:
        if page_name == "login":
            return LoginPage(self.driver, self.base_url)
        elif page_name == "dashboard":
            return NewTask(self.driver, self.base_url)
        elif page_name == "inbox":
            return ProjectPage(self.driver, self.base_url)
        else:
            raise ValueError(f"Unknown page:{page_name}")
