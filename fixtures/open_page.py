import pytest

from pages.login_page_toolshop import LoginPageToolshop as login_page_toolshop
from pages.main_page_toolshop import MainPageToolshop as main_page_toolshop
from pages.registration_page_toolshop import (
    RegistrationPageToolshop as registration_page_toolshop,
)


@pytest.fixture(scope="class")
def open_main_page(page) -> None:
    """
    Фикстура для открытия главной страницы приложения.
    Args:
        page: Фикстура страницы Playwright
    """
    main_page_toolshop(page).visit_main_page_toolshop()


@pytest.fixture(scope="class")
def open_login_page(page) -> None:
    """
    Фикстура для открытия страницы авторизации.
    Args:
        page: Фикстура страницы Playwright
    """
    login_page_toolshop(page).visit_login_page_toolshop()


@pytest.fixture(scope="class")
def open_registration_page(page) -> None:
    """
    Фикстура для открытия страницы регистрации.
    Args:
        page: Фикстура страницы Playwright
    """
    registration_page_toolshop(page).visit_register_page_toolshop()


@pytest.fixture(scope="class")
def registration_page(page, open_main_page) -> None:
    """
    Фикстура для подготовки к тестам регистрации.
    Открывает главную страницу и переходит на страницу авторизации,
    откуда можно перейти к регистрации.
    Args:
        page: Фикстура страницы Playwright
        open_main_page: Фикстура открытия главной страницы
    """
    login_page_toolshop(page).navbar.visit_login_page()
