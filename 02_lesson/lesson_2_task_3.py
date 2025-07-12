import math

def kvadrat(s):
    area = s * s
    if not isinstance(s, int):  # Проверяем, является ли s целым числом
        area = math.ceil(area)  # Округляем вверх, если нет
    return area

s = float(input("Длина стороны квадрата: "))  # Используем float, чтобы учесть дробные числа
result = kvadrat(s)
print("Площадь квадрата:", result)