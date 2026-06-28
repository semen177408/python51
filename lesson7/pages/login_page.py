from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATORS = {
        "username": (By.NAME, "user-name"),
        "password": (By.NAME, "password"),
        "login_button": (By.NAME, "login-button"),
        "inventory_list": (By.CLASS_NAME, "inventory_list"),
    }

    def open(self, url="https://www.saucedemo.com/"):
        self.driver.get(url)

    def login(self, username="standard_user", password="secret_sauce"):
        username_field = self.wait_for_element(self.LOCATORS["username"])
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.find_element(self.LOCATORS["password"])
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.find_element(self.LOCATORS["login_button"])
        login_button.click()

        # Ожидание загрузки главной страницы
        self.wait_for_element(self.LOCATORS["inventory_list"])
