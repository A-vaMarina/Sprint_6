import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import UserData


@allure.epic('Яндекс.Самокат')
@allure.feature('Заказ самоката')
class TestOrder:
    @allure.title('Проверка флоу позитивного сценария через две точки входа')
    @allure.description("Успешное оформление заказа через кнопку «Заказать» вверху и внизу страницы. Используется два набора тестовых данных.")
    @pytest.mark.parametrize('entry_point, user_data', [('top', UserData.USER_1), ('bottom', UserData.USER_2)])
    def test_successful_order(self, driver, entry_point, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies_if_present()

        if entry_point == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()
    
        order_page.fill_first_form(user_data)
        order_page.is_second_form_opened()
        order_page.fill_second_form(user_data)
        order_page.confirm_order()
        
        assert "Заказ оформлен" in order_page.get_success_message()
        

