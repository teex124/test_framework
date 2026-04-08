import allure
from playwright.sync_api import Page


class BasePage:
    url = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.url)
        return self

    def click(self, locator):
        self.page.locator(locator).click()
        return  self

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)
