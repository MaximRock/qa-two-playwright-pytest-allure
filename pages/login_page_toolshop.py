from playwright.sync_api import Page

from components.login_form.login_form import LoginForm
from page_factory.title import Title
from pages.base_page import BasePage


class LoginPageToolshop(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_form: LoginForm = LoginForm(page)
        self.title_login_page: Title = Title(
            page, locator="//h3[text()='Login']", name="Login"
        )

    def check_login_page(self, text: str) -> None:
        self.title_login_page.should_contain_text(text=text)

    def login_email(self, email: str) -> None:
        self.login_form.clear_input_email()
        self.login_form.fill_input_email(value_email=email)

    def login_password(self, password: str) -> None:
        self.login_form.clear_input_password()
        self.login_form.fill_input_password(value_pwd=password)
