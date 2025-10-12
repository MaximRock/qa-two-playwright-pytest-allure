import pytest

from pages.login_page_toolshop import LoginPageToolshop


@pytest.mark.usefixtures("open_main_page")
@pytest.mark.user_login
class TestOpenLogin:
    """Тесты для проверки функциональности страницы авторизации."""

    def test_open_login_page(
        self,
        login_page_toolshop: LoginPageToolshop,
    ) -> None:
        """
        Тест открытия страницы авторизации.
        Steps:
        1. Перейти на страницу авторизации через навигационную панель
        2. Проверить, что заголовок страницы содержит текст 'Login'
        Args:
            login_page_toolshop: Фикстура страницы авторизации
        """
        login_page_toolshop.navbar.visit_login_page()
        login_page_toolshop.check_login_page(text="Login")
