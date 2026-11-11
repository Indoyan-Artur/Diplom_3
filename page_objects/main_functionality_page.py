from selenium.webdriver.support import expected_conditions as EC
from page_objects import BasePage
from locators import MainFunctionalityLocators


class MainFunctionalityPage(BasePage, MainFunctionalityLocators):
    def switch_to_constructor(self):
        self.click(self.button_constructor)

    def transition_to_order_feed(self):
        self.click(self.button_order_feed)

    def open_ingredient_details(self):
        self.click(self.ingredient)

    def close_ingredient_modal(self):
        self.click(self.ingredient_modal_close_button)
        self.wait.until(EC.invisibility_of_element_located(self.ingredient_details))

    def get_ingredient_details_text(self):
        return self.get_text(self.ingredient_details)

    def drag_ingredient_to_burger(self):
        self.drag_and_drop(self.ingredient, self.bun_slot_top)

    def get_counter_value(self):
        return self.wait.until(EC.visibility_of_element_located(self.counter_number)).text

    def place_order(self):
        self.click(self.button_place_an_order)

    def get_order_preparing_text(self):
        return self.get_text(self.order_preparing_text)