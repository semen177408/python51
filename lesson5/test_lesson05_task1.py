from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()

    try:
        # Открыть страницу
        driver.get("https://httpbin.org/")
        original_url = driver.current_url
        print(f"Начальный URL: {original_url}")
        Lin = "//a[contains(@href, 'form') or contains(., 'form')]"

        # Найти ссылку по XPath (более гибкий поиск)
        # Ищем элемент <a>, который содержит слово "form" в любом регистре
        forms_link = WebDriverWait(driver, 10).until(
                                                    EC.element_to_be_clickable
                                                    ((By.XPATH, Lin)))

        print(f"Найдена ссылка: '{forms_link.text}'")
        forms_link.click()

        # Проверяем, что URL изменился на /forms
        WebDriverWait(driver, 5).until(
            EC.url_contains("/forms")
        )
        assert "/forms" in driver.current_url
        print(f"URL после клика: {driver.current_url}")

        # Вернуться назад на главную страницу
        driver.back()

        # Проверяем, что вернулись на исходный URL
        WebDriverWait(driver, 5).until(
            EC.url_to_be(original_url)
        )
        assert driver.current_url == original_url
        print(f"URL после возврата: {driver.current_url}")

        print("Тест пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_navigation()
