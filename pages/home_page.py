from time import sleep

from playwright.sync_api import expect

from pages.base import BasePage
import allure



class HomePage(BasePage):
    url = 'https://github.com/'
    def search_repository(self):
        allure.dynamic.title('Поиск репозитория')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description('Открытие Git Hub > Ввод данных > Enter > Проверка')
        allure.dynamic.story('Требуется возможность поиска репозиториев ')
        allure.dynamic.link(self.url)
        allure.attach('<h1>Hellow world</h1>', attachment_type=allure.attachment_type.HTML)
        with allure.step('Нажимаем на кнопку поиска репозитория'):
            self.page.locator('.header-search-button').click()
        with allure.step('Вводим данные в поиска'):
            input = self.page.locator('#query-builder-test')
            input.fill('teex124/pomodoro')
        with allure.step('Начинаем поиск'):
            input.press('Enter')
        self.page.get_by_role('link', name='teex124/pomodoro').click()
        self.page.get_by_role('link', name = '12 Commits').click()
        expect(self.page.get_by_role('link', name='ce02ad6')).to_be_visible()



