from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница формы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_SELECT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница формы заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    BLACK_CHECKBOX = (By.ID, 'black')
    GRAY_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']",)
    CONFIRM_MODAL = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]",)

    @staticmethod
    def metro_option(station):
        return (By.XPATH, f"//button[contains(@class, 'select-search__option')]//div[text()='{station}']")

    @staticmethod
    def rental_period_option(period):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
