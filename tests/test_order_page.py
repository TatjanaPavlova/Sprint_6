import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import TestData


class TestOrderPage:

    @allure.title('Позитивный сценарий оформления заказа')
    @allure.description('Сквозное тестирование функциональности оформления заказа из двух точек входа')
    @pytest.mark.parametrize('order_button, user_data', [
        (MainPageLocators.ORDER_BUTTON_HEADER, TestData.test_data_user1),
        (MainPageLocators.ORDER_BUTTON_MAIN, TestData.test_data_user2)
    ])
    def test_order_success(self, driver, order_button, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.scroll_to(order_button)
        main_page.click(order_button)

        order_page.fill_first_form(user_data)
        order_page.fill_second_form(user_data)

        assert order_page.is_status_button_displayed()