class Expectations:
    """Класс для управления настройками ожиданий в тестах."""

    def __init__(self) -> None:
        """
        Инициализация настроек ожиданий.

        Attributes:
            DEFAULT_TIMEOUT: Время ожидания по умолчанию в миллисекундах
        """
        self.DEFAULT_TIMEOUT = 60 * 1000
