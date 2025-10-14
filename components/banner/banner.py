from playwright.sync_api import Page

from page_factory.banner import Banner


class BannerComponents:
    """Компонент баннера для главной страницы приложения."""

    def __init__(self, page: Page) -> None:
        """
        Инициализация компонентов баннера.
        Args:
            page: Экземпляр страницы Playwright для взаимодействия с браузером
        """
        self.page: Page = page
        self.img_banner: Banner = Banner(
            page, locator="img[alt='Banner']", name="Banner on the main page"
        )

    def check_banner(self) -> None:
        """Проверить видимость баннера на главной странице.
        Метод проверяет, что баннер отображается на странице.
        Используется для подтверждения загрузки главной страницы.
        Raises:
            ElementNotVisibleError: Если баннер не видим на странице
        """
        self.img_banner.should_be_visible()
