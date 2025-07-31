# Открыть браузер FireFox.
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Запуск Firefox с автоматической установкой geckodriver
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
driver.get("http://the-internet.herokuapp.com/inputs") 

#найти элемент верстки, записать в переменную для использования
search_field = "[type=number]"
search_input = driver.find_element(By.CSS_SELECTOR, search_field) #сохранили ссылку на элемент в переменную

# Ввести в поле текст Sky.
search_input.send_keys("Sky")

# Очистить это поле (метод clear()).
search_input.clear()

# Ввести в поле текст Pro.
search_input.send_keys("Pro")

# Закрыть браузер
driver.quit()  