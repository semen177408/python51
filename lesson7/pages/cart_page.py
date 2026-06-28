from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATORS = {
        "checkout_button": (By.NAME, "checkout")
    }

    def click_checkout(self):
        # Теперь метод находится внутри класса и имеет правильный отступ
        self.driver.find_element(*self.LOCATORS["checkout_button"]).click()
