import allure
import settings
from pages.main_page import MainPage
from pages.account_page import AccountPage
from selenium.webdriver.common.by import By
import pytest
from conftest import driver

class TestOrderList:

    @allure.description('Проверяем всплывающего окна с деталями из ленты заказов')
    @allure.title('Проверка открытия модального окна с деталями заказа')
    def test_move_to_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.wait_and_find_clickable_element(main_page.CONSTRUCTOR_BUTTON)
        main_page.button_click(main_page.ORDERS_LIST_BUTTON)
        main_page.wait_and_find_element(main_page.ORDER_LIST_TEXT)
        main_page.button_click(main_page.FIRST_ORDER_IN_LIST)
        main_page.wait_and_find_element(main_page.MODAL_ORDER_DETAILS)

    @allure.description('Проверяем отображение заказов пользователя в Ленте заказов')
    @allure.title('Проверяем номера заказов из истории заказов пользователя на отображение в ленте заказов')
    def test_check_orders_from_history_in_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.wait_and_find_clickable_element(main_page.CONSTRUCTOR_BUTTON)
        main_page.add_ingredient()
        main_page.button_click(main_page.ENTER_BUTTON_UNDER_ORDER)
        main_page.set_login(AccountPage.LOGIN_FIELD)
        main_page.set_password()
        main_page.enter_click()
        main_page.wait_and_find_element(main_page.PLACE_ORDER_BUTTON)
        main_page.button_click(main_page.PLACE_ORDER_BUTTON)
        main_page.wait_and_find_clickable_element(main_page.MODAL_WINDOW_ORDER_CREATED)
        main_page.wait_and_find_clickable_element(main_page.CLOSE_MODAL_ORDER_BUTTON)
        main_page.check_order_number_equal()







