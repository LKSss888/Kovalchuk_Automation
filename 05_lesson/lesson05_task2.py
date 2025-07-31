# Открыть браузер Google Chrome.
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# Перейти на страницу: http://uitestingplayground.com/dynamicid.
driver.get("http://uitestingplayground.com/dynamicid") #открывается первая страница

#найти элемент верстки, записать в переменную для использования
button = ".btn.btn-primary"
button_input = driver.find_element(By.CSS_SELECTOR, button) #сохранили ссылку на элемент в переменную

# Кликнуть на синюю кнопку.
button_input.click()

sleep(8)