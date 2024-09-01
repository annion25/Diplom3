import time
from selenium.webdriver.common.by import By
import allure
from seletools.actions import drag_and_drop
import settings
from data import AccountServiceData
from pages.base_page import BasePage



class MainPage(BasePage):
    ACCOUNT_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Личный Кабинет"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Конструктор"]')
    ORDERS_LIST_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Лента Заказов"]')
    BURGER_SECTION_TEXT = (By.XPATH, '//h1[contains(@class, "text") and text() = "Соберите бургер"]')
    ORDER_LIST_TEXT = (By.XPATH, '//h1[contains(@class, "text") and text() = "Лента заказов"]')
    SAUSE_IMAGE = (By.XPATH, '//img[contains(@class, "BurgerIngredient") and @alt = "Соус Spicy-X"]')
    MODAL_DETAILS_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]')
    MODAL_DETAILS_TEXT = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')
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
    CLOSE_MODAL_ORDER_BUTTON = (By.XPATH,
                                '//section[contains(@class,"Modal_modal_opened")]//button[contains(@class,"Modal_modal__close_modified")]')
    CLOSE_MODAL_ORDER_BUTTON_TWO = (By.XPATH, '//svg[contains(@xmlns, "http")]')
    ORDER_NUMBER_CREATED = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')
    ORDERS_BIG_LIST = (By.XPATH, '//p[contains(@class, "text text_type")]')
    PASSWORD_FIELD_MAIN = (By.XPATH, '//input[contains(@class, "input__textfield") and @type = "password"]')
    ENTER_BUTTON_MAIN = (By.XPATH, '//button[contains(@class, "button") and text() = "Войти"]')
    LOGIN_FIELD = (By.XPATH, '//input[contains(@class, "input__textfield") and @type = "text"]')
    ORDER_AMOUNT_ALL = (By.XPATH,
                        '//p[contains(@class, "text") and text() = "Выполнено за все время:"]/following-sibling::p')
    ORDER_AMOUNT_TODAY = (By.XPATH,
                          '//p[contains(@class, "text") and text() = "Выполнено за сегодня:"]/following-sibling::p')
    ORDER_IN_WORK = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')



    @allure.step('Нажать кнопку')
    def button_click(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step('Нажать кнопку Коструктор')
    def constr_button_click(self):
        button = self.wait_and_find_element(self.CONSTRUCTOR_BUTTON)
        button.click()

    @allure.step('Нажать кнопку Лента Заказов')
    def orderlist_button_click(self):
        button = self.wait_and_find_element(self.ORDERS_LIST_BUTTON)
        button.click()

    @allure.step('Нажать кнопку Соус')
    def sause_button_click(self):
        button = self.wait_and_find_element(self.SAUSE_IMAGE)
        button.click()

    @allure.step('Нажать кнопку Закрыть модальное окно')
    def close_button_click(self):
        button = self.wait_and_find_element(self.MODAL_DETAILES_CLOSE_BUTTON)
        button.click()

    @allure.step('Проверяем редирект на главную')
    def check_main_page(self):
        self.wait_and_find_element(self.BURGER_SECTION_TEXT)
        current_url = self.get_current_url()
        assert current_url == settings.URL

    @allure.step('Проверяем переход на Ленту Заказов')
    def check_orderlist_page(self):
        self.wait_and_find_element(self.ORDER_LIST_TEXT)
        current_url = self.get_current_url()
        assert 'feed' in current_url

    @allure.step('Проверяет открытие окна с деталями ингредента')
    def check_ingr_det_window(self):
        text = self.wait_and_find_element(self.MODAL_DETAILS_WINDOW).text
        assert "Детали" in text

    @allure.step('Проверяем, что модальное окно закрылось')
    def check_close_modal_window(self):
        button = self.wait_and_find_clickable_element(self.CONSTRUCTOR_BUTTON)
        assert button is not None

    @allure.step('Перетаскиваем ингредиент')
    def add_ingredient(self):
        self.wait_and_find_clickable_element(self.CONSTRUCTOR_BUTTON)
        ingredient = self.wait_and_find_element(self.BUN_IMAGE)
        burger_place = self.wait_and_find_element(self.ORDER_PLACE_ROW)
        drag_and_drop(self.driver, ingredient, burger_place)

    @allure.step('Проверяем увеличение каунтера')
    def check_counter_bun(self):
        time.sleep(3)
        counter = self.wait_and_find_element(self.COUNTER_PLACE)
        text = str(counter.text)
        assert text == "2"

    @allure.step('Вводим логин')
    def set_login(self):
        login_field = self.wait_and_find_element(self.LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(AccountServiceData.login)

    @allure.step('Вводим пароль')
    def set_password(self):
        pass_field = self.wait_and_find_element(self.PASSWORD_FIELD_MAIN)
        pass_field.click()
        pass_field.send_keys(AccountServiceData.password)

    @allure.step("Нажимаем кнопку Войти")
    def enter_click(self):
        enter_button = self.wait_and_find_clickable_element(self.ENTER_BUTTON_MAIN)
        enter_button.click()

    @allure.step("Нажимаем кнопку Войти")
    def enter_click_low(self):
        enter_button = self.wait_and_find_clickable_element(self.ENTER_BUTTON_UNDER_ORDER)
        enter_button.click()

    @allure.step("Нажимаем кнопку Заказать")
    def place_order_click(self):
        button = self.wait_and_find_clickable_element(self.PLACE_ORDER_BUTTON)
        button.click()


    @allure.step("Найти кнопку Закрыть модальное окно")
    def find_button(self):
        element = self.driver.find_element(By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Сохраняем номер заказа и проверяем его в списке")
    def check_order_number_equal(self):
        self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED)
        self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED_TEXT)
        self.wait_and_find_clickable_element(self.CLOSE_MODAL_ORDER_BUTTON)
        order_number = self.wait_and_find_element(self.ORDER_NUMBER_CREATED)
        order_number_text = order_number.text
        self.wait_and_find_clickable_element(self.CLOSE_MODAL_ORDER_BUTTON)
        self.wait_and_find_visible_element(self.CLOSE_MODAL_ORDER_BUTTON)
        self.find_button()
        self.wait_and_find_clickable_element(self.ORDERS_LIST_BUTTON)
        list_orders_button = self.wait_and_find_clickable_element(self.ORDERS_LIST_BUTTON)
        list_orders_button.click()
        orders_list = self.wait_and_find_element(self.ORDERS_BIG_LIST).text

        assert order_number_text in orders_list

    @allure.step("Сохраняем номер заказа и проверяем его в работе")
    def check_order_number_in_work(self):
        self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED)
        self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED_TEXT)
        self.wait_and_find_clickable_element(self.CLOSE_MODAL_ORDER_BUTTON)
        order_number = self.wait_and_find_element(self.ORDER_NUMBER_CREATED)
        order_number_text = order_number.text
        self.wait_and_find_clickable_element(self.CLOSE_MODAL_ORDER_BUTTON)
        self.wait_and_find_visible_element(self.CLOSE_MODAL_ORDER_BUTTON)
        self.find_button()
        list_orders_button = self.wait_and_find_clickable_element(self.ORDERS_LIST_BUTTON)
        self.wait_and_find_visible_element(self.ORDERS_LIST_BUTTON)
        list_orders_button.click()
        order_in_work = self.wait_and_find_element(self.ORDER_IN_WORK)
        order_in_work_num = order_in_work.text

        assert int(order_in_work_num) == int(order_number_text)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED)
        self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED_TEXT)
        self.wait_and_find_clickable_element(self.CLOSE_MODAL_ORDER_BUTTON)
        self.wait_and_find_element(self.ORDER_NUMBER_CREATED)
        self.wait_and_find_clickable_element(self.CLOSE_MODAL_ORDER_BUTTON)
        self.wait_and_find_visible_element(self.CLOSE_MODAL_ORDER_BUTTON)
        self.find_button()
        self.wait_and_find_clickable_element(self.ORDERS_LIST_BUTTON)
        self.wait_and_find_visible_element(self.ORDERS_LIST_BUTTON)

    @allure.step("Проверяем, что количество заказов после создания заказа увеличилось")
    def check_amount(self, amount_1, amount_2):
        assert int(amount_2) > int(amount_1)


    @allure.step("Проверка окна создания заказа")
    def check_order_creation(self):
        self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED)
        text = self.wait_and_find_element(self.MODAL_WINDOW_ORDER_CREATED_TEXT).text
        assert "Ваш заказ начали готовить" in text

    @allure.step("Проверяем модальное окно деталей первого заказа из Ленты заказов")
    def check_first_order(self):
        self.wait_and_find_element(self.ORDER_LIST_TEXT)
        self.button_click(self.FIRST_ORDER_IN_LIST)
        window = self.wait_and_find_element(self.MODAL_ORDER_DETAILS)
        assert window is not None

    @allure.step("Запоминаем число заказов за все время")
    def write_all_amount(self):
        all_amount = self.wait_and_find_element(self.ORDER_AMOUNT_ALL)
        all_amount_number = all_amount.text
        return all_amount_number

    @allure.step("Запоминаем число заказов за сегодня")
    def write_today_amount(self):
        today_amount = self.wait_and_find_element(self.ORDER_AMOUNT_TODAY)
        today_amount_number = today_amount.text
        return today_amount_number




