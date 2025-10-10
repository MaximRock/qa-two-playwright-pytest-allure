import pytest
from transliterate import translit

from config.generate_person import GeneratePerson
from config.path_manager import PathManager


@pytest.fixture(scope="session")
def generator() -> GeneratePerson:
    return GeneratePerson()


@pytest.fixture(scope="session")
def generate_user(generator: GeneratePerson) -> dict[str, str]:
    data: dict[str, str] = generator.generate_registration_data()
    generator.save_to_json(data)

    return data


@pytest.fixture(scope="session")
def get_generated_file(generator: GeneratePerson) -> dict[str, str]:
    path_manager = PathManager()

    if not path_manager.exists(generator.dir_path):
        data: dict[str, str] = generator.generate_registration_data()
        generator.save_to_json(data)

    return generator.load_from_json()


@pytest.fixture
def user_credentials(get_generated_file, request):
    request.cls.email = get_generated_file["email"]
    request.cls.password = get_generated_file["password"]


@pytest.fixture
def user_full_name(get_generated_file, request) -> str:
    full_name = (
        f" {get_generated_file["first_name"]}"
        f" {get_generated_file["last_name"]} "
        )
    request.cls.full_name = full_name
    return full_name


@pytest.fixture
def full_name_translit(user_full_name) -> str:
    return translit(user_full_name, "ru", reversed=True).lower().strip()
