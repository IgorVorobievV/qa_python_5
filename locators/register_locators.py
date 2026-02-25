from selenium.webdriver.common.by import By

class RegisterLocators:
    USERNAME_INPUT = (By.XPATH, ".//label[contains(text(),'Имя')]/parent::div/input")
    USEREMAIL_INPUT = (By.XPATH, ".//label[contains(text(),'Email')]/parent::div/input")
    PASSWORD_INPUT = (By.XPATH, ".//label[contains(text(),'Пароль')]/parent::div/input")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    FLASH_MESSAGE_ACCOUNT_EXISTS = (By.XPATH, "//p[contains(text(),'Такой пользователь уже существует')]")
    FLASH_MESSAGE_INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    