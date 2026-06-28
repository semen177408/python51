class DriverSingleton:
    _instance = None
    _driver = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_driver(self, driver):
        """Устанавливает драйвер извне (из фикстуры)"""
        self._driver = driver

    def get_driver(self):
        if self._driver is None:
            raise RuntimeError("""Драйвер не инициализирован.
                               Вызовите set_driver() в фикстуре.""")
        return self._driver

    def quit_driver(self):
        if self._driver:
            self._driver.quit()
            self._driver = None
