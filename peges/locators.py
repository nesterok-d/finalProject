from selenium.webdriver.common.by import By

# класс для локаторов общих для ввсех страниц
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")                                        # локатор кнопки перехода на страницу логина
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")                                    # локатор кнопки добавления в корзины
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")                                          # локатор иконки пользователя

# класс для локаторов страницы логина
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id='login_form']")                              # локатор формы логина
    LOGIN_USERNAME = (By.CSS_SELECTOR, "input[id='id_login-username']")                  # локатор поля имя пользователя
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[id='id_login-password']")                  # локатор поля пароля
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-lg[name='login_submit']")               # локатор кнопки входа
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form[id='register_form']")                    # локатор формы регистарции
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input[id='id_registration-email']")          # локатор поля email
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "input[id='id_registration-password1']")  # локатор поля пароля1
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "input[id='id_registration-password2']")  # локатор поля пароля2
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.btn-lg[name='registration_submit']") # локатор кнопки регистарции

# класс для локаторов страницы продукта
class ProductPageLocators():
    TITLE_THE_BOOK = (By.CSS_SELECTOR, "div.product_main h1")                            # локатор названия книги
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")                 # локатор кнопки добавления в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")                         # локатор сообщения об успешном добавлении в корзину

# класс для локаторов страницы корзины
class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items div.row")                      # локатор элемента в корзине
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "div[id = 'content_inner'] p")                 # локатор сообщения "корзина пуста"