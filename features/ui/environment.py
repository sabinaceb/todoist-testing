from config import (
    BASE_URL,
    # BROWSER_NAME,
    BROWSERSTACK_USERNAME,
    BROWSERSTACK_KEY,
    RUN_ON_BROWSERSTACK,
)
from factories.page_factory import PageFactory

from selenium import webdriver
from selenium.webdriver.common.options import BaseOptions
import time
from typing import Any


def before_all(context: Any) -> None:
    if RUN_ON_BROWSERSTACK:
        # options = BaseOptions()
        # if BROWSER_NAME == "Chrome":
        options = webdriver.ChromeOptions()
        options.set_capability("os", context.config.userdata.get("os"))
        options.set_capability("os_version", context.config.userdata.get("os_version"))
        options.set_capability("browser", context.config.userdata.get("browser"))
        options.set_capability(
            "browser_version", context.config.userdata.get("browser_version")
        )
        options.set_capability("name", "Behave UI Test on BrowserStack")

        context.driver = webdriver.Remote(
            command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_KEY}@hub-cloud.browserstack.com/wd/hub",
            options=options,
        )
    else:
        context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.page_factory = PageFactory(context.driver, BASE_URL)


def after_all(context: Any) -> None:
    time.sleep(0.3)
    context.driver.quit()
