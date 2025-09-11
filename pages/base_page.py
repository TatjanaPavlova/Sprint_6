from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Клик по элементу")
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Скролл до элемента")
    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввод текста в поле ввода")
    def fill_input(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    @allure.step("Переключение на следующую вкладку")
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    @allure.step("Получение заголовка страницы")
    def get_title(self):
        return self.driver.title
    
    @allure.step("Проверка отображения элемента")
    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()