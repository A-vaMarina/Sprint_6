import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Locators


class OrderPage(BasePage):

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, data):
        self.wait_for_element_visible(Locators.NAME_INPUT)
        self.send_keys_to_element(Locators.NAME_INPUT, data['name'])
        self.send_keys_to_element(Locators.SURNAME_INPUT, data['surname'])
        self.send_keys_to_element(Locators.ADDRESS_INPUT, data['address'])
        self.send_keys_to_element(Locators.METRO_SELECT, data['metro'])
        self.wait_and_click(Locators.metro_option(data['metro']))
        self.send_keys_to_element(Locators.PHONE_INPUT, data['phone'])
        self.wait_and_click(Locators.NEXT_BUTTON)

    @allure.step("Проверить появление второй формы")
    def is_second_form_opened(self):
        return self.wait_for_element_visible(Locators.RENT_HEADER).is_displayed()

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, data):
        self.send_keys_to_element(Locators.DATE_INPUT, data['date'])
        self.click_on_element(Locators.RENT_HEADER)
        self.wait_and_click(Locators.RENTAL_PERIOD_DROPDOWN)
        self.wait_and_click(Locators.rental_period_option(data['rental_period']))
        self.wait_and_click(Locators.color_checkbox(data['color']))
        if data['comment']:
            self.send_keys_to_element(Locators.COMMENT_INPUT, data['comment'])
        self.wait_and_click(Locators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ") 
    def confirm_order(self):
        self.wait_for_element_visible(Locators.CONFIRM_MODAL)
        self.wait_and_click(Locators.CONFIRM_YES_BUTTON)

    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text_of_element(Locators.SUCCESS_MESSAGE)
