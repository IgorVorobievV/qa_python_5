from selenium.webdriver.common.by import By

class MainLocators:
    BUNS_BUTTON = (By.XPATH, ".//span[contains(@class,'text_type_main-default') and contains(text(), 'Булки')]")
    SAUCES_BUTTON = (By.XPATH, ".//span[contains(@class,'text_type_main-default') and contains(text(), 'Соусы')]")
    TOPPINGS_BUTTON= (By.XPATH, ".//span[contains(@class,'text_type_main-default') and contains(text(), 'Начинки')]")
    H2 = (By.XPATH, ".//h2")
    BUNS_H2 = (By.XPATH, ".//h2[contains(text(), 'Булки')]")
    SAUCES_H2 = (By.XPATH, ".//h2[contains(text(), 'Соусы')]")
    TOPPINGS_H2 = (By.XPATH, ".//h2[contains(text(), 'Начинки')]")