from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    """
    Главная страница демонстрационного веб-приложения
    
    Attributes:
        CART_BUTTON: Локатор кнопки корзины
        CART_BADGE: Локатор счетчика корзины
    """
    
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину
        
        Args:
            product_name: Название товара
        """
        # Правильный локатор для кнопки добавления в корзину
        # Используем data-test атрибут, который виден в HTML
        add_button_locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(@data-test, 'add-to-cart')]")
        
        # Ждем, пока кнопка станет кликабельной
        self.wait.until(EC.element_to_be_clickable(add_button_locator))
        
        # Находим и кликаем кнопку
        add_button = self.driver.find_element(*add_button_locator)
        add_button.click()
        
        # Проверяем, что товар добавился (появился счетчик корзины)
        self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        self.take_screenshot(f"added_{product_name.replace(' ', '_')}")

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину покупок"""
        self.click(self.CART_BUTTON)

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Получает количество товаров в корзине
        
        Returns:
            int: Количество товаров в корзине
        """
        try:
            cart_badge = self.find_element(self.CART_BADGE)
            return int(cart_badge.text)
        except:
            return 0