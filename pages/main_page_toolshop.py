from playwright.sync_api import Page

from components.search_form.search_form import SearchForm
from page_factory.title import Title
from pages.base_page import BasePage


class MainPageToolshop(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_form: SearchForm = SearchForm(page)
        self.product_name: Title = Title(
            page,
            locator="//h5[text()=' M4 Nuts ']",
            name="Product name",
        )

    def search(self, search_value: str) -> None:
        self.search_form.search_reset()
        self.search_form.search_fill(value=search_value)
        self.search_form.search_submit()

    def check_search_result(self, serch_result: str) -> None:
        self.product_name.should_contain_text(text=serch_result)

    def click_product(self) -> None:
        self.product_name.click()
