from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_objects import BasePage
from locators import MainFunctionalityLocators, PersonalAccountLocators, OrderFeedLocators


class OrderFeedPage(BasePage, MainFunctionalityLocators, PersonalAccountLocators, OrderFeedLocators):
    def transition_to_order_feed(self):
        self.click(self.button_order_feed)

    def switch_to_constructor(self):
        self.click(self.button_constructor)

    def dragging_an_ingredient(self):
        self.drag_and_drop(self.ingredient, self.bun_slot_top)

    def order_placement(self):
        self.click(self.button_place_an_order)

    def close_the_details(self):
        self.click(self.button_close)

    def click_to_order(self):
        self.click(self.order)

    def tab(self):
        self.tab_from_field()

    def click_personal_account(self):
        self.click(self.personal_account_link)

    def click_history_of_orders(self):
        self.click(self.button_order_history)

    def number_of_orders_today(self):
        return int(self.order_number_fixation(self.quantity_for_today))

    def number_of_orders_over_time(self):
        return int(self.order_number_fixation(self.order_feed_number))

    def get_order_number(self):
        self.wait.until(EC.presence_of_element_located(self.order_preparing_text))
        first = self.order_number_fixation(self.order_number)
        try:
            WebDriverWait(self.driver, 10).until(lambda d: self.order_number_fixation(self.order_number) != first)
        except TimeoutException:
            pass  
        return int(self.order_number_fixation(self.order_number))

    def get_feed_order_numbers(self):
        return [int(el.text.strip().lstrip('#'))
                for el in self.driver.find_elements(*self.order_numbers_in_line)]

    def wait_order_in_feed(self, order_number, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda d: order_number in self.get_feed_order_numbers())

    def order_details(self):
        return self.is_element_present(self.order_details_box)

    def order_in_story(self):
        elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[starts-with(text(), '#')]")))
        return [int(el.text.lstrip('#')) for el in elements]

    def wait_counter_reached(self, locator, min_value, timeout=20):
        el = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, timeout).until(lambda d: int(el.text) >= min_value)