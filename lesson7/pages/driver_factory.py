from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    _driver = None

    @classmethod
# Возвращает единственный экземпляр драйвера (Singleton)
    def get_driver(cls) -> webdriver.Chrome:
        if cls._driver is None:
            options = Options()
            # options.add_argument("--headless")  # раскомментируй для headless
            cls._driver = webdriver.Chrome(options=options)
        return cls._driver

    @classmethod
# Завершение драйвера
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
