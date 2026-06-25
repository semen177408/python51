from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    # 1. Откройте страницу в Google Chrome
    driver = webdriver.Chrome()
    driver.get("""
        https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html""")

    # 2. В поле ввода по локатору #delay введите значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажмите на кнопки: 7, +, 8, =
    buttons = {
        "7": "//span[text()='7']",
        "+": "//span[text()='+']",
        "8": "//span[text()='8']",
        "=": "//span[text()='=']"
    }

    for button_text, xpath in buttons.items():
        button = driver.find_element(By.XPATH, xpath)
        button.click()

    # 4. Проверьте, что в окне отобразится результат 15 через 45 секунд
    result_locator = (By.CSS_SELECTOR, ".screen")

    # Ожидаем, что результат появится и будет равен 15
    wait = WebDriverWait(driver, 50)  # ждем максимум 50 секунд

    def result_equals_15(driver):
        result_element = driver.find_element(*result_locator)
        result_text = result_element.text.strip()
        return result_text == "15"

    wait.until(result_equals_15)

    # Проверка через assert
    result_element = driver.find_element(*result_locator)
    assert result_element.text.strip() == "15", \
        (f"Ожидался результат 15, получен {result_element.text}")

    # Закрываем браузер
    driver.quit()
