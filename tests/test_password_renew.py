import allure
import settings
from pages.account_page import AccountPage
import pytest
from conftest import driver

class TestPasswordRenew:

    @allure.description('Проверяем переход на страницу восстановления пароля со страницы логина по клику на восстановить пароль')
    @allure.title('Переход на страницу восстановления пароля')
    def test_pass_renew(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.wait_and_find_clickable_element(account_page.ACCOUNT_BUTTON)
        account_page.account_button_click(account_page.ACCOUNT_BUTTON)
        account_page.wait_and_find_clickable_element(account_page.RENEW_PASS_BUTTON)
        account_page.account_button_click(account_page.RENEW_PASS_BUTTON)
        account_page.check_renew_pass_page()

    @allure.description(
        'Проверяем клин на восстановить пароль')
    @allure.title('Восстановление пароля')
    def test_pass_renew_click(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.wait_and_find_clickable_element(account_page.ACCOUNT_BUTTON)
        account_page.account_button_click(account_page.ACCOUNT_BUTTON)
        account_page.wait_and_find_clickable_element(account_page.RENEW_PASS_BUTTON)
        account_page.account_button_click(account_page.RENEW_PASS_BUTTON)
        account_page.wait_and_find_element(account_page.RENEW_PASS_EMAIL_BUTTON)
        account_page.account_button_click(account_page.RENEW_PASS_EMAIL_FIELD)
        account_page.set_login(account_page.RENEW_PASS_EMAIL_FIELD)
        account_page.account_button_click(account_page.RENEW_PASS_EMAIL_BUTTON)
        account_page.wait_and_find_element(account_page.NEW_PASS_FIELD)
        account_page.check_update_pass_page()

    @allure.title("Проверка подсветки поля пароль при сбросе")
    @allure.description("Проверяем, что поле подсвечивается при нажатии кнопки показать пароль на странице сброса пароля")
    def test_pass_field_light(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page(settings.URL)
        account_page.wait_and_find_clickable_element(account_page.ACCOUNT_BUTTON)
        account_page.account_button_click(account_page.ACCOUNT_BUTTON)
        account_page.wait_and_find_clickable_element(account_page.RENEW_PASS_BUTTON)
        account_page.account_button_click(account_page.RENEW_PASS_BUTTON)
        account_page.wait_and_find_clickable_element(account_page.RENEW_PASS_EMAIL_BUTTON)
        account_page.set_login(account_page.RENEW_PASS_EMAIL_FIELD)
        account_page.account_button_click(account_page.RENEW_PASS_EMAIL_BUTTON)
        account_page.wait_and_find_element(account_page.NEW_PASS_FIELD)
        account_page.set_login(account_page.NEW_PASS_FIELD)
        account_page.account_button_click(account_page.EYE_BUTTON)
        account_page.wait_and_find_element(account_page.EYE_BUTTON_ACTIVE)




