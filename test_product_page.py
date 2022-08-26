import time
import pytest

# Наследуем методы классов
from peges.basket_page import BasketPage
from peges.locators import BasePageLocators
from peges.login_page import LoginPage
from peges.product_page import ProductPage


# создаем тестовые сцениарии

#проверка корректности сообщений о добавлении в корзину
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_be_btn_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.compare_titles_of_books()

#негативный тест: гость не видит сообщения о добавлении товара после добавления
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_be_btn_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    page.compare_titles_of_books()

#гость не видит сообщения о добавлении товара на странице товара до добавления в корзину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_not_be_success_message()

#Негативный тест: сообщение о добавлении в корзину исчезает
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_be_btn_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_is_disappeared_success_message()

#группа тестов для гостя
@pytest.mark.login_guest
class TestLoginFromMainPage():

    # на странице продукта для гостя отображается кнопка для перехода на страницу логина
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    # гость может перейти на страницу логина со станицы продукта
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser,  link)                     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                            # открываем страницу
        page.go_to_login_page()                                # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)   # открываем страницу с формами логина и регистрации
        login_page.should_be_login_page()                      # выполняем проверку на отображение страницы

    # гость не видит товары в пустой корзине, показано сообщение "корзина пуста"
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                            # открываем страницу
        page.is_element_present(*BasePageLocators.BASKET_LINK) # проверяем наличие кнопки для перехода в корзину
        page.go_to_basket_page()                               # выполняем метод страницы — переходим на страницу корзины
        basket = BasketPage(browser, browser.current_url)      # открываем страницу корзины
        basket.should_be_message_in_basket()                   # выполняем проверку на поиск сообщения "корзина пуста"
        basket.should_be_no_items_in_basket()                  # выполняем проверку на отображение элементов списка на странице

#группа тестов для авторизованного пользователя
@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    #фикстура для авторизвации пользователя на каждом тесте
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                            # открываем страницу
        page.go_to_login_page()                                # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)   # открываем страницу с формами логина и регистрации
        email = str(time.time()) + "@fakemail.org"             # создаем тестовый email
        password = str(time.time())                            # создаем тестовый пароль
        login_page.register_new_user(email, password)          # вызываем функцию для регистарции пользователя

    #негативный тест: авторизавнный пользователь не видит сообщения о добавлении товара в корзину
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                            # открываем страницу
        page.should_be_btn_add_to_basket()                     # проверяем наличие кнопки для добавления товара в корзину
        page.add_product_to_basket()                           # выполняем метод страницы — добавляем товар в корзину
        page.should_not_be_success_message()                   # проверяем, что сообщение не появилось
        page.compare_titles_of_books()                         # проверяем корректность сообщения

    # авторизованный пользователь может добавить товар в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)                      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                            # открываем страницу
        page.should_be_btn_add_to_basket()                     # проверяем наличие кнопки для добавления товара в корзину
        page.add_product_to_basket()                           # выполняем метод страницы — добавляем товар в корзину
        page.should_be_success_message()                       # проверяем, что сообщение появилось
        page.compare_titles_of_books()                         # проверяем корректность сообщения
