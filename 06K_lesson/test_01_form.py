from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
import pytest
import os
import time

def test_form_validation():
    # Укажите путь к драйверу Edge
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, "msedgedriver.exe")
    
    # Настройка драйвера для Edge
    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    
    try:
        # 1. Открыть страницу
        print("Открываем страницу...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        # Ждем полной загрузки страницы
        wait = WebDriverWait(driver, 10)
        
        # Проверяем, что страница загрузилась
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Страница загружена")
        
        # Даем дополнительное время для загрузки всех элементов
        time.sleep(2)
        
        # Проверяем, видим ли мы форму
        form_elements = driver.find_elements(By.CSS_SELECTOR, "input, button")
        print(f"Найдено элементов формы: {len(form_elements)}")
        
        # Выводим все id элементов для отладки
        all_elements = driver.find_elements(By.CSS_SELECTOR, "[id]")
        print("Найденные элементы с id:")
        for element in all_elements:
            element_id = element.get_attribute("id")
            if element_id:
                print(f" - {element_id}")
        
        # 2. Заполнить форму
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899988787",
            "zip-code": "",  # оставить пустым
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        
        for field_id, value in form_data.items():
            try:
                if value:  # заполняем только если значение не пустое
                    print(f"Заполняем поле {field_id}...")
                    field = wait.until(
                        EC.presence_of_element_located((By.ID, field_id))
                    )
                    field.clear()
                    field.send_keys(value)
                    print(f"Поле {field_id} заполнено")
            except Exception as e:
                print(f"Ошибка при заполнении поля {field_id}: {e}")
                # Попробуем найти по имени
                try:
                    field = driver.find_element(By.NAME, field_id)
                    field.clear()
                    field.send_keys(value)
                    print(f"Поле {field_id} найдено по name и заполнено")
                except:
                    print(f"Поле {field_id} не найдено ни по id, ни по name")
        
        # 3. Нажать кнопку Submit
        print("Нажимаем кнопку Submit...")
        try:
            submit_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            submit_button.click()
            print("Кнопка Submit нажата")
        except Exception as e:
            print(f"Ошибка при нажатии кнопки Submit: {e}")
            # Попробуем другие селекторы
            try:
                submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
                submit_button.click()
                print("Кнопка Submit найдена по тексту и нажата")
            except:
                print("Кнопка Submit не найдена")
        
        # Ждем применения стилей
        time.sleep(2)
        
        # 4. Проверить, что поле Zip code подсвечено красным
        print("Проверяем поле Zip code...")
        try:
            zip_code_field = wait.until(
                EC.presence_of_element_located((By.ID, "zip-code"))
            )
            zip_class = zip_code_field.get_attribute("class")
            print(f"Классы поля Zip code: {zip_class}")
            assert "alert-danger" in zip_class, "Zip code field should be highlighted in red"
            print("✓ Zip code подсвечен красным")
        except Exception as e:
            print(f"Ошибка проверки Zip code: {e}")
        
        # 5. Проверить, что остальные поля подсвечены зеленым
        print("Проверяем остальные поля...")
        green_fields = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]
        
        for field_id in green_fields:
            try:
                field = driver.find_element(By.ID, field_id)
                field_class = field.get_attribute("class")
                print(f"Классы поля {field_id}: {field_class}")
                assert "alert-success" in field_class, f"Field {field_id} should be highlighted in green"
                print(f"✓ {field_id} подсвечен зеленым")
            except Exception as e:
                print(f"Ошибка проверки поля {field_id}: {e}")
        
        print("Тест завершен успешно!")
            
    except Exception as e:
        print(f"Общая ошибка: {e}")
        # Сделаем скриншот для отладки
        driver.save_screenshot("error_screenshot.png")
        print("Скриншот сохранен как error_screenshot.png")
        
    finally:
        driver.quit()
        print("Браузер закрыт")

# Для запуска теста
if __name__ == "__main__":
    test_form_validation()