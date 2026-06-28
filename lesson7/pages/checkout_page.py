from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    LOCATORS = {
        "first_name": (By.ID, "first-name"),
        "last_name": (By.ID, "last-name"),
        "postal_code": (By.ID, "postal-code"),
        "continue_button": (By.ID, "continue"),
        "summary_info": (By.CLASS_NAME, "summary_info"),
        "total_label": (By.CLASS_NAME, "summary_total_label"),
    }

    def fill_checkout_form(self, first_name, last_name, postal_code):
        first_name_field = self.wait_for_element(self.LOCATORS["first_name"])
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.find_element(self.LOCATORS["last_name"])
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.find_element(self.LOCATORS["postal_code"])
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        continue_btn = self.find_element(self.LOCATORS["continue_button"])
        continue_btn.click()
        self.wait_for_element(self.LOCATORS["summary_info"])

    def get_total_price(self) -> float:
        total_label = self.find_element(self.LOCATORS["total_label"])
        text = total_label.text  # "Total: $58.29"
        total_str = text.replace("Total: ", "").replace("$", "")
        return float(total_str)
