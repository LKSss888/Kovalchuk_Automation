from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def test_calculator():
    # Простая настройка драйвера для Chrome
    # Chrome автоматически найдет драйвер если он в PATH
    driver = webdriver.Chrome()
    
    try:
        print("Открываем страницу калькулятора...")
        # 1. Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        print("Страница загружена")
        time.sleep(2)  # Даем время для полной загрузки
        
        # 2. Ввести значение задержки
        print("Устанавливаем задержку 45 секунд...")
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        print("Задержка установлена")
        
        # 3. Нажать кнопки: 7 + 8 =
        print("Нажимаем кнопки: 7 + 8 =")
        
        # Находим и нажимаем кнопки
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        print("Все кнопки нажаты")
        
        # 4. Проверить результат через 45 секунд
        print("Ожидаем результат 15 секунд...")
        
        # Ждем результат с таймаутом 50 секунд
        wait = WebDriverWait(driver, 50)
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        
        # Проверяем результат
        result = driver.find_element(By.CLASS_NAME, "screen").text
        print(f"Полученный результат: {result}")
        
        assert result == "15", f"Ожидался результат 15, но получено {result}"
        print("✓ Тест пройден успешно! Результат: 15")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # Делаем скриншот для отладки
        driver.save_screenshot("error_calc.png")
        print("Скриншот ошибки сохранен как error_calc.png")
        raise e
        
    finally:
        driver.quit()
        print("Браузер закрыт")

# Запуск теста
if __name__ == "__main__":
    test_calculator()