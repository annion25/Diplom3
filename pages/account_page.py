from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure

import data
from pages.base_page import BasePage


class AccountPage(BasePage):

    LOGIN_FIELD = (By.XPATH, '//input[contains(@class, "input__textfield") and @type = "text"]')
    PASSWORD_FIELD = (By.XPATH, '//input[contains(@class, "input__textfield") and @type = "password"]')
    ACCOUNT_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Личный Кабинет"]')
    ENTER_BUTTON = (By.XPATH, '//button[contains(@class, "button") and text() = "Войти"]')
    PROFILE_BUTTON = (By.XPATH, '//a[contains(@class, "Account_link") and text() = "Профиль"]')
    HISTORY_BUTTON = (By.XPATH, '//a[contains(@class, "Account_link") and text() = "История заказов"]')
    ORDERS_LIST = (By.XPATH, '//a[contains(@class, "OrderHistory")]')
    EXIT_BUTTON = (By.XPATH, '//button[contains(@class, "Account_button") and text() = "Выход"]')
    RENEW_PASS_BUTTON = (By.XPATH, '//a[contains(@class, "Auth_link") and text() = "Восстановить пароль"]')
    RENEW_PASS_EMAIL_BUTTON = (By.XPATH, '//button[contains(@class, "button") and text() = "Восстановить"]')
    RENEW_PASS_EMAIL_FIELD = (By.XPATH, '//input[contains(@class, "input__textfield") and @type = "text"]')
    NEW_PASS_FIELD = (By.XPATH, '//input[contains(@class, "input__textfield") and @type = "password"]')
    EYE_BUTTON = (By.XPATH, '//div[contains(@class, "input__icon")]')
    EYE_BUTTON_ACTIVE = (By.XPATH, '//div[contains(@class, "input_status_active")]')


    @allure.step('Проверяем редирект на страницу логина')
    def check_loginpage(self):
        current_url = self.get_current_url()
        assert 'login' in current_url

    @allure.step('Вводим логин')
    def set_login(self, locator):
        login_field = self.wait_and_find_element(locator)
        login_field.click()
        login_field.send_keys(data.AccountServiceData.login)

    @allure.step('Вводим пароль')
    def set_password(self):
        pass_field = self.wait_and_find_element(self.PASSWORD_FIELD)
        pass_field.click()
        pass_field.send_keys(data.AccountServiceData.password)

    @allure.step("Нажимаем кнопку Войти")
    def enter_click(self):
        enter_button = self.wait_and_find_clickable_element(self.ENTER_BUTTON)
        enter_button.click()

    @allure.step('Проверяем редирект в личный кабинет')
    def check_account_page(self):
        current_url = self.get_current_url()
        assert 'account/profile' in current_url

    @allure.step('Проверяем редирект на историю заказов')
    def check_orders_page(self):
        current_url = self.get_current_url()
        assert 'order-history' in current_url

    @allure.step('Проверяем редирект на восстановление пароля')
    def check_renew_pass_page(self):
        current_url = self.get_current_url()
        assert 'forgot-password' in current_url

    @allure.step('Проверяем редирект на сброс пароля')
    def check_update_pass_page(self):
        current_url = self.get_current_url()
        assert 'reset-password' in current_url



