from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class ProjectPage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver: WebDriver = driver
        self.actions: ActionChains = ActionChains(self.driver)
        self.url = f"{base_url}/app/inbox"

        # Locators
        self.btn_my_projects = (By.XPATH, "//BUTTON[@aria-label='My projects menu']")
        self.btn_add_project = (By.XPATH, "//DIV[@aria-label='Add project']")
        self.txt_name = (By.ID, "edit_project_modal_field_name")
        self.btn_create_project = (By.XPATH, "//BUTTON[@type='submit']")
        self.btn_more_actions = (
            By.XPATH,
            "//BUTTON[@aria-label='Project options menu']",
        )
        self.btn_delete = (By.XPATH, "//DIV[text()='Delete']")
        self.btn_modal_delete = (By.XPATH, "//BUTTON//SPAN[text()='Delete']/..")

    # Methods
    def load(self) -> None:
        self.driver.get(self.url)

    def tap_add_project_button(self) -> None:
        self.driver.find_element(*self.btn_my_projects).click()
        self.driver.find_element(*self.btn_add_project).click()

    def create_a_project(self, name: str) -> None:
        self.driver.find_element(*self.txt_name).send_keys(name)
        self.driver.find_element(*self.btn_create_project).click()

    def delete_project(self) -> None:
        self.driver.find_element(*self.btn_more_actions).click()
        self.driver.find_element(*self.btn_delete).click()
        self.driver.find_element(*self.btn_modal_delete).click()
