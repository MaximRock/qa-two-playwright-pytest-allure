import logging
from pathlib import Path

from config.exception import FileNotFoundError

logger: logging.Logger = logging.getLogger(__name__)


class PathManager:
    def __init__(self, base_dir: str | Path | None = None) -> None:
        """
        Инициализация менеджера путей.
        Args:
            base_dir: Базовая директория. Если None, используется родительская
            директория файла.
        """
        if base_dir is None:
            self.base_dir: Path = Path(__file__).resolve().parent.parent
        else:
            self.base_dir = Path(base_dir).resolve()

    def get_path(self, *path_parts: str) -> Path:
        """
        Возвращает путь относительно базовой директории.
        Args:
            *path_parts: Части пути
        Returns:
            Path: Полный путь
        """
        return self.base_dir.joinpath(*path_parts)

    def exists(self, *path_parts) -> bool:
        """
        Проверяет существование пути.
        Args:
            *path_parts: Части пути
        Returns:
            bool: True если путь существует
        """
        return self.get_path(*path_parts).exists()

    def is_file(self, *path_parts: str) -> bool:
        """Проверяет, является ли путь файлом."""
        path = self.get_path(*path_parts)
        return path.is_file()

    def create_file(self, *path_parts: str, content: str = "") -> Path:
        """
        Создает файл с указанным содержимым.
        Args:
            *path_parts: Части пути к файлу
            content: Содержимое файла
        Returns:
            Path: Путь к созданному файлу
        """
        try:
            file_path = self.get_path(*path_parts)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding="utf-8")
            return file_path
        except OSError as e:
            logger.error(f"Ошибка OS при создании файла: {file_path}")
            raise FileNotFoundError() from e

    def read_file(self, *path_parts: str) -> dict:
        """
        Читает содержимое файла.
        Args:
            *path_parts: Части пути к файлу
        Returns:
            str: Содержимое файла
        """
        try:
            file_path = self.get_path(*path_parts)
            if not file_path.exists():
                raise FileNotFoundError(f"Файл не существует: {file_path}")
            if not file_path.is_file():
                raise FileNotFoundError(f"Путь не является файлом: {file_path}")
            return file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as e:
            logger.error(f"Ошибка декодирования файла: {file_path}")
            raise FileNotFoundError() from e
        except PermissionError as e:
            logger.error(f"Нет прав на чтение файла: {file_path}")
            raise FileNotFoundError() from e
