import pytest

from pages.login_page_toolshop import LoginPageToolshop
from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.mark.user_registration
@pytest.mark.usefixtures("open_registration_page")
class TestRegistrationUser:
    def test_registration_user(
        self,
        get_generated_file,
        login_page_toolshop: LoginPageToolshop,
        registration_page_toolshop: RegistrationPageToolshop,
    ) -> None:

        registration_page_toolshop.form.fill_all_fields_except(data=get_generated_file)
        registration_page_toolshop.click_button()
        login_page_toolshop.check_login_page(text="Login")
