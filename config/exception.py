class TestBaseExceptionError(Exception):
    """Базовое исключение для тестовой среды."""

    default_message: str = "Test Error"

    def __init__(self, message: str | None = None, *args, **kwargs) -> None:
        self.message: str = message or self.default_message
        super().__init__(self.message, *args, **kwargs)

    def __str__(self) -> str:
        return self.message


class LocatorNotStringError(TestBaseExceptionError):
    """Исключение, возникающее когда передан не строка в качестве локатора."""

    default_message: str = "Локатор должен быть строкой"


class ElementNotVisibleError(TestBaseExceptionError):
    """Исключение, возникающее когда элемент не виден на странице."""

    default_message: str = "Элемент не виден на странице"


class ElementNotFoundError(TestBaseExceptionError):
    """Исключение, возникающее когда элемент не найден на странице."""

    default_message: str = "Элемент не найден на странице"


class ElementTimeoutError(TestBaseExceptionError):
    """Исключение, возникающее когда выходит время ожидания элемента."""

    default_message: str = "Время ожидания элемента истекло"


class FileNotFoundError(TestBaseExceptionError):
    """Исключение, возникающее когда не найден файл."""

    default_message: str = "Не найден файл"
