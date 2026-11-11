from selenium.webdriver.support import expected_conditions as EC
from page_objects import BasePage
from locators import LoginLocators, PersonalAccountLocators
from config import URL_AUTHORIZATION_PAGE


class PersonalAccountPage(BasePage, LoginLocators, PersonalAccountLocators):
    def open_personal_account(self):
        self.click(self.personal_account_link)

    def open_order_history(self):
        self.click(self.order_history)

    def exit(self):
        self.click(self.personal_account_link)
        self.click(self.button_exit)
        self.wait.until(EC.url_to_be(URL_AUTHORIZATION_PAGE))

    def is_login_form_visible(self):
        return self.is_element_present(self.button_login, timeout=10)

    def is_logged_in(self, timeout=10):
        return self.is_element_present(self.button_exit, timeout=timeout)