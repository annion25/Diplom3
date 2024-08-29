import time

import allure
import settings
from pages.main_page import MainPage
from pages.account_page import AccountPage
from conftest import driver

class TestMainPage:

    @allure.description('Проверяем переход в Конструктор со страницы логина')
    @allure.title('Переход по кнопке Конструктор со страницы логина на главную')
    def test_move_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.account_button_click()
        main_page.constr_button_click()
        main_page.check_main_page()

    @allure.description('Проверяем переход в Ленту заказов с главной')
    @allure.title('Переход по кнопке Лента заказов с главной страницы')
    def test_move_to_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.orderlist_button_click()
        main_page.check_orderlist_page()


    @allure.title("Проверка всплывающего окна по клику на ингредиент из конструктора")
    @allure.description("Кликаем на элемент, проверяем появление окна с деталями")
    def test_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.sause_button_click()
        main_page.check_ingr_det_window()

    @allure.title("Проверка закрытия всплывающего окна по клику на ингредиент из конструктора")
    @allure.description("Кликаем на элемент, проверяем появление окна с деталями, закрываем крестиком")
    def test_ingredient_details_window_close(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.sause_button_click()
        main_page.close_button_click()
        main_page.check_close_modal_window()


    @allure.title("Проверка увеличения каунтера при добавлении ингредиента в заказ")
    @allure.description("Добавляем ингредиент в заказ, проверяем изменение счетчика")
    def test_increase_counter_after_ingredient_add(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.add_ingredient()
        main_page.check_counter_bun()


    @allure.title("Оформление заказа залогиненным пользователем")
    @allure.description("Добавляем ингредиент, логинимся, оформляем заказ")
    def test_order_creation_with_auth(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.add_ingredient()
        main_page.enter_click_low()
        main_page.set_login()
        main_page.set_password()
        main_page.enter_click()
        main_page.place_order_click()
        main_page.check_order_creation()


