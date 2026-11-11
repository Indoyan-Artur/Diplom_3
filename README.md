**Автотесты Stellar Burgers**

Автотесты веб-приложения «Stellar Burgers» (учебный стенд) на Python + Selenium + pytest.
Покрыты разделы: восстановление пароля, личный кабинет, основной функционал
(конструктор, оформление заказа), лента заказов.

**Тесты выполняются в Firefox и Chrome.**

**Стек**

- Python 3.11, Selenium, pytest
- Firefox и Chrome (параметризация)
- Allure-отчёт, pytest-cov (покрытие)
- Page Object Model, локаторы — отдельным пакетом
- Регистрация/создание тестовых данных — через API (requests)

**Структура проекта**
─ conftest.py # фикстуры (браузеры, пользователь через API, авторизация)
─ config.py # URLs стенда
─ test_data.py # тестовые данные
─ locators/ # локаторы страниц (по классу на страницу)
─ page_objects/ # Page Objects (по классу на страницу)
─ tests/ # тесты, разделённые по тематике (классы)

**Установка**
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

**Запуск**
*все тесты*
pytest tests -v

*отдельный раздел*
pytest tests/test_order_feed.py -v



