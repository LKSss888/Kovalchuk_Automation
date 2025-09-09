import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShopping:
    """
    Тестовый класс для проверки процесса покупок
    """

    @allure.title("Проверка итоговой суммы заказа")
    @allure.description("Тест проверяет корректность расчета итоговой суммы при добавлении нескольких товаров в корзину")
    @allure.feature("Корзина покупок")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shopping_cart_total(self, browser) -> None:
        """
        Тест проверки итоговой суммы заказа
        
        Args:
            browser: Фикстура браузера
        """
        
        with allure.step("Логин в систему"):
            login_page = LoginPage(browser)
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Добавление товаров в корзину"):
            main_page = MainPage(browser)
            
            # Добавляем первый товар и проверяем счетчик
            main_page.add_product_to_cart("Sauce Labs Backpack")
            assert main_page.get_cart_items_count() == 1, "Первый товар не добавился в корзину"
            
            # Добавляем второй товар и проверяем счетчик
            main_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
            assert main_page.get_cart_items_count() == 2, "Второй товар не добавился в корзину"
            
            # Добавляем третий товар и проверяем счетчик
            main_page.add_product_to_cart("Sauce Labs Onesie")
            assert main_page.get_cart_items_count() == 3, "Третий товар не добавился в корзину"
        
        with allure.step("Переход в корзину"):
            main_page.go_to_cart()
            
        with allure.step("Проверка количества товаров в корзине"):
            cart_page = CartPage(browser)
            cart_page.verify_cart_items_count(3)
        
        with allure.step("Оформление заказа"):
            cart_page.click_checkout()
        
        with allure.step("Заполнение формы оформления"):
            checkout_page = CheckoutPage(browser)
            checkout_page.fill_checkout_form("John", "Doe", "12345")
        
        with allure.step("Проверка итоговой суммы"):
            total = checkout_page.get_total_amount()
            assert total == "58.29", f"Expected $58.29, but got ${total}"
            allure.attach(
                browser.get_screenshot_as_png(),
                name="final_total_amount",
                attachment_type=allure.attachment_type.PNG
            )