year = int(input("Введите год: "))

def is_year_leap(year):
    print(year)

if (year % 4 == 0):
    print('True')  # Високосный
else:
    print('False')   # Не високосный
result = is_year_leap(year)

print("Год ", year, " = ", {result})  # не получается вывести результаты работы функции. Выводит: Год  2011  =  {None}