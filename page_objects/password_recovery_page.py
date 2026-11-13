from selenium.webdriver.support import expected_conditions as EC
import allure

from page_objects import BasePage
from locators import PasswordRecoveryLocators


class PasswordRecoveryPage(BasePage):
    locators = PasswordRecoveryLocators()

    @allure.step("Перейти на страницу восстановления пароля")
    def open_recovery_page(self):
        self.click(self.locators.button_login)
        self.click(self.locators.password_recovery_link)

    @allure.step("Ввести e-mail {email}")
    def enter_email(self, email):
        self.send_keys(self.locators.field_email, email)

    @allure.step("Нажать «Восстановить»")
    def click_restore(self):
        self.click(self.locators.button_restore)

    @allure.step("Дождаться формы нового пароля")
    def wait_new_password_form(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.button_show_password))

    @allure.step("Переключить видимость пароля")
    def toggle_password_visibility(self):
        self.click(self.locators.button_show_password)

    @allure.step("Прочитать значение поля e-mail")
    def get_email_value(self):
        el = self.wait.until(EC.presence_of_element_located(self.locators.field_email))
        return el.get_attribute("value")

    @allure.step("Прочитать type поля пароля")
    def get_password_type(self):
        el = self.wait.until(EC.presence_of_element_located(self.locators.password_field))
        return el.get_attribute("type")

    def is_field_focused(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return document.activeElement === arguments[0];", el)

    @allure.step("Проверить, что поле пароля в фокусе")
    def is_password_field_focused(self):
        return self.is_field_focused(self.locators.password_field)