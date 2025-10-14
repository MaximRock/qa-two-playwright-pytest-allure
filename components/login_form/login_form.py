from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.input import Input


class LoginForm:
    """Компонент формы авторизации для страницы входа в систему."""

    def __init__(self, page: Page) -> None:
        """
        Инициализация компонентов формы авторизации.
        Args:
            page: Экземпляр страницы Playwright для взаимодействия с браузером
        """
        self.page: Page = (page,)
        self.login_email: Input = Input(
            page,
            locator="input[data-test='email']",
            name="Login email",
        )
        self.login_password: Input = Input(
            page, locator="input[data-test='password']", name="Login password"
        )
        self.login_button: Button = Button(
            page,
            locator="[data-test='login-submit']",
            name="Login button",
        )

    def clear_input_email(self) -> None:
        """Очистить поле ввода email."""
        self.login_email.clear()

    def fill_input_email(self, value_email: str) -> None:
        """Заполнить поле ввода email.
        Args:
            value_email: Email пользователя для авторизации
        """
        self.login_email.fill(value=value_email)

    def clear_input_password(self) -> None:
        """Очистить поле ввода пароля."""
        self.login_password.clear()

    def fill_input_password(self, value_pwd: str) -> None:
        """Заполнить поле ввода пароля.
        Args:
            value_pwd: Пароль пользователя для авторизации
        """
        self.login_password.fill(value=value_pwd)

    def click_login_button(self) -> None:
        """Нажать кнопку авторизации для входа в систему."""
        self.login_button.click()
