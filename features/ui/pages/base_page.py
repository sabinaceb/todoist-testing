from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str) -> None:
        self.driver: WebDriver = driver
        self.url = base_url

    # Load Page Method
    def load(self) -> None:
        self.driver.get(self.url)
