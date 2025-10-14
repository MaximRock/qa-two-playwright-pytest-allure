import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Класс для работы с настройками приложения и утилитами."""

    def __init__(self) -> None:
        """Инициализация настроек и словаря для транслитерации."""
        self.password: str = str(os.getenv("PASSWORD"))
        self.translit_dict: dict[str, str] = {
            "а": "a",
            "б": "b",
            "в": "v",
            "г": "g",
            "д": "d",
            "е": "e",
            "ё": "yo",
            "ж": "zh",
            "з": "z",
            "и": "i",
            "й": "y",
            "к": "k",
            "л": "l",
            "м": "m",
            "н": "n",
            "о": "o",
            "п": "p",
            "р": "r",
            "с": "s",
            "т": "t",
            "у": "u",
            "ф": "f",
            "х": "kh",
            "ц": "ts",
            "ч": "ch",
            "ш": "sh",
            "щ": "shch",
            "ъ": "",
            "ы": "y",
            "ь": "",
            "э": "e",
            "ю": "yu",
            "я": "ya",
            "А": "A",
            "Б": "B",
            "В": "V",
            "Г": "G",
            "Д": "D",
            "Е": "E",
            "Ё": "Yo",
            "Ж": "Zh",
            "З": "Z",
            "И": "I",
            "Й": "Y",
            "К": "K",
            "Л": "L",
            "М": "M",
            "Н": "N",
            "О": "O",
            "П": "P",
            "Р": "R",
            "С": "S",
            "Т": "T",
            "У": "U",
            "Ф": "F",
            "Х": "Kh",
            "Ц": "Ts",
            "Ч": "Ch",
            "Ш": "Sh",
            "Щ": "Shch",
            "Ъ": "",
            "Ы": "Y",
            "Ь": "",
            "Э": "E",
            "Ю": "Yu",
            "Я": "Ya",
        }

    def transliterate_cyrillic_to_latin(self, text) -> str:
        """
        Транслитерирует текст из кириллицы в латиницу.
        Args:
            text: Исходный текст на кириллице для транслитерации
        Returns:
            str: Транслитерированный текст на латинице
        """
        result: str = ""

        for char in text:
            if char in self.translit_dict:
                result += self.translit_dict[char]
            else:
                result += char

        return result
