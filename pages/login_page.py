from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from curl import LOGIN_URL, ACCOUNT_URL


class LoginPage(BasePage):
    
    def open_login_page(self):
        self.open(LOGIN_URL)
    
    def login(self, useremail, password):
        self.type(LoginLocators.USEREMAIL_INPUT, useremail)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.SUBMIT_BUTTON)

    def find_check_button(self):
        self.find(LoginLocators.CHECK_BUTTON)

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def click_account_button(self):
        self.click(LoginLocators.ACCOUNT_BUTTON)
    
    def check_login_page(self):
        return self.check_page(LOGIN_URL)

    def check_account_page(self):
        return self.check_page(ACCOUNT_URL)
