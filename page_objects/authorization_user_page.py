from selenium.webdriver.support import expected_conditions as EC
import allure

from page_objects import BasePage
from locators import LoginLocators



class AuthorizationUserPage(BasePage):
    locators = LoginLocators() 

    @allure.step("Ввести логин и пароль, войти в аккаунт")
    def authorization_user(self, email, password):
        self.send_keys(self.locators.field_email, email)
        self.send_keys(self.locators.field_password, password)
        self.click(self.locators.button_login)
        self.wait.until(EC.invisibility_of_element_located(self.locators.button_login))
