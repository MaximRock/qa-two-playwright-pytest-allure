import pytest

from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.mark.user_registration
@pytest.mark.usefixtures("registration_page")
class TestOpenRegistrationPage:
    """Тесты для проверки открытия страницы регистрации."""

    def test_open_registration_page(
        self,
        registration_page_toolshop: RegistrationPageToolshop,
    ) -> None:
        """
        Тест открытия страницы регистрации.

        Steps:
        1. Открыть страницу регистрации через клик по ссылке
        2. Проверить, что заголовок страницы содержит текст 'Customer registration'

        Args:
            registration_page_toolshop: Фикстура страницы регистрации
        """
        registration_page_toolshop.open_registration_page_toolship()
        registration_page_toolshop.check_registration_page(text="Customer registration")
