from selenium.webdriver.support import expected_conditions as EC
from page_objects import BasePage
from locators import PasswordRecoveryLocators


class PasswordRecoveryPage(BasePage, PasswordRecoveryLocators):
    def open_recovery_page(self):
        self.click(self.button_login)
        self.click(self.password_recovery_link)

    def enter_email(self, email):
        self.send_keys(self.field_email, email)

    def click_restore(self):
        self.click(self.button_restore)

    def wait_new_password_form(self):
        self.wait.until(EC.visibility_of_element_located(self.button_show_password))

    def toggle_password_visibility(self):
        self.click(self.button_show_password)

    def get_email_value(self):
        el = self.wait.until(EC.presence_of_element_located(self.field_email))
        return el.get_attribute("value")

    def get_password_type(self):
        el = self.wait.until(EC.presence_of_element_located(self.password_field))
        return el.get_attribute("type")

    def is_field_focused(self, locator):
        """Поле активно: на нём стоит фокус (CSS :focus и даёт «подсветку»)."""
        el = self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.execute_script(
            "return document.activeElement === arguments[0];", el
        )