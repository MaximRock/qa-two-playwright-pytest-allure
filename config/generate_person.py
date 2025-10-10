import json
import logging
import random
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
        birth_year: int = random.randint(1980, 2000)  # noqa: S311
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
            number[i:i + group_size] for i in range(0, len(number), group_size)
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


#   regisration_generate_person: RegisrationGeneratePerson = RegisrationGeneratePerson()
#   ter = regisration_generate_person.seve_to_json()
#    print(ter)


# class GeneratePerson:
#     def __init__(
#         self,
#         persons: int = 1,
#         person_index: int = 0,
#         locale: str = "ru_RU",
#         file_name: str = "person_data.json",
#         dir_name: str = "data",
#     ) -> None:
#         self.path_manager: PathManager = PathManager()
#         self.faker: Faker = Faker(locale)
#         self.num_records: int = persons
#         self.person_index: int = person_index
#         self._data: list[str] = None
#         self.dir_name: str = dir_name
#         self.file_name: str = file_name
#         self.dir_path: str = self.path_manager.create_dir(self.dir_name)
#         self.file_path: str = f"{self.dir_name}/{self.file_name}"


#     def date_of_birth(self) -> str:
#         birth_year: int = random.randint(1980, 2000)  # noqa: S311
#         birth_date: str = self.faker.date_of_birth()
#         birth_date: str = birth_date.replace(year=birth_year)
#         return str(birth_date)

#     def generate_data(self) -> list[str]:
#         data: list = []
#         for _ in range(self.num_records):
#             record: list = [
#                 self.faker.first_name_male(),
#                 self.faker.last_name_male(),
#                 str(self.date_of_birth()),
#                 self.faker.street_name(),
#                 str(self.faker.postcode()),
#                 self.faker.city(),
#                 self.faker.region(),
#                 str(self.faker.msisdn()),
#                 self.faker.email(),
#             ]
#             data.append(record)
#         self._data = data
#         return data

#     def save_to_json(self) -> None:
#         if self._data is None:
#             self.generate_data()

#         with open(self.file_path, "w", encoding="utf-8") as file:
#             json.dump(self._data, file, ensure_ascii=False, indent=2)

#     def load_from_json(self, person_index) -> list[str]:
#         try:
#             with open(self.file_path, encoding="utf-8") as file:
#                 if person_index > self.num_records:
#                     raise IndexError(f"list index out of range {self.num_records}")
#                 else:
#                     test_data: list[str] = json.load(file)
#                 return test_data[self.person_index]
#         except FileNotFoundError as f:
#             raise ValueError(f"Not found file {self.file_path}") from f

#     def get_email(self, person_index) -> str:
#         person_index: int = self.person_index
#         with open(self.file_path, encoding="utf-8") as file:
#             test_data = json.load(file)

#             email = test_data[person_index][8]
#         return email

#     def __repr__(self) -> str:
#         return f"""GeneratePerson(
#                     {self.num_records},
#                     {self.faker.locales[0]},
#                     {self.file_name},
#                     {self.dir_name})"""

#     def __len__(self) -> int:
#         if self._data is None:
#             self.generate_data()
#         return len(self._data)

#     def __getitem__(self, person_index) -> list[str]:
#         if self._data is None:
#             self.generate_data()
#         if isinstance(person_index, int):
#             if person_index > self.num_records:
#                 raise IndexError(f"list index out of range {self.num_records}")
#             else:
#                 return self._data[person_index]
#         else:
#             raise TypeError(
#                 f"index must be integer, not {type(person_index).__name__}"
#             ) from TypeError()

#     def __iter__(self) -> Iterator[str]:
#         if self._data is None:
#             self.generate_data()
#         return iter(self._data)

#     def __contains__(self, item: list[str]) -> bool:
#         if self._data is None:
#             self.generate_data()
#         return item in self._data

#     def __enter__(self):
#         if self._data is None:
#             self.generate_data()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self._data is None:
#             self.save_to_json()
#         if exc_type:
#             logger.error(f"Error: {exc_val}")
