import pytest
from playwright.sync_api import Page

from src.pages.home_page import HomePage


@pytest.fixture(scope="function")
def home_page(page: Page):
    yield HomePage(page).open()
