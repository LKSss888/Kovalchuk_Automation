from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

## В этом шаге будет новая информация — тонкости работы с явными ожиданиями.
#Для работы с ними требуется дополнительно импортировать WebDriverWait и expected_conditions:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("http://www.uitestingplayground.com/progressbar")

waiter = WebDriverWait(driver, 40)
#в переменной находится экземпляр с параметрами: 
# 1 параметр - наш драйвер, 2 параметр - 40 секунд на ожидание

waiter.until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#progressBar"), "75%")
)