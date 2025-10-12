from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.title import Title
from pages.base_page import BasePage


class ProductPageToolshop(BasePage):
    """Page Object Model для страницы товара в приложении Toolshop."""

    def __init__(self, page: Page) -> None:
        """
        Инициализация страницы товара.
        Args:
            page: Экземпляр страницы Playwright для взаимодействия с браузером
        """
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
        """
        Проверить название товара на странице.
        Args:
            product_name: Ожидаемое название товара
        Raises:
            AssertionError: Если название товара не соответствует ожидаемому
        """
        self.title_product_name.should_to_have_text(text=product_name)

    def click_button_add_to_cart(self) -> None:
        """Нажать кнопку добавления товара в корзину."""
        self.button_add_to_cart.click()

    def add_multiple_items(self, items: int) -> None:
        """
        Добавить несколько единиц товара в корзину.
        Args:
            items: Количество единиц товара для добавления в корзину
        """
        for _ in range(items):
            self.click_button_add_to_cart()
