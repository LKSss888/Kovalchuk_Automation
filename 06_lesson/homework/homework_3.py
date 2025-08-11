# 3) Дождаться картинки

# Выведите значение в консоль.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождитесь загрузки всех картинок.
driver.implicitly_wait(15) #ждем 50 секунд

jpg_3 = driver.find_element(By.CSS_SELECTOR, "#award") # нашли элемент - 3 картинка.

# Получите значение атрибута # src#  у 3-й картинки.
# Выведите значение в консоль.
print(jpg_3.get_attribute("src"))

driver.quit()
