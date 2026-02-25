from pages.register_page import RegisterPage
from data_gen import *

def test_success_register(driver):
    #зарегистрируй аккаунт с валидными данными
    page = RegisterPage(driver)
    page.open_register_page()
    name = generate_password(6)
    email = generate_email()
    password = generate_password(6)
    page.register(name, email, password)
    
    #проверь создание аккаунта
    page.open_register_page()
    page.register(name, email, password)
    assert page.check_flash_message_account_exists()

def test_invalid_register_incorrect_password(driver):
    #зарегистрируй аккаунт с невалидным паролем
    page = RegisterPage(driver)
    page.open_register_page()
    name = generate_password(6)
    email = generate_email()
    password = generate_password(5)
    page.register(name, email, password)

    #проверь вывод ошибки
    assert page.check_flash_message_incorrect_password()

def test_success_click_login_link(driver):
    # проверь клик по кнопке «Войти»
    page = RegisterPage(driver)
    page.open_register_page()
    page.click_login_link()
    assert page.check_login_page()