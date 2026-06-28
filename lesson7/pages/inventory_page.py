from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    LOCATORS = {
        "backpack_add": (By.NAME, "add-to-cart-sauce-labs-backpack"),
        "tshirt_add": (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "onesie_add": (By.NAME, "add-to-cart-sauce-labs-onesie"),
        "cart_icon": (By.CLASS_NAME, "shopping_cart_link"),
        "cart_list": (By.CLASS_NAME, "cart_list"),
    }

    def add_backpack(self):
        btn = self.find_element(self.LOCATORS["backpack_add"])
        btn.click()

    def add_tshirt(self):
        btn = self.find_element(self.LOCATORS["tshirt_add"])
        btn.click()

    def add_onesie(self):
        btn = self.find_element(self.LOCATORS["onesie_add"])
        btn.click()

    def go_to_cart(self):
        cart_icon = self.find_element(self.LOCATORS["cart_icon"])
        cart_icon.click()
        self.wait_for_element(self.LOCATORS["cart_list"])
