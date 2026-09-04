import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import UserData


@allure.epic('Яндекс.Самокат')
@allure.feature('Оформление заказа')
class TestOrder:

    @allure.title("Успешное оформление заказа через {entry_point} - кнопку 'Заказать'")
    @allure.description('Проверка флоу позитивного сценария для двух точек входа и с двумя наборами данных.')
    @pytest.mark.parametrize('entry_point, user_data', [('top', UserData.USER_1), ('bottom', UserData.USER_2)])
    def test_successful_order(self, driver, entry_point, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Принять куки"):
            main_page.accept_cookies_if_present()

        with allure.step("Нажать на кнопку 'Заказать'"):
            main_page.click_order_button(entry_point)

        with allure.step("Заполнить форму заказа"):
            order_page.fill_first_form(user_data)
            order_page.is_second_form_opened()
            order_page.fill_second_form(user_data)

        with allure.step("Отправить форму заказа"):
            order_page.confirm_order()
        
        with allure.step("Проверить, что появилось окно с сообщением об успешном заказе"):
            assert "Заказ оформлен" in order_page.get_success_message()
