class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.products = page.locator(".inventory_item")
        self.add_to_cart = page.locator("button:has-text('Add to cart')")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_first_item(self):
        self.add_to_cart.first.click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()