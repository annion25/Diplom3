import time

import allure
import settings
from pages.main_page import MainPage
from pages.account_page import AccountPage
import pytest
from conftest import driver

class TestMainPage:

    @allure.description('Проверяем переход в Конструктор со страницы логина')
    @allure.title('Переход по кнопке Конструктор со страницы логина на главную')
    def test_move_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.wait_and_find_clickable_element(main_page.CONSTRUCTOR_BUTTON)
        main_page.button_click(main_page.ACCOUNT_BUTTON)
        main_page.wait_and_find_clickable_element(AccountPage.LOGIN_FIELD)
        main_page.button_click(main_page.CONSTRUCTOR_BUTTON)
        main_page.wait_and_find_element(main_page.BURGER_SECTION_TEXT)
        main_page.check_main_page()

    @allure.description('Проверяем переход в Ленту заказов с главной')
    @allure.title('Переход по кнопке Лента заказов с главной страницы')
    def test_move_to_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.wait_and_find_clickable_element(main_page.CONSTRUCTOR_BUTTON)
        main_page.button_click(main_page.ORDERS_LIST_BUTTON)
        main_page.wait_and_find_element(main_page.ORDER_LIST_TEXT)

    @allure.title("Проверка всплывающего окна по клику на ингредиент из конструктора")
    @allure.description("Кликаем на элемент, проверяем появление окна с деталями")
    def test_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.wait_and_find_clickable_element(main_page.CONSTRUCTOR_BUTTON)
        main_page.button_click(main_page.SAUSE_IMAGE)
        main_page.wait_and_find_element(main_page.MODAL_DETAILS_WINDOW)

    @allure.title("Проверка закрытия всплывающего окна по клику на ингредиент из конструктора")
    @allure.description("Кликаем на элемент, проверяем появление окна с деталями, закрываем крестиком")
    def test_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.wait_and_find_clickable_element(main_page.CONSTRUCTOR_BUTTON)
        main_page.button_click(main_page.SAUSE_IMAGE)
        main_page.wait_and_find_element(main_page.MODAL_DETAILS_WINDOW)
        main_page.button_click(main_page.MODAL_DETAILES_CLOSE_BUTTON)
        main_page.wait_and_find_element(main_page.CONSTRUCTOR_BUTTON)

    @allure.title("Проверка увеличения каунтера при добавлении ингредиента в заказ")
    @allure.description("Добавляем ингредиент в заказ, проверяем изменение счетчика")
    def test_increase_counter_after_ingredient_add(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.wait_and_find_clickable_element(main_page.CONSTRUCTOR_BUTTON)
        main_page.add_ingredient()
        main_page.wait_and_find_element(main_page.COUNTER_PLACE)
        time.sleep(3)
        main_page.check_counter_bun()


    @allure.title("Оформление заказа залогиненным пользователем")
    @allure.description("Добавляем ингредиент, логинимся, оформляем заказ")
    def test_order_creation_with_auth(self, driver):
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
        main_page.wait_and_find_element(main_page.MODAL_WINDOW_ORDER_CREATED)
        main_page.wait_and_find_element(main_page.MODAL_WINDOW_ORDER_CREATED_TEXT)


















