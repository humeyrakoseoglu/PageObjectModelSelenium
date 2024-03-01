import time

from selenium.webdriver.common.by import By

from base.base_test import BaseTest
from pages.login_page import LoginPage


class TestPom(BaseTest):
    driver = 'chrome'

    def test_pom(self):
        """
        POM testlerini gerçekleştirmek için kullanılan bir test metodu.
        """
        login = LoginPage(self.driver)
        login.enter_user_name('standard_user')
        login.enter_password('secret_sauce')
        time.sleep(2)
        home_page = login.click_login_button()

        name = home_page.get_product_name()
        # Ürünü sepete ekle
        time.sleep(2)
        home_page.click_add_to_cart('backpack')
        time.sleep(1)
        home_page.click_add_to_cart('bike-light')

        # Sepete git
        time.sleep(2)
        cart_page = home_page.click_cart_button()
        # Sepetteki ürünün adını al
        cart_name = cart_page.get_item_name()
        # Ürünün doğru bir şekilde sepete eklenip eklenmediğini kontrol et
        self.assertEqual(name, cart_name, "Product is not added to cart")
        time.sleep(2)
        # Ürünü sepetten kaldır
        cart_page.click_remove_item('backpack')
        # Ürünün başarıyla kaldırılıp kaldırılmadığını kontrol et
        self.assertTrue(cart_page.is_product_removed('backpack'))
        time.sleep(2)