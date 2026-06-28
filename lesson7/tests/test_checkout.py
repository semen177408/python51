import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from drivers.driver_factory import DriverFactory
from drivers.driver_singleton import DriverSingleton


@pytest.fixture(scope="function")
def driver():
    drv = DriverFactory.create_driver(browser="firefox", headless=False)
    singleton = DriverSingleton()
    singleton.set_driver(drv)
    yield drv
    singleton.quit_driver()


def test_checkout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login()

    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()

    inventory_page.go_to_cart()
    cart_page.click_checkout()

    checkout_page.fill_checkout_form("Семен", "Лавелин", "196634")
    checkout_page.click_continue()

    total = checkout_page.get_total_price()
    expected_total = 58.29

    assert total == expected_total, f"Ожидалась сумма ${expected_total},\
        получено ${total}"
