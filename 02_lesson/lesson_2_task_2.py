year = int(input("Введите год: "))

def is_year_leap(year):
    if (year % 4 == 0):
        return True  # Високосный
    else:
        return False  # Не високосный

result = is_year_leap(year)
print("Год", year, "=", result)