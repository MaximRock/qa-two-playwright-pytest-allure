import logging
from pathlib import Path

from config.path_manager import PathManager


def setup_logging():
    # Настройка формата логов
    # log_format = "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s" #noqa
    log_format = "%(asctime)s | [%(levelname)s] %(name)s: %(message)s"
    formatter = logging.Formatter(log_format)

    # Создание директории для логов
    path_manager: PathManager = PathManager()
    log_file: Path = path_manager.base_dir / "logs" / "logs.log"

    # Файловый обработчик (пишет в файл)
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.ERROR)

    # Консольный обработчик (выводит в терминал)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.ERROR)

    # Настройка корневого логгера
    root_logger: logging.Logger = logging.getLogger()
    root_logger.setLevel(logging.ERROR)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # Настройка логгера для Playwright (уменьшаем уровень шума)
    playwright_logger: logging.Logger = logging.getLogger("playwright")
    playwright_logger.setLevel(logging.ERROR)

    return root_logger


setup_logging()
