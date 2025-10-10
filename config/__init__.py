from config.expectations import Expectations
from config.path_manager import PathManager
from config.playwright import Playwright
from config.settings import Settings

playwright: Playwright = Playwright()
expectations: Expectations = Expectations()
password: str = Settings().password
# pm: PathManager = PathManager()
