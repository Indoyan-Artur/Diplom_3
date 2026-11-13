from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.by import By
import allure

from page_objects import BasePage
from locators import MainFunctionalityLocators, PersonalAccountLocators, OrderFeedLocators


class OrderFeedPage(BasePage):
    locators = OrderFeedLocators()
    locators_main = MainFunctionalityLocators()
    locators_account = PersonalAccountLocators()

    @allure.step("Перейти в раздел «Лента заказов»")
    def transition_to_order_feed(self):
        self.click(self.locators_main.button_order_feed)

    @allure.step("Перейти в Конструктор")
    def switch_to_constructor(self):
        self.click(self.locators_main.button_constructor)

    @allure.step("Перетащить ингредиент в слот бургера")
    def dragging_an_ingredient(self):
        self.drag_and_drop(self.locators_main.ingredient, self.locators_main.bun_slot_top)

    @allure.step("Оформить заказ")
    def order_placement(self):
        self.click(self.locators_main.button_place_an_order)

    @allure.step("Закрыть окно деталей")
    def close_the_details(self):
        self.click(self.locators.button_close)

    @allure.step("Открыть заказ из ленты")
    def click_to_order(self):
        self.click(self.locators.order)

    @allure.step("Переключить вкладку заказа")
    def tab(self):
        self.tab_from_field()

    @allure.step("Перейти в Личный кабинет")
    def click_personal_account(self):
        self.click(self.locators_account.personal_account_link)

    @allure.step("Открыть «Историю заказов»")
    def click_history_of_orders(self):
        self.click(self.locators.button_order_history)

    @allure.step("Прочитать счётчик заказов за сегодня")
    def number_of_orders_today(self):
        return int(self.order_number_fixation(self.locators.quantity_for_today))

    @allure.step("Прочитать счётчик заказов за всё время")
    def number_of_orders_over_time(self):
        return int(self.order_number_fixation(self.locators.order_feed_number))

    @allure.step("Получить номер нового заказа")
    def get_order_number(self):
        self.wait.until(EC.presence_of_element_located(self.locators_main.order_preparing_text))
        first = self.order_number_fixation(self.locators.order_number)
        try:
            WebDriverWait(self.driver, 10).until(lambda d: self.order_number_fixation(self.locators.order_number) != first)
        except TimeoutException:
            pass
        return int(self.order_number_fixation(self.locators.order_number))

    @allure.step("Прочитать номера заказов в ленте")
    def get_feed_order_numbers(self):
        return [int(el.text.strip().lstrip('#'))
                for el in self.driver.find_elements(*self.locators.order_numbers_in_line)]

    @allure.step("Дождаться появления заказа {order_number} в ленте")
    def wait_order_in_feed(self, order_number, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda d: order_number in self.get_feed_order_numbers())

    @allure.step("Проверить, что окно деталей заказа открыто")
    def order_details(self):
        return self.is_element_present(self.locators.order_details_box)

    @allure.step("Прочитать номера заказов в Истории")
    def order_in_story(self):
        elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[starts-with(text(), '#')]")))
        return [int(el.text.lstrip('#')) for el in elements]

    def wait_counter_reached(self, locator, min_value, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda d: int(self.get_text(locator)) >= min_value)

    @allure.step("Дождаться, пока счётчик за сегодня станет не меньше {min_value}")
    def wait_orders_today_reached(self, min_value, timeout=20):
        self.wait_counter_reached(self.locators.quantity_for_today, min_value, timeout)

    @allure.step("Дождаться, пока счётчик за всё время станет не меньше {min_value}")
    def wait_orders_over_time_reached(self, min_value, timeout=20):
        self.wait_counter_reached(self.locators.order_feed_number, min_value, timeout)