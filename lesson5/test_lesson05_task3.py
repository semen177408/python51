from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")
    current_url = driver.current_url

    print(f"Текущая страница: {current_url}")
    print(f"Всего найдено ссылок: {len(links)}")
    print("\nПроверяем, есть ли ссылка на текущую страницу:")

    # Проверяем, есть ли среди ссылок текущий URL
    has_self_link = False
    for link in links:
        href = link.get_attribute("href")
        if href == current_url:
            has_self_link = True
            print(f"Найдена ссылка на себя: {href}")
            break

    if not has_self_link:
        print("Ссылка на себя ОТСУТСТВУЕТ (это правильно для httpbin.org)")

    print("\nВсе ссылки на странице:")
    for i, link in enumerate(links, 1):
        href = link.get_attribute("href")
        print(f"  {i}. Текст: '{link.text}' -> {href}")

    driver.quit()


if __name__ == "__main__":
    test_multiple_elements()
