import time

from selenium.webdriver.common.by import By
import allure
from seletools.actions import drag_and_drop
import settings
import data
from pages.base_page import BasePage
from pages.account_page import AccountPage


class MainPage(BasePage):
    ACCOUNT_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Личный Кабинет"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Конструктор"]')
    ORDERS_LIST_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Лента Заказов"]')
    BURGER_SECTION_TEXT = (By.XPATH, '//h1[contains(@class, "text") and text() = "Соберите бургер"]')
    ORDER_LIST_TEXT = (By.XPATH, '//h1[contains(@class, "text") and text() = "Лента заказов"]')
    SAUSE_IMAGE = (By.XPATH, '//img[contains(@class, "BurgerIngredient") and @alt = "Соус Spicy-X"]')
    MODAL_DETAILS_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]')
    MODAL_DETAILES_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close") and @type = "button"]')
    ORDER_PLACE_ROW = (By.XPATH, '//div[contains(@class, "constructor-element constructor-element_pos_top")]')
    BUN_IMAGE = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient") and contains(@href, "aaa6c")]')
    COUNTER_PLACE = (By.XPATH, '//ul/a[contains(@href, "aaa6c")]/div/p')
    ENTER_BUTTON_UNDER_ORDER = (By.XPATH, '//button[contains(@class, "button_button") and text() = "Войти в аккаунт"]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "button_button") and text() = "Оформить заказ"]')
    MODAL_WINDOW_ORDER_CREATED = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]')
    MODAL_WINDOW_ORDER_CREATED_TEXT = (By.XPATH, '//p[text() = "Ваш заказ начали готовить"]')
    FIRST_ORDER_IN_LIST = (By.XPATH, '//li[1][contains(@class, "OrderHistory")]')
    MODAL_ORDER_DETAILS = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]')
    MODAL_ORDER_TEXT = (By.XPATH, '//p[contains(@class, "text_type") and text() = "Состав"]')
    CLOSE_MODAL_ORDER_BUTTON = (
    By.XPATH, '//button[contains(@class, "Modal_modal__close_modified") and @type = "button"]')
    CLOSE_MODAL_ORDER_BUTTON_TWO = (By.XPATH, '//svg[contains(@xmlns, "http")]')
    ORDER_NUMBER_CREATED = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')
    ORDERS_BIG_LIST = (By.XPATH, '//p[contains(@class, "text text_type")]')

    @allure.step('Нажать кнопку')
    def button_click(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step('Проверяем редирект на главную')
    def check_main_page(self):
        current_url = self.get_current_url()
        assert current_url == settings.URL

    @allure.step('Перетаскиваем ингредиент')
    def add_ingredient(self):
        ingredient = self.wait_and_find_element(MainPage.BUN_IMAGE)
        burger_place = self.wait_and_find_element(MainPage.ORDER_PLACE_ROW)
        drag_and_drop(self.driver, ingredient, burger_place)

    @allure.step('Проверяем увеличение каунтера')
    def check_counter_bun(self):
        counter = self.wait_and_find_element(MainPage.COUNTER_PLACE)
        text = str(counter.text)
        assert text == "2"

    @allure.step('Вводим логин')
    def set_login(self, locator):
        login_field = self.wait_and_find_element(locator)
        login_field.click()
        login_field.send_keys(data.AccountServiceData.login)

    @allure.step('Вводим пароль')
    def set_password(self):
        pass_field = self.wait_and_find_element(AccountPage.PASSWORD_FIELD)
        pass_field.click()
        pass_field.send_keys(data.AccountServiceData.password)

    @allure.step("Нажимаем кнопку Войти")
    def enter_click(self):
        enter_button = self.wait_and_find_clickable_element(AccountPage.ENTER_BUTTON)
        enter_button.click()

    @allure.step("Сохраняем номер заказа")
    def check_order_number_equal(self):
        order_number = self.wait_and_find_element(MainPage.ORDER_NUMBER_CREATED)
        order_number_text = order_number.text
        #self.wait_and_find_element(MainPage.CLOSE_MODAL_ORDER_BUTTON)
        time.sleep(20)
        self.find_button()
        list_orders_button = self.wait_and_find_clickable_element(MainPage.ORDERS_LIST_BUTTON)
        list_orders_button.click()
        orders_list = self.wait_and_find_element(MainPage.ORDERS_BIG_LIST).text

        assert order_number_text in self.wait_and_find_element(MainPage.ORDERS_BIG_LIST).text
