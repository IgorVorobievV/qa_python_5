from pages.base_page import BasePage
from locators.account_locators import AccountLocators
from locators.login_locators import LoginLocators
from curl import ACCOUNT_URL, BASE_URL, LOGIN_URL


class AccountPage(BasePage):

    def open_login_page(self):
        self.open(LOGIN_URL)
    
    def login(self, useremail, password):
        self.type(LoginLocators.USEREMAIL_INPUT, useremail)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.SUBMIT_BUTTON)
        return self.find(LoginLocators.CHECK_BUTTON)
    
    def open_account_page(self):
        self.open(ACCOUNT_URL)
    
    def click_constructor_button(self):
        self.click(AccountLocators.CONSTRUCTOR_P)
        return self.current_url() == BASE_URL
    
    def click_logo(self):
        self.click(AccountLocators.LOGO_IMG)
        return self.current_url() == BASE_URL

    def logout(self):
        self.click(AccountLocators.EXIT_BUTTON)
    
    def click_account_button_without_login(self):
        self.click(LoginLocators.ACCOUNT_BUTTON)
        return self.current_url() == LOGIN_URL
