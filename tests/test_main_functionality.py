import allure
from page_objects import MainFunctionalityPage
from config import URL_ORDER_LIST, BASE_URL


@allure.feature("Проверка основного функционала")
class TestMainFunctionality:
    @allure.story("Переходы по клику")
    def test_transitions_to_feed_and_constructor(self, browser):
        page = MainFunctionalityPage(browser)
        page.open_()
        page.transition_to_order_feed()

        assert page.get_current_url() == URL_ORDER_LIST, f"Ожидали {URL_ORDER_LIST}, получили: {page.get_current_url()}"
       
        page.switch_to_constructor()
        
        assert page.get_current_url().rstrip('/') == BASE_URL.rstrip('/'), f"Ожидали {BASE_URL}, получили: {page.get_current_url()}"

    @allure.story("Окно деталей ингредиента")
    def test_ingredient_details_modal(self, browser):
        page = MainFunctionalityPage(browser)
        page.open_()
        page.switch_to_constructor()
        page.open_ingredient_details()
        
        assert "Детали ингредиента" in page.get_ingredient_details_text(), "В окне деталей нет заголовка 'Детали ингредиента'"
        
        page.close_ingredient_modal()

    @allure.story("Добавление ингредиента и оформление заказа")
    def test_add_ingredient_and_place_order(self, authorization_user, browser):
        page = MainFunctionalityPage(browser)
        page.open_()
        page.switch_to_constructor()
        before = int(page.get_counter_value())
        page.drag_ingredient_to_burger()
        after = int(page.get_counter_value())
        
        assert after > before, f"Количество не увеличился: было {before}, стало {after}"