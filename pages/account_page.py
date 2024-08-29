from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure

from data import AccountServiceData
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
        self.wait_and_find_clickable_element(self.LOGIN_FIELD)
        current_url = self.get_current_url()
        assert 'login' in current_url

    @allure.step('Вводим логин')
    def set_login(self):
        login_field = self.wait_and_find_element(self.LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(AccountServiceData.login)

    @allure.step('Вводим логин')
    def set_login_renew(self):
        login_field = self.wait_and_find_element(self.RENEW_PASS_EMAIL_FIELD)
        login_field.click()
        login_field.send_keys(AccountServiceData.login)


    @allure.step('Вводим логин')
    def set_login_renew_mail(self):
        login_field = self.wait_and_find_element(self.NEW_PASS_FIELD)
        login_field.click()
        login_field.send_keys(AccountServiceData.login)

    @allure.step("Нажимаем кнопку Восстановить")
    def renew_click(self):
        button = self.wait_and_find_clickable_element(self.RENEW_PASS_EMAIL_BUTTON)
        button.click()

    @allure.step("Нажимаем кнопку Глаз")
    def eye_click(self):
        button = self.wait_and_find_clickable_element(self.EYE_BUTTON)
        button.click()

    @allure.step("Проверяем, что глаз активен")
    def check_eye(self):
        eye = self.wait_and_find_element(self.EYE_BUTTON_ACTIVE)
        assert eye is not None


    @allure.step('Вводим пароль')
    def set_password(self):
        pass_field = self.wait_and_find_element(self.PASSWORD_FIELD)
        pass_field.click()
        pass_field.send_keys(AccountServiceData.password)

    @allure.step("Нажимаем кнопку Войти")
    def enter_click(self):
        enter_button = self.wait_and_find_clickable_element(self.ENTER_BUTTON)
        enter_button.click()

    @allure.step('Проверяем редирект в личный кабинет')
    def check_account_page(self):
        self.wait_and_find_clickable_element(self.PROFILE_BUTTON)
        current_url = self.get_current_url()
        assert 'account/profile' in current_url

    @allure.step('Проверяем редирект на историю заказов')
    def check_orders_page(self):
        self.wait_and_find_element(self.ORDERS_LIST)
        current_url = self.get_current_url()
        assert 'order-history' in current_url

    @allure.step('Проверяем редирект на восстановление пароля')
    def check_renew_pass_page(self):
        current_url = self.get_current_url()
        assert 'forgot-password' in current_url

    @allure.step('Проверяем редирект на сброс пароля')
    def check_update_pass_page(self):
        self.wait_and_find_element(self.NEW_PASS_FIELD)
        current_url = self.get_current_url()
        assert 'reset-password' in current_url

    @allure.step('Нажать кнопку История')
    def history_button_click(self):
        history_button = self.wait_and_find_clickable_element(self.HISTORY_BUTTON)
        history_button.click()

    @allure.step('Нажать кнопку Выход')
    def exit_button_click(self):
        exit_button = self.wait_and_find_clickable_element(self.EXIT_BUTTON)
        exit_button.click()


    @allure.step('Нажать кнопку Восстановить пароль')
    def renewpass_button(self):
        button = self.wait_and_find_clickable_element(self.RENEW_PASS_EMAIL_BUTTON)
        button.click()

    @allure.step('Нажать кнопку Восстановить пароль')
    def renewpass_button_click(self):
        renewpass_button = self.wait_and_find_clickable_element(self.RENEW_PASS_BUTTON)
        renewpass_button.click()


    @allure.step('Кликнуть в поле нового логина')
    def renewlogin_field_click(self):
        self.wait_and_find_element(self.RENEW_PASS_EMAIL_BUTTON)
        renew_field = self.wait_and_find_element(self.RENEW_PASS_EMAIL_FIELD)
        renew_field.click()







