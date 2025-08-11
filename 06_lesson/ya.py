from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep #импортировали метод из пакета

browser = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install())) #можно записать в одну строку

browser.maximize_window() #для разворачивания окна
browser.get("https://ya.ru/") #для перехода на нужную страницу
sleep(5) #для паузы на загрузку контента страницы
browser.save_screenshot("./ya.png") #для сохранения скриншота
browser.quit() #для закрытия окна