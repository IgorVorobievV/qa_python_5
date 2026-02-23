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
    message = page.get_flash_message()
    assert "Такой пользователь уже существует" in message

def test_invalid_register_invalid_pass_error(driver):
    #зарегистрируй аккаунт с невалидным паролем
    page = RegisterPage(driver)
    page.open_register_page()
    name = generate_password(6)
    email = generate_email()
    password = generate_password(5)
    page.register(name, email, password)

    #проверь вывод ошибки
    message = page.get_flash_message()
    assert "Некорректный пароль" in message

def test_success_click_login_link(driver):
    # проверь клик по кнопке «Войти»
    page = RegisterPage(driver)
    page.open_register_page()
    assert page.click_login_link()