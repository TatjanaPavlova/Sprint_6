import pytest
import allure
from data import TestData
from pages.main_page import MainPage

class TestMainPageFAQ:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления нужного текста при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question_index, expected_answer', TestData.test_data_question_answer)
    def test_faq_questions(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq()
        main_page.wait_faq_question(question_index)
        main_page.click_faq_question(question_index)
        main_page.wait_faq_answer(question_index)

        assert main_page.get_faq_answer_text(question_index) == expected_answer
