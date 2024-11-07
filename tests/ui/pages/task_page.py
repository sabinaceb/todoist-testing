from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from .base_page import BasePage


class TaskPage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str):
        super().__init__(driver, base_url)
        self.actions: ActionChains = ActionChains(self.driver)
        self.url = f"{base_url}/app/today"

        # Locators
        self.btn_add_task = (By.CLASS_NAME, "plus_add_button")
        self.content_task_list = (By.CLASS_NAME, "task_list_item__content")
        self.txt_name = (By.XPATH, "//DIV[@aria-label='Task name']")
        self.txt_description = (By.XPATH, "//DIV[@aria-label='Description']")
        self.btn_create_task = (
            By.XPATH,
            "//BUTTON[@data-testid='task-editor-submit-button']",
        )
        self.btn_more_actions = (By.XPATH, "//BUTTON[@data-testid='more_menu']")
        self.btn_delete = (
            By.XPATH,
            "//DIV[@data-action-hint='task-overflow-menu-delete']//DIV[contains(text(),'Delete')]",
        )
        self.btn_dialog_delete = (
            By.XPATH,
            "//BUTTON//SPAN[contains(text(), 'Delete')]/..",
        )

    # Methods
    def new_task_name(self, name: str) -> tuple[By, str]:
        return (By.XPATH, f"//DIV[@class='task_content' and contains(text(),'{name}')]")

    def new_task_description(self, description: str) -> tuple[By, str]:
        return (
            By.XPATH,
            f"//DIV[@class='task_description']//P[contains(text(),'{description}')]",
        )

    def click_add_task_button(self) -> None:
        self.driver.find_element(*self.btn_add_task).click()

    def create_a_task(self, name: str, description: str) -> None:
        self.driver.find_element(*self.txt_name).send_keys(name)
        for element in description:
            self.driver.find_element(*self.txt_description).send_keys(element)
        time.sleep(0.1)
        self.driver.find_element(*self.btn_create_task).click()

    def delete_task(self, name: str) -> None:
        txt_task_by_name = (
            By.XPATH,
            f"//DIV[@class='task_content' and contains(text(), '{name}')]",
        )
        task_content = self.driver.find_element(*txt_task_by_name)
        self.actions.move_to_element(task_content).perform()

        self.driver.find_element(*self.btn_more_actions).click()
        self.driver.find_element(*self.btn_delete).click()
        self.driver.find_element(*self.btn_dialog_delete).click()
