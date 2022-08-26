#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage

#наследование от MainPageLocators
from .locators import MainPageLocators

#создание класса "основная станица"
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)