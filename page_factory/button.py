import allure
from playwright.sync_api import Locator

from page_factory.component import Component


class Button(Component):
    """Компонент кнопки для взаимодействия в пользовательском интерфейсе."""

    @property
    def type_of(self) -> str:
        """Возвращает тип компонента для использования в логировании и
        сообщениях об ошибках.
        Returns:
            str: Тип компонента - 'button'
        """
        return "button"

    def __bool__(self) -> bool:
        """Проверяет видимость кнопки без ожидания.
        Returns:
            bool: True если кнопка видима, False в противном случае
        """
        try:
            return self.get_locator().is_visible(timeout=0)
        except TimeoutError:
            return False

    def is_visible(self, timeout: float, **kwargs) -> bool:
        """Проверяет видимость кнопки с заданным временем ожидания.
        Args:
            timeout: Время ожидания в миллисекундах
            **kwargs: Дополнительные аргументы для локатора
        Returns:
            bool: True если кнопка стала видимой в течение заданного времени,
            False в противном случае
        """
        with allure.step(
            f"Check that '{self.type_of}' with the name '{self.name}' visible"
        ):
            try:
                self.get_locator(**kwargs).wait_for(state="visible", timeout=timeout)
                return True
            except TimeoutError:
                return False

    def hover(self, **kwargs) -> None:
        """Наводит курсор на кнопку.
        Args:
            **kwargs: Дополнительные аргументы для локатора
        """
        with allure.step(
            f"Pointed to the button '{self.type_of}' with the name '{self.name}'"
        ):
            locator: Locator = self.is_visible(**kwargs)
            locator.hover()
