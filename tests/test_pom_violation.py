import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Bu sınıfı POM kurallarına göre yeniden yazacağız

class TestPomViolation(unittest.TestCase):

    def test_pom_violation(self):
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()

        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        time.sleep(2)
        driver.find_element(By.ID, 'login-button').click()
        name = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')[0].get_attribute('name')
        time.sleep(2)
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        cart_name = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')[0].get_attribute('name')
        self.assertEqual(name, cart_name, "Product is not added to cart")
        time.sleep(5)