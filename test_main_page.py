#наследуем методы из класса MainPage
from final_project.pages.basket_page import BasketPage
from final_project.pages.locators import BasePageLocators
from final_project.pages.main_page import MainPage

from pages.login_page import LoginPage

#создаем тестовые сцениарии

#поиск ссылки на страницу логина
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#переход на страницу логина
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                            # открываем страницу
    page.go_to_login_page()                                # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)   # открываем страницу с формами логина и регистрации
    login_page.should_be_login_page()                      # выполняем проверку на отображение страницы

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.is_element_present(*BasePageLocators.BASKET_LINK)
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_message_in_basket()
    basket.should_be_no_items_in_basket()
