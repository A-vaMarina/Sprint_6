# qa_python_Sprint_6
# Автотесты для сервиса «Яндекс.Самокат»

Проект UI-автотестов для учебного сервиса
[qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru/),
реализованный с использованием паттерна **Page Object Model**, фреймворка
**pytest** и отчётов **Allure**.

## Стек технологий

- Python 3
- Selenium WebDriver
- pytest + параметризация
- Allure (allure-pytest)
- Браузер: **Mozilla Firefox** (geckodriver)

## Структура проекта

```
Sprint_6/
├── conftest.py                  # фикстура driver, конфигурация запуска
├── data.py                      # тестовые данные (URL, наборы данных, FAQ)
├── pytest.ini                   # конфигурация pytest
├── requirements.txt             # зависимости проекта
├── locators/                    # локаторы элементов (отдельно от логики)
│   ├── main_page_locators.py
│   └── order_page_locators.py
├── pages/                       # Page Object классы
│   ├── base_page.py             # базовый класс с общими методами
│   ├── main_page.py             # главная страница
│   └── order_page.py            # страница/форма заказа
└── tests/                       # тесты, сгруппированные по функциональности
    ├── test_faq.py              # тесты аккордеона «Вопросы о важном»
    ├── test_order.py            # тесты позитивного сценария заказа
    └── test_redirects.py        # тесты переходов по логотипам
```

## Тестовые сценарии

1. **FAQ («Вопросы о важном»)** — `tests/test_faq.py`
   Для каждого из 8 вопросов отдельный параметризованный тест проверяет,
   что при клике на вопрос открывается ожидаемый текст ответа.

2. **Оформление заказа** — `tests/test_order.py`
   Проверяется весь позитивный сценарий заказа самоката:
   - клик по кнопке «Заказать» (двойная параметризация — сверху/снизу страницы);
   - заполнение формы заказа (двойная параметризация — два набора данных);
   - проверка всплывающего окна подтверждения заказа.

   Итого 4 теста (2 точки входа × 2 набора данных), сценарий заполнения
   формы при этом переиспользуется через `OrderPage.make_order(...)`,
   а не дублируется.

3. **Переходы по логотипам** — `tests/test_redirects.py`
   - клик по логотипу «Самоката» возвращает на главную страницу;
   - клик по логотипу Яндекса открывает в новой вкладке страницу Дзена
     (редирект).

## Установка

1. Установите Python 3.9+ и [Mozilla Firefox](https://www.mozilla.org/firefox/).

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск конкретного файла:

```bash
pytest tests/test_faq.py
pytest tests/test_order.py
pytest tests/test_redirects.py
```

Запуск в headless-режиме (без открытия окна браузера):

```bash
pytest --headless
```

## Формирование Allure-отчёта

1. Прогоните тесты со сбором результатов Allure:

   ```bash
   pytest --alluredir=allure_results
   ```

2. Сгенерируйте и откройте HTML-отчёт (требуется установленный
   [Allure Commandline](https://allurereport.org/docs/gettingstarted-installation/)):

   ```bash
   allure serve allure_results
   ```

Отчёт содержит группировку тестов по epic/feature/story и шаги выполнения
(`allure.step`).
