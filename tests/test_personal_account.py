import allure
from page_objects import PersonalAccountPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.story("Вход, история заказов, выход")
    def test_personal_account_flow(self, authorization_user, browser):
        account = PersonalAccountPage(browser)
        account.open_()
        account.open_personal_account()

        assert "/account" in account.get_current_url(), f"После клика на Личный кабинет ожидали /account, получили: {account.get_current_url()}"
       
        account.open_order_history()
       
        assert "/feed" in account.get_current_url(), f"После клика на История заказов ожидали /feed, получили: {account.get_current_url()}"
        
        account.exit()
       
        assert account.is_login_form_visible(), "После выхода ждем страницу выхода"