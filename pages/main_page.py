from pages.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    
    def click_buns_button(self):
        self.click(MainLocators.BUNS_BUTTON)
        return self.find(MainLocators.BUNS_H2).text
    
    def click_sauces_button(self):
        self.click(MainLocators.SAUCES_BUTTON)
        return self.find(MainLocators.SAUCES_H2).text
    
    def click_toppings_button(self):
        self.click(MainLocators.TOPPINGS_BUTTON)
        return self.find(MainLocators.TOPPINGS_H2).text