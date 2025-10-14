import logging

import allure
from playwright.sync_api import Locator, expect

from config.exception import ElementNotFoundError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Paragraph(Component):
    """Компонент параграфа для работы с текстовыми блоками на веб-страницах."""

    @property
    def type_of(self) -> str:
        """Возвращает тип компонента для использования в логировании
        и сообщениях об ошибках.
        Returns:
            str: Тип компонента - 'paragraph'
        """
        return "paragraph"

    def must_contain_text(self, text: str, **kwargs) -> None:
        """Проверить, что параграф содержит указанный текст.
        Метод проверяет, что текстовый блок содержит ожидаемый текст
        (частичное совпадение).
        Используется для валидации содержания текстовых элементов на странице.
        Args:
            text: Ожидаемый текст, который должен содержаться в параграфе
            **kwargs: Дополнительные аргументы для локатора
        Raises:
            ElementNotFoundError: Если параграф не содержит ожидаемый текст
                или если произошла ошибка при проверке текста
        Example:
            >>> welcome_message.must_contain_text("Добро пожаловать")
        """
        try:
            with allure.step(f"The {self.type_of} {self.name} must contain {text}"):
                locator: Locator = self.wait_for_element(**kwargs)
                expect(locator).to_contain_text(text)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotFoundError(self.error_msg) from e
