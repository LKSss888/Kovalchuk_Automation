import pytest
from pages.calculator_page import CalculatorPage

class TestCalculator:
    def test_calculator_with_delay(self, browser):
        calculator_page = CalculatorPage(browser)
        calculator_page.open()
        calculator_page.set_delay(45)
        
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")
        
        result = calculator_page.get_result()
        assert result == "15", f"Expected 15, but got {result}"