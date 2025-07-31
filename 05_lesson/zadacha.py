#Задача: вывести информацию по книгам о Python с сайта labirint.ru.
# #Шаги:
# Реализовать скрипт на Python.
# Посчитать количество книг по теме Python на странице labirint.ru.
# Вывести в консоль информацию по каждой книге (название, автор, цена).

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

#зайти на сайт библиотеки
driver.get("https://www.labirint.ru/") #открывается первая страница

#найти элемент верстки, записать в переменную для использования
search_field = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_field) #сохранили ссылку на элемент в переменную

#поиск по запросу "Python"
search_input.send_keys("Python")
search_input.send_keys(Keys.RETURN)

#собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

#вывести в консоль инфо: название + автор + цена
for book in books:
	title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
	price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
	author = " " 
	try:
		author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
	except:
		author = "Автор не указан"
	print(author + "\t" + title + "\t" + price)

sleep(8)