import logging

import allure
from playwright.sync_api import Locator

from config.exception import ElementNotFoundError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Select(Component):
    """Компонент выпадающего списка для работы с элементами select на веб-страницах."""

    @property
    def type_of(self) -> str:
        """Возвращает тип компонента для использования в
        логировании и сообщениях об ошибках.
        Returns:
            str: Тип компонента - 'select'
        """
        return "select"

    def select_option(self, value: str, **kwargs) -> None:
        """Выбрать опцию в выпадающем списке по значению.
        Метод выбирает указанное значение в выпадающем списке.
        Используется для заполнения форм, где присутствуют элементы select.
        Args:
            value: Значение опции, которую необходимо выбрать
            **kwargs: Дополнительные аргументы для локатора
        Raises:
            ElementNotFoundError: Если выпадающий список не найден
                или если произошла ошибка при выборе опции
        Example:
            >>> country_select.select_option("RU")
            >>> payment_method.select_option("credit_card")
        """
        try:
            with allure.step(f"Choose {self.type_of} {self.name} option {value}"):
                locator: Locator = self.wait_for_element(**kwargs)
                locator.select_option(value=value)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotFoundError(self.error_msg) from e
