# avito-qa-trainee-spring-2026
Тестовое задание на позицию стажера QA (Весна 2026). Скриншот с багами + Автотесты API на Python

# Тестирование API объявлений (Avito QA Trainee)
Данный репозиторий содержит решение задания 2.1 (API тесты) для отбора на позицию стажера QA-инженера. В проекте реализован полноценный фреймворк для автоматизации API-тестов на Python

## Стек технологий
* **Язык:** Python 3.10+
* **Фреймворк:** `pytest`
* **Библиотеки:** `requests` (API), `allure-pytest` (отчеты), `flake8/black` (качество кода)
* **Паттерн:** API Client Pattern (Service Object Layer)
* **Логирование:** Logging + Helpers

---

## Структура проекта
* `helpers/assertions.py` - Кастомные проверки с логированием и Allure
* `helpers/utils.py` - Парсинг ID
* `tests/` — директория с автоматизированными тестами
* `api_client.py` — клиент для взаимодействия с API 
* `conftest.py` — конфигурация pytest, общие фикстуры и настройки логирования
* `TESTCASES.md` — подробное описание тест-кейсов и стратегии тестирования
* `BUGS.md` — отчет о найденных дефектах в процессе автоматизации
* `requirements.txt` — список зависимостей проекта

---

## Запуск проекта

### Подготовка окружения
Клонируйте репозиторий и создайте виртуальное окружение:
```bash
git clone <https://github.com/kllrqnn/avito-qa-trainee-spring-2026.git>
cd avito-qa-trainee-spring-2026
python3 -m venv venv
source venv/bin/activate #для Linux/Mac 
source venv\Scripts\activate # для Windows
```
### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Запуск тестов
```bash
pytest # для обычного запуска
pytest --alluredir=allure-results # для запуска с генерацией данных для Allure-отчета
```
### Запуск Allure
```bash
allure serve allure-results
```


