import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.password: str = str(os.getenv("PASSWORD"))
