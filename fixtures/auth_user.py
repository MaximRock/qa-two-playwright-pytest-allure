import pytest

from pages.account_page_toolshop import AccountPageToolshop as account_page_toolshop
from pages.login_page_toolshop import LoginPageToolshop as login_page_toolshop


@pytest.fixture
def auth_user(page, open_login_page, get_generated_file) -> None:
    login_page_toolshop(page).login_email(email=get_generated_file["email"])
    login_page_toolshop(page).login_password(password=get_generated_file["password"])
    login_page_toolshop(page).login_form.click_login_button()
    account_page_toolshop(page).wait_for_page_loaded()
