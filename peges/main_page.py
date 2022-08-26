#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage

#создание класса "основная станица"
class MainPage(BasePage):
    # функция инициализации страницы
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)