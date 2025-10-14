import pytest

from pages.account_page_toolshop import AccountPageToolshop
from pages.checkout_page_toolshop import CheckoutPageToolshop
from pages.login_page_toolshop import LoginPageToolshop
from pages.main_page_toolshop import MainPageToolshop
from pages.product_page_toolshop import ProductPageToolshop
from pages.registration_page_toolshop import RegistrationPageToolshop


@pytest.fixture
def main_page_toolshop(page) -> MainPageToolshop:
    """
    Фикстура для создания экземпляра главной страницы.
    Args:
        page: Фикстура страницы Playwright
    Returns:
        MainPageToolshop: Экземпляр Page Object главной страницы
    """
    return MainPageToolshop(page)


@pytest.fixture
def login_page_toolshop(page) -> LoginPageToolshop:
    """
    Фикстура для создания экземпляра страницы авторизации.
    Args:
        page: Фикстура страницы Playwright
    Returns:
        LoginPageToolshop: Экземпляр Page Object страницы авторизации
    """
    return LoginPageToolshop(page)


@pytest.fixture
def registration_page_toolshop(page) -> RegistrationPageToolshop:
    """
    Фикстура для создания экземпляра страницы регистрации.
    Args:
        page: Фикстура страницы Playwright
    Returns:
        RegistrationPageToolshop: Экземпляр Page Object страницы регистрации
    """
    return RegistrationPageToolshop(page)


@pytest.fixture
def account_page_toolshop(page) -> AccountPageToolshop:
    """
    Фикстура для создания экземпляра страницы аккаунта.
    Args:
        page: Фикстура страницы Playwright
    Returns:
        AccountPageToolshop: Экземпляр Page Object страницы аккаунта
    """
    return AccountPageToolshop(page)


@pytest.fixture
def product_page_toolshop(page) -> ProductPageToolshop:
    """
    Фикстура для создания экземпляра страницы товара.
    Args:
        page: Фикстура страницы Playwright
    Returns:
        ProductPageToolshop: Экземпляр Page Object страницы товара
    """
    return ProductPageToolshop(page)


@pytest.fixture
def checkout_page_toolshop(page) -> CheckoutPageToolshop:
    """
    Фикстура для создания экземпляра страницы оформления заказа.
    Args:
        page: Фикстура страницы Playwright
    Returns:
        CheckoutPageToolshop: Экземпляр Page Object страницы оформления заказа
    """
    return CheckoutPageToolshop(page)
