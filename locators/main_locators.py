from selenium.webdriver.common.by import By

class MainLocators:
    BUNS_BUTTON = (By.XPATH, ".//span[contains(@class,'text_type_main-default') and contains(text(), 'Булки')]/parent::div")
    SAUCES_BUTTON = (By.XPATH, ".//span[contains(@class,'text_type_main-default') and contains(text(), 'Соусы')]/parent::div")
    TOPPINGS_BUTTON = (By.XPATH, ".//span[contains(@class,'text_type_main-default') and contains(text(), 'Начинки')]/parent::div")
    ACTIVE_BUTTON = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]")