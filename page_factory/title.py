import logging

import allure
from playwright.sync_api import Locator, expect

from config.exception import ElementNotFoundError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Title(Component):
    """Компонент заголовка для работы с текстовыми заголовками на веб-страницах."""

    @property
    def type_of(self) -> str:
        """Возвращает тип компонента для использования в логировании
        и сообщениях об ошибках.

        Returns:
            str: Тип компонента - 'title'
        """
        return "title"

    def should_contain_text(self, text: str, **kwargs) -> None:
        """Проверить, что заголовок содержит точный указанный текст.
        Метод проверяет полное соответствие текста заголовка ожидаемому значению.
        Используется для валидации заголовков страниц,
        разделов и других текстовых элементов.
        Args:
            text: Ожидаемый точный текст заголовка
            **kwargs: Дополнительные аргументы для локатора
        Raises:
            ElementNotFoundError: Если заголовок не содержит точный ожидаемый текст
                или если произошла ошибка при проверке текста
        Example:
            >>> page_title.should_contain_text("Мой аккаунт")
            >>> section_title.should_contain_text("Личная информация")
        """
        try:
            with allure.step(
                f"Check that {self.type_of} with name "
                f"'{self.name}' contains text '{text}'"
            ):
                locator: Locator = self.wait_for_element(**kwargs)
                expect(locator).to_have_text(text, timeout=self.timeout)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotFoundError(self.error_msg) from e
