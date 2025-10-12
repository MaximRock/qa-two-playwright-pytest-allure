import pytest

from pages.account_page_toolshop import AccountPageToolshop
from pages.login_page_toolshop import LoginPageToolshop
from pages.main_page_toolshop import MainPageToolshop


@pytest.mark.usefixtures("open_login_page")
@pytest.mark.usefixtures("user_credentials")
@pytest.mark.usefixtures("user_full_name")
@pytest.mark.user_login
class TestLoginUser:
    """Тесты для проверки функциональности авторизации пользователя."""

    def test_login_user(
        self,
        main_page_toolshop: MainPageToolshop,
        login_page_toolshop: LoginPageToolshop,
        account_page_toolshop: AccountPageToolshop,
    ) -> None:
        """
        Тест успешной авторизации пользователя.
        Steps:
        1. Заполнить поле email данными пользователя
        2. Заполнить поле password данными пользователя
        3. Нажать кнопку авторизации
        4. Проверить переход на страницу аккаунта
        5. Проверить отображение имени пользователя в навигационной панели
        Args:
            main_page_toolshop: Фикстура главной страницы
            login_page_toolshop: Фикстура страницы авторизации
            account_page_toolshop: Фикстура страницы аккаунта
        """
        login_page_toolshop.login_email(email=self.email)
        login_page_toolshop.login_password(password=self.password)
        login_page_toolshop.login_form.click_login_button()
        account_page_toolshop.check_title_account_page(text="My account")
        main_page_toolshop.navbar.check_user_login(user_text=self.full_name)
