#наследуем методы из классов
from peges.basket_page import BasketPage
from peges.locators import BasePageLocators
from peges.login_page import LoginPage
from peges.main_page import MainPage

#создаем тестовые сцениарии

#поиск ссылки на страницу логина
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                            # открываем страницу
    page.should_be_login_link()                            # выполняем метод страницы — проверяем наличие ссылки на страницу логина

#переход на страницу логина
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                             # открываем страницу
    page.go_to_login_page()                                 # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)    # открываем страницу с формами логина и регистрации
    login_page.should_be_login_page()                       # выполняем проверку на отображение страницы

#проверка что пользователь не видит товары в корзине
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                             # открываем страницу
    page.is_element_present(*BasePageLocators.BASKET_LINK)  # проверяем отображение кнопки перехода в корзину
    page.go_to_basket_page()                                # выполняем метод страницы — переходим на страницу корзины
    basket = BasketPage(browser, browser.current_url)       # открываем страницу корзины
    basket.should_be_message_in_basket()                    # выполняем проверку на отображение сообщения "корзина пуста"
    basket.should_be_no_items_in_basket()                   # выполняем проверку на отсутствие элементов в корзине
