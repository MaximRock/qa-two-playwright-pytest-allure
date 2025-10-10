import allure
from playwright.sync_api import Page, Response, expect

from components.banner.banner import BannerComponents
from components.navbar.navbar import Navbar
from config.toolshop_urls import ToolshopUrls


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.urls: ToolshopUrls = ToolshopUrls()
        self.navbar: Navbar = Navbar(page)
        self.banner: BannerComponents = BannerComponents(page)

    def visit_main_page_toolshop(self) -> Response | None:
        with allure.step(f"Open main page ToolShop: '{self.urls['main']}'"):
            return self.page.goto(str(self.urls["main"]))

    def visit_login_page_toolshop(self) -> Response | None:
        with allure.step(f"open is url: '{self.urls["login"]}'"):
            return self.page.goto(str(self.urls["login"]))

    def visit_register_page_toolshop(self) -> Response | None:
        with allure.step(f"open is url: '{self.urls["register"]}'"):
            return self.page.goto(str(self.urls["register"]))

    def visit_account_page_toolshop(self) -> Response | None:
        with allure.step(f"open is url: '{self.urls["account"]}'"):
            return self.page.goto(
                str(self.urls["account"]), wait_until="domcontentloaded")

    def get_current_page(self, url) -> None:
        with allure.step(
            f"Check that the current page is '{url}'"):
            expect(self.page).to_have_url(url)
