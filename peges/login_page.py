#наследование свойств базовой страницы из класса BasePage
from .base_page import BasePage

#наследование от MainPageLocators
from .locators import LoginPageLocators

# создение класса для методов страницы логина
class LoginPage(BasePage):

    # метод проверки содержимого страницы
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # метод проверки url
    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.url, "Login url did not contain login"

    # метод проверки наличия формы логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # метод проверки наличия формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "registration form is not presented"

    # метод регистрации нового пользователя
    def register_new_user(self, email, password):
        email1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email1.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2.send_keys(password)
