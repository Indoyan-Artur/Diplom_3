import allure
from page_objects import PasswordRecoveryPage
from test_data import EMAIL
from config import URL_FORGOT_PASSWORD


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления, ввод почты, показ пароля активирует поле")
    def test_password_recovery_flow(self, browser):
        self.password = PasswordRecoveryPage(browser)
        self.password.open_()

        self.password.open_recovery_page()

        assert URL_FORGOT_PASSWORD in self.password.get_current_url(), f"Ожидали {URL_FORGOT_PASSWORD}, получили: {self.password.get_current_url()}"

        self.password.enter_email(EMAIL["email"])

        assert self.password.get_email_value() == EMAIL["email"], f"В поле ожидали {EMAIL['email']}, получили: {self.password.get_email_value()}"
        
        self.password.click_restore()
        self.password.wait_new_password_form()

        self.password.toggle_password_visibility()
    
        assert self.password.get_password_type() == "text", f"После клика ожидаем (type='text'), получили: {self.password.get_password_type()}"

        assert self.password.is_password_field_focused(), "После клика «показать пароль» поле должно стать активным (получить фокус)"