import allure
from playwright.sync_api import Page


class BasePage:
    url = None
    def __init__(self, page: Page):
        self.page = page
    @allure.step('Открытие окна')
    def open(self):
        self.page.goto(self.url)

