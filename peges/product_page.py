import math
# наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage

# наследование от ProductPageLocators
from .locators import ProductPageLocators


# создание класса "основная станица"
class ProductPage(BasePage):

    # метод для нахождения кнопки добавления товара в корзину
    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "btn_add_to_basket is not presented"

    # метод для добавления товара в корзину
    def add_product_to_basket(self):
        btn_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        btn_to_basket.click()

    # метод поиска сообщения об успешном добавлении в корзину
    def should_be_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "сообщение о добавлении товара в корзину не получено"

    def take_title_the_book(self):
        title_the_book = self.browser.find_element(*ProductPageLocators.TITLE_THE_BOOK)
        return title_the_book.text

    def take_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        return success_message.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"