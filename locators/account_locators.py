from selenium.webdriver.common.by import By

class AccountLocators:
    EXIT_BUTTON = (By.XPATH, ".//button[contains(text(),'Выход')]")
    CONSTRUCTOR_P = (By.XPATH, ".//p[contains(text(),'Конструктор')]")
    LOGO_IMG = (By.XPATH, ".//div[contains(@class,'header__logo')]/a")