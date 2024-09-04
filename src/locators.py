from selenium.webdriver.common.by import By


class Locators:
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[href='/account']") # кнопка "личный кабинет"
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[href='/register']") # кнопка "Зарегистрироваться"
    NAME_FIELD = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input") # поле ввода "имя"
    EMAIL_FIELD = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input") # поле ввода "email"
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']") # поле ввода "Пароль"
    REGISTER_FINAL_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]") # Кнопка "Зарегистрироваться"
    MESSAGE_INCORRECT_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный "
                                            "пароль']") # Сообщение о неккоретном пароле
    INPUT_MAIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]") # Кнопка "Войти"
    INPUT_REGISTER_BUTTON = (By.CSS_SELECTOR, "[href='/login']") # Кнопка "Войти" на странице восстановления пароля
    PASSWORD_RECOVERY_BUTTON = (By.CSS_SELECTOR, "[href='/forgot-password']") # Кнопка "Восстановить пароль"
    SECTIONS = (By.CSS_SELECTOR, "[class='Account_nav__Lgali']") # Разделы личного кабинте(Профиль, История закзазов, Выход)
    CONSRUKTOR_BUTTON = (By.CSS_SELECTOR, "[class='AppHeader_header__link__3D_hX']") # Кнопка конструктора
    LOGOTIP_BUTTON = (By.CSS_SELECTOR, "[class='AppHeader_header__logo__2D0X2']") # Логотип программы
    SOBERITE_BURGER = (By.CSS_SELECTOR, "[class='text text_type_main-large mb-5 mt-10']") # Надпись "Соберите бургер"
    EXIT_BUTTON = (By.CSS_SELECTOR, "[class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']") # Кнопка "Выход"
    BULKI_SECTION = (By.XPATH, "//span[text()='Булки']/parent::*") # Раздел "Булки"
    SOUS_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::*") # Раздел "Соусы"
    NACHINKI_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::*") # Раздел "Начинки"


