import logging
import os
from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, Page, expect

from config.exception import (
    ElementNotFoundError,
    ElementNotVisibleError,
    ElementTimeoutError,
    LocatorNotStringError,
)

logger: logging.Logger = logging.getLogger(__name__)


class Component(ABC):
    """Абстрактный базовый класс для всех компонентов пользовательского интерфейса."""

    def __init__(self, page: Page, locator: str, name: str) -> None:
        """
        Инициализация базового компонента.
        Args:
            page: Экземпляр страницы Playwright
            locator: Локатор элемента на странице
            name: Человекочитаемое имя элемента для логирования
        """
        self.page: Page = page
        self.locator: str = locator
        self.name: str = name
        self.timeout: int = int(os.getenv("TIMEOUT", 5000))
        self.error_msg: str = (
            f"Element '{self.name}' with locator '{self.locator}'type '{self.type_of}'"
        )

    @property
    @abstractmethod
    def type_of(self) -> str:
        """Абстрактное свойство, возвращающее тип компонента.
        Returns:
            str: Тип компонента (например, 'button', 'input', 'title')
        """
        return "component"

    def get_locator(self, **kwargs) -> Locator:
        """Получить локатор элемента с подстановкой параметров.
        Args:
            **kwargs: Параметры для форматирования локатора
        Returns:
            Locator: Объект локатора Playwright
        Raises:
            LocatorNotStringError: Если локатор не является строкой
        """
        if not isinstance(self.locator, str):
            logger.error(
                f"Locator should be a string, but got {type(self.locator)}",
                exc_info=True,
            )
            raise LocatorNotStringError()

        locator: str = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def wait_for_element(self, timeout=None, **kwargs) -> Locator:
        """Ожидать появления элемента на странице.
        Args:
            timeout: Время ожидания в миллисекундах (по умолчанию из env)
            **kwargs: Дополнительные аргументы для локатора
        Returns:
            Locator: Видимый локатор элемента
        Raises:
            ElementTimeoutError: Если элемент не появился за указанное время
        """
        try:
            if timeout is None:
                timeout: float = self.timeout
            locator: Locator = self.get_locator(**kwargs)
            locator.wait_for(state="visible", timeout=timeout)
            return locator
        except Exception as e:
            logger.error(f"Element '{self.type_of}' timed out", exc_info=True)
            raise ElementTimeoutError() from e

    def click(self, **kwargs) -> None:
        """Кликнуть по элементу.
        Args:
            **kwargs: Дополнительные аргументы для локатора
        Raises:
            ElementNotFoundError: Если элемент не найден или недоступен для клика
        """
        try:
            with allure.step(f"Click on '{self.type_of}' with the name '{self.name}'"):
                locator: Locator = self.wait_for_element(**kwargs)
                locator.click()
        except Exception as e:
            logger.error(
                f"Element '{self.type_of}' with the name '{self.name}' not found",
            )
            raise ElementNotFoundError(f"{self.error_msg} not clickable") from e

    def should_be_visible(self, **kwargs) -> bool:
        """Проверить, что элемент видим на странице.
        Args:
            **kwargs: Дополнительные аргументы для локатора
        Returns:
            bool: True если элемент видим
        Raises:
            ElementNotVisibleError: Если элемент не видим в течение таймаута
        """
        try:
            with allure.step(
                f"Checking that '{self.type_of}' with the name '{self.name}' is visible"
            ):
                locator: Locator = self.get_locator(**kwargs)
                return expect(locator).to_be_visible(visible=True)
        except Exception as e:
            logger.error(f"Element '{self.type_of}' not visible", exc_info=True)
            raise ElementNotVisibleError(
                f"{self.error_msg} not visible within {self.timeout}ms"
            ) from e

    def should_to_have_text(self, text: str, **kwargs) -> None:
        """Проверить, что элемент содержит ожидаемый текст.
        Args:
            text: Ожидаемый текст элемента
            **kwargs: Дополнительные аргументы для локатора
        Raises:
            ElementNotVisibleError: Если элемент не содержит ожидаемый текст
        """
        try:
            with allure.step(
                f"Checking that {self.type_of} '{self.name}' has a text '{text}'"
            ):
                locator: Locator = self.wait_for_element(**kwargs)
                expect(locator).to_have_text(text)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotVisibleError(self.error_msg) from e
