from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step('Заполнение первой части формы заказа')
    def fill_first_form(self, data):
        self.wait_for_visible(OrderPageLocators.name_field)
        self.fill_input(OrderPageLocators.name_field, data[0])
        self.fill_input(OrderPageLocators.lastname_field, data[1])
        self.fill_input(OrderPageLocators.address_field, data[2])
        self.fill_input(OrderPageLocators.subway_station, data[3])
        self.click(OrderPageLocators.select_subway_station)
        self.fill_input(OrderPageLocators.phone_field, data[4])
        self.click(OrderPageLocators.button_next)

    @allure.step('Заполнение второй части формы заказа')
    def fill_second_form(self, data):
        self.wait_for_visible(OrderPageLocators.date)
        self.fill_input(OrderPageLocators.date, data[5])
        self.click(OrderPageLocators.field_rental_period)
        self.click(OrderPageLocators.dropdown_item_rental_period)
        self.click(OrderPageLocators.checkbox_grey_color_scooter)
        self.fill_input(OrderPageLocators.comment, data[6])
        self.click(OrderPageLocators.button_make_order)
        self.wait_for_visible(OrderPageLocators.button_yes_confirm_order)
        self.click(OrderPageLocators.button_yes_confirm_order)

    @allure.step('Выбор даты через календарь')
    def select_date_from_calendar(self):
        self.click(OrderPageLocators.calendar_item)

    @allure.step('Проверка кнопки "Посмотреть статус" после заказа')
    def is_status_button_displayed(self):
        return self.is_displayed(OrderPageLocators.button_check_status_of_order)


