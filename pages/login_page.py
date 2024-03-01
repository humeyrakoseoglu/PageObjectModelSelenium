from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    """
    Giriş sayfası işlemlerini gerçekleştirmek için kullanılan sayfa sınıfı.
    """

    user_name = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_page_load(self): # Sayfanın yüklenmesini bekler.
        self.wait.until(ec.visibility_of_element_located(self.user_name))
        self.wait.until(ec.visibility_of_element_located(self.password))
        self.wait.until(ec.visibility_of_element_located(self.login_button))

    def enter_user_name(self, name): # Kullanıcı adı girişini yapar.
        self.driver.find_element(*self.user_name).send_keys(name)

    def enter_password(self, password): # Şifre girişini yapar.
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self): # Giriş butonuna tıklar ve anasayfaya yönlendirir.
        self.driver.find_element(*self.login_button).click()
        return HomePage(self.driver)