from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # Кнопка "да все привыкли"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']")
    FAQ_QUESTIONS = (By.XPATH, "//div[@class='accordion__item']")
    FAQ_QUESTION_BUTTONS = (By.XPATH, "//div[@id='accordion__heading-{index}']")
    FAQ_ANSWER_PANELS = (By.XPATH, "//div[@id='accordion__panel-{index}']/p")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        self.click(self.COOKIE_BUTTON)

    def click_order_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.click(self.ORDER_BUTTON_BOTTOM)

    def get_faq_answer_text(self, index):
        """Получить текст ответа на вопрос по индексу (0-based)"""
        question_button = (By.ID, f"accordion__heading-{index}")
        answer_panel = (By.ID, f"accordion__panel-{index}")

        self.click(question_button)
        # Ждем, пока ответ станет видимым
        self.wait.until(EC.visibility_of_element_located(answer_panel))
        return self.find_element(answer_panel).text

    def click_scooter_logo(self):
        self.click((By.XPATH, "//img[@alt='Scooter']"))

    def click_yandex_logo(self):
        self.click((By.XPATH, "//img[@alt='Yandex']"))