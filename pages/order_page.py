from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure
from data import TestData

class OrderPage(BasePage):

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.name_field)
        self.click_on_element(OrderPageLocators.name_field)
        self.send_keys_to_input(OrderPageLocators.name_field, test_data[0])
        self.click_on_element(OrderPageLocators.lastname_field)
        self.send_keys_to_input(OrderPageLocators.lastname_field, test_data[1])
        self.click_on_element(OrderPageLocators.address_field)
        self.send_keys_to_input(OrderPageLocators.address_field, test_data[2])
        self.click_on_element(OrderPageLocators.subway_station)
        self.send_keys_to_input(OrderPageLocators.subway_station, test_data[3])
        self.click_on_element(OrderPageLocators.select_subway_station)
        self.click_on_element(OrderPageLocators.phone_field)
        self.send_keys_to_input(OrderPageLocators.phone_field, test_data[4])
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.date)
        self.click_on_element(OrderPageLocators.date)
        self.send_keys_to_input(OrderPageLocators.date, test_data[5])
        self.click_on_element(OrderPageLocators.checkbox_grey_color_scooter)
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(OrderPageLocators.dropdown_item_rental_period)
        self.click_on_element(OrderPageLocators.comment)
        self.send_keys_to_input(OrderPageLocators.comment, test_data[6])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)

    @allure.step('Кликнуть по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.select_subway_station)

    @allure.step('Ввести дату заказа в поле "Когда привезти самокат"')
    def send_keys_date_by_keyboard_input(self):
        self.send_keys_to_input(OrderPageLocators.date).send_keys(TestData.test_data_user1[5])

    @allure.step('Кликнуть по выбранной дате в выпадающем календаре поля ввода даты начала аренды')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.calendar_item)

    @allure.step('Проверить отображаение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.button_check_status_of_order)


