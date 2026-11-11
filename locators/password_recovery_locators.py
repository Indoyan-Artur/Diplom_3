from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    button_login = (By.XPATH, "//*[normalize-space(text())='Войти в аккаунт']")
    password_recovery_link = (By.XPATH, "//*[normalize-space(text())='Восстановить пароль']")
    field_email = (By.CLASS_NAME, "input__textfield")
    button_restore = (By.XPATH, "//*[normalize-space(text())='Восстановить']")
    button_show_password = (By.CSS_SELECTOR, "div.input__icon-action")
    password_field = (By.NAME, "Введите новый пароль")

    overlay = (By.CSS_SELECTOR, ".Modal_modal_overlay")

   