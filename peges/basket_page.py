#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage
from .locators import BasketPageLocators

# создание класса для методов страницы корзины
class BasketPage(BasePage):

    # метод проверки, что в корзине нет элементов
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "items in basket is presented, but should not be"

    # метод проверки, что в корзине есть сообщение "корзина пуста"
    def should_be_message_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_BASKET), \
            "message in basket is not presented, but should be"