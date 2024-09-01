import allure
import settings
from pages.main_page import MainPage
from pages.account_page import AccountPage
from conftest import driver

class TestOrderList:

    @allure.description('Проверяем всплывающего окна с деталями из ленты заказов')
    @allure.title('Проверка открытия модального окна с деталями заказа')
    def test_modal_in_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.orderlist_button_click()
        main_page.check_first_order()

    @allure.description('Проверяем отображение заказов пользователя в Ленте заказов')
    @allure.title('Проверяем номера заказов из истории заказов пользователя на отображение в ленте заказов')
    def test_check_orders_from_history_in_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.add_ingredient()
        main_page.enter_click_low()
        main_page.set_login()
        main_page.set_password()
        main_page.enter_click()
        main_page.place_order_click()
        main_page.check_order_number_equal()

    @allure.title("Проверяем увеличение счетчика за все время при создании нового заказа")
    @allure.description("Запоминаем счетчик, создаем заказ, проверяем, что значение больше предыдущего")
    def test_check_increase_amount_orders_all(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.orderlist_button_click()
        amount_1 = main_page.write_all_amount()
        main_page.constr_button_click()
        main_page.add_ingredient()
        main_page.enter_click_low()
        main_page.set_login()
        main_page.set_password()
        main_page.enter_click()
        main_page.place_order_click()
        main_page.close_modal()
        main_page.orderlist_button_click()
        amount_2 = main_page.write_all_amount()
        main_page.check_amount(amount_1, amount_2)

    @allure.title("Проверяем увеличение счетчика за сегодня при создании нового заказа")
    @allure.description("Запоминаем счетчик, создаем заказ, проверяем, что значение больше предыдущего")
    def test_check_increase_amount_orders_today(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.orderlist_button_click()
        amount_1 = main_page.write_today_amount()
        main_page.constr_button_click()
        main_page.add_ingredient()
        main_page.enter_click_low()
        main_page.set_login()
        main_page.set_password()
        main_page.enter_click()
        main_page.place_order_click()
        main_page.close_modal()
        main_page.orderlist_button_click()
        amount_2 = main_page.write_today_amount()
        main_page.check_amount(amount_1, amount_2)

    @allure.title("Проверяем появления нового закза в разделе в работе")
    @allure.description("Создаем заказ, переходим ленту, проверяем там наличие номера заказа")
    def test_check_new_order_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(settings.URL)
        main_page.add_ingredient()
        main_page.enter_click_low()
        main_page.set_login()
        main_page.set_password()
        main_page.enter_click()
        main_page.place_order_click()
        main_page.check_order_number_in_work()










