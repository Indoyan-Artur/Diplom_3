from selenium.webdriver.common.by import By


class LoginLocators:
    field_email = (By.XPATH, "//input[contains(@class, 'input__textfield') and @type = 'text']")
    field_password = (By.XPATH, "//input[contains(@class, 'input__textfield') and @type = 'password']")
    button_login = (By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text() = 'Войти']")