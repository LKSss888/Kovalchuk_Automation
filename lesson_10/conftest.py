import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import allure


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для создания и закрытия браузера
    
    Returns:
        WebDriver: Экземпляр WebDriver
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания отчетов при падении тестов
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            if "browser" in item.funcargs:
                browser = item.funcargs["browser"]
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")