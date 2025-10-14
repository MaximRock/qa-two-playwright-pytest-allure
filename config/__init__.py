from config.expectations import Expectations
from config.playwright import Playwright
from config.settings import Settings

# Конфигурация настроек Playwright для управления браузером
playwright: Playwright = Playwright()

# Конфигурация ожиданий для управления таймаутами и условиями
expectations: Expectations = Expectations()

# Пароль из настроек приложения
password: str = Settings().password
