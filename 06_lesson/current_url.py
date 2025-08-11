from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

browser.get("https://ya.ru/") 
url = browser.current_url # создаем метод current_url, поместим его в переменную url и 
print(url) # вызовем переменную в терминал

browser.quit()