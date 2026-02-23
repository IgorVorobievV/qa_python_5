from pages.login_page import LoginPage
from data_gen import *

def test_success_login(driver):
    # проверь вход в существующий аккаунт
    page = LoginPage(driver)
    page.open_login_page()
    assert page.login(right_email, right_pass)

def test_success_click_login_button(driver):
    # проверь клик по кнопке «Войти в аккаунт» на главной
    page = LoginPage(driver)
    page.open()
    assert page.click_login_button()

def test_success_click_account_button(driver):
    # проверь клик по кнопке «Личный Кабинет»
    page = LoginPage(driver)
    page.open()
    assert page.click_account_button_without_login()

def test_success_enter_profile_page(driver):
    # проверь переход по клику на «Личный кабинет»
    page = LoginPage(driver)
    page.open_login_page()
    page.login(right_email, right_pass)
    assert page.click_account_button_with_login()