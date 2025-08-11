from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

my_cookie = { #переменная с объектом
	'name': 'cookie_policy',
	'value': '1'}

driver.get("https://labirint.ru/") #переход на страницу
driver.add_cookie(my_cookie) #добавление cookie

driver.refresh() #обновление страницы

sleep(10)
driver.quit()