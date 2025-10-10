import pytest  # noqa: F401

from pages.main_page_toolshop import MainPageToolshop


class TestOpenBasePage:
    def test_open_base_page(self, main_page_toolshop: MainPageToolshop) -> None:
        main_page_toolshop.visit_main_page_toolshop()
        main_page_toolshop.banner.check_banner()
