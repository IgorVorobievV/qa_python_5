from pages.account_page import AccountPage
from data_gen import *

def test_success_click_constructor_button(driver):
    # проверь переход по клику на «Конструктор»
    page = AccountPage(driver)
    page.open_login_page()
    page.login(right_email, right_pass)
    page.open_account_page()
    page.click_constructor_button()
    assert page.check_page()

def test_success_click_logo(driver):
    # проверь переход по клику на логотип Stellar Burgers
    page = AccountPage(driver)
    page.open_login_page()
    page.login(right_email, right_pass)
    page.open_account_page()
    page.click_logo()
    assert page.check_page()

def test_success_logout(driver):
    # проверь выход по кнопке «Выйти» в личном кабинете
    page = AccountPage(driver)
    page.open_login_page()
    page.login(right_email, right_pass)
    page.open_account_page()
    page.logout()
    page.click_account_button()
    assert page.check_login_page()
