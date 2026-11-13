from selenium.webdriver.support import expected_conditions as EC
import allure

from page_objects import BasePage
from locators import LoginLocators, PersonalAccountLocators
from config import URL_AUTHORIZATION_PAGE


class PersonalAccountPage(BasePage):
    locators = PersonalAccountLocators()
    locators_login = LoginLocators()

    @allure.step("Открыть Личный кабинет")
    def open_personal_account(self):
        self.click(self.locators.personal_account_link)

    @allure.step("Открыть «Историю заказов»")
    def open_order_history(self):
        self.click(self.locators.order_history)

    @allure.step("Выйти из аккаунта")
    def exit(self):
        self.click(self.locators.personal_account_link)
        self.click(self.locators.button_exit)
        self.wait.until(EC.url_to_be(URL_AUTHORIZATION_PAGE))

    @allure.step("Проверить, что видна форма логина")
    def is_login_form_visible(self):
        return self.is_element_present(self.locators_login.button_login, timeout=10)

    @allure.step("Проверить, что пользователь авторизован")
    def is_logged_in(self, timeout=10):
        return self.is_element_present(self.locators.button_exit, timeout=timeout)