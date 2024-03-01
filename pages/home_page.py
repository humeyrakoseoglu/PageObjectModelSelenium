from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


class HomePage(BasePage):
    """
    Ana sayfa işlemleri için kullanılan sayfa sınıfı.
    """
    add_to_cart_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart_bike = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_to_cart_shirt = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    add_to_cart = 'add-to-cart-sauce-labs-{}'
    product = "//div[@class='inventory_item_name' and contains(text(), '{}')]"
    cart_button = (By.ID, 'shopping_cart_container')
    product_name = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self): # Sayfanın yüklenmesini bekler.
        self.wait.until(ec.visibility_of_element_located(self.cart_button))

    #her bir ürünü sepete ayrı ayrı eklemek için tıklama methodları:
    def click_add_to_cart_backpack(self):
        self.driver.find_element(*self.add_to_cart_backpack).click()

    def click_add_to_cart_bike(self):
        self.driver.find_element(*self.add_to_cart_bike).click()

    """
    Üsttekiler gibi her ürün için ayrı metot yerine tek bir metot ile bunu gerçekleştirelim
    Belirtilen ürünü sepete eklemek için ilgili butona tıklar ve ProductPage'e yönlendirir.
    """
    def click_add_to_cart(self, product_name):
        self.driver.find_element(By.ID, self.add_to_cart.format(product_name)).click()

    def click_product(self, product_name):  # Belirtilen ürün adına sahip olan ürüne tıklar ve ProductPage'e yönlendirir.
        self.driver.find_element(By.XPATH, self.product.format(product_name)).click()
        return ProductPage(self.driver)

    def click_cart_button(self): # Sepet butonuna tıklar ve CartPage'e yönlendirir.
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)

    def get_product_name(self): # İlk ürünün adını alır ve döndürür.
        return self.driver.find_elements(*self.product_name)[0].text