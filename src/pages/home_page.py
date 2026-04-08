from time import sleep

from playwright.sync_api import expect
import allure

from src.models.search_input import SearchInput
from src.models.social_btn import SocialBtn

from src.pages.base import BasePage
from src.utils.test_datas.page_test_data.home_page_test_data import TestData



class HomePage(BasePage):
    url = 'https://sauce-demo.myshopify.com/'

    def check_open_product(self):
        '''Проверка возможности открыть продукт'''
        allure.dynamic.title('Проверка возможности открыть продукт')
        with allure.step('Нажатие на изображение продукции'):
            self.page.get_by_alt_text('Grey jacket').click()
        with allure.step('Проверка на url'):
            expect(self.page).to_have_url(TestData.JACKET_URL)
        return self

    def check_navbar_button(self, button_text: str, search_text: str):
        with allure.step('Нажатие на кнопку с текстом: ' + str(button_text)):
            self.page.get_by_role('link', name=button_text).click()
        with allure.step('Поиск заданного текста'):
            allure.attach(self.page.url, attachment_type=allure.attachment_type.TEXT)
            expect(self.page.get_by_text(search_text)).to_be_visible()
        return self

    def check_social_button(self, social_btn: SocialBtn):
        with allure.step(f'Нажатие на кнопку с локатором {social_btn.btn_locator}'):
            with self.page.context.expect_page() as new_page:
                self.click(social_btn.btn_locator)
            new_page = new_page.value
        with allure.step('Проверка соответствия URL'):
            expect(new_page).to_have_url(social_btn.open_link)
        return self

    def check_search(self, search_input: SearchInput):
        with allure.step('Заполнение поля поиска продукции'):
            self.fill('#search-field', search_input.searched_item)
        with allure.step('Нажатие на кнопку поиска'):
            self.click('#search-submit')
        with allure.step('Ожидание изображение продукции'):
            expect(self.page.get_by_alt_text(search_input.image_alt_text)).to_be_visible()
        return self