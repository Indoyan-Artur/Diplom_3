import allure
from page_objects import OrderFeedPage


@allure.feature("Раздел «Лента заказов»")
class TestOrderFeed:
    @allure.story("Новый заказ: номер в ленте, счётчики, детали, история")
    def test_order_feed(self, authorization_user, browser):
        page = OrderFeedPage(browser)
        page.open_()
        page.transition_to_order_feed()
        orders_today_before = page.number_of_orders_today()
        orders_over_time_before = page.number_of_orders_over_time()

        page.switch_to_constructor()
        page.dragging_an_ingredient()
        page.order_placement()
        order_number = page.get_order_number()
        page.close_the_details()
        page.transition_to_order_feed()
        page.wait_order_in_feed(order_number)

        assert order_number in page.get_feed_order_numbers(), f"Заказ {order_number} не найден в разделе в работе: {page.get_feed_order_numbers()}"

        page.wait_counter_reached(page.quantity_for_today, orders_today_before + 1)

        assert page.number_of_orders_today() >= orders_today_before + 1, f"Счётчик за сегодня не вырос: было {orders_today_before}, стало {page.number_of_orders_today()}"
        
        page.wait_counter_reached(page.order_feed_number, orders_over_time_before + 1)
        
        assert page.number_of_orders_over_time() >= orders_over_time_before + 1, f"Счётчик за всё время не вырос: было {orders_over_time_before}, стало {page.number_of_orders_over_time()}"

        page.click_to_order()

        assert page.order_details(), "Не открылось окно деталей заказа"

        page.tab()
        page.click_personal_account()
        page.click_history_of_orders()

        assert order_number in page.order_in_story(), f"Заказ {order_number} не найден в Истории заказов"