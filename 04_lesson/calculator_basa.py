# модульное тестирование

from calculator import Calculator  # из файла calculator импортируй класс Calculator

calculator = Calculator()

# 5 тестов на сложение:
# ++ |
# -- |
# -+ |
# _,_| не целые числа
# n+0|

print("start")
res = calculator.sum(4, 5)
assert res == 9  # проверь, что сумма 4 и 5 = 9 "ЭТО ОЖИДАЕМЫЙ РЕЗУЛЬТАТ ТЕСТА"

res = calculator.sum(-6, -10)
assert res == -16  # проверь, что сумма -6 и -10 = -16

res = calculator.sum(-6, 6)
assert res == 0  # проверь, что сумма -6 и 6 = 0

res = calculator.sum(5.3, 4.6)
res = round(res, 1)  # округлили сумму полученую в python - в идеале скорректировать док с классом, функция sum
assert res == 9.9

res = calculator.sum(10, 0)
assert res == 10

# тесты для деления:

res = calculator.div(10, 2)
assert res == 5

# тесты для среднего значения:

numbers = []
res = calculator.avg(numbers)
assert res == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
res = calculator.avg(numbers)
print(res)
assert res == 5

print("finish")

#res = calculator.div(10, 0)
#assert res == None