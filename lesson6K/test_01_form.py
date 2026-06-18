from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation():
    """
    Автотест для проверки валидации формы на странице
    https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    """
    driver = webdriver.Edge()  # Открытие страницы в Edge
    driver.get(
       "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Явное ожидание загрузки первого поля
    wait = WebDriverWait(driver, 5)

    # 2. Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")  # пустое поле
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # 3. Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 4. Проверка подсветки поля Zip code (подсвечено красным)
    zip_element = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code")))
    assert "danger" in zip_element.get_attribute("class"), \
        "Zip code должен быть подсвечен красным (класс danger)"

    # 5. Проверка остальных полей (подсвечено зелёнм)
    other_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]
    # Ждем, пока элемент найдется и получит нужный класс
    for field_name in other_fields:
        element = wait.until(
                    EC.presence_of_element_located((By.ID, field_name)))
    assert "success" in element.get_attribute("class"), \
        f"Поле {field_name} должно быть подсвечено зелёным (класс success)"

    driver.quit()
