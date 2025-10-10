from playwright.sync_api import Page

from page_factory.title import Title
from pages.base_page import BasePage


class AccountPageToolshop(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title_account_page: Title = Title(
            page, locator="//h1[text()='My account']", name="My account"
        )

    def wait_for_page_loaded(self) -> None:
        self.page.wait_for_url(self.urls["account"])

    def check_title_account_page(self, text: str) -> None:
        self.title_account_page.should_contain_text(text=text)
