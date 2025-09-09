import pytest
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestLabirint:
    """
    Тестовый класс для проверки функциональности сайта Лабиринт
    """

    @pytest.fixture(autouse=True)
    def setup(self, browser) -> None:
        """
        Настройка перед каждым тестом
        
        Args:
            browser: Фикстура браузера
        """
        self.browser = browser
        self.base_page = BasePage(browser)
        self.cookie = {"name": "cookie_policy", "value": "1"}

    @allure.step("Открыть сайт Лабиринт")
    def open_labirint(self) -> None:
        """Открывает сайт Лабиринт и добавляет cookie"""
        self.base_page.open("https://www.labirint.ru/")
        self.browser.maximize_window()
        self.browser.add_cookie(self.cookie)
        self.base_page.take_screenshot("labirint_opened")

    @allure.step("Выполнить поиск по термину: {term}")
    def search(self, term: str) -> None:
        """
        Выполняет поиск на сайте
        
        Args:
            term: Поисковый запрос
        """
        search_field = (By.CSS_SELECTOR, "#search-field")
        search_button = (By.CSS_SELECTOR, "button[type=submit]")
        
        self.base_page.type_text(search_field, term)
        self.base_page.click(search_button)
        self.base_page.take_screenshot(f"search_{term}")

    @allure.step("Добавить книги в корзину")
    def add_books(self) -> int:
        """
        Добавляет книги в корзину
        
        Returns:
            int: Количество добавленных книг
        """
        buy_buttons = self.base_page.find_elements((By.CSS_SELECTOR, "[data-carttext]"))
        
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        
        self.base_page.take_screenshot("books_added")
        return counter

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину"""
        self.base_page.open("https://www.labirint.ru/cart/")

    @allure.step("Получить счетчик корзины")
    def get_cart_counter(self) -> int:
        """
        Получает значение счетчика корзины
        
        Returns:
            int: Количество товаров в корзине
        """
        cart_counter = (By.ID, 'basket-default-prod-count2')
        txt = self.base_page.get_text(cart_counter)
        return int(txt.split()[0])

    @allure.title("Проверка счетчика корзины")
    @allure.description("Тест проверяет корректность работы счетчика товаров в корзине")
    @allure.feature("Корзина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_counter(self) -> None:
        """Тест проверки счетчика корзины"""
        
        with allure.step("Открытие сайта"):
            self.open_labirint()
        
        with allure.step("Поиск книг по слову Python"):
            self.search("Python")
        
        with allure.step("Добавление книг в корзину"):
            added = self.add_books()
        
        with allure.step("Переход в корзину"):
            self.go_to_cart()
        
        with allure.step("Проверка счетчика корзины"):
            cart_counter = self.get_cart_counter()
            assert added == cart_counter, f"Expected {added}, but got {cart_counter}"