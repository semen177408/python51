from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


class DriverFactory:
    @staticmethod
    def create_driver(browser="firefox", headless=False):
        if browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

        elif browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            # Новый флаг для современных версий Chrome
            driver = webdriver.Chrome(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        return driver
