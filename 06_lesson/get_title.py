from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

browser.get("https://ya.ru/") #перехода на страницу
current_title = browser.title #сбор названия вкладки и Сохраним результат выполнения метода browser.title в переменную
print(current_title)

browser.quit()

#В результате работы скрипта мы получили в терминале название вкладки