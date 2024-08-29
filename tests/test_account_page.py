import allure
import settings
from pages.account_page import AccountPage
from conftest import driver

class TestAccountPage:

    @allure.description('Проверяем переход в Личный кабинет по клику на кнопку Личный кабинет незалогиненным '
                        'пользователем')
    @allure.title('Переход в Личный кабинет незалогиненным пользователем')
    def test_account_login_page(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.account_button_click()
        account_page.check_loginpage()

    @allure.description(
            'Проверяем переход в Личный кабинет по клику на кнопку Личный кабинет незалогиненным пльзователем, логин, '
            'проверяем, что в личном кабинете в правой панели есть кнопка Профиль и изменился url')
    @allure.title('Переход в Личный кабинет залогиненным пользователем')
    def test_account_enter(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.account_button_click()
        account_page.check_loginpage()
        account_page.set_login()
        account_page.set_password()
        account_page.enter_click()
        account_page.account_button_click()
        account_page.check_account_page()

    @allure.title("Проверка перехода в личном кабинете в историю заказов")
    @allure.description("Проверяем в личном кабинете переход в список заказов и отображение заказа")
    def test_orders_list(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.account_button_click()
        account_page.set_login()
        account_page.set_password()
        account_page.enter_click()
        account_page.account_button_click()
        account_page.history_button_click()
        account_page.check_orders_page()


    @allure.title("Проверка выхода из аккаунта")
    @allure.description("Проверяем разлогин")
    def test_exit(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.account_button_click()
        account_page.set_login()
        account_page.set_password()
        account_page.enter_click()
        account_page.account_button_click()
        account_page.exit_button_click()
        account_page.check_loginpage()










