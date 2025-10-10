import logging

import allure
from playwright.async_api import Locator

from config.exception import ElementNotVisibleError
from page_factory.component import Component

logger: logging.Logger = logging.getLogger(__name__)


class Link(Component):
    @property
    def type_of(self) -> str:
        return "link"

    def wait_for_link(self, state: str, **kwargs) -> None:
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
