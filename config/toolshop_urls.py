class ToolshopUrls:
    """Класс для управления URL-адресами приложения Toolshop."""

    def __init__(self) -> None:
        """
        Инициализация словаря URL-адресов приложения.
        Attributes:
            _urls: Словарь с URL-адресами различных страниц приложения
        """
        self._urls: dict[str, str] = {
            "main": "https://practicesoftwaretesting.com/",
            "login": "https://practicesoftwaretesting.com/auth/login",
            "register": "https://practicesoftwaretesting.com/auth/register",
            "account": "https://practicesoftwaretesting.com/account",
            "checkout": "https://practicesoftwaretesting.com/checkout",
        }

    def __getitem__(self, key: str) -> str:
        """Получить URL по ключу.
        Args:
            key: Ключ для получения URL из словаря
        Returns:
            str: URL-адрес соответствующей страницы
        Raises:
            KeyError: Если указанный ключ не найден в словаре URL-адресов
        """
        try:
            if isinstance(key, str):
                return self._urls[key]
        except KeyError as e:
            raise KeyError(f"Указанный ключ '{key}' не найден в словаре.") from e
