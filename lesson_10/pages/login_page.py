from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    """
    Страница логина демонстрационного веб-приложения
    
    Attributes:
        USERNAME_INPUT: Локатор поля имени пользователя
        PASSWORD_INPUT: Локатор поля пароля
        LOGIN_BUTTON: Локатор кнопки входа
    """
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Открыть страницу логина")
    def open(self) -> None:
        """
        Открывает страницу логина
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в соответствующее поле
        
        Args:
            username: Имя пользователя для ввода
        """
        self.type_text(self.USERNAME_INPUT, username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в соответствующее поле
        
        Args:
            password: Пароль для ввода
        """
        self.type_text(self.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку входа")
    def click_login_button(self) -> None:
        """Нажимает кнопку входа в систему"""
        self.click(self.LOGIN_BUTTON)

    @allure.step("Выполнить полный процесс логина")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет полный процесс входа в систему
        
        Args:
            username: Имя пользователя
            password: Пароль
        """
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
        # Ждем 3 секунды, чтобы алерт Chrome мог появиться и исчезнуть
        self.wait_seconds(3)
        
        self.take_screenshot("after_login")