from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Откройте страницу (теперь правильно внутри функции)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Найдите и нажмите на кнопку Start
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # Дождитесь появления текста "Hello World!"
    wait = WebDriverWait(driver, 10)
    hello_text_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # Сделайте скриншот страницы
    driver.save_screenshot("lesson6/screenshots/"
                           "dynamic_loading_screenshot.png")

    # Проверьте, что появившийся текст равен "Hello World!"
    actual_text = hello_text_element.text
    assert actual_text == "Hello World!", (
     f"Expected 'Hello World!', but got '{actual_text}'"
    )

    driver.quit()


test_dynamic_loading()
