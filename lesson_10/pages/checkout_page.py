from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """
    Страница оформления заказа
    
    Attributes:
        FIRST_NAME_INPUT: Локатор поля имени
        LAST_NAME_INPUT: Локатор поля фамилии
        POSTAL_CODE_INPUT: Локатор поля почтового индекса
        CONTINUE_BUTTON: Локатор кнопки продолжения
        TOTAL_AMOUNT: Локатор итоговой суммы
    """
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_AMOUNT = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа
        
        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс
        """
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
        self.take_screenshot("checkout_form_filled")

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа
        
        Returns:
            str: Итоговая сумма
        """
        total_text = self.get_text(self.TOTAL_AMOUNT)
        return total_text.split("$")[1]