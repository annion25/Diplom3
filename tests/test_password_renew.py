import allure
import settings
from pages.account_page import AccountPage
from conftest import driver

class TestPasswordRenew:

    @allure.description('Проверяем переход на страницу восстановления пароля со страницы логина по клику на восстановить пароль')
    @allure.title('Переход на страницу восстановления пароля')
    def test_pass_renew(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.account_button_click()
        account_page.renewpass_button_click()
        account_page.check_renew_pass_page()

    @allure.description(
        'Проверяем клин на восстановить пароль')
    @allure.title('Восстановление пароля')
    def test_pass_renew_click(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.account_button_click()
        account_page.renewpass_button_click()
        account_page.renewlogin_field_click()
        account_page.set_login_renew()
        account_page.renewpass_button()
        account_page.check_update_pass_page()

    @allure.title("Проверка подсветки поля пароль при сбросе")
    @allure.description("Проверяем, что поле подсвечивается при нажатии кнопки показать пароль на странице сброса пароля")
    def test_pass_field_light(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.account_button_click()
        account_page.renewpass_button_click()
        account_page.set_login_renew()
        account_page.renew_click()
        account_page.set_login_renew_mail()
        account_page.eye_click()
        account_page.check_eye()




