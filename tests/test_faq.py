import allure
import pytest

from pages.main_page import MainPage
from data import Faq


@allure.epic("Яндекс.Самокат")
@allure.feature("Вопросы о важном (FAQ)")
class TestFaq:

    @allure.story("При клике на вопрос открывается ответ с верным текстом")
    @allure.title("Текст ответа на вопрос № {number}: {question} соответствует ожидаемому")
    @pytest.mark.parametrize("number, question, expected_answer", Faq.FAQ, ids=[f"Вопрос {number}" for number, _, _ in Faq.FAQ],)
    def test_faq_answer_text(self, driver, number, question, expected_answer):
        index = number - 1

        with allure.step(f"Открыть главную страницу и раскрыть вопрос №{number}: {question}"):
            main_page = MainPage(driver)
            main_page.accept_cookies_if_present()
            actual_answer = main_page.get_faq_answer_text(index)

        with allure.step("Сравнить текст ответа с ожидаемым"):
            assert actual_answer == expected_answer, (f"Текст ответа на вопрос '{question}' не совпадает с ожидаемым.\n"
                f"Ожидалось: {expected_answer}\nПолучено: {actual_answer}")
