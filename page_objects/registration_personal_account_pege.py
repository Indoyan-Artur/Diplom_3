import allure

from page_objects import BasePage
from locators import RegistrationLocators


class RegistrePage(BasePage):
    locators = RegistrationLocators()

    @allure.step("Зарегистрироваться: имя {name}, e-mail {email}, пароль")
    def register(self, name, email, password):
        self.send_keys(self.locators.field_name, name)
        self.send_keys(self.locators.field_email, email)
        self.send_keys(self.locators.field_password, password)
        self.click(self.locators.button_register)