from selenium.webdriver.common.by import By


class OrderFeedLocators:
    button_order_history = (By.XPATH, "//a[contains(@class, 'text_type_main-medium') and normalize-space(text()) = 'История заказов']")
    order_feed_number = (By.XPATH, "//p[contains(., 'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    quantity_for_today = (By.XPATH, "//p[contains(., 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    order_number = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow') and following-sibling::p[normalize-space() = 'идентификатор заказа']]")
    button_close = (By.CSS_SELECTOR, "button[class*='Modal_modal__close_modified']")
    order_numbers_in_line = (By.CSS_SELECTOR, "li.text_type_digits-default.mb-2")
    order_details_box = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    order = (By.CSS_SELECTOR, "li[class*='OrderHistory_listItem'] a")
