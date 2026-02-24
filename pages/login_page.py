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
        return self.find(LoginLocators.CHECK_BUTTON)

    def get_flash_message(self):
        return self.get_text(LoginLocators.FLASH_MESSAGE)

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)
        return self.current_url() == LOGIN_URL
    
    def click_account_button_without_login(self):
        self.click(LoginLocators.ACCOUNT_BUTTON)
        return self.current_url() == LOGIN_URL
    
    def click_account_button_with_login(self):
        self.click(LoginLocators.ACCOUNT_BUTTON)
        return self.current_url() == ACCOUNT_URL
