class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.url = link

    def open(self):
        self.browser.get(self.url)