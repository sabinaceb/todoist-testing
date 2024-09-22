from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver, base_url: str) -> None:
        self.driver: WebDriver = driver
        self.url = f"{base_url}/auth/login"

        # locators
        self.txt_username = (By.ID, "element-0")
        self.txt_password = (By.ID, "element-3")
        self.btn_submit = (By.XPATH, "//BUTTON[@type='submit']")

    # functions
    def load(self) -> None:
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        self.driver.find_element(*self.txt_username).send_keys(username)
        self.driver.find_element(*self.txt_password).send_keys(password)
        self.driver.find_element(*self.btn_submit).click()

    def validate_unsuccessful_login(self) -> None:
        assert self.driver.find_element(*self.btn_submit).is_displayed()

    def validate_successful_login(self) -> None:
        assert self.driver.find_element(By.XPATH, "//H1[text()='Today']").is_displayed()
