from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from curl import BASE_URL

class BasePage:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url=BASE_URL):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text