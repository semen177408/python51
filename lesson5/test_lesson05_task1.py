from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()

    # Открыть страницу
    driver.get("https://httpbin.org/")
    original_url = driver.current_url

    # Ожидаем появления кликабельной ссылки на веб-странице
    forms_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "HTML form")))
    forms_link.click()

    # Проверяем, что URL изменился на /forms/post
    WebDriverWait(driver, 5).until(
        EC.url_contains("/forms"))
    assert "/forms" in driver.current_url

    # Вернуться назад на главную страницу
    driver.back()

    # Проверяем, что вернулись на исходный URL
    WebDriverWait(driver, 5).until(
        EC.url_to_be(original_url))
    assert driver.current_url == original_url
    driver.quit()


test_navigation()
