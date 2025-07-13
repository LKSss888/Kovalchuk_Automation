from Address import Address
from Mailing import Mailing

# Создаем адреса
to_address = Address(656030, 'Saratov', 'Lisina', 11, 8)
from_address = Address(123456, 'Moscow', 'Lenina', 5, 42)

# Создаем почтовое отправление
mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RB123456789RU"
)

# Печатаем информацию
print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")