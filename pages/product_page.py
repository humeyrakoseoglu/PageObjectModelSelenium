from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductPage(BasePage):
    """
    Ürün sayfası işlemlerini gerçekleştirmek için kullanılan sayfa sınıfı.
    """

    add_to_cart = 'add-to-cart-sauce-labs-{}'
    product_title = (By.CSS_SELECTOR, '.inventory_details_name')
    product_price = (By.CSS_SELECTOR, '.inventory_details_price')
    back_button = (By.CSS_SELECTOR, '#back-to-products')

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart(self, product_name): # Belirtilen ürünü sepete eklemek için ilgili butona tıklar.
        self.driver.find_element(By.ID, self.add_to_cart.format(product_name)).click()
        return ProductPage(self.driver)

    def get_product_title(self): # Ürün başlığını alır.
        return self.driver.find_element(*self.product_title).text

    def get_product_price(self): # Ürün fiyatını  alır.
        return self.driver.find_element(*self.product_price).text

    def click_back_button(self): # Geri butonuna tıklar.
        self.driver.find_element(*self.back_button).click()