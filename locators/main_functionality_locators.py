from selenium.webdriver.common.by import By


class MainFunctionalityLocators:
    button_constructor = (By.XPATH, "//a[normalize-space(.) = 'Конструктор']")
    button_order_feed = (By.XPATH, "//a[normalize-space(.) = 'Лента Заказов']")
    ingredient = (By.CSS_SELECTOR, "a[href='/ingredient/691577430cc94f001a65b859']")
    ingredient_details = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')][.//h2[normalize-space(text()) = 'Детали ингредиента']]")
    ingredient_modal_close_button = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
    bun_slot_top = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]/li[1]")
    counter_number = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    button_place_an_order = (By.XPATH, "//button[normalize-space(.) = 'Оформить заказ']")
    order_preparing_text = (By.XPATH, "//p[normalize-space(text()) = 'Ваш заказ начали готовить']")