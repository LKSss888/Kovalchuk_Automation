# 1) Нажать на кнопку
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

element = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click() #кликаем на кнопку
driver.implicitly_wait(20) #ждем 20 секунд

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text #ищем в элементе текст
print(txt) #выводим текст в консоль

driver.quit()
