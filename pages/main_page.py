from pages.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    
    def click_buns_button(self):
        self.click(MainLocators.BUNS_BUTTON)
    
    def click_sauces_button(self):
        self.click(MainLocators.SAUCES_BUTTON)
    
    def click_toppings_button(self):
        self.click(MainLocators.TOPPINGS_BUTTON)
    
    def check_active_buns_button(self):
        return self.find(MainLocators.ACTIVE_BUTTON).text == 'Булки'
    
    def check_active_sauces_button(self):
        return self.find(MainLocators.ACTIVE_BUTTON).text == 'Соусы'
    
    def check_active_toppings_button(self):
        return self.find(MainLocators.ACTIVE_BUTTON).text == 'Начинки'
        