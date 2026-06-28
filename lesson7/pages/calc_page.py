from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        # Увеличиваем таймаут для калькулятора

        # Локаторы
        self._delay_input_locator = (By.CSS_SELECTOR, "#delay")
        self._screen_locator = (By.CSS_SELECTOR, ".screen")

        # XPath для кнопок
        self._buttons = {
            "7": "//span[text()='7']",
            "+": "//span[text()='+']",
            "8": "//span[text()='8']",
            "=": "//span[text()='=']",
        }

    def open(self, url: str):
        self.driver.get(url)

    def set_delay(self, delay: int):
        input_el = self.driver.find_element(*self._delay_input_locator)
        input_el.clear()
        input_el.send_keys(str(delay))

    def click_buttons(self, sequence: list[str]):
        for button_text in sequence:
            if button_text not in self._buttons:
                raise ValueError(f"Неизвестная кнопка: {button_text}")
            xpath = self._buttons[button_text]
            button = self.driver.find_element(By.XPATH, xpath)
            button.click()

    def wait_for_result(self, expected_result: str, timeout: int = 60):
        def condition(driver):
            result_el = driver.find_element(*self._screen_locator)
            return result_el.text.strip() == expected_result

        self.wait.until(condition)

    def get_result(self) -> str:
        return self.driver.find_element(*self._screen_locator).text.strip()
