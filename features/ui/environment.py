from selenium import webdriver
from factories.page_factory import PageFactory
from config import BASE_URL
import time


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.page_factory = PageFactory(context.driver, BASE_URL)


def after_all(context):
    time.sleep(0.3)
    context.driver.quit()
