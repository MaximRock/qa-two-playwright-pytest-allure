import pytest

from config.generate_person import GeneratePerson
from config.path_manager import PathManager
from config.settings import Settings


@pytest.fixture(scope="session")
def generator() -> GeneratePerson:
    """Фикстура для создания экземпляра генератора тестовых данных."""
    return GeneratePerson()


@pytest.fixture(scope="session")
def generate_user(generator: GeneratePerson) -> dict[str, str]:
    """
    Фикстура для генерации и сохранения данных пользователя.
    Returns:
        dict: Сгенерированные данные пользователя для регистрации
    """
    data: dict[str, str] = generator.generate_registration_data()
    generator.save_to_json(data)

    return data


@pytest.fixture(scope="session")
def get_generated_file(generator: GeneratePerson) -> dict[str, str]:
    """
    Фикстура для получения данных пользователя из файла или генерации новых.
    Если файл с данными не существует, генерирует новые данные и сохраняет их.
    Returns:
        dict: Данные пользователя из файла или вновь сгенерированные
    """
    path_manager = PathManager()

    if not path_manager.exists(generator.dir_path):
        data: dict[str, str] = generator.generate_registration_data()
        generator.save_to_json(data)

    return generator.load_from_json()


@pytest.fixture
def user_credentials(get_generated_file, request) -> None:
    """
    Фикстура для установки учетных данных пользователя в тестовый класс.
    Устанавливает email и password из сгенерированных данных
    в атрибуты тестового класса.
    """
    request.cls.email = get_generated_file["email"]
    request.cls.password = get_generated_file["password"]


@pytest.fixture
def user_full_name(get_generated_file, request) -> str:
    """
    Фикстура для получения полного имени пользователя.
    Returns:
        str: Полное имя пользователя в формате 'Имя Фамилия'
    """
    full_name = (
        f" {get_generated_file['first_name']} {get_generated_file['last_name']} "
    )
    request.cls.full_name = full_name
    return full_name


@pytest.fixture
def full_name_translit(user_full_name) -> str:
    """
    Фикстура для транслитерации полного имени пользователя в латиницу.
    Returns:
        str: Транслитерированное полное имя пользователя в нижнем регистре
    """
    full_name = user_full_name.lower().strip()
    translit: str = Settings().transliterate_cyrillic_to_latin(full_name)
    return translit
