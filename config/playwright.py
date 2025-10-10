import os

from dotenv import load_dotenv

load_dotenv()


class Playwright:
    def __init__(self) -> None:
        self.PAGE_VIEWPORT_SIZE: dict[str, int] = {
            "width": int(os.getenv("PAGE_VIEWPORT_WIDTH", 1920)),
            "height": int(os.getenv("PAGE_VIEWPORT_HEIGHT", 1080)),
        }
        self.BROWSER: str = os.getenv("BROWSER", "chromium")
        self.IS_HEADLESS: bool = os.getenv("IS_HEADLESS", "true") == "true"
        self.SLOW_MO: int = int(os.getenv("SLOW_MO", "50"))
        self.LOCALE: str = "en-US"
