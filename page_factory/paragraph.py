import logging

import allure
from playwright.sync_api import Locator, expect

from config.exception import ElementNotFoundError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Paragraph(Component):
    @property
    def type_of(self) -> str:
        return "paragraph"

    def must_contain_text(self, text: str, **kwargs) -> None:
        try:
            with allure.step(f"The {self.type_of} {self.name} must contain {text}"):
                locator: Locator = self.wait_for_element(**kwargs)
                expect(locator).to_contain_text(text)
        except Exception as e:
            logger.error(self.error_msg, exc_info=True)
            raise ElementNotFoundError(self.error_msg) from e
