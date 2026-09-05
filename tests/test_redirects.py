import allure

from pages.main_page import MainPage
from data import Urls


@allure.epic("Яндекс.Самокат")
@allure.feature("Переходы по логотипам на главной странице")
class TestRedirects:

    @allure.title("Клик по логотипу Самоката ведет на главную страницу Самоката.")
    @allure.description("Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)

        with allure.step("Принять cookies"):
            main_page.accept_cookies_if_present()

        with allure.step("Нажать кнопку 'Заказать' в шапке страницы"):
            main_page.click_order_button_top()

        with allure.step("Кликнуть по логотипу Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить, что произошёл переход на главную страницу"):
            assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title("Клик по логотипу Яндекса ведет на главную страницу Дзена.")
    @allure.description("Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        original_window = driver.current_window_handle
    
        with allure.step("Принять cookies"):
                main_page.accept_cookies_if_present()

        with allure.step("Кликнуть по логотипу Яндекса"):
                main_page.click_yandex_logo()

        with allure.step("Переключиться на новую вкладку"):
                main_page.switch_to_new_window()

        with allure.step("Дождаться редиректа на страницу Дзена"):
                main_page.wait_for_url_contains(Urls.DZEN_HOST)

        with allure.step("Проверить, что открылась страница Дзена"):
                assert Urls.DZEN_HOST in main_page.get_current_url()

        with allure.step("Закрыть текущую вкладку Дзена и вернуться на главную"):
                main_page.switch_to_original_window(original_window)