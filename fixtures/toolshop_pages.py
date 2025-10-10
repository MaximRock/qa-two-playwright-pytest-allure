import pytest

from pages.account_page_toolshop import AccountPageToolshop
from pages.checkout_page_toolshop import CheckoutPageToolshop
from pages.login_page_toolshop import LoginPageToolshop
from pages.main_page_toolshop import MainPageToolshop
from pages.product_page_toolshop import ProductPageToolshop
from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.fixture
def main_page_toolshop(page) -> MainPageToolshop:
    return MainPageToolshop(page)


@pytest.fixture
def login_page_toolshop(page) -> LoginPageToolshop:
    return LoginPageToolshop(page)


@pytest.fixture
def registration_page_toolshop(page) -> RegistrationPageToolshop:
    return RegistrationPageToolshop(page)


@pytest.fixture
def account_page_toolshop(page) -> AccountPageToolshop:
    return AccountPageToolshop(page)


@pytest.fixture
def product_page_toolshop(page) -> ProductPageToolshop:
    return ProductPageToolshop(page)


@pytest.fixture
def checkout_page_toolshop(page) -> CheckoutPageToolshop:
    return CheckoutPageToolshop(page)
