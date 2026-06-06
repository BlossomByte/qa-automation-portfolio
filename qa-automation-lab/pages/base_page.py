import time

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def wait(self, seconds=5):
        time.sleep(seconds)