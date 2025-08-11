from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#все драйверы помещены в единую переменную browser, это вызовет ошибку. 
# Поэтому поменяем переменную browser на конкретные названия браузеров.
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

#Чтобы понимать, какой скриншот в каком браузере был сделан, изменим название для скриншотов с помощью метода browser.name
def make_screenshot(browser):
	browser.maximize_window()
	browser.get("https://ya.ru/")
	sleep(5)
	browser.save_screenshot("./ya_"+browser.name+".png")
	browser.quit()

#Дальше будем вызывать метод make_screenshot(browser) для трех разных браузеров
make_screenshot(chrome)
make_screenshot(ff)
make_screenshot(edge)