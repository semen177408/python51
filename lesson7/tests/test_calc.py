import pytest
from pages.driver_factory import DriverFactory
from pages.calc_page import CalculatorPage
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="function")
def page():
    driver = DriverFactory.get_driver()
    page = CalculatorPage(driver)
    yield page
    # Опционально: можно сбрасывать страницу или чистить состояние здесь


def test_calc(page: CalculatorPage):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    page.open(url)

    # 1. Устанавливаем задержку 45 секунд
    page.set_delay(45)

    # 2. Нажимаем кнопки: 7, +, 8, =
    page.click_buttons(["7", "+", "8", "="])

    # 3. Ждём и проверяем, что результат равен 15
    page.wait_for_result("15")
    assert page.get_result() == "15", f"Ожидался результат 15,\
          получен {page.get_result()}"


@pytest.fixture(autouse=True, scope="session")
# Закрытие драйвера после теста
def cleanup():
    yield
    DriverFactory.quit_driver()
