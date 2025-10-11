import allure
from playwright.sync_api import Page, Response, expect

from components.banner.banner import BannerComponents
from components.navbar.navbar import Navbar
from config.toolshop_urls import ToolshopUrls


class BasePage:
    """Базовый класс для работы со страницами веб-приложения ToolShop.

    Обеспечивает общие методы для навигации между страницами и проверки URL.
    """

    def __init__(self, page: Page) -> None:
        """Инициализация экземпляра BasePage.

        Args:
            page: Экземпляр объекта Page из Playwright для взаимодействия с браузером.
        """
        self.page: Page = page
        self.urls: ToolshopUrls = ToolshopUrls()
        self.navbar: Navbar = Navbar(page)
        self.banner: BannerComponents = BannerComponents(page)

    def visit_main_page_toolshop(self) -> Response | None:
        """Открывает главную страницу ToolShop.

        Использует allure.step для логирования действия в отчетах тестирования.

        Returns:
            Ответ сервера после перехода или None, если произошла ошибка.
        """
        with allure.step(f"Open main page ToolShop: '{self.urls['main']}'"):
            return self.page.goto(str(self.urls["main"]))
     
    def visit_login_page_toolshop(self) -> Response | None:
        """Открывает страницу входа в систему ToolShop.

        Использует allure.step для логирования действия в отчетах тестирования.

        Returns:
            Ответ сервера после перехода или None, если произошла ошибка.
        """
        with allure.step(f"open is url: '{self.urls['login']}'"):
            return self.page.goto(str(self.urls["login"]))
     
    def visit_register_page_toolshop(self) -> Response | None:
        """Открывает страницу регистрации в ToolShop.

        Использует allure.step для логирования действия в отчетах тестирования.

        Returns:
            Ответ сервера после перехода или None, если произошла ошибка.
        """
        with allure.step(f"open is url: '{self.urls['register']}'"):
            return self.page.goto(str(self.urls["register"]))

    def visit_account_page_toolshop(self) -> Response | None:
        """Открывает страницу аккаунта пользователя в ToolShop.

        Использует allure.step для логирования действия в отчетах тестирования.
        Дожидается загрузки контента страницы (domcontentloaded).

        Returns:
            Ответ сервера после перехода или None, если произошла ошибка.
        """
        with allure.step(f"open is url: '{self.urls['account']}'"):
            return self.page.goto(
                str(self.urls["account"]), wait_until="domcontentloaded"
            )

    def get_current_page(self, url) -> None:
        """Проверяет, что текущая страница соответствует указанному URL.

        Использует allure.step для логирования действия в отчетах тестирования.
        Выполняет ассерт через expect.to_have_url().

        Args:
            url: Ожидаемый URL для проверки.
        """
        with allure.step(f"Check that the current page is '{url}'"):
            expect(self.page).to_have_url(url)






