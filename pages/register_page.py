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

    def get_flash_message(self):
        return self.get_text(RegisterLocators.FLASH_MESSAGE)

    def click_login_link(self):
        self.click(RegisterLocators.LOGIN_LINK)
        return self.driver.current_url == LOGIN_URL