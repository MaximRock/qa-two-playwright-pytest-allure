import logging

import allure
from playwright.sync_api import Locator, expect

from config.exception import ElementNotFoundError, ElementNotVisibleError
from page_factory.component import Component

logger = logging.getLogger(__name__)


class Input(Component):
    @property
    def type_of(self) -> str:
        return "Input"

    def clear(self, **kwargs) -> None:
        with allure.step(f"Clearing {self.type_of} '{self.name}'"):
            try:
                locator: Locator = self.wait_for_element(**kwargs)
                locator.clear()
            except Exception as e:
                logger.error(self.error_msg, exc_info=True)
                raise ElementNotFoundError(self.error_msg) from e

    def fill(self, value: str, validate_value: bool = False, **kwargs) -> None:
        try:
            with allure.step(f"Fill {self.type_of} '{self.name}' to value {value}"):
                locator: Locator = self.wait_for_element(**kwargs)
                locator.fill(value, force=False)

                if validate_value:
                    self.should_have_value()
        except Exception as e:
            logger.error({self.error_msg}, exc_info=True)
            raise ElementNotFoundError(self.error_msg) from e

    def should_have_value(self, value: str, **kwargs) -> None:
        try:
            with allure.step(
                f"Checking that {self.type_of} '{self.name}' has a value '{value}'"
            ):
                locator: Locator = self.get_locator(**kwargs)
                expect(locator).to_have_value(value)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotVisibleError(self.error_msg) from e
