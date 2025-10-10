from playwright.sync_api import Page

from page_factory.banner import Banner


class BannerComponents:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.img_banner: Banner = Banner(
            page, locator="img[alt='Banner']", name="Banner on the main page"
        )

    def check_banner(self) -> None:
        self.img_banner.should_be_visible()
