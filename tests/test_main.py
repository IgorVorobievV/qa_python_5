from pages.main_page import MainPage
from data_gen import *

def test_success_click_buns_button(driver):
    # проверь, что работают переходы к разделам: «Булки»
    page = MainPage(driver)
    page.open()
    page.click_sauces_button()
    page.click_buns_button()
    assert page.check_active_buns_button()

def test_success_click_sauces_button(driver):
    # проверь, что работают переходы к разделам: «Соусы»
    page = MainPage(driver)
    page.open()
    page.click_sauces_button()
    assert page.check_active_sauces_button()

def test_success_click_toppings_button(driver):
    # проверь, что работают переходы к разделам: «Начинки»
    page = MainPage(driver)
    page.open()
    page.click_toppings_button()
    assert page.check_active_toppings_button()