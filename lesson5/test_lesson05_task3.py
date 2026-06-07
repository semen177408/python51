import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.xfail("Баг: Ссылок 9, а не 10")
def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")

    # Проверка количества ссылок
    assert len(links) == 10

    # Проверка, что все ссылки отображаются
    for link in links:
        assert link.is_displayed()

    # Проверка текста первой ссылки
    assert "1" in links[0].text

    driver.quit()
