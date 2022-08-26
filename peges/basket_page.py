#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "items in basket is presented, but should not be"

    def should_be_message_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_BASKET), \
            "message in basket is not presented, but should be"