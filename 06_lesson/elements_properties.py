from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

id = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').id # собираем информацию об идентификаторе

print(id) # выводим информацию из переменной в терминал

driver.quit()
------------------------------------------------------------------------------------------------------
## Метод text — используется для сбора текстовой информации, которая содержится в элементе.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

txt = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').text #в переменную с методом text соберется информация об элементе

print(txt) #запрос выведет информацию из переменной в терминал
driver.quit() #закрываем драйвер
------------------------------------------------------------------------------------------------------
## Метод tag_name — позволяет узнать, каким тегом описан элемент на странице.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

tag = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').tag_name #собираем информацию о теге в переменную

print(tag) #выводим информацию из переменной в терминал

driver.quit()
------------------------------------------------------------------------------------------------------
## Метод id — нужен для сбора информации об уникальном для страницы идентификаторе элемента. 
# То есть метод выведет идентификатор элемента, который не повторяется ни у какого другого элемента на странице.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

id = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').id #собираем информацию об идентификаторе

print(id) #выводим информацию из переменной в терминал

driver.quit()

# Браузер генерирует новые id для элементов с каждым новым открытием. 
# Именно поэтому мы не сохраняем элемент в переменную, а обращаемся к нему снова и снова через локатор!
------------------------------------------------------------------------------------------------------
## Метод get_attribute — помогает собрать информацию из атрибута элемента.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))  
driver.get("https://ya.ru")

href = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').get_attribute("href")

print(href)

driver.quit()
------------------------------------------------------------------------------------------------------
## Метод value_of_css_property
# CSS-свойства элементов — это свойства, которые определяют внешний вид и поведение элементов на веб-страницах. 
# К CSS-свойствам относятся цвет текста, размер шрифта, стиль шрифта, отступы, поля, границы, фон, выравнивание текста и многое другое.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

ff = (driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').value_of_css_property("font-family"))
print(ff)

driver.quit()

# Рекомендуем самостоятельно потренироваться в работе с методом value_of_css_property: 
# собрать информацию о цвете элемента ("color"), его высоте ("height"), расстоянии между буквами ("letter-spacing") и так далее.
------------------------------------------------------------------------------------------------------
