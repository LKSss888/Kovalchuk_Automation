from smartphone import Smartphone

# Создаем каталог с 5 разными смартфонами
catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79123456789"),
    Smartphone("Apple", "iPhone 15", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"),
    Smartphone("Honor", "90 Lite", "+79456789012"),
    Smartphone("Google", "Pixel 7", "+79567890123")
]

# Печатаем каталог в заданном формате
for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")