from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):

    @allure.step('Ожидание кнопки "Заказать" в хэдере')
    def wait_order_button_in_header(self):
        self.wait_for_visibility(MainPageLocators.order_button_in_header)

    @allure.step('Клик по кнопке "Заказать" в хэдере')
    def click_order_button_in_header(self):
        self.click(MainPageLocators.order_button_in_header)

    @allure.step('Ожидание кнопки "Заказать" внизу страницы')
    def wait_order_button_in_main(self):
        self.wait_for_visibility(MainPageLocators.order_button_in_main)

    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_order_button_in_main(self):
        self.click(MainPageLocators.order_button_in_main)

    @allure.step('Ожидание логотипа "Самокат" в хэдере')
    def wait_logo_scooter(self):
        self.wait_for_visibility(MainPageLocators.header_logo_scooter)

    @allure.step('Клик по логотипу "Самокат"')
    def click_logo_scooter(self):
        self.click(MainPageLocators.header_logo_scooter)

    @allure.step('Ожидание логотипа "Яндекс" в хэдере')
    def wait_logo_yandex(self):
        self.wait_for_visibility(MainPageLocators.header_logo_yandex)

    @allure.step('Клик по логотипу "Яндекс"')
    def click_logo_yandex(self):
        self.click(MainPageLocators.header_logo_yandex)

    @allure.step('Ожидание заголовка главной страницы')
    def wait_main_header(self):
        self.wait_for_visibility(MainPageLocators.main_header)

    @allure.step('Проверка отображения заголовка главной страницы')
    def is_main_header_displayed(self):
        return self.is_displayed(MainPageLocators.main_header)

    @allure.step('Скролл до секции "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to(MainPageLocators.faq_section)

    @allure.step('Ожидание вопроса FAQ')
    def wait_faq_question(self, index):
        self.wait_for_visibility(MainPageLocators.faq_questions[index])

    @allure.step('Клик по вопросу FAQ')
    def click_faq_question(self, index):
        self.click(MainPageLocators.faq_questions[index])

    @allure.step('Ожидание ответа FAQ')
    def wait_faq_answer(self, index):
        self.wait_for_visibility(MainPageLocators.faq_answers[index])

    @allure.step('Получение текста ответа FAQ')
    def get_faq_answer_text(self, index):
        return self.get_text(MainPageLocators.faq_answers[index])

    