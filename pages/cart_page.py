from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from base.base_page import BasePage


class CartPage(BasePage):
    """
    Sepet sayfasıyla ilgili işlemleri gerçekleştirmek için kullanılan sayfa sınıfı.
    """
    checkout_button = (By.ID, 'checkout')
    item_name = (By.CLASS_NAME, 'inventory_item_name')
    remove_item_button = 'remove-sauce-labs-{}'

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        """
        Sayfanın yüklenmesini bekler.
        """
        self.wait.until(ec.visibility_of_element_located(self.checkout_button))
        self.wait.until(ec.visibility_of_element_located(self.item_name))

    def click_checkout_button(self):  #  Checkout butonuna tıklar.
        self.driver.find_element(*self.checkout_button).click()

    def get_item_name(self):  #  Ürünün adını alır.
        return self.driver.find_element(*self.item_name).text

    def click_remove_item(self, product_name):  #  Belirtilen ürünü sepetten kaldırmak için ilgili butona tıklar.
        self.driver.find_element(By.ID, self.remove_item_button.format(product_name)).click()

    def is_product_removed(self, product_name):  #  Belirtilen ürünün sepetten kaldırılıp kaldırılmadığını kontrol eder.
        return not self.is_element_present((By.ID, self.remove_item_button.format(product_name)))

