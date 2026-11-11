from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    personal_account_link = (By.CSS_SELECTOR, "a[href='/account']")
    order_history = (By.CSS_SELECTOR, "a[href='/feed']")
    button_exit = (By.XPATH, "//button[contains(@class, 'text_type_main-medium') and text() = 'Выход']")
