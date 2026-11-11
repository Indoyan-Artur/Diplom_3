from selenium.webdriver.support import expected_conditions as EC
from page_objects import BasePage
from locators import LoginLocators



class AuthorizationUserPage(BasePage, LoginLocators):
    def authorization_user(self, email, password):
        self.send_keys(self.field_email, email)
        self.send_keys(self.field_password, password)
        self.click(self.button_login)
        self.wait.until(EC.invisibility_of_element_located(self.button_login))
