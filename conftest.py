import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language: es or ru")  #настройка пользовательского параметра запуска тестов

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")                                # считывание значения параметра из командной строки
    options = webdriver.ChromeOptions()                                                 # создание объекта для запуска браузера с параметром
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # заполнение этого параметра значением из командной строки
    browser = webdriver.Chrome(options=options)                                         # запуск зрайвера с параметром
    yield browser                                                                       # описание действий, которве выполнятся после завершения теста
    print("\nquit browser..")
    browser.quit()                                                                      # закрытие браузера
