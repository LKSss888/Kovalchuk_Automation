from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

element = driver.find_element(By.CSS_SELECTOR, "#text")
element.send_keys("test skypro")
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

sleep(10)

driver.quit()

## Используйте другой сайт и элементы для взаимодействия в скрипте. Для осуществления поиска в google.com необходимо нажать кнопку Enter.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com") 

element = driver.find_element(By.NAME, "q") #нашли элемент - строку поиска
element.send_keys("test skypro") #отправляем текст  
element.send_keys(Keys.RETURN) #нажимаем Enter  

sleep(10)

driver.quit()

## Скрипт для имитации нажатия на иконку всех приложений на странице google.com будет выглядеть вот так:

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com") 

driver.find_element(By.CSS_SELECTOR, ".gb_A").click() #нажимаем на иконку все приложения

sleep(10)

driver.quit()