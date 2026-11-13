from selenium.webdriver.support import expected_conditions as EC
import allure

from page_objects import BasePage
from locators import MainFunctionalityLocators


class MainFunctionalityPage(BasePage):
    locators = MainFunctionalityLocators() 

    @allure.step("Перейти в Конструктор")
    def switch_to_constructor(self):
        self.click(self.locators.button_constructor)

    @allure.step("Перейти в раздел «Лента заказов»")
    def transition_to_order_feed(self):
        self.click(self.locators.button_order_feed)

    @allure.step("Открыть карточку ингредиента")
    def open_ingredient_details(self):
        self.click(self.locators.ingredient)

    @allure.step("Закрыть карточку ингредиента")
    def close_ingredient_modal(self):
        self.click(self.locators.ingredient_modal_close_button)
        self.wait.until(EC.invisibility_of_element_located(self.locators.ingredient_details))

    @allure.step("Прочитать текст карточки ингредиента")
    def get_ingredient_details_text(self):
        return self.get_text(self.locators.ingredient_details)

    @allure.step("Перетащить ингредиент в слот бургера")
    def drag_ingredient_to_burger(self):
        self.drag_and_drop(self.locators.ingredient, self.locators.bun_slot_top)

    @allure.step("Прочитать значение счётчика")
    def get_counter_value(self):
        return self.wait.until(EC.visibility_of_element_located(self.locators.counter_number)).text

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(self.locators.button_place_an_order)

    @allure.step("Прочитать текст статуса «Заказ готовится»")
    def get_order_preparing_text(self):
        return self.get_text(self.locators.order_preparing_text)