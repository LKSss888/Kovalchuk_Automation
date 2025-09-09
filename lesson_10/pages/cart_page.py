from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class CartPage(BasePage):
    """
    Страница корзины покупок
    
    Attributes:
        CHECKOUT_BUTTON: Локатор кнопки оформления заказа
        CART_ITEMS: Локатор элементов корзины
        CART_ITEM_NAMES: Локатор названий товаров в корзине
    """
    
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self) -> None:
        """Нажимает кнопку оформления заказа"""
        # Сначала проверяем, что корзина загрузилась
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEMS))
        self.click(self.CHECKOUT_BUTTON)
        self.take_screenshot("checkout_clicked")

    @allure.step("Проверить количество товаров в корзине: {expected_count}")
    def verify_cart_items_count(self, expected_count: int) -> None:
        """
        Проверяет количество товаров в корзине
        
        Args:
            expected_count: Ожидаемое количество товаров
        """
        # Ждем загрузки корзины
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEMS))
        
        items = self.find_elements(self.CART_ITEMS)
        
        # Для диагностики выведем названия товаров, если они есть
        if items:
            item_names = self.find_elements(self.CART_ITEM_NAMES)
            names_text = ", ".join([item.text for item in item_names])
            print(f"Найдены товары в корзине: {names_text}")
        
        assert len(items) == expected_count, f"Expected {expected_count} items, but found {len(items)}"

    @allure.step("Получить названия товаров в корзине")
    def get_cart_item_names(self) -> list[str]:
        """
        Получает названия всех товаров в корзине
        
        Returns:
            list[str]: Список названий товаров
        """
        item_names = self.find_elements(self.CART_ITEM_NAMES)
        return [item.text for item in item_names]