class Card:    # класс Карта
	number = '0000 0000 0000 0000'
	validDate = '01/99'
	holder = 'unknown'

	def __init__(self, number, date, holder):    # конструктор
		self.number = number     # номер карточки
		self.validDate = date     # дата до которой действительна карта
		self.holder = holder       # владелец
		
    def pay(self, amount):    # метод Pay - оплата какой-то суммы
		print("с карты", self.number, "списали", amount)