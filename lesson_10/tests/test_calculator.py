import pytest
import allure
from pages.calculator_page import CalculatorPage


class TestCalculator:
    """
    Тестовый класс для проверки функциональности калькулятора
    """

    @allure.title("Проверка работы калькулятора с задержкой")
    @allure.description("Тест проверяет корректность вычислений калькулятора с установленной задержкой")
    @allure.feature("Калькулятор")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculator_with_delay(self, browser) -> None:
        """
        Тест работы калькулятора с задержкой
        
        Args:
            browser: Фикстура браузера
        """
        calculator_page = CalculatorPage(browser)
        
        with allure.step("Открытие калькулятора"):
            calculator_page.open()
        
        with allure.step("Установка задержки 3 секунды для быстрого теста"):
            calculator_page.set_delay(3)
        
        with allure.step("Выполнение вычисления 7 + 8"):
            calculator_page.click_button("7")
            calculator_page.click_button("+")
            calculator_page.click_button("8")
            calculator_page.click_button("=")
        
        with allure.step("Проверка результата"):
            result = calculator_page.get_result(timeout=10)
            assert result == "15", f"Expected 15, but got {result}"
            allure.attach(
                browser.get_screenshot_as_png(),
                name="calculator_result",
                attachment_type=allure.attachment_type.PNG
            )