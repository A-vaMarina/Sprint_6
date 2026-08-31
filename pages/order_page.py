from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Первая страница заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_SELECT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[@class='select-search__select']//li[contains(text(), '{station}')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_OPTION = (By.XPATH, "//div[@class='react-datepicker__day--{day}']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-control']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='{period}']")
    COLOR_CHECKBOX = (By.ID, "{color}")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and text()='Заказ оформлен']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_first_form(self, name, surname, address, metro_station, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)

        self.click(self.METRO_SELECT)
        metro_locator = (By.XPATH, f"//div[@class='select-search__select']//li[contains(text(), '{metro_station}')]")
        self.click(metro_locator)

        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment=None):
        # Дата
        self.click(self.DATE_INPUT)
        date_locator = (By.XPATH, f"//div[@class='react-datepicker__day--{date}']")
        self.click(date_locator)

        # Период аренды
        self.click(self.RENTAL_PERIOD)
        period_locator = (By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{rental_period}']")
        self.click(period_locator)

        # Цвет
        color_locator = (By.ID, color)
        self.click(color_locator)

        # Комментарий (опционально)
        if comment:
            self.send_keys(self.COMMENT_INPUT, comment)

        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text