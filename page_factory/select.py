import logging

import allure
from playwright.sync_api import Locator

from config.exception import ElementNotFoundError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Select(Component):
    @property
    def type_of(self) -> str:
        return "select"

    def select_option(self, value: str, **kwargs) -> None:
        try:
            with allure.step(f"Choose {self.type_of} {self.name} option {value}"):
                locator: Locator = self.wait_for_element(**kwargs)
                locator.select_option(value=value)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotFoundError(self.error_msg) from e
