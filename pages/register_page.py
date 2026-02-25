from pages.base_page import BasePage
from locators.register_locators import RegisterLocators
from curl import REGISTER_URL, LOGIN_URL


class RegisterPage(BasePage):
    
    def open_register_page(self):
        self.open(REGISTER_URL)

    def register(self, username, useremail, password):
        self.type(RegisterLocators.USERNAME_INPUT, username)
        self.type(RegisterLocators.USEREMAIL_INPUT, useremail)
        self.type(RegisterLocators.PASSWORD_INPUT, password)
        self.click(RegisterLocators.SUBMIT_BUTTON)

    def check_flash_message_account_exists(self):
        return self.find(RegisterLocators.FLASH_MESSAGE_ACCOUNT_EXISTS).is_displayed()
    
    def check_flash_message_incorrect_password(self):
        return self.find(RegisterLocators.FLASH_MESSAGE_INCORRECT_PASSWORD).is_displayed()

    def click_login_link(self):
        self.click(RegisterLocators.LOGIN_LINK)
    
    def check_login_page(self):
        return self.check_page(LOGIN_URL)