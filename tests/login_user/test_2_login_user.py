import pytest

from pages.account_page_toolshop import AccountPageToolshop
from pages.login_page_toolshop import LoginPageToolshop
from pages.main_page_toolshop import MainPageToolshop


@pytest.mark.usefixtures("open_login_page")
@pytest.mark.usefixtures("user_credentials")
@pytest.mark.usefixtures("user_full_name")
@pytest.mark.user_login
class TestLoginUser:
    def test_login_user(
        self,
        main_page_toolshop: MainPageToolshop,
        login_page_toolshop: LoginPageToolshop,
        account_page_toolshop: AccountPageToolshop,
    ) -> None:

        login_page_toolshop.login_email(email=self.email)
        login_page_toolshop.login_password(password=self.password)
        login_page_toolshop.login_form.click_login_button()
        account_page_toolshop.check_title_account_page(text="My account")
        main_page_toolshop.navbar.check_user_login(user_text=self.full_name)
