from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.input import Input


class LoginForm:
    def __init__(self, page: Page) -> None:
        self.page: Page = (page,)
        self.login_email: Input = Input(
            page,
            locator="input[data-test='email']",
            name="Login email",
        )
        self.login_password: Input = Input(
            page, locator="input[data-test='password']",
            name="Login password"
        )
        self.login_button: Button = Button(
            page,
            locator="[data-test='login-submit']",
            name="Login button",
        )

    def clear_input_email(self) -> None:
        self.login_email.clear()

    def fill_input_email(self, value_email: str) -> None:
        self.login_email.fill(value=value_email)

    def clear_input_password(self) -> None:
        self.login_password.clear()

    def fill_input_password(self, value_pwd: str) -> None:
        self.login_password.fill(value=value_pwd)

    def click_login_button(self) -> None:
        self.login_button.click()

    # def input_email(self, value: str) -> None:
    #     self._clear_input_email()
    #     self._fill_input_email(value_email=value)

    # def input_password(self, value: str) -> None:
    #     self._clear_input_password()
    #     self._fill_input_password(value_pwd=value)
