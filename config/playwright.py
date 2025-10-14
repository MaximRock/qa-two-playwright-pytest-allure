import os

from dotenv import load_dotenv

load_dotenv()


class Playwright:
    """Класс для управления настройками Playwright."""

    def __init__(self) -> None:
        """
        Инициализация настроек Playwright из переменных окружения.
        Attributes:
            PAGE_VIEWPORT_SIZE: Размер viewport страницы
            BROWSER: Тип браузера для тестов
            IS_HEADLESS: Режим headless браузера
            SLOW_MO: Замедление выполнения операций (в миллисекундах)
            LOCALE: Локаль браузера
        """
        self.PAGE_VIEWPORT_SIZE: dict[str, int] = {
            "width": int(os.getenv("PAGE_VIEWPORT_WIDTH", 1920)),
            "height": int(os.getenv("PAGE_VIEWPORT_HEIGHT", 1080)),
        }
        self.BROWSER: str = os.getenv("BROWSER", "chromium")
        self.IS_HEADLESS: bool = os.getenv("IS_HEADLESS", "true") == "true"
        self.SLOW_MO: int = int(os.getenv("SLOW_MO", "50"))
        self.LOCALE: str = "en-US"
