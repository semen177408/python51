from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_method():
    """Настройка браузера Firefox перед каждым тестом"""
    options = Options()
    # Раскомментируйте для запуска в фоновом режиме
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Шаг 1: Откройте сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Шаг 2: Авторизуйтесь как пользователь standard_user
    username_field = wait.until(
        EC.presence_of_element_located((By.NAME, "user-name"))
    )
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.NAME, "login-button")
    login_button.click()

    # Ожидаем загрузки главной страницы
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Шаг 3: Добавьте в корзину товары
    # Sauce Labs Backpack
    backpack_add = driver.find_element(By.NAME,
                                       "add-to-cart-sauce-labs-backpack")
    backpack_add.click()

    # Sauce Labs Bolt T-Shirt
    tshirt_add = driver.find_element(By.NAME,
                                     "add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt_add.click()

    # Sauce Labs Onesie
    onesie_add = driver.find_element(By.NAME,
                                     "add-to-cart-sauce-labs-onesie")
    onesie_add.click()

    # Шаг 4: Перейдите в корзину
    cart_icon = driver.find_element(By.CLASS_NAME,
                                    "shopping_cart_link")
    cart_icon.click()

    # Ожидаем загрузки страницы корзины
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )

    # Шаг 5: Нажмите Checkout
    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    # Шаг 6: Заполните форму своими данными
    first_name_field = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name_field.send_keys("Семен")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Лавелин")

    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("196634")

    # Шаг 7: Нажмите кнопку Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Ожидаем загрузки страницы с итогами
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_info"))
    )

    # Шаг 8: Прочитайте со страницы итоговую стоимость (Total)
    total_label = driver.find_element(By.CLASS_NAME,
                                      "summary_total_label")
    total_text = total_label.text

    # Извлекаем числовое значение из строки "Total: $XX.XX"
    total_value = total_text.replace("Total: ", "").replace("$", "")
    total_float = float(total_value)

    # Шаг 9: Закройте браузер
    driver.quit()

    # Шаг 10: Проверьте, что итоговая сумма равна $58.29
    expected_total = 58.29
    assert total_float == expected_total, \
        f"Ожидалась сумма ${expected_total}, получено ${total_float}"
