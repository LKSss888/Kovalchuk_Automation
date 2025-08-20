from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time

def test_shopping_cart():
    # Настройка драйвера для Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    try:
        print("Открываем сайт магазина...")
        # 1. Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")
        
        wait = WebDriverWait(driver, 10)
        
        # Ждем загрузки страницы авторизации
        wait.until(EC.presence_of_element_located((By.ID, "login-button")))
        print("Страница авторизации загружена")
        
        # 2. Авторизоваться как пользователь standard_user
        print("Авторизуемся...")
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        
        # Проверяем успешную авторизацию
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("Авторизация успешна")
        
        # 3. Добавить товары в корзину
        print("Добавляем товары в корзину...")
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        for product_name in products_to_add:
            try:
                # Находим кнопку "Add to cart" для конкретного товара
                add_button_xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
                add_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, add_button_xpath))
                )
                add_button.click()
                print(f"✓ Добавлен товар: {product_name}")
            except Exception as e:
                print(f"Ошибка при добавлении {product_name}: {e}")
        
        # 4. Перейти в корзину
        print("Переходим в корзину...")
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        
        # Проверяем переход в корзину
        wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        print("Корзина загружена")
        
        # 5. Нажать Checkout
        print("Нажимаем Checkout...")
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        
        # Проверяем переход к оформлению заказа
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        print("Форма оформления заказа загружена")
        
        # 6. Заполнить форму своими данными
        print("Заполняем форму...")
        checkout_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "postal-code": "123456"
        }
        
        for field_id, value in checkout_data.items():
            field = driver.find_element(By.ID, field_id)
            field.clear()
            field.send_keys(value)
            print(f"Заполнено поле {field_id}")
        
        # 7. Нажать кнопку Continue
        print("Нажимаем Continue...")
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
        # Ждем загрузки страницы с итогами
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        print("Страница с итогами загружена")
        
        # 8. Прочитать итоговую стоимость
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")
        print(f"Итоговая стоимость: ${total_amount}")
        
        # 9. Закрыть браузер (будет в finally)
        
        # 10. Проверить итоговую сумму
        assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получено ${total_amount}"
        print("✓ Итоговая сумма верна: $58.29")
        
    except Exception as e:
        print(f"Ошибка в тесте: {e}")
        # Сделаем скриншот для отладки
        driver.save_screenshot("shop_error.png")
        print("Скриншот сохранен как shop_error.png")
        raise e
        
    finally:
        # 9. Закрыть браузер
        driver.quit()
        print("Браузер закрыт")

# Для запуска теста
if __name__ == "__main__":
    test_shopping_cart()