import allure
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):

    @allure.step("Принять cookies, если баннер отображается")
    def accept_cookies_if_present(self):
        try:
            self.wait_and_click(Locators.COOKIE_BUTTON, timeout=3)
        except TimeoutException:
            # баннер cookies уже был закрыт ранее
            pass

    @allure.step("Нажать кнопку 'Заказать' в шапке страницы")
    def click_order_button_top(self):
        self.wait_and_click(Locators.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' в нижней части страницы")
    def click_order_button_bottom(self):
        self.scroll_to_element(Locators.ORDER_BUTTON_BOTTOM)
        self.wait_and_click(Locators.ORDER_BUTTON_BOTTOM)

    @allure.step("Раскрыть вопрос FAQ и получить текст ответа")
    def get_faq_answer_text(self, index):
        question_locator = Locators.faq_question_button(index)
        answer_locator = Locators.faq_answer_panel(index)

        self.scroll_to_element(question_locator)
        self.wait_and_click(question_locator)
        return self.get_text_of_element(answer_locator)

    @allure.step("Раскрыть вопрос в разделе FAQ")
    def click_faq_question(self, index):
        question_locator = Locators.faq_question_button(index)
        self.scroll_to_element(question_locator)
        self.wait_and_click(question_locator)

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_on_element(Locators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(Locators.YANDEX_LOGO)
