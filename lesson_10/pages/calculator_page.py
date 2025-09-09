from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class CalculatorPage(BasePage):
    """
    Страница калькулятора
    
    Attributes:
        DELAY_INPUT: Локатор поля задержки
        RESULT_DISPLAY: Локатор дисплея результата
    """
    
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку: {delay_value} секунд")
    def set_delay(self, delay_value: int) -> None:
        """
        Устанавливает значение задержки
        
        Args:
            delay_value: Значение задержки в секундах
        """
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    @allure.step("Нажать кнопку: {button_text}")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку калькулятора
        
        Args:
            button_text: Текст на кнопке
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Получить результат вычислений")
    def get_result(self, timeout: int = 60) -> str:
        """
        Получает результат вычислений с ожиданием
        
        Args:
            timeout: Таймаут ожидания в секундах
            
        Returns:
            str: Результат вычислений
        """
        # Ждем, пока результат не станет отличным от текущего выражения
        wait = WebDriverWait(self.driver, timeout)
        
        # Ожидаем, пока результат не станет числом (не будет содержать операторов)
        def result_is_calculated(driver):
            result_text = driver.find_element(*self.RESULT_DISPLAY).text
            # Проверяем, что результат - число (не содержит +, -, *, /, =)
            return result_text and not any(op in result_text for op in ['+', '-', '*', '/', '='])
        
        wait.until(result_is_calculated)
        result = self.driver.find_element(*self.RESULT_DISPLAY).text
        self.take_screenshot(f"calculator_result_{result}")
        return result