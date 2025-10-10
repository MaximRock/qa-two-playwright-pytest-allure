from dotenv import load_dotenv

load_dotenv()


pytest_plugins: list[str] = [
    "fixtures.page",
    "fixtures.toolshop_pages",
    "fixtures.logger",
    "fixtures.open_page",
    "fixtures.auth_user",
    "fixtures.generated_users",
]
