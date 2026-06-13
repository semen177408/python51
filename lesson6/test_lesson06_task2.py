from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Cookie для пользователя 1
    user1_cookies = [
        {'name': "SESSION",
         'value': 'NjUxNDBmZTEtMzM5ZS00MzZhLWJiNTQtN2Q4YTdkMGUxNjNl',
         'domain': 'gitflic.ru'}
    ]

    # Cookie для пользователя 2
    user2_cookies = [
        {'name': "SESSION",
         'value': 'NDQ2ODc1MDktNjZjYy00NzJmLTgwYTItYzQ1YzJjNmQ3MTI0',
         'domain': 'gitflic.ru'},
    ]

    # Шаг 1-5: Работа с пользователем 1
    # Шаг 1: Открываем главную страницу
    driver.get("https://gitflic.ru/")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # Шаг 2: Устанавливаем cookie пользователя 1

    for cookie in user1_cookies:
        driver.add_cookie(cookie)
    # Шаг 3: Обновляем страницу
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Шаг 4: Переходим на страницу пользователя 1
    # URL страницы профиля пользователя 1
    user1_profile_url = "https://gitflic.ru/user/170874"
    driver.get(user1_profile_url)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Шаг 5: Сохраняем текущий URL пользователя 1
    url_user1 = driver.current_url

    # Шаг 6: Разлогиниваемся (очищаем куки)
    driver.delete_all_cookies()

    # Шаг 7-10: Работа с пользователем 2
    # Шаг 7: Устанавливаем cookie пользователя 2
    driver.get("https://gitflic.ru/")
    # Сначала переходим на сайт, чтобы установить cookie
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    for cookie in user2_cookies:
        driver.add_cookie(cookie)

    # Шаг 8: Обновляем страницу
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Шаг 9: Переходим на страницу пользователя 2
    user2_profile_url = "https://gitflic.ru/user/740817"
    driver.get(user2_profile_url)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Шаг 10: Сохраняем текущий URL пользователя 2
    url_user2 = driver.current_url

    # Шаг 11: Проверяем, что URL различаются
    assert url_user1 != url_user2, f"""
    URL одинаковые: {url_user1} == {url_user2}"""

    driver.quit()


test_session_storage_auth()
