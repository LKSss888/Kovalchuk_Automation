from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import allure
import time


class BasePage:
    """
    Базовый класс для всех страниц с Page Object pattern
    
    Attributes:
        driver: Экземпляр WebDriver для управления браузером
        timeout: Таймаут для ожиданий в секундах
    """

    def __init__(self, driver: WebDriver, timeout: int = 15) -> None:
        """
        Инициализация базовой страницы
        
        Args:
            driver: Экземпляр WebDriver
            timeout: Таймаут для ожиданий в секундах (по умолчанию 15)
        """
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Ожидание {seconds} секунд")
    def wait_seconds(self, seconds: int) -> None:
        """
        Ожидает указанное количество секунд
        
        Args:
            seconds: Количество секунд для ожидания
        """
        time.sleep(seconds)

    @allure.step("Открыть URL: {url}")
    def open(self, url: str) -> None:
        """
        Открывает указанный URL в браузере
        
        Args:
            url: URL адрес для открытия
        """
        self.driver.get(url)

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator: tuple) -> WebElement:
        """
        Находит элемент на странице с ожиданием его видимости
        
        Args:
            locator: Кортеж (By, locator) для поиска элемента
            
        Returns:
            WebElement: Найденный элемент
            
        Raises:
            TimeoutException: Если элемент не найден в течение таймаута
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элементы по локатору: {locator}")
    def find_elements(self, locator: tuple) -> list[WebElement]:
        """
        Находит все элементы по локатору
        
        Args:
            locator: Кортеж (By, locator) для поиска элементов
            
        Returns:
            list[WebElement]: Список найденных элементов
        """
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator: tuple) -> None:
        """
        Кликает по указанному элементу
        
        Args:
            locator: Кортеж (By, locator) для поиска элемента
        """
        element = self.find_element(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def type_text(self, locator: tuple, text: str) -> None:
        """
        Вводит текст в поле ввода
        
        Args:
            locator: Кортеж (By, locator) для поиска элемента
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator: tuple) -> str:
        """
        Получает текст элемента
        
        Args:
            locator: Кортеж (By, locator) для поиска элемента
            
        Returns:
            str: Текст элемента
        """
        element = self.find_element(locator)
        return element.text

    @allure.step("Проверить наличие элемента: {locator}")
    def is_element_present(self, locator: tuple) -> bool:
        """
        Проверяет наличие элемента на странице
        
        Args:
            locator: Кортеж (By, locator) для поиска элемента
            
        Returns:
            bool: True если элемент присутствует, False если нет
        """
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    @allure.step("Сделать скриншот: {name}")
    def take_screenshot(self, name: str) -> None:
        """
        Делает скриншот и прикрепляет к Allure отчету
        
        Args:
            name: Название скриншота
        """
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )