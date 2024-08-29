from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure
from conftest import driver

class BasePage:

    ACCOUNT_BUTTON = (By.XPATH, '//p[contains(@class, "AppHeader") and text() = "Личный Кабинет"]')
    CLOSE_MODAL_ORDER = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")


    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем видимый элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ищем нажимаемый элемент')
    def wait_and_find_clickable_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Проверяем текущий url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Нажать кнопку Личный Кабинет')
    def account_button_click(self):
        account_button = self.wait_and_find_clickable_element(self.ACCOUNT_BUTTON)
        account_button.click()

    @allure.step("Найти кнопку Закрыть модальное окно")
    def find_button(self):
        self.wait_and_find_clickable_element(self.CLOSE_MODAL_ORDER)
        element = self.driver.find_element(self.CLOSE_MODAL_ORDER)
        self.driver.execute_script("arguments[0].click();", element)

