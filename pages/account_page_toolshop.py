from playwright.sync_api import Page

from page_factory.title import Title
from pages.base_page import BasePage


class AccountPageToolshop(BasePage):
    """Page Object Model для страницы 'Мой аккаунт' в приложении Toolshop."""

    def __init__(self, page: Page) -> None:
        """
        Инициализация страницы AccountPageToolshop.
        Args:
            page: Экземпляр страницы Playwright для взаимодействия с браузером
        """
        super().__init__(page)
        self.title_account_page: Title = Title(
            page, locator="//h1[text()='My account']", name="My account"
        )

    def wait_for_page_loaded(self) -> None:
        """
        Ожидание полной загрузки страницы аккаунта путем проверки URL.
        Метод ожидает пока браузер не перейдет на URL страницы аккаунта,
        определенный в конфигурации urls базовой страницы.
        """
        self.page.wait_for_url(self.urls["account"])

    def check_title_account_page(self, text: str) -> None:
        """
        Проверить, что заголовок страницы аккаунта содержит ожидаемый текст.
        Args:
            text: Ожидаемый текст, который должен содержаться
            в заголовке страницы аккаунта
        Raises:
            AssertionError: Если заголовок не содержит ожидаемый текст
        """
        self.title_account_page.should_contain_text(text=text)
