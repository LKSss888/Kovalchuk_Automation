from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

#идем на страницу:
driver.get("https://the-internet.herokuapp.com/checkboxes")

#записываем верхнюю html-ветку в переменную div
div = driver.find_element(By.CSS_SELECTOR, "#page-footer")

#через div идем по ветке до элемента с тегом a
a = div.find_element(By.CSS_SELECTOR, "a")

#запрашиваем ссылку из элемента с тегом a
print(a.get_attribute("href"))

driver.quit()