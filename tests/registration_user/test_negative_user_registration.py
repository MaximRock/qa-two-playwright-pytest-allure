import pytest
from playwright.sync_api import Page, expect

from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.mark.usefixtures("open_registration_page")
class TestNegativeUserRegistration:
    @pytest.mark.parametrize(
        "field",
        [
            "first_name",
            "last_name",
            "date_of_birth",
            "street_name",
            "postcode",
            "city",
            "region",
            "country",
            "phone",
            "email",
            "password",
        ],
    )
    def test_empty_field_validation(
        self,
        page: Page,
        field: str,
        get_generated_file,
        registration_page_toolshop: RegistrationPageToolshop,
    ) -> None:
        """
        Тест проверки валидации пустых полей формы регистрации
        """
        registration_page_toolshop.form.fill_all_fields_except(
            data=get_generated_file, exclude_field=field
        )
        registration_page_toolshop.click_button()
        registration_page_toolshop.form.check_error_text(error_field=field)
