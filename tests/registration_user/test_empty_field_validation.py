import pytest

from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.mark.usefixtures("open_registration_page")
class TestEmptyFieldValidation:
    """Тесты для проверки валидации обязательных полей формы регистрации."""

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
        field: str,
        get_generated_file,
        registration_page_toolshop: RegistrationPageToolshop,
    ) -> None:
        """
        Тест проверки валидации пустых полей формы регистрации.

        Steps:
        1. Заполнить все поля формы регистрации кроме одного указанного
        2. Нажать кнопку регистрации
        3. Проверить отображение сообщения об ошибке для незаполненного поля

        Args:
            field: Название поля, которое должно остаться пустым
            get_generated_file: Фикстура сгенерированных данных пользователя
            registration_page_toolshop: Фикстура страницы регистрации
        """
        registration_page_toolshop.form.fill_all_fields_except(
            data=get_generated_file, exclude_field=field
        )
        registration_page_toolshop.click_button()
        registration_page_toolshop.form.check_error_text(error_field=field)
