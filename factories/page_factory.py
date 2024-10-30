from pages.login_page import LoginPage
from pages.task_page import TaskPage
from pages.project_page import ProjectPage
from selenium.webdriver.remote.webdriver import WebDriver


class PageFactory:
    def __init__(self, driver: WebDriver, base_url: str) -> None:
        self.driver: WebDriver = driver
        self.base_url: str = base_url

    def get_page(self, page_name: str) -> object:
        match page_name:
            case "login":
                return LoginPage(self.driver, self.base_url)
            case "task":
                return TaskPage(self.driver, self.base_url)
            case "project":
                return ProjectPage(self.driver, self.base_url)
            case _:
                raise ValueError(f"Unknown page:{page_name}")
