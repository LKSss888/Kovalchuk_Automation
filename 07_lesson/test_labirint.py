from selenium import webdriver
from selenium.webdriver.common.by import By

cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome()

def open_labirint():
  browser.get("https://www.labirint.ru/")
  browser.implicitly_wait(4)
  browser.maximize_window()
  browser.add_cookie(cookie)

def search(term):
  browser.find_element(
    By.CSS_SELECTOR, "#search-field").send_keys(term)
  browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def add_books():
  buy_buttons = browser.find_elements(
    By.CSS_SELECTOR, "[data-carttext]")

  counter = 0
  for btn in buy_buttons:
    btn.click()
    counter += 1

  return counter

def go_to_cart():
  # Переходим в корзину
  browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
  # Проверяем счетчик книг. Должен быть равен числу нажатий
  txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
  # Возвращаем число
  return int(txt.split()[0])

def close_driver():
  # Закрываем браузер
  browser.quit()

def test_cart_counter():
  open_labirint()  # Открываем сайт
  search("Python")  # Ищем книги по слову
  added = add_books()  # Добавляем книги и сохраняем результат в переменную
  go_to_cart()  # Идем в корзину
  cart_counter = get_cart_counter()  # Забираем значение счетчика из корзины
  close_driver()  # закрываем браузер

  assert added == cart_counter  # Сравниваем counter со счетчиком корзины