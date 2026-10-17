# NASA API Tests

Учебный проект для изучения **pytest** и автоматизации тестирования REST API на Python.

## Стек

- Python
- pytest
- Requests
- python-dotenv

## Что проверяется

- **APOD (Astronomy Picture of the Day)** — астрономическая фотография дня.
- **NeoWs** — данные о сближающихся с Землей астероидах.
- **NASA Image and Video Library** — поиск изображений и метаданных.
- **NASA Exoplanet Archive** — данные об экзопланетах.

Тесты проверяют успешность запросов, структуру JSON-ответов, наличие обязательных полей и корректность типов данных.

## Установка и запуск

1. Клонировать репозиторий и перейти в папку проекта.

```bash
  git clone https://github.com/Tr-Veronika/nasa-api-pytest.git
  cd nasa-api-pytest
```

2. Создать виртуальное окружение и активировать его:

```bash
  python -m venv .venv
  .venv\Scripts\Activate.ps1
```

3. Установить зависимости из `requirements.txt`:

```bash
  pip install -r requirements.txt
```

4. Создать файл `.env` в корне проекта и добавить API-ключ NASA:

```text
NASA_API_KEY=your_api_key
```

5. Запустить тесты:

```bash
pytest -v
```

## Цель проекта

Практика работы с pytest, фикстурами, HTTP-запросами и проверкой ответов REST API.
