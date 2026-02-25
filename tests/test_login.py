from pages.login_page import LoginPage
from data_gen import *

def test_success_login(driver):
    # проверь вход в существующий аккаунт
    page = LoginPage(driver)
    page.open_login_page()
    page.login(right_email, right_pass)
    page.find_check_button()
    assert page.check_page()

def test_success_click_login_button(driver):
    # проверь клик по кнопке «Войти в аккаунт» на главной
    page = LoginPage(driver)
    page.open()
    page.click_login_button()
    assert page.check_login_page()

def test_success_click_account_button(driver):
    # проверь клик по кнопке «Личный Кабинет»
    page = LoginPage(driver)
    page.open()
    page.click_login_button()
    assert page.check_login_page()

def test_success_enter_profile_page(driver):
    # проверь переход по клику на «Личный кабинет»
    page = LoginPage(driver)
    page.open_login_page()
    page.login(right_email, right_pass)
    page.click_account_button()
    assert page.check_account_page()