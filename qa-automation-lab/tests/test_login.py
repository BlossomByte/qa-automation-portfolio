from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger()

def test_login_flow(page):
    logger.info("Starting test")

    login = LoginPage(page)
    inventory = InventoryPage(page)

    page.goto("https://www.saucedemo.com/")
    logger.info("Opened login page")

    login.login("standard_user", "secret_sauce")
    logger.info("Logged in")

    inventory.products.first.wait_for()

    inventory.add_first_item()
    logger.info("Item added to cart")

    assert inventory.get_cart_count() == "1"
    logger.info("Test passed")