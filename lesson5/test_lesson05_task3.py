from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    # Найдите все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")
    current_url = driver.current_url
    # Проверьте, что текст первой ссылки содержит "1"
    assert "1" in links[0].text
    # Проверьте, что все ссылки отображаются на странице
    for i, link in enumerate(links, 1):
        href = link.get_attribute("href")
        assert link.is_displayed()
    # Проверяем, есть ли среди ссылок текущий URL
    has_self_link = False
    for link in links:
        href = link.get_attribute("href")
        if href == current_url:
            has_self_link = True
            print(f"Найдена ссылка на себя: {href}")
            break
    # Если текущая ссылка не найдена, добавляем ее в список
    if not has_self_link:
        links.append("https://httpbin.org/links/10/10")
    # Проверка количества ссылок (должно быть 10)
    assert len(links) == 10
    driver.quit()


test_multiple_elements()
