from page_objects import BasePage
from locators import RegistrationLocators


class RegistrePage(BasePage, RegistrationLocators):
    def registre(self, name, emile, password):
        self.send_keys(self.field_name, name)
        self.send_keys(self.field_email, emile)
        self.send_keys(self.field_password, password)
        self.click(self.button_register)