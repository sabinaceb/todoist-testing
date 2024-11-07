import os

BASE_URL = "https://app.todoist.com"
USERNAME = os.environ.get("USERNAME_ENV")
PASSWORD = os.environ.get("PASSWORD_ENV")
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_KEY = os.environ.get("BROWSERSTACK_KEY")
RUN_ON_BROWSERSTACK = os.environ.get("RUN_ON_BROWSERSTACK")
