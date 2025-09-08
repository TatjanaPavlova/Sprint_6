import allure
from pages.main_page import MainPage

class TestLogo:

    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат" в шапке сайта')
    def test_logo_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert "Дзен" in main_page.get_page_title()