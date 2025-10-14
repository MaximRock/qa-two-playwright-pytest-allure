from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.input import Input


class SearchForm:
    """Компонент формы поиска для взаимодействия с поисковой системой приложения."""

    def __init__(self, page: Page) -> None:
        """
        Инициализация компонентов формы поиска.
        Args:
            page: Экземпляр страницы Playwright для взаимодействия с браузером
        """
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
        """Сбросить поисковый запрос.
        Нажимает кнопку сброса поиска для очистки поискового поля и результатов.
        """
        self.search_reset_button.click()

    def search_fill(self, value: str) -> None:
        """Заполнить поле поиска указанным значением.
        Args:
            value: Текст для поиска товаров в каталоге
        """
        self.search_input.fill(value=value)

    def search_submit(self) -> None:
        """Отправить поисковый запрос.
        Нажимает кнопку отправки поиска для выполнения поиска по введенному запросу.
        """
        self.search_submit_button.click()
