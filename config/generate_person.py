import json
import logging
import secrets
from pathlib import Path

from dotenv import load_dotenv
from faker import Faker

from config.path_manager import PathManager
from config.settings import Settings

load_dotenv()
logger: logging.Logger = logging.getLogger(__name__)


class GeneratePerson:
    def __init__(self, locale: str = "ru_RU") -> None:
        self.faker: Faker = Faker(locale)
        self.path_manager: PathManager = PathManager()
        self.settings: Settings = Settings()
        self._data = None
        self.file_name: str = "person_data.json"
        self.dir_name: str = "data"
        self.dir_path: str = f"{self.dir_name}/{self.file_name}"

    def date_of_birth(self) -> str:
        """Генерация даты рождения"""
        birth_year: int = 1980 + secrets.randbelow(2000 - 1980 + 1)
        birth_date: str = self.faker.date_of_birth()
        birth_date: str = birth_date.replace(year=birth_year)
        return str(birth_date)

    def credit_card_expire(self) -> str:
        expire_date: str = self.faker.credit_card_expire()
        month, year = expire_date.split("/")
        return f"{month}/20{year}"

    def card_number(self, delimiter: str = "-", group_size: int = 4) -> str:
        number: str = self.faker.credit_card_number()
        parts: list[str] = [
            number[i : i + group_size] for i in range(0, len(number), group_size)
        ]
        return delimiter.join(parts)

    def generate_registration_data(self, exclude_field=None) -> dict[str, str]:
        """Генерация данных для регистрации с возможностью исключения полей"""
        data: dict[str, str] = {
            "first_name": self.faker.first_name_male(),
            "last_name": self.faker.last_name_male(),
            "date_of_birth": self.date_of_birth(),
            "street_name": self.faker.street_name(),
            "postcode": str(self.faker.postcode()),
            "city": self.faker.city(),
            "region": self.faker.region(),
            "country": self.faker.current_country_code(),
            "phone": self.faker.msisdn(),
            "email": self.faker.email(),
            "password": self.settings.password,
            "cart_number": self.card_number(),
            "expiration_date": self.credit_card_expire(),
            "cvv": self.faker.credit_card_security_code(),
        }

        if exclude_field:
            data[exclude_field] = ""

        self._data: dict[str, str] = data

        return data

    def save_to_json(self, json_data) -> Path:
        if self._data is None:
            self.generate_registration_data()
        json_data: str = json.dumps(self._data, ensure_ascii=False, indent=2)
        json_file: Path = self.path_manager.create_file(
            f"{self.dir_name}/{self.file_name}",
            content=json_data,
        )
        return json_file

    def load_from_json(self) -> dict:
        json_file: str = self.path_manager.read_file(
            self.dir_path,
        )
        return json.loads(json_file)
