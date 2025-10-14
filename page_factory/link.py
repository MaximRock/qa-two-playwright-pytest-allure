import logging

import allure
from playwright.async_api import Locator

from config.exception import ElementNotVisibleError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Link(Component):
    """Компонент ссылки для работы с гиперссылками на веб-страницах."""

    @property
    def type_of(self) -> str:
        """Возвращает тип компонента для использования в логировании
        и сообщениях об ошибках.
        Returns:
            str: Тип компонента - 'link'
        """
        return "link"

    def wait_for_link(self, state: str, **kwargs) -> None:
        """Ожидать достижения ссылкой определенного состояния.
        Метод ожидает, пока ссылка перейдет в заданное состояние
        (visible, hidden, detached).
        Используется для синхронизации тестов с состоянием элементов страницы.
        Args:
            state: Ожидаемое состояние ссылки ('visible', 'hidden', 'detached')
            **kwargs: Дополнительные аргументы для локатора
        Raises:
            ElementNotVisibleError: Если ссылка не достигла ожидаемого состояния
                в течение заданного времени ожидания
        Example:
            >>> registration_link.wait_for_link(state="visible")
        """
        try:
            with allure.step(
                f"We expect that '{self.type_of}' "
                f"with  name '{self.name}' will '{state}'"
            ):
                locator: Locator = self.get_locator(**kwargs)
                locator.wait_for(state=state, timeout=self.timeout)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotVisibleError(self.error_msg) from e
