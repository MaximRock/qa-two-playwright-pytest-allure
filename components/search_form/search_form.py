from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.input import Input


class SearchForm:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.search_input: Input = Input(
            page,
            locator="input[data-test='search-query']",
            name="Input Search",
        )
        self.search_reset_button: Button = Button(
            page,
            locator="button[data-test='search-reset']",
            name="Reset Search",
        )
        self.search_submit_button: Button = Button(
            page,
            locator="button[data-test='search-submit']",
            name="Submit Search",
        )

    def search_reset(self) -> None:
        self.search_reset_button.click()

    def search_fill(self, value: str) -> None:
        self.search_input.fill(value=value)

    def search_submit(self) -> None:
        self.search_submit_button.click()
