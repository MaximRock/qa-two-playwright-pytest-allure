import pytest

from pages.login_page_toolshop import LoginPageToolshop


@pytest.mark.usefixtures("open_main_page")
@pytest.mark.user_login
class TestOpenLogin:
    def test_open_login_page(
        self,
        login_page_toolshop: LoginPageToolshop,
    ) -> None:
        login_page_toolshop.navbar.visit_login_page()
        login_page_toolshop.check_login_page(text="Login")
