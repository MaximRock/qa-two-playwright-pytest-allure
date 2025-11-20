# Playwrigth, Pytest

Учебный проект тестовой платформы [Practice Software Testing - Toolshop][1]


## Проверяемые функции

- Открытие страницы регистрации
- Успешная регистрация пользователя
  - Негативный тест - проверка на пустое поле

- Открытие страницы авторизации
  - Успешная авторизация пользователя

- Проверка полного цикла покуки после авторизации пользователя

## Настройка тестов

- Создадаем директорию _test_ :

```bash
cd ~ && mkdir ~/test && cd ~/test
```

- Клонируем репозиторий:

``` bash
git clone https://github.com/MaximRock/qa-two-playwright-pytest-allure.git
```

```bash
cd qa-two-playwright-pytest-allure
```

Для установки пакетов в проекте используется утилита _uv_.

- Устаноавим, если установленна пропустите этот шаг:
  > Если Вы не использовали _uv_ рекомендую ознакомится с документацией на сайте [uv][2]

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# With pip.
pip install uv
```

- для Ubuntu можно воспользоваться _snap_:

```bash
sudo snap install astral-uv --classic
```

- для Arch-Linux:

```bash
sudo pacman -S uv
```

- Устанавливаем необходимые пакеты:

```bash
uv sync
```

- Активируем виртуальное окружение:

```bash
source .venv/bin/activate
```

- Установим playwright:

```bash
playwright install
```

- Запустите скрипт _user_manager.sh_ который создает директорию _logs_, переименует файл _.env.example_ в _.env_ и попросит Вас ввести пароль:

```bash
chmod +x user_manager.sh && ./user_manager.sh
```

> **ВАЖНО**<br>
> Ознакомтесь с файлом _.env_ и при необходимости исмените переменные.

## Запуск тестов

- В _pytest_, пример:

```bash
pytest -vs tests/registration_user/test_registration_user.py
```

- С использованием _allure_, пример:

```bash
# результаты тестов будут находится в allure-results
pytest -vs --alluredir=allure-results tests/registration_user/test_registration_user.py

# генерация отчета в docs
allure generate allure-results -o docs --clean

# просмотр отчета
allure open docs

# или если не надо сохранять отчет
pytest -vs --alluredir=allure-results tests/registration_user/test_registration_user.py && allure serve allure-results
```



<!-- allowed_elements = (["details", "summary", "br"]) -->
<details>
<summary>Структура проекта:</summary>

В каждом файле проекта имеется довольно подробный _docstring_.

- В директории _components_ находятся объекты или компоненты страницы.
 Например: форма регистрации или логирования, баннер на главной странице.

&nbsp;&nbsp;&nbsp;&nbsp;./components<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── banner<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; └── banner.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── login_form<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; └── login_form.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── navbar<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; └── navbar.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── registration_form<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; └── registration_form.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── search_form<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; └── search_form.py

- в _config_ файлы конфигурции для проекта;
- в _data_ с генирированный _json_ файл для тестовых данных;
- в _docs_ документация allure отчета;
- в _fixtures_ фикстуры для тестов;
- в _logs_ error логи;
- в _page_factory_ элементы взаимодействия на странице (button, link, input);
- в _pages_ страницы сайта;
- в _tests_ сами тесты:

&nbsp;&nbsp;&nbsp;&nbsp;./tests<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── login_user<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; ├── test_1_open_login_page.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; └── test_2_login_user.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── main_page<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; ├── test_complete_purchase_flow_after_login.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp; └── test_open_base_page.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── registration_user<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ├── test_empty_field_validation.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ├── test_open_registration_page.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; └── test_registration_user.py

</details>

[1]: https://practicesoftwaretesting.com/
[2]: https://docs.astral.sh/uv/getting-started/installation/
