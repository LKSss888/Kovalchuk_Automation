from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# driver.set_window_size(640, 460) #окно браузера уменьшится под параметры
driver.maximize_window #открыть окно по размеру экрана
# driver.minimize_window #свернуть окно браузера
# driver.fullscreen_window #развернуть окно на весь экран, аналог F11

driver.get("https://ya.ru/") #открывается первая страница
# driver.get("https://vk.com/") #открывается вторая страница

# for x in range(1, 10): #цикл повторений
# driver.back()
# driver.forward()

sleep(8)

driver.save_screenshot("./ya.png") #цикл