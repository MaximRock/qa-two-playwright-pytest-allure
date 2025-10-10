import pytest

from pages.login_page_toolshop import LoginPageToolshop as login_page_toolshop
from pages.main_page_toolshop import MainPageToolshop as main_page_toolshop
from pages.registration_page_toolshop import (
    RegistrationPageToolshop as registration_page_toolshop,
)


@pytest.fixture(scope="class")
def open_main_page(page) -> None:
    main_page_toolshop(page).visit_main_page_toolshop()


@pytest.fixture(scope="class")
def open_login_page(page) -> None:
    login_page_toolshop(page).visit_login_page_toolshop()


@pytest.fixture(scope="class")
def open_registration_page(page) -> None:
    registration_page_toolshop(page).visit_register_page_toolshop()


@pytest.fixture(scope="class")
def registration_page(page, open_main_page) -> None:
    login_page_toolshop(page).navbar.visit_login_page()
