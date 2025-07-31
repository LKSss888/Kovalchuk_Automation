# Открыть браузер FireFox.
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Запуск Firefox с автоматической установкой geckodriver
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

# Перейти на страницу: http://the-internet.herokuapp.com/login.
driver.get("http://the-internet.herokuapp.com/login") 

#найти элемент верстки, записать в переменную для использования
# В поле username
search_field_a = "[name=username]"
search_input_a = driver.find_element(By.CSS_SELECTOR, search_field_a) #сохранили ссылку на элемент в переменную
# В поле password
search_field_b = "[name=password]"
search_input_b = driver.find_element(By.CSS_SELECTOR, search_field_b) #сохранили ссылку на элемент в переменную
# кнопкa Login
search_field_c = ".fa.fa-2x.fa-sign-in"
search_input_c = driver.find_element(By.CSS_SELECTOR, search_field_c) #сохранили ссылку на элемент в переменную

# В поле username ввести значение tomsmith.
search_input_a.send_keys("tomsmith")

# В поле password ввести значение SuperSecretPassword!.
search_input_b.send_keys("SuperSecretPassword!")

# Нажать кнопку Login.
search_input_c.click()

# Вывести текст с зеленой плашки в консоль.
element = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
print(element)

# Закрыть браузер
driver.quit()  