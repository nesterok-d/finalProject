from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "input[id='id_login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[id='id_login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-lg[name='login_submit']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form[id='register_form']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input[id='id_registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "input[id='id_registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "input[id='id_registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.btn-lg[name='registration_submit']")

class ProductPageLocators():
    TITLE_THE_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")

class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items div.row")
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "div[id = 'content_inner'] p")