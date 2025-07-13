from Address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address        # Адрес получателя (объект Address)
        self.from_address = from_address    # Адрес отправителя (объект Address)
        self.cost = cost                    # Стоимость (число)
        self.track = track                  # Трек-номер (строка)