

class ToolshopUrls:
    def __init__(self) -> None:
        self._urls: dict[str, str] = {
            "main": "https://practicesoftwaretesting.com/",
            "login": "https://practicesoftwaretesting.com/auth/login",
            "register": "https://practicesoftwaretesting.com/auth/register",
            "account": "https://practicesoftwaretesting.com/account",
            "checkout": "https://practicesoftwaretesting.com/checkout",
        }

    def __getitem__(self, key: str) -> str:
        try:
            if isinstance(key, str):
                return self._urls[key]
        except KeyError as e:
            raise KeyError(f"Указанный ключ '{key}' не найден в словаре.") from e
