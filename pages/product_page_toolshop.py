from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.title import Title
from pages.base_page import BasePage


class ProductPageToolshop(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title_product_name: Title = Title(
            page=page, locator="h1[data-test='product-name']", name="Title product name"
        )
        self.button_add_to_cart: Button = Button(
            page=page,
            locator="button[data-test='add-to-cart']",
            name="Button add to cart",
        )

    def check_product_name(self, product_name: str) -> None:
        self.title_product_name.should_to_have_text(text=product_name)

    def click_button_add_to_cart(self) -> None:
        self.button_add_to_cart.click()

    def add_multiple_items(self, items: int) -> None:
        for _ in range(items):
            self.click_button_add_to_cart()
