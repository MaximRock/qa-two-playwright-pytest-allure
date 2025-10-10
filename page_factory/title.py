import logging

import allure
from playwright.sync_api import Locator, expect

from config.exception import ElementNotFoundError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Title(Component):
    @property
    def type_of(self) -> str:
        return "title"

    def should_contain_text(self, text: str, **kwargs) -> None:
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
