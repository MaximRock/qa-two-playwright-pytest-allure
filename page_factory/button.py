import allure
from playwright.sync_api import Locator

from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return "button"

    def __bool__(self) -> bool:
        try:
            return self.get_locator().is_visible(timeout=0)
        except TimeoutError:
            return False

    def is_visible(self, timeout: float, **kwargs) -> bool:
        with allure.step(
            f"Check that '{self.type_of}' with the name '{self.name}' visible"
        ):
            try:
                self.get_locator(**kwargs).wait_for(state="visible", timeout=timeout)
                return True
            except TimeoutError:
                return False

    def hover(self, **kwargs) -> None:
        with allure.step(
            f"Pointed to the button '{self.type_of}' with the name '{self.name}'"
        ):
            locator: Locator = self.is_visible(**kwargs)
            locator.hover()
