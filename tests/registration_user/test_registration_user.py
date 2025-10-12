import pytest

from pages.login_page_toolshop import LoginPageToolshop
from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.mark.user_registration
@pytest.mark.usefixtures("open_registration_page")
class TestRegistrationUser:
    """Тесты для проверки регистрации нового пользователя."""

    def test_registration_user(
        self,
        get_generated_file,
        login_page_toolshop: LoginPageToolshop,
        registration_page_toolshop: RegistrationPageToolshop,
    ) -> None:
        """
        Тест успешной регистрации нового пользователя.

        Steps:
        1. Заполнить все обязательные поля формы регистрации
        2. Нажать кнопку регистрации
        3. Проверить, что произошел переход на страницу авторизации

        Args:
            get_generated_file: Фикстура сгенерированных данных пользователя
            login_page_toolshop: Фикстура страницы авторизации
            registration_page_toolshop: Фикстура страницы регистрации
        """
        registration_page_toolshop.form.fill_all_fields_except(data=get_generated_file)
        registration_page_toolshop.click_button()
        login_page_toolshop.check_login_page(text="Login")
