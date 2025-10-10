from playwright.sync_api import Page

from components.registration_form.registration_form import RegistrationForm
from page_factory.button import Button
from page_factory.link import Link
from page_factory.title import Title
from pages.base_page import BasePage


class RegistrationPageToolshop(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.form: RegistrationForm = RegistrationForm(page)
        self.register_account: Link = Link(
            page, locator="[data-test='register-link']", name="Register your account"
        )
        self.title_registration_page: Title = Title(
            page,
            locator="//h3[text()='Customer registration']",
            name="Customer registration",
        )
        self.button_register: Button = Button(
            page,
            locator="[data-test='register-submit']",
            name="Register button",
        )

    def open_registration_page_toolship(self) -> None:
        self.register_account.wait_for_link(state="visible")
        self.register_account.click()

    def check_registration_page(self, text: str) -> None:
        self.title_registration_page.should_contain_text(text=text)

    def click_button(self) -> None:
        if self.button_register:
            self.button_register.is_visible(timeout=5000)
            self.button_register.click()
