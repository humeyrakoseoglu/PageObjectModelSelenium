import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # BaseTest sınıfının yapıcı metodu.

        # WebDriver'ı başlatmak için get_driver metodu çağrılır
        self.driver = self.get_driver(self.driver)

        # Testin çalıştırılacağı web sitesine gitmek için WebDriver'ı kullan
        self.driver.get('https://www.saucedemo.com/')

        self.driver.maximize_window() # Pencereyi maksimize et

    def get_driver(self, driver):
        """
        Belirtilen driver tipine göre uygun WebDriver'ı döndürür.
        """
        if driver == 'chrome':
            self.driver = webdriver.Chrome()
        elif driver == 'safari':
            self.driver = webdriver.Safari()
        elif driver == 'firefox':
            self.driver = webdriver.Firefox()
        elif driver == 'edge':
            self.driver = webdriver.Edge()
        return self.driver