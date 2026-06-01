from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # Заполняем поле имени
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Семен Лавелин")

    # Задержка для полной загрузки страницы
    import time
    time.sleep(3)
    Lin2 = "//button[contains(text(), 'Submit order')]"

    # Найдем кнопку отправки формы (по тексту "Submit order")
    # Внимание: кнопка имеет текст "Submit order", не "Submit"
    submit_button = driver.find_element(By.XPATH, Lin2)

    # Кликаем по кнопке
    submit_button.click()

    # Ждем изменения URL (максимум 5 секунд)
    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_changes("https://httpbin.org/forms/post"))

    # Проверяем, что URL изменился
    current_url = driver.current_url
    print(f"Новый URL: {current_url}")

    # Проверяем, что мы перешли на страницу результата
    assert ("https://httpbin.org/post" in current_url
            ), f"Ожидался URL https://httpbin.org/post, получен {current_url}"

    print("Тест пройден успешно!")

    driver.quit()


if __name__ == "__main__":
    test_form_submission()
