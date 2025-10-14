import pytest

from pages.account_page_toolshop import AccountPageToolshop as account_page_toolshop
from pages.login_page_toolshop import LoginPageToolshop as login_page_toolshop


@pytest.fixture
def auth_user(page, open_login_page, get_generated_file) -> None:
    """
    Фикстура для авторизации пользователя перед выполнением тестов.

    Выполняет полный процесс авторизации пользователя с использованием
    сгенерированных данных и ожидает загрузки страницы аккаунта.

    Args:
        page: Фикстура страницы Playwright
        open_login_page: Фикстура открытия страницы авторизации
        get_generated_file: Фикстура с данными пользователя

    Steps:
        1. Заполняет поле email данными пользователя
        2. Заполняет поле password данными пользователя
        3. Нажимает кнопку авторизации
        4. Ожидает загрузки страницы аккаунта

    Usage:
        @pytest.mark.usefixtures("auth_user")
        def test_some_functionality():
            # Тест выполняется для авторизованного пользователя
    """
    login_page_toolshop(page).login_email(email=get_generated_file["email"])
    login_page_toolshop(page).login_password(password=get_generated_file["password"])
    login_page_toolshop(page).login_form.click_login_button()
    account_page_toolshop(page).wait_for_page_loaded()
