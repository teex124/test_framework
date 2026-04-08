import allure

from src.models.nvabar_btn import NavBarBtn
from src.models.search_input import SearchInput
from src.models.social_btn import SocialBtn

from src.utils.test_datas.test_data.navbar_data import NAVBAR_BUTTONS
from src.utils.test_datas.test_data.social_data import SOCIAL_BUTTONS
from src.utils.test_datas.test_data.seach_data import SEARCH_INPUTS

import pytest

@pytest.mark.ui
class TestHomePage:

    def test_open_product(self, home_page):
        home_page.open()
        home_page.check_open_product()

    @pytest.mark.parametrize(
        'navbar_btn',
        NAVBAR_BUTTONS,
        ids=[i.btn_text for i in NAVBAR_BUTTONS],
    )
    def test_navbar_buttons(self, home_page, navbar_btn: NavBarBtn):
        home_page.check_navbar_button(navbar_btn.btn_text, navbar_btn.search_text)

    @pytest.mark.parametrize(
        'social_btn',
        SOCIAL_BUTTONS,
        ids=[i.btn_locator[1::] for i in SOCIAL_BUTTONS],
    )
    def test_social_buttons(self, home_page, social_btn: SocialBtn):
        allure.dynamic.title(social_btn.btn_locator[1::])
        home_page.check_social_button(social_btn)


    @pytest.mark.parametrize(
        'search_input',
        SEARCH_INPUTS,
        ids=[i.test_description for i in SEARCH_INPUTS],
    )
    def test_search(self, home_page, search_input: SearchInput):
        allure.dynamic.title(search_input.test_description)
        home_page.check_search(search_input)




