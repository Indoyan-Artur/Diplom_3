from selenium.webdriver.common.by import By


class RegistrationLocators:
    field_name = (By.XPATH, "//label[normalize-space(text()) = 'Имя']/following-sibling::input")
    field_email = (By.XPATH, "//label[normalize-space(text()) = 'Email']/following-sibling::input")
    field_password = (By.XPATH, "//label[normalize-space(text()) = 'Пароль']/following-sibling::input")
    button_register = (By.XPATH, "//button[normalize-space(.) = 'Зарегистрироваться']")