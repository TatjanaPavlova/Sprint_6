import allure
from pages.main_page import MainPage


class TestLogoNavigation:

    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат"')
    def test_logo_scooter_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.wait_order_button_in_header()
        main_page.click_order_button_in_header()
        main_page.wait_logo_scooter()
        main_page.click_logo_scooter()
        main_page.wait_main_header()
        assert main_page.is_main_header_displayed()

    @allure.title('Проверка перехода на страницу "Дзен" при клике на лого "Яндекс"')
    def test_logo_yandex_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.wait_logo_yandex()
        main_page.click_logo_yandex()
        main_page.switch_to_next_tab()
        main_page.wait_for_url("dzen.ru")
        assert "dzen.ru" in main_page.get_current_url()