from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from config import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_(self, url=None):
        self.driver.get(url or BASE_URL)

    def click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text

    def get_current_url(self):
        return self.driver.current_url

    def is_element_present(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def order_number_fixation(self, locator, message=""):
        return self.wait.until(EC.presence_of_element_located(locator), message).text

    def tab_from_field(self):
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    #этот тест написан через скрипт поскольку ActionChains не умеет генерировать HTML5 drag-события в Firefox
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        self.driver.execute_script("""
            const source = arguments[0], target = arguments[1];
            const data = new DataTransfer();
            function fire(el, type) {
                const r = el.getBoundingClientRect();
                el.dispatchEvent(new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    clientX: r.left + r.width / 2,
                    clientY: r.top + r.height / 2,
                    dataTransfer: data
                }));
            }
            fire(source, 'dragstart');
            fire(target, 'dragenter');
            fire(target, 'dragover');
            fire(target, 'drop');
            fire(source, 'dragend');
        """, source, target)

