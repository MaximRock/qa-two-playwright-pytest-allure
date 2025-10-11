import pytest

from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.mark.user_registration
@pytest.mark.usefixtures("registration_page")
class TestOpenRegistrationPage:
    def test_open_registration_page(
        self,
        registration_page_toolshop: RegistrationPageToolshop,
    ) -> None:
        registration_page_toolshop.open_registration_page_toolship()
        registration_page_toolshop.check_registration_page(text="Customer registration")
