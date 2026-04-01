from playwright.sync_api import Page

from pages.home_page import HomePage
import pytest

@pytest.mark.ui
def test_home_page(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.search_repository()

