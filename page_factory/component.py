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
    NoElementsFoundError,
)

logger: logging.Logger = logging.getLogger(__name__)


class Component(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
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
        return "component"

    def get_locator(self, **kwargs) -> Locator:
        if not isinstance(self.locator, str):
            logger.error(
                f"Locator should be a string, but got {type(self.locator)}",
                exc_info=True,
            )
            raise LocatorNotStringError()

        locator: str = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def get_elements(self, **kwargs) -> list:
        elements: list = self.get_locator(**kwargs).all()
        if not elements:
            logger.error(
                f"No elements found '{elements}' locator '{self.locator}'",
                exc_info=True,
            )
            raise NoElementsFoundError()

        return elements

    def wait_for_element(self, timeout=None, **kwargs) -> Locator:
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
        try:
            with allure.step(
                f"Checking that {self.type_of} '{self.name}' has a text '{text}'"):
                locator: Locator = self.wait_for_element(**kwargs)
                expect(locator).to_have_text(text)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotVisibleError(self.error_msg) from e

    def should_to_have_url(self, url: str) -> None:
        try:
            with allure.step(
                f"Checking that {self.type_of} '{self.name}' has a url '{url}'"):
                expect(self.page).to_have_url(url)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotVisibleError(self.error_msg) from e
