from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure
from conftest import driver

class BasePage:

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем видимый элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ищем нажимаемый элемент')
    def wait_and_find_clickable_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Проверяем текущий url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключаемся на новое окно")
    def switch_to_latest_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Скролим страницу до нужного элемента')
    def scroll(self, list):
        return self.driver.execute_script("arguments[0].scrollIntoView();", list)


    @allure.step('Нажать кнопку Личный Кабинет')
    def account_button_click(self, locator):
        account_button = self.wait_and_find_element(locator)
        account_button.click()

    @allure.step("Найти кнопку Закрыть модальное окно")
    def find_button(self):
        element = self.driver.find_element(By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
        self.driver.execute_script("arguments[0].click();", element)

