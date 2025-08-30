from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))
    
    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.driver.find_element(*button_locator)
        button.click()
    
    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda driver: driver.find_element(*self.result_display).text != ""
        )
        return self.driver.find_element(*self.result_display).text