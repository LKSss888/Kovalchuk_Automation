import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestShopping:
    def test_shopping_cart_total(self, browser):
        # Логин
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        # Добавление товаров в корзину
        main_page = MainPage(browser)
        main_page.add_product_to_cart("Sauce Labs Backpack")
        main_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        main_page.add_product_to_cart("Sauce Labs Onesie")
        
        # Переход в корзину и оформление заказа
        main_page.go_to_cart()
        
        cart_page = CartPage(browser)
        cart_page.click_checkout()
        
        # Заполнение формы
        checkout_page = CheckoutPage(browser)
        checkout_page.fill_checkout_form("John", "Doe", "12345")
        
        # Проверка итоговой суммы
        total = checkout_page.get_total_amount()
        assert total == "58.29", f"Expected $58.29, but got ${total}"